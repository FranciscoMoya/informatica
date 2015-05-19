#ifndef CONSOLE_H
#define CONSOLE_H

void* console_set_raw_mode (int fd);
void console_restore (int fd, void* state);

#endif
