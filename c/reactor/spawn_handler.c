#include "spawn_handler.h"
#include <sys/select.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

static void spawn_handler_destroy(event_handler* ev)
{
    spawn_handler* h = (spawn_handler*)ev;

    close(h->out);
    close(h->ev.fd);

    if (h->pid) { // parent
        kill(h->pid, SIGTERM);
        waitpid(h->pid, NULL, 0);
    }

    if (h->destroy)
        h->destroy(ev);
}


event_handler* spawn_handler_new (event_handler_function parent_handle,
                                  event_handler_function child_handle)
{
    spawn_handler* h = malloc(sizeof(spawn_handler));
    spawn_handler_construct(h, parent_handle, child_handle);
    h->destroy = (event_handler_function)free;
    return &h->ev;
}


int spawn_handler_is_child (spawn_handler* ev)
{
    return 0 == ev->pid;
}


void spawn_handler_construct (spawn_handler* h,
                              event_handler_function parent_handle,
                              event_handler_function child_handle)
{
    int parent_to_child[2], child_to_parent[2];

    pipe(parent_to_child); pipe(child_to_parent);
    h->destroy = NULL;
    h->pid = fork();
    if (spawn_handler_is_child(h)) {
        event_handler_construct(&h->ev, parent_to_child[0], child_handle);
        h->out = child_to_parent[1];
        close(parent_to_child[1]); close(child_to_parent[0]);
    }
    else {
        event_handler_construct(&h->ev, child_to_parent[0], parent_handle);
        h->out = parent_to_child[1];
        close(child_to_parent[1]); close(parent_to_child[0]);
    }
    h->ev.destroy = spawn_handler_destroy;
}


void spawn_handler_stay_forever_on_child (spawn_handler* ev)
{
    if (!spawn_handler_is_child(ev))
        return;

    reactor* r = reactor_new();
    reactor_add(r, &ev->ev);
    reactor_run(r);
    reactor_destroy(r);
    exit(0);
}
