#include "accelerometer.h"

#include <wiringPi.h>

enum {
    POWER_CTL = 0x2d,
    DATA_FORMAT = 0x31,
    BW_RATE = 0x2c,
    DATAX = 0x32,
    DATAY = 0x34,
    DATAZ = 0x36
};

enum {
    POWER_CTL__Link = 0x20,
    POWER_CTL__AUTO_SLEEP = 0x10,
    POWER_CTL__Measure = 0x8,
    POWER_CTL__Sleep = 0x4,
    POWER_CTL__Wakeup = 0x3,
    POWER_CTL__Wakeup_8Hz = 0x0,
    POWER_CTL__Wakeup_4Hz = 0x1,
    POWER_CTL__Wakeup_2Hz = 0x2,
    POWER_CTL__Wakeup_1Hz = 0x3,
};

enum {
    DATA_FORMAT__SELF_TEST = 0x80,
    DATA_FORMAT__SPI = 0x40,
    DATA_FORMAT__INT_INVERT = 0x20,
    DATA_FORMAT__FULL_RES = 0x8,
    DATA_FORMAT__Justify = 0x4,
    DATA_FORMAT__Range = 0x3,
    DATA_FORMAT__Range_2g = 0x0,
    DATA_FORMAT__Range_4g = 0x1,
    DATA_FORMAT__Range_8g = 0x2,
    DATA_FORMAT__Range_16g = 0x3,
};

enum {
    BW_RATE__LOW_POWER = 0x10,
    BW_RATE__Rate = 0xf,
    BW_RATE__Rate_3200 = 0xf,
    BW_RATE__Rate_1600 = 0xe,
    BW_RATE__Rate_800 = 0xd,
    BW_RATE__Rate_400 = 0xc,
    BW_RATE__Rate_200 = 0xb,
    BW_RATE__Rate_100 = 0xa,
    BW_RATE__Rate_50 = 0x9,
    BW_RATE__Rate_25 = 0x8,
    BW_RATE__Rate_12_5 = 0x7,
    BW_RATE__Rate_6_25 = 0x6,
};


int accelerometer_setup()
{
    int fd = wiringPiI2CSetup(0x53);
    wiringPiI2CWriteReg8(fd, POWER_CTL, POWER_CTL__Measure);
    wiringPiI2CWriteReg8(fd, DATA_FORMAT, DATA_FORMAT__FULL_RES);
    wiringPiI2CWriteReg8(fd, BW_Rate, BW_RATE__Rate_200);
    return fd;
}


acceleration_value accelerometer_read(int fd)
{
    acceleration_value a = {
        (short) wiringPiI2CReadReg16(fd, DATAX)),
        (short) wiringPiI2CReadReg16(fd, DATAY)),
        (short) wiringPiI2CReadReg16(fd, DATAZ))
    };
}
