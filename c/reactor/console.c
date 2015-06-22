#include "console.h"
#include <stdlib.h>
#include <termios.h>

struct termios saved;

void* console_set_raw_mode (int fd)
{
    struct termios* t = malloc(sizeof(struct termios));
    tcgetattr(fd, t);
    struct termios nt = *t;

    nt.c_lflag &= ~(ISIG|ICANON|ECHO);
    nt.c_cc[VMIN] = 1;
    nt.c_cc[VTIME] = 0;

    tcsetattr(fd, TCSANOW, &nt);
    return t;
}

void console_restore (int fd, void* state)
{
    struct termios* t = (struct termios*) state;
    tcsetattr(fd, TCSANOW, t);
    free(t);
}
