import streamlit as st
import pandas as pd
import math

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="BIOROOT | Digital Twin",
    page_icon="🌱",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "screen" not in st.session_state:
    st.session_state.screen = "Industry Portal"

if "initialized" not in st.session_state:
    st.session_state.initialized = False

if "facility_data" not in st.session_state:
    st.session_state.facility_data = {}

if "design_data" not in st.session_state:
    st.session_state.design_data = {}

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f7f9fb;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    .metric-card {
        background: white;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e1e5ea;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .section-title {
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .technical-box {
        background: #eef3f7;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #2c7a7b;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.markdown("## 🌱 BIOROOT")
st.sidebar.caption("AI-Enabled Circular Wastewater Digital Twin")

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
            screen_name,
            use_container_width=True,
            disabled=True
        )

st.sidebar.markdown("---")

st.sidebar.caption(
    "Prototype platform\n"
    "Virtual predictions require experimental calibration."
)

# =====================================================
# INDUSTRY PORTAL
# =====================================================

if st.session_state.screen == "Industry Portal":

    st.title("🏭 Industry Portal")

    st.markdown(
        "### Industrial Wastewater Treatment Configuration"
    )

    st.caption(
        "Enter facility-level operating parameters. "
        "The optimization engine converts these inputs into "
        "a customized BIOROOT treatment architecture."
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Facility Information")

        facility_id = st.text_input(
            "Facility ID",
            value="PLANT-001"
        )

        sector = st.selectbox(
            "Industrial Sector",
            [
                "Biopharmaceutical Manufacturing",
                "Biomedical Laboratory",
                "Pharmaceutical Manufacturing",
                "Chemical Processing",
                "Food Processing",
                "Research Facility"
            ]
        )

        operating_hours = st.number_input(
            "Daily Operating Hours",
            min_value=1.0,
            max_value=24.0,
            value=16.0,
            step=1.0
        )

        treatment_priority = st.selectbox(
            "Treatment Priority",
            [
                "Balanced treatment",
                "Maximum phosphate removal",
                "Maximum dye removal",
                "Minimum material requirement"
            ]
        )

    with col2:

        st.markdown("### Hydraulic Parameters")

        diameter_mm = st.number_input(
            "Existing Pipe Diameter (mm)",
            min_value=25.0,
            max_value=1000.0,
            value=150.0,
            step=5.0
        )

        length_m = st.number_input(
            "Available Pipe Length (m)",
            min_value=1.0,
            max_value=500.0,
            value=20.0,
            step=1.0
        )

        flow_l_min = st.number_input(
            "Wastewater Flow Rate (L/min)",
            min_value=1.0,
            max_value=5000.0,
            value=50.0,
            step=5.0
        )

        temperature = st.number_input(
            "Operating Temperature (°C)",
            min_value=5.0,
            max_value=60.0,
            value=27.0,
            step=0.5
        )

        pressure = st.number_input(
            "Operating Pressure (bar)",
            min_value=0.1,
            max_value=20.0,
            value=1.0,
            step=0.1
        )

    st.markdown("---")

    st.markdown("### Optional Laboratory Measurements")

    st.caption(
        "These measurements are optional. The optimization can operate "
        "using facility and hydraulic information alone."
    )

    lab1, lab2, lab3 = st.columns(3)

    with lab1:

        phosphate_input = st.number_input(
            "Phosphate concentration (mg/L)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

    with lab2:

        dye_input = st.number_input(
            "Dye concentration (mg/L)",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

    with lab3:

        organic_input = st.number_input(
            "Organic load indicator",
            min_value=0.0,
            value=0.0,
            step=1.0
        )

    st.markdown("---")

    if st.button(
        "🚀 Generate Optimized Treatment Design",
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
            "treatment_priority": treatment_priority,
            "phosphate_input": phosphate_input,
            "dye_input": dye_input,
            "organic_input": organic_input
        }

        st.session_state.initialized = True
        st.session_state.screen = "Optimized Prediction"

        st.rerun()

# =====================================================
# OPTIMIZED PREDICTION
# =====================================================

elif st.session_state.screen == "Optimized Prediction":

    if not st.session_state.initialized:

        st.warning(
            "Please configure an industrial facility first."
        )

        if st.button("← Back to Industry Portal"):

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

        priority = data["treatment_priority"]

        phosphate_input = data["phosphate_input"]
        dye_input = data["dye_input"]

        # =================================================
        # HYDRAULIC CALCULATIONS
        # =================================================

        diameter_m = diameter_mm / 1000

        pipe_area = math.pi * (
            diameter_m / 2
        ) ** 2

        flow_m3_s = (
            flow_l_min / 1000 / 60
        )

        velocity = flow_m3_s / pipe_area

        pipe_volume_m3 = (
            pipe_area * length_m
        )

        pipe_volume_l = (
            pipe_volume_m3 * 1000
        )

        residence_time = (
            pipe_volume_l / flow_l_min
        )

        # =================================================
        # BASE FORMULATION
        # =================================================

        if priority == "Maximum phosphate removal":

            alginate = 36
            sargassum = 30
            eggshell = 24
            recycled_plastic = 10

            base_phosphate = 82
            base_dye = 65

        elif priority == "Maximum dye removal":

            alginate = 40
            sargassum = 34
            eggshell = 16
            recycled_plastic = 10

            base_phosphate = 68
            base_dye = 82

        elif priority == "Minimum material requirement":

            alginate = 30
            sargassum = 27
            eggshell = 23
            recycled_plastic = 20

            base_phosphate = 70
            base_dye = 68

        else:

            alginate = 36
            sargassum = 31
            eggshell = 23
            recycled_plastic = 10

            base_phosphate = 76
            base_dye = 76

        # =================================================
        # HYDRAULIC ADAPTATION
        # =================================================

        hydraulic_stress = velocity / 0.05

        alginate += max(
            -4,
            min(6, (hydraulic_stress - 1) * 3)
        )

        recycled_plastic += max(
            -3,
            min(8, (hydraulic_stress - 1) * 4)
        )

        sargassum += (
            (diameter_mm / 150 - 1) * 2
        )

        eggshell += (
            (pressure - 1) * 1.5
        )

        # =================================================
        # NORMALIZATION
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
        recycled_plastic = (
            recycled_plastic / total * 100
        )

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

        bead_loading = (
            420
            + diameter_mm * 0.8
            + flow_l_min * 1.2
            + pressure * 25
        )

        bead_loading = max(
            250,
            min(1500, bead_loading)
        )

        # =================================================
        # BRANCH COUNT
        # =================================================

        branch_count = int(
            round(
                3
                + length_m / 10
                + flow_l_min / 40
                + diameter_mm / 300
            )
        )

        branch_count = max(
            3,
            min(15, branch_count)
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

            branch_angle += 5

        elif priority == "Maximum dye removal":

            branch_angle -= 3

        elif priority == "Minimum material requirement":

            branch_angle -= 5

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
        # CONTACT / TREATMENT FACTOR
        # =================================================

        contact_factor = (
            residence_time / 7
        )

        contact_factor = max(
            0.4,
            min(1.5, contact_factor)
        )

        structural_factor = (
            1
            + recycled_plastic / 100 * 0.5
            + eggshell / 100 * 0.2
        )

        # =================================================
        # TEMPERATURE EFFECT
        # =================================================

        temperature_factor = (
            (temperature - 27) * 0.12
        )

        # =================================================
        # FLOW PENALTY
        # =================================================

        flow_penalty = min(
            25,
            max(
                0,
                (flow_l_min - 50) * 0.12
            )
        )

        # =================================================
        # PREDICTED PERFORMANCE
        # =================================================

        phosphate_removal = (
            base_phosphate
            + 8 * (contact_factor - 1)
            + 5 * (structural_factor - 1)
            + temperature_factor
            + (diameter_mm / 150 - 1) * 3
            - flow_penalty
        )

        dye_removal = (
            base_dye
            + 8 * (contact_factor - 1)
            + 4 * (structural_factor - 1)
            + (temperature - 27) * 0.10
            + (length_m / 20 - 1) * 3
            - flow_penalty
        )

        # Optional laboratory measurement influence

        if phosphate_input > 0:

            phosphate_adjustment = min(
                5,
                phosphate_input / 100
            )

            phosphate_removal += (
                phosphate_adjustment
            )

        if dye_input > 0:

            dye_adjustment = min(
                5,
                dye_input / 100
            )

            dye_removal += (
                dye_adjustment
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
        # SAVE DESIGN
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
            "pipe_volume_l": pipe_volume_l,
            "residence_time": residence_time,

            "phosphate_removal": phosphate_removal,
            "dye_removal": dye_removal

        }

        # =================================================
        # PAGE HEADER
        # =================================================

        st.title("🌱 Optimized Prediction")

        st.caption(
            "AI-assisted design optimization based on facility "
            "hydraulics, treatment priority and material constraints."
        )

        st.markdown("---")

        st.markdown(
            f"""
            <div class="technical-box">

            <b>Optimization Target:</b> {priority}<br>
            <b>Facility:</b> {facility_id}<br>
            <b>Sector:</b> {sector}<br>
            <b>Hydraulic Regime:</b> {velocity:.3f} m/s<br>
            <b>Optimization Status:</b> Design converged

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # PERFORMANCE METRICS
        # =================================================

        st.markdown("### 📊 Predicted Treatment Performance")

        m1, m2, m3, m4 = st.columns(4)

        with m1:

            st.metric(
                "Phosphate Removal",
                f"{phosphate_removal:.1f}%"
            )

        with m2:

            st.metric(
                "Dye Removal",
                f"{dye_removal:.1f}%"
            )

        with m3:

            st.metric(
                "Residence Time",
                f"{residence_time:.2f} min"
            )

        with m4:

            st.metric(
                "Flow Velocity",
                f"{velocity:.3f} m/s"
            )

        # =================================================
        # FORMULATION
        # =================================================

        st.markdown("---")

        st.markdown(
            "### 🧪 Optimized Bead Formulation"
        )

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "Sodium Alginate",
                f"{alginate:.1f}%"
            )

        with c2:

            st.metric(
                "Sargassum tenerrimum",
                f"{sargassum:.1f}%"
            )

        with c3:

            st.metric(
                "Eggshell Powder",
                f"{eggshell:.1f}%"
            )

        with c4:

            st.metric(
                "Recycled PP",
                f"{recycled_plastic:.1f}%"
            )

        st.caption(
            "Recycled polypropylene is treated here primarily as "
            "a structural reinforcement component."
        )

        # =================================================
        # ROOT ARCHITECTURE
        # =================================================

        st.markdown("---")

        st.markdown(
            "### 🌿 Optimized Root Architecture"
        )

        r
