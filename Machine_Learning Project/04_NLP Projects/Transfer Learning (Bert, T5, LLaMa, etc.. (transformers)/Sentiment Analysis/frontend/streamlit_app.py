import streamlit as st
from api_client import sentiment
from pathlib import Path


st.set_page_config(
    page_title="Sentiment Analysis",
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
    <h1>Sentiment Analysis</h1>
    <p>Analyzes the sentiment of the provided text using the Roberta model.</p>
</div>
""", unsafe_allow_html=True)


# Text
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Input Text</div>',
        unsafe_allow_html=True
    )


    text = st.text_area(
        "Input Text",
        placeholder="Type in your review...")

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Analyze Text",
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
            result = sentiment(payload)
            
        st.success("Sentiment Analysis Completed")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <p><strong>Text:</strong> {result['text']}</p>
        <p><strong>Sentiment Scores:</strong> {result['sentiment_scores']}</p>
        <p><strong>Model:</strong> {result['model']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
