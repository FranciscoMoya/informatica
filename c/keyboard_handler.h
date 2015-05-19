#ifndef KEYBOARD_HANDLER_H
#define KEYBOARD_HANDLER_H

// This event handler is designed to be used for digital input
// scanning. It is implemented as a spawn_handler in order to avoid
// interference with critical tasks (keyboard polling may require
// several I2C transactions).

// The parent side is a regular event handler while the child side is
// meant to be used as a timeout handler. Child side is currently
// hidden from users.

#include "spawn_handler.h"

#define KEYBOARD_HANDLER_MAX_KEYS 64


typedef struct keyboard_handler_ keyboard_handler;

typedef void (*keyboard_handler_function)(keyboard_handler* h, int key);

struct keyboard_handler_ {
    spawn_handler ev;
    keyboard_handler_function key_press;
    keyboard_handler_function key_release;
    int status[KEYBOARD_HANDLER_MAX_KEYS];
    int num_keys;
    int* keys;
};

event_handler* keyboard_handler_new (int* keys, int num_keys,
                                     keyboard_handler_function press,
                                     keyboard_handler_function release);
void keyboard_handler_construct (keyboard_handler* ev,
                                 int* keys, int num_keys,
                                 keyboard_handler_function press,
                                 keyboard_handler_function release);

#endif
