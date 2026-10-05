from __future__ import annotations

import numpy as np
import pandas as pd

from src.models.thermal_model import ThermalModelConfig, outdoor_temperature_at_time, thermal_rhs


def estimate_energy_kwh(hvac_capacity: float, operating_hours: float, cop: float = 3.0) -> float:
    if cop <= 0:
        raise ValueError("COP must be positive.")
    return float((hvac_capacity * operating_hours) / (1000.0 * cop))


def insulation_coefficient(level: str) -> float:
    mapping = {"Poor": 1.8, "Medium": 1.0, "Good": 0.55}
    level_name = level.capitalize()
    if level_name not in mapping:
        raise ValueError("Insulation level must be Poor, Medium, or Good.")
    return float(mapping[level_name])


def compare_insulation(base_config: ThermalModelConfig | dict) -> pd.DataFrame:
    if isinstance(base_config, dict):
        base_config = ThermalModelConfig(**base_config)

    rows = []
    for label in ["Poor", "Medium", "Good"]:
        cfg = ThermalModelConfig(**base_config.__dict__)
        cfg.insulation_level = label
        cfg.heat_transfer_coefficient = max(base_config.heat_transfer_coefficient * insulation_coefficient(label), 1e-3)
        result = simulate_thermal_system(cfg)
        rows.append({
            "insulation": label,
            "final_temperature": float(result["indoor_temp"].iloc[-1]),
            "time_to_target": float(result.loc[result["indoor_temp"] <= cfg.target_temperature, "time_hours"].min()) if (result["indoor_temp"] <= cfg.target_temperature).any() else None,
        })
    return pd.DataFrame(rows)
