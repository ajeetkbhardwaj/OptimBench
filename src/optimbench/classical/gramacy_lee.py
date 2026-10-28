"""gramacy_lee(X)
Compute the Gramacy-Lee function on sample vector X.

The function is usually evaluated on x_i in [0, 1].
"""

import numpy as np


def gramacy_lee(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 1:
        raise ValueError("Sample vector must have length 1.")

    x = X[:, 0]

    y = np.array([
        (1 - x) ** 2 + 10 * np.sin(np.pi * x) ** 2 +
        0.1 * (np.pi * x) ** 2
        for x in x
    ])

    return y