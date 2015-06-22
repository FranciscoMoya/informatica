#include "moving_average.h"

static void extract_least_recent(moving_average* m);


void moving_average_construct(moving_average* m)
{
    ring_buffer_construct(&m->buf);
    m->sum = 0;
}


int moving_average_input(moving_average* m, int data)
{
    if (ring_buffer_full(&m->buf))
        extract_least_recent(m);
    m->sum += data;
    ring_buffer_push_back(&m->buf, data);
    return m->sum / m->buf.n;
}


static void extract_least_recent(moving_average* m)
{
    m->sum -= ring_buffer_pop_front(&m->buf);
}
