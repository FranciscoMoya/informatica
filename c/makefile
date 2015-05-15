CFLAGS=-std=c11 -Wall -D_POSIX_C_SOURCE -ggdb -Ireactor -Imock

.PHONY=subdirs

all: subdirs test_keyboard

test_keyboard: test_keyboard.o keyboard_handler.o \
	reactor/spawn_handler.o reactor/reactor.o \
	mock/wiringPi.o

subdirs:
	$(MAKE) -C reactor
	$(MAKE) -C mock

clean:
	$(RM) *~ *.o
	$(MAKE) -C reactor clean
	$(MAKE) -C mock clean
