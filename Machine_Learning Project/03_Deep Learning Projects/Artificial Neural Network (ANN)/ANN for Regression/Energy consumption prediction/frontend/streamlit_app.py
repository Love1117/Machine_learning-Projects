import streamlit as st
from api_client import predict_energy_consumption
from pathlib import Path


st.set_page_config(
    page_title="Energy Consumption Prediction",
    page_icon="⚡",
    layout="wide")


def load_css():
    css_path = Path(__file__).parent / "styles.css"
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True)
        
load_css()



st.markdown("""
<div class="main-header">
    <h1>Energy Consumption Prediction</h1>
    <p>Predict price of energy consumed using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Structural & Household Info
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Structural & Household Info</div>',
        unsafe_allow_html=True
    )

    
    col1, col2 = st.columns(2)
        
    with col1:
        Home_ID = st.number_input(
        "Home ID",
        value=None,
        placeholder="Enter home id(e.g. 94)")

    
    with col2:
        Household_Size = st.number_input(
        "Household Size",
        value=None,
        placeholder="Enter household size. (e.g. 2)")


    
    st.markdown(
        '<div class="section-title">Weather Metrics & Appliance</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
            
    with col1:
        Outdoor_Temperature_C = st.number_input(
        "Outdoor Temperature_C",
        value=None,
        format="%.2f",
        placeholder="Enter household size. (e.g. 1.0)")
  
    with col2:
        Season_status = st.selectbox(
        "Season",
        ["Spring", "Summer", "Winter", "Fall"],
        index=None,
        placeholder="Choose Option"
)

    
    with col3:
        Appliance_Type_status = st.selectbox(
        "Appliance Type",
        ["Air Conditioning", "Computer", "Dishwasher", "Fridge", "Heater", "Lights", "Microwave", Oven", "TV", "Washing Machine"],
        index=None,
        placeholder="Choose Option"
)


    # -------------------------------
    # Time & Schedule
    # -------------------------------
    
    st.markdown(
    '<div class="section-title">Time & Schedule</div>',
    unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        Year = st.number_input(
        "Year",
        value=None,
        placeholder="Enter Year (e.g. 2024)")
  
    with col2:
        Month = st.number_input(
        "Month",
        value=None,
        placeholder="Enter Month (e.g. 5)")


  
    col3, col4 = st.columns(2)

    with col3:
        Day = st.number_input(
        "Day",
        value=None,
        placeholder="Enter day (e.g. 23)")
  
    with col4:
        Days_Of_The_Week = st.selectbox(
        "Days Of The Week",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        index=None,
        placeholder="Choose Option"
) 


    col5, col6 = st.columns(2)
  
    with col5:
        Hour = st.number_input(
        "Hour",
        value=None,
        placeholder="Enter hour (e.g. 2)")
  
    with col6:
        Weekend = st.selectbox(
        "Weekend",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"


# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Energy Price",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if Home_ID is None:
        missing_fields.append("Home ID")

    if Household_Size is None:
        missing_fields.append("Household Size")

    if Outdoor_Temperature_C is None:
        missing_fields.append("Outdoor Temperature_C")

    if Season_status is None:
        missing_fields.append("Season")

    if Appliance_Type_status is None:
        missing_fields.append("Appliance Type")

    if Year is None:
        missing_fields.append("Year")

    if Month is None:
        missing_fields.append("Month")

    if Day is None:
        missing_fields.append("Day")

    if Days_Of_The_Week is None:
        missing_fields.append("Days Of The Week")

    if Hour is None:
        missing_fields.append("Hour")

    if Weekend is None:
        missing_fields.append("Weekend")
  
    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "Home_ID": Home_ID,
        "Household_Size": Household_Size,
        "Outdoor_Temperature_C": Outdoor_Temperature_C,
        "Year": Year,
        "Month": Month,
        "Day": Day,
        "Days_Of_The_Week": Days_Of_The_Week,
        "Hour": Hour,
        "Weekend": Weekend,
        "Appliance_Type_status": Appliance_Type_status,
        "Season_status": Season_status
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_energy_consumption(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Prediction Result</h3>
        <p><strong>Energy_Consumption_(kWh):</strong> {result['prediction']:,.2f}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
