#ifndef ACCELERATION_HANDLER_H
#define ACCELERATION_HANDLER_H

// This event handler is designed to process incoming accelerometer
// data.  New values of acceleration are softened with a moving
// average filter.

#include "moving_average.h"
#include "motion_detector.h"

typedef struct acceleration_handler_ acceleration_handler;
typedef void (*acceleration_handler_function) (acceleration_handler* h);

struct acceleration_handler_ {
    event_handler ev;
    moving_average ax, ay, az;
    motion_detector motion;
    int accel;
    acceleration_handler_function handler;
};

event_handler* acceleration_handler_new (acceleration_handler_function handler);
void acceleration_handler_construct (acceleration_handler* ev, acceleration_handler_function handler);


#endif
