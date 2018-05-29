#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import re
from numpy.distutils.core import setup, Extension

# load version form _version.py
VERSIONFILE = "py3nj/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# fortran extension
ext = Extension(name='py3nj._wigner',
                sources=['fortran/_wigner.pyf', 'fortran/drc.f90',
                         'fortran/xermsg.f', 'fortran/d1mach.f',
                         'fortran/drc3jj.f',
                         'fortran/drc6j.f'],
                extra_compile_args=['-fopenmp'])

# module
setup(name='py3nj',
      version=verstr,
      author="Keisuke Fujii",
      author_email="fujiisoup@gmail.com",
      description=("numpy compatible wigner 3n-J symbols"),
      license="BSD 3-clause",
      keywords="atomic physics, quantum physics",
      url="http://github.com/fujiisoup/py3nj",
      packages=["py3nj", ],
      package_dir={'py3nj': 'py3nj'},
      py_modules=['py3nj.__init__'],
      ext_modules=[ext],
      classifiers=['License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Scientific/Engineering :: Physics']
      )
