"""disc_brake_design(X)
Compute the Disc Brake design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #5.

Returns:
    f: list of 2 objective values
    g: list of 4 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def disc_brake_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    x4 = float(x[3])

    f = np.zeros(2)
    f[0] = 4.9e-5 * (x2 ** 2 - x1 ** 2) * (x4 - 1)
    f[1] = 9.82e6 * (x2 ** 2 - x1 ** 2) / (x3 * x4 * (x2 ** 3 - x1 ** 3))

    g = np.zeros(4)
    g[0] = 20 - (x2 - x1)
    g[1] = x3 / (np.pi * (x2 ** 2 - x1 ** 2)) - 0.4
    g[2] = 2.22e-3 * x3 * (x2 ** 3 - x1 ** 3) / (x2 ** 2 - x1 ** 2) ** 2 - 1
    g[3] = 900 - 2.66e-2 * x3 * x4 * (x2 ** 3 - x1 ** 3) / (x2 ** 2 - x1 ** 2)

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()