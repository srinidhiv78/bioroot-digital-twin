import streamlit as st

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
# SIDEBAR NAVIGATION
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

        if st.button(
            f"{i:02d}  {screen_name}",
            use_container_width=True,
            disabled=(screen_name != "Industry Portal")
        ):
            st.session_state.screen = screen_name

    st.markdown("---")

    st.markdown(
        '<div class="status-card">'
        '<div class="small-label">DIGITAL TWIN STATUS</div>'
        '<b>● STANDBY</b>'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# INDUSTRY PORTAL
# =========================================================

if st.session_state.screen == "Industry Portal":

    st.markdown("""
    <div class="portal-header">

    <h1>🌱 BIOROOT</h1>

    <p>
    AI-Enabled Digital Twin for Circular Wastewater Treatment
    </p>

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
    # HYDRAULIC CONFIGURATION
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
            "Existing pipe diameter",
            min_value=20.0,
            max_value=2000.0,
            value=150.0,
            step=10.0
        )

        pipe_length = st.number_input(
            "Available pipe length",
            min_value=1.0,
            max_value=500.0,
            value=20.0,
            step=1.0
        )

    with col2:
        flow_rate = st.number_input(
            "Wastewater flow rate",
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
    # OPTIONAL WATER QUALITY INFORMATION
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-card">'
        '<h3>🧪 Wastewater Characterization</h3>'
        '<p>Optional measurements can be entered when available from '
        'facility laboratory analysis.</p>'
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
            "operate using the selected application profile and system "
            "parameters for this prototype."
        )


    st.markdown("---")


    # -----------------------------------------------------
    # INITIALIZE
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

        st.session_state.initialized = True

        st.success(
            f"Facility {facility_id} successfully configured. "
            "Digital-twin environment initialized."
        )

        st.session_state.screen = "Optimized Prediction"

        st.rerun()


# =========================================================
# PLACEHOLDER SCREENS
# =========================================================

else:

    st.title(f"🌱 {st.session_state.screen}")

    st.info(
        "This module will be built in the next development step."
    )

    if st.button("← Back to Industry Portal"):
        st.session_state.screen = "Industry Portal"
        st.rerun()
