import streamlit as st
from api_client import iris_flower

st.set_page_config(
    page_title="Iris Flower-type Classification",
    page_icon="🏠",
    layout="wide")


def load_css():
    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
        
load_css()


st.markdown("""
<div class="main-header">
    <h1>Iris_flower-type_classification_System</h1>
    <p>Predict iris flower-type using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Flower Measurements
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Flower Measurements</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        sepal_length = st.number_input(
        "sepal length",
        value=None,
        format="%.2f",
        placeholder="Enter sepal length CM (e.g. 4.7)")

    with col2:
        sepal_width = st.number_input(
        "sepal width",
        value=None,
        format="%.2f",
        placeholder="Enter sepal width CM (e.g. 3.2)")


    
    co3, col4 = st.columns(2)
    with col3:
        petal_length = st.number_input(
        "petal length",
        value=None,
        format="%.2f",
        placeholder="Enter sepal width CM (e.g. 1.3)")
  
    with col4:
        petal_width = st.number_input(
        "petal width",
        value=None,
        format="%.2f",
        placeholder="Enter sepal width CM (e.g. 0.2)")



# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Iris Flower",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if sepal_length is None:
        missing_fields.append("sepal length")

    if sepal_width is None:
        missing_fields.append("sepal width")

    if petal_length is None:
        missing_fields.append("petal length")

    if petal_width is None:
        missing_fields.append("petal width")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }


    try:
        with st.spinner("Generating prediction..."):
            result = iris_flower(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
        '<div class="prediction-card">Prediction Result</div>',
        unsafe_allow_html=True)

        st.metric(
            label="Predicted Flower type",
            value=f"{result['prediction']}")

    except Exception as e:
        st.error(str(e))
