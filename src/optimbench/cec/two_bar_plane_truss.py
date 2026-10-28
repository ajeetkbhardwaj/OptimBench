"""two_bar_plane_truss(X)
Compute the Two bar plane Truss problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #10.

Returns:
    f: list of 2 objective values
    g: list of 2 inequality constraints
    h: list of 2 equality constraints
"""

import numpy as np


def two_bar_plane_truss(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])

    rho = 0.283
    h_val = 100
    P = 104
    E = 3e7
    rho0 = 2e4

    f = np.zeros(2)
    f[0] = 2 * rho * h_val * x2 * np.sqrt(1 + x1 ** 2)
    f[1] = rho * h_val * (1 + x1 ** 2) ** 1.5 * (1 + x1 ** 4) ** 0.5 / (2 * np.sqrt(2) * E * x1 ** 2 * x2)

    g = np.zeros(2)
    h = np.zeros(2)
    g[0] = P * (1 + x1) * (1 + x1 ** 2) ** 0.5 / (2 * np.sqrt(2) * x1 * x2) - rho0
    g[1] = P * (-x1 + 1) * (1 + x1 ** 2) ** 0.5 / (2 * np.sqrt(2) * x1 * x2) - rho0

    return f.tolist(), g.tolist(), h.tolist()