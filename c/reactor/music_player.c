#include "music_player.h"
#define __USE_XOPEN_EXTENDED
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <dirent.h>
#include <unistd.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <stdio.h>
#include <signal.h>

#define MUSIC_PLAYER "/usr/bin/mpg123","music_player","--loop","-1"

static void music_player_destroy (music_player* h);

event_handler* music_player_new (char* path)
{
    music_player* h = malloc(sizeof(music_player));
    music_player_construct(h, path);
    h->ev.destroy = (event_handler_function) music_player_destroy;
    return &h->ev.ev;
}

static void music_player_find_songs (music_player* h, char* path);
static void parent_handler (event_handler* ev);
static void child_handler (event_handler* ev);

void music_player_construct (music_player* h, char* path)
{
    h->current = h->num_songs = 0;
    h->player = -1;
    music_player_find_songs(h, path);
    spawn_handler_construct(&h->ev, parent_handler, child_handler);
    spawn_handler_stay_forever_on_child(&h->ev);
}


void music_player_play (music_player* h, int song)
{
    h->current = song;
    write(h->ev.out, &h->current, sizeof(h->current));
}


void music_player_stop (music_player* h)
{
    music_player_play (h, -1);
}


void music_player_next (music_player* h)
{
    int next = h->current + 1;
    if (next >= h->num_songs)
        next -= h->num_songs;

    music_player_play (h, next);
}


void music_player_prev (music_player* h)
{
    int prev = h->current - 1;
    if (prev < 0)
        prev += h->num_songs;

    music_player_play (h, prev);
}


static void music_player_add_song (music_player* h, char* song);

static void music_player_find_songs (music_player* h, char* path)
{
    DIR* d = opendir(path);

    if (! d)
        return;

    for(;;) {
        struct dirent* entry = readdir(d);

        if (!entry) break;

        char song[PATH_MAX];
        sprintf(song, "%s/%s", path, entry->d_name);

        struct stat stbuf;
        stat(song, &stbuf);

        if (!S_ISDIR(stbuf.st_mode))
            music_player_add_song(h, song);
        else if (strcmp(entry->d_name, "..")
                 && strcmp (entry->d_name, "."))
            music_player_find_songs (h, song);
    }

    closedir(d);
}


static void music_player_add_song (music_player* h, char* song)
{
    if (h->num_songs >= MUSIC_PLAYER_MAX_SONGS)
        return;

    h->songs[h->num_songs++] = strdup(song);
}


static void music_player_destroy (music_player* h)
{
    music_player_stop(h);
    for (int i=0; i<h->num_songs; ++i)
        free(h->songs[i]);
    free(h);
}


static void parent_handler (event_handler* ev)
{
    // child side should not say anything
    return;
    abort();
}

static void player_start (music_player* h, const char* song);
static void player_stop (music_player* h);

static void child_handler (event_handler* ev)
{
    int song = 0;
    if (sizeof(song) != read (ev->fd, &song, sizeof(song)))
        return;

    music_player* h = (music_player*)ev;
    player_stop(h);
    if (song >= 0)
        player_start(h, h->songs[song]);
}


static void player_start (music_player* h, const char* song)
{
    h->player = vfork();
    if (!h->player)
        execlp(MUSIC_PLAYER, song, 0);
}


static void player_stop (music_player* h)
{
    if (h->player < 0) return;

    kill(h->player, SIGTERM);
    waitpid(h->player, NULL, 0);
    h->player = -1;
}
