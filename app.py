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
    # WASTEWATER CHARACTERIZATION
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

    # -----------------------------------------------------
    # INITIALIZATION
    # -----------------------------------------------------

    st.markdown("---")

    st.markdown("### 🚀 System Initialization")

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

    <p>BIOROOT Adaptive Treatment Architecture Engine</p>

    <p>
    HYDRAULIC + MATERIAL + TREATMENT PARAMETER OPTIMIZATION
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Prototype optimization engine. Numerical outputs are "
        "demonstration estimates and require experimental calibration."
    )

    # =====================================================
    # INPUT EXTRACTION
    # =====================================================

    diameter_mm = data["pipe_diameter"]
    length_m = data["pipe_length"]
    flow_l_min = data["flow_rate"]
    temperature = data["temperature"]
    pressure = data["operating_pressure"]
    priority = data["treatment_priority"]

    # =====================================================
    # HYDRAULIC MODEL
    # =====================================================

    diameter_m = diameter_mm / 1000

    pipe_area = math.pi * (diameter_m / 2) ** 2

    flow_m3_s = flow_l_min / 1000 / 60

    velocity = flow_m3_s / pipe_area

    pipe_volume_l = pipe_area * length_m * 1000

    residence_time = pipe_volume_l / flow_l_min

    # =====================================================
    # NORMALIZED DESIGN FACTORS
    # =====================================================

    # Larger pipe = more treatment volume
    diameter_factor = min(
        1.5,
        max(0.5, diameter_mm / 150)
    )

    # Longer pipe = more available treatment length
    length_factor = min(
        1.5,
        max(0.5, length_m / 20)
    )

    # Higher flow = shorter contact time
    flow_factor = min(
        2.0,
        max(0.4, flow_l_min / 50)
    )

    # Temperature influence for prototype kinetic adjustment
    temperature_factor = 1 + (
        (temperature - 27) * 0.01
    )

    # Pressure has a smaller architectural influence
    pressure_factor = min(
        1.3,
        max(0.7, pressure)
    )

    # =====================================================
    # BASE FORMULATION
    # =====================================================

    if priority == "Maximum phosphate removal":

        alginate = 34
        sargassum = 38
        eggshell = 20
        plastic = 8

        base_phosphate = 84
        base_dye = 70

    elif priority == "Maximum dye removal":

        alginate = 39
        sargassum = 37
        eggshell = 14
        plastic = 10

        base_phosphate = 70
        base_dye = 86

    elif priority == "Minimum material requirement":

        alginate = 42
        sargassum = 30
        eggshell = 18
        plastic = 10

        base_phosphate = 65
        base_dye = 68

    else:

        alginate = 38
        sargassum = 33
        eggshell = 19
        plastic = 10

        base_phosphate = 77
        base_dye = 79

    # =====================================================
    # FORMULATION ADAPTATION
    # =====================================================

    # High flow → slightly more structural reinforcement
    if flow_l_min > 75:

        plastic += 4
        alginate -= 2
        sargassum -= 1
        eggshell -= 1

    elif flow_l_min < 30:

        plastic = max(6, plastic - 2)
        alginate += 1
        sargassum += 1

    # Larger diameter → slightly more bead loading possible
    if diameter_mm > 250:

        alginate += 2
        sargassum += 1
        plastic -= 2
        eggshell -= 1

    elif diameter_mm < 100:

        plastic += 2
        alginate -= 1
        sargassum -= 1

    # High pressure → reinforce structure
    if pressure > 3:

        plastic += 2
        alginate -= 1
        eggshell -= 1

    # Normalize formulation to exactly 100%
    total = alginate + sargassum + eggshell + plastic

    alginate = round(alginate / total * 100)
    sargassum = round(sargassum / total * 100)
    eggshell = round(eggshell / total * 100)

    plastic = 100 - alginate - sargassum - eggshell

    # =====================================================
    # BEAD SIZE
    # =====================================================

    bead_size = 9.0

    if diameter_mm > 300:
        bead_size += 2

    if flow_l_min > 75:
        bead_size -= 1

    if flow_l_min < 30:
        bead_size += 1

    if pressure > 3:
        bead_size -= 0.5

    bead_size = max(
        6,
        min(14, bead_size)
    )

    # =====================================================
    # BEAD LOADING
    # =====================================================

    bead_loading = 50

    bead_loading += diameter_factor * 8
    bead_loading += length_factor * 5
    bead_loading -= flow_factor * 6

    if priority == "Maximum phosphate removal":
        bead_loading += 8

    elif priority == "Maximum dye removal":
        bead_loading += 6

    elif priority == "Minimum material requirement":
        bead_loading -= 10

    bead_loading = max(
        30,
        min(80, bead_loading)
    )

    # =====================================================
    # ROOT ARCHITECTURE
    # =====================================================

    branches = 5

    branches += round(diameter_factor * 2)
    branches += round(length_factor)
    branches -= round(flow_factor)

    if priority == "Maximum phosphate removal":
        branches += 2

    elif priority == "Maximum dye removal":
        branches += 1

    elif priority == "Minimum material requirement":
        branches -= 2

    branches = max(
        3,
        min(14, branches)
    )

    branch_spacing = length_m / branches

    # Higher flow → more aggressive branching angle
    if flow_l_min > 100:
        branch_angle = 50
    elif flow_l_min > 60:
        branch_angle = 45
    elif flow_l_min < 30:
        branch_angle = 30
    else:
        branch_angle = 35

    # =====================================================
    # PERFORMANCE MODEL
    # =====================================================

    contact_factor = min(
        1.5,
        max(
            0.4,
            residence_time / 7
        )
    )

    structural_factor = min(
        1.25,
        max(
            0.7,
            bead_loading / 55
        )
    )

    hydraulic_penalty = min(
        25,
        max(
            0,
            (flow_l_min - 50) * 0.12
        )
    )

    # Prototype removal predictions
    phosphate_removal = (
        base_phosphate
        + 8 * (contact_factor - 1)
        + 5 * (structural_factor - 1)
        + (temperature - 27) * 0.12
        + (diameter_factor - 1) * 3
        - hydraulic_penalty
    )

    dye_removal = (
        base_dye
        + 8 * (contact_factor - 1)
        + 4 * (structural_factor - 1)
        + (temperature - 27) * 0.10
        + (length_factor - 1) * 3
        - hydraulic_penalty
    )

    # =====================================================
    # OPTIONAL CONCENTRATION EFFECT
    # =====================================================

    if data["phosphate"] is not None:

        phosphate_load_factor = min(
            1.3,
            max(
                0.7,
                data["phosphate"] / 50
            )
        )

        phosphate_removal -= (
            phosphate_load_factor - 1
        ) * 8

    if data["dye_concentration"] is not None:

        dye_load_factor = min(
            1.3,
            max(
                0.7,
                data["dye_concentration"] / 40
            )
        )

        dye_removal -= (
            dye_load_factor - 1
        ) * 8

    # Temperature and pressure adjustment
    phosphate_removal *= temperature_factor
    dye_removal *= temperature_factor

    phosphate_removal = max(
        20,
        min(95, phosphate_removal)
    )

    dye_removal = max(
        20,
        min(95, dye_removal)
    )

    # =====================================================
    # STORE DESIGN
    # =====================================================

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

    # =====================================================
    # SYSTEM STATUS
    # =====================================================

    st.success(
        "✓ OPTIMIZATION COMPLETE — DESIGN GENERATED FROM "
        "CURRENT FACILITY CONDITIONS"
    )

    # =====================================================
    # PERFORMANCE
    # =====================================================

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

    # =====================================================
    # FORMULATION
    # =====================================================

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
            f'<p>Bead diameter: <b>{bead_size:.1f} mm</b></p>'
            f'<p>Bead loading: <b>{bead_loading:.1f}%</b></p>'
            f'<p>Branch count: <b>{branches}</b></p>'
            f'<p>Branch spacing: <b>{branch_spacing:.2f} m</b></p>'
            f'<p>Branch angle: <b>{branch_angle}°</b></p>'
            '</div>',
            unsafe_allow_html=True
        )

    # =====================================================
    # INPUT → DESIGN TRACE
    # =====================================================

    st.markdown("---")

    st.markdown("### 🔬 Optimization Trace")

    trace1, trace2, trace3 = st.columns(3)

    with trace1:
        st.metric(
            "Hydraulic regime",
            f"{velocity:.3f} m/s"
        )
        st.caption(
            "Derived from pipe diameter + wastewater flow"
        )

    with trace2:
        st.metric(
            "Available treatment volume",
            f"{pipe_volume_l:.1f} L"
        )
        st.caption(
            "Derived from pipe geometry + available length"
        )

    with trace3:
        st.metric(
            "Design objective",
            priority
        )
        st.caption(
            "Optimization target selected by facility"
        )

    # =====================================================
    # DESIGN TRADE-OFF GRAPH
    # =====================================================

    st.markdown("---")

    st.markdown("### 📈 Design Trade-off Analysis")

    chart_data = {
        "Design": [
            "Material Efficient",
            "Balanced",
            "High Treatment"
        ],
        "Treatment Index": [
            max(0, phosphate_removal - 12),
            phosphate_removal,
            min(98, phosphate_removal + 7)
        ],
        "Material Utilization": [
            65,
            78,
            92
        ]
    }

    st.line_chart(
        {
            "Material Efficient": chart_data["Treatment Index"],
            "Balanced": [
                chart_data["Material Utilization"][0],
                chart_data["Material Utilization"][1],
                chart_data["Material Utilization"][2]
            ],
            "High Treatment": [
                chart_data["Treatment Index"][0],
                chart_data["Treatment Index"][1],
                chart_data["Treatment Index"][2]
            ]
        }
    )

    st.caption(
        "Prototype design-space visualization. Curves represent "
        "optimization trade-offs rather than experimentally validated "
        "performance data."
    )

    # =====================================================
    # DIGITAL TWIN HANDOFF
    # =====================================================

    st.markdown("---")

    st.markdown("### 🔄 Digital Twin Handoff")

    st.write(
        "The optimized architecture has been instantiated from the "
        "current facility configuration and is ready for virtual "
        "operation."
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
