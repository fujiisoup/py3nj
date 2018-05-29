Examples
========

.. ipython:: python
   :suppress:

    import py3nj

Basic interfaces
----------------

Most basic interface are :py:func:`wigner3j`, :py:func:`wigner6j`, :py:func:`wigner9j`, :py:func:`clebsch_gordan`.

For example, if you want to compute

.. math::

  \begin{pmatrix}
  0&\frac{1}{2}&\frac{1}{2}\\
  0&\frac{1}{2}&-\frac{1}{2}
  \end{pmatrix}.

then pass the doubled value, [0, 1, 1, 0, 1, -1] to :py:func:`wigner3j`.

.. ipython:: python

    py3nj.wigner3j(0, 1, 1,
                   0, 1, -1)

The arguments should be integer or array of integers.

All the functions of py3nj accept array-like as arguments,

.. ipython:: python

    py3nj.wigner3j([0, 1], [1, 2], [1, 1],
                   [0, -1], [1, 2], [-1, -1])

where the output has the same size of the input.
``np.ndarray`` with more than 1 dimension can be also used.

This vectorization not only reduce the python overhead, but also reusing the
result with the same argument.
Therefore, if you need to compute these coefficients for many cases, it is recommended to consider how your calculation can be vectorized.


Advanced interfaces
-------------------

py3nj wraps slatec fortran implementation.
The similar interfaces to the original slatec functions,
:py:func:`wigner.drc3jj` and :py:func:`drc6j` are also supported.

This function computes all the possible values of :math:`J_1` and their
corresponding 3j symbol with given :math:`J_2, J_3, M_2, M_3` values,

.. ipython:: python

    two_l1, three_j = py3nj.wigner.drc3jj(1, 1, 1, 1)
    two_l1
    three_j

This function can be also vectorized,

.. ipython:: python

    two_l1, three_j = py3nj.wigner.drc3jj([1, 0], [1, 2], [1, 0], [1, 2])
    two_l1
    three_j

Note that even in this advanced interfaces, the vectorized version will be much
faster than that sequencial calculation if you need many calcluations.
