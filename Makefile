PYTHON=python

all: _festival.so

_festival.so: _festival.cpp
	CFLAGS="-g -fopenmp" $(PYTHON) setup.py build
	ln -sf build/*/_festival*.so _festival.so

clean:
	$(PYTHON) setup.py clean
	rm -rf build _festival.so *.pyc
