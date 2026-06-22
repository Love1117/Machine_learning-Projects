import streamlit as st
from api_client import chat_bot
from pathlib import Path


st.set_page_config(
    page_title="AI Assistant(chat bot)",
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
    <h1>AI Assistant(chat bot)</h1>
    <p>Generates a chat/image/record response using the gemma-3-27b-it model.</p>
</div>
""", unsafe_allow_html=True)


# Text
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Ask a Question</div>',
        unsafe_allow_html=True
    )


    text = st.text_area(
        "Input Text",
        placeholder="Ask question...")

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Generate Answer",
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
        with st.spinner("Generating Answer..."):
            result = chat_bot(payload)
            
        st.success("Response Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <p><strong>Prompt:</strong> {text}</p>
        <p><strong>Answer:</strong> {result['response']}</p>
    </div>
    """,
    unsafe_allow_html=True)
      
    except Exception as e:
        st.error(str(e))
