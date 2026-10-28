"""alpine_1(X, n=3)
Compute the n-dimensional Alpine function 1 on sample vector X.

The function is usually evaluated on x_i in [-10, 10].
"""

import numpy as np


def alpine_1(X, n=3):
    X = np.atleast_2d(X)
    if X.shape[1] != n:
        raise ValueError(f"Sample vector tuples must be length {n}.")

    y = np.array([
        np.sum([abs(xi * np.sin(xi)) + 0.1 * xi for xi in x], axis=0)
        for x in X
    ])

    return y


"""alpine_2(X, n=3)
Compute the n-dimensional Alpine function 2 on sample vector X.

The function is usually evaluated on x_i in [-10, 10].
"""



def alpine_2(X, n=3):
    X = np.atleast_2d(X)
    if X.shape[1] != n:
        raise ValueError(f"Sample vector tuples must be length {n}.")

    y = np.array([
        np.sum([(abs(xi) + 1) * np.sin(abs(xi)) + 0.1 * xi ** 2 for xi in x], axis=0)
        for x in X
    ])

    return y