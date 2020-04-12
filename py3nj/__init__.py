# https://github.com/fujiisoup/py3nj/issues/6
import os
import sys
extra_dll_dir = os.path.join(os.path.dirname(__file__), '.libs')

if sys.platform == 'win32' and os.path.isdir(extra_dll_dir):
    os.environ.setdefault('PATH', '')
    os.environ['PATH'] += os.pathsep + extra_dll_dir

from ._version import __version__

from .wigner import wigner3j, wigner6j, wigner9j, clebsch_gordan
from . import wigner
