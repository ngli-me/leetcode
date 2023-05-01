CC=g++
CFLAGS=-I.
DEPS = 
OBJ = add.o add.o 

%.o: %.c # $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

addmake: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
