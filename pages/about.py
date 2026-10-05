from __future__ import annotations

import pandas as pd
import streamlit as st

from src.utils.constants import DEFAULT_DEMO
from src.utils.styling import apply_theme

apply_theme()

st.title("Reports")

report = {
    "Project title": "Smart Room Temperature Predictor",
    "Simulation date": "2026-10-05",
    "Input parameters": DEFAULT_DEMO,
    "Building parameters": {
        "Room area": DEFAULT_DEMO["room_area"],
        "Insulation": DEFAULT_DEMO["insulation_level"],
    },
    "Outdoor model": DEFAULT_DEMO["outdoor_mode"],
    "HVAC": DEFAULT_DEMO["hvac_mode"],
    "Numerical method": "Bisection + Newton-Raphson",
    "Target time": 8.0,
    "Final temperature": 24.5,
    "Energy estimate": 2.4,
    "Errors": "To be generated from simulation data.",
}

st.json(report)

if st.button("Download CSV"):
    df = pd.DataFrame({"time_hours": [0, 1, 2], "temperature": [DEFAULT_DEMO["initial_temperature"], 29.0, 26.0]})
    st.download_button("Download", df.to_csv(index=False), file_name="simulation_report.csv", mime="text/csv")

if st.button("Download Simulation Data"):
    df = pd.DataFrame({"time_hours": [0, 1, 2], "indoor_temp": [32.0, 29.0, 26.0]})
    st.download_button("Download", df.to_csv(index=False), file_name="simulation_data.csv", mime="text/csv")
