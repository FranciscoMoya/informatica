#ifndef COMPOSITE_HANDLER_H
#define COMPOSITE_HANDLER_H

// This event handler holds a set of event handlers which are fired on
// every firing of the composite handler. It is mainly designed to be
// used for timeout handlers.

#include "reactor.h"

#define COMPOSITE_HANDLER_MAX_CHILDREN 64

typedef struct composite_handler_ composite_handler;

struct composite_handler_ {
    event_handler ev;
    int num_children;
    event_handler* children[COMPOSITE_HANDLER_MAX_CHILDREN];
    event_handler_function destroy_composite;
};

event_handler* composite_handler_new (int fd);
void composite_handler_construct (composite_handler* ev, int fd);
void composite_handler_add (composite_handler* ev, event_handler* child);

#endif
