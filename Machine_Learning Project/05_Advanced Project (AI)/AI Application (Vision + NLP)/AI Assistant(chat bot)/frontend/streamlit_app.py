import streamlit as st
from api_client import chat_bot
from pathlib import Path
from streamlit_mic_recorder import mic_recorder


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

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
<div class="main-header">
    <h1>AI Assistant(chat bot)</h1>
    <p>Generates a chat/image/record response using the gemma-3-27b-it model.</p>
</div>
""", unsafe_allow_html=True)


# Display old chats
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# Text
with st.form("prediction_form"):

    st.markdown(
        '<div class="section-title">Ask a Question</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3, col4 = st.columns([1,8,1,1])

    with col1:
        with st.popover("➕"):
            uploaded_file = st.file_uploader(
                "Upload Image",
                type=["png","jpg","jpeg"])

            camera_image = st.camera_input(
                "Take Picture")

    with col2:
        prompt = st.text_area(
            "Ask Anything",
            label_visibility="collapsed",
            placeholder="Ask anything...",
            height=70)

    with col3:
        audio = mic_recorder(
            start_prompt="🎤",
            stop_prompt="⏹")

    with col4:
        submit = st.form_submit_button("➤")


    
if audio:
    st.audio(audio["bytes"])
    

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if not prompt.strip() and not audio:
        missing_fields.append("Ask Question or Voice Recording")

    if missing_fields:
        st.warning(
            f"⚠️ Please complete the following fields: {', '.join(missing_fields)}"
        )
        st.stop()


    try:
        with st.spinner("Generating Answer..."):
            image = uploaded_file if uploaded_file else camera_image

            result = chat_bot(
                question=prompt,
                image=image,
                audio=audio)

        
        st.success("Response Generated Successfully")
        
        # Save user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt if prompt else "🎤 Voice Message"})

        # Save assistant response
        st.session_state.messages.append({
        "role": "assistant",
        "content": result["response"]})

        st.rerun()
      
    except Exception as e:
        st.error(str(e))
