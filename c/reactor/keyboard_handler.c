#include "keyboard_handler.h"
#include <stdlib.h>
#include <unistd.h>
#include <stdarg.h>
#include <string.h>
#include <wiringPi.h>

#define KEYBOARD_POLL_PERIOD_MSEC 50

static void keyboard_parent_handler(event_handler* ev);
static void keyboard_child_handler(event_handler* ev);

event_handler* keyboard_handler_new (int* keys, int num_keys,
                                     keyboard_handler_function press,
                                     keyboard_handler_function release)
{
    keyboard_handler* h = malloc(sizeof(keyboard_handler));
    keyboard_handler_construct(h, keys, num_keys, press, release);
    h->ev.destroy = (event_handler_function) free;
    return &h->ev.ev;
}


static void keyboard_handler_stay_forever_on_child(keyboard_handler* h);

void keyboard_handler_construct (keyboard_handler* ev,
                                 int* keys, int num_keys,
                                 keyboard_handler_function press,
                                 keyboard_handler_function release)
{
    ev->key_press = press;
    ev->key_release = release;
    ev->keys = keys;
    ev->num_keys = num_keys;
    memset(ev->status, 0, sizeof(ev->status));
    spawn_handler_construct(&ev->ev, keyboard_parent_handler, keyboard_child_handler);
    if (spawn_handler_is_child(&ev->ev))
        keyboard_handler_stay_forever_on_child(ev);
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


static void keyboard_handler_stay_forever_on_child(keyboard_handler* h)
{
    reactor* r = reactor_new();
    reactor_set_timeout(r, KEYBOARD_POLL_PERIOD_MSEC, &h->ev.ev);
    reactor_run(r);
    reactor_destroy(r);
    exit(0);
}
