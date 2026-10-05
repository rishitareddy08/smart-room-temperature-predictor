from __future__ import annotations

import numpy as np


def newton_raphson_method(function, derivative, initial_guess: float, tolerance: float = 1e-6, max_iterations: int = 100):
    if tolerance <= 0:
        raise ValueError("Tolerance must be positive.")
    if max_iterations <= 0:
        raise ValueError("Max iterations must be positive.")

    current = float(initial_guess)
    history = []
    for iteration in range(1, max_iterations + 1):
        value = function(current)
        deriv = derivative(current)
        if abs(deriv) < 1e-12:
            return {"root": current, "iterations": iteration - 1, "error": float("inf"), "converged": False, "history": history}
        next_value = current - value / deriv
        error = abs(next_value - current)
        history.append({
            "iteration": iteration,
            "current_estimate": current,
            "f_x": value,
            "f_prime_x": deriv,
            "next_estimate": next_value,
            "error": error,
        })
        if abs(value) < tolerance or error < tolerance:
            return {"root": next_value, "iterations": iteration, "error": error, "converged": True, "history": history}
        current = next_value

    return {"root": current, "iterations": len(history), "error": abs(function(current)), "converged": False, "history": history}
