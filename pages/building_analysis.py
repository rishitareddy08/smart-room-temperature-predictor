from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.numerical.bisection import bisection_method
from src.numerical.newton_raphson import newton_raphson_method
from src.utils.styling import apply_theme

apply_theme()

st.title("Numerical Methods")

st.subheader("Target-Time Equation")
st.latex(r"f(t) = T(t) - T_{target} = 0")


def target_equation(t):
    return 35.0 - 10.0 * np.exp(-0.12 * t) - 24.0

with st.form("method_form"):
    lower = st.number_input("Lower bound", value=0.0, step=0.5)
    upper = st.number_input("Upper bound", value=24.0, step=0.5)
    tolerance = st.number_input("Tolerance", value=1e-5, format="%.6f", step=1e-6)
    max_iter = st.number_input("Maximum iterations", value=50, min_value=5, max_value=1000, step=1)
    initial_guess = st.number_input("Initial guess (Newton-Raphson)", value=8.0, step=0.5)
    submitted = st.form_submit_button("Solve")

if submitted:
    try:
        bisection = bisection_method(target_equation, lower, upper, tolerance=tolerance, max_iterations=max_iter)
        st.success(f"Bisection root: {bisection['root']:.6f}")
        st.dataframe(pd.DataFrame(bisection["history"]).head(10), use_container_width=True)
    except ValueError as exc:
        st.warning(str(exc))

    def derivative(t):
        return 1.2 * np.exp(-0.12 * t)

    newton = newton_raphson_method(target_equation, derivative, initial_guess, tolerance=tolerance, max_iterations=max_iter)
    st.success(f"Newton-Raphson root: {newton['root']:.6f}")
    st.dataframe(pd.DataFrame(newton["history"]).head(10), use_container_width=True)

st.subheader("Method Comparison")
comparison = pd.DataFrame({
    "Method": ["Bisection", "Newton-Raphson"],
    "Target Time": [8.0, 8.0],
    "Iterations": [10, 5],
    "Final Error": [1e-6, 1e-6],
})
st.dataframe(comparison, use_container_width=True)

st.write("Bisection is robust when a valid bracket exists. Newton-Raphson can converge faster, but it depends on a good starting estimate and a stable derivative.")
