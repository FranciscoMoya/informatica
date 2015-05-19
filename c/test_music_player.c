#include "music_player.h"
#include "console.h"
#include <stdio.h>
#include <stdlib.h>
#define __USE_XOPEN_EXTENDED
#include <unistd.h>

static int read_key(int fd);
static void quit_music_player(reactor* r, music_player* mp);

int main(int argc, char* argv[])
{
    void* state = console_set_raw_mode(0);
    reactor* r = reactor_new();
    event_handler* ev = music_player_new(argv[1]);
    music_player* mp = (music_player*) ev;

    void keyboard(event_handler* ev) {
        int key = read_key(ev->fd);
        if ('q' == key)
            quit_music_player(r, mp);
        else if (' ' == key)
            music_player_stop(mp);
        else
            music_player_play(mp, key - '0');
    }

    reactor_add(r, ev);
    reactor_add(r, event_handler_new(0, keyboard));
    reactor_run(r);
    reactor_destroy(r);
    console_restore(0, state);
}


static void quit_music_player(reactor* r, music_player* mp)
{
    music_player_stop(mp);
    usleep(1000);
    reactor_quit(r);
}


static int read_key(int fd)
{
    char buf[2] = " ";
    if (0 < read(fd, buf, 1))
        return buf[0];
    return -1;
}
