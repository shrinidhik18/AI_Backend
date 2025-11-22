import tensorflow as tf
import numpy as np

class ModelLoader:
    def __init__(self):
        print("Loading TensorFlow MobileNetV2 model...")
        self.model = tf.keras.applications.MobileNetV2(weights="imagenet")
        self.input_size = (224, 224)

    def preprocess(self, image):
        image = image.resize(self.input_size)
        array = np.array(image)
        array = tf.keras.applications.mobilenet_v2.preprocess_input(array)
        return np.expand_dims(array, axis=0)

    def predict(self, image):
        tensor = self.preprocess(image)
        preds = self.model.predict(tensor)
        decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=5)[0]
        return decoded
