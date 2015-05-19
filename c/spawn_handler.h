#ifndef SPAWN_HANDLER_H
#define SPAWN_HANDLER_H

// This event handler is meant to be used for process spawning.
// Constructor returns a different event handler for each process.
// Two pipes are used to interconnect both processes.  Output
// descriptor is filled in a public data member.  Destructor takes
// care of process destruction.
// See test_spawn.c for an example.

#include "reactor.h"

typedef struct spawn_handler_ spawn_handler;

struct spawn_handler_ {
    event_handler ev;
    int pid;
    int out;
    event_handler_function destroy;
};

event_handler* spawn_handler_new (event_handler_function parent_handle,
                                  event_handler_function child_handle);

void spawn_handler_construct (spawn_handler* ev,
                              event_handler_function parent_handle,
                              event_handler_function child_handle);

int spawn_handler_is_child (spawn_handler* ev);

void spawn_handler_stay_forever_on_child (spawn_handler* ev);

#endif
