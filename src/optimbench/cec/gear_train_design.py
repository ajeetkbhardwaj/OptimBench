"""gear_train_design(X)
Compute the Gear Train design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #7.

Returns:
    f: list of 2 objective values
    g: list of 1 inequality constraint
    h: list of 1 equality constraint
"""

import numpy as np


def gear_train_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    x4 = float(x[3])

    f = np.zeros(2)
    f[0] = abs(6.931 - x3 * x4 / (x1 * x2))
    f[1] = max(x1, x2, x3, x4)

    g = np.zeros(1)
    h = np.zeros(1)
    g[0] = f[0] / 6.931 - 0.5

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()