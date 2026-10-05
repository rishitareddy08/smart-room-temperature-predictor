from __future__ import annotations

import streamlit as st

from src.utils.constants import DEFAULT_DEMO
from src.utils.styling import apply_theme

apply_theme()

st.title("Smart Room Temperature Predictor")
st.caption("Numerical intelligence for understanding indoor thermal behavior.")

st.write("This home page introduces the project and helps you launch the main engineering simulation workflow.")

if st.button("Launch Simulator"):
    st.switch_page("pages/simulator.py")

if st.button("Explore Numerical Methods"):
    st.switch_page("pages/numerical_methods.py")

st.markdown("### Key Features")
st.markdown(
    "- Temperature prediction and thermal trend analysis\n"
    "- Bisection and Newton-Raphson methods\n"
    "- HVAC control logic and insulation study\n"
    "- Multi-room simulation\n"
    "- CSV-based validation and reporting"
)

st.metric("Demo Initial Temperature", f"{DEFAULT_DEMO['initial_temperature']}°C")
st.metric("Demo Target Temperature", f"{DEFAULT_DEMO['target_temperature']}°C")
st.metric("Simulation Duration", f"{DEFAULT_DEMO['simulation_duration']} hours")
