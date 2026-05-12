import base64
from PIL import Image
import io



def encode_image(img_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(img_bytes))
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")
