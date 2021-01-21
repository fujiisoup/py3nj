#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import re
from numpy.distutils.core import setup, Extension

import platform
from ctypes.util import find_library

# load version form _version.py
VERSIONFILE = "py3nj/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


# If macOS, use ctypes.util.find_library to determine if OpenMP is available.
openmp = None
if openmp is None and platform.system() == 'Darwin':  # Check if macOS
    if find_library("omp") != None:
        openmp = True
        print("libOMP found, building with OpenMP")
    else:
        print("libOMP not found, building without OpenMP")
elif openmp in (None, True, "True", "true"):
    openmp = True
elif openmp in (False, "False", "false"):
    openmp = False
    print("Building without OpenMP")
else:
    raise ValueError("Env var ompy_OpenMP must be either True or False "
                     "(or not set); use eg. 'export ompy_OpenMP=False'"
                     f"Now it is: {openmp}")

extra_compile_args = ["-O3", "-ffast-math", "-march=native"]
extra_link_args = []
if openmp and platform.system() == 'Darwin':
    extra_compile_args.insert(-1, "-Xpreprocessor -fopenmp")
    extra_link_args.insert(-1, "-lomp")
elif openmp:
    extra_compile_args.insert(-1, "-fopenmp")
    extra_link_args.insert(-1, "-fopenmp")
    
# fortran extension
ext = Extension(
    name="py3nj._wigner",
    sources=[
        "fortran/_wigner.pyf",
        "fortran/drc.f90",
        "fortran/xermsg.f",
        "fortran/d1mach.f",
        "fortran/drc3jj.f",
        "fortran/drc6j.f",
    ],
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

# module
setup(
    name="py3nj",
    version=verstr,
    author="Keisuke Fujii",
    author_email="fujiisoup@gmail.com",
    description=("numpy compatible wigner 3n-J symbols"),
    license="BSD 3-clause",
    keywords="atomic physics, quantum physics",
    url="http://github.com/fujiisoup/py3nj",
    packages=["py3nj"],
    package_dir={"py3nj": "py3nj"},
    py_modules=["py3nj.__init__"],
    ext_modules=[ext],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Physics",
    ],
)
