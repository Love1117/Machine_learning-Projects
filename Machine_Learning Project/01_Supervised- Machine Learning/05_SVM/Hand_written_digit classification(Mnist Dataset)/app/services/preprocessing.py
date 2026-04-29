from PIL import Image
import numpy as np

preprocess_image(image: Image.Image) -> np.ndarray:
  image = image.convert("L")
  # Resize to 8x8

  image = image.resize((8, 8))
  # Convert to numpy

  image_array = np.array(image)
  # Normalize to 0–16 (sklearn digits scale)

  image_array = image_array / 255.0 * 16
  # Flatten

  return image_array.reshape(1, -1)
