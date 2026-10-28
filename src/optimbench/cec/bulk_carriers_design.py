"""bulk_carriers_design(X)
Compute the Bulk carriers design problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #17.

Returns:
    f: list of 3 objective values
    g: list of 9 inequality constraints (negated in original)
    h: list of 1 equality constraint
"""

import numpy as np


def bulk_carriers_design(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    L = float(x[0])
    B = float(x[1])
    D = float(x[2])
    T = float(x[3])
    Vk = float(x[4])
    CB = float(x[5])

    a = 4977.06 * CB ** 2 - 8105.61 * CB + 4456.51
    b = -10847.2 * CB ** 2 + 12817 * CB - 6960.32
    Fn = 0.5144 / (9.8065 * L) ** 0.5

    P = ((1.025 * L * B * T * CB) ** (2/3) * Vk ** 3) / (a + b * Fn)

    Ws = 0.034 * L ** 1.7 * B ** 0.6 * D ** 0.4 * CB ** 0.5
    Wo = L ** 0.8 * B ** 0.6 * D ** 0.3 * CB ** 0.1
    Wm = 0.17 * P ** 0.9
    ls = Ws + Wo + Wm

    Dwt = 1.025 * L * B * T * CB - ls
    Fc = 0.19 * 24 * P / 1000 + 0.2
    Dcwt = Dwt - Fc * ((5000 * Vk) / 24 + 5) - 2 * Dwt ** 0.5
    Rtrp = 350 / ((5000 * Vk) / 24 + 2 * (Dcwt / 8000 + 0.5))
    ac = Dcwt * Rtrp

    f = np.zeros(3)
    f[0] = (Cc + Cr + Cv) / ac if 'Cc' in dir() else ac / ac  # placeholder - need to recalc
    f[1] = ls
    f[2] = -ac

    # Actually let me recalculate properly
    Cc = 0.2 * 1.3 * (2000 * Ws ** 0.85 + 3500 * Wo + 2400 * P ** 0.8)
    Cr = 40000 * Dwt ** 0.3
    Cv = (1.05 * 100 * Fc * (5000 * Vk / 24) + 6.3 * Dwt ** 0.8) * Rtrp

    f[0] = (Cc + Cr + Cv) / ac

    g = np.zeros(9)
    h = np.zeros(1)
    g[0] = L / B - 6
    g[1] = 15 - L / D
    g[2] = 19 - L / T
    g[3] = 0.45 * Dwt ** 0.31 - T
    g[4] = 0.7 * D + 0.7 - T
    g[5] = 0.32 - Fn
    g[6] = 0.53 * T + ((0.085 * CB - 0.002) * B ** 2) / (T * CB) - (1 + 0.52 * D) - 0.07 * B
    g[7] = Dwt - 3000
    g[8] = 500000 - Dwt

    g = -g  # negated as per original

    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()