apply_theme = """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0B1120 0%, #111827 100%);
        color: #E5E7EB;
    }
    .stApp {
        background: #0B1120;
    }
    .stTabs [role="tablist"] button {
        background: #111827;
        color: #E5E7EB;
        border: 1px solid rgba(148,163,184,0.25);
        border-radius: 0.75rem;
        padding: 0.5rem 1rem;
    }
    .stMetric {
        background: #111827;
        border: 1px solid rgba(148,163,184,0.2);
        border-radius: 1rem;
        padding: 0.7rem;
    }
    .stDataFrame, .stTable {
        background: #0F172A;
    }
</style>
"""


def apply_theme() -> None:
    import streamlit as st

    st.markdown(apply_theme, unsafe_allow_html=True)
