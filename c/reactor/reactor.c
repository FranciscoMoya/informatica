#include "reactor.h"
#include <string.h>
#include <stdlib.h>
#include <assert.h>

static int max(int a, int b) { return a>b? a: b; }

event_handler* event_handler_new (int fd, event_handler_function handler)
{
    event_handler* ev = malloc(sizeof(event_handler));
    event_handler_construct (ev, fd, handler);
    ev->destroy = (event_handler_function) free;
    return ev;
}

void event_handler_construct (event_handler* ev, int fd, event_handler_function handle)
{
    ev->fd = fd; ev->handle = handle; ev->destroy = NULL;
}

void event_handler_destroy (event_handler* ev)
{
    if (ev->destroy)
        ev->destroy(ev);
}

static void event_handler_run (event_handler* ev)
{
    if (ev->handle)
        ev->handle(ev);
}


static void reactor_destroy_internal (reactor* r);
static void reactor_destroy_and_free (reactor* r);

reactor* reactor_new ()
{
    reactor* r = malloc(sizeof(reactor));
    reactor_construct (r);
    r->destroy = reactor_destroy_and_free;
    return r;
}

void reactor_construct (reactor* r)
{
    r->running = r->paused = 0;
    FD_ZERO(&r->fds);
    r->max_fd = 0;
    r->num_handlers = 0;
    reactor_set_timeout(r, 1000, NULL);
    r->destroy = reactor_destroy_internal;
}

void reactor_destroy (reactor* r)
{
    if (r->destroy)
        r->destroy(r);
}

static void reactor_dispatch_event (reactor* r, fd_set* fds);
static void reactor_dispatch_timeout (reactor* r);
static void reactor_demultiplex_events (reactor* r);

void reactor_run (reactor* r)
{
    r->running = 1;
    while(r->running)
        reactor_demultiplex_events(r);
}

void reactor_add (reactor* r, event_handler* h)
{
    r->handlers[r->num_handlers++] = h;
    r->max_fd = max(r->max_fd, h->fd);
    reactor_enable(r, h->fd);
}

static void reactor_erase_handler_for_fd (reactor* r, int fd);

void reactor_remove (reactor* r, int fd)
{
    reactor_disable(r, fd);
    reactor_erase_handler_for_fd (r, fd);
}

void reactor_enable (reactor* r, int fd)
{
    FD_SET(fd, &r->fds);
}

void reactor_disable (reactor* r, int fd)
{
    FD_CLR(fd, &r->fds);
}

void reactor_set_timeout(reactor* r, int msec, event_handler* h)
{
    r->timeout_handler = h;
    r->timeout.tv_sec = msec / 1000;
    r->timeout.tv_usec = (msec % 1000) * 1000;
    r->tv = r->timeout;
}

void reactor_pause(reactor* r, int do_pause)
{
    r->paused = do_pause;
}

void reactor_quit(reactor* r)
{
    r->running = 0;
}


static void reactor_destroy_internal (reactor* r)
{
    for (int i=0; i<r->num_handlers; ++i)
        event_handler_destroy(r->handlers[i]);
    if (r->timeout_handler)
        event_handler_destroy(r->timeout_handler);
}

static void reactor_destroy_and_free (reactor* r)
{
    reactor_destroy_internal(r);
    free(r);
}

static void reactor_run_handler(reactor* r, int fd);

static void reactor_dispatch_event (reactor* r, fd_set* fds)
{
    for (int fd = 0; fd <= r->max_fd; ++fd)
        if (FD_ISSET (fd, fds))
            reactor_run_handler(r, fd);
}

static void reactor_dispatch_timeout (reactor* r)
{
    if (!r->paused && r->timeout_handler)
        event_handler_run(r->timeout_handler);
    r->tv = r->timeout;
}

static void reactor_demultiplex_events (reactor* r)
{
    fd_set fds_copy = r->fds;
    int ret = select(r->max_fd+1, &fds_copy, 0, 0, &r->tv);
    assert(ret >= 0);

    if (ret > 0) {
        reactor_dispatch_event(r, &fds_copy);
        return;
    }

    reactor_dispatch_timeout(r);
}

static void reactor_run_handler(reactor* r, int fd)
{
    for (int i=0; i<r->num_handlers; ++i)
        if (fd == r->handlers[i]->fd) {
            event_handler_run(r->handlers[i]);
            return;
        }
}


static void erase_handler (event_handler* ev[], int i, int n);

static void reactor_erase_handler_for_fd (reactor* r, int fd)
{
    for (int i=0; i<r->num_handlers; ++i)
        if (fd == r->handlers[i]->fd)
            erase_handler(r->handlers, i, r->num_handlers);
}

static void erase_handler (event_handler* ev[], int i, int n)
{
    event_handler_destroy(ev[i]);
    memmove(ev+i, ev + i + 1, (n - i - 1)*sizeof(ev[0]));
    ev[n-1] = NULL;
}
