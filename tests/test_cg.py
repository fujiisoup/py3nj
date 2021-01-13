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


def test_wigner3j_value():
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
