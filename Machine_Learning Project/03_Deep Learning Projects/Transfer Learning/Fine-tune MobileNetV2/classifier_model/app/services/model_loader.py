import tensorflow as tf
from app.core.config import MODEL_DIR
import tensorflow_hub as hub


IMAGE_SHAPE = (224, 224)

# Define the exact TF Hub URL for the classifier model
classifier_model_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"

# 1. Load the TensorFlow Hub module (tf.Module) directly using hub.load()
loaded_tfhub_module = hub.load(classifier_model_url)

classifier_lambda_layer = tf.keras.layers.Lambda(
    lambda inputs: loaded_tfhub_module(inputs),
    name='tfhub_mobilenet_v2_classifier_lambda_layer')


classifier_loaded = tf.keras.Sequential([
    tf.keras.Input(shape=IMAGE_SHAPE + (3,)),
    classifier_lambda_layer])

# 4. Loading ONLY the weights from the saved .keras file into the newly constructed model.
try:
    classifier_loaded.load_weights(MODEL_DIR / "my_image_classifier.keras")

except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load weights from {model_save_path}. Please ensure the model architecture matches the TF Hub model. Error: {e}")
