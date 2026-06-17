import streamlit as st
from api_client import hand_digit
from pathlib import Path


st.set_page_config(
    page_title="Hand Written Digit Classification",
    page_icon="📒",
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
    <h1>Hand Written Digit Classification</h1>
    <p>Predict hand written digits using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# File
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Upload file,</div>',
        unsafe_allow_html=True
    )

    col1, = st.columns(1)
        
    with col1:
        file = st.file_uploader(
        "Upload Digit Image",
        type=["png", "jpg", "jpeg"])

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Digit Image",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    if file is None:
        st.warning("⚠️ Please upload an image file.")
        st.stop()

    try:

        with st.spinner("Generating prediction..."):
            result = hand_digit(file)

        st.success("Prediction Generated Successfully")

        st.markdown('<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Predicted Digit",
            value=result["predicted_digit"]
        )

    except Exception as e:
        st.error(str(e))
