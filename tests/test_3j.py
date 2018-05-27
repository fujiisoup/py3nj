import numpy as np
import pytest
from py3nj import wigner


rng = np.random.RandomState(0)
# precalculated 3j symbols. Input, result
THREE_J = (
    ((1, 1, 0, 0, 0, 0), -np.sqrt(1/3)),
    ((0, 1, 1, 0, 0, 0), -np.sqrt(1/3)),
    ((2, 1, 1, 0, 0, 0), np.sqrt(2/15)),
    ((0, 1, 1, 0,-1, 1), np.sqrt(1/3)),
)


def test_drc3jj():
    for three_j, result in THREE_J:
        three_j = np.array(three_j) * 2
        l, thrcof = wigner._drc3jj(three_j[1], three_j[2], three_j[4],
                                   three_j[5])
        assert np.allclose(thrcof[l == three_j[0]], result)


def test_invalid():
    with pytest.raises(ValueError):
        l, thrcof = wigner._drc3jj(1, 3, 0, 0)

    with pytest.raises(ValueError):
        l, thrcof = wigner._drc3jj(1, 3, 4, 0)


def test_drc3jj_vec():
    n = 1000
    l2 = rng.randint(0, 40, size=n)
    l3 = rng.randint(0, 40, size=n)
    m2 = np.zeros(n, dtype=int)
    m3 = np.zeros(n, dtype=int)
    for i in range(n):
        if l2[i] > 0:
            m2[i] = rng.randint(-l2[i], l2[i]+1)
        if l3[i] > 0:
            m3[i] = rng.randint(-l3[i], l3[i]+1)

    l, actual = wigner.drc3jj(l2, l3, m2, m3)
    for i in range(n):
        if (actual[i] != 0).any():
            l, expected = wigner._drc3jj(l2[i], l3[i], m2[i], m3[i])
            assert np.allclose(actual[i, l], expected)
        else:
            with pytest.raises(ValueError):
                l, expected = wigner._drc3jj(l2[i], l3[i], m2[i], m3[i])


def test_drc3jj_vec_err():
    n = 1000
    l2 = (0, 1, 2)
    l3 = (0, 1, 2)
    m2 = (1, 0, 0)
    m3 = (0, 0, 0)
    with pytest.raises(ValueError):
        _, actual = wigner.drc3jj(l2, l3, m2, m3)
