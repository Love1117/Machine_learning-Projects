import streamlit as st
from api_client import predict_grad
from pathlib import Path


st.set_page_config(
    page_title="Customer Insurance Prediction",
    page_icon="🫰",
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
    <h1>Customer Insurance Prediction</h1>
    <p>Predict if a customer has insurance or not using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Personal Info
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title"Personal Info</div>',
        unsafe_allow_html=True
    )

    
    col1, col2 = st.columns(2)
        
    with col1:
        age = st.number_input(
        "age",
        value=None,
        placeholder="Enter age (e.g. 53)")

    
    with col2:
        sex = st.selectbox(
        "sex",
        ["Male","Female"],
        index=None,
        placeholder="Choose Option"
)


    
    st.markdown(
        '<div class="section-title">Health & Lifestyle Metrics</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
            
    with col1:
        bmi = st.number_input(
        "bmi",
        value=None,
        format="%.2f",
        placeholder="Enter Body Mass Inde. (e.g. 27.900)")
  
    with col2:
        smoker = st.selectbox(
        "smoker",
        ["Yes","No"],
        index=None,
        placeholder="Choose Option"
)

    
    # -------------------------------
    # Household/Geographic  & Financial Info
    # -------------------------------
    
    st.markdown(
    '<div class="section-title">Household/Geographic  & Financial Info</div>',
    unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        children = st.number_input(
        "children",
        value=None,
        placeholder="Enter number of children (e.g. 2)")
  
    with col2:
        region = st.number_input(
        "region",
        value=None,
        placeholder="Enter region (e.g. 1)")


    with col3:
        charges = st.number_input(
        "charges",
        value=None,
        format="%.2f",
        placeholder="Enter charges (e.g. 16884.92)")

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Insurace",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if age is None:
        missing_fields.append("age")

    if sex is None:
        missing_fields.append("sex")

    if bmi is None:
        missing_fields.append("bmi")

    if smoker is None:
        missing_fields.append("smoker")

    if children is None:
        missing_fields.append("children")

    if region is None:
        missing_fields.append("region")

    if charges is None:
        missing_fields.append("charges")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "smoker": smoker,
        "children": children,
        "region": region,
        "charges": charges
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_grad(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Prediction Result</h3>
        <p><strong>Insurance_Claim:</strong> {result['predicted_insurance_claim']}</p>
        <p><strong>Probability:</strong> {result['prediction_probability']:.2%}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
