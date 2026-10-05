from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.models.thermal_model import ThermalModelConfig, compare_insulation_scenarios
from src.models.building import estimate_energy_kwh
from src.utils.constants import DEFAULT_DEMO
from src.utils.styling import apply_theme

apply_theme()

st.title("Building Analysis")

base = DEFAULT_DEMO.copy()
base_config = ThermalModelConfig(**base)
comparison = compare_insulation_scenarios(base_config)

st.subheader("Insulation Comparison")
fig = px.bar(comparison, x="insulation", y="final_temperature", color="insulation", title="Final Temperature by Insulation Level")
fig.update_layout(template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Energy Estimation")
capacity = st.number_input("HVAC capacity", value=1500.0, min_value=100.0, max_value=5000.0, step=50.0)
operating_hours = st.number_input("Operating hours", value=8.0, min_value=1.0, max_value=24.0, step=1.0)
cop = st.number_input("COP / Efficiency", value=3.0, min_value=1.0, max_value=10.0, step=0.5)
energy = estimate_energy_kwh(capacity, operating_hours, cop)
st.info(f"Estimated energy: {energy:.2f} kWh")
st.caption("Energy calculation is an educational approximation and is not a substitute for professional HVAC energy modelling.")

st.dataframe(comparison, use_container_width=True)
