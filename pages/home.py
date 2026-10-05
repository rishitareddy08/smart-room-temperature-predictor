from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from src.utils.validation import validate_csv_upload
from src.utils.metrics import mae, rmse, relative_error


def load_uploaded_csv(file_obj) -> pd.DataFrame:
    if file_obj is None:
        raise ValueError("No CSV file uploaded.")
    df = pd.read_csv(file_obj)
    validate_csv_upload(df)
    return df


def calculate_actual_vs_predicted(actual_df: pd.DataFrame, predicted_df: pd.DataFrame) -> pd.DataFrame:
    merged = actual_df[["time", "temperature"]].merge(predicted_df[["time", "temperature"]], on="time", how="inner", suffixes=("_actual", "_predicted"))
    merged["absolute_error"] = (merged["temperature_actual"] - merged["temperature_predicted"]).abs()
    merged["relative_error_percent"] = (merged["absolute_error"] / merged["temperature_actual"].abs().replace(0, np.nan)).fillna(0.0) * 100.0
    merged["mae"] = mae(merged["temperature_actual"].to_numpy(), merged["temperature_predicted"].to_numpy())
    merged["rmse"] = rmse(merged["temperature_actual"].to_numpy(), merged["temperature_predicted"].to_numpy())
    return merged


def summarize_data_analysis(actual_df: pd.DataFrame, predicted_df: pd.DataFrame) -> dict:
    merged = calculate_actual_vs_predicted(actual_df, predicted_df)
    return {
        "dataframe": merged,
        "mae": float(merged["mae"].iloc[0]),
        "rmse": float(merged["rmse"].iloc[0]),
        "max_absolute_error": float(merged["absolute_error"].max()),
    }
