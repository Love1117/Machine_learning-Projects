import streamlit as st
from api_client import (ask_question, get_main_questions)
from pathlib import Path


st.set_page_config(
    page_title="Question And Answering",
    layout="wide")


@st.cache_data
def load_questions():
    return get_main_questions()["Questions"]

Questions = load_questions()


def load_css():
    css_path = Path(__file__).parent / "styles.css"
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True)
        
load_css()



st.markdown("""
<div class="main-header">
    <h1>Question Answering</h1>
    <p>This model was fine-tuned on the biography of
        <em>Loveday Shadrack</em> and answers questions
        based on the provided information.</p>
</div>
""", unsafe_allow_html=True)


# Question
with st.form("prediction_form"):
    
    st.markdown(
        '<div class="section-title">Question</div>',
        unsafe_allow_html=True
    )
    
    selected_question = st.selectbox(
    "Question",
    Questions,
    index= None,
    placeholder="Select Question"
)


  
# -------------------------------
# Prediction Button
# -------------------------------
    
    submit = st.form_submit_button(
    "Answer Question",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if selected_question is None:
        missing_fields.append("Question")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "question": selected_question
    }


    try:
        with st.spinner("Generating prediction..."):
            result = question(payload)
            
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Prediction Result</h3>
        <p><strong>Question:</strong> {result['question']}</p>
        <p><strong>Answer:</strong> {result['answer']}</p>
        <p><strong>Score:</strong> {result['score']:.2%}</p>
    </div>
    """,
    unsafe_allow_html=True
)


    except Exception as e:
        st.error(str(e))
