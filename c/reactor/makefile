CFLAGS=-std=c11 -Wall -D_POSIX_C_SOURCE -ggdb -Ireactor -Imock
BINARIES= subdirs \
	  test_reactor test_composite test_spawn test_fire_n \
	  test_keyboard test_led test_multi_mode \
	  test_ring_buffer test_music_player

.PHONY=subdirs dist

all: $(BINARIES)

test_reactor: test_reactor.o reactor.o console.o

test_composite: test_composite.o reactor.o composite_handler.o decimation_handler.o

test_fire_n: test_fire_n.o reactor.o fire_n_handler.o

test_spawn: test_spawn.o reactor.o spawn_handler.o

test_keyboard: test_keyboard.o keyboard_handler.o \
	spawn_handler.o reactor.o \
	mock/wiringPi.o

test_led: test_led.o led_handler.o \
	fire_n_handler.o reactor.o \
	mock/wiringPi.o

test_multi_mode: test_multi_mode.o multi_mode.o \
	reactor.o

test_ring_buffer: test_ring_buffer.o ring_buffer.o

test_music_player: test_music_player.o music_player.o \
	spawn_handler.o reactor.o console.o

subdirs:
	$(MAKE) -C mock

dist:
	tar -czvf reactor-`date -I`.tgz `find . -name \*.c -o -name \*.h -o -name makefile`

clean:
	$(RM) *~ *.o $(BINARIES) *.tgz
	$(MAKE) -C mock clean
