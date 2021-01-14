import numpy as np
import pytest
from py3nj import wigner, wigner6j


rng = np.random.RandomState(0)
# precalculated 3j symbols. Input, result
SIX_J = (
    ((0, 0, 0, 0, 0, 0), 1.0),
    ((2, 2, 2, 2, 2, 2), -3.0 / 70),
    ((4, 2, 2, 2, 2, 2), 2.0 / 35),
    ((4, 3, 2, 2, 2, 2), -(1.0 / 7) * np.sqrt(1.0 / 2)),
    ((0.5, 0.5, 1, 0.5, 0.5, 1), 1.0 / 6),
    ((0.5, 1.5, 1, 0.5, 0.5, 1), -(1.0 / 3)),
)


def test_drc6j():
    for six_j, result in SIX_J:
        six_j = (np.array(six_j) * 2).astype(np.int32)
        l, sixcof = wigner._drc6j(*(six_j[1:]))
        assert six_j[0] in l
        assert np.allclose(sixcof[l == six_j[0]], result)


def test_drc6j_vec():
    n = 1000
    l2 = rng.randint(0, 10, size=n)
    l3 = rng.randint(0, 10, size=n)
    l4 = rng.randint(0, 10, size=n)
    l5 = rng.randint(0, 10, size=n)
    l6 = rng.randint(0, 10, size=n)

    l, actual = wigner.drc6j(l2, l3, l4, l5, l6)
    for _ in range(2):
        l, actual = wigner.drc6j(l2, l3, l4, l5, l6)

    for i in range(n):
        if (actual[i] != 0).any():
            l, expected = wigner._drc6j(l2[i], l3[i], l4[i], l5[i], l6[i])
            assert np.allclose(actual[i, l], expected)
        else:
            with pytest.raises(ValueError):
                # all zeros or invalid argument
                l, expected = wigner._drc6j(l2[i], l3[i], l4[i], l5[i], l6[i])
                if (expected == 0).all():
                    raise ValueError


def test_wigner6j():
    n = 10000
    n2 = 10
    l2 = rng.randint(0, 40, size=n)
    l3 = rng.randint(0, 40, size=n)
    l4 = rng.randint(0, 40, size=n)
    l5 = rng.randint(0, 40, size=n)
    l6 = rng.randint(0, 40, size=n)

    l, expected_all = wigner.drc6j(l2, l3, l4, l5, l6)
    for _ in range(n2):
        lindex = rng.randint(0, 40, n)
        two_l1 = l[lindex]
        actual = wigner6j(two_l1, l2, l3, l4, l5, l6)
        expected = expected_all[np.arange(len(lindex)), lindex]
        assert np.allclose(actual, expected)


@pytest.mark.parametrize("ignore_invalid", [True, False])
def test_wigner6j_value(ignore_invalid):
    # scalar test
    for six_j, expected in SIX_J:
        six_j = (np.array(six_j) * 2).astype(int)
        actual = wigner6j(*six_j, ignore_invalid=ignore_invalid)
        assert np.allclose(actual, expected)
    # test vector
    six_j = np.array([six for six, _ in SIX_J]).T * 2
    expected = np.array([value for _, value in SIX_J]).T
    actual = wigner6j(*six_j.astype(int), ignore_invalid=ignore_invalid)
    assert np.allclose(actual, expected)


def test_wigner6j_GH13():
    """
    Test for https://github.com/fujiisoup/py3nj/issues/13
    """
    N = np.arange(10)
    J = np.arange(11)[:, np.newaxis]
    # should not fail
    wigner6j(0, N * 2, N * 2, J * 2, 2, 2)
