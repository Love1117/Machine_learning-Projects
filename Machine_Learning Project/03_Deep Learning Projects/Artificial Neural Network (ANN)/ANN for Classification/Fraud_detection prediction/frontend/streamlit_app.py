import streamlit as st
from api_client import predict_fraud
from pathlib import Path


st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🧖",
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
    <h1>Fraud Detection System</h1>
    <p>Predict if a transaction is a fraud or not using Machine Learning</p>
</div>
""", unsafe_allow_html=True)


# Behavioral Patterns
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Behavioral Patterns</div>',
        unsafe_allow_html=True
    )

    
    col1, col2 = st.columns(2)
        
    with col1:
        click_duration = st.number_input(
        "click duration",
        value=None,
        format="%.2f",
        help="Enter how long a person stays on a webpage after clicking a link. calculated in minutes per sec(e.g. 0.29)")

    
    with col2:
        click_frequency = st.number_input(
        "click frequency",
        value=None,
        help="Enter how many times a single visitor clicks on the same link within a short period. (e.g. 7)")


    col3, col4 = st.columns(2)
        
    with col3:
        time_since_last_click = st.number_input(
        "time since last click",
        value=None,
        help="Enter how time gap between each click. meassured in milliseconds(Seconds)  (e.g. 72)")

    with col4:
        scroll_depth = st.number_input(
        "scroll depth",
        value=None,
        format="%.2f",
        help="Enter what percentage of the page did they actually see.  (e.g. 15)")


    col5, col6 = st.columns(2)
        
    with col5:
        mouse_movement = st.number_input(
        "mouse movement",
        value=None,
        help="Enter time movement of mouse. meassured in milliseconds(Seconds)  (e.g. 111)")
    
    with col6:
        keystrokes_detected = st.number_input(
        "keystrokes detected",
        value=None,
        help="Enter The time it takes to type from one key to another. calculated in milliseconds.  (e.g. 8)")

  
    st.markdown(
        '<div class="section-title">Network Security & Anonymization</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
            
    with col1:
        VPN_usage = st.selectbox(
        "VPN usage",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)
  
    with col2:
        proxy_usage = st.selectbox(
        "proxy usage",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option"
)

    
    with col3:
        device_ip_reputation_status = st.selectbox(
        "device ip reputation",
        ["Good", "Suspicious", "Bad"],
        index=None,
        placeholder="Choose Option"
)


    # -------------------------------
    # Environment & Device Fingerprinting
    # -------------------------------

    st.markdown(
    '<div class="section-title">Environment & Device Fingerprinting</div>',
    unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        device_type_status = st.selectbox(
        "device type",
        ["Desktop", "Mobile", "Tablet"],
        index=None,
        placeholder="Choose Option"
)
  
    with col2:
        browser_status = st.selectbox(
        "browser",
        ["Edge", "Firefox", "Opera", "Safari", "Chrome"],
        index=None,
        placeholder="Choose Option"
)

      
    with col3:
        operating_system_status = st.selectbox(
        "operating system",
        ["Linux", "iOS", "macOS", "Windows", "Android"],
        index=None,
        placeholder="Choose Option"
) 

    
    st.markdown(
    '<div class="section-title">Time & Schedule</div>',
    unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
        "year",
        value=None,
        help="Enter Year (e.g. 2024)")
  
    with col2:
        month = st.number_input(
        "month",
        value=None,
        help="Enter Month (e.g. 5)")


  
    col3, col4 = st.columns(2)

    with col3:
        day = st.number_input(
        "day",
        value=None,
        help="Enter day (e.g. 23)")
  
    with col4:
        days_of_the_week = st.selectbox(
        "days of the week",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        index=None,
        placeholder="Choose Option"
) 


    col5, col6 = st.columns(2)
  
    with col5:
        hour = st.number_input(
        "hour",
        value=None,
        help="Enter hour (e.g. 2)")
  
    with col6:
        weekend = st.selectbox(
        "weekend",
        ["Yes", "No"],
        index=None,
        placeholder="Choose Option")


    st.markdown(
        '<div class="section-title">Risk Intelligence Scoring/Risk Intelligence Scoring</div>',
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        ad_position_status = st.selectbox(
        "ad position",
        ["Side", "Bottom", "Top"],
        index=None,
        placeholder="Choose Option")
  
    with col2:
        bot_likelihood_score = st.number_input(
        "bot likelihood score",
        value=None,
        format="%.2f",
        help="Enter bot likelihood score per (e.g. 0.29)")


# -------------------------------
# Prediction Button
# -------------------------------
            
    submit = st.form_submit_button(
    "Predict Fraud Risk",
    use_container_width=True)

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if click_duration is None:
        missing_fields.append("click duration")

    if click_frequency is None:
        missing_fields.append("click frequency")

    if time_since_last_click is None:
        missing_fields.append("time since last click")

    if scroll_depth is None:
        missing_fields.append("scroll depth")

    if mouse_movement is None:
        missing_fields.append("mouse movement")

    if keystrokes_detected is None:
        missing_fields.append("keystrokes detected")

    if VPN_usage is None:
        missing_fields.append("VPN usage")

    if proxy_usage is None:
        missing_fields.append("proxy usage")

    if device_ip_reputation_status is None:
        missing_fields.append("device ip reputation")

    if device_type_status is None:
        missing_fields.append("device type")

    if browser_status is None:
        missing_fields.append("browser")

    if operating_system_status is None:
        missing_fields.append("operating system")

    if year is None:
        missing_fields.append("year")

    if month is None:
        missing_fields.append("month")

    if day is None:
        missing_fields.append("day")

    if days_of_the_week is None:
        missing_fields.append("days of the week")

    if hour is None:
        missing_fields.append("hour")

    if weekend is None:
        missing_fields.append("weekend")

    if ad_position_status is None:
        missing_fields.append("ad position")

    if bot_likelihood_score is None:
        missing_fields.append("bot likelihood score")
  
    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    payload = {
        "click_duration": click_duration,
        "scroll_depth": scroll_depth,
        "mouse_movement": mouse_movement,
        "keystrokes_detected": keystrokes_detected,
        "click_frequency": click_frequency,
        "time_since_last_click": time_since_last_click,
        "VPN_usage": VPN_usage,
        "proxy_usage": proxy_usage,
        "bot_likelihood_score": bot_likelihood_score,
        "year": year,
        "month": month,
        "day": day,
        "days_of_the_week": days_of_the_week,
        "hour": hour,
        "weekend": weekend,
        "device_type_status": device_type_status,
        "device_ip_reputation_status": device_ip_reputation_status,
        "browser_status": browser_status,
        "operating_system_status": operating_system_status,
        "ad_position_status": ad_position_status
    }


    try:
        with st.spinner("Generating prediction..."):
            result = predict_fraud(payload)
            
        st.success("Prediction Generated Successfully")
        
        st.markdown(
    f"""
    <div class="prediction-card">
        <h3>Prediction Result</h3>
        <p><strong>Is_fraudulent:</strong> {result['prediction_class']}</p>
        <p><strong>Probability:</strong> {result['probability']:.2%}</p>
    </div>
    """,
    unsafe_allow_html=True
)

    except Exception as e:
        st.error(str(e))
