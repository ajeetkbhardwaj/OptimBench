"""multiple_disk_clutch_brake_design(X)
Compute the Multiple-disk clutch brake design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #14.

Returns:
    f: list of 2 objective values
    g: list of 8 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def multiple_disk_clutch_brake_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    x1 = float(x[0])
    x2 = float(x[1])
    x3 = float(x[2])
    x4 = float(x[3])
    x5 = float(x[4])

    Mf = 3
    Ms = 40
    Iz = 55
    n = 250
    Tmax = 15
    s = 1.5
    delta = 0.5
    Vsrmax = 10
    rho = 0.0000078
    pmax = 1
    mu = 0.6
    Lmax = 30
    delR = 20

    Rsr = 2/3 * (x2 ** 3 - x1 ** 3) / (x2 ** 2 * x1 ** 2)
    Vsr = np.pi * Rsr * n / 30
    A = np.pi * (x2 ** 2 - x1 ** 2)
    Prz = x4 / A
    w = np.pi * n / 30
    Mh = 2/3 * mu * x4 * x5 * (x2 ** 3 - x1 ** 3) / (x2 ** 2 - x1 ** 2)
    T = Iz * w / (Mh + Mf)

    f = np.zeros(2)
    f[0] = np.pi * (x2 ** 2 - x1 ** 2) * x3 * (x5 + 1) * rho
    f[1] = T

    g = np.zeros(8)
    g[0] = -x2 + x1 + delR
    g[1] = (x5 + 1) * (x3 + delta) - Lmax
    g[2] = Prz - pmax
    g[3] = Prz * Vsr - pmax * Vsrmax
    g[4] = Vsr - Vsrmax
    g[5] = T - Tmax
    g[6] = s * Ms - Mh
    g[7] = -T

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()