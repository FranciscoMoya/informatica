#include "ring_buffer.h"
#include <stdio.h>

int main()
{
    ring_buffer b;
    ring_buffer_construct(&b);

    for (int i=0; i<8; ++i)
        ring_buffer_push_back(&b, i);

    printf("Pop 4 front items: ");
    for (int i=0; i<4; ++i)
        printf("%d ", ring_buffer_pop_front(&b));
    puts("");

    for (int i=0; i<4; ++i)
        ring_buffer_push_back(&b, i);

    printf("Pop 8 back items: ");
    for (int i=0; i<8; ++i)
        printf("%d ", ring_buffer_pop_back(&b));
    puts("");

}
