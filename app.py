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
        flow_l_min = data["flow_l_min"]
        temperature = data["temperature"]
        pressure = data["pressure"]
        phosphate_input = data["phosphate_input"]
        dye_input = data["dye_input"]

        phosphate_removal = design["phosphate_removal"]
        dye_removal = design["dye_removal"]
        residence_time = design["residence_time"]
        bead_loading = design["bead_loading"]
        branch_count = design["branch_count"]

        # =================================================
        # DIGITAL TWIN SIMULATION STATE
        # =================================================

        simulation_time = 18

        dynamic_flow = (
            flow_l_min
            + 3 * math.sin(simulation_time / 4)
        )

        dynamic_temperature = (
            temperature
            + 0.4 * math.sin(simulation_time / 6)
        )

        dynamic_pressure = (
            pressure
            + 0.03 * math.sin(simulation_time / 5)
        )

        dynamic_residence = (
            residence_time
            * (flow_l_min / dynamic_flow)
        )

        dynamic_phosphate_removal = max(
            20,
            min(
                95,
                phosphate_removal
                - max(
                    0,
                    (dynamic_flow - flow_l_min) * 0.12
                )
            )
        )

        dynamic_dye_removal = max(
            20,
            min(
                95,
                dye_removal
                - max(
                    0,
                    (dynamic_flow - flow_l_min) * 0.12
                )
            )
        )

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
            * (1 - dynamic_phosphate_removal / 100)
        )

        outlet_dye = (
            inlet_dye
            * (1 - dynamic_dye_removal / 100)
        )

        system_health = max(
            70,
            min(
                99,
                96
                - max(
                    0,
                    (dynamic_flow - 70) * 0.15
                )
                - max(
                    0,
                    (bead_loading - 18) * 0.4
                )
            )
        )

        # =================================================
        # HEADER
        # =================================================

        st.header("🖥️ Digital Twin Control Room")

        st.caption(
            f"Virtual operating environment • Facility {facility_id} • "
            "Prototype real-time digital twin"
        )

        # =================================================
        # SYSTEM STATUS
        # =================================================

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "System status",
                "● ONLINE"
            )

        with col2:
            st.metric(
                "Twin synchronization",
                "ACTIVE"
            )

        with col3:
            st.metric(
                "Simulation time",
                f"{simulation_time} min"
            )

        with col4:
            st.metric(
                "System health",
                f"{system_health:.1f}%"
            )

        # =================================================
        # VIRTUAL TREATMENT PROCESS
        # =================================================

        st.markdown("---")

        st.subheader("🌊 Virtual Treatment Process")

        st.caption(
            "Live virtual representation of wastewater movement "
            "through the biofunctional root-treatment network."
        )

        process_col1, process_col2, process_col3 = st.columns(
            [1, 3, 1]
        )

        with process_col1:

            st.markdown("### INLET")

            st.metric(
                "Flow",
                f"{dynamic_flow:.1f} L/min"
            )

            st.metric(
                "Pressure",
                f"{dynamic_pressure:.2f} bar"
            )

        with process_col2:

            st.markdown(
                """
                <div style="
                    border:2px solid #4CAF50;
                    border-radius:18px;
                    padding:25px;
                    background:#f8fff8;
                    text-align:center;
                ">

                <h3>🌿 BIOROOT REACTOR</h3>

                <p>────────●──────●──────●────────</p>

                <p>↘ &nbsp;&nbsp; ↘ &nbsp;&nbsp; ↘ &nbsp;&nbsp; ↘</p>

                <p>● &nbsp;&nbsp; ● &nbsp;&nbsp; ● &nbsp;&nbsp; ●</p>

                <p>↗ &nbsp;&nbsp; ↗ &nbsp;&nbsp; ↗ &nbsp;&nbsp; ↗</p>

                <p>────────●──────●──────●────────</p>

                <strong>
                Biofunctional composite bead network
                </strong>

                </div>
                """,
                unsafe_allow_html=True
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

        with process_col3:

            st.markdown("### OUTLET")

            st.metric(
                "Phosphate",
                f"{outlet_phosphate:.1f} mg/L"
            )

            st.metric(
                "Dye",
                f"{outlet_dye:.1f} mg/L"
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
        # TREATMENT ZONE MONITORING
        # =================================================

        st.markdown("---")

        st.subheader("🧬 Treatment Zone Monitoring")

        zone_data = pd.DataFrame(
            {
                "Treatment zone": [
                    "Inlet zone",
                    "Root zone 1",
                    "Root zone 2",
                    "Root zone 3",
                    "Outlet zone"
                ],

                "Virtual flow (L/min)": [
                    dynamic_flow,
                    dynamic_flow * 0.98,
                    dynamic_flow * 0.96,
                    dynamic_flow * 0.94,
                    dynamic_flow * 0.93
                ],

                "Relative treatment state (%)": [
                    0,
                    dynamic_phosphate_removal * 0.30,
                    dynamic_phosphate_removal * 0.55,
                    dynamic_phosphate_removal * 0.78,
                    dynamic_phosphate_removal
                ],

                "Bead interaction": [
                    "Initial contact",
                    "Adsorption / interaction",
                    "Extended contact",
                    "Final treatment",
                    "Treated effluent"
                ]
            }
        )

        st.dataframe(
            zone_data,
            use_container_width=True,
            hide_index=True
        )

        # =================================================
        # LIVE RESPONSE PROFILE
        # =================================================

        st.markdown("---")

        st.subheader("📈 Live Twin Response Profile")

        time_points = [
            0,
            2,
            4,
            6,
            8,
            10,
            12,
            14,
            16,
            18
        ]

        flow_profile = []
        phosphate_profile = []
        dye_profile = []

        for t in time_points:

            simulated_flow = (
                flow_l_min
                + 3 * math.sin(t / 4)
            )

            simulated_phosphate = max(
                20,
                min(
                    95,
                    phosphate_removal
                    - max(
                        0,
                        (simulated_flow - flow_l_min)
                        * 0.12
                    )
                )
            )

            simulated_dye = max(
                20,
                min(
                    95,
                    dye_removal
                    - max(
                        0,
                        (simulated_flow - flow_l_min)
                        * 0.12
                    )
                )
            )

            flow_profile.append(
                simulated_flow
            )

            phosphate_profile.append(
                simulated_phosphate
            )

            dye_profile.append(
                simulated_dye
            )

        live_data = pd.DataFrame(
            {
                "Simulation time (min)": time_points,
                "Flow rate (L/min)": flow_profile,
                "Phosphate removal (%)": phosphate_profile,
                "Dye removal (%)": dye_profile
            }
        )

        st.line_chart(
            live_data,
            x="Simulation time (min)",
            y=[
                "Flow rate (L/min)",
                "Phosphate removal (%)",
                "Dye removal (%)"
            ]
        )

        # =================================================
        # DIGITAL TWIN INTELLIGENCE
        # =================================================

        st.markdown("---")

        st.subheader("🧠 Digital Twin Intelligence")

        if dynamic_flow > flow_l_min + 2:

            st.warning(
                "Hydraulic loading is increasing. The virtual twin "
                "predicts reduced residence time and recommends "
                "monitoring treatment efficiency."
            )

        else:

            st.success(
                "Hydraulic conditions remain within the configured "
                "operating envelope. Treatment performance is "
                "predicted to remain stable."
            )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Predicted current phosphate removal",
                f"{dynamic_phosphate_removal:.1f}%"
            )

        with col2:

            st.metric(
                "Predicted current dye removal",
                f"{dynamic_dye_removal:.1f}%"
            )

        # =================================================
        # TWIN MODEL STATE
        # =================================================

        st.markdown("---")

        st.subheader("⚙️ Twin Model State")

        model_state = pd.DataFrame(
            {
                "Parameter": [
                    "Hydraulic model",
                    "Treatment response model",
                    "Composite state",
                    "Root architecture",
                    "Virtual sensor network",
                    "Calibration status"
                ],

                "Current state": [
                    "ACTIVE",
                    "ACTIVE",
                    "ACTIVE",
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
            "⚠️ This Digital Twin Control Room is a prototype virtual "
            "simulation. Displayed sensor values and treatment responses "
            "are model-generated and require experimental calibration "
            "before representing real plant measurements."
        )

        # =================================================
        # NAVIGATION
        # =================================================

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "← Back to Optimized Prediction",
                use_container_width=True
            ):

                st.session_state.screen = (
                    "Optimized Prediction"
                )

                st.rerun()

        with col2:

            if st.button(
                "Open Performance Analytics →",
                type="primary",
                use_container_width=True
            ):

                st.session_state.screen = (
                    "Performance Analytics"
                )

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
