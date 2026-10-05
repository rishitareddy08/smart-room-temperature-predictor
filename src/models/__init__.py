from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd

from src.models.hvac import thermostat_state


@dataclass
class ThermalModelConfig:
    initial_temperature: float
    outdoor_temperature: float
    target_temperature: float
    room_area: float
    heat_transfer_coefficient: float
    thermal_capacitance: float
    simulation_duration: float
    time_step: float
    insulation_level: str = "Medium"
    hvac_mode: str = "Automatic"
    hvac_capacity: float = 2500.0
    deadband: float = 1.0
    internal_heat_gain: float = 300.0
    solar_heat_gain: float = 200.0
    outdoor_mode: str = "Constant"
    mean_temperature: float = 25.0
    amplitude: float = 6.0
    phase: float = 0.0


def outdoor_temperature_at_time(
    time_value: float,
    mode: str = "Constant",
    constant_temp: float = 25.0,
    mean_temp: float = 25.0,
    amplitude: float = 6.0,
    phase: float = 0.0,
) -> float:
    if mode == "Daily Variation":
        return mean_temp + amplitude * np.sin(0.26 * time_value + phase)
    return constant_temp


def compute_ua(room_area: float, heat_transfer_coefficient: float) -> float:
    return max(room_area * heat_transfer_coefficient, 1e-6)


def analytical_solution(time_value: float, initial_temp: float, outdoor_temp: float, k: float) -> float:
    return outdoor_temp + (initial_temp - outdoor_temp) * np.exp(-k * time_value)


def thermal_rhs(time_value: float, temperature: float, config: ThermalModelConfig) -> float:
    ua = compute_ua(config.room_area, config.heat_transfer_coefficient)
    outdoor = outdoor_temperature_at_time(
        time_value,
        config.outdoor_mode,
        constant_temp=config.outdoor_temperature,
        mean_temp=config.mean_temperature,
        amplitude=config.amplitude,
        phase=config.phase,
    )
    hvac_effect, hvac_status = thermostat_state(
        temperature,
        config.target_temperature,
        config.deadband,
        config.hvac_mode,
        config.hvac_capacity,
    )
    net_heat = ua * (outdoor - temperature) + hvac_effect + config.internal_heat_gain + config.solar_heat_gain
    return net_heat / config.thermal_capacitance


def simulate_thermal_system(config: ThermalModelConfig | dict | None) -> pd.DataFrame:
    if config is None:
        config = ThermalModelConfig(initial_temperature=30.0, outdoor_temperature=25.0, target_temperature=24.0, room_area=20.0,
                                     heat_transfer_coefficient=0.12, thermal_capacitance=1800.0, simulation_duration=12.0,
                                     time_step=0.5, insulation_level="Medium", hvac_mode="Automatic", hvac_capacity=2000.0,
                                     deadband=1.0, internal_heat_gain=250.0, solar_heat_gain=150.0, outdoor_mode="Constant",
                                     mean_temperature=25.0, amplitude=6.0, phase=0.0)
    if isinstance(config, dict):
        config = ThermalModelConfig(**config)

    steps = int(max(1, round(config.simulation_duration / config.time_step))) + 1
    time_values = np.linspace(0.0, config.simulation_duration, steps)
    indoor = np.empty_like(time_values, dtype=float)
    outdoor = np.empty_like(time_values, dtype=float)
    hvac_status = ["OFF"] * len(time_values)
    hvac_effects = np.zeros_like(time_values, dtype=float)

    indoor[0] = config.initial_temperature

    for idx in range(1, len(time_values)):
        current_t = time_values[idx - 1]
        current_temp = indoor[idx - 1]
        outdoor[idx - 1] = outdoor_temperature_at_time(
            current_t,
            config.outdoor_mode,
            constant_temp=config.outdoor_temperature,
            mean_temp=config.mean_temperature,
            amplitude=config.amplitude,
            phase=config.phase,
        )
        hvac_effect, status = thermostat_state(
            current_temp,
            config.target_temperature,
            config.deadband,
            config.hvac_mode,
            config.hvac_capacity,
        )
        hvac_effects[idx - 1] = hvac_effect
        hvac_status[idx - 1] = status

        derivative = thermal_rhs(current_t, current_temp, config)
        indoor[idx] = current_temp + derivative * config.time_step

    outdoor[-1] = outdoor_temperature_at_time(
        time_values[-1],
        config.outdoor_mode,
        constant_temp=config.outdoor_temperature,
        mean_temp=config.mean_temperature,
        amplitude=config.amplitude,
        phase=config.phase,
    )
    hvac_effect, status = thermostat_state(
        indoor[-1],
        config.target_temperature,
        config.deadband,
        config.hvac_mode,
        config.hvac_capacity,
    )
    hvac_status[-1] = status
    hvac_effects[-1] = hvac_effect

    df = pd.DataFrame({
        "time_hours": time_values,
        "indoor_temp": indoor,
        "outdoor_temp": outdoor,
        "target_temp": config.target_temperature,
        "hvac_status": hvac_status,
        "hvac_effect": hvac_effects,
    })
    return df


def compare_insulation_scenarios(base_config: ThermalModelConfig | dict) -> pd.DataFrame:
    if isinstance(base_config, dict):
        base_config = ThermalModelConfig(**base_config)
    insulation_levels = {
        "Poor": 1.8,
        "Medium": 1.0,
        "Good": 0.55,
    }
    rows = []
    for label, multiplier in insulation_levels.items():
        cfg = ThermalModelConfig(**base_config.__dict__)
        cfg.heat_transfer_coefficient = base_config.heat_transfer_coefficient * multiplier
        cfg.insulation_level = label
        result = simulate_thermal_system(cfg)
        rows.append({
            "insulation": label,
            "final_temperature": float(result["indoor_temp"].iloc[-1]),
            "time_to_target": float(result.loc[result["indoor_temp"] <= cfg.target_temperature, "time_hours"].min()) if (result["indoor_temp"] <= cfg.target_temperature).any() else None,
            "average_outdoor": float(result["outdoor_temp"].mean()),
        })
    return pd.DataFrame(rows)
