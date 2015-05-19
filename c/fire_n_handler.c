#include "fire_n_handler.h"
#include <stdlib.h>

static void fire_n_handle_events(event_handler* ev)
{
    fire_n_handler* h = (fire_n_handler*) ev;
    if (h->remaining) {
        h->handle(ev);
        --h->remaining;
    }
}


event_handler* fire_n_handler_new (int fd, event_handler_function handler)
{
    fire_n_handler* h = malloc(sizeof(fire_n_handler));
    fire_n_handler_construct(h, fd, handler);
    h->ev.destroy = (event_handler_function) free;
    return &h->ev;
}


void fire_n_handler_construct (fire_n_handler* ev, int fd, event_handler_function handle)
{
    event_handler_construct(&ev->ev, fd, fire_n_handle_events);
    ev->handle = handle;
    ev->remaining = 0;
}


void fire_n_handler_repeat(fire_n_handler* ev, int n)
{
    ev->remaining = n;
}
