"""spring_design(X)
Compute the Spring design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #15.

Returns:
    f: list of 2 objective values
    g: list of 8 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def spring_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = int(np.round(x[0]))
    x2 = float(x[1])

    d = [0.009, 0.0095, 0.0104, 0.0118, 0.0128, 0.0132, 0.014,
         0.015, 0.0162, 0.0173, 0.018, 0.020, 0.023, 0.025,
         0.028, 0.032, 0.035, 0.041, 0.047, 0.054, 0.063,
         0.072, 0.080, 0.092, 0.0105, 0.120, 0.135, 0.148,
         0.162, 0.177, 0.192, 0.207, 0.225, 0.244, 0.263,
         0.283, 0.307, 0.331, 0.362, 0.394, 0.4375, 0.500]

    x3 = d[max(1, min(42, int(np.round(x[2]))))]

    cf = (4 * x2 / x3 - 1) / (4 * x2 / x3 - 4) + 0.615 * x3 / x2
    K = (11.5e6 * x3 ** 4) / (8 * x1 * x2 ** 3)
    lf = 1000 / K + 1.05 * (x1 + 2) * x3
    sigp = 300 / K

    f = np.zeros(2)
    f[0] = (np.pi ** 2 * x2 * x3 ** 2 * (x1 + 2)) / 4
    f[1] = (8000 * cf * x2) / (np.pi * x3 ** 3)

    g = np.zeros(8)
    g[0] = (8000 * cf * x2) / (np.pi * x3 ** 3) - 189000
    g[1] = lf - 14
    g[2] = 0.2 - x3
    g[3] = x2 - 3
    g[4] = 3 - x2 / x3
    g[5] = sigp - 6
    g[6] = sigp + 700 / K + 1.05 * (x1 + 2) * x3 - lf
    g[7] = 1.25 - 700 / K

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()