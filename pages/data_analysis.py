from __future__ import annotations

import plotly.express as px
import streamlit as st

from src.simulation.multi_room import simulate_multi_room
from src.utils.styling import apply_theme

apply_theme()

st.title("Multi-Room Simulation")

room_defaults = [
    {"name": "Living Room", "initial_temperature": 30.0, "target_temperature": 24.0, "room_area": 25.0, "heat_transfer_coefficient": 0.12, "thermal_capacitance": 2200.0, "insulation": "Medium", "hvac_mode": "Automatic", "hvac_capacity": 2000.0},
    {"name": "Bedroom", "initial_temperature": 28.0, "target_temperature": 22.0, "room_area": 18.0, "heat_transfer_coefficient": 0.10, "thermal_capacitance": 1800.0, "insulation": "Good", "hvac_mode": "Automatic", "hvac_capacity": 1500.0},
    {"name": "Office", "initial_temperature": 31.0, "target_temperature": 23.5, "room_area": 20.0, "heat_transfer_coefficient": 0.14, "thermal_capacitance": 1900.0, "insulation": "Poor", "hvac_mode": "Automatic", "hvac_capacity": 1800.0},
]

rooms = []
for room in room_defaults:
    rooms.append(room)

if room_defaults:
    result = simulate_multi_room(rooms, duration_hours=24.0, time_step=0.5)
    if not result.empty:
        fig = px.line(result, x="time_hours", y="indoor_temp", color="room_name", title="Room Temperatures over Time")
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(result.tail(20), use_container_width=True)
