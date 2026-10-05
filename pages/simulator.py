from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.models.thermal_model import simulate_thermal_system
from src.utils.constants import DEFAULT_DEMO
from src.utils.styling import apply_theme

apply_theme()

st.title("Dashboard")

if "simulation_config" not in st.session_state:
    st.session_state.simulation_config = DEFAULT_DEMO.copy()

if st.button("Run Demo Simulation"):
    st.session_state.simulation_result = simulate_thermal_system(st.session_state.simulation_config)

if "simulation_result" not in st.session_state:
    st.session_state.simulation_result = simulate_thermal_system(st.session_state.simulation_config)

result = st.session_state.simulation_result

col1, col2, col3, col4 = st.columns(4)
col1.metric("Current Indoor Temp", f"{result['indoor_temp'].iloc[-1]:.2f}°C")
col2.metric("Outdoor Temp", f"{result['outdoor_temp'].iloc[-1]:.2f}°C")
col3.metric("Target Temp", f"{st.session_state.simulation_config['target_temperature']:.2f}°C")
col4.metric("HVAC Status", result["hvac_status"].iloc[-1])

fig = px.line(result, x="time_hours", y=["indoor_temp", "outdoor_temp", "target_temp"], title="Temperature Profile")
fig.update_layout(template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

hvac_fig = px.line(result, x="time_hours", y="hvac_status", title="HVAC Status")
hvac_fig.update_layout(template="plotly_dark")
st.plotly_chart(hvac_fig, use_container_width=True)

st.subheader("System Status")
if result["indoor_temp"].iloc[-1] > st.session_state.simulation_config["target_temperature"] + st.session_state.simulation_config["deadband"]:
    st.warning("Cooling Required")
elif result["indoor_temp"].iloc[-1] < st.session_state.simulation_config["target_temperature"] - st.session_state.simulation_config["deadband"]:
    st.warning("Heating Required")
else:
    st.success("Comfort Range")

st.dataframe(result.tail(10), use_container_width=True)
