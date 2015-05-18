#ifndef MOVING_AVERAGE_H
#define MOVING_AVERAGE_H

// Filter implementing moving average

#include "ring_buffer.h"

typedef struct moving_average_ moving_average;
struct moving_average_ {
    ring_buffer buf;
    long sum;
};

void moving_average_construct(moving_average* m);
int moving_average_input(moving_average* m, int data);

#endif
