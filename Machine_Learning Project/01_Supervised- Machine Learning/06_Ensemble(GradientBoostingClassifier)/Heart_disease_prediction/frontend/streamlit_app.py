import streamlit as st
from api_client import predict_disease
from pathlib import Path


st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="💌",
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
    <h1>Heart_disease_prediction_System</h1>
    <p>Predict if a heart disease exist using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Personal Info
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Personal Info</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox(
        "Gender",
        ["Male","Female"],
        index=None,
        placeholder="Select Gender"
)

    with col2:
        age = st.number_input(
        "Age",
        value=None,
        placeholder="Enter your age (e.g. 50)")


  
    
    st.markdown(
        '<div class="section-title">Health  Metrics</div>',
        unsafe_allow_html=True
    )
            
    col1, col2 = st.columns(2)

    with col1:
        height = st.number_input(
        "Height",
        value=None,
        format="%.2f",
        placeholder="Enter hieght CM. (e.g. 168.0)")

  
    with col2:
        weight = st.number_input(
        "Weight",
        value=None,
        format="%.2f",
        placeholder="Enter hieght CM. (e.g. 62.0)")
      


    col3, col4, col5 = st.columns(3)
  
    with col3:
        bmi = st.number_input(
        "Bmi",
        value=None,
        format="%.2f",
        placeholder="Enter  Bmi. (e.g. 21.967120)")

  
    with col4:
        systolic_blood_pressure = st.number_input(
        "Systolic Blood Pressure",
        value=None,
        placeholder="Enter Systolic Blood Pressure. (e.g. 110)")

    with col5:
        diastolic_blood_pressure = st.number_input(
        "Diastolic Blood Pressure",
        value=None,
        placeholder="Enter Diastolic Blood Pressure. (e.g. 80)")


  
  
    col6, col7, col8 = st.columns(3)

    with col6:
        bp_status = st.selectbox(
        "Hypertension",
        ["stage1", "stage2", "normal", "Elevated"],
        index=None,
        placeholder="Select Hypertension "
)

  
    with col7:
        cholesterol = st.number_input(
        "Cholesterol",
        value=None,
        placeholder="Enter Cholesterol (e.g. 1")

  
    with col8:
        gluc = st.number_input(
        "Glucose",
        value=None,
        placeholder="Enter Glucose (e.g. 1")



    st.markdown(
        '<div class="section-title">Lifestyle</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
  
    with col1:
        smoke = st.selectbox(
        "Smoke",
        ["Yes","No"],
        index=None,
        placeholder="Select OPtion"
)

    with col2:
        alcohol_intake = st.selectbox(
        "Alcohol Intake",
        ["Yes","No"],
        index=None,
        placeholder="Select Option"
)

    with col2:
        Physical_activity = st.selectbox(
        "Physical Activity",
        ["Yes","No"],
        index=None,
        placeholder="Select Option"
)


# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Heart Disease",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if gender is None:
        missing_fields.append("Gender")
    
    if age is None:
        missing_fields.append("Age")

    if height is None:
        missing_fields.append("Height")

    if weight is None:
        missing_fields.append("Weight")

    if bmi is None:
        missing_fields.append("Bmi")

    if diastolic_blood_pressure is None:
        missing_fields.append("Diastolic Blood Pressure")

    if systolic_blood_pressure is None:
        missing_fields.append("Systolic Blood Pressure")
    
    if bp_status is None:
        missing_fields.append("Hypertension")

    if cholesterol is None:
        missing_fields.append("Cholesterol")

    if gluc is None:
        missing_fields.append("Glucose")

    if smoke is None:
        missing_fields.append("Smoke")

    if alcohol_intake is None:
        missing_fields.append("Alcohol Intake")

    if physical_activity is None:
        missing_fields.append("Physical Activity")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "gender": gender,
        "height": height,
        "weight": weight,
        "systolic_blood_pressure": systolic_blood_pressure,
        "diastolic_blood_pressure": diastolic_blood_pressure,
        "cholesterol": cholesterol,
        "gluc": gluc,
        "smoke": smoke,
        "alcohol_intake": alcohol_intake,
        "Physical_activity": Physical_activity,
        "age": age,
        "bmi": bmi,
        "bp_status": bp_status
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_disease(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Heart_Disease",
            value=f"{result['Heart_Disease']}")

    except Exception as e:
        st.error(str(e))
