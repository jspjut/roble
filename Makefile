# Defaults, change your environment if you want them different.

CXX ?= g++
CXXFLAGS ?= -ggdb -Wall -03

# will need to add conditionals for opengl stuff to CXXFLAGS

LDFLAGS ?=

mkdirs=objs

all: mkdirs roble
default: mkdirs roble

mkdirs:
	@mkdir -p objs;

objs/%.o: src/%.cc
	@echo "Building $<"
	@$(CXX) $(CXXFLAGS) -o $@ -c $< -MD

SOURCES := $(wildcard src/*.cc)
OBJS := $(addprefix objs/, $(notdir $(SOURCES:.cc=.o)))

# Include dependency files
-include $(patsubst %.o,%.d,$(OBJS))

roble: $(OBJS)
	@echo "Building roble"
	@$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $(OBJS)

clean:
	rm -rf objs/ roble
