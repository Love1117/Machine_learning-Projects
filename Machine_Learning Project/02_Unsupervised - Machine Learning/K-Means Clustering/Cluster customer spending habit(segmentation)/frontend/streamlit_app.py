import streamlit as st
from api_client import predict_spend_habit
from pathlib import Path


st.set_page_config(
    page_title="Customers Spending Habit Prediction",
    page_icon="💳",
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
    <h1>Customers_Spending_Habit</h1>
    <p>Predict customers spending habit using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Demographic Features
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Demographic Features</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        Gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        index=None,
        placeholder="Select Gender"
)


    with col2:
        Age = st.number_input(
        "Age",
        value=None,
        help="Enter Age (e.g. 44)")
      
            
    col3, col4 = st.columns(2)

    with col3:
        Ever_Married  = st.selectbox(
        "Ever Married",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

  
    with col4:
        Family_Size = st.number_input(
        "Family Size",
        value=None,
        format="%.2f",
        help="Enter Family Size (e.g. 3.0 )")



  
    st.markdown(
        '<div class="section-title">Education & Career Features</div>',
        unsafe_allow_html=True)
      
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Graduated  = st.selectbox(
        "Graduated",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

      
    with col2:
        Profession_status = st.selectbox(
        "Profession",
        ["Doctor", "Engineer", "Entertainment", "Executive", "Healthcare", "Homemaker", "Lawyer", "Marketing", "Artist"],
        index=None,
        placeholder="search profession"
)
    
    with col3:
        Work_Experience = st.number_input(
        "Work Experience",
        value=None,
        format="%.2f",
        help="Enter Work Experience (e.g. 8 years and 6 Months (8.6) )")


  
    st.markdown(
        '<div class="section-title">Behavioral Features</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        Spending_Score  = st.number_input(
        "Spending Score",
        value=None,
        help="Enter Spending Score (e.g. 3)")


    with col2:
        Variable_status = st.selectbox(
        "Variable status",
        ["Cat_1", "Cat_2", "Cat_3", "Cat_4", "Cat_5", "Cat_6", "Cat_7"],
        index=None,
        placeholder="Select category"
)

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Customer Spending Habit",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if Gender is None:
        missing_fields.append("Gender")

    if Age is None:
        missing_fields.append("Age")

    if Ever_Married is None:
        missing_fields.append("Ever Married")

    if Family_Size is None:
        missing_fields.append("Family Size")

    if Graduated is None:
        missing_fields.append("Graduated")

    if Profession_status is None:
        missing_fields.append("Profession")

    if Work_Experience is None:
        missing_fields.append("Work Experience")

    if Spending_Score is None:
        missing_fields.append("Spending Score")

    if Variable_status is None:
        missing_fields.append("Variable status")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "Gender": Gender,
        "Age": Age,
        "Ever_Married": Ever_Married,
        "Family_Size": Family_Size,
        "Graduated": Graduated,
        "Profession_status": Profession_status,
        "Work_Experience": Work_Experience,
        "Spending_Score": Spending_Score,
        "Variable_status": Variable_status,
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_spend_habit(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Falls_into",
            value=f"{result['prediction']}")

    except Exception as e:
        st.error(str(e))
