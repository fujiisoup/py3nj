# py3nj

![travis](https://travis-ci.org/fujiisoup/py3nj.svg?branch=master)

A small python library to calcluate wigner's 3j-, 6j- and 9j- symbols.
`py3nj` is designed to be compatible with numpy's np.ndarray and
its calculation is vectorized automatically.

## Basic Usage

The basic interfaces are `py3nj.wigner3j`, `py3nj.wigner6j`,
`py3nj.wigner9j`, and `py3nj.clebsch_gordan`.

```python
>>> # Calculate (0/2, 1/2, 1/2,
... #           (0/2, 1/2,-1/2)
... # Note that all the arguments should be doubled
... py3nj.wigner3j(0, 1, 1,
...                0, 1,-1)
0.7071067811865476

>>> # vectorization is supported
... py3nj.wigner3j([0, 2], [1, 0], [ 1, 0],
...                [0, 0], [1, 0], [-1, 0])
array([0.70710678, 0.        ])

>>> # 6J symbol
>>> py3nj.wigner6j([2, 1], [1, 2], [1, 1],
...                [1, 2], [2, 1], [0, 0])
array([0.40824829, 0.40824829])

>>> # 9J symbol
>>> py3nj.wigner9j([2, 2], [4, 4], [2, 2],
...                [2, 4], [2, 6], [2, 2],
...                [2, 2], [2, 4], [2, 2])
array([0.05555556, 0.03651484])

>>> Clebsch Gordanh coefficient
>>> py3nj.clebsch_gordan(2, 2, 4,
...                      2, 0, 2)
0.7071067811865475

>>> # Vectorized calcluation of C.G. coef
... py3nj.clebsch_gordan([2, 1], [2, 1], [4, 0],
...                      [2,-1], [0, 1], [2, 0])
array([ 0.70710678, -0.70710678])
```

## Install

```
pip install py3nj
```


### Installing py3nj in macOS

In macOS, even after installing gcc via homebrew, the gcc command is an alias to clang.
Symlinked gcc to `/opt/homebrew/bin/gcc-12` as follows:

```bash
cd /opt/homebrew/bin
ln -s gcc-12 gcc
```

Then `CC=gcc pip3 install py3nj` installs the package without errors. 

See [issue 18](https://github.com/fujiisoup/py3nj/issues/18#issuecomment-1400560818) for the original post.

## Acknowledgement

py3nj wraps [slatec](http://www.netlib.org/slatec/) fortran implementation.
See http://www.netlib.org/slatec/ for the details.

## License

Copyright 2018, py3nj Developers

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
