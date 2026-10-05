import numpy as np

from src.models.thermal_model import ThermalModelConfig, analytical_solution, simulate_thermal_system


def test_initial_condition():
    config = ThermalModelConfig(
        initial_temperature=30.0,
        outdoor_temperature=25.0,
        target_temperature=24.0,
        room_area=20.0,
        heat_transfer_coefficient=0.12,
        thermal_capacitance=1800.0,
        simulation_duration=4.0,
        time_step=0.5,
        hvac_mode="OFF",
    )
    result = simulate_thermal_system(config)
    assert result["indoor_temp"].iloc[0] == 30.0


def test_analytical_solution():
    value = analytical_solution(1.0, 30.0, 20.0, 0.5)
    assert value > 20.0
    assert value < 30.0


def test_constant_outdoor_temperature():
    config = ThermalModelConfig(
        initial_temperature=32.0,
        outdoor_temperature=38.0,
        target_temperature=24.0,
        room_area=20.0,
        heat_transfer_coefficient=0.12,
        thermal_capacitance=1800.0,
        simulation_duration=12.0,
        time_step=1.0,
        hvac_mode="OFF",
    )
    result = simulate_thermal_system(config)
    assert result["outdoor_temp"].iloc[0] == 38.0
    assert result["outdoor_temp"].iloc[-1] == 38.0
