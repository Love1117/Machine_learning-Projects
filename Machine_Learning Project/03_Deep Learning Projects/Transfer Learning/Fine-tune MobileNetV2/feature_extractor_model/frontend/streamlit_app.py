import streamlit as st
from api_client import predict_flower
from pathlib import Path


st.set_page_config(
    page_title="Flowers photos classification",
    page_icon="💮",
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
    <h1>Flowers photos classification</h1>
    <p>Predict 5 types of Flower Photo  using Light wieght model,  mobilenet_v2 feature_vector/4</p>
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
        "Upload CIFAR-10 images",
        type=["png", "jpg", "jpeg"])

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Flower Image",
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
            result = predict_flower(file)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Prediction Result</h3>
        <p><strong>Prediction:</strong> {result['predicted_class']}</p>
        <p><strong>confidence:</strong> {result['confidence']:.2%}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
