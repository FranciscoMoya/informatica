#ifndef ACCELEROMETER_H
#define ACCELEROMETER_H

typedef struct {
    int x, y, z;
} acceleration_value;

int accelerometer_setup();
acceleration_value accelerometer_read(int fd);

#endif
