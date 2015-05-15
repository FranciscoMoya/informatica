#include "composite_handler.h"
#include <stdlib.h>

static void composite_handle_events(event_handler* ev)
{
    composite_handler* h = (composite_handler*)ev;

    for (int i = 0; i < h->num_children; ++i)
        h->children[i]->handle(h->children[i]);
}

static void composite_handler_destroy(event_handler* ev)
{
    composite_handler* h = (composite_handler*)ev;

    for (int i = 0; i < h->num_children; ++i)
        event_handler_destroy(h->children[i]);

    if (h->destroy_composite)
        h->destroy_composite(ev);
}

event_handler* composite_handler_new (int fd)
{
    composite_handler* h = malloc(sizeof(composite_handler));
    composite_handler_construct(h, fd);
    h->destroy_composite = (event_handler_function) free;
    return &h->ev;
}

void composite_handler_construct (composite_handler* h, int fd)
{
    event_handler_construct(&h->ev, 0, composite_handle_events);
    h->ev.destroy = composite_handler_destroy;
    h->num_children = 0;
}

void composite_handler_add (composite_handler* h, event_handler* child)
{
    h->children[h->num_children++] = child;
    child->fd = h->ev.fd;
}
