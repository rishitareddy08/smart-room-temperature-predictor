import streamlit as st

from src.utils.constants import DEFAULT_DEMO
from src.utils.styling import apply_theme
from src.models.thermal_model import simulate_thermal_system

apply_theme()

st.set_page_config(
    page_title="Smart Room Temperature Predictor",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("SMARTTEMP")
st.sidebar.caption("Numerical intelligence for understanding indoor thermal behavior.")

st.sidebar.page_link("app.py", label="🏠 Home", icon="🏠")
st.sidebar.page_link("pages/dashboard.py", label="📊 Dashboard", icon="📊")
st.sidebar.page_link("pages/simulator.py", label="🌡️ Simulator", icon="🌡️")
st.sidebar.page_link("pages/numerical_methods.py", label="🧮 Numerical Methods", icon="🧮")
st.sidebar.page_link("pages/building_analysis.py", label="🏢 Building Analysis", icon="🏢")
st.sidebar.page_link("pages/multi_room.py", label="🏠 Multi-Room", icon="🏠")
st.sidebar.page_link("pages/data_analysis.py", label="📈 Data Analysis", icon="📈")
st.sidebar.page_link("pages/reports.py", label="📄 Reports", icon="📄")
st.sidebar.page_link("pages/about.py", label="ℹ️ About", icon="ℹ️")

st.markdown(
    """
    <div style='text-align:center; padding:1.5rem 0 1rem 0;'>
        <h1 style='color:#E5E7EB; margin-bottom:0.2rem;'>Smart Room Temperature Predictor</h1>
        <p style='color:#94A3B8; font-size:1.1rem; margin-top:0;'>Numerical intelligence for understanding indoor thermal behavior.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Run demo automatically if available
if "demo_result" not in st.session_state:
    st.session_state.demo_result = simulate_thermal_system(DEFAULT_DEMO)

cols = st.columns(2)
with cols[0]:
    st.subheader("Smart Building Heat Transfer Simulation")
    st.write(
        "Simulate room temperature, compare numerical methods, analyze insulation, and evaluate HVAC behavior using a simplified yet educational thermal model."
    )
    if st.button("Launch Simulator", use_container_width=True):
        st.switch_page("pages/simulator.py")
    if st.button("Explore Numerical Methods", use_container_width=True):
        st.switch_page("pages/numerical_methods.py")

with cols[1]:
    st.subheader("Demo Result")
    res = st.session_state.demo_result
    st.metric("Current Indoor Temp", f"{res['indoor_temp'].iloc[-1]:.2f}°C")
    st.metric("Outdoor Temp", f"{res['outdoor_temp'].iloc[-1]:.2f}°C")
    st.metric("Target Temp", f"{DEFAULT_DEMO['target_temperature']}°C")
    st.metric("HVAC State", res["hvac_status"].iloc[-1])

st.markdown("### Key Features")
feature_cols = st.columns(6)
features = [
    ("🌡️", "Temperature Prediction", "Estimate indoor thermal response over time."),
    ("🧮", "Numerical Methods", "Bisection and Newton-Raphson are implemented manually."),
    ("❄️", "HVAC Analysis", "Cooling and heating behavior are modelled intelligently."),
    ("🏢", "Building Analysis", "Evaluate insulation, exposure, and target conditions."),
    ("📈", "Data Analysis", "Compare actual temperatures with predicted trends."),
    ("🏠", "Multi-Room Simulation", "Model multiple rooms simultaneously."),
]
for i, (icon, title, description) in enumerate(features):
    with feature_cols[i]:
        st.markdown(f"""
        <div style='padding:1rem; border-radius:1rem; background:#111827; border:1px solid rgba(148,163,184,0.15); min-height: 150px;'>
            <div style='font-size:2rem;'>{icon}</div>
            <h4 style='margin:0.5rem 0 0.5rem 0; color:#E5E7EB;'>{title}</h4>
            <p style='color:#94A3B8; margin:0;'>{description}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("### How It Works")
for idx, step in enumerate([
    "Enter building parameters",
    "Build mathematical model",
    "Apply numerical methods",
    "Analyze and visualize results",
    "Generate report",
], start=1):
    st.markdown(f"**STEP {idx}:** {step}")

st.markdown("### Numerical Methods")
col_a, col_b, col_c = st.columns(3)
with col_a:
    st.info("Bisection Method\nFinds a root inside a valid interval by repeatedly narrowing the bracket.")
with col_b:
    st.info("Newton-Raphson\nUses the derivative to accelerate convergence toward the solution.")
with col_c:
    st.info("RK4 / Euler\nSolve the thermal differential equation numerically and compare it with the analytical result.")

st.markdown("### Project Statistics")
stat_cols = st.columns(4)
with stat_cols[0]:
    st.metric("Rooms", "3 default")
with stat_cols[1]:
    st.metric("Methods", "4")
with stat_cols[2]:
    st.metric("Charts", "Interactive")
with stat_cols[3]:
    st.metric("Goal", "Comfort prediction")

st.markdown("### Real-world Applications")
st.write(
    "- Residential buildings\n"
    "- Smart classrooms and offices\n"
    "- Energy-conscious HVAC setpoint planning\n"
    "- Building envelope analysis and insulation review"
)

st.markdown("### Call to Action")
st.info("Use the simulator to evaluate your building conditions and generate an engineering-style thermal report.")

st.markdown("---")
st.caption("SMARTTEMP © 2026 • B.Tech Numerical Methods Mini Project")
