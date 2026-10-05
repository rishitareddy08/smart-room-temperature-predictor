from __future__ import annotations

import pandas as pd

from src.models.thermal_model import ThermalModelConfig, simulate_thermal_system


def run_simulation(config: ThermalModelConfig | dict) -> dict:
    if isinstance(config, dict):
        config = ThermalModelConfig(**config)
    df = simulate_thermal_system(config)
    target_hit = df[df["indoor_temp"] <= config.target_temperature]
    time_to_target = None if target_hit.empty else float(target_hit["time_hours"].iloc[0])
    summary = {
        "dataframe": df,
        "time_to_target": time_to_target,
        "final_temperature": float(df["indoor_temp"].iloc[-1]),
        "hvac_status": str(df["hvac_status"].iloc[-1]),
    }
    return summary
