#ifndef LED_HANDLER_H
#define LED_HANDLER_H

// This event handler is designed to be used for a digital output
// driving a led. It is meant to be used as a timeout handler and
// provides functions to control led blinking.

#include "fire_n_handler.h"

typedef struct led_handler_ led_handler;

struct led_handler_ {
    fire_n_handler ev;
    int led;
    int status;
};

event_handler* led_handler_new (int led);
void led_handler_construct (led_handler* ev, int led);
void led_handler_set (led_handler* h, int status);
void led_handler_toggle (led_handler* h);
void led_handler_blink (led_handler* ev, int n);

#endif
