"""ackley_1(X, n=3)
Compute the n-dimensional Ackley function on sample vector X.

The function is usually evaluated on x_i in [-32, 32].
"""

import numpy as np


def ackley_1(X, n=2, a=20.0, b=0.02, c=np.pi):
    X = np.atleast_2d(X)
    if X.shape[1] != n:
        raise ValueError(f"Sample vector tuples must be length {n}.")

    def _ackley(x):
        term1 = -a * np.exp(-b * np.sqrt(1 / n * sum([xi ** 2 for xi in x])))
        term2 = np.exp(1 / n * sum([np.cos(c * xi) for xi in x]))
        return -term1 - term2 + a + np.exp(1)

    y = np.array([_ackley(x) for x in X])

    return y


"""ackley_2(X)
Compute the 2-dimensional Ackley function on sample vector X.

The function is usually evaluated on x_i in [-32, 32].
"""

def ackley_2(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    n = 2
    a = 20.0
    b = 0.2
    c = 2 * np.pi

    def _ackley(x):
        term1 = -a * np.exp(-b * np.sqrt(1 / n * sum([xi ** 2 for xi in x])))
        term2 = np.exp(1 / n * sum([np.cos(c * xi) for xi in x]))
        return -term1 - term2 + a + np.exp(1)

    y = np.array([_ackley(x) for x in X])

    return y


"""ackley_3(X)
Compute the 3-dimensional Ackley function on sample vector X.

The function is usually evaluated on x_i in [-32, 32].
"""

def ackley_3(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 3:
        raise ValueError("Sample vector must have length 3.")

    n = 3
    a = 20.0
    b = 0.2
    c = 2 * np.pi

    def _ackley(x):
        term1 = -a * np.exp(-b * np.sqrt(1 / n * sum([xi ** 2 for xi in x])))
        term2 = np.exp(1 / n * sum([np.cos(c * xi) for xi in x]))
        return -term1 - term2 + a + np.exp(1)

    y = np.array([_ackley(x) for x in X])

    return y


"""ackley_4(X)
Compute the 4-dimensional Ackley function on sample vector X.

The function is usually evaluated on x_i in [-32, 32].
"""

def ackley_4(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 4:
        raise ValueError("Sample vector must have length 4.")

    n = 4
    a = 20.0
    b = 0.2
    c = 2 * np.pi

    def _ackley(x):
        term1 = -a * np.exp(-b * np.sqrt(1 / n * sum([xi ** 2 for xi in x])))
        term2 = np.exp(1 / n * sum([np.cos(c * xi) for xi in x]))
        return -term1 - term2 + a + np.exp(1)

    y = np.array([_ackley(x) for x in X])

    return y