
import streamlit as st

st.set_page_config(
    page_title="BIOROOT Digital Twin",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 BIOROOT")
st.subheader("AI-Enabled Digital Twin for Circular Wastewater Treatment")

st.info(
    "Prototype digital twin — model predictions currently based on "
    "demonstration data and require experimental calibration."
)

st.write("Welcome to the BIOROOT treatment-system design platform.")

st.success("Application setup successful!")
