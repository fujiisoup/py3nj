import numpy as np
import pytest
from py3nj import wigner, wigner3j


rng = np.random.RandomState(0)
# precalculated 3j symbols. Input, result
THREE_J = (
    ((1, 1, 0, 0, 0, 0), -np.sqrt(1.0/3)),
    ((0, 1, 1, 0, 0, 0), -np.sqrt(1.0/3)),
    ((2, 1, 1, 0, 0, 0), np.sqrt(2.0/15)),
    ((0, 1, 1, 0,-1, 1), np.sqrt(1.0/3)),
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


@pytest.mark.parametrize('half_integer', [1, 0])
def test_drc3jj_vec(half_integer):
    n = 1000
    l2 = rng.randint(0, 10, size=n) * 2 + half_integer
    l3 = rng.randint(0, 10, size=n) * 2 + half_integer
    m2 = np.zeros(n, dtype=int)
    m3 = np.zeros(n, dtype=int)
    for i in range(n):
        if l2[i] > 0:
            m2[i] = rng.randint(-l2[i], l2[i]+1)
        if l3[i] > 0:
            m3[i] = rng.randint(-l3[i], l3[i]+1)

    l, actual = wigner.drc3jj(l2, l3, m2, m3)
    for _ in range(2):
        l, actual = wigner.drc3jj(l2, l3, m2, m3)

    for i in range(n):
        if (actual[i] != 0).any():
            l, expected = wigner._drc3jj(l2[i], l3[i], m2[i], m3[i])
            assert np.allclose(actual[i, l], expected)
        else:
            with pytest.raises(ValueError):
                # all zeros or invalid argument
                l, expected = wigner._drc3jj(l2[i], l3[i], m2[i], m3[i])
                if (expected == 0).all():
                    raise ValueError


def test_drc3jj_vec_err():
    l2 = (0, 1, 2)
    l3 = (0, 1, 2)
    m2 = (1, 0, 0)
    m3 = (0, 0, 0)
    with pytest.raises(ValueError):
        _, actual = wigner.drc3jj(l2, l3, m2, m3)


@pytest.mark.parametrize('half_integer', [1, 0])
def test_wigner3j(half_integer):
    n = 10000
    n2 = 10
    l2 = rng.randint(0, 40, size=n) * 2 + half_integer
    l3 = rng.randint(0, 40, size=n) * 2 + half_integer
    m2 = np.zeros(n, dtype=int)
    m3 = np.zeros(n, dtype=int)
    for i in range(n):
        if l2[i] > 0:
            m2[i] = rng.randint(-l2[i], l2[i]+1)
        if l3[i] > 0:
            m3[i] = rng.randint(-l3[i], l3[i]+1)

    l, expected_all = wigner.drc3jj(l2, l3, m2, m3)
    for _ in range(n2):
        lindex = rng.randint(0, 40, n) * 2 - 1 + half_integer
        two_l1 = l[lindex]
        two_m1 = -(m2 + m3)
        actual = wigner3j(two_l1, l2, l3, two_m1, m2, m3)
        expected = expected_all[np.arange(len(lindex)), lindex]
        assert np.allclose(actual, expected)


def test_wigner3j_value():
    # scalar test
    for three_j, expected in THREE_J:
        three_j = np.array(three_j) * 2
        actual = wigner3j(*three_j)
        assert np.allclose(actual, expected)
    # test vector
    three_j = np.array([thr for thr, _ in THREE_J]).T * 2
    expected = np.array([value for _, value in THREE_J]).T
    actual = wigner3j(*three_j)
    assert np.allclose(actual, expected)


def test0d():
    for _ in range(100):
        l2 = rng.randint(0, 40) * 2
        l3 = rng.randint(0, 40) * 2
        m2 = 0
        if l2 > 0:
            m2 = rng.randint(-l2, l2+1)
        m3 = 0
        if l3 > 0:
            m3 = rng.randint(-l3, l3+1)
        l, actual = wigner.drc3jj(l2, l3, m2, m3)
        assert actual.ndim == 1

        if (actual != 0).any():
            l, expected = wigner._drc3jj(l2, l3, m2, m3)
            assert np.allclose(actual[l], expected)
        else:
            with pytest.raises(ValueError):
                # all zeros or invalid argument
                l, expected = wigner._drc3jj(l2, l3, m2, m3)
                if (expected == 0).all():
                    raise ValueError


def test2d():
    n = (10, 11)
    l2 = rng.randint(0, 10, size=n) * 2
    l3 = rng.randint(0, 10, size=n) * 2
    m2 = np.zeros(n, dtype=int)
    m3 = np.zeros(n, dtype=int)
    for i0 in range(n[0]):
        for i1 in range(n[1]):
            i = (i0, i1)
            if l2[i] > 0:
                m2[i] = rng.randint(-l2[i], l2[i]+1)
            if l3[i] > 0:
                m3[i] = rng.randint(-l3[i], l3[i]+1)

    l, actual = wigner.drc3jj(l2, l3, m2, m3)
    for i0 in range(n[0]):
        for i1 in range(n[1]):
            i = (i0, i1)
            if (actual[i] != 0).any():
                l, expected = wigner._drc3jj(l2[i], l3[i], m2[i], m3[i])
                assert np.allclose(actual[i][l], expected)
            else:
                with pytest.raises(ValueError):
                    # all zeros or invalid argument
                    l, expected = wigner._drc3jj(l2[i], l3[i], m2[i], m3[i])
                    if (expected == 0).all():
                        raise ValueError
