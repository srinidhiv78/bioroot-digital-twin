import streamlit as st

st.set_page_config(
    page_title="BIOROOT Digital Twin",
    page_icon="🌱",
    layout="wide"
)

# ---------- HEADER ----------

st.title("🌱 BIOROOT")
st.subheader("AI-Enabled Digital Twin for Circular Wastewater Treatment")

st.info(
    "Prototype digital twin — model predictions currently based on "
    "demonstration data and require experimental calibration."
)

st.markdown("---")

# ---------- INDUSTRY INPUT ----------

st.header("🏭 Industrial System Inputs")

st.write(
    "Enter the existing wastewater-system parameters. "
    "BIOROOT will use these inputs to recommend a treatment architecture."
)

col1, col2 = st.columns(2)

with col1:
    pipe_diameter = st.number_input(
        "Existing pipe diameter (mm)",
        min_value=20.0,
        max_value=2000.0,
        value=150.0,
        step=10.0
    )

    pipe_length = st.number_input(
        "Available pipe length (m)",
        min_value=1.0,
        max_value=500.0,
        value=20.0,
        step=1.0
    )

with col2:
    flow_rate = st.number_input(
        "Wastewater flow rate (L/min)",
        min_value=1.0,
        max_value=10000.0,
        value=50.0,
        step=5.0
    )

    application = st.selectbox(
        "Wastewater application",
        [
            "Laboratory wastewater",
            "Pharmaceutical wastewater",
            "Biotechnology industry",
            "Food-processing wastewater",
            "Municipal wastewater"
        ]
    )

treatment_priority = st.selectbox(
    "Primary treatment priority",
    [
        "Balanced treatment",
        "Maximum phosphate removal",
        "Maximum dye removal",
        "Minimum material requirement"
    ]
)

st.markdown("---")

# ---------- ACTION ----------

if st.button("⚙️ Generate AI Treatment Design", use_container_width=True):

    st.header("🧠 BIOROOT AI Design Recommendation")

    # Simple prototype logic
    if treatment_priority == "Maximum phosphate removal":
        alginate = 35
        sargassum = 35
        eggshell = 20
        plastic = 10
        branches = 8
        bead_size = 10
        phosphate_removal = 86
        dye_removal = 68

    elif treatment_priority == "Maximum dye removal":
        alginate = 40
        sargassum = 35
        eggshell = 15
        plastic = 10
        branches = 7
        bead_size = 8
        phosphate_removal = 72
        dye_removal = 88

    elif treatment_priority == "Minimum material requirement":
        alginate = 40
        sargassum = 30
        eggshell = 20
        plastic = 10
        branches = 5
        bead_size = 8
        phosphate_removal = 68
        dye_removal = 70

    else:
        alginate = 38
        sargassum = 32
        eggshell = 20
        plastic = 10
        branches = 6
        bead_size = 9
        phosphate_removal = 78
        dye_removal = 80

    # ---------- PERFORMANCE METRICS ----------

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Predicted phosphate removal", f"{phosphate_removal}%")
    m2.metric("Predicted dye removal", f"{dye_removal}%")
    m3.metric("Recommended branches", branches)
    m4.metric("Bead diameter", f"{bead_size} mm")

    st.markdown("---")

    # ---------- MATERIAL FORMULATION ----------

    st.subheader("🧪 Recommended Bead Formulation")

    formulation_col1, formulation_col2 = st.columns(2)

    with formulation_col1:
        st.write("**Composite formulation**")
        st.write(f"• Sodium alginate: **{alginate}%**")
        st.write(f"• *Sargassum tenerrimum*: **{sargassum}%**")
        st.write(f"• Eggshell powder: **{eggshell}%**")
        st.write(f"• Recycled polypropylene: **{plastic}%**")

    with formulation_col2:
        st.write("**Recommended architecture**")
        st.write(f"• Branch count: **{branches}**")
        st.write(f"• Bead diameter: **{bead_size} mm**")
        st.write("• Root-inspired branched configuration")
        st.write("• Recycled PP provides structural reinforcement")

    st.markdown("---")

    # ---------- DIGITAL TWIN ----------

    st.subheader("🔄 Digital Twin Simulation")

    st.write(
        "The virtual treatment system mirrors the proposed physical "
        "bead-and-pipe configuration and provides a prototype prediction "
        "of treatment performance."
    )

    twin1, twin2, twin3 = st.columns(3)

    twin1.metric("Pipe diameter", f"{pipe_diameter:.0f} mm")
    twin2.metric("Flow rate", f"{flow_rate:.0f} L/min")
    twin3.metric("Available length", f"{pipe_length:.0f} m")

    st.success(
        "Digital twin status: CONFIGURATION GENERATED"
    )

    st.caption(
        "Prototype prediction only. Performance values require calibration "
        "using experimental wastewater-treatment data."
    )
