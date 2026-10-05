from __future__ import annotations

from typing import Tuple


def thermostat_state(
    current_temperature: float,
    target_temperature: float,
    deadband: float,
    hvac_mode: str,
    hvac_capacity: float,
) -> Tuple[float, str]:
    if hvac_mode == "OFF":
        return 0.0, "OFF"

    if hvac_mode == "Cooling":
        return -hvac_capacity, "Cooling"

    if hvac_mode == "Heating":
        return hvac_capacity, "Heating"

    if current_temperature > target_temperature + deadband:
        return -hvac_capacity, "Cooling"
    if current_temperature < target_temperature - deadband:
        return hvac_capacity, "Heating"
    return 0.0, "OFF"


def hvac_status_label(current_temperature: float, target_temperature: float, deadband: float) -> str:
    if current_temperature > target_temperature + deadband:
        return "Cooling Required"
    if current_temperature < target_temperature - deadband:
        return "Heating Required"
    return "Comfort Range"
