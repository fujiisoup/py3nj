# py3nj

![travis](https://travis-ci.org/fujiisoup/py3nj.svg?branch=master)

A small library to calcluate wigner's 3j-, 6j- and 9j- symbols.
This library is designed to be compatible with numpy's np.ndarray and
the calculation is vectorized automatically.

Currently, 9j-symbols are not yet implemented.

## Basic Usage

Convenient function is `py3nj.wigner3j`, `py3nj.wigner6j`, and `py3nj.clebsch_gordan`.

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
python setup.py build
python setup.py install
```

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
