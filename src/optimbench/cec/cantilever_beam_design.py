"""cantilever_beam_design(X)
Compute the Cantilever beam design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #16.

Returns:
    f: list of 2 objective values
    g: list of 2 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def cantilever_beam_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])

    P = 1
    E = 207000000
    Sy = 300000
    delta_max = 0.005
    rho = 7800

    f = np.zeros(2)
    f[0] = 0.25 * rho * np.pi * x2 * x1 ** 2
    f[1] = (64 * P * x2 ** 3) / (3 * E * np.pi * x1 ** 4)

    g = np.zeros(2)
    h = np.zeros(1)
    g[0] = -Sy + (32 * P * x2) / (np.pi * x1 ** 3)
    g[1] = -delta_max + (64 * P * x2 ** 3) / (3 * E * np.pi * x1 ** 4)

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()