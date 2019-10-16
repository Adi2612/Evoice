#!/usr/bin/env python
from distutils.core import setup, Extension
from distutils.util import get_platform
import os

festival_include = os.environ.get("FESTIVAL_INCLUDE", '/usr/include/festival')
speech_tools_include = os.environ.get("SPECCH_INCLUDE", '/usr/include/speech_tools')
festival_lib = os.environ.get("FESTIVAL_LIB", '/usr/lib')


libraries = ['Festival', 'estools', 'estbase', 'eststring']


setup(
    name='festiv',
    py_modules=['festival'],
    ext_modules=[
        Extension(
            '_festival',
            ['_festival.cpp'],
            include_dirs=[festival_include, speech_tools_include],
            library_dirs=[festival_lib],
            libraries=libraries
        ),
    ],
    platforms=["*nix"]
)
