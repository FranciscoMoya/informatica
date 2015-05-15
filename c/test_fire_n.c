#include "reactor.h"
#include "fire_n_handler.h"
#include <stdio.h>

static void handle(event_handler* ev) { puts("1"); }

int main()
{
    reactor* r = reactor_new();
    event_handler* ev = fire_n_handler_new(-1, handle);
    fire_n_handler_repeat((fire_n_handler*)ev, 3);
    reactor_set_timeout(r, 1000, ev);
    reactor_run(r);
}
