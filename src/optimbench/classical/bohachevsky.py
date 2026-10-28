"""bohachevsky_1(X)
Compute the Bohachevsky 1 function on sample vector X.

The function is usually evaluated on x_i in [-10, 10].
"""

import numpy as np


def bohachevsky_1(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x = X[:, 0]
    y = X[:, 1]

    y_val = np.array([
        x ** 2 + 2 * y ** 2 - 0.3 * np.cos(3 * np.pi * x) - 0.4 * np.cos(4 * np.pi * y) + 0.7
        for x, y in zip(x, y)
    ])

    return y_val


"""bohachevsky_2(X)
Compute the Bohachevsky 2 function on sample vector X.

The function is usually evaluated on x_i in [-10, 10].
"""

import numpy as np


def bohachevsky_2(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x = X[:, 0]
    y = X[:, 1]

    y_val = np.array([
        (x ** 2 + y - 11) ** 2 +
        (x + y ** 2 - 7) ** 2
        for x, y in zip(x, y)
    ])

    return y_val

"""bohachevsky_3(X)
Compute the Bohachevsky 3 function on sample vector X.

The function is usually evaluated on x_i in [-10, 10].
"""

import numpy as np


def bohachevsky_3(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x = X[:, 0]
    y = X[:, 1]

    y_val = np.array([
        (2 * x ** 2 - 0.3 * np.cos(3 * np.pi * x) + 2 * y ** 2 - 0.4 * np.cos(4 * np.pi * y)) +
        (3 * x * y + 1) ** 2
        for x, y in zip(x, y)
    ])

    return y_val