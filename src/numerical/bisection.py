from __future__ import annotations

import numpy as np


def bisection_method(function, lower_bound: float, upper_bound: float, tolerance: float = 1e-6, max_iterations: int = 100):
    if not np.isfinite(lower_bound) or not np.isfinite(upper_bound):
        raise ValueError("Bounds must be finite numbers.")
    if tolerance <= 0:
        raise ValueError("Tolerance must be positive.")
    if max_iterations <= 0:
        raise ValueError("Max iterations must be positive.")

    lower_value = function(lower_bound)
    upper_value = function(upper_bound)
    history = []
    if lower_value * upper_value > 0:
        raise ValueError("Invalid bracket: f(lower) * f(upper) > 0. The root is not bracketed.")

    midpoint = 0.0
    for iteration in range(1, max_iterations + 1):
        midpoint = (lower_bound + upper_bound) / 2.0
        midpoint_value = function(midpoint)
        error = abs(upper_bound - lower_bound) / 2.0
        history.append({
            "iteration": iteration,
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "midpoint": midpoint,
            "f_midpoint": midpoint_value,
            "absolute_error": error,
        })
        if abs(midpoint_value) < tolerance or error < tolerance:
            return {
                "root": midpoint,
                "iterations": iteration,
                "error": error,
                "converged": True,
                "history": history,
            }
        if lower_value * midpoint_value <= 0:
            upper_bound = midpoint
            upper_value = midpoint_value
        else:
            lower_bound = midpoint
            lower_value = midpoint_value

    return {
        "root": midpoint,
        "iterations": len(history),
        "error": abs(upper_bound - lower_bound) / 2.0,
        "converged": False,
        "history": history,
    }
