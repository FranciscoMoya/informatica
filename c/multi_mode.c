#include "multi_mode.h"
#include <stdlib.h>

multi_mode* multi_mode_new(multi_mode_function reset)
{
    multi_mode* m = malloc(sizeof(multi_mode));
    multi_mode_construct(m, reset);
    m->destroy = (multi_mode_function) free;
    return m;
}


void multi_mode_construct(multi_mode* m, multi_mode_function reset)
{
    m->num_modes = m->mode = m->running = 0;
    m->reset = reset;
    reset(m);
}


void multi_mode_destroy(multi_mode* m)
{
    m->reset(m);
    for (int i = 0; i < m->num_modes; ++i)
        reactor_destroy(m->modes[i]);
}


void multi_mode_add_mode(multi_mode* m, reactor* r)
{
    m->modes[m->num_modes++] = r;
}


void multi_mode_set_mode(multi_mode* m, int mode)
{
    m->reset(m);
    reactor_quit(m->modes[m->mode]);
    m->mode = mode;
}


void multi_mode_next_mode(multi_mode* m)
{
    int mode = m->mode + 1;
    if (mode >= m->num_modes) mode = 0;
    multi_mode_set_mode(m, mode);
}


void multi_mode_prev_mode(multi_mode* m)
{
    int mode = m->mode - 1;
    if (mode < 0) mode = m->num_modes;
    multi_mode_set_mode(m, mode);
}


void multi_mode_quit(multi_mode* m)
{
    m->running = 0;
}


void multi_mode_run(multi_mode* m)
{
    m->running = 1;
    while(m->running && m->num_modes > m->mode)
        reactor_run(m->modes[m->mode]);
}
