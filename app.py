import streamlit as st
import math

st.set_page_config(
    page_title="BIOROOT | Digital Twin Platform",
    page_icon="🌱",
    layout="wide"
)

# =========================================================
# SESSION STATE
# =========================================================

if "screen" not in st.session_state:
    st.session_state.screen = "Industry Portal"

if "initialized" not in st.session_state:
    st.session_state.initialized = False

if "facility_data" not in st.session_state:
    st.session_state.facility_data = {}

if "design_data" not in st.session_state:
    st.session_state.design_data = {}


# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

.portal-header {
    padding: 25px 30px;
    border-radius: 14px;
    background: linear-gradient(135deg, #102a43, #243b53);
    color: white;
    margin-bottom: 25px;
}

.portal-header h1 {
    margin-bottom: 5px;
    font-size: 38px;
}

.portal-header p {
    margin-top: 0px;
    color: #d9e2ec;
    font-size: 16px;
}

.section-card {
    padding: 22px;
    border-radius: 12px;
    background: white;
    border: 1px solid #d9e2ec;
    margin-bottom: 18px;
}

.status-card {
    padding: 16px;
    border-radius: 10px;
    background: #f0f4f8;
    border-left: 5px solid #2f80ed;
}

.small-label {
    color: #627d98;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.5px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🌱 BIOROOT")

    st.caption("Circular Wastewater Intelligence Platform")

    st.markdown("---")

    st.markdown("### SYSTEM WORKFLOW")

    screens = [
        "Industry Portal",
        "Optimized Prediction",
        "Digital Twin Control Room",
        "Performance Analytics",
        "Scenario Simulator",
        "Regeneration & Lifecycle"
    ]

    for i, screen_name in enumerate(screens, 1):

        enabled = (
            screen_name == "Industry Portal"
            or (
                screen_name == "Optimized Prediction"
                and st.session_state.initialized
            )
        )

        if st.button(
            f"{i:02d}  {screen_name}",
            use_container_width=True,
            disabled=not enabled
        ):
            st.session_state.screen = screen_name

    st.markdown("---")

    twin_status = (
        "● CONFIGURED"
        if st.session_state.initialized
        else "● STANDBY"
    )

    st.markdown(
        f'<div class="status-card">'
        f'<div class="small-label">DIGITAL TWIN STATUS</div>'
        f'<b>{twin_status}</b>'
        f'</div>',
        unsafe_allow_html=True
    )


# =========================================================
# INDUSTRY PORTAL
# =========================================================

if st.session_state.screen == "Industry Portal":

    st.markdown("""
    <div class="portal-header">

    <h1>🌱 BIOROOT</h1>

    <p>AI-Enabled Digital Twin for Circular Wastewater Treatment</p>

    <p>
    INDUSTRIAL CONFIGURATION & DIGITAL TWIN INITIALIZATION PORTAL
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Prototype platform: digital-twin predictions are demonstration "
        "outputs and require calibration against experimental treatment data."
    )

    # -----------------------------------------------------
    # FACILITY PROFILE
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-card">'
        '<h3>🏭 Facility Profile</h3>'
        '<p>Define the industrial environment in which the BIOROOT '
        'treatment architecture will operate.</p>'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        facility_id = st.text_input(
            "Facility / Plant ID",
            value="PLANT-001"
        )

    with col2:
        application = st.selectbox(
            "Industrial Sector",
            [
                "Laboratory / Research Facility",
                "Pharmaceutical Manufacturing",
                "Biotechnology Industry",
                "Food Processing",
                "Municipal Wastewater"
            ]
        )

    with col3:
        operating_hours = st.number_input(
            "Daily operating hours",
            min_value=1.0,
            max_value=24.0,
            value=16.0,
            step=1.0
        )

    # -----------------------------------------------------
    # HYDRAULIC PARAMETERS
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-card">'
        '<h3>⚙️ Hydraulic System Parameters</h3>'
        '<p>Enter the existing process-pipe conditions available for '
        'BIOROOT integration.</p>'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

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

        temperature = st.number_input(
            "Operating temperature (°C)",
            min_value=5.0,
            max_value=60.0,
            value=27.0,
            step=0.5
        )

    with col3:

        operating_pressure = st.number_input(
            "Operating pressure (bar)",
            min_value=0.1,
            max_value=20.0,
            value=1.0,
            step=0.1
        )

        treatment_priority = st.selectbox(
            "Primary treatment objective",
            [
                "Balanced treatment",
                "Maximum phosphate removal",
                "Maximum dye removal",
                "Minimum material requirement"
            ]
        )

    # -----------------------------------------------------
    # OPTIONAL WATER QUALITY
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-card">'
        '<h3>🧪 Wastewater Characterization</h3>'
        '<p>Optional laboratory measurements can be entered when '
        'available.</p>'
        '</div>',
        unsafe_allow_html=True
    )

    use_measurements = st.checkbox(
        "I have laboratory measurements available"
    )

    if use_measurements:

        col1, col2, col3 = st.columns(3)

        with col1:
            phosphate = st.number_input(
                "Phosphate concentration (mg/L)",
                min_value=0.0,
                max_value=10000.0,
                value=50.0,
                step=1.0
            )

        with col2:
            dye_concentration = st.number_input(
                "Dye / colour index (mg/L)",
                min_value=0.0,
                max_value=10000.0,
                value=40.0,
                step=1.0
            )

        with col3:
            organic_load = st.number_input(
                "Organic load indicator (mg/L)",
                min_value=0.0,
                max_value=10000.0,
                value=100.0,
                step=5.0
            )

    else:

        phosphate = None
        dye_concentration = None
        organic_load = None

        st.caption(
            "No laboratory concentration data entered. BIOROOT will "
            "use the selected application profile and system parameters "
            "for this prototype."
        )

    st.markdown("---")

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    st.markdown("### 🚀 System Initialization")

    st.write(
        "The entered facility parameters will be transferred to the "
        "BIOROOT optimization and digital-twin environment."
    )

    if st.button(
        "🚀 INITIALIZE BIOROOT DIGITAL TWIN",
        use_container_width=True
    ):

        st.session_state.facility_data = {
            "facility_id": facility_id,
            "application": application,
            "operating_hours": operating_hours,
            "pipe_diameter": pipe_diameter,
            "pipe_length": pipe_length,
            "flow_rate": flow_rate,
            "temperature": temperature,
            "operating_pressure": operating_pressure,
            "treatment_priority": treatment_priority,
            "phosphate": phosphate,
            "dye_concentration": dye_concentration,
            "organic_load": organic_load
        }

        st.session_state.initialized = True
        st.session_state.screen = "Optimized Prediction"

        st.rerun()


# =========================================================
# OPTIMIZED PREDICTION
# =========================================================

elif st.session_state.screen == "Optimized Prediction":

    data = st.session_state.facility_data

    st.markdown("""
    <div class="portal-header">

    <h1>🧠 OPTIMIZED PREDICTION</h1>

    <p>
    BIOROOT Adaptive Treatment Architecture Engine
    </p>

    <p>
    HYDRAULIC + MATERIAL + TREATMENT PARAMETER OPTIMIZATION
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Prototype optimization engine. Numerical outputs are "
        "demonstration estimates and require experimental calibration."
    )

    # -----------------------------------------------------
    # HYDRAULIC CALCULATION
    # -----------------------------------------------------

    diameter_m = data["pipe_diameter"] / 1000

    area = math.pi * (diameter_m / 2) ** 2

    flow_m3_s = data["flow_rate"] / 1000 / 60

    velocity = flow_m3_s / area

    pipe_volume_l = area * data["pipe_length"] * 1000

    residence_time = pipe_volume_l / data["flow_rate"]

    # -----------------------------------------------------
    # BASE OPTIMIZATION
    # -----------------------------------------------------

    priority = data["treatment_priority"]

    if priority == "Maximum phosphate removal":

        alginate = 35
        sargassum = 35
        eggshell = 20
        plastic = 10

        phosphate_base = 86
        dye_base = 68

        branches = 8
        bead_size = 10

    elif priority == "Maximum dye removal":

        alginate = 40
        sargassum = 35
        eggshell = 15
        plastic = 10

        phosphate_base = 72
        dye_base = 88

        branches = 7
        bead_size = 8

    elif priority == "Minimum material requirement":

        alginate = 40
        sargassum = 30
        eggshell = 20
        plastic = 10

        phosphate_base = 68
        dye_base = 70

        branches = 5
        bead_size = 8

    else:

        alginate = 38
        sargassum = 32
        eggshell = 20
        plastic = 10

        phosphate_base = 78
        dye_base = 80

        branches = 6
        bead_size = 9

    # -----------------------------------------------------
    # HYDRAULIC ADJUSTMENT
    # -----------------------------------------------------

    reference_flow = 50.0

    flow_factor = reference_flow / max(data["flow_rate"], 1)

    hydraulic_adjustment = 10 * (flow_factor - 1)

    phosphate_removal = phosphate_base + hydraulic_adjustment

    dye_removal = dye_base + hydraulic_adjustment

    temperature_adjustment = (
        (data["temperature"] - 27.0) * 0.15
    )

    phosphate_removal += temperature_adjustment
    dye_removal += temperature_adjustment

    phosphate_removal = max(
        20,
        min(95, phosphate_removal)
    )

    dye_removal = max(
        20,
        min(95, dye_removal)
    )

    # -----------------------------------------------------
    # ARCHITECTURE ADJUSTMENT
    # -----------------------------------------------------

    if velocity > 0.15:

        branches += 2

    elif velocity < 0.03:

        branches = max(4, branches - 1)

    branches = min(branches, 12)

    branch_spacing = data["pipe_length"] / branches

    branch_angle = 35 if velocity < 0.10 else 45

    bead_loading = min(
        80,
        max(
            35,
            55 + (data["flow_rate"] - 50) * 0.2
        )
    )

    # -----------------------------------------------------
    # STORE DESIGN
    # -----------------------------------------------------

    st.session_state.design_data = {

        "alginate": alginate,
        "sargassum": sargassum,
        "eggshell": eggshell,
        "plastic": plastic,

        "branches": branches,
        "bead_size": bead_size,
        "bead_loading": bead_loading,

        "branch_spacing": branch_spacing,
        "branch_angle": branch_angle,

        "velocity": velocity,
        "residence_time": residence_time,

        "phosphate_removal": phosphate_removal,
        "dye_removal": dye_removal
    }

    # -----------------------------------------------------
    # STATUS
    # -----------------------------------------------------

    st.success(
        "✓ OPTIMIZATION COMPLETE — DESIGN GENERATED FROM CURRENT "
        "FACILITY CONDITIONS"
    )

    # -----------------------------------------------------
    # PERFORMANCE
    # -----------------------------------------------------

    st.markdown("### 📊 Predicted Treatment Performance")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric(
        "Phosphate removal",
        f"{phosphate_removal:.1f}%"
    )

    m2.metric(
        "Dye removal",
        f"{dye_removal:.1f}%"
    )

    m3.metric(
        "Residence time",
        f"{residence_time:.2f} min"
    )

    m4.metric(
        "Flow velocity",
        f"{velocity:.3f} m/s"
    )

    # -----------------------------------------------------
    # MATERIAL FORMULATION
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown("### 🧪 Optimized Bead Formulation")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            '<div class="section-card">'
            '<h4>COMPOSITE MATRIX</h4>'
            f'<p>Sodium alginate: <b>{alginate}%</b></p>'
            f'<p><i>Sargassum tenerrimum</i>: <b>{sargassum}%</b></p>'
            f'<p>Eggshell powder: <b>{eggshell}%</b></p>'
            f'<p>Recycled polypropylene: <b>{plastic}%</b></p>'
            '</div>',
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            '<div class="section-card">'
            '<h4>STRUCTURAL PARAMETERS</h4>'
            f'<p>Bead diameter: <b>{bead_size} mm</b></p>'
            f'<p>Bead loading: <b>{bead_loading:.1f}%</b></p>'
            f'<p>Branch count: <b>{branches}</b></p>'
            f'<p>Branch spacing: <b>{branch_spacing:.2f} m</b></p>'
            f'<p>Branch angle: <b>{branch_angle}°</b></p>'
            '</div>',
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # DIGITAL TWIN HANDOFF
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown("### 🔄 Digital Twin Handoff")

    st.write(
        "The optimized architecture is ready to be instantiated "
        "inside the BIOROOT virtual operating environment."
    )

    if st.button(
        "▶ LAUNCH DIGITAL TWIN CONTROL ROOM",
        use_container_width=True
    ):

        st.session_state.screen = "Digital Twin Control Room"

        st.rerun()

    if st.button("← Back to Industry Portal"):

        st.session_state.screen = "Industry Portal"

        st.rerun()


# =========================================================
# OTHER SCREENS
# =========================================================

else:

    st.title(f"🌱 {st.session_state.screen}")

    st.info(
        "This module will be built in the next development step."
    )

    if st.button("← Back"):

        st.session_state.screen = "Optimized Prediction"

        st.rerun()
