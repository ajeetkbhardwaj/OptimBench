"""bird(X)
Compute the Bird function on sample vector X.

The function is usually evaluated on x_i in [-5, 5].
"""

import numpy as np


def bird(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x1 = X[:, 0]
    x2 = X[:, 1]

    y = np.array([
        x1 ** 2 + x2 ** 2 - 0.3 * np.cos(3 * np.pi * x1) - 0.4 * np.cos(4 * np.pi * x2) + 0.7
        for x in X
    ])

    return y