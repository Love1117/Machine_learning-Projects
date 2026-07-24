import streamlit as st
from api_client import chat_bot
from pathlib import Path
from streamlit_mic_recorder import mic_recorder



st.set_page_config(
    page_title="AI Assistant(🗨️ chat-bot)",
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


if "upload_version" not in st.session_state:
    st.session_state.upload_version = 0

if "camera_version" not in st.session_state:
    st.session_state.camera_version = 0

if "mic_version" not in st.session_state:
    st.session_state.mic_version = 0

if "prompt_version" not in st.session_state:
    st.session_state.prompt_version = 0

if "image_source" not in st.session_state:
    st.session_state.image_source = None

if "recorded_audio" not in st.session_state:
    st.session_state.recorded_audio = None



audio = st.session_state.recorded_audio




uploaded_file = None
camera_image = None

st.markdown("""
<div class="main-header">
    <h1>AI Assistant(🗨️chat bot)</h1>
    <p>Generates a chat/image/record response using meta-llama 3.3 model.</p>
</div>
""", unsafe_allow_html=True)


# Display old chats
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# Text

st.markdown(
        '<div class="section-title">Ask a Question</div>',
        unsafe_allow_html=True)


col1, col2, col3, col4 = st.columns([1,8,1,1])

with col1:
    with st.popover("➕"):
        if st.session_state.image_source is None:
            if st.button("📁 Upload"):
                st.session_state.image_source = "upload"

            if st.button("📷 Camera"):
                st.session_state.image_source = "camera"


        elif st.session_state.image_source == "upload":
            uploaded_file = st.file_uploader(
                "Upload Image, files",
                type=["png","jpg","jpeg"],
                key=f"upload_{st.session_state.upload_version}")

            if st.button("⬅ Back"):
                st.session_state.image_source = None
                st.rerun()
                
        elif st.session_state.image_source == "camera":
            camera_image = st.camera_input(
                "Take Picture",
                key=f"camera_{st.session_state.camera_version}")

            if st.button("⬅ Back"):
                st.session_state.image_source = None
                st.rerun()

with col2:
    prompt = st.text_area(
        "Ask Anything",
        label_visibility="collapsed",
        placeholder="Ask anything...",
        height=70,
        key=f"prompt_{st.session_state.prompt_version}")

with col3:
    new_audio = mic_recorder(
        start_prompt="🎙️",
        stop_prompt="⏹",
        key=f"mic_{st.session_state.mic_version}")
            
    if new_audio:
        st.session_state.recorded_audio = new_audio

    audio = st.session_state.recorded_audio


    
with col4:
    submit = st.button("➤", use_container_width=True)


    
if audio:
    col_audio, col_delete = st.columns([8,1])

    with col_audio:
        st.audio(audio["bytes"])

    with col_delete:
        if st.button("🗑", help="Delete recording"):
            st.session_state.recorded_audio = None
            st.session_state.mic_version += 1
            st.rerun()    
    

    
if submit:

    # -----------------------------------
    # Validate Required Fields
    # -----------------------------------
    missing_fields = []

    if (not prompt.strip()
        and audio is None
        and uploaded_file is None
        and camera_image is None):
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
            "content": prompt if prompt else "🎙️ Voice Message"})

        # Save assistant response
        st.session_state.messages.append({
        "role": "assistant",
        "content": result["response"]})

        st.session_state.upload_version += 1
        st.session_state.camera_version += 1
        st.session_state.mic_version += 1
        st.session_state.prompt_version += 1
        st.session_state.image_source = None
        st.session_state.recorded_audio = None

        st.rerun()
      
    except Exception as e:
        st.error(str(e))
