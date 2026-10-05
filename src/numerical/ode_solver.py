from __future__ import annotations

import numpy as np


def euler_method(function, x0: float, y0: float, step_size: float, steps: int):
    x = [x0]
    y = [y0]
    for _ in range(steps):
        next_y = y[-1] + function(x[-1], y[-1]) * step_size
        x.append(x[-1] + step_size)
        y.append(next_y)
    return np.array(x), np.array(y)


def rk4_method(function, x0: float, y0: float, step_size: float, steps: int):
    x = [x0]
    y = [y0]
    for _ in range(steps):
        xi = x[-1]
        yi = y[-1]
        k1 = function(xi, yi)
        k2 = function(xi + 0.5 * step_size, yi + 0.5 * step_size * k1)
        k3 = function(xi + 0.5 * step_size, yi + 0.5 * step_size * k2)
        k4 = function(xi + step_size, yi + step_size * k3)
        next_y = yi + (step_size / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        x.append(xi + step_size)
        y.append(next_y)
    return np.array(x), np.array(y)
