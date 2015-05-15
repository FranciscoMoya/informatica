#include "keyboard_handler.h"
#include <stdlib.h>
#include <unistd.h>
#include <stdarg.h>
#include <string.h>
#include <wiringPi.h>


static void keyboard_parent_handler(event_handler* ev);
static void keyboard_child_handler(event_handler* ev);

event_handler* keyboard_handler_new (keyboard_handler_function press,
                                     keyboard_handler_function release)
{
    keyboard_handler* h = malloc(sizeof(keyboard_handler));
    keyboard_handler_construct(h, press, release);
    h->ev.destroy = (event_handler_function) free;
    return &h->ev.ev;
}


void keyboard_handler_construct (keyboard_handler* ev,
                                 keyboard_handler_function press,
                                 keyboard_handler_function release)
{
    ev->key_press = press;
    ev->key_release = release;
    ev->num_keys = 0;
    memset(ev->status, 0, sizeof(ev->status));
    spawn_handler_construct(&ev->ev, keyboard_parent_handler, keyboard_child_handler);
}


void keyboard_handler_add_keys (keyboard_handler* ev, int count, ...)
{
    va_list ap;
    va_start (ap, count);
    for (int i = 0; i < count; ++i)
        ev->keys[ev->num_keys++] = va_arg (ap, int);
    va_end (ap);
}


static int keyboard_recv_key(keyboard_handler* h, int* key, int* status);

static void keyboard_parent_handler(event_handler* ev)
{
    keyboard_handler* h = (keyboard_handler*)ev;
    int key, status;

    if (0 > keyboard_recv_key(h, &key, &status)) return;

    if (status)
        h->key_press(h, key & 0xffff);
    else
        h->key_release(h, key & 0xffff);
}


static void keyboard_poll_key(keyboard_handler* h, int key);

static void keyboard_child_handler(event_handler* ev)
{
    keyboard_handler* h = (keyboard_handler*)ev;
    for (int i = 0; i < h->num_keys; ++i)
        keyboard_poll_key(h, i);
}


static void keyboard_send_key(keyboard_handler* h, int key, int status);

static void keyboard_poll_key(keyboard_handler* h, int key)
{
    int status = digitalRead(h->keys[key]);
    if (status != h->status[key]) {
        h->status[key] = status;
        keyboard_send_key(h, key, status);
    }
}

// In order to minimize inter-process traffic we use a single int to
// communicate keys and press/release status. Key code is stored in
// the lower 24 bits while release status is stored in the 24th bit.

static void keyboard_send_key(keyboard_handler* h, int key, int status)
{
    int data = h->keys[key] | (status ? 0 : 0x1000000);
    write(h->ev.out, &data, sizeof(data));
}


static int keyboard_recv_key(keyboard_handler* h, int* key, int* status)
{
    event_handler* ev = &h->ev.ev;
    if (sizeof(*key) != read(ev->fd, key, sizeof(*key)))
        return -1;
    *status = (*key >> 24);
    *key &= 0xffffff;
    return 0;
}
