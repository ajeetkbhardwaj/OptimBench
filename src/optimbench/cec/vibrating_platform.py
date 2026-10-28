"""vibrating_platform(X)
Compute the Vibrating Platform problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #2.

Returns:
    f: list of 2 objective values
    g: list of 5 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def vibrating_platform(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    d1 = x[0]
    d2 = x[1]
    d3 = x[2]
    b = x[3]
    L = x[4]

    rho1 = 100
    rho2 = 2770
    rho3 = 7780
    E1 = 1.6
    E2 = 70
    E3 = 200
    c1 = 500
    c2 = 1500
    c3 = 800

    mu = 2 * b * (rho1 * d1 + rho2 * (d2 - d1) + rho3 * (d3 - d2))
    EI = (2 * b / 3) * (E1 * d1 ** 3 + E2 * (d2 ** 3 - d1 ** 3) + rho3 * (d3 - d2))

    f = np.zeros(2)
    f[0] = (-np.pi / (2 * L)) ** 2 * (abs(EI / mu)) ** 0.5
    f[1] = 2 * b * L * (c1 * d1 + c2 * (d2 - d1) + c3 * (d3 - d2))

    g = np.zeros(5)
    g[0] = mu * L - 2800
    g[1] = d1 - d2
    g[2] = d2 - d1 - 0.15
    g[3] = d2 - d3
    g[4] = d3 - d2 - 0.01

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()