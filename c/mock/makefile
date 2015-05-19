CFLAGS=-std=c11 -Wall -D_POSIX_C_SOURCE -ggdb
BINARIES=test_wiringPi

all: $(BINARIES)

test_wiringPi: test_wiringPi.o wiringPi.o

clean:
	$(RM) *~ *.o $(BINARIES)
