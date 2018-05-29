
Wigner symbols for Python
=========================

py3nj is a small library to calculate Wigner symbols, such as wigner's 3j, 6j,
9j symbols, as well as Clebsch Gordan coefficients.

py3nj mostly wraps the original Fortran implementation in slatec,
but it is designed to highly compatible to numpy's nd-array,
i.e. the automatic vectorization is supported.


Installing
----------

py3nj is available on pypi.
To install

```bash
pip install py3nj
```

You may need fortran compiler installed in your environment.


Documentation
-------------

**Examples**

* :doc:`examples`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Examples

   examples

**Help & reference**

* :doc:`whats-new`
* :doc:`api`

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Help & reference

   whats-new
   api

License
-------

py3nj is available under the open source `Apache License`__.

__ http://www.apache.org/licenses/LICENSE-2.0.html
