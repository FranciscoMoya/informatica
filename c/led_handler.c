#include "led_handler.h"
#include <stdlib.h>
#include <wiringPi.h>

event_handler* led_handler_new (int led)
{
    led_handler* h = malloc(sizeof(led_handler));
    event_handler* ev = &h->ev.ev;
    led_handler_construct(h, led);
    ev->destroy = (event_handler_function) free;
    return ev;
}


static void led_handle_events(event_handler* ev);
static void led_set_status(int led, int status);

void led_handler_construct (led_handler* h, int led)
{
    event_handler* ev = &h->ev.ev;
    h->led = led;
    h->status = 0;
    fire_n_handler_construct(&h->ev, -1, led_handle_events);
    led_set_status(h->led, h->status);
}


void led_handler_blink (led_handler* h, int n)
{
    fire_n_handler_repeat(&h->ev, 2*n);
}


static void led_handle_events(event_handler* ev)
{
    led_handler* h = (led_handler*) ev;

    h->status = ! h->status;
    led_set_status(h->led, h->status);
}


static void led_set_status(int led, int status)
{
    digitalWrite(led, status);
}
