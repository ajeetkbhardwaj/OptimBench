"""gear_box_design(X)
Compute the Gear box design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #13.

Returns:
    f: list of 3 objective values
    g: list of 11 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def gear_box_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = int(np.round(x[2]))
    x4 = float(x[3])
    x5 = float(x[4])
    x6 = float(x[5])
    x7 = float(x[6])

    f = np.zeros(3)
    f[0] = 0.7854 * x1 * x2 ** 2 * (10 * x3 ** 2 / 3 + 14.933 * x3 - 43.0934) - 1.508 * x1 * (x6 ** 2 + x7 ** 2) + 7.477 * (x6 ** 3 + x7 ** 3) + 0.7854 * (x4 * x6 ** 2 + x5 * x7 ** 2)
    f[1] = np.sqrt((745 * x4 / (x2 * x3)) ** 2 + 1.69e7) / (0.1 * x6 ** 3)
    f[2] = np.sqrt((745 * x5 / (x2 * x3)) ** 2 + 1.575e8) / (0.1 * x7 ** 3)

    g = np.zeros(11)
    h = np.zeros(1)
    g[0] = 1 / (x1 * x2 ** 2 * x3) - 1/27
    g[1] = 1 / (x1 * x2 ** 2 * x3 ** 2) - 1/397.5
    g[2] = x4 ** 3 / (x2 * x3 * x6 ** 4) - 1/1.93
    g[3] = x5 ** 3 / (x2 * x3 * x7 ** 4) - 1/1.93
    g[4] = x2 * x3 - 40
    g[5] = x1 / x2 - 12
    g[6] = -x1 / x2 + 5
    g[7] = 1.9 - x4 + 1.5 * x6
    g[8] = 1.9 - x5 + 1.1 * x7
    g[9] = f[1] - 1300
    g[10] = f[2] - 1100

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()