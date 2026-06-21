import streamlit as st
from api_client import (predict_car, get_car_models, get_car_names)
from pathlib import Path


st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide")


@st.cache_data
def load_models():
    return get_car_models()["car_model_and_year"]

@st.cache_data
def load_car_names():
    return get_car_names()["car_names"]

models = load_models()
car_names = load_car_names()


def load_css():
    css_path = Path(__file__).parent / "styles.css"
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True)
        
load_css()


st.markdown("""
<div class="main-header">
    <h1>🚗 Car Price Prediction System</h1>
    <p>Predict the market value of used vehicles using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Vehicle Information
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Vehicle Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
        
    with col1:
        car_ModelAndYear = st.selectbox(
            "Select Car_Model & Year",
            models,
            index=None,
            placeholder="type or Select Car_Model & Year"
)

    with col2:
        car_name = st.selectbox(
            "Select Car_Name",
             car_names,
             index=None,
             placeholder="Type or Select Car_Name"
)

    col3, col4 = st.columns(2)

    with col3:
        year = st.number_input(
        "Year",
        min_value=1990,
        max_value=2030,
        value=None,
        help="Enter Year (e.g. 2015)"
    )

    with col4:
        transmission = st.selectbox(
            "Transmission",
            ["Manual", "Automatic"],
            index=None,
            placeholder="Select Transmission..."
)


# -------------------------------
# Specifications
# -------------------------------

    st.markdown(
    '<div class="section-title">Technical Specifications</div>',
    unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        mileage = st.number_input(
        "Mileage",
        value=None,
        format="%.2f",
        help="Enter mileage (e.g. 20.0)")

    with col2:
        engine = st.number_input(
        "Engine Capacity",
        value=None,
        format="%.2f",
        help="Enter engine capacity (e.g. 1200.0)")

    with col3:
        max_power = st.number_input(
        "Max Power",
        value=None,
        format="%.2f",
        help="Enter max_power (e.g. 80.0)")

    col4, col5 = st.columns(2)

    with col4:
        seats = st.number_input(
        "Seats",
        min_value=1,
        value=None,
        help="Enter No of seats (e.g. 5)")

    with col5:
        km_driven = st.number_input(
        "KM Driven",
        value=None,
        format="%.2f",
        help="Enter Km driven (e.g. 50000)")


# -------------------------------
# Ownership
# -------------------------------

    st.markdown(
    '<div class="section-title">Ownership Information</div>',
    unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        fuel = st.selectbox(
        "Fuel Type",
        ["Diesel", "Petrol", "LPG", "CNG"],
        index=None,
        placeholder="Select fuel_type"
)

    with col2:
        owner = st.selectbox(
        "Owner Type",
        ["First Owner",
            "Second Owner",
            "Third Owner",
            "Fourth & Above Owner",
            "Test Drive Car"
        ],
        index=None,
        placeholder="Select Owner type..."
)

    with col3:
        seller_type = st.selectbox(
        "Seller Type",
        [
            "Individual",
            "Dealer",
            "Trustmark Dealer"
        ],
        index=None,
        placeholder="Select seller type"
)

# -------------------------------
# Prediction Button
# -------------------------------

    submit = st.form_submit_button(
    "🚗 Predict Car Price",
    use_container_width=True)

    
if submit:

    payload = {
        "car_ModelAndYear": car_ModelAndYear,
        "car_name": car_name,
        "year": year,
        "km_driven": km_driven,
        "transmission": transmission,
        "mileage": mileage,
        "engine": engine,
        "max_power": max_power,
        "seats": seats,
        "fuel": fuel,
        "owner": owner,
        "seller_type": seller_type
    }

    missing_fields = []

    if car_ModelAndYear is None:
        missing_fields.append("Select Car_Model & Year")

    if car_name is None:
        missing_fields.append("Select Car_Name")

    if year is None:
        missing_fields.append("Year")

    if transmission is None:
        missing_fields.append("Transmission")

    if mileage is None:
        missing_fields.append("Mileage")

    if engine is None:
        missing_fields.append("Engine Capacity")

    if max_power is None:
        missing_fields.append("Max Power")

    if seats is None:
        missing_fields.append("Seats")

    if km_driven is None:
        missing_fields.append("KM Driven")

    if fuel is None:
        missing_fields.append("Fuel Type")

    if owner is None:
        missing_fields.append("Owner Type")

    if seller_type is None:
        missing_fields.append("Seller Type")

    if missing_fields:
        st.warning(
        f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
    )
        st.stop()
           
    try:
        with st.spinner("Generating prediction..."):
             result = predict_car(payload)

        st.success("Prediction Generated Successfully")

        st.markdown(
        '<div class="prediction-card">Prediction</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Estimated Car Price",
            value=f"${result['Car_Price']:,.2f}")

    except Exception as e:
        st.error(str(e))
