import streamlit as st
from api_client import similar_word, word_similar
from pathlib import Path


st.set_page_config(
    page_title="Building Words with Similar meaning",
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
    <h1>Building Words with Similar meaning</h1>
    <p>Predicting words most similar to the given word and also calculating the similarity between two given words.</p>
</div>
""", unsafe_allow_html=True)


# Text
with st.form("Similar_word_prediction_form"):

    st.markdown(
        '<div class="section-title">Predict Words Most Similar To The Given Word</div>',
        unsafe_allow_html=True
    )


    col1, = st.columns(1)

    with col1:
        word = st.text_area(
        "Input word",
        placeholder="Type word"
)

  
    col2, = st.columns(1)
  
    with col2:
        topn = st.number_input(
        "No of similar words needed",
        min_value=1,
        value=None,
        help="Example: 5"        
)

# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Find Similar Words",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if not word.strip():
        missing_fields.append("Input word")

    if topn is None:
        missing_fields.append("No of similar words needed")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "word": word,
        "topn": topn
    }


    try:
        with st.spinner("Generating prediction..."):
            result = similar_word(payload)
            
        st.success("Similar Words Extracted Completed")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <p><strong>Word:</strong> {word}</p>
        <p><strong>No Of Similar Words:</strong> {topn}</p>
        <p><strong>similar Words:</strong> {result['similar_words']}</p>
        
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))










with st.form("similarity_prediction_form"):

    st.markdown(
        '<div class="section-title">calculate the similarity between two given words</div>',
        unsafe_allow_html=True
    )


    col1, = st.columns(1)

    with col1:
        word1 = st.text_area(
        "Word 1",
        placeholder="Type word"
)

  
    col2, = st.columns(1)
  
    with col2:
        word2 = st.text_area(
        "Word 2",
        placeholder="Type word"
)

# -------------------------------
# Prediction Button
# -------------------------------
            
    similarity_submit = st.form_submit_button(
    "Word Similarity Score",
    use_container_width=True)

    
if similarity_submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if not word1.strip():
        missing_fields.append("word 1")

    if not word2.strip():
        missing_fields.append("word 2")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload2 = {
        "word1": word1,
        "word2": word2
    }


    try:
        with st.spinner("Generating prediction..."):
            result = word_similar(payload2)
            
        st.success("Similarity Score Completed")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <p><strong>word1:</strong> {word1}</p>
        <p><strong>word2:</strong> {word2}</p>
        <p><strong>Similarity Score:</strong> {result['similarity']:.2%}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
