"""car_side_impact_design(X)
Compute the Car Side Impact design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #8.

Returns:
    f: list of 3 objective values
    g: list of 9 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def car_side_impact_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    x4 = float(x[3])
    x5 = float(x[4])
    x6 = float(x[5])
    x7 = float(x[6])

    VMBP = 10.58 - 0.674 * x1 * x2 - 0.67275 * x2
    VFD = 16.45 - 0.489 * x3 * x7 - 0.843 * x5 * x6

    f = np.zeros(3)
    f[0] = 1.98 + 4.9 * x1 * 6.67 * x2 + 6.98 * x3 + 4.01 * x4 + 1.78 * x5 + 1e-5 * x6 + 2.73 * x7
    f[1] = 4.72 - 0.5 * x4 - 0.19 * x2 * x3
    f[2] = 0.5 * (VMBP + VFD)

    g = np.zeros(9)
    h = np.zeros(1)
    g[0] = -1 + 1.16 - 0.3717 * x2 * x4 - 0.0092928 * x3
    g[1] = -0.32 + 0.261 - 0.0159 * x1 * x2 - 0.06486 * x1 - 0.019 * x2 * x7 + 0.0144 * x2 * x5 + 0.0154464 * x6
    g[2] = -0.32 + 0.74 - 0.61 * x2 - 0.031296 * x3 - 0.031872 * x7 + 0.227 * x2 ** 2
    g[3] = -0.32 + 0.214 + 0.00817 * x5 - 0.045195 * x1 - 0.0135168 * x1 + 0.03099 * x2 * x6 - 0.018 * x2 * x7 + 0.007176 * x3 + 0.023232 * x3 - 0.00364 * x5 * x6 - 0.018 * x2 ** 2
    g[4] = -32 + 33.86 + 2.95 * x3 - 5.057 * x1 * x2 - 3.795 * x2 - 3.4431 * x7 + 1.45728
    g[5] = -32 + 28.98 + 3.818 * x3 - 4.2 * x1 * x2 + 1.27296 * x6 - 2.68065 * x7
    g[6] = -32 + 46.36 - 9.9 * x2 - 4.4505 * x1
    g[7] = f[1] - 4
    g[8] = VMBP - 9.9

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()