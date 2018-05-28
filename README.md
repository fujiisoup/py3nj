# py3nj

![travis](https://travis-ci.org/fujiisoup/py3nj.svg?branch=master)

A small library to calcluate wigner's 3j-, 6j- and 9j- symbols.
This library is designed to be compatible with numpy's np.ndarray and
the calculation is vectorized automatically.

Currently, only 3j-symbols are implemented.

## Usage
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

Copyright 2014-2017, xarray Developers

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
