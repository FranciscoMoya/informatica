#include "acceleration_handler.h"
#include "accelerometer.h"
#include <stdlib.h>

static void acceleration_timeout_handler(event_handler* ev);
static int accelerometer_setup(void);
static int accelerometer_read(int);


event_handler* acceleration_handler_new (acceleration_handler_function handler)
{
    acceleration_handler* h = malloc(sizeof(acceleration_handler));
    acceleration_handler_construct(h, handler);
    h->ev.destroy = (event_handler_function) free;
    return &h->ev;
}


void acceleration_handler_construct (acceleration_handler* h, acceleration_handler_function handler)
{
    event_handler_construct(&h->ev, -1, acceleration_timeout_handler);
    moving_average_construct(&h->ax);
    moving_average_construct(&h->ay);
    moving_average_construct(&h->az);
    motion_detector_construct(&h->motion);
    h->handler = handler;
    h->accel = accelerometer_setup();
}

static void acceleration_timeout_handler(event_handler* ev)
{
    (acceleration_handler*) h = (acceleration_handler*) ev;
    motion_detector_input(&h->motion, filtered_acceleration_read(h));
    h->handler(h);
}


static acceleration_value filtered_acceleration_read(acceleration_handler* h)
{
    acceleration_value a = accelerometer_read(h->accel);
    acceleration_value fa = {
        moving_average_input(&h->ax, a.x),
        moving_average_input(&h->ay, a.y),
        moving_average_input(&h->az, a.z)
    };
    return fa;
}
