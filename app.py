import streamlit as st
import pandas as pd
import math

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="BIOROOT | Digital Twin",
    page_icon="🌿",
    layout="wide"
)

# =================================================
# CUSTOM CSS
# =================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1 {
    font-size: 2.6rem !important;
    font-weight: 700 !important;
}

h2 {
    font-size: 2rem !important;
}

h3 {
    font-size: 1.35rem !important;
}

[data-testid="stMetricValue"] {
    font-size: 1.7rem;
}

[data-testid="stMetricLabel"] {
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# =================================================
# SESSION STATE
# =================================================

if "screen" not in st.session_state:
    st.session_state.screen = "Industry Portal"

if "initialized" not in st.session_state:
    st.session_state.initialized = False

if "facility_data" not in st.session_state:
    st.session_state.facility_data = {}

if "design_data" not in st.session_state:
    st.session_state.design_data = {}

# =================================================
# SIDEBAR NAVIGATION
# =================================================

st.sidebar.title("🌿 BIOROOT")

st.sidebar.caption(
    "AI-Enabled Circular Wastewater Treatment"
)

st.sidebar.markdown("---")

screens = [
    "Industry Portal",
    "Optimized Prediction",
    "Digital Twin Control Room",
    "Performance Analytics",
    "Scenario Simulator",
    "Regeneration & Lifecycle"
]

for screen_name in screens:

    if screen_name in ["Industry Portal", "Optimized Prediction"]:

        if st.sidebar.button(
            screen_name,
            use_container_width=True
        ):
            st.session_state.screen = screen_name

    else:

        st.sidebar.button(
            "🔒 " + screen_name,
            use_container_width=True,
            disabled=True
        )

# =================================================
# HEADER
# =================================================

st.title("🌿 BIOROOT")

st.caption(
    "AI-enabled digital twin for circular wastewater treatment "
    "using biofunctional composite beads and recycled laboratory plastics."
)

# =================================================
# INDUSTRY PORTAL
# =================================================

if st.session_state.screen == "Industry Portal":

    st.header("🏭 Industry Portal")

    st.write(
        "Configure the existing wastewater infrastructure and treatment "
        "requirements. BIOROOT uses these operating parameters to generate "
        "a customized treatment architecture."
    )

    st.markdown("---")

    st.subheader("Facility Identification")

    col1, col2 = st.columns(2)

    with col1:
        facility_id = st.text_input(
            "Facility ID",
            value="FAC-001"
        )

    with col2:
        sector = st.selectbox(
            "Industrial sector",
            [
                "Biotechnology / Pharmaceutical",
                "Chemical Processing",
                "Food Processing",
                "Textile",
                "Research Laboratory",
                "Other"
            ]
        )

    st.markdown("---")

    st.subheader("Existing Infrastructure")

    col1, col2, col3 = st.columns(3)

    with col1:
        operating_hours = st.number_input(
            "Daily operating hours",
            min_value=1.0,
            max_value=24.0,
            value=16.0,
            step=1.0
        )

    with col2:
        diameter_mm = st.number_input(
            "Existing pipe diameter (mm)",
            min_value=50.0,
            max_value=500.0,
            value=150.0,
            step=10.0
        )

    with col3:
        length_m = st.number_input(
            "Available pipe length (m)",
            min_value=5.0,
            max_value=100.0,
            value=20.0,
            step=5.0
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        flow_l_min = st.number_input(
            "Wastewater flow rate (L/min)",
            min_value=5.0,
            max_value=200.0,
            value=50.0,
            step=5.0
        )

    with col2:
        temperature = st.number_input(
            "Operating temperature (°C)",
            min_value=10.0,
            max_value=50.0,
            value=27.0,
            step=1.0
        )

    with col3:
        pressure = st.number_input(
            "Operating pressure (bar)",
            min_value=0.2,
            max_value=5.0,
            value=1.0,
            step=0.1
        )

    st.markdown("---")

    st.subheader("Treatment Objective")

    priority = st.selectbox(
        "Treatment priority",
        [
            "Balanced",
            "Maximum phosphate removal",
            "Maximum dye removal",
            "Minimum material requirement"
        ]
    )

    st.markdown("---")

    st.subheader("Optional Laboratory Measurements")

    st.caption(
        "These measurements are optional. The prototype can generate a "
        "design using facility operating conditions alone."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        phosphate_input = st.number_input(
            "Phosphate concentration (mg/L)",
            min_value=0.0,
            value=0.0,
            step=10.0
        )

    with col2:
        dye_input = st.number_input(
            "Dye concentration (mg/L)",
            min_value=0.0,
            value=0.0,
            step=10.0
        )

    with col3:
        organic_load = st.number_input(
            "Organic load (mg/L)",
            min_value=0.0,
            value=0.0,
            step=10.0
        )

    st.markdown("---")

    if st.button(
        "⚡ Generate Optimized Treatment Design",
        type="primary",
        use_container_width=True
    ):

        st.session_state.facility_data = {
            "facility_id": facility_id,
            "sector": sector,
            "operating_hours": operating_hours,
            "diameter_mm": diameter_mm,
            "length_m": length_m,
            "flow_l_min": flow_l_min,
            "temperature": temperature,
            "pressure": pressure,
            "priority": priority,
            "phosphate_input": phosphate_input,
            "dye_input": dye_input,
            "organic_load": organic_load
        }

        st.session_state.initialized = True
        st.session_state.screen = "Optimized Prediction"

        st.rerun()

# =================================================
# OPTIMIZED PREDICTION
# =================================================

elif st.session_state.screen == "Optimized Prediction":

    if not st.session_state.initialized:

        st.warning(
            "Please configure the industry parameters first."
        )

        if st.button("← Return to Industry Portal"):
            st.session_state.screen = "Industry Portal"
            st.rerun()

    else:

        data = st.session_state.facility_data

        facility_id = data["facility_id"]
        sector = data["sector"]
        operating_hours = data["operating_hours"]
        diameter_mm = data["diameter_mm"]
        length_m = data["length_m"]
        flow_l_min = data["flow_l_min"]
        temperature = data["temperature"]
        pressure = data["pressure"]
        priority = data["priority"]
        phosphate_input = data["phosphate_input"]
        dye_input = data["dye_input"]

        st.header("⚙️ Optimized Prediction")

        st.write(
            "AI-assisted configuration of the treatment composite and "
            "root-like hydraulic architecture."
        )

        # =================================================
        # HYDRAULIC CALCULATIONS
        # =================================================

        diameter_m = diameter_mm / 1000

        pipe_area = math.pi * (diameter_m / 2) ** 2

        flow_m3_s = flow_l_min / 1000 / 60

        velocity = flow_m3_s / pipe_area

        pipe_volume_m3 = pipe_area * length_m

        pipe_volume_l = pipe_volume_m3 * 1000

        residence_time = pipe_volume_l / flow_l_min

        # =================================================
        # BASE FORMULATION
        # =================================================

        if priority == "Maximum phosphate removal":

            base_alginate = 46
            base_sargassum = 30
            base_eggshell = 18
            base_plastic = 6

            base_phosphate = 88
            base_dye = 68

        elif priority == "Maximum dye removal":

            base_alginate = 44
            base_sargassum = 36
            base_eggshell = 14
            base_plastic = 6

            base_phosphate = 72
            base_dye = 88

        elif priority == "Minimum material requirement":

            base_alginate = 42
            base_sargassum = 30
            base_eggshell = 18
            base_plastic = 10

            base_phosphate = 76
            base_dye = 70

        else:

            base_alginate = 45
            base_sargassum = 33
            base_eggshell = 16
            base_plastic = 6

            base_phosphate = 82
            base_dye = 80

        # =================================================
        # FORMULATION ADAPTATION
        # =================================================

        hydraulic_stress = (
            (flow_l_min / 50)
            * (pressure / 1)
        )

        alginate = base_alginate
        sargassum = base_sargassum
        eggshell = base_eggshell
        recycled_plastic = base_plastic

        if hydraulic_stress > 1:

            recycled_plastic += min(
                5,
                (hydraulic_stress - 1) * 2
            )

            alginate -= min(
                2,
                (hydraulic_stress - 1)
            )

        else:

            recycled_plastic -= min(
                2,
                (1 - hydraulic_stress)
            )

        if diameter_mm > 150:

            sargassum += min(
                4,
                (diameter_mm - 150) / 100
            )

        if priority == "Maximum phosphate removal":

            eggshell += 3
            alginate -= 1

        elif priority == "Maximum dye removal":

            sargassum += 3
            alginate -= 1

        # =================================================
        # NORMALIZE FORMULATION
        # =================================================

        total = (
            alginate
            + sargassum
            + eggshell
            + recycled_plastic
        )

        alginate = alginate / total * 100
        sargassum = sargassum / total * 100
        eggshell = eggshell / total * 100
        recycled_plastic = recycled_plastic / total * 100

        # =================================================
        # BEAD DIAMETER
        # =================================================

        bead_size = 9.0

        bead_size += (
            (diameter_mm - 150) / 100
        )

        bead_size -= (
            (flow_l_min - 50) / 80
        )

        bead_size -= (
            (pressure - 1) * 0.25
        )

        if priority == "Maximum phosphate removal":

            bead_size += 1.0

        elif priority == "Maximum dye removal":

            bead_size -= 0.5

        elif priority == "Minimum material requirement":

            bead_size -= 1.0

        bead_size = max(
            5.0,
            min(15.0, bead_size)
        )

        # =================================================
        # BEAD LOADING
        # =================================================

        bead_loading = 12.0

        bead_loading += (
            flow_l_min / 50 * 2
        )

        bead_loading += (
            diameter_mm / 150 * 1.5
        )

        if priority == "Minimum material requirement":

            bead_loading -= 3

        bead_loading = max(
            5,
            min(25, bead_loading)
        )

        # =================================================
        # BRANCH COUNT
        # =================================================

        branch_count = 4

        if diameter_mm >= 250:

            branch_count += 2

        elif diameter_mm >= 180:

            branch_count += 1

        if length_m >= 40:

            branch_count += 2

        elif length_m >= 25:

            branch_count += 1

        if flow_l_min >= 100:

            branch_count += 1

        branch_count = max(
            3,
            min(12, branch_count)
        )

        # =================================================
        # BRANCH ANGLE
        # =================================================

        if velocity < 0.03:

            branch_angle = 25

        elif velocity < 0.06:

            branch_angle = 35

        elif velocity < 0.10:

            branch_angle = 45

        elif velocity < 0.18:

            branch_angle = 55

        else:

            branch_angle = 65

        branch_angle += (
            (diameter_mm - 150) / 100
        )

        if priority == "Maximum phosphate removal":

            branch_angle += 3

        elif priority == "Maximum dye removal":

            branch_angle -= 2

        branch_angle = max(
            20,
            min(70, branch_angle)
        )

        # =================================================
        # BRANCH SPACING
        # =================================================

        branch_spacing = (
            length_m / branch_count
        )

        # =================================================
        # STRUCTURAL FACTOR
        # =================================================

        structural_factor = (
            1
            + recycled_plastic / 100 * 0.8
        )

        structural_factor = max(
            0.8,
            min(1.2, structural_factor)
        )

        # =================================================
        # CONTACT FACTOR
        # =================================================

        contact_factor = (
            residence_time / 7
        )

        contact_factor = max(
            0.4,
            min(1.5, contact_factor)
        )

        # =================================================
        # PERFORMANCE MODEL
        # =================================================

        phosphate_removal = (

            base_phosphate

            + 8 * (contact_factor - 1)

            + 5 * (structural_factor - 1)

            + (temperature - 27) * 0.12

            + (diameter_mm / 150 - 1) * 3

            - max(
                0,
                (flow_l_min - 50) * 0.12
            )
        )

        dye_removal = (

            base_dye

            + 8 * (contact_factor - 1)

            + 4 * (structural_factor - 1)

            + (temperature - 27) * 0.10

            + (length_m / 20 - 1) * 3

            - max(
                0,
                (flow_l_min - 50) * 0.12
            )
        )

        # =================================================
        # OPTIONAL CONCENTRATION ADJUSTMENT
        # =================================================

        if phosphate_input > 0:

            phosphate_removal -= min(
                10,
                phosphate_input / 100
            )

        if dye_input > 0:

            dye_removal -= min(
                10,
                dye_input / 100
            )

        phosphate_removal = max(
            20,
            min(95, phosphate_removal)
        )

        dye_removal = max(
            20,
            min(95, dye_removal)
        )

        # =================================================
        # SAVE DESIGN DATA
        # =================================================

        st.session_state.design_data = {

            "alginate": alginate,
            "sargassum": sargassum,
            "eggshell": eggshell,
            "recycled_plastic": recycled_plastic,

            "bead_size": bead_size,
            "bead_loading": bead_loading,

            "branch_count": branch_count,
            "branch_angle": branch_angle,
            "branch_spacing": branch_spacing,

            "velocity": velocity,
            "residence_time": residence_time,

            "phosphate_removal": phosphate_removal,
            "dye_removal": dye_removal
        }

        # =================================================
        # FACILITY CONFIGURATION
        # =================================================

        st.markdown("---")

        st.subheader("🏭 Facility Configuration")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Facility",
                facility_id
            )

        with col2:
            st.metric(
                "Sector",
                sector
            )

        with col3:
            st.metric(
                "Operating hours",
                f"{operating_hours:.0f} h/day"
            )

        with col4:
            st.metric(
                "Treatment priority",
                priority
            )

        # =================================================
        # HYDRAULIC ANALYSIS
        # =================================================

        st.markdown("---")

        st.subheader("💧 Hydraulic Analysis")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Flow rate",
                f"{flow_l_min:.1f} L/min"
            )

        with col2:
            st.metric(
                "Flow velocity",
                f"{velocity:.3f} m/s"
            )

        with col3:
            st.metric(
                "Pipe volume",
                f"{pipe_volume_l:.1f} L"
            )

        with col4:
            st.metric(
                "Residence time",
                f"{residence_time:.2f} min"
            )

        # =================================================
        # PREDICTED PERFORMANCE
        # =================================================

        st.markdown("---")

        st.subheader("📊 Predicted Treatment Performance")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Phosphate removal",
                f"{phosphate_removal:.1f}%"
            )

        with col2:

            st.metric(
                "Dye removal",
                f"{dye_removal:.1f}%"
            )

        with col3:

            st.metric(
                "Composite utilization",
                f"{bead_loading:.1f}%"
            )

        st.caption(
            "Prototype prediction generated from a simplified surrogate "
            "model. Values require experimental calibration and validation "
            "before real-world deployment."
        )

        # =================================================
        # BEAD FORMULATION
        # =================================================

        st.markdown("---")

        st.subheader("🧪 Optimized Bead Formulation")

        st.caption(
            "AI-optimized composite matrix based on facility hydraulics, "
            "treatment priority and structural requirements."
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Sodium alginate",
                f"{alginate:.1f}%"
            )

            st.caption(
                "Polymer matrix"
            )

        with col2:

            st.metric(
                "Sargassum tenerrimum",
                f"{sargassum:.1f}%"
            )

            st.caption(
                "Natural biosorbent"
            )

        with col3:

            st.metric(
                "Eggshell powder",
                f"{eggshell:.1f}%"
            )

            st.caption(
                "Functional filler"
            )

        with col4:

            st.metric(
                "Recycled polypropylene",
                f"{recycled_plastic:.1f}%"
            )

            st.caption(
                "Structural reinforcement"
            )

        st.markdown("#### Composite Matrix")

        formulation_data = pd.DataFrame(
            {
                "Component": [
                    "Sodium alginate",
                    "Sargassum tenerrimum",
                    "Eggshell powder",
                    "Recycled polypropylene"
                ],

                "Recommended composition (%)": [
                    alginate,
                    sargassum,
                    eggshell,
                    recycled_plastic
                ],

                "Role in composite": [
                    "Bead-forming polymer matrix",
                    "Natural biosorbent",
                    "Calcium-rich functional filler",
                    "Structural reinforcement"
                ]
            }
        )

        st.dataframe(
            formulation_data,
            use_container_width=True,
            hide_index=True
        )

        # =================================================
        # ROOT ARCHITECTURE
        # =================================================

        st.markdown("---")

        st.subheader("🌿 Optimized Root Architecture")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:

            st.metric(
                "Branches",
                f"{branch_count}"
            )

        with col2:

            st.metric(
                "Branch angle",
                f"{branch_angle:.1f}°"
            )

        with col3:

            st.metric(
                "Branch spacing",
                f"{branch_spacing:.2f} m"
            )

        with col4:

            st.metric(
                "Bead diameter",
                f"{bead_size:.1f} mm"
            )

        with col5:

            st.metric(
                "Bead loading",
                f"{bead_loading:.1f}%"
            )

        # =================================================
        # OPTIMIZATION TRACE
        # =================================================

        st.markdown("---")

        st.subheader("🧠 Optimization Trace")

        trace_data = pd.DataFrame(
            {
                "Optimization variable": [
                    "Flow rate",
                    "Pipe diameter",
                    "Pipe length",
                    "Operating pressure",
                    "Treatment priority",
                    "Residence time",
                    "Structural factor"
                ],

                "Input / calculated value": [
                    f"{flow_l_min:.1f} L/min",
                    f"{diameter_mm:.1f} mm",
                    f"{length_m:.1f} m",
                    f"{pressure:.2f} bar",
                    priority,
                    f"{residence_time:.2f} min",
                    f"{structural_factor:.3f}"
                ],

                "Design response": [
                    "Hydraulic loading",
                    "Root capacity",
                    "Contact opportunity",
                    "Structural requirement",
                    "Treatment weighting",
                    "Treatment exposure",
                    "Mechanical reinforcement"
                ]
            }
        )

        st.dataframe(
            trace_data,
            use_container_width=True,
            hide_index=True
        )

        # =================================================
        # HYDRAULIC-TREATMENT RESPONSE
        # =================================================

        st.markdown("---")

        st.subheader("📈 Hydraulic–Treatment Response")

        flow_range = [
            max(10, flow_l_min - 40),
            max(10, flow_l_min - 20),
            flow_l_min,
            flow_l_min + 20,
            flow_l_min + 40
        ]

        phosphate_curve = []
        dye_curve = []

        for test_flow in flow_range:

            test_contact = (
                residence_time
                * (flow_l_min / test_flow)
            )

            test_contact_factor = max(
                0.4,
                min(1.5, test_contact / 7)
            )

            test_phosphate = (

                base_phosphate

                + 8 * (test_contact_factor - 1)

                + 5 * (structural_factor - 1)

                + (temperature - 27) * 0.12

                + (diameter_mm / 150 - 1) * 3

                - max(
                    0,
                    (test_flow - 50) * 0.12
                )
            )

            test_dye = (

                base_dye

                + 8 * (test_contact_factor - 1)

                + 4 * (structural_factor - 1)

                + (temperature - 27) * 0.10

                + (length_m / 20 - 1) * 3

                - max(
                    0,
                    (test_flow - 50) * 0.12
                )
            )

            phosphate_curve.append(
                max(20, min(95, test_phosphate))
            )

            dye_curve.append(
                max(20, min(95, test_dye))
            )

        response_data = pd.DataFrame(
            {
                "Flow rate (L/min)": flow_range,
                "Phosphate removal (%)": phosphate_curve,
                "Dye removal (%)": dye_curve
            }
        )

        st.line_chart(
            response_data,
            x="Flow rate (L/min)",
            y=[
                "Phosphate removal (%)",
                "Dye removal (%)"
            ]
        )

        st.caption(
            "Prototype sensitivity analysis showing how predicted "
            "treatment performance changes with hydraulic loading. "
            "This is a model-based response and is not experimental data."
        )

        # =================================================
        # HANDOFF
        # =================================================

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🧬 Open Digital Twin Control Room",
                type="primary",
                use_container_width=True
            ):

                st.session_state.screen = (
                    "Digital Twin Control Room"
                )

                st.rerun()

        with col2:

            if st.button(
                "← Modify Industry Parameters",
                use_container_width=True
            ):

                st.session_state.screen = "Industry Portal"

                st.rerun()

# =================================================
# DIGITAL TWIN CONTROL ROOM
# =================================================

elif st.session_state.screen == "Digital Twin Control Room":

    st.header("🖥️ Digital Twin Control Room")

    st.info(
        "Digital Twin Control Room is the next development module. "
        "It will display the virtual wastewater treatment system, "
        "live hydraulic variables and simulated treatment response."
    )

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("System status", "ONLINE")

    with col2:
        st.metric("Twin synchronization", "ACTIVE")

    with col3:
        st.metric("Virtual sensors", "12")

    with col4:
        st.metric("Model state", "CALIBRATION")

    st.markdown("---")

    if st.button("← Back to Optimized Prediction"):
        st.session_state.screen = "Optimized Prediction"
        st.rerun()

# =================================================
# PERFORMANCE ANALYTICS
# =================================================

elif st.session_state.screen == "Performance Analytics":

    st.header("📊 Performance Analytics")

    st.info(
        "Performance analytics will compare current system behaviour "
        "with predicted future treatment performance."
    )

    if st.button("← Back"):
        st.session_state.screen = "Optimized Prediction"
        st.rerun()

# =================================================
# SCENARIO SIMULATOR
# =================================================

elif st.session_state.screen == "Scenario Simulator":

    st.header("🧪 Scenario Simulator")

    st.info(
        "Scenario simulation will allow changes in flow, temperature, "
        "pollutant loading and bead condition."
    )

    if st.button("← Back"):
        st.session_state.screen = "Optimized Prediction"
        st.rerun()

# =================================================
# REGENERATION & LIFECYCLE
# =================================================

elif st.session_state.screen == "Regeneration & Lifecycle":

    st.header("♻️ Regeneration & Lifecycle")

    st.info(
        "This module will track bead utilization, regeneration cycles, "
        "replacement requirements and plastic waste diversion."
    )

    if st.button("← Back"):
        st.session_state.screen = "Optimized Prediction"
        st.rerun()
