from __future__ import annotations

import streamlit as st

from src.utils.styling import apply_theme

apply_theme()

st.title("About / Methodology")

st.markdown(
    """
    ## Project Objective
    This project models indoor thermal response using a simplified engineering approach that explains how temperature changes under weather, insulation, and HVAC control.

    ## Mathematical Model
    Newton's law of cooling and heating gives the fundamentals:
    
    
    
    
    """
)

st.latex(r"\frac{dT}{dt} = -k(T - T_{out})")
st.latex(r"T(t) = T_{out} + (T_0 - T_{out})e^{-kt}")
st.latex(r"C\frac{dT}{dt} = UA(T_{out} - T) - Q_{HVAC} + Q_{internal} + Q_{solar}")

st.markdown(
    """
    ## Numerical Methods
    - Bisection Method: repeatedly narrows a valid bracket until the function root is found.
    - Newton-Raphson Method: uses the derivative to achieve faster convergence.
    - Euler Method: a first-order approximation of the ODE.
    - RK4 Method: a higher-order method with improved accuracy.

    ## Higher-Order ODE Extension
    The extended model can be written as:
    
    """
)

st.latex(r"\frac{d^2T}{dt^2} + a\frac{dT}{dt} + bT = f(t)")

title = "How this project maps to the Numerical Methods syllabus"
st.subheader(title)

st.markdown(
    "- Unit II: Bisection and Newton-Raphson\n"
    "- Unit IV: First-order ODE, Newton's Law of Cooling, heating/cooling applications\n"
    "- Unit V: Higher-order ODE extension, homogeneous and non-homogeneous formulation"
)

st.caption("This project is intended for educational demonstration and not as a complete commercial building model.")
