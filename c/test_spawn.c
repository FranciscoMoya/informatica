#include "reactor.h"
#include "spawn_handler.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void parent (event_handler* ev)
{
    spawn_handler* h = (spawn_handler*) ev;

    char buf[128];
    int n = read(ev->fd, buf, sizeof(buf));
    if (n > 0)
        printf("Parent got: %s\n", buf);

    static int calls = 3;
    if (--calls < 0) return;

    write(h->out, "parent", 7);
}

void child (event_handler* ev)
{
    spawn_handler* h = (spawn_handler*) ev;

    char buf[128];
    int n = read(ev->fd, buf, sizeof(buf));
    if (n > 0)
        printf("Child got: %s\n", buf);

    write(h->out, "child", 6);
}



int main()
{
    reactor* r  = reactor_new();
    event_handler* ev = spawn_handler_new(parent, child);

    void quit() { reactor_quit(r); }

    spawn_handler* h = (spawn_handler*) ev;
    spawn_handler_stay_forever_on_child(h);
    reactor_add(r, ev);
    reactor_set_timeout(r, 1000, event_handler_new(-1, quit));
    write(h->out, "main", 5);

    reactor_run(r);
    reactor_destroy(r);
}
