#include "motion_detector.h"
#include <string.h>
#include <stdlib.h>

#define NELEMS(x) (sizeof(x)/sizeof(x[0]))

static int detect_motion(motion_detector* m);

void motion_detector_construct(motion_detector* m)
{
    m->moving = 0;
    memset(m->a, 0, sizeof(m->a));
}


int motion_detector_input(motion_detector* m, acceleration_value a)
{
    memmove(m->a, m->a+1, sizeof(m->a) - sizeof(m->a[0]));
    m->a[NELEMS(m->a)-1] = a;
    m->moving = detect_motion(m);
}


static int detect_motion_start(motion_detector* m);
static int detect_motion_stop(motion_detector* m);

static int detect_motion(motion_detector* m)
{
    if (!m->moving)
        return detect_motion_start(m);

    return detect_motion_stop(m);
}


// OJO! Mantengo la misma condición de arranque, pero no se si es
// correcta. No se trata de detectar cambios en la aceleración sino de
// ver si hay aceleración descontando la gravedad.

#define START(axis) abs(a[2].axis - a[1].axis) > START_THRESHOLD

static int detect_motion_start(motion_detector* m)
{
    acceleration_value* a = m->a;
    if (START(x) || START(y) || START(z))
        m->motion = 1;
    return m->motion;
}


// OJO! Mantengo la misma condición de paro, pero no se si es
// correcta. No se trata de detectar cambios en la aceleración sino de
// ver si hay aceleración descontando la gravedad.

#define STOP(axis) \
    ( abs(a[2].axis - a[1].axis) < STOP_THRESHOLD \
    && abs(a[1].axis - a[0].axis) < STOP_THRESHOLD )

static int detect_motion_stop(motion_detector* m)
{
    acceleration_value* a = m->a;
    if (STOP(x) && STOP(y) && STOP(z))
        m->motion = 0;
    return m->motion;
}
