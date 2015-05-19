CFLAGS=-std=c11 -Wall -D_POSIX_C_SOURCE -ggdb -Ireactor -Imock
BINARIES= subdirs test_keyboard test_led test_multi_mode \
	  test_ring_buffer test_music_player
.PHONY=subdirs

all: $(BINARIES)

test_keyboard: test_keyboard.o keyboard_handler.o \
	reactor/spawn_handler.o reactor/reactor.o \
	mock/wiringPi.o

test_led: test_led.o led_handler.o \
	reactor/fire_n_handler.o reactor/reactor.o \
	mock/wiringPi.o

test_multi_mode: test_multi_mode.o multi_mode.o \
	reactor/reactor.o

test_ring_buffer: test_ring_buffer.o ring_buffer.o

test_music_player: test_music_player.o music_player.o \
	reactor/spawn_handler.o reactor/reactor.o reactor/console.o

subdirs:
	$(MAKE) -C reactor
	$(MAKE) -C mock

clean:
	$(RM) *~ *.o $(BINARIES)
	$(MAKE) -C reactor clean
	$(MAKE) -C mock clean
