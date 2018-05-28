import numpy as np
import pytest
from py3nj import wigner, wigner3j


rng = np.random.RandomState(0)
# precalculated 3j symbols. Input, result
SIX_J = (
    ((0, 0, 0, 0, 0, 0), 1.0),
    ((2, 2, 2, 2, 2, 2), -3.0/70),
    ((4, 2, 2, 2, 2, 2), 2.0/35),
    ((4, 3, 2, 2, 2, 2), -(1.0/7) * np.sqrt(1.0/2)),
    ((0.5, 0.5, 1, 0.5, 0.5, 1), 1.0/6),
    ((0.5, 1.5, 1, 0.5, 0.5, 1), -(1.0/3)),
)


def test_drc6j():
    for six_j, result in SIX_J:
        six_j = (np.array(six_j) * 2).astype(np.int32)
        l, sixcof = wigner._drc6j(*(six_j[1:]))
        assert six_j[0] in l
        assert np.allclose(sixcof[l == six_j[0]], result)
