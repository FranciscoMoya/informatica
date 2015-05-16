#include "reactor.h"
#include "multi_mode.h"
#include <stdio.h>

static void reset (multi_mode* m) { puts("Reset"); }

multi_mode* m = NULL;

static void mode0_timeout (event_handler* ev)
{
    puts("Mode0");
    static int i = 0;
    if (++i % 4 == 0)
        multi_mode_next_mode(m);
}

static void mode1_timeout (event_handler* ev)
{
    puts("Mode1");
    static int i = 0;
    if (++i % 3 == 0)
        multi_mode_next_mode(m);
}

static reactor* setup_mode0()
{
    reactor* r = reactor_new();
    reactor_set_timeout(r, 1000,
                        event_handler_new(-1, mode0_timeout));
    return r;
}

static reactor* setup_mode1()
{
    reactor* r = reactor_new();
    reactor_set_timeout(r, 1000,
                        event_handler_new(-1, mode1_timeout));
    return r;
}

int main()
{
    m = multi_mode_new(reset);
    multi_mode_add_mode(m, setup_mode0());
    multi_mode_add_mode(m, setup_mode1());
    multi_mode_run(m);
}
