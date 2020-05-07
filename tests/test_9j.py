import numpy as np
import pytest
from py3nj import wigner9j


rng = np.random.RandomState(0)
# precalculated 3j symbols. Input, result
NINE_J = (
    ((1, 1, 1,
      1, 1, 1,
      1, 1, 1), 0.0),
    #
    ((1, 2, 1,
      1, 1, 1,
      1, 1, 1), 1.0 / 18),
    #
    ((1, 2, 1,
      2, 3, 1,
      1, 2, 1), 1.0 / 5.0 * np.sqrt(1.0/30)),
)


def test_wigner9j():
    # scalar test
    for nine_j, expected in NINE_J:
        nine_j = (np.array(nine_j) * 2).astype(int)
        actual = wigner9j(*nine_j)
        print(nine_j)
        assert np.allclose(actual, expected)
    # test vector
    nine_j = (np.array([nine for nine, _ in NINE_J]).T * 2).astype(int)
    expected = np.array([value for _, value in NINE_J]).T
    actual = wigner9j(*nine_j)
    assert np.allclose(actual, expected)


def test_issue2():
  # https://github.com/fujiisoup/py3nj/issues/2
  actual = wigner9j(0, 0, 0, 2 * 1, 0, 2 * 1, 2 * 1, 0, 2 * 1)
  expected = 1.0 / 3.0
  assert np.allclose(actual, expected)