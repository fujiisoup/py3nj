import numpy as np
import _wigner


def wigner3j(l1, l2, l3, m1, m2, m3):
    """
    Calculate wigner 3j symbol
    (  L1   L2 L3)
    (-M2-M3 M2 M3)

    Parameters
    ----------
    l1, l2, l3, m1, m2, m3 : 1d-np.ndarray

    Returns
    -------
    threej: 1d-np.ndarray
    """
    pass


def drc3jj(two_l2, two_l3, two_m2, two_m3):
    """
    Calculate wigner 3j symbol
    (  L1   L2 L3)
    (-M2-M3 M2 M3)
    for all the possible L1 values.

    Parameters
    ----------
    l2, l3, m2, m3 : 1d-np.ndarray, shape (m, )

    Returns
    -------
    l1: 1d-np.ndarray, shape (n, )
    threej: 2d-np.ndarray, shape (m, n)
    """
    two_l2 = np.atleast_1d(two_l2)
    two_l3 = np.atleast_1d(two_l3)
    two_m2 = np.atleast_1d(two_m2)
    two_m3 = np.atleast_1d(two_m3)

    if (two_l2 < 0).any() or (two_l3 < 0).any():
        raise ValueError('Some of l values are negative')
    if (two_l2 < np.abs(two_m2)).any() or (two_l3 < np.abs(two_m3)).any():
        raise ValueError('Some of m values are larger than l')

    two_l2, two_l3, two_m2, two_m3 = np.broadcast_arrays(
        two_l2, two_l3, two_m2, two_m3)
    shape = two_l2.shape
    l1max = int(np.max(two_l2 + two_l3)) + 1
    thrcof, ier = _wigner.drc3jj_vec(
        two_l2.ravel(), two_l3.ravel(), two_m2.ravel(), two_m3.ravel(),
        l1max, two_l2.size)
    return np.arange(l1max), thrcof.reshape(shape + (l1max, ))


def _drc3jj(two_l2, two_l3, two_m2, two_m3):
    """ scalar version of drc3jj """
    l1max = (two_l2 + two_l3) / 2
    l1min = max(np.abs(two_l2 - two_l3), np.abs(two_m2 + two_m3)) / 2
    ndim = int(l1max - l1min + 1)

    l1min, l1max, thrcof, ier = _wigner.drc3jj_int(
        two_l2, two_l3, two_m2, two_m3, ndim)
    if ier == 1:
        raise ValueError('Either L2.LT.ABS(M2) or L3.LT.ABS(M3).')
    elif ier == 2:
        raise ValueError('Either L2+ABS(M2) or L3+ABS(M3) non-integer.')
    elif ier == 3:
        raise ValueError('L1MAX-L1MIN not an integer.')
    elif ier == 4:
        raise ValueError('L1MAX less than L1MIN.')
    elif ier == 5:
        raise ValueError('NDIM less than L1MAX-L1MIN+1.')

    return np.arange(l1min, l1min + ndim * 2, 2), thrcof
