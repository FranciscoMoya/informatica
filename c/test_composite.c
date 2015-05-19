#include "reactor.h"
#include "composite_handler.h"
#include "decimation_handler.h"
#include <stdio.h>

static void handle1(event_handler* ev) { puts("1"); }
static void handle2(event_handler* ev) { puts("2"); }
static void handle4(event_handler* ev) { puts("4"); }

int main()
{
    reactor* r = reactor_new();
    event_handler* ev = composite_handler_new(-1);

    composite_handler* c = (composite_handler*) ev;
    composite_handler_add(c, event_handler_new(-1, handle1));
    composite_handler_add(c, decimation_handler_new(-1, handle2, 2));
    composite_handler_add(c, decimation_handler_new(-1, handle4, 4));

    reactor_set_timeout(r, 1000, ev);
    reactor_run(r);
}
