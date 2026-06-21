import streamlit as st
from api_client import predict_customers
from pathlib import Path


st.set_page_config(
    page_title="Customers Mall Segmentation",
    page_icon="🏬",
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
    <h1>Customers Mall Segmentation</h1>
    <p>Segment customers into spending groups using Machine Learning.</p>
</div>
""", unsafe_allow_html=True)


# Info
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Info</div>',
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
        Annual_Income_k = st.number_input(
        "Annual Income",
        value=None,
        help="Enter your annual income in thousands (e.g., enter 50 for $50,000).")

  
    with col4:
        Spending_Score_1_100 = st.number_input(
        "Spending Score",
        value=None,
        help="Enter Spending Score from 1-100 (e.g. 5 )")




# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Customer",
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

    if Annual_Income_k is None:
        missing_fields.append("Annual Income")

    if Spending_Score_1_100 is None:
        missing_fields.append("Spending Score")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "Gender": Gender,
        "Age": Age,
        "Annual_Income_k": Annual_Income_k,
        "Spending_Score_1_100": Spending_Score_1_100
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_customers(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Customer Segment",
            value=f"{result['prediction']}")

    except Exception as e:
        st.error(str(e))
