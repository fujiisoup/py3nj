# https://github.com/fujiisoup/py3nj/issues/6
import os
import sys

extra_dll_dir = os.path.join(os.path.dirname(__file__), ".libs")

if sys.platform == "win32" and os.path.isdir(extra_dll_dir):
    os.environ.setdefault("PATH", "")
    os.environ["PATH"] += os.pathsep + extra_dll_dir
    os.add_dll_directory(extra_dll_dir)

# TODO: This is an ugly workaround to add dll for fortran compilers, if this is in user space
# The fortran compiler can be different from gfortran, or can be different from what was used when py3nj is installed 
if sys.platform == "win32":
    import subprocess
    result = subprocess.check_output(['where', 'gfortran'], stdout=subprocess.PIPE)
    path = os.path.dirname(result.stdout.decode('utf-8'))
    os.add_dll_directory(path)

from ._version import __version__

from .wigner import wigner3j, wigner6j, wigner9j, clebsch_gordan
from . import wigner
