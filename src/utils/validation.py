from __future__ import annotations

import math

import numpy as np
import pandas as pd


def validate_temperature(value: float, name: str) -> float:
    if value is None or not np.isfinite(float(value)):
        raise ValueError(f"{name} must be a finite number.")
    return float(value)


def validate_positive(name: str, value: float, allow_zero: bool = False) -> float:
    numeric = float(value)
    if not np.isfinite(numeric):
        raise ValueError(f"{name} must be finite.")
    if allow_zero:
        if numeric < 0:
            raise ValueError(f"{name} must be non-negative.")
    elif numeric <= 0:
        raise ValueError(f"{name} must be positive.")
    return numeric


def validate_timestep(value: float) -> float:
    return validate_positive("time step", value)


def validate_duration(value: float) -> float:
    return validate_positive("simulation duration", value)


def validate_index(value: int) -> int:
    if not isinstance(value, (int, np.integer)) or value < 0:
        raise ValueError("Index must be a non-negative integer.")
    return int(value)


def validate_csv_upload(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("Uploaded CSV is empty.")
    missing = {col for col in ["time", "temperature"] if col not in df.columns}
    if missing:
        raise ValueError(f"CSV is missing required columns: {sorted(missing)}")
    if df[["time", "temperature"]].isnull().any().any():
        raise ValueError("CSV contains missing values in required columns.")
    if not np.isfinite(df["time"]).all() or not np.isfinite(df["temperature"]).all():
        raise ValueError("CSV contains non-finite values.")
