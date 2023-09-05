import numpy as np
import pytest
from py3nj import clebsch_gordan


rng = np.random.RandomState(0)

# reference values from
# https://en.wikipedia.org/wiki/Table_of_Clebsch%E2%80%93Gordan_coefficients


CG = (
    # j1 = 1/2, j2 = 1/2
    ((1, 1, 2, 1, 1, 2), 1),
    ((1, 1, 2, -1, -1, -2), 1),
    ((1, 1, 2, 1, -1, 0), np.sqrt(0.5)),
    ((1, 1, 2, -1, 1, 0), np.sqrt(0.5)),
    ((1, 1, 0, 1, -1, 0), np.sqrt(0.5)),
    ((1, 1, 0, -1, 1, 0), -np.sqrt(0.5)),
    # j1 = 1, j2 = 1/2
    ((2, 2, 4, 2, 0, 2), np.sqrt(1.0 / 2)),
)
def test_clebsch_gordan_value():
    # scalar test
    for three_j, expected in CG:
        print(three_j)
        three_j = np.array(three_j)
        actual = clebsch_gordan(*three_j)
        assert np.allclose(actual, expected)
    # test vector
    three_j = np.array([thr for thr, _ in CG]).T
    expected = np.array([value for _, value in CG]).T
    actual = clebsch_gordan(*three_j)
    assert np.allclose(actual, expected)


# reference from https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients#Special%20cases
def test_clebsch_gordan_value_more():
    # if J3 = M3 = 0
    for offset in [0, 0.5]:
        for j1 in np.arange(offset, 4 + offset):
            for j2 in np.arange(offset, 3 + offset):
                m1 = np.arange(-j1, j1 + 1)[:, np.newaxis]
                m2 = np.arange(-j2, j2 + 1)
                expected = np.where(
                    (j1 == j2) * (m1 == -m2), 
                    (-1) ** (j1 - m1) / np.sqrt(2 * j1 + 1),
                    0.0
                )
                actual = clebsch_gordan(
                    int(2 * j1), int(2 * j2), 0, (2 * m1).astype(int), (2 * m2).astype(int), 0
                )
                assert np.allclose(expected, actual)
            