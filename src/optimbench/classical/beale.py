"""beale(X)
Compute the Beale function on sample vector X.

The function is usually evaluated on x_i in [0, 4.5] and y_i in [0, 4.5].
"""

import numpy as np


def beale(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x = X[:, 0]
    y = X[:, 1]

    y_val = np.array([
        (1.5 - x + x * y) ** 2 +
        (2.25 - x + x * y ** 2) ** 2 +
        (2.625 - x + x * y ** 3) ** 2 +
        (2.71875 - x + x * y ** 4) ** 2
        for x in X
    ])

    return y_val