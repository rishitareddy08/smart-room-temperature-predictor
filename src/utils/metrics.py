from __future__ import annotations

import numpy as np


def absolute_error(actual: float, predicted: float) -> float:
    return abs(actual - predicted)


def relative_error(actual: float, predicted: float) -> float:
    if abs(actual) < 1e-12:
        return 0.0
    return abs(actual - predicted) / abs(actual) * 100.0


def mae(actual: np.ndarray, predicted: np.ndarray) -> float:
    return float(np.mean(np.abs(actual - predicted)))


def rmse(actual: np.ndarray, predicted: np.ndarray) -> float:
    return float(np.sqrt(np.mean((actual - predicted) ** 2)))


def percent_difference(actual: float, predicted: float) -> float:
    return relative_error(actual, predicted)
