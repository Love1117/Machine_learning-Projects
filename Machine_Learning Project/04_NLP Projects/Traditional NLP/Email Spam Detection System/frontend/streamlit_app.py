import streamlit as st
from api_client import predict_mail
from pathlib import Path


st.set_page_config(
    page_title="Email Spam Detection System",
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
    <h1>Email Spam Detection System</h1>
    <p>Predict if a mail is genuie or scam using deep learning model.</p>
</div>
""", unsafe_allow_html=True)


# Text
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Input Mail</div>',
        unsafe_allow_html=True
    )


    col1, = st.columns(1)

    with col1:
        text = st.text_area(
        "Input Text",
        placeholder="type in mail..."
)

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Mail",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if not text.strip():
        missing_fields.append("Input Text")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "text": text
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_mail(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Mail Status</h3>
        <p>{result['prediction']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
