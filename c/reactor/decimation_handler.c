#include "decimation_handler.h"
#include <stdlib.h>

static void decimation_handle_events(event_handler* ev)
{
    decimation_handler* h = (decimation_handler*) ev;
    if (0 == --h->remaining) {
        h->remaining = h->skip;
        h->handle(ev);
    }
}


event_handler* decimation_handler_new (int fd, event_handler_function handle, int skip)
{
    decimation_handler* h = malloc(sizeof(decimation_handler));
    decimation_handler_construct(h, fd, handle, skip);
    h->ev.destroy = (event_handler_function) free;
    return &h->ev;
}


void decimation_handler_construct (decimation_handler* ev, int fd, event_handler_function handle, int skip)
{
    event_handler_construct(&ev->ev, fd, decimation_handle_events);
    ev->handle = handle;
    ev->skip = ev->remaining = skip;
}
