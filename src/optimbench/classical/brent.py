"""brent(X)
Compute the Brent function on sample vector X.

The function is usually evaluated on x_i in [-10, 10].
"""

import numpy as np


def brent(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x = X[:, 0]
    y = X[:, 1]

    y_val = np.array([
        100 * (y - x ** 2) ** 2 + (1 - x) ** 2 +
        90 * (y - 1) ** 2 + 10.1 * (x - 1) ** 2 +
        19.8 * (y - 1) * (x - 1)
        for x, y in zip(x, y)
    ])

    return y_val