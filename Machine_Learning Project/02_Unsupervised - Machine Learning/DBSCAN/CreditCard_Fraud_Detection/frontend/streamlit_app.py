import streamlit as st
from api_client import predict_fraud
from pathlib import Path


st.set_page_config(
    page_title="Credit-Card Fraud Detection",
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
    <h1>Credit-card Fraud Detection</h1>
    <p>Predict Credit-card Fraud using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Transaction Data
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Transaction Data</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        step = st.number_input(
        "Step",
        value=None,
        help="Enter No of step (e.g. 183)")

    with col2:
        type_status = st.selectbox(
        "Select Payment Type",
        ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"],
        index=None,
        placeholder="Select payment type..."
)


    with col3:
        amount = st.number_input(
        "Amount",
        value=None,
        format="%.2f",
        help="Enter Amount $ (e.g. 22004.84)")
      


    st.markdown(
        '<div class="section-title">Sender Account Measures</div>',
        unsafe_allow_html=True
    )
            
    col1, col2 = st.columns(2)

    with col1:
        oldbalanceOrg = st.number_input(
        "Old Balance of Sender",
        value=None,
        format="%.2f",
        help="Enter balance of the sender before the transaction (e.g. 87956.18)")

  
    with col2:
        newbalanceOrig = st.number_input(
        "New Balance of Sender",
        value=None,
        format="%.2f",
        help="Enter balance of the sender after the transaction (e.g. 65951.34)")



  
    st.markdown(
        '<div class="section-title">Receiver Account Measures</div>',
        unsafe_allow_html=True
    )
            
    col1, col2 = st.columns(2)

    with col1:
        oldbalanceDest = st.number_input(
        "Old Balance of Receiver",
        value=None,
        format="%.2f",
        help="Enter old balance of receiver account (e.g. 0.00)")

  
    with col2:
        newbalanceDest = st.number_input(
        "New Balance of Receiver",
        value=None,
        format="%.2f",
        help="Enter new balance of destination account (e.g. 0.00)")


# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Transaction",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if step is None:
        missing_fields.append("Step")

    if type_status is None:
        missing_fields.append("Select Payment Type")

    if amount is None:
        missing_fields.append("Amount")

    if oldbalanceOrg is None:
        missing_fields.append("Old Balance of Sender")

    if newbalanceOrig is None:
        missing_fields.append("New Balance of Sender")

    if oldbalanceDest is None:
        missing_fields.append("Old Balance of Receiver")

    if newbalanceDest is None:
        missing_fields.append("New Balance of Receiver")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "step": step,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "type_status": type_status
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_fraud(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="is fraud transaction",
            value=f"{result['prediction']}")

    except Exception as e:
        st.error(str(e))
