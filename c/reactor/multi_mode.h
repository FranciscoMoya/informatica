#ifndef MULTI_MODE_H
#define MULTI_MODE_H

// This is just a composite reactor with functions to switch among the
// internal reactors.

#include "reactor.h"

#define MULTI_MODE_MAX_MODES 10

typedef struct multi_mode_ multi_mode;
typedef void (*multi_mode_function) (multi_mode*);

struct multi_mode_ {
    int num_modes;
    reactor* modes[MULTI_MODE_MAX_MODES];
    int mode;
    int running;
    multi_mode_function reset;
    multi_mode_function destroy;
};

multi_mode* multi_mode_new(multi_mode_function reset);
void multi_mode_construct(multi_mode* m, multi_mode_function reset);
void multi_mode_destroy(multi_mode* m);
void multi_mode_add_mode(multi_mode* m, reactor* r);
void multi_mode_set_mode(multi_mode* m, int mode);
void multi_mode_next_mode(multi_mode* m);
void multi_mode_prev_mode(multi_mode* m);
void multi_mode_quit(multi_mode* m);
void multi_mode_run(multi_mode* m);

#endif
