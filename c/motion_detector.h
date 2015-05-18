#ifndef MOTION_DETECTOR_H
#define MOTION_DETECTOR_H

#include "accelerometer.h"

typedef struct {
    acceleration_value a[3];
    int moving;
} motion_detector;

void motion_detector_construct(motion_detector* m);
int motion_detector_input(motion_detector* m, acceleration_value a);

#endif
