#include "reactor.h"
#include "led_handler.h"
#include <stdio.h>

int main()
{
    reactor* r = reactor_new();
    event_handler* ev = led_handler_new(8);

    led_handler* led = (led_handler*) ev;
    led_handler_blink(led, 3);

    reactor_set_timeout(r, 100, ev);
    reactor_run(r);
}
