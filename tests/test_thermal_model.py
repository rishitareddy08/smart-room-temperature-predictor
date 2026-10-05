import pytest

from src.numerical.newton_raphson import newton_raphson_method


def test_newton_known_root():
    def f(x):
        return x**2 - 4
    def df(x):
        return 2 * x
    result = newton_raphson_method(f, df, 3.0, tolerance=1e-8, max_iterations=50)
    assert abs(result["root"] - 2.0) < 1e-6
    assert result["converged"] is True


def test_newton_convergence():
    def f(x):
        return x**2 - 9
    def df(x):
        return 2 * x
    result = newton_raphson_method(f, df, 5.0, tolerance=1e-7, max_iterations=30)
    assert result["iterations"] > 0


def test_newton_derivative_zero_case():
    def f(x):
        return x**2 - 4
    def df(x):
        return 0.0
    result = newton_raphson_method(f, df, 3.0, tolerance=1e-8, max_iterations=30)
    assert result["converged"] is False
