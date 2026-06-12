import tensorflow as tf
from app.core.config import MODEL_DIR
import tensorflow_hub as hub
import joblib


# Define image dimensions
img_height = 224
img_width = 224


feature_extractor_model_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/4"
feature_extractor_module = hub.load(feature_extractor_model_url)


feature_extractor_layer = tf.keras.layers.Lambda(
    lambda x: feature_extractor_module(x, training=False),
    name='feature_extractor_lambda_layer')

class_names = joblib.load(MODEL_DIR / "class_names.keras")
num_classes = len(class_names)

inputs = tf.keras.Input(shape=(img_height, img_width, 3))
x = feature_extractor_layer(inputs)
# Assuming a dense classification head was added after the feature extractor
outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)


loaded_model = tf.keras.Model(inputs, outputs)
loaded_model.load_weights(MODEL_DIR / "Flower_photo-feature-extractor-model.keras")
