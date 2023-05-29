BUILD_DIR := build
CC=g++
CFLAGS=-I.
DEPS = 
OBJ = add.o 

$(BUILD_DIR)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) -c -o $@ $< $(CFLAGS)

$(BUILD_DIR)/add: $(OBJ)
	mkdir -p $(dir $@)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean
clean:
	rm *.o
