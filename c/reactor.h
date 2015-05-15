#ifndef REACTOR_H
#define REACTOR_H

#include <sys/select.h>
#include <time.h>

typedef struct event_handler_ event_handler;
typedef void (*event_handler_function)(event_handler* ev);

struct event_handler_ {
    int fd;
    event_handler_function handle;
    event_handler_function destroy;
};

event_handler* event_handler_new (int fd, event_handler_function handler);
void event_handler_construct (event_handler* ev, int fd, event_handler_function handler);
void event_handler_destroy (event_handler* ev);

#define REACTOR_MAX_HANDLERS 64

typedef struct reactor_ reactor;
typedef void (*reactor_function)(reactor* ev);

struct reactor_ {
    int running;
    int paused;
    int max_fd;
    fd_set fds;
    int num_handlers;
    event_handler* handlers[REACTOR_MAX_HANDLERS];
    event_handler* timeout_handler;
    struct timeval tv, timeout;
    reactor_function destroy;
};

reactor* reactor_new ();
void reactor_construct (reactor* r);
void reactor_destroy (reactor* r);
void reactor_run (reactor* r);
void reactor_add (reactor* r, event_handler* h);
void reactor_remove (reactor* r, int fd);
void reactor_enable (reactor* r, int fd);
void reactor_disable (reactor* r, int fd);
void reactor_set_timeout(reactor* r, int msecs, event_handler* h);
void reactor_pause(reactor* r, int do_pause);
void reactor_quit(reactor* r);

#endif
