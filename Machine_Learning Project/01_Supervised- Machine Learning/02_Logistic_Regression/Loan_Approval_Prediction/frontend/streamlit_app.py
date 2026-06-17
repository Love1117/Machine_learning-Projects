import streamlit as st
from api_client import (loan_approval, get_options)

st.set_page_config(
    page_title="House_price_prediction",
    page_icon="🏠",
    layout="wide")


@st.cache_data
def load_options():
    return get_options()

options = load_options()


loan_intent = options["Loan_intent"]
home_ownership = options["Home_ownership"]


def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
        
load_css()


st.markdown("""
<div class="main-header">
    <h1>Loan_approval_prediction System</h1>
    <p>Predict user Loan status using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Personal Information
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">personal Information</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input(
        "Age",
        value=None,
        placeholder="Enter your Age (e.g. 48)")

    with col2:
        Gender = st.selectbox(
        "Gender",
        ["Male","Female"])
      
    with col3:
        Education = st.selectbox(
        "Education",
        ["High School", "Associate", "Bachelor", "Master", "Doctorate"])

    
    col4, col5, col6 = st.columns(3)
    with col4:
        Income = st.number_input(
        "Income",
        value=None,
        format="%.2f",
        placeholder="Enter Income $. (e.g. 66135.0)")
  
    with col5:
        Employment_experience = st.number_input(
        "Employment experience",
        value=None,
        format="%.2f",
        placeholder="Enter your years of employment experience (e.g. 25)")

    with col6:
        Home_ownership = st.selectbox(
        "Home ownership",
        home_ownership)
      


    # -------------------------------
    # Loan information
    # -------------------------------

    st.markdown(
    '<div class="section-title">Loan Information</div>',
    unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        Loan_amount = st.number_input(
        "Loan amount",
        value=None,
        format="%.2f",
        placeholder="Enter Loan amount $ (e.g. 35000.0)")

    with col2:
        Loan_intent = st.selectbox(
        "Loan intent",
        loan_intent)
      
    with col3:
        Loan_interest_rate = st.number_input(
        "Loan interest rate",
        value=None,
        format="%.2f",
        placeholder="Enter Loan interset rate % (e.g. 6.25)")



    col4, col5 = st.columns(2)

    with col4:
        Loan_percent_income = st.number_input(
        "Loan percent income",
        value=None,
        format="%.2f",
        placeholder="Enter  Loan percent income % (e.g. o.25)")

  
    with col5:
        Credit_history_length = st.number_input(
        "Credit history length",
        min_value=2,
        max_value=30
        value=None,
        placeholder="Enter your Credit history length (e.g. 5)")


    
    col6, col7 = st.columns(2)
  
    with col6:
        Credit_score = st.number_input(
        "Credit score",
        value=None,
        placeholder="Enter your Credit score (e.g. 586)")

    with col7:
        Previous_loan_defaults_on_file = st.selectbox(
        "Previous loan defaults on file",
        ["Yes","No"])


# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Loan Approval",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if Age is None:
        missing_fields.append("Age")

    if Income is None:
        missing_fields.append("Income")

    if Employment_experience is None:
        missing_fields.append("Employment experience")

    if Loan_amount is None:
        missing_fields.append("Loan amount")

    if Loan_interest_rate is None:
        missing_fields.append("Loan interest rate")

    if Loan_percent_income is None:
        missing_fields.append("Loan percent income")

    if Credit_history_length is None:
        missing_fields.append("Credit history length")

    if Credit_score is None:
        missing_fields.append("Credit score")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "Age": Age,
        "Gender": Gender,
        "Education": Education,
        "Income": Income,
        "Employment_experience": Employment_experience,
        "Home_ownership": Home_ownership,
        "Loan_amount": Loan_amount,
        "Loan_intent": Loan_intent,
        "Loan_interest_rate": Loan_interest_rate,
        "Loan_percent_income": Loan_percent_income,
        "Credit_history_length": Credit_history_length,
        "Credit_score": Credit_score,
        "Previous_loan_defaults_on_file": Previous_loan_defaults_on_file
    }


    try:
        with st.spinner("Generating prediction..."):
            result = loan_approval(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="loan_Status",
            value=f"${result['prediction']:,.2f}")

    except Exception as e:
        st.error(str(e))
