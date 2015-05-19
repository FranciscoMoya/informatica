CFLAGS=-std=c11 -Wall -D_POSIX_C_SOURCE -ggdb
BINARIES=test_reactor test_composite test_spawn test_fire_n

all: $(BINARIES)

test_reactor: test_reactor.o reactor.o console.o

test_composite: test_composite.o reactor.o composite_handler.o decimation_handler.o

test_fire_n: test_fire_n.o reactor.o fire_n_handler.o

test_spawn: test_spawn.o reactor.o spawn_handler.o

clean:
	$(RM) *~ *.o $(BINARIES)
