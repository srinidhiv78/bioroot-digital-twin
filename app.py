import streamlit as st
import pandas as pd
import math
import time

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

    if screen_name in [
        "Industry Portal",
        "Optimized Prediction",
        "Digital Twin Control Room",
        "Performance Analytics",
        "Scenario Simulator",
        "Regeneration & Lifecycle"
    ]:

        if st.sidebar.button(
            screen_name,
            use_container_width=True
        ):
            st.session_state.screen = screen_name
            st.rerun()

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
            "Please configure the Industry Portal first."
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

    if not st.session_state.initialized:

        st.warning(
            "Please configure the Industry Portal first."
        )

        if st.button("← Return to Industry Portal"):
            st.session_state.screen = "Industry Portal"
            st.rerun()

    else:

        data = st.session_state.facility_data
        design = st.session_state.design_data

        facility_id = data["facility_id"]
        base_flow = data["flow_l_min"]
        base_temperature = data["temperature"]
        base_pressure = data["pressure"]

        phosphate_input = data["phosphate_input"]
        dye_input = data["dye_input"]

        base_phosphate_removal = design["phosphate_removal"]
        base_dye_removal = design["dye_removal"]
        base_residence_time = design["residence_time"]
        base_bead_loading = design["bead_loading"]
        branch_count = design["branch_count"]

        # =================================================
        # SIMULATION CONTROLS
        # =================================================

        if "twin_time" not in st.session_state:
            st.session_state.twin_time = 0

        if "twin_playing" not in st.session_state:
            st.session_state.twin_playing = False

        # =================================================
        # HEADER
        # =================================================

        st.header("🖥️ Digital Twin Control Room")

        st.caption(
            f"Virtual operating environment • Facility {facility_id} • "
            "Real-time process simulation"
        )

        # =================================================
        # SIMULATION CONTROL BAR
        # =================================================

        st.markdown("---")

        st.subheader("⏱️ Simulation Control")

        control_col1, control_col2, control_col3 = st.columns(
            [5, 1, 1]
        )

        with control_col1:

            simulation_time = st.slider(
                "Virtual operating time",
                min_value=0,
                max_value=60,
                value=st.session_state.twin_time,
                step=1,
                format="%d min"
            )

            st.session_state.twin_time = simulation_time

        with control_col2:

            if st.button(
                "▶ Play",
                use_container_width=True
            ):

                st.session_state.twin_playing = True
                st.rerun()

        with control_col3:

            if st.button(
                "⏸ Pause",
                use_container_width=True
            ):

                st.session_state.twin_playing = False
                st.rerun()

        # =================================================
        # TIME-DEPENDENT VIRTUAL PROCESS MODEL
        # =================================================

        t = simulation_time

        dynamic_flow = (
            base_flow
            + 8 * math.sin(t / 7)
            + 2 * math.sin(t / 2.5)
        )

        dynamic_temperature = (
            base_temperature
            + 1.2 * math.sin(t / 11)
        )

        dynamic_pressure = (
            base_pressure
            + 0.06 * math.sin(t / 6)
            + (dynamic_flow - base_flow) * 0.002
        )

        dynamic_residence = (
            base_residence_time
            * (base_flow / max(dynamic_flow, 1))
        )

        hydraulic_factor = (
            base_flow / max(dynamic_flow, 1)
        )

        hydraulic_factor = max(
            0.65,
            min(1.20, hydraulic_factor)
        )

        temperature_factor = (
            1
            + (dynamic_temperature - base_temperature)
            * 0.012
        )

        dynamic_bead_loading = (
            base_bead_loading
            + (t / 60) * 5
        )

        dynamic_bead_loading = min(
            100,
            dynamic_bead_loading
        )

        # =================================================
        # CURRENT TREATMENT PERFORMANCE
        # =================================================

        dynamic_phosphate_removal = (
            base_phosphate_removal
            * hydraulic_factor
            * temperature_factor
        )

        dynamic_dye_removal = (
            base_dye_removal
            * hydraulic_factor
            * temperature_factor
        )

        lifecycle_penalty = max(
            0,
            (dynamic_bead_loading - 18) * 0.25
        )

        dynamic_phosphate_removal -= lifecycle_penalty
        dynamic_dye_removal -= lifecycle_penalty * 0.8

        dynamic_phosphate_removal = max(
            20,
            min(95, dynamic_phosphate_removal)
        )

        dynamic_dye_removal = max(
            20,
            min(95, dynamic_dye_removal)
        )

        # =================================================
        # INLET / OUTLET CONCENTRATIONS
        # =================================================

        if phosphate_input > 0:

            inlet_phosphate = phosphate_input

        else:

            inlet_phosphate = 100.0

        if dye_input > 0:

            inlet_dye = dye_input

        else:

            inlet_dye = 100.0

        outlet_phosphate = (
            inlet_phosphate
            * (
                1
                - dynamic_phosphate_removal / 100
            )
        )

        outlet_dye = (
            inlet_dye
            * (
                1
                - dynamic_dye_removal / 100
            )
        )

        # =================================================
        # SYSTEM HEALTH
        # =================================================

        hydraulic_stress = (
            dynamic_flow / max(base_flow, 1)
        )

        system_health = (
            98
            - max(
                0,
                (hydraulic_stress - 1) * 18
            )
            - max(
                0,
                (dynamic_bead_loading - 18) * 0.35
            )
        )

        system_health = max(
            65,
            min(99, system_health)
        )

        # =================================================
        # STATUS HEADER
        # =================================================

        st.markdown("---")

        status_col1, status_col2, status_col3, status_col4 = st.columns(4)

        with status_col1:

            st.metric(
                "SYSTEM STATUS",
                "● ONLINE"
            )

        with status_col2:

            st.metric(
                "TWIN SYNCHRONIZATION",
                "ACTIVE"
            )

        with status_col3:

            st.metric(
                "VIRTUAL TIME",
                f"{t} min"
            )

        with status_col4:

            st.metric(
                "SYSTEM HEALTH",
                f"{system_health:.1f}%"
            )

        # =================================================
        # VIRTUAL PROCESS VISUALIZATION
        # =================================================

        st.markdown("---")

        st.subheader("🌊 Live Virtual Treatment Process")

        st.caption(
            "Virtual wastewater flow through the BIOROOT treatment "
            "network at the selected simulation time."
        )

        process_col1, process_col2, process_col3 = st.columns(
            [1, 3, 1]
        )

        # =================================================
        # INLET
        # =================================================

        with process_col1:

            st.markdown("### 💧 INLET")

            st.metric(
                "Flow",
                f"{dynamic_flow:.1f} L/min"
            )

            st.metric(
                "Pressure",
                f"{dynamic_pressure:.2f} bar"
            )

            st.metric(
                "Temperature",
                f"{dynamic_temperature:.1f} °C"
            )

        # =================================================
        # ROOT REACTOR
        # =================================================

        with process_col2:

            animation_duration = max(
                0.8,
                2.5 - dynamic_flow / 100
            )

            reactor_html = f"""
            <style>

            .reactor {{
                border: 2px solid #4CAF50;
                border-radius: 20px;
                padding: 22px;
                background: linear-gradient(
                    180deg,
                    #f8fff8,
                    #eef9f0
                );
                text-align: center;
                overflow: hidden;
            }}

            .reactor-title {{
                font-size: 22px;
                font-weight: 700;
                margin-bottom: 12px;
            }}

            .pipe {{
                position: relative;
                height: 120px;
                margin: 10px 0;
                border-top: 5px solid #7a8a91;
                border-bottom: 5px solid #7a8a91;
                overflow: hidden;
                background: #eef5f7;
            }}

            .water {{
                position: absolute;
                left: -30px;
                top: 48px;
                width: 18px;
                height: 18px;
                border-radius: 50%;
                background: #4aa3df;
                animation: flow {animation_duration}s linear infinite;
            }}

            .water:nth-child(2) {{
                animation-delay: 0.4s;
            }}

            .water:nth-child(3) {{
                animation-delay: 0.8s;
            }}

            .water:nth-child(4) {{
                animation-delay: 1.2s;
            }}

            .water:nth-child(5) {{
                animation-delay: 1.6s;
            }}

            @keyframes flow {{
                0% {{
                    left: -30px;
                }}
                100% {{
                    left: 105%;
                }}
            }}

            .root {{
                position: absolute;
                left: 15%;
                right: 15%;
                top: 20px;
                bottom: 20px;
            }}

            .root-main {{
                position: absolute;
                left: 50%;
                top: 0;
                width: 7px;
                height: 100%;
                background: #4CAF50;
                transform: translateX(-50%);
                border-radius: 10px;
            }}

            .branch {{
                position: absolute;
                height: 6px;
                background: #4CAF50;
                width: 80px;
                border-radius: 10px;
            }}

            .b1 {{
                top: 20px;
                left: 20%;
                transform: rotate(25deg);
            }}

            .b2 {{
                top: 45px;
                right: 20%;
                transform: rotate(-25deg);
            }}

            .b3 {{
                top: 70px;
                left: 20%;
                transform: rotate(-25deg);
            }}

            .b4 {{
                top: 95px;
                right: 20%;
                transform: rotate(25deg);
            }}

            </style>

            <div class="reactor">

                <div class="reactor-title">
                    🌿 BIOROOT REACTOR
                </div>

                <div class="pipe">

                    <div class="water"></div>
                    <div class="water"></div>
                    <div class="water"></div>
                    <div class="water"></div>
                    <div class="water"></div>

                    <div class="root">

                        <div class="root-main"></div>

                        <div class="branch b1"></div>
                        <div class="branch b2"></div>
                        <div class="branch b3"></div>
                        <div class="branch b4"></div>

                    </div>

                </div>

                <strong>
                    Biofunctional composite bead treatment network
                </strong>

                <br>

                <small>
                    {branch_count} virtual treatment branches
                </small>

            </div>
            """

            st.components.v1.html(
                reactor_html,
                height=210
            )

            st.progress(
                min(
                    1.0,
                    max(
                        0.0,
                        dynamic_residence / 10
                    )
                )
            )

            st.caption(
                f"Virtual residence time: "
                f"{dynamic_residence:.2f} min"
            )

        # =================================================
        # OUTLET
        # =================================================

        with process_col3:

            st.markdown("### 🚰 OUTLET")

            st.metric(
                "Phosphate",
                f"{outlet_phosphate:.1f} mg/L"
            )

            st.metric(
                "Dye",
                f"{outlet_dye:.1f} mg/L"
            )

        # =================================================
        # CURRENT STATE
        # =================================================

        st.markdown("---")

        st.subheader("📡 Current Virtual State")

        current_col1, current_col2, current_col3, current_col4 = st.columns(4)

        with current_col1:

            st.metric(
                "Flow velocity",
                f"{design['velocity'] * dynamic_flow / max(base_flow, 1):.3f} m/s"
            )

        with current_col2:

            st.metric(
                "Residence time",
                f"{dynamic_residence:.2f} min"
            )

        with current_col3:

            st.metric(
                "PO₄ removal",
                f"{dynamic_phosphate_removal:.1f}%"
            )

        with current_col4:

            st.metric(
                "Dye removal",
                f"{dynamic_dye_removal:.1f}%"
            )

        # =================================================
        # VIRTUAL SENSOR ARRAY
        # =================================================

        st.markdown("---")

        st.subheader("📡 Virtual Sensor Array")

        sensor1, sensor2, sensor3, sensor4, sensor5, sensor6 = st.columns(6)

        with sensor1:

            st.metric(
                "FLOW",
                f"{dynamic_flow:.1f}"
            )

            st.caption("L/min")

        with sensor2:

            st.metric(
                "TEMP",
                f"{dynamic_temperature:.1f}"
            )

            st.caption("°C")

        with sensor3:

            st.metric(
                "PRESSURE",
                f"{dynamic_pressure:.2f}"
            )

            st.caption("bar")

        with sensor4:

            st.metric(
                "RESIDENCE",
                f"{dynamic_residence:.2f}"
            )

            st.caption("min")

        with sensor5:

            st.metric(
                "PO₄ REMOVAL",
                f"{dynamic_phosphate_removal:.1f}%"
            )

            st.caption("virtual")

        with sensor6:

            st.metric(
                "DYE REMOVAL",
                f"{dynamic_dye_removal:.1f}%"
            )

            st.caption("virtual")

        # =================================================
        # PERFORMANCE TRAJECTORY
        # =================================================

        st.markdown("---")

        st.subheader("📈 Digital Twin Performance Trajectory")

        time_points = list(
            range(
                0,
                61,
                5
            )
        )

        flow_profile = []
        phosphate_profile = []
        dye_profile = []
        health_profile = []

        for simulated_time in time_points:

            simulated_flow = (
                base_flow
                + 8 * math.sin(simulated_time / 7)
                + 2 * math.sin(simulated_time / 2.5)
            )

            simulated_hydraulic_factor = (
                base_flow
                / max(simulated_flow, 1)
            )

            simulated_hydraulic_factor = max(
                0.65,
                min(
                    1.20,
                    simulated_hydraulic_factor
                )
            )

            simulated_temperature = (
                base_temperature
                + 1.2 * math.sin(
                    simulated_time / 11
                )
            )

            simulated_temperature_factor = (
                1
                + (
                    simulated_temperature
                    - base_temperature
                )
                * 0.012
            )

            simulated_bead_loading = (
                base_bead_loading
                + (
                    simulated_time / 60
                ) * 5
            )

            simulated_lifecycle_penalty = max(
                0,
                (
                    simulated_bead_loading
                    - 18
                ) * 0.25
            )

            simulated_phosphate = (
                base_phosphate_removal
                * simulated_hydraulic_factor
                * simulated_temperature_factor
                - simulated_lifecycle_penalty
            )

            simulated_dye = (
                base_dye_removal
                * simulated_hydraulic_factor
                * simulated_temperature_factor
                - simulated_lifecycle_penalty * 0.8
            )

            simulated_health = (
                98
                - max(
                    0,
                    (
                        simulated_flow
                        / max(base_flow, 1)
                        - 1
                    ) * 18
                )
                - max(
                    0,
                    (
                        simulated_bead_loading
                        - 18
                    ) * 0.35
                )
            )

            flow_profile.append(
                simulated_flow
            )

            phosphate_profile.append(
                max(
                    20,
                    min(
                        95,
                        simulated_phosphate
                    )
                )
            )

            dye_profile.append(
                max(
                    20,
                    min(
                        95,
                        simulated_dye
                    )
                )
            )

            health_profile.append(
                max(
                    65,
                    min(
                        99,
                        simulated_health
                    )
                )
            )

        trajectory_data = pd.DataFrame(
            {
                "Simulation time (min)": time_points,
                "Flow rate (L/min)": flow_profile,
                "Phosphate removal (%)": phosphate_profile,
                "Dye removal (%)": dye_profile,
                "System health (%)": health_profile
            }
        )

        st.line_chart(
            trajectory_data,
            x="Simulation time (min)",
            y=[
                "Flow rate (L/min)",
                "Phosphate removal (%)",
                "Dye removal (%)",
                "System health (%)"
            ]
        )

        # =================================================
        # CURRENT STATE INTELLIGENCE
        # =================================================

        st.markdown("---")

        st.subheader("🧠 Current-State Intelligence")

        if dynamic_flow > base_flow * 1.08:

            st.warning(
                "⚠️ Hydraulic loading has increased relative to "
                "the configured baseline. The digital twin predicts "
                "reduced hydraulic residence time and increased "
                "treatment stress."
            )

        elif dynamic_flow < base_flow * 0.92:

            st.info(
                "ℹ️ Hydraulic loading is below the configured baseline. "
                "The digital twin predicts increased residence time "
                "and additional treatment exposure."
            )

        else:

            st.success(
                "✓ Current hydraulic conditions remain close to the "
                "configured operating envelope."
            )

        intelligence_col1, intelligence_col2 = st.columns(2)

        with intelligence_col1:

            st.metric(
                "Current phosphate removal",
                f"{dynamic_phosphate_removal:.1f}%"
            )

            st.metric(
                "Current outlet phosphate",
                f"{outlet_phosphate:.1f} mg/L"
            )

        with intelligence_col2:

            st.metric(
                "Current dye removal",
                f"{dynamic_dye_removal:.1f}%"
            )

            st.metric(
                "Current outlet dye",
                f"{outlet_dye:.1f} mg/L"
            )

        # =================================================
        # TWIN MODEL STATE
        # =================================================

        st.markdown("---")

        st.subheader("⚙️ Digital Twin Model State")

        model_state = pd.DataFrame(
            {
                "Model layer": [
                    "Hydraulic state",
                    "Thermal state",
                    "Treatment response",
                    "Composite utilization",
                    "Root architecture",
                    "Virtual sensors",
                    "Calibration"
                ],
                "Status": [
                    "ACTIVE",
                    "ACTIVE",
                    "ACTIVE",
                    "TRACKING",
                    f"{branch_count} branches",
                    "SYNCHRONIZED",
                    "Prototype / requires experimental data"
                ]
            }
        )

        st.dataframe(
            model_state,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            "⚠️ The displayed sensor values and treatment responses "
            "are model-generated prototype values. They are intended "
            "to demonstrate digital-twin functionality and require "
            "experimental calibration before representing real plant "
            "measurements."
        )

        # =================================================
        # NAVIGATION
        # =================================================

        st.markdown("---")

        nav_col1, nav_col2 = st.columns(2)

        with nav_col1:

            if st.button(
                "← Back to Optimized Prediction",
                use_container_width=True
            ):

                st.session_state.twin_playing = False

                st.session_state.screen = (
                    "Optimized Prediction"
                )

                st.rerun()

        with nav_col2:

            if st.button(
                "Open Performance Analytics →",
                type="primary",
                use_container_width=True
            ):

                st.session_state.twin_playing = False

                st.session_state.screen = (
                    "Performance Analytics"
                )

                st.rerun()

        # =================================================
        # AUTO-PLAY
        # =================================================

        if st.session_state.twin_playing:

            next_time = (
                st.session_state.twin_time
                + 1
            )

            if next_time > 60:

                st.session_state.twin_playing = False

            else:

                st.session_state.twin_time = next_time

                time.sleep(0.25)

                st.rerun()

# =================================================
# PERFORMANCE ANALYTICS
# =================================================

elif st.session_state.screen == "Performance Analytics":

    st.header("📊 Performance Analytics")

    st.caption(
        "Real-time performance intelligence and forward treatment trajectory"
    )

    facility_data = st.session_state.get(
        "facility_data",
        {}
    )

    design_data = st.session_state.get(
        "design_data",
        {}
    )

    if not facility_data or not design_data:

        st.warning(
            "Complete the Industry Portal and Optimized Prediction "
            "modules before viewing performance analytics."
        )

    else:

        # -----------------------------
        # BASE SYSTEM PARAMETERS
        # -----------------------------

        base_flow = facility_data.get(
            "flow_l_min",
            55
        )

        base_phosphate = design_data.get(
            "phosphate_removal",
            82
        )

        base_dye = design_data.get(
            "dye_removal",
            75
        )

        base_health = 96

        # -----------------------------
        # PERFORMANCE TRAJECTORY
        # -----------------------------

        forecast_times = [
            0,
            5,
            10,
            30,
            60
        ]

        performance_data = []

        for t in forecast_times:

            flow_factor = (
                1
                + 0.05 * math.sin(t / 8)
            )

            lifecycle_penalty = (
                1
                - 0.0008 * t
            )

            phosphate = min(
                99,
                max(
                    0,
                    base_phosphate
                    * flow_factor
                    * lifecycle_penalty
                )
            )

            dye = min(
                99,
                max(
                    0,
                    base_dye
                    * flow_factor
                    * lifecycle_penalty
                )
            )

            health = max(
                65,
                base_health
                - 0.18 * t
                - 2 * abs(math.sin(t / 12))
            )

            dynamic_flow = (
                base_flow
                * (
                    1
                    + 0.08 * math.sin(t / 7)
                )
            )

            performance_data.append(
                {
                    "Time": t,
                    "Flow Rate": dynamic_flow,
                    "Phosphate Removal": phosphate,
                    "Dye Removal": dye,
                    "System Health": health
                }
            )

        performance_df = pd.DataFrame(
            performance_data
        )

        # -----------------------------
        # CURRENT PERFORMANCE
        # -----------------------------

        current = performance_df.iloc[0]

        st.subheader("Current System Performance")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Phosphate Removal",
            f"{current['Phosphate Removal']:.1f}%"
        )

        col2.metric(
            "Dye Removal",
            f"{current['Dye Removal']:.1f}%"
        )

        col3.metric(
            "System Health",
            f"{current['System Health']:.1f}%"
        )

        col4.metric(
            "Hydraulic Flow",
            f"{current['Flow Rate']:.1f} L/min"
        )

        st.divider()

        # -----------------------------
        # LIVE PERFORMANCE GRAPH
        # -----------------------------

        st.subheader("Treatment Performance Trajectory")

        chart_df = performance_df.set_index(
            "Time"
        )[
            [
                "Phosphate Removal",
                "Dye Removal",
                "System Health"
            ]
        ]

        st.line_chart(
            chart_df,
            height=350
        )

        st.caption(
            "Virtual forecast generated by the prototype digital twin. "
            "Experimental calibration is required before deployment."
        )

        # -----------------------------
        # FORECAST TABLE
        # -----------------------------

        st.subheader("Forward Performance Forecast")

        forecast_display = performance_df.copy()

        forecast_display["Time"] = (
            forecast_display["Time"]
            .astype(str)
            .replace(
                {
                    "0": "Now",
                    "5": "+5 min",
                    "10": "+10 min",
                    "30": "+30 min",
                    "60": "+1 hr"
                }
            )
        )

        forecast_display = forecast_display[
            [
                "Time",
                "Flow Rate",
                "Phosphate Removal",
                "Dye Removal",
                "System Health"
            ]
        ]

        forecast_display.columns = [
            "Forecast Horizon",
            "Flow (L/min)",
            "PO₄ Removal (%)",
            "Dye Removal (%)",
            "System Health (%)"
        ]

        st.table(
            forecast_display.round(1)
        )

        # -----------------------------
        # PERFORMANCE INTELLIGENCE
        # -----------------------------

        st.subheader("🧠 Performance Intelligence")

        future_health = performance_df.iloc[-1][
            "System Health"
        ]

        future_phosphate = performance_df.iloc[-1][
            "Phosphate Removal"
        ]

        if future_health > 85:

            st.success(
                f"System trajectory remains stable. "
                f"Projected system health after 1 hour: "
                f"{future_health:.1f}%."
            )

        elif future_health > 70:

            st.info(
                f"Stable treatment trajectory with gradual lifecycle-related "
                f"performance decline. Projected system health after 1 hour: "
                f"{future_health:.1f}%."
            )

        else:

            st.error(
                f"Potential intervention window detected. "
                f"Projected system health: "
                f"{future_health:.1f}%."
            )

        st.info(
            f"Digital-twin forecast indicates approximately "
            f"{future_phosphate:.1f}% phosphate removal at the "
            f"+1 hour horizon under the simulated operating conditions."
        )

        # -----------------------------
        # SYSTEM DIAGNOSTICS
        # -----------------------------

        st.subheader("System Diagnostics")

        diagnostic_col1, diagnostic_col2 = st.columns(2)

        with diagnostic_col1:

            st.markdown("### Hydraulic State")

            st.write(
                f"**Baseline flow:** {base_flow:.1f} L/min"
            )

            st.write(
                f"**Forecast flow:** "
                f"{performance_df.iloc[-1]['Flow Rate']:.1f} L/min"
            )

            st.write(
                "**Hydraulic regime:** Adaptive flow simulation"
            )

        with diagnostic_col2:

            st.markdown("### Treatment State")

            st.write(
                f"**PO₄ removal:** "
                f"{current['Phosphate Removal']:.1f}%"
            )

            st.write(
                f"**Dye removal:** "
                f"{current['Dye Removal']:.1f}%"
            )

            st.write(
                "**Model state:** Digital twin synchronized"
            )

        st.divider()

        # -----------------------------
        # NAVIGATION
        # -----------------------------

        col_back, col_next = st.columns(2)

        with col_back:

            if st.button(
                "← Back to Digital Twin",
                use_container_width=True
            ):

                st.session_state.screen = (
                    "Digital Twin Control Room"
                )

                st.rerun()

        with col_next:

            if st.button(
                "Continue to Scenario Simulator →",
                use_container_width=True
            ):

                st.session_state.screen = (
                    "Scenario Simulator"
                )

                st.rerun()

# =================================================
# SCENARIO SIMULATOR
# =================================================

elif st.session_state.screen == "Scenario Simulator":

    st.header("🧪 Scenario Simulator")
    st.caption(
        "Interactive digital-twin stress testing under changing operating conditions"
    )

    facility_data = st.session_state.get("facility_data", {})
    design_data = st.session_state.get("design_data", {})

    if not facility_data or not design_data:

        st.warning(
            "Complete the Industry Portal and Optimized Prediction "
            "modules before running scenarios."
        )

    else:

        st.subheader("⚙️ Operating Conditions")

        col1, col2, col3 = st.columns(3)

        with col1:
            scenario_flow = st.slider(
                "Flow Rate (L/min)",
                min_value=10,
                max_value=150,
                value=int(facility_data.get("flow_l_min", 50)),
                step=5
            )

        with col2:
            scenario_temperature = st.slider(
                "Temperature (°C)",
                min_value=15,
                max_value=45,
                value=int(facility_data.get("temperature", 30)),
                step=1
            )

        with col3:
            pollutant_load = st.slider(
                "Pollutant Loading (%)",
                min_value=25,
                max_value=150,
                value=100,
                step=5
            )

        st.divider()

        # -----------------------------
        # DIGITAL TWIN RESPONSE MODEL
        # -----------------------------

        base_flow = facility_data.get(
            "flow_l_min",
            50
        )

        base_phosphate = design_data.get(
            "phosphate_removal",
            82
        )

        base_dye = design_data.get(
            "dye_removal",
            75
        )

        base_residence = design_data.get(
            "residence_time",
            5
        )

        # Hydraulic response
        flow_ratio = scenario_flow / base_flow

        simulated_residence = (
            base_residence / flow_ratio
        )

        # Temperature response
        temperature_factor = (
            1
            + 0.015 * (
                scenario_temperature
                - facility_data.get("temperature", 30)
            )
        )

        # Hydraulic treatment penalty
        hydraulic_factor = (
            1 / (
                1
                + 0.18 * (
                    flow_ratio - 1
                )
            )
        )

        # Pollutant loading effect
        loading_factor = (
            1
            - 0.0015 * (
                pollutant_load - 100
            )
        )

        simulated_phosphate = min(
            99,
            max(
                0,
                base_phosphate
                * hydraulic_factor
                * temperature_factor
                * loading_factor
            )
        )

        simulated_dye = min(
            99,
            max(
                0,
                base_dye
                * hydraulic_factor
                * temperature_factor
                * loading_factor
            )
        )

        system_health = min(
            100,
            max(
                50,
                100
                - 0.25 * abs(
                    scenario_flow - base_flow
                )
                - 0.15 * abs(
                    scenario_temperature
                    - facility_data.get("temperature", 30)
                )
                - 0.12 * abs(
                    pollutant_load - 100
                )
            )
        )

        # -----------------------------
        # LIVE DIGITAL TWIN OUTPUT
        # -----------------------------
        # -----------------------------
        # VIRTUAL TREATMENT FLOW
        # -----------------------------

        st.subheader("🌊 Virtual Treatment Flow")

        flow_intensity = min(
            1.0,
            max(
                0.2,
                scenario_flow / 100
            )
        )

        animation_speed = max(
            0.3,
            1.5 - flow_intensity
        )

        flow_html = f"""
        <style>

        .twin-container {{
            background: #0b1220;
            border-radius: 15px;
            padding: 20px;
            color: white;
            font-family: Arial, sans-serif;
            overflow: hidden;
        }}

        .pipeline {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }}

        .node {{
            border: 2px solid #38bdf8;
            border-radius: 12px;
            padding: 15px;
            min-width: 110px;
            text-align: center;
            background: #111827;
            box-shadow: 0 0 12px rgba(56,189,248,0.35);
        }}

        .root {{
            border-color: #22c55e;
            box-shadow: 0 0 15px rgba(34,197,94,0.35);
        }}

        .outlet {{
            border-color: #a78bfa;
            box-shadow: 0 0 15px rgba(167,139,250,0.35);
        }}

        .arrow {{
            font-size: 28px;
            color: #38bdf8;
            animation: pulse {animation_speed}s infinite;
        }}

        @keyframes pulse {{
            0% {{ opacity: 0.25; }}
            50% {{ opacity: 1; }}
            100% {{ opacity: 0.25; }}
        }}

        .sensor {{
            margin-top: 15px;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
        }}

        .sensor-box {{
            background: #111827;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            border: 1px solid #334155;
        }}

        </style>

        <div class="twin-container">

            <div class="pipeline">

                <div class="node">
                    <b>INLET</b><br>
                    <small>{scenario_flow} L/min</small>
                </div>

                <div class="arrow">➜</div>

                <div class="node root">
                    <b>ROOT REACTOR</b><br>
                    <small>{design_data.get("branch_count", 6)} branches</small>
                </div>

                <div class="arrow">➜</div>

                <div class="node root">
                    <b>BIOBEADS</b><br>
                    <small>{design_data.get("bead_size", 10)} mm</small>
                </div>

                <div class="arrow">➜</div>

                <div class="node outlet">
                    <b>OUTLET</b><br>
                    <small>Virtual sensor</small>
                </div>

            </div>

            <div class="sensor">

                <div class="sensor-box">
                    <b>PO₄ REMOVAL</b><br>
                    {simulated_phosphate:.1f}%
                </div>

                <div class="sensor-box">
                    <b>DYE REMOVAL</b><br>
                    {simulated_dye:.1f}%
                </div>

                <div class="sensor-box">
                    <b>HEALTH</b><br>
                    {system_health:.1f}%
                </div>

            </div>

        </div>
        """

        st.components.v1.html(
            flow_html,
            height=230
        )
        st.subheader("🧬 Digital Twin Response")

        metric1, metric2, metric3, metric4 = st.columns(4)

        metric1.metric(
            "Simulated PO₄ Removal",
            f"{simulated_phosphate:.1f}%"
        )

        metric2.metric(
            "Simulated Dye Removal",
            f"{simulated_dye:.1f}%"
        )

        metric3.metric(
            "Residence Time",
            f"{simulated_residence:.2f} min"
        )

        metric4.metric(
            "System Health",
            f"{system_health:.1f}%"
        )

        st.divider()

        # -----------------------------
        # SYSTEM STATE
        # -----------------------------
         # -----------------------------
        # DYNAMIC ROOT ARCHITECTURE
        # -----------------------------

        st.subheader("🌿 Live Root Reactor")

        branch_count = int(
            design_data.get(
                "branch_count",
                6
            )
        )

        branch_angle = design_data.get(
            "branch_angle",
            45
        )

        branch_spacing = design_data.get(
            "branch_spacing",
            20
        )

        bead_size = design_data.get(
            "bead_size",
            10
        )

        # Flow controls animation speed
        animation_duration = max(
            0.35,
            min(
                1.8,
                100 / max(
                    scenario_flow,
                    10
                )
            )
        )

        # Pollutant loading controls particle density
        particle_count = int(
            min(
                30,
                max(
                    5,
                    pollutant_load / 4
                )
            )
        )

        # Treatment efficiency controls outlet particle visibility
        outlet_particles = int(
            particle_count
            * (
                1
                - simulated_phosphate / 100
            )
        )

        inlet_particles = ""

        for i in range(particle_count):

            left_position = (
                5
                + (i * 6) % 85
            )

            delay = (
                i * 0.15
            )

            inlet_particles += f"""
            <span
                class="particle"
                style="
                    left:{left_position}%;
                    animation-delay:{delay}s;
                "
            ></span>
            """

        outlet_particle_html = ""

        for i in range(
            max(
                1,
                outlet_particles
            )
        ):

            left_position = (
                10
                + (i * 13) % 80
            )

            delay = (
                i * 0.2
            )

            outlet_particle_html += f"""
            <span
                class="outlet-particle"
                style="
                    left:{left_position}%;
                    animation-delay:{delay}s;
                "
            ></span>
            """

        root_html = f"""
        <style>

        .reactor {{
            background:#0b1220;
            border-radius:16px;
            padding:20px;
            color:white;
            font-family:Arial,sans-serif;
        }}

        .reactor-title {{
            text-align:center;
            font-size:18px;
            font-weight:bold;
            margin-bottom:15px;
        }}

        .flow-zone {{
            position:relative;
            height:330px;
            overflow:hidden;
            border-radius:12px;
            background:#111827;
        }}

        .water-flow {{
            position:absolute;
            left:0;
            top:42%;
            width:100%;
            height:70px;
            background:rgba(56,189,248,0.12);
            border-top:2px solid rgba(56,189,248,0.35);
            border-bottom:2px solid rgba(56,189,248,0.35);
        }}

        .trunk {{
            position:absolute;
            left:50%;
            top:35px;
            width:14px;
            height:250px;
            transform:translateX(-50%);
            background:#22c55e;
            border-radius:10px;
            box-shadow:0 0 15px rgba(34,197,94,0.5);
        }}

        .branch {{
            position:absolute;
            left:50%;
            height:7px;
            width:145px;
            background:#38bdf8;
            border-radius:5px;
            transform-origin:left center;
            box-shadow:0 0 10px rgba(56,189,248,0.5);
        }}

        .branch1 {{
            top:75px;
            transform:rotate(-{branch_angle}deg);
        }}

        .branch2 {{
            top:75px;
            transform:rotate({branch_angle}deg);
        }}

        .branch3 {{
            top:130px;
            transform:rotate(-{branch_angle + 10}deg);
        }}

        .branch4 {{
            top:130px;
            transform:rotate({branch_angle + 10}deg);
        }}

        .branch5 {{
            top:185px;
            transform:rotate(-{branch_angle + 15}deg);
        }}

        .branch6 {{
            top:185px;
            transform:rotate({branch_angle + 15}deg);
        }}

        .particle {{
            position:absolute;
            left:-10px;
            top:45%;
            width:7px;
            height:7px;
            background:#f59e0b;
            border-radius:50%;
            animation:flowRight {animation_duration}s linear infinite;
        }}

         @keyframes flowRight {{

            0% {{
                left:-10px;
                opacity:0;
            }}

            15% {{
                opacity:1;
            }}

            85% {{
                opacity:1;
            }}

            100% {{
                left:100%;
                opacity:0;
            }}

        }}

        .outlet-particle {{
            position:absolute;
            bottom:15px;
            width:6px;
            height:6px;
            background:#ef4444;
            border-radius:50%;
            animation:outletFlow {animation_duration}s linear infinite;
        }}

        @keyframes outletFlow {{

            0% {{
                bottom:15px;
                opacity:0;
            }}

            50% {{
                opacity:1;
            }}

            100% {{
                bottom:0px;
                opacity:0;
            }}

        }}

        .bead {{
            position:absolute;
            width:{max(8, bead_size)}px;
            height:{max(8, bead_size)}px;
            background:#f59e0b;
            border-radius:50%;
            box-shadow:0 0 8px rgba(245,158,11,0.7);
        }}

        .b1 {{
            left:40%;
            top:95px;
        }}

        .b2 {{
            left:58%;
            top:105px;
        }}

        .b3 {{
            left:38%;
            top:150px;
        }}

        .b4 {{
            left:60%;
            top:165px;
        }}

        .b5 {{
            left:42%;
            top:205px;
        }}

        .b6 {{
            left:58%;
            top:220px;
        }}

        .sensor {{
            position:absolute;
            right:15px;
            top:15px;
            background:#020617;
            border:1px solid #334155;
            border-radius:8px;
            padding:10px;
            font-size:12px;
            line-height:1.6;
        }}

        .status {{
            margin-top:12px;
            text-align:center;
            color:#94a3b8;
            font-size:13px;
        }}

        </style>

        <div class="reactor">

            <div class="reactor-title">
                LIVE DIGITAL TWIN — ROOT REACTOR
            </div>

            <div class="flow-zone">

                <div class="water-flow"></div>

                <div class="trunk"></div>

                <div class="branch branch1"></div>
                <div class="branch branch2"></div>
                <div class="branch branch3"></div>
                <div class="branch branch4"></div>
                <div class="branch branch5"></div>
                <div class="branch branch6"></div>

                <div class="bead b1"></div>
                <div class="bead b2"></div>
                <div class="bead b3"></div>
                <div class="bead b4"></div>
                <div class="bead b5"></div>
                <div class="bead b6"></div>

                {inlet_particles}

                {outlet_particle_html}

                <div class="sensor">

                    <b>VIRTUAL SENSORS</b><br>

                    Flow:
                    {scenario_flow} L/min<br>

                    Temperature:
                    {scenario_temperature} °C<br>

                    Loading:
                    {pollutant_load}%<br>

                    Health:
                    {system_health:.1f}%

                </div>

            </div>

            <div class="status">

                Branches: {branch_count}
                &nbsp; | &nbsp;
                Angle: {branch_angle}°
                &nbsp; | &nbsp;
                Spacing: {branch_spacing}
                &nbsp; | &nbsp;
                Bead: {bead_size} mm

            </div>

        </div>
        """

        st.components.v1.html(
            root_html,
            height=390
        )
        st.subheader("📡 Virtual Sensor State")

        sensor_col1, sensor_col2 = st.columns(2)

        with sensor_col1:

            st.markdown("### Hydraulic Sensors")

            st.write(
                f"**Inlet flow:** {scenario_flow} L/min"
            )

            st.write(
                f"**Flow ratio:** {flow_ratio:.2f}× baseline"
            )

            st.write(
                f"**Estimated residence time:** "
                f"{simulated_residence:.2f} min"
            )

        with sensor_col2:

            st.markdown("### Process Sensors")

            st.write(
                f"**Temperature:** {scenario_temperature} °C"
            )

            st.write(
                f"**Pollutant loading:** {pollutant_load}%"
            )

            st.write(
                "**Twin state:** Dynamically recalculated"
            )

        st.divider()

        # -----------------------------
        # INTERVENTION LOGIC
        # -----------------------------

        st.subheader("🧠 AI Intervention Assessment")

        if system_health >= 90:

            st.success(
                "Operating conditions remain within the "
                "simulated optimal control envelope."
            )

        elif system_health >= 75:

            st.info(
                "Moderate process stress detected. "
                "The digital twin predicts a manageable reduction "
                "in treatment performance."
            )

        else:

            st.warning(
                "High process stress detected. "
                "The digital twin recommends reviewing flow rate, "
                "pollutant loading or bead configuration."
            )

        st.caption(
            "Prototype digital-twin simulation. "
            "Predictions require experimental calibration before deployment."
        )

        st.divider()

        # -----------------------------
        # NAVIGATION
        # -----------------------------

        col_back, col_next = st.columns(2)

        with col_back:

            if st.button(
                "← Back to Performance Analytics",
                use_container_width=True
            ):

                st.session_state.screen = (
                    "Performance Analytics"
                )

                st.rerun()

        with col_next:

            if st.button(
                "Continue to Regeneration & Lifecycle →",
                use_container_width=True
            ):

                st.session_state.screen = (
                    "Regeneration & Lifecycle"
                )

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
