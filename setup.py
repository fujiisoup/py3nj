#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy.distutils.core import setup, Extension

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
    extra_compile_args=["-fopenmp"],
)

setup(
    packages=["py3nj"],
    package_dir = {'py3nj': 'src'},
    ext_modules=[ext],
)
