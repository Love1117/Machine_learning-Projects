import base64
from PIL import Image
from faster_whisper import WhisperModel
import tempfile
import os
import io


model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe_audio(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(audio_bytes)
        temp_path = temp_file.name
    segments, info = model.transcribe(temp_path)
    text = " ".join(
        segment.text
        for segment in segments)
    os.remove(temp_path)
    return text



def encode_image(img_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(img_bytes))
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")
