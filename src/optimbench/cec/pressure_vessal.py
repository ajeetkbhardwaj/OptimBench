"""pressure_vessal(X)
Compute the Pressure Vessal problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #1.

Returns:
    f: list of 2 objective values
    g: list of 2 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def pressure_vessal(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = int(np.round(x[0]))
    x2 = int(np.round(x[1]))
    x3 = float(x[2])
    x4 = float(x[3])

    z1 = 0.0625 * x1
    z2 = 0.0625 * x2

    f = np.zeros(2)
    f[0] = 1.7781 * z1 * x3 ** 2 + 0.6224 * z1 * x2 * x4 + 3.1661 * z1 ** 2 * x3 + 19.84 * z1 ** 2 * x3
    f[1] = -np.pi * x3 ** 2 * x4 - (4/3) * np.pi * x3 ** 3

    g = np.zeros(2)
    g[0] = 0.00954 * x3 - z2
    g[1] = 0.0193 * x3 - z1

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()