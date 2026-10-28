"""hydro_static_thrust_bearing_design(X)
Compute the Hydro-static thrust bearing design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #20.

Returns:
    f: list of 2 objective values
    g: list of 7 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def hydro_static_thrust_bearing_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    R = float(x[0])
    Ro = float(x[1])
    mu = float(x[2])
    Q = float(x[3])

    gamma = 0.0307
    C = 0.5
    n = -3.55
    C1 = 10.04
    Ws = 101000
    Pmax = 1000
    delTmax = 50
    hmin = 0.001
    gg = 386.4
    N = 750

    P_val = (np.log10(np.log10(8.122e6 * mu + 0.8)) - C1) / n
    delT = 2 * (10 ** P_val - 560)
    Ef = 9336 * Q * gamma * C * delT
    h_val = (2 * np.pi * N / 60) ** 2 * 2 * np.pi * mu / Ef * (R ** 4 / 4 - Ro ** 4 / 4) - 1e-5
    Po = (6 * mu * Q / (np.pi * h_val ** 3)) * np.log(R / Ro)
    W = np.pi * Po / 2 * (R ** 2 - Ro ** 2) / (np.log(R / Ro) - 1e-5)

    f = np.zeros(2)
    f[0] = (Q * Po / 0.7 + Ef) / 12
    f[1] = gamma / (gg * Po) * (Q / (2 * np.pi * R * h_val))

    g = np.zeros(7)
    g[0] = Ws - W
    g[1] = Po - Pmax
    g[2] = delT - delTmax
    g[3] = hmin - h_val
    g[4] = Ro - R
    g[5] = f[1] - 0.001
    g[6] = W / (np.pi * (R ** 2 - Ro ** 2) + 1e-5) - 5000

    h = np.array([0.0])  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()