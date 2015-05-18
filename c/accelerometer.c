#include "accelerometer.h"

#include <wiringPi.h>

static int accelerometer_setup()
{
    int fd = wiringPiI2CSetup(0x53);
    wiringPiI2CWriteReg8(fd, 0x2D, 8); //Configuramos Registro PowerCTL
    wiringPiI2CWriteReg8(fd, 0x31, 8); //Configuramos Registro Data_Format
    wiringPiI2CWriteReg8(fd, 0x2C, 11); //Configuramos Registro BW_Rate
    return fd;
}


static acceleration_value accelerometer_read(int fd)
{
    acceleration_value a = {
        (short) wiringPiI2CReadReg16(fd, 0x32)),
        (short) wiringPiI2CReadReg16(fd, 0x34)),
        (short) wiringPiI2CReadReg16(fd, 0x36))
    };
}
