"""bartels_conn(X)
Compute the Bartels-Conn function on sample vector X.

The function is usually evaluated on x_i in [-5, 5].
"""

import numpy as np


def bartels_conn(X):
    X = np.atleast_2d(X)
    n = X.shape[1]

    y = np.array([
        np.sum([(xi ** 2 + xi + 1) ** 0.5 for xi in x]) for x in X
    ])

    return y