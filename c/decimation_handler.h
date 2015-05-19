#ifndef DECIMATION_HANDLER_H
#define DECIMATION_HANDLER_H

// This event handler is actually only fired on every few firings of
// the handler. It is designed to be used in timeout handlers in
// combination with the composite_handler

#include "reactor.h"

typedef struct decimation_handler_ decimation_handler;

struct decimation_handler_ {
    event_handler ev;
    event_handler_function handle;
    int skip;
    int remaining;
};

event_handler* decimation_handler_new (int fd, event_handler_function handler, int skip);
void decimation_handler_construct (decimation_handler* ev, int fd, event_handler_function handle, int skip);


#endif
