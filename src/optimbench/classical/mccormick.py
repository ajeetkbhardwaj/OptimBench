"""mccormick(X)
Compute the McCormick function on sample vector X.

The function is usually evaluated on x_i in [-1.5, 4].
"""

import numpy as np


def mccormick(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x = X[:, 0]
    y = X[:, 1]

    y_val = np.array([
        np.sin(x) + y - ((x - y) ** 2 / np.pi) + np.exp(-(x + y) ** 2)
        for x, y in zip(x, y)
    ])

    return y_val