import math

import pytest

from src.numerical.bisection import bisection_method


def test_bisection_known_root():
    def f(x):
        return x**2 - 4
    result = bisection_method(f, 0.0, 10.0, tolerance=1e-8, max_iterations=100)
    assert abs(result["root"] - 2.0) < 1e-6
    assert result["converged"] is True


def test_bisection_convergence():
    def f(x):
        return x**3 - 27
    result = bisection_method(f, 0.0, 10.0, tolerance=1e-6, max_iterations=200)
    assert result["iterations"] > 0
    assert result["error"] >= 0


def test_bisection_invalid_bracket():
    def f(x):
        return x**2 + 1
    with pytest.raises(ValueError):
        bisection_method(f, -2.0, 2.0, tolerance=1e-6, max_iterations=50)
