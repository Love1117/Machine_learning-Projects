import streamlit as st
from api_client import (predict_salary, get_options)
from pathlib import Path


st.set_page_config(
    page_title="Employee_salary_prediction",
    page_icon="👔",
    layout="wide")


@st.cache_data
def load_options():
    return get_options()

options = load_options()


country = options["Country"]
racism = options["Race"]
job_title = options["Job_title"]

def load_css():
    css_path = Path(__file__).parent / "styles.css"
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True)
        
load_css()



st.markdown("""
<div class="main-header">
    <h1>Employee_salary_prediction System</h1>
    <p>Predict Employee Salary using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Personal Information
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Personal Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input(
        "Age",
        value=None,
        placeholder="Enter Age (e.g. 35)")
        
    with col2:
        Gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        index=None,
        placeholder="Type Or Select Gender"
)

    with col3:
        Education_Level = st.number_input(
        "Education Level",
        min_value=0,
        max_value=3,
        value=None,
        placeholder="Enter Education_Level (e.g. 3)")

            
    col4, col5 = st.columns(2)

    with col4:
        Country = st.selectbox(
        "Country",
        country,
        index=None,
        placeholder="Type or Select Country"
)

    with col5:
        Race = st.selectbox(
        "Racism",
        racism,
        index=None,
        placeholder="Type Or Select Segregation"
)



# -------------------------------
# Employment Details
# -------------------------------

    st.markdown(
    '<div class="section-title">Employment Details</div>',
    unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        Job_title = st.selectbox(
        "Job Title",
        job_title,
        index=None,
        placeholder="Type Or Select Job_title"
)

    with col2:
        Years_of_Experience = st.number_input(
        "Years of Experience",
        min_value=0,
        max_value=32,
        value=None,
        placeholder="Enter Years_of_Experience (e.g. 10)")

    with col3:
        Senior = st.selectbox(
        "Senior Employee",
        ["Yes", "No"],
        index=None,
        placeholder="Type Or Select Senior Employee"
)

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Salary",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if Age is None:
        missing_fields.append("Age")

    if Education_Level is None:
        missing_fields.append("Education Level")

    if Years_of_Experience is None:
        missing_fields.append("Years of Experience")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()

    
    
    payload = {
        "Age": Age,
        "Gender": Gender,
        "Education_Level": Education_Level,
        "Years_of_Experience": Years_of_Experience,
        "Country": Country,
        "Race": Race,
        "Senior": Senior,
        "Job_title": Job_title
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_salary(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Estimated Employee Salary",
            value=f"${result['Employee_Salary']:,.2f}")

    except Exception as e:
        st.error(str(e))
