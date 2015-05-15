#ifndef FIRE_N_HANDLER_H
#define FIRE_N_HANDLER_H

// This handler is designed to be used as a timeout to limit the
// number of effective firings of the handler to a given ammount.
// It may be used to implement led blinking.

#include "reactor.h"

typedef struct fire_n_handler_ fire_n_handler;

struct fire_n_handler_ {
    event_handler ev;
    event_handler_function handle;
    int remaining;
};

event_handler* fire_n_handler_new (int fd, event_handler_function handler);
void fire_n_handler_construct (fire_n_handler* ev, int fd, event_handler_function handle);
void fire_n_handler_repeat(fire_n_handler* ev, int n);


#endif
