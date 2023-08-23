project(
  'py3nj', 'c', 'fortran',
  version: run_command('utils/version.py', check: true).stdout().strip(),
  meson_version: '>=0.64.0',
  default_options : ['warning_level=2'],
)

py_mod = import('python')
py = py_mod.find_installation(pure: false)

incdir_numpy = run_command(
  py,
  ['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get_include())'],
  check : true,
).stdout().strip()

incdir_f2py = run_command(
  py,
  ['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get_include())'],
  check : true,
).stdout().strip()

wigner_source = custom_target(
  input : ['fortran/_wigner.pyf'],
  output : ['_wignermodule.c', '_wigner-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@'],
)

py.extension_module(
  '_wigner',
  wigner_source,
  'fortran/drc.f90',
  'fortran/xermsg.f',
  'fortran/d1mach.f',
  'fortran/drc3jj.f',
  'fortran/drc6j.f',
  incdir_f2py / 'fortranobject.c',
  include_directories: include_directories(incdir_numpy, incdir_f2py),
  dependencies : dependency('openmp'),
  install : true,
  subdir: 'py3nj',
)

py.install_sources(
  'src/__init__.py',
  'src/_version.py',
  'src/wigner.py',
  pure: false,
  subdir: 'py3nj',
)
