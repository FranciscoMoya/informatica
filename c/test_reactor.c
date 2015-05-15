#include "reactor.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void timeout(event_handler* ev)
{
    puts("Timeout");
}

typedef struct {
    event_handler ev;
    reactor* r;
} keyboard_handler;

static void keyboard(event_handler* ev)
{
    keyboard_handler* kb = (keyboard_handler*)ev;

    char buf[2] = " ";
    read(ev->fd, buf, 1);

    if (buf[0] == 'q')
        reactor_quit(kb->r);

    printf("Got %c\n", buf[0]);
}

event_handler* keyboard_handler_new(reactor* r)
{
    keyboard_handler* kb = malloc(sizeof(keyboard_handler));
    event_handler_construct(&kb->ev, 0, keyboard);
    kb->r = r;
    return &kb->ev;
}


int main()
{
    reactor* r = reactor_new();
    event_handler* ev = event_handler_new(-1, timeout);
    event_handler* kb = keyboard_handler_new(r);
    reactor_add(r, kb);
    reactor_set_timeout(r, 1000, ev);
    reactor_run(r);
}
