"""brown(X, n=3)
Compute the n-dimensional Brown function on sample vector X.

The function is usually evaluated on x_i in [-1, 4].
"""

import numpy as np


def brown(X, n=3):
    X = np.atleast_2d(X)
    if X.shape[1] != n:
        raise ValueError(f"Sample vector tuples must be length {n}.")

    y = np.array([
        sum([(xi - 1) ** 2 for xi in x]) + sum([xi for xi in x]) ** 2 +
        sum([xi for xi in x]) ** 4
        for x in X
    ])

    return y