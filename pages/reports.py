from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

from src.simulation.multi_room import load_uploaded_csv, summarize_data_analysis
from src.utils.styling import apply_theme

apply_theme()

st.title("Data Analysis")

uploaded = st.file_uploader("Upload temperature CSV", type=["csv"])
if uploaded is not None:
    try:
        actual = load_uploaded_csv(uploaded)
        st.success("CSV uploaded and validated successfully.")
        predicted = pd.read_csv("data/sample_temperature.csv")
        summary = summarize_data_analysis(actual, predicted)
        st.metric("MAE", f"{summary['mae']:.4f}")
        st.metric("RMSE", f"{summary['rmse']:.4f}")
        st.metric("Max Absolute Error", f"{summary['max_absolute_error']:.4f}")

        merged = summary["dataframe"]
        fig = px.line(merged, x="time", y=["temperature_actual", "temperature_predicted"], title="Actual vs Predicted Temperature")
        fig.update_layout(template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(merged, use_container_width=True)
    except ValueError as exc:
        st.error(str(exc))
else:
    st.info("Upload a CSV file with columns: time and temperature.")
    sample = pd.read_csv("data/sample_temperature.csv")
    st.dataframe(sample, use_container_width=True)
