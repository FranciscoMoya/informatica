#ifndef RING_BUFFER_H
#define RING_BUFFER_H

// Simple ring buffer

#define RING_BUFFER_SIZE 10

typedef struct ring_buffer_ ring_buffer;
struct ring_buffer_ {
    int data[RING_BUFFER_SIZE];
    int head, tail, n;
};


void ring_buffer_construct(ring_buffer* b);
int ring_buffer_empty(ring_buffer* b);
int ring_buffer_full(ring_buffer* b);
void ring_buffer_push_back(ring_buffer* b, int i);
int ring_buffer_pop_back(ring_buffer* b);
void ring_buffer_push_front(ring_buffer* b, int i);
int ring_buffer_pop_front(ring_buffer* b);

#endif
