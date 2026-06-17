import streamlit as st
from api_client import (predict_house_price, get_options)

st.set_page_config(
    page_title="House_price_prediction",
    page_icon="🏠",
    layout="wide")


@st.cache_data
def load_options():
    return get_options()

options = load_options()


address_and_city = options["Address_And_City"]
state = options["State"]
county = options["County"]

def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
        
load_css()


st.markdown("""
<div class="main-header">
    <h1>House_price_prediction System</h1>
    <p>Predict the price of house using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# House Information
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">House Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        Bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=54,
        value=None,
        placeholder="Enter No of Bedrooms (e.g. 5)")

    with col2:
        Bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=66,
        value=None,
        placeholder="Enter No of Bathrooms (e.g. 5)")
      

            
    col3, col4 = st.columns(2)

    with col3:
        Living_Space = st.number_input(
        "Living Space",
        value=None,
        placeholder="Enter Living_Space size sq. ft. (e.g. 1538)")

  
    with col4:
        Median_Household_Income = st.number_input(
        "Median Household Income",
        value=None,
        format="%.2f",
        placeholder="Enter Median Household Income $ (e.g. 370046.00)")
      


    col5, col6 = st.columns(2)

    with col5:
        Zip_Code = st.number_input(
        "Zip Code",
        value=None,
        placeholder="Enter  Zip Code. (e.g. 1538)")

  
    with col6:
        Latitude = st.number_input(
        "Latitude",
        value=None,
        format="%.2f",
        placeholder="Enter Latitude. (e.g. 40.72)")


  
    col7, col8 = st.columns(2)

    with col7:
        Longitude = st.number_input(
        "Longitude",
        value=None,
        format="%.2f",
        placeholder="Enter  Longitude (e.g. 74.00)")

  
    with col8:
        Address_And_City = st.selectbox(
        "Address and city",
        address_and_city)

  

    col9, col10 = st.columns(2)
  
    with col9:
        State = st.selectbox(
        "State",
        state)

    with col10:
        County = st.selectbox(
        "County",
        county)


# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict House Price",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if Bedrooms is None:
        missing_fields.append("Bedrooms")

    if Bathrooms is None:
        missing_fields.append("Bathrooms")

    if Living_Space is None:
        missing_fields.append("Living Space")

    if Median_Household_Income is None:
        missing_fields.append("Median Household Income")

    if Zip_Code is None:
        missing_fields.append("Zip Code")

    if Latitude is None:
        missing_fields.append("Latitude")

    if Longitude is None:
        missing_fields.append("Longitude")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "Bedrooms": Bedrooms,
        "Bathrooms": Bathrooms,
        "Living_Space": Living_Space,
        "Median_Household_Income": Median_Household_Income,
        "Zip_Code": Zip_Code,
        "Latitude": Latitude,
        "Longitude": Longitude,
        "Address_And_City": Address_And_City,
        "State": State,
        "County": County
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_house_price(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Estimated House Price",
            value=f"${result['House_price']:,.2f}")

    except Exception as e:
        st.error(str(e))
