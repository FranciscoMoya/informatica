#include "reactor.h"
#include "keyboard_handler.h"
#include <stdio.h>

static void press(keyboard_handler* ev, int key) { printf("Press %d\n", key); }
static void release(keyboard_handler* ev, int key) { printf("Release %d\n", key); }

int main()
{
    reactor* r = reactor_new();
    int keys[] = { 5 };
    event_handler* ev = keyboard_handler_new(keys, 1, press, release);

    reactor_add(r, ev);
    reactor_run(r);
}
