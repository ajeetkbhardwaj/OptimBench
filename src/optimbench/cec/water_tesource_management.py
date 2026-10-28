"""water_tesource_management(X)
Compute the Water Resource Management problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #11.

Returns:
    f: list of 5 objective values
    g: list of 7 inequality constraints (negated in original)
    h: list of 1 equality constraint
"""

import numpy as np


def water_tesource_management(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])

    f = np.zeros(5)
    f[0] = 106780.37 * (x2 + x3) + 61704.67
    f[1] = 3000 * x1
    f[2] = 305700 * 2289 * x2 / ((0.06 * 2289) ** 0.65)
    f[3] = 250 * 2289 * np.exp(-39.75 * x2 + 9.9 * x3 + 2.74)
    f[4] = 25 * (1.39 / (x1 * x2) + 4940 * x3 - 80)

    g = np.zeros(7)
    h = np.zeros(1)
    g[0] = 1 - (0.00139 / (x1 * x2) + 4.94 * x3 - 0.08)
    g[1] = 1 - (0.000306 / (x1 * x2) + 1.082 * x3 - 0.0986)
    g[2] = 50000 - (12.307 / (x1 * x2) + 49408.24 * x3 + 4051.02)
    g[3] = 16000 - (2.098 / (x1 * x2) + 8046.33 * x3 - 696.71)
    g[4] = 10000 - (2.138 / (x1 * x2) + 7883.39 * x3 - 705.04)
    g[5] = 2000 - (0.417 * x1 * x2 + 1721.26 * x3 - 136.54)
    g[6] = 550 - (0.164 / (x1 * x2) + 631.13 * x3 - 54.48)
    g = -g  # negated as per original

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()