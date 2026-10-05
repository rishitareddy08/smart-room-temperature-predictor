from __future__ import annotations

import numpy as np
import pandas as pd

from src.models.thermal_model import ThermalModelConfig, analytical_solution, outdoor_temperature_at_time


def solve_room_ode(config: ThermalModelConfig | dict):
    if isinstance(config, dict):
        config = ThermalModelConfig(**config)

    time_values = np.linspace(0.0, config.simulation_duration, int(round(config.simulation_duration / config.time_step)) + 1)
    analytical = []
    for t in time_values:
        outdoor = outdoor_temperature_at_time(
            t,
            config.outdoor_mode,
            config.outdoor_temperature,
            config.mean_temperature,
            config.amplitude,
            config.phase,
        )
        analytical.append(analytical_solution(t, config.initial_temperature, outdoor, 0.08))

    def model_rhs(t, temp):
        ua = config.room_area * config.heat_transfer_coefficient
        return (ua * (outdoor_temperature_at_time(t, config.outdoor_mode, config.outdoor_temperature, config.mean_temperature, config.amplitude, config.phase) - temp) + config.internal_heat_gain + config.solar_heat_gain) / config.thermal_capacitance

    # Euler
    euler = [config.initial_temperature]
    for i in range(1, len(time_values)):
        value = euler[-1] + model_rhs(time_values[i - 1], euler[-1]) * config.time_step
        euler.append(value)

    # RK4
    rk4 = [config.initial_temperature]
    for i in range(1, len(time_values)):
        xi = time_values[i - 1]
        yi = rk4[-1]
        h = config.time_step
        k1 = model_rhs(xi, yi)
        k2 = model_rhs(xi + 0.5 * h, yi + 0.5 * h * k1)
        k3 = model_rhs(xi + 0.5 * h, yi + 0.5 * h * k2)
        k4 = model_rhs(xi + h, yi + h * k3)
        next_y = yi + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        rk4.append(next_y)

    results = pd.DataFrame({
        "time_hours": time_values,
        "analytical": analytical,
        "euler": euler,
        "rk4": rk4,
        "euler_error": np.abs(np.array(analytical) - np.array(euler)),
        "rk4_error": np.abs(np.array(analytical) - np.array(rk4)),
    })
    return results
