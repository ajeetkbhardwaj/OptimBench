"""four_bar_plane_truss(X)
Compute the Four Bar Plane Truss problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #9.

Returns:
    f: list of 2 objective values
    g: list of 1 inequality constraint
    h: list of 1 equality constraint
"""

import numpy as np


def four_bar_plane_truss(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    x4 = float(x[3])

    F = 10
    E = 2e5
    L = 200
    sig = 10

    f = np.zeros(2)
    f[0] = L * (2 * x1 + np.sqrt(2) * x2 + np.sqrt(2) * x3 + x4)
    f[1] = F * L / E * (2 / x1 + 2 * np.sqrt(2) / x2 - 2 * np.sqrt(2) / x3 + 2 / x4)

    g = np.zeros(1)
    h = np.zeros(1)

    return f.tolist(), g.tolist(), h.tolist()