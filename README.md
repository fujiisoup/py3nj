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

`py3nj` can be installed through either `pip` or github repository.  You'll 
likely need to have [ninja](https://ninja-build.org/) installed.

Also, any fortran compiler must be installed in the system. 
An example setup for Windows systems will be found below.

### Install by pip
```
pip install py3nj
```

### Install through github

```
git clone https://github.com/fujiisoup/py3nj
cd py3nj
pip install .
```

### Installing Fortran to Windows

There are several ways to install Fortran. Common ways are
- Install cygwin, or MinGW
- Install WSL (windows subsystem for linux)

Sometimes people have problems with installing Fortran, not only because of the lack of experience, but also due to the security rules from the owners institutes.
In my case, I am not able to install WSL.

The following is one of the example installation configuration, which might not be affected by the security rules.

#### Install [`quickstart-fortran`](https://github.com/LKedward/quickstart-fortran)

[`quickstart-fortran`](https://github.com/LKedward/quickstart-fortran) is an easy Windows installer and launcher for GFortran and the Fortran Package Manager.
This does not require the administrative privilege, and thus it might not be affected many of the security rules.

Go to their [*Release* page](https://github.com/LKedward/quickstart-fortran/releases), download the latest version of the installer, and run it after it is downloaded.

You may need to restart your terminal, such as `Anaconda Prompt`.
Then, do either

```
pip install py3nj
```

or 

```
git clone https://github.com/fujiisoup/py3nj
cd py3nj
pip install .
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
