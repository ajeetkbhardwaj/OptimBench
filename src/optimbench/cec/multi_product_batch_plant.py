"""multi_product_batch_plant(X)
Compute the Multi-product batch plant problem.

Real-World Multiobjective Constrained Optimization Problem (RW-MOP-2021) #19.

Returns:
    f: list of 3 objective values
    g: list of 10 inequality constraints
    h: list of 1 equality constraint
"""

import numpy as np


def multi_product_batch_plant(x):
    x = np.atleast_1d(np.array(x, dtype=float))
    N1 = int(np.round(x[0]))
    N2 = int(np.round(x[1]))
    N3 = int(np.round(x[2]))
    V1 = float(x[3])
    V2 = float(x[4])
    V3 = float(x[5])
    TL1 = float(x[6])
    TL2 = float(x[7])
    B1 = float(x[8])
    B2 = float(x[9])

    S = np.array([[2, 3, 4], [4, 6, 3]])
    t = np.array([[8, 20, 8], [16, 4, 4]])
    H = 6000
    alp = 250
    beta = 0.6
    Q1 = 40000
    Q2 = 20000

    f = np.zeros(3)
    f[0] = alp * (N1 * V1 ** beta + N2 * V2 ** beta + N3 * V3 ** beta)
    f[1] = 65 * (Q1 / B1 + Q2 / B2) + 0.08 * Q1 + 0.1 * Q2
    f[2] = Q1 * TL1 / B1 + Q2 * TL2 / B2

    g = np.zeros(10)
    g[0] = Q1 * TL1 / B1 + Q2 * TL2 / B2 - H
    g[1] = S[0, 0] * B1 + S[1, 0] * B2 - V1
    g[2] = S[0, 1] * B1 + S[1, 1] * B2 - V2
    g[3] = S[0, 2] * B1 + S[1, 2] * B2 - V3
    g[4] = t[0, 0] - N1 * TL1
    g[5] = t[0, 1] - N2 * TL1
    g[6] = t[0, 2] - N3 * TL1
    g[7] = t[1, 0] - N1 * TL2
    g[8] = t[1, 1] - N2 * TL2
    g[9] = t[1, 2] - N3 * TL2

    h = np.zeros(1)
    h[0] = 0.0  # no equality constraints in original

    return f.tolist(), g.tolist(), h.tolist()