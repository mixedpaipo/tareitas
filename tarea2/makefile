CC = gcc
CFLAGS = -Wall -Werror
TARGET = TreasureFinder

SRCS = Bomba.c Tablero.c TreasureFinder.c
OBJS = $(SRCS:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

run: $(TARGET)
	valgrind ./$(TARGET)

clean:
	rm -f $(OBJS) $(TARGET)

