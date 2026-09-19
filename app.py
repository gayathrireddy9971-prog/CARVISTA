import os
import json
import joblib
import pandas as pd
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CARVISTA | Used Car Price Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "carvista_rf_pipeline.joblib"
)

METADATA_PATH = os.path.join(
    BASE_DIR,
    "models",
    "carvista_metadata.json"
)


# ============================================================
# LOAD MODEL + METADATA
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_metadata():
    with open(METADATA_PATH, "r") as f:
        return json.load(f)


model = load_model()
metadata = load_metadata()

reference_year = metadata["reference_year"]
categorical_values = metadata["categorical_values"]
brand_model_map = metadata["brand_model_map"]


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN PAGE
       ===================================================== */

    .stApp {
    background:
        /* Top-left futuristic blue glow */
        radial-gradient(
            circle at 8% 12%,
            rgba(0, 132, 255, 0.24),
            transparent 24%
        ),

        /* Top-right cyan glow */
        radial-gradient(
            circle at 92% 8%,
            rgba(0, 195, 255, 0.16),
            transparent 22%
        ),

        /* Center blue atmosphere */
        radial-gradient(
            circle at 50% 45%,
            rgba(0, 82, 180, 0.10),
            transparent 38%
        ),

        /* Bottom futuristic glow */
        radial-gradient(
            circle at 50% 100%,
            rgba(0, 110, 255, 0.14),
            transparent 32%
        ),

        /* Subtle tech-grid effect */
        linear-gradient(
            rgba(40, 130, 210, 0.035) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(40, 130, 210, 0.035) 1px,
            transparent 1px
        ),

        /* Main deep-space background */
        linear-gradient(
            135deg,
            #02050c 0%,
            #061326 45%,
            #020711 100%
        );

    background-size:
        auto,
        auto,
        auto,
        auto,
        45px 45px,
        45px 45px,
        auto;

    background-attachment: fixed;

    color: #f4f8ff;
}


    /* =====================================================
       WIDE CONTENT
       ===================================================== */

    .block-container {
        max-width: 1600px !important;

        padding-top: 2.5rem !important;
        padding-left: 3.5rem !important;
        padding-right: 3.5rem !important;
        padding-bottom: 3rem !important;
    }


    /* =====================================================
       TITLE
       ===================================================== */

    .carvista-title {
        text-align: center;

        font-size: 4.4rem;
        font-weight: 950;

        letter-spacing: 10px;

        color: #ffffff;

        margin-bottom: 0.2rem;

        text-shadow:
            0 0 6px rgba(255,255,255,0.85),
            0 0 14px rgba(50,160,255,0.95),
            0 0 28px rgba(0,120,255,0.90),
            0 0 55px rgba(0,90,255,0.65);
    }


    .carvista-subtitle {
        text-align: center;

        color: #a9c8ec;

        font-size: 1.05rem;

        letter-spacing: 2px;

        margin-bottom: 1.2rem;
    }


    .blue-line {
        height: 3px;

        width: 170px;

        margin: 0 auto 2.8rem auto;

        border-radius: 20px;

        background:
            linear-gradient(
                90deg,
                transparent,
                #1687ff,
                #70c5ff,
                #1687ff,
                transparent
            );

        box-shadow:
            0 0 12px rgba(20,130,255,0.8);
    }


    /* =====================================================
       INPUT CARD
       ===================================================== */

    .input-card {
        background:
            linear-gradient(
                145deg,
                rgba(9,25,47,0.94),
                rgba(4,16,31,0.94)
            );

        border: 1px solid rgba(68,145,230,0.30);

        border-radius: 22px;

        padding: 1.7rem 1.8rem 1.3rem 1.8rem;

        box-shadow:
            0 18px 55px rgba(0,0,0,0.30),
            inset 0 1px 0 rgba(255,255,255,0.04);
    }


    .section-title {
        font-size: 1.5rem;

        font-weight: 850;

        color: #ffffff;

        margin-bottom: 0.3rem;
    }


    .section-description {
        color: #91afd1;

        font-size: 0.92rem;

        margin-bottom: 1.4rem;
    }


    /* =====================================================
       LABELS
       ===================================================== */

    label {
        color: #dcecff !important;

        font-weight: 650 !important;
    }


    /* =====================================================
       SELECT BOXES
       ===================================================== */

    div[data-baseweb="select"] > div {
        background-color: #0b1c33 !important;

        border: 1px solid #294e78 !important;

        border-radius: 10px !important;

        color: white !important;
    }


    div[data-baseweb="select"] > div:hover {
        border-color: #1687ff !important;

        box-shadow:
            0 0 10px rgba(0,130,255,0.18);
    }


    /* =====================================================
       NUMBER INPUTS
       ===================================================== */

    div[data-testid="stNumberInput"] input {
        background-color: #0b1c33 !important;

        color: white !important;

        border: 1px solid #294e78 !important;

        border-radius: 10px !important;
    }


    div[data-testid="stNumberInput"] input:focus {
        border-color: #1687ff !important;

        box-shadow:
            0 0 10px rgba(0,130,255,0.18) !important;
    }


    /* =====================================================
       CAR AGE
       ===================================================== */

    .age-box {
        background:
            linear-gradient(
                135deg,
                rgba(13,58,97,0.75),
                rgba(6,29,54,0.85)
            );

        border: 1px solid rgba(56,143,229,0.38);

        border-radius: 12px;

        padding: 0.85rem 1rem;

        margin-top: 1rem;
        margin-bottom: 0.4rem;

        color: #b9d8f8;

        font-size: 0.92rem;
    }


    .age-value {
        color: #ffffff;

        font-size: 1.15rem;

        font-weight: 850;

        margin-left: 5px;
    }


    /* =====================================================
       PREDICT BUTTON
       ===================================================== */

    div.stButton {
        width: 100%;

        margin-top: 1.6rem;
    }


    div.stButton > button {
        width: 100% !important;

        min-height: 60px;

        border-radius: 14px;

        border: 1px solid rgba(90,180,255,0.40);

        background:
            linear-gradient(
                135deg,
                #087cf5,
                #075bd1
            );

        color: white !important;

        font-size: 1.1rem;

        font-weight: 900 !important;

        letter-spacing: 0.7px;

        box-shadow:
            0 10px 30px rgba(0,104,255,0.35);

        transition: all 0.2s ease;
    }


    div.stButton > button:hover {
        background:
            linear-gradient(
                135deg,
                #1590ff,
                #0867e6
            );

        border-color: #65bdff;

        box-shadow:
            0 12px 38px rgba(0,125,255,0.50);

        transform: translateY(-2px);
    }


    div.stButton > button p {
        color: white !important;

        font-weight: 900 !important;
    }


    /* =====================================================
       SUCCESS MESSAGE
       ===================================================== */

    div[data-testid="stAlert"] {
        margin-top: 1.2rem;

        border-radius: 12px;
    }


    /* =====================================================
       PREDICTION RESULT
       ===================================================== */

    .prediction-wrapper {
        margin-top: 1.6rem;

        padding: 1.8rem;

        text-align: center;

        border-radius: 20px;

        background:
            linear-gradient(
                135deg,
                rgba(8,73,137,0.82),
                rgba(7,39,76,0.94)
            );

        border: 1px solid rgba(74,169,255,0.48);

        box-shadow:
            0 18px 50px rgba(0,75,170,0.25);
    }


    .prediction-label {
        color: #b0d0ef;

        font-size: 0.95rem;

        margin-bottom: 0.5rem;
    }


    .prediction-value {
        color: #ffffff;

        font-size: 3rem;

        font-weight: 950;

        line-height: 1.15;

        text-shadow:
            0 0 12px rgba(80,180,255,0.60),
            0 0 28px rgba(40,150,255,0.35);
    }


    .prediction-note {
        color: #9ebddd;

        font-size: 0.8rem;

        margin-top: 0.6rem;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        text-align: center;

        color: #607b9d;

        font-size: 0.78rem;

        margin-top: 2.8rem;

        letter-spacing: 0.5px;
    }


    /* =====================================================
       HIDE STREAMLIT DEFAULT UI
       ===================================================== */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="carvista-title">CARVISTA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="carvista-subtitle">'
    'USED CAR PRICE INTELLIGENCE & PREDICTION'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="blue-line"></div>',
    unsafe_allow_html=True
)


# ============================================================
# VEHICLE INFORMATION
# ============================================================

st.markdown(
    '<div class="input-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">Vehicle Information</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Enter the details of the used car to estimate its market value.'
    '</div>',
    unsafe_allow_html=True
)


# IMPORTANT:
# These columns now use the full available page width.

left_col, right_col = st.columns(
    [1, 1],
    gap="large"
)


# ============================================================
# LEFT COLUMN
# ============================================================

with left_col:

    brand = st.selectbox(
        "Brand",
        categorical_values["Brand"]
    )

    available_models = brand_model_map.get(
        brand,
        categorical_values["Car_Model"]
    )

    car_model = st.selectbox(
        "Car Model / Variant",
        available_models
    )

    location = st.selectbox(
        "Location",
        categorical_values["Location"]
    )

    fuel_type = st.selectbox(
        "Fuel Type",
        categorical_values["Fuel_Type"]
    )

    transmission = st.selectbox(
        "Transmission",
        categorical_values["Transmission"]
    )

    owner_type = st.selectbox(
        "Owner Type",
        categorical_values["Owner_Type"]
    )


# ============================================================
# RIGHT COLUMN
# ============================================================

with right_col:

    year_min = int(
        metadata["numerical_ranges"]["Year"]["min"]
    )

    year_max = int(
        metadata["numerical_ranges"]["Year"]["max"]
    )

    year = st.number_input(
        "Manufacturing Year",
        min_value=year_min,
        max_value=year_max,
        value=2017,
        step=1
    )

    kilometers = st.number_input(
        "Kilometers Driven",
        min_value=0.0,
        max_value=float(
            metadata["numerical_ranges"]["Kilometers_Driven"]["max"]
        ),
        value=50000.0,
        step=1000.0
    )

    mileage = st.number_input(
        "Mileage (km/l)",
        min_value=0.1,
        max_value=float(
            metadata["numerical_ranges"]["Mileage"]["max"]
        ),
        value=18.0,
        step=0.1
    )

    engine = st.number_input(
        "Engine (CC)",
        min_value=1.0,
        max_value=float(
            metadata["numerical_ranges"]["Engine"]["max"]
        ),
        value=1200.0,
        step=50.0
    )

    power = st.number_input(
        "Power (BHP)",
        min_value=1.0,
        max_value=float(
            metadata["numerical_ranges"]["Power"]["max"]
        ),
        value=80.0,
        step=5.0
    )

    seats = st.number_input(
        "Seats",
        min_value=int(
            metadata["numerical_ranges"]["Seats"]["min"]
        ),
        max_value=int(
            metadata["numerical_ranges"]["Seats"]["max"]
        ),
        value=5,
        step=1
    )


# ============================================================
# CAR AGE
# ============================================================

car_age = reference_year - int(year)

st.markdown(
    f"""
    <div class="age-box">
        Calculated Car Age:
        <span class="age-value">{car_age} years</span>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# PREDICTION BUTTON
# ============================================================

predict_clicked = st.button(
    "PREDICT USED CAR PRICE",
    use_container_width=True
)


# ============================================================
# PREDICTION
# ============================================================

if predict_clicked:

    input_data = pd.DataFrame(
        {
            "Location": [location],
            "Fuel_Type": [fuel_type],
            "Transmission": [transmission],
            "Owner_Type": [owner_type],
            "Year": [year],
            "Kilometers_Driven": [kilometers],
            "Mileage": [mileage],
            "Engine": [engine],
            "Power": [power],
            "Seats": [seats],
            "Car_Age": [car_age],
            "Brand": [brand],
            "Car_Model": [car_model]
        }
    )

    prediction = model.predict(input_data)[0]


    # --------------------------------------------------------
    # SUCCESS MESSAGE
    # --------------------------------------------------------

    st.success(
        "Prediction generated successfully!"
    )


    # --------------------------------------------------------
    # PREDICTION RESULT
    # --------------------------------------------------------

    st.html(
    f"""
    <div class="prediction-wrapper">

        <div class="prediction-label">
            Estimated Used Car Price
        </div>

        <div class="prediction-value">
            ₹ {prediction:.2f} Lakhs
        </div>

        <div class="prediction-note">
            Estimated by the CARVISTA machine-learning model
        </div>

    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        CARVISTA • Used Car Price Intelligence & Prediction
    </div>
    """,
    unsafe_allow_html=True
)