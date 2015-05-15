CFLAGS=-std=c11 -Wall -D_POSIX_C_SOURCE -ggdb

all: test_reactor test_composite test_spawn

test_reactor: test_reactor.o reactor.o

test_composite: test_composite.o reactor.o composite_handler.o decimation_handler.o

test_spawn: test_spawn.o reactor.o spawn_handler.o

clean:
	$(RM) *~ *.o
