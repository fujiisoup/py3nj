# py3nj

![travis](https://travis-ci.org/fujiisoup/py3nj.svg?branch=master)

A small library to calcluate wigner's 3j-, 6j- and 9j- symbols.
This library is designed to be compatible with numpy's np.ndarray and
the calculation is vectorized automatically.

Currently, only 3j-symbols are implemented.

# Usage
```
>>> # Calculate (0/2, 1/2, 1/2,
... #           (0/2, 1/2,-1/2)
... py3nj.wigner3j(0, 1, 1,
...                0, 1,-1)
0.7071067811865476

>>> # vectorization supported
... py3nj.wigner3j([0, 2], [1, 0], [ 1, 0],
...                [0, 0], [1, 0], [-1, 0])
array([0.70710678, 0.        ])
```

# Install

```
python setup.py build
python setup.py install
```
