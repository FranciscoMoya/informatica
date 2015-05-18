#include "ring_buffer.h"

static int wrap_index (int i);


void ring_buffer_construct(ring_buffer* b)
{
    b->head = b->tail = b->n = 0;
}


int ring_buffer_empty(ring_buffer* b)
{
    return b->n == 0;
}


int ring_buffer_full(ring_buffer* b)
{
    return b->n == RING_BUFFER_SIZE;
}


void ring_buffer_push_back(ring_buffer* b, int i)
{
    if (ring_buffer_full(b))
        ring_buffer_pop_front(b);

    b->data[b->tail] = i;
    ++b->n;
    b->tail = wrap_index(b->tail + 1);
}


int ring_buffer_pop_back(ring_buffer* b)
{
    if (ring_buffer_empty(b))
        return 0;

    --b->n;
    b->tail = wrap_index(b->tail - 1);
    return b->data[b->tail];
}


void ring_buffer_push_front(ring_buffer* b, int i)
{
    if (ring_buffer_full(b))
        ring_buffer_pop_back(b);

    b->head = wrap_index(b->head - 1);
    b->data[b->head] = i;
    ++b->n;
}


int ring_buffer_pop_front(ring_buffer* b)
{
    if (ring_buffer_empty(b))
        return 0;

    int i = b->data[b->head];
    --b->n;
    b->head = wrap_index(b->head + 1);
    return i;
}


static int wrap_index (int i)
{
    if (i >= RING_BUFFER_SIZE)
        return i - RING_BUFFER_SIZE;
    if (i < 0)
        return i + RING_BUFFER_SIZE;
    return i;
}
