#ifndef MUSIC_PLAYER_H
#define MUSIC_PLAYER_H

// This is a spawn_handler designed to be used as a music player.

#include "spawn_handler.h"

#define MUSIC_PLAYER_MAX_SONGS 32

typedef struct music_player_ music_player;
struct music_player_ {
    spawn_handler ev;
    int current, num_songs;
    char* songs[MUSIC_PLAYER_MAX_SONGS];
    int player;
};

event_handler* music_player_new (char* path);
void music_player_construct (music_player* ev, char* path);
void music_player_play (music_player* ev, int song);
void music_player_stop (music_player* ev);
void music_player_next (music_player* ev);
void music_player_prev (music_player* ev);


#endif
