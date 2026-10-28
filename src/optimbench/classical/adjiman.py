"""adjiman(X)
Compute the 2-dimensional Adjiman function on sample vector X.

The function is usually evaluated on x_i in [-5, 10].
"""

import numpy as np


def adjiman(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x1 = X[:, 0]
    x2 = X[:, 1]

    y = np.array([
        100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2 +
        12.5 * (1 - x2) ** 2 + 0.1 * (1 - x1 - x2) ** 2
        for x in X
    ])

    return y