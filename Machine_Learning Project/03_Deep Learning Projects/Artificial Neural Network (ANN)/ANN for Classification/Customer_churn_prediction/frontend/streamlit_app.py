import streamlit as st
from api_client import predict_churn
from pathlib import Path


st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🙎‍♂️",
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
    <h1>Customer_churn__prediction System</h1>
    <p>Predict if customer leaves or stayes using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Personal Info
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">personal Info</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
        
    with col1:
        gender = st.selectbox(
        "Gender",
        ["Male","Female"],
        index=None,
        placeholder="Choose Option"
)


  
    with col2:
        SeniorCitizen = st.selectbox(
        "Senior Citizen",
        ["Yes","No"],
        index=None,
        placeholder="Choose Option"
)


    col3, col4 = st.columns(2)
        
    with col3:
        Partner = st.selectbox(
        "Partner",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

    with col4:
        Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)



  
    st.markdown(
        '<div class="section-title">Telephony Services</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
            
    with col1:
        PhoneService = st.selectbox(
        "Phone Service",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)
  
    with col2:
        MultipleLines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)



    # -------------------------------
    # Internet & Add-on Services
    # -------------------------------

    st.markdown(
    '<div class="section-title">Internet & Add-on Services</div>',
    unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        InternetService_status = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"],
        index=None,
        placeholder="Choose Option"
)
  
    with col2:
        OnlineBackup = st.selectbox(
        "Online Backup",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

      
    with col3:
        OnlineSecurity = st.selectbox(
        "Online Security",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
) 


    col4, col5 = st.columns(2)

    with col4:
        DeviceProtection = st.selectbox(
        "Device Protection",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

      
    with col5:
        TechSupport = st.selectbox(
        "Tech Support",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
) 


    
    col6, col7 = st.columns(2)
  
    with col6:
        StreamingTV = st.selectbox(
        "Streaming TV",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

    with col7:
        StreamingMovies = st.selectbox(
        "Streaming Movies",
        ["Yes","No"],
        index=None,
        placeholder="Choose Option"
)


    
    st.markdown(
        '<div class="section-title">Account Info</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
        
    with col1:
        tenure = st.number_input(
        "tenure",
        value=None,
        placeholder="Enter years customer has stayed with the business (e.g. 5 represent 5years)")


  
    with col2:
        Contract_status = st.selectbox(
        "Contract",
        ["One year", "Two year", "Month-to-month"],
        index=None,
        placeholder="Choose Contract"

          

    st.markdown(
        '<div class="section-title"> Financial & Billing Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
        
    with col1:
        PaperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

  
    with col2:
        PaymentMethod_status = st.selectbox(
        "Payment Method",
        ["Credit card (automatic)", "Electronic check", "Mailed check", "Bank transfer (automatic)"],
        index=None,
        placeholder="Choose Contract"


    col3, col4 = st.columns(2)
        
    with col3:
        MonthlyCharges = st.number_input(
        "Monthly Charges",
        value=None,
        format="%.2f",
        placeholder="Enter Monthly Charges (e.g. 29.85)")

    with col4:
        TotalCharges = st.number_input(
        "Total Charges",
        value=None,
        format="%.2f",
        placeholder="Enter the total charges (e.g. 29.85)")




  

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Customer Status",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if TotalCharges is None:
        missing_fields.append("Total Charges")

    if MonthlyCharges is None:
        missing_fields.append("Monthly Charges")

    if tenure is None:
        missing_fields.append("Employment experience")

    if gender is None:
        missing_fields.append("Gender")

    if SeniorCitizen is None:
        missing_fields.append("Senior Citizen")

    if Partner is None:
        missing_fields.append("Partner")

    if Dependents is None:
        missing_fields.append("Dependents")

    if PhoneService is None:
        missing_fields.append("Phone Service")

    if MultipleLines is None:
        missing_fields.append("Multiple Lines")

    if InternetService_status is None:
        missing_fields.append("Internet Service")

    if OnlineBackup is None:
        missing_fields.append("Online Backup")

    if OnlineSecurity is None:
        missing_fields.append("Online Security")

    if DeviceProtection is None:
        missing_fields.append("Device Protection")

    if TechSupport is None:
        missing_fields.append("Tech Support")

    if StreamingTV is None:
        missing_fields.append("Streaming TV")

    if StreamingMovies is None:
        missing_fields.append("Streaming Movies")

    if Contract_status is None:
        missing_fields.append("Contract")

    if PaperlessBilling is None:
        missing_fields.append("Paperless Billing")

    if PaymentMethod_status is None:
        missing_fields.append("Payment Method")
  
    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "PaperlessBilling": PaperlessBilling,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "PaymentMethod_status": PaymentMethod_status,
        "Contract_status": Contract_status,
        "InternetService_status": InternetService_status
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_churn(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Prediction Result</h3>
        <p><strong>Customer_Status:</strong> {result['prediction_class']}</p>
        <p><strong>Probability:</strong> {result['probability']:.2%}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
