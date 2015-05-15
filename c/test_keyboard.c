#include "reactor.h"
#include "keyboard_handler.h"
#include <stdio.h>

static void press(keyboard_handler* ev, int key) { printf("Press %d\n", key); }
static void release(keyboard_handler* ev, int key) { printf("Release %d\n", key); }

int main()
{
    reactor* r = reactor_new();
    event_handler* ev = keyboard_handler_new(press, release);

    keyboard_handler* kb = (keyboard_handler*) ev;
    if (kb->ev.pid)
        reactor_add(r, ev);
    else {
        keyboard_handler_add_keys(kb, 1, 5);
        reactor_set_timeout(r, 100, ev);
    }
    reactor_run(r);
}
