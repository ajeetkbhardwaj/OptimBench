"""booth(X)
Compute the Booth function on sample vector X.

The function is usually evaluated on x_i in [-10, 10].
"""

import numpy as np


def booth(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x = X[:, 0]
    y = X[:, 1]

    y_val = np.array([
        (x + 2 * y - 7) ** 2 +
        (2 * x + y - 5) ** 2
        for x, y in zip(x, y)
    ])

    return y_val