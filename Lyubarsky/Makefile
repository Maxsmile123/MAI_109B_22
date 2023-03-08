CXX       := g++
CXX_FLAGS := -std=c++17 -Wall -fsanitize=address

BIN     := bin
LAB     := ./lab23
SRC     := src
INCLUDE := include
LIB     := lib
TESTS   := tests
LIBRARIES   := -lstdc++ -lm
EXECUTABLE  := main

build: $(LAB)/$(BIN)/$(EXECUTABLE)

run: clean build
	clear
	@echo "Executing..."
	$(LAB)/$(BIN)/$(EXECUTABLE)

$(LAB)/$(BIN)/$(EXECUTABLE): $(LAB)/$(SRC)/*.cpp | $(LAB)/$(BIN)
	@echo "Building..."
	$(CXX) $(CXX_FLAGS) -I $(LAB)/$(INCLUDE) -L $(LAB)/$(LIB) $^ -o $@ $(LIBRARIES)

$(LAB)/$(TESTS)/$(EXECUTABLE): $(LAB)/$(SRC)/*.cpp
	@echo "Building..."
	$(CXX) $(CXX_FLAGS) -I $(LAB)/$(INCLUDE) -L $(LAB)/$(LIB) $^ -o $@ $(LIBRARIES)

$(LAB)/$(BIN):
	mkdir $@

clean:
	@echo "Clearing..."
	-rm $(LAB)/$(BIN)/*

test: clean
	clear
	@echo "Run tests..."
	./$(LAB)/$(TESTS)/$(EXECUTABLE)



