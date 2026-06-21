import streamlit as st
from api_client import predict_next_word
from pathlib import Path


st.set_page_config(
    page_title="Next Word Prediction",
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
    <h1>Next Word Prediction</h1>
    <p>Generate the next words in a sentence using a LSTM deep learning model.</p>
    <p>This model was trained on the novel <em>War and Peace</em> from Project Gutenberg and may perform best on text with a similar writing style.</p>
</div>
""", unsafe_allow_html=True)


# Personal Info
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">type a word and input the length of next words to predict</div>',
        unsafe_allow_html=True
    )


    col1, col2 = st.columns(2)

    with col1:
        input_word = st.text_area(
        "Input Text",
        placeholder="Write a sentence..."
)

    with col2:
        len_of_words = st.number_input(
        "Number of Words to Predict",
        min_value=1,
        value=None,
        help="Example: 5"        
)
  

  
# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Next Word",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if not input_word.strip():
        missing_fields.append("Input Text")

    if len_of_words is None:
        missing_fields.append("Number of Words to Predict")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "input_word": input_word,
        "len_of_words": len_of_words
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_next_word(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Prediction Result</h3>
        <p>{result['generated_text']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
