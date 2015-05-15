#include "wiringPi.h"
#include <stdio.h>

#define ELEMS(arr) (sizeof(arr)/sizeof(arr[0]))

int digitalRead (int pin)
{
    static int i = 0;
    static int values[] = {
        0, 0, 1, 1, 1, 0, 0, 0, 1, 0
    };

    i %= ELEMS(values);
    printf("digitalRead %d -> %d\n", pin, values[i]);
    return values[i++];
}
