from __future__ import annotations

import numpy as np
import pandas as pd

from src.models.thermal_model import ThermalModelConfig, simulate_thermal_system


def simulate_multi_room(room_configs: list[dict], duration_hours: float = 24.0, time_step: float = 0.5) -> pd.DataFrame:
    frames = []
    for room in room_configs:
        cfg = ThermalModelConfig(**{
            "initial_temperature": room["initial_temperature"],
            "outdoor_temperature": room.get("outdoor_temperature", 30.0),
            "target_temperature": room["target_temperature"],
            "room_area": room["room_area"],
            "heat_transfer_coefficient": room["heat_transfer_coefficient"],
            "thermal_capacitance": room["thermal_capacitance"],
            "simulation_duration": duration_hours,
            "time_step": time_step,
            "insulation_level": room.get("insulation", "Medium"),
            "hvac_mode": room.get("hvac_mode", "Automatic"),
            "hvac_capacity": room.get("hvac_capacity", 1500.0),
            "deadband": room.get("deadband", 1.0),
            "internal_heat_gain": room.get("internal_heat_gain", 200.0),
            "solar_heat_gain": room.get("solar_heat_gain", 150.0),
            "outdoor_mode": room.get("outdoor_mode", "Constant"),
            "mean_temperature": room.get("mean_temperature", 24.0),
            "amplitude": room.get("amplitude", 5.0),
            "phase": room.get("phase", 0.0),
        })
        sim = simulate_thermal_system(cfg)
        sim["room_name"] = room["name"]
        sim["target_temperature"] = room["target_temperature"]
        frames.append(sim)

    if not frames:
        return pd.DataFrame()

    return pd.concat(frames, ignore_index=True)
