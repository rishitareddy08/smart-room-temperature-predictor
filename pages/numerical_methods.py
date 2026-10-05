from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.models.thermal_model import ThermalModelConfig, simulate_thermal_system
from src.utils.constants import DEFAULT_DEMO
from src.utils.styling import apply_theme

apply_theme()

st.title("Temperature Simulator")

config = DEFAULT_DEMO.copy()

with st.form("simulation_form"):
    col1, col2 = st.columns(2)
    with col1:
        initial_temp = st.number_input("Initial temperature (°C)", value=config["initial_temperature"], min_value=-20.0, max_value=60.0, step=0.5)
        outdoor_temp = st.number_input("Outdoor temperature (°C)", value=config["outdoor_temperature"], min_value=-30.0, max_value=60.0, step=0.5)
        target_temp = st.number_input("Target temperature (°C)", value=config["target_temperature"], min_value=-20.0, max_value=60.0, step=0.5)
        room_area = st.number_input("Room area (m²)", value=config["room_area"], min_value=1.0, max_value=200.0, step=0.5)
        heat_coeff = st.number_input("Heat-transfer coefficient", value=config["heat_transfer_coefficient"], min_value=0.01, max_value=2.0, step=0.01)
        thermal_cap = st.number_input("Thermal capacitance", value=config["thermal_capacitance"], min_value=50.0, max_value=5000.0, step=10.0)
    with col2:
        duration = st.number_input("Simulation duration (hours)", value=config["simulation_duration"], min_value=1.0, max_value=168.0, step=1.0)
        time_step = st.number_input("Time step (hours)", value=config["time_step"], min_value=0.1, max_value=2.0, step=0.1)
        insulation_level = st.selectbox("Insulation", ["Poor", "Medium", "Good"], index=1)
        outdoor_mode = st.selectbox("Outdoor temperature model", ["Constant", "Daily Variation"], index=0)
        hvac_mode = st.selectbox("HVAC", ["OFF", "Automatic", "Cooling", "Heating"], index=1)
        hvac_capacity = st.number_input("HVAC capacity", value=config["hvac_capacity"], min_value=100.0, max_value=6000.0, step=50.0)
        deadband = st.number_input("Deadband (°C)", value=config["deadband"], min_value=0.1, max_value=5.0, step=0.1)
        internal_gain = st.number_input("Internal heat gain", value=config["internal_heat_gain"], min_value=0.0, max_value=3000.0, step=25.0)
        solar_gain = st.number_input("Solar heat gain", value=config["solar_heat_gain"], min_value=0.0, max_value=3000.0, step=25.0)

    run_clicked = st.form_submit_button("Run Simulation")
    reset_clicked = st.form_submit_button("Reset")
    demo_clicked = st.form_submit_button("Load Demo")

if demo_clicked:
    st.session_state.simulation_config = DEFAULT_DEMO.copy()
    st.rerun()

if reset_clicked:
    st.session_state.simulation_config = DEFAULT_DEMO.copy()
    st.rerun()

if run_clicked:
    model_config = ThermalModelConfig(
        initial_temperature=initial_temp,
        outdoor_temperature=outdoor_temp,
        target_temperature=target_temp,
        room_area=room_area,
        heat_transfer_coefficient=heat_coeff,
        thermal_capacitance=thermal_cap,
        simulation_duration=duration,
        time_step=time_step,
        insulation_level=insulation_level,
        hvac_mode=hvac_mode,
        hvac_capacity=hvac_capacity,
        deadband=deadband,
        internal_heat_gain=internal_gain,
        solar_heat_gain=solar_gain,
        outdoor_mode=outdoor_mode,
        mean_temperature=outdoor_temp,
        amplitude=max(0.0, abs(outdoor_temp - target_temp) * 0.25),
        phase=0.0,
    )
    result = simulate_thermal_system(model_config)
    st.session_state.simulation_result = result
    st.session_state.simulation_config = model_config.__dict__

if "simulation_result" not in st.session_state:
    st.session_state.simulation_result = simulate_thermal_system(DEFAULT_DEMO)
    st.session_state.simulation_config = DEFAULT_DEMO.copy()

result = st.session_state.simulation_result

st.subheader("Simulation Result")
fig = px.line(result, x="time_hours", y=["indoor_temp", "outdoor_temp", "target_temp"], title="Indoor vs Outdoor vs Target Temperature")
fig.update_layout(template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

st.dataframe(result.tail(10), use_container_width=True)
