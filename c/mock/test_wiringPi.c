#include "wiringPi.h"
#include <stdio.h>

int main()
{
    for (int i=0; i<10; ++i)
        printf("%d\n", digitalRead(5));
}
