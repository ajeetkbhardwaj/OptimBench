"""simply_supported_I_beam_design(X)
Compute the Simply supported I-beam design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #12.

Returns:
    f: list of 2 objective values
    g: list of 1 inequality constraint
    h: list of 1 equality constraint
"""

import numpy as np


def simply_supported_I_beam_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    x4 = float(x[3])

    P = 600
    L = 200
    E = 2e4

    f = np.zeros(2)
    f[0] = 2 * x2 * x4 + x3 * (x1 - 2 * x4)
    f[1] = P * L ** 3 / (48 * E * (x3 * ((x1 - 2 * x4) ** 3) + 2 * x2 * x4 * (4 * x4 ** 2 + 3 * x1 * (x1 - 2 * x4)) / 12))

    g = np.zeros(1)
    h = np.zeros(1)
    g[0] = -16 + 180000 * x1 / (x3 * ((x1 - 2 * x4) ** 3) + 2 * x2 * x4 * (4 * x4 ** 2 + 3 * x1 * (x1 - 2 * x4)) / 12) + 15000 * x2 / ((x1 - 2 * x4) * x3 ** 3 + 2 * x4 * x2 ** 3)

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()