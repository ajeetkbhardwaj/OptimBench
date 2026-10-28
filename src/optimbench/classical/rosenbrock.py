"""rosenbrock(X, n=2)
Compute the n-dimensional Rosenbrock function on sample vector X.

The function is usually evaluated on x_i in [-5, 10] or x_i in [-2.048, 2.048].
"""

import numpy as np


def rosenbrock(X, n=2):
    X = np.atleast_2d(X)
    if X.shape[1] != n:
        raise ValueError(f"Sample vector tuples must be length {n}.")

    y = np.array([
        np.sum([100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2 for i in range(n - 1)])
        for x in X
    ])

    return y