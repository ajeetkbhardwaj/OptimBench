"""weldan_beam_design(X)
Compute the Weldan Beam design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #4.

Returns:
    f: list of 2 objective values
    g: list of 4 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def weldan_beam_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    x4 = float(x[3])

    P = 6000
    L = 14
    E = 30e6
    tmax = 13600
    sigmax = 30000
    G = 12e6

    Pc = (4.013 * E * ((x3 ** 2 + x4 ** 6) / 36) ** 0.5) / (L ** 2) * (1 - x3 / (2 * L) * (E / (4 * G)) ** 0.5)
    sigma = (6 * P * L) / (x4 * x3 ** 2)
    J = 2 * (np.sqrt(2) * x1 * x2 * (x2 ** 2 / 12 + ((x1 + x3) / 2) ** 2))
    R = np.sqrt(x2 ** 2 / 4 + ((x1 + x3) / 2) ** 2)
    M = P * (L + x2 / 2)
    tho1 = P / (np.sqrt(2) * x1 * x2)
    tho2 = M * R / J
    tho = np.sqrt(tho1 ** 2 + 2 * tho1 * tho2 * x2 / (2 * R) + tho2 ** 2)

    f = np.zeros(2)
    f[0] = 1.10471 * x1 ** 2 * x2 + 0.04811 * x3 * x4 * (14 + x2)
    f[1] = (4 * P * L ** 3) / (E * x4 * x3 ** 3)

    g = np.zeros(4)
    g[0] = tho - tmax
    g[1] = sigma - sigmax
    g[2] = x1 - x4
    g[3] = P - Pc

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()