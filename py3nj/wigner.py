import numpy as np
from py3nj import _wigner


def int_broadcast(*args):
    args = np.broadcast_arrays(*args)
    if any(a.dtype.kind not in 'iu' for a in args):
        raise ValueError('Argument should be integer.')
    return args


def clebsch_gordan(two_j1, two_j2, two_j3, two_m1, two_m2, two_m3):
    """ Calulate Clebsch-Gordan coefficient
    <j1 m1, j2 m2 | j3 m3>
    """
    two_j1, two_j2, two_j3, two_m1, two_m2, two_m3 = int_broadcast(
        two_j1, two_j2, two_j3, two_m1, two_m2, two_m3)

    phase = (two_j1 - two_j2 + two_m3) % 4 - 1
    return -phase * np.sqrt(two_j3 + 1) * wigner3j(two_j1, two_j2, two_j3,
                                                  two_m1, two_m2, -two_m3)


def wigner3j(two_l1, two_l2, two_l3, two_m1, two_m2, two_m3):
    """
    Calculate wigner 3j symbol
    (  L1   L2 L3)
    (-M2-M3 M2 M3)

    Parameters
    ----------
    two_l1: array of integers
    two_l2: array of integers
    two_l3: array of integers
    two_m1: array of integers
    two_m2: array of integers
    two_m3: array of integers
        Since L1, ..., M3 should be integers or half integers, two_l1 (which
        means 2 x L1) should be all integers.

    Returns
    -------
    threej: array
        The value of 3J symbol with the same shape of the arguments.
    """
    two_l1, two_l2, two_l3, two_m1, two_m2, two_m3 = int_broadcast(
        two_l1, two_l2, two_l3, two_m1, two_m2, two_m3)

    if (two_l1 < 0).any():
        raise ValueError('Some of l values are negative')

    l, thrcof = drc3jj(two_l2, two_l3, two_m2, two_m3)

    l1max = thrcof.shape[-1]
    shape = thrcof.shape[:-1]

    two_l1 = two_l1.ravel()
    valid = (two_l1 < l1max) * ((two_m1 + two_m2 + two_m3).ravel() == 0)

    if shape == ():  # scale case
        return np.where(valid, thrcof[two_l1], 0.0)[0]
    thrcof = np.where(valid, thrcof[np.arange(len(two_l1)), two_l1], 0.0)
    return thrcof.reshape(shape)


def wigner6j(two_l1, two_l2, two_l3, two_l4, two_l5, two_l6):
    """
    Calculate wigner 6j symbol
    (L1 L2 L3)
    (L4 L5 L6)

    Parameters
    ----------
    two_l1: array of integers
    two_l2: array of integers
    two_l3: array of integers
    two_l4: array of integers
    two_l5: array of integers
    two_l6: array of integers
        Since L1, ..., L6 should be integers or half integers, two_l1 (which
        means 2 x L1) should be all integers.

    Returns
    -------
    threej: array
        The value of 6J symbol with the same shape of the arguments.
    """
    two_l1, two_l2, two_l3, two_l4, two_l5, two_l6 = int_broadcast(
        two_l1, two_l2, two_l3, two_l4, two_l5, two_l6)

    if (two_l1 < 0).any():
        raise ValueError('Some of l values are negative')

    l, sixcof = drc6j(two_l2, two_l3, two_l4, two_l5, two_l6)

    l1max = sixcof.shape[-1]
    shape = sixcof.shape[:-1]

    two_l1 = two_l1.ravel()
    valid = two_l1 < l1max

    if shape == ():  # scale case
        return np.where(valid, sixcof[two_l1], 0.0)[0]
    sixcof = np.where(valid, sixcof[np.arange(len(two_l1)), two_l1], 0.0)
    return sixcof.reshape(shape)


def drc3jj(two_l2, two_l3, two_m2, two_m3):
    """
    Calculate Wigner's 3j symbol
    (  L1   L2 L3)
    (-M2-M3 M2 M3)
    for all the possible L1 values.

    Parameters
    ----------
    two_l2: array of integers, size (...)
    two_l3: array of integers, size (...)
    two_m2: array of integers, size (...)
    two_m3: array of integers, size (...)
        Since L2, ..., M3 should be integers or half integers, two_l1 (which
        means 2 x L1) should be all integers.

    Returns
    -------
    two_l1: 1d-np.ndarray of integer, shape (n, )
        The possible L1 values.
    threej: array, shape (..., n)
        The value of 3J symbol
    """
    two_l2, two_l3, two_m2, two_m3 = int_broadcast(
        two_l2, two_l3, two_m2, two_m3)

    if (two_l2 < 0).any() or (two_l3 < 0).any():
        raise ValueError('Some of l values are negative.')
    if (two_l2 < np.abs(two_m2)).any() or (two_l3 < np.abs(two_m3)).any():
        raise ValueError('Some of m values are larger than l.')

    shape = two_l2.shape
    l1max = int(np.max(two_l2 + two_l3) + 1)

    thrcof, ier = _wigner.drc3jj_vec(
        two_l2=two_l2.ravel(), two_l3=two_l3.ravel(),
        two_m2=two_m2.ravel(), two_m3=two_m3.ravel(),
        nvec=two_l2.size, ndim=l1max)
    return np.arange(l1max), thrcof.reshape(shape + (l1max, ))


def _drc3jj(two_l2, two_l3, two_m2, two_m3):
    """ scalar version of drc3jj """
    l1max = (two_l2 + two_l3)
    l1min = max(np.abs(two_l2 - two_l3), np.abs(two_m2 + two_m3))
    ndim = int((l1max - l1min + 2) / 2)

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


def drc6j(two_l2, two_l3, two_l4, two_l5, two_l6):
    """
    Calculate Wigner's 6j symbol
    (L1 L2 L3)
    (L4 L5 L6)
    for all the possible L1 values.

    Parameters
    ----------
    two_l2: array of integers, size (...)
    two_l3: array of integers, size (...)
    two_l4: array of integers, size (...)
    two_l5: array of integers, size (...)
    two_l6: array of integers, size (...)
        Since L2, ..., L6 should be integers or half integers, two_l2, ...
        (whichs 2 x L1) should be all integers.

    Returns
    -------
    two l1: 1d-np.ndarray of integer, shape (n, )
        The possible L1 values.
    threej: array, shape (..., n)
        The value of 3J symbol
    """
    two_l2, two_l3, two_l4, two_l5, two_l6 = int_broadcast(
        two_l2, two_l3, two_l4, two_l5, two_l6)

    if ((two_l2 < 0).any() or (two_l3 < 0).any() or (two_l4 < 0).any() or
            (two_l4 < 0).any() or (two_l5 < 0).any()):
        raise ValueError('Some of l values are negative')

    shape = two_l2.shape
    l1max = int(np.max(two_l2 + two_l3) + 1)

    sixcof, ier = _wigner.drc6j_vec(
        two_l2=two_l2.ravel(), two_l3=two_l3.ravel(),
        two_l4=two_l4.ravel(), two_l5=two_l5.ravel(),
        two_l6=two_l6.ravel(),
        nvec=two_l2.size, ndim=l1max)
    return np.arange(l1max), sixcof.reshape(shape + (l1max, ))


def _drc6j(two_l2, two_l3, two_l4, two_l5, two_l6):
    """ scalar version of drc6j """
    two_l1min = max(abs(two_l2 - two_l3), abs(two_l5 - two_l6))
    two_l1max = min(two_l2 + two_l3, two_l5 + two_l6)
    ndim = int((two_l1max - two_l1min) / 2 + 1)

    l1min, l1max, sixcof, ier = _wigner.drc6j_int(
        two_l2, two_l3, two_l4, two_l5, two_l6, ndim)

    if ier == 1:
        raise ValueError('L2+L3+L5+L6 and L2+L4+L6 must be integers')
    elif ier == 2:
        raise ValueError('ABS(L2-L4).LE.L6.LE.L2+L4 must be satisfied.')
    elif ier == 3:
        raise ValueError('ABS(L4-L5).LE.L3.LE.L4+L5 must be satisfied.')
    elif ier == 4:
        raise ValueError('L1MAX-L1MIN must be a non-negative integer, '
                         'where L1MAX=MIN(L2+L3,L5+L6) and'  'L1MIN=MAX(ABS(L2-L3),ABS(L5-L6)).')

    return np.arange(l1min, l1min + ndim * 2, 2), sixcof
