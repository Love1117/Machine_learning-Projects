import streamlit as st
from api_client import summarize_text
from pathlib import Path


st.set_page_config(
    page_title="Text Summarization using spaCy+TextRank",
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
    <h1>Text Summarization using spaCy+TextRank for Natural language processing</h1>
    <p>extractive text summarization using spaCy and PyTextRank for ranking key phrases and sentences..</p>
</div>
""", unsafe_allow_html=True)


# Personal Info
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Input Text</div>',
        unsafe_allow_html=True
    )


    col1, = st.columns(1)

    with col1:
        text = st.text_area(
        "Input Text",
        placeholder="Write a sentence..."
)


    col2, = st.columns(1)

    with col2:
        limit_phrases = st.number_input(
        "Limit Phrases",
        min_value=1,
        value=1,
        help="Max key terms to extract. Eg 10"        
)
    
    col3, = st.columns(1)

    with col3:
        limit_sentences = st.number_input(
        "Limit Sentences",
        min_value=1,
        value=1,
        help="Max sentences in summary. Eg 5"        
)

  
# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Summarize Text",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if not text.strip():
        missing_fields.append("Input Text")

    if limit_phrases is None:
        missing_fields.append("Limit Phrases")

    if limit_sentences is None:
        missing_fields.append("Limit Sentences")
      
    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "text": text,
        "limit_phrases": limit_phrases,
        "limit_sentences": limit_sentences
    }


    try:
        with st.spinner("Generating prediction..."):
            result = summarize_text(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Summary</h3>
        <p>{result['summary']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
