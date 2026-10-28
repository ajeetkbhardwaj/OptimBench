"""two_bar_Truss_design_problems(X)
Compute the Two bar Truss design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #3.

Returns:
    f: list of 2 objective values
    g: list of 3 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def two_bar_Truss_design_problems(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])

    f = np.zeros(2)
    f[0] = x1 * (16 + x3 ** 2) ** 0.5 + x2 * (1 + x3 ** 2) ** 0.5
    f[1] = (20 * (16 + x3 ** 2) ** 0.5) / (x3 * x1)

    g = np.zeros(3)
    g[0] = f[0] - 0.1
    g[1] = f[1] - 1e5
    g[2] = (80 * (1 + x3 ** 2) ** 0.5) / (x3 * x2) - 1e5

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()