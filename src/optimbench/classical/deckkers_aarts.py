"""deckkers_aarts(X)
Compute the Deckkers-Aarts function on sample vector X.

The function is usually evaluated on x_i in [-5, 5].
"""

import numpy as np


def deckkers_aarts(X):
    X = np.atleast_2d(X)
    if X.shape[1] != 2:
        raise ValueError("Sample vector must have length 2.")

    x1 = X[:, 0]
    x2 = X[:, 1]

    term1 = (x1 ** 2 + 3 * x2 - 9) ** 2
    term2 = (x1 + x2 + 1) ** 2
    term3 = 19 * (x2 - x1 ** 2) ** 2
    term4 = 6 * x1 + 7 * x2 + 13

    y_val = np.array([term1 + term2 + term3 + term4 for term1, term2, term3, term4 in zip(term1, term2, term3, term4)])

    return y_val