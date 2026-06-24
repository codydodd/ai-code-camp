import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load a MobileNetV2 model pretrained on ImageNet
model = tf.keras.applications.MobileNetV2(weights="imagenet")

# ImageNet class index for "bird" categories
BIRD_CLASSES = [
    "n01514668", "n01514859", "n01518878", "n01530575", "n01531178",
    "n01532829", "n01534433", "n01537544", "n01558993", "n01560419",
    "n01580077", "n01582220", "n01592084", "n01601694", "n01608432",
    "n01614925", "n01616318"
]

def is_bird(img_path):
    # Load and preprocess image
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)

    # Run prediction
    preds = model.predict(x)
    decoded = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=3)[0]

    # Check if any top predictions are bird classes
    for class_id, label, score in decoded:
        if class_id in BIRD_CLASSES:
            return True, label, float(score)

    return False, decoded[0][1], float(decoded[0][2])


# Example usage
img_path = "computer_vision/cat.jpg"
bird, label, confidence = is_bird(img_path)

if bird:
    print(f"Bird detected: {label} ({confidence:.2f})")
else:
    print(f"No bird detected. Top guess: {label} ({confidence:.2f})")
