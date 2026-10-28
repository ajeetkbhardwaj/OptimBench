"""front_rail_design(X)
Compute the Front rail design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #18.

Returns:
    f: list of 2 objective values
    g: list of 3 inequality constraints (negated in original)
    h: list of 1 equality constraint
"""

import numpy as np


def front_rail_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    hh = float(x[0])
    w = float(x[1])
    t = float(x[2])

    Ea = 14496.5
    Fa = 234.9

    E = -70973.4 + 958.656 * w + 614.173 * hh - 3.827 * w * hh + 57.023 * w * t + 63.274 * hh * t - 3.582 * w ** 2 - 1.4842 * hh ** 2 - 1890.174 * t ** 2
    F = 111.854 - 20.210 * w + 7.560 * hh - 0.025 * w * hh + 2.731 * w * t - 1.479 * hh * t + 0.165 * w ** 2

    f = np.zeros(2)
    f[0] = Ea / E
    f[1] = F / Fa

    g = np.zeros(3)
    h = np.zeros(1)
    g[0] = (hh - 136) * (146 - hh)
    g[1] = (w - 58) * (66 - w)
    g[2] = (t - 1.4) * (2.2 - t)
    g = -g  # negated as per original

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()