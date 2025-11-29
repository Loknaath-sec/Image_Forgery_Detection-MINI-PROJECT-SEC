import gradio as gr
import numpy as np
import tensorflow as tf
from PIL import Image

from preprocess_ela import convert_to_ela_image
from model_def import IMAGE_SIZE, build_forgery_model

# Load model (inference only)
model = tf.keras.models.load_model("forgery_cnn_best.h5", compile=False)

def classify_image(input_image):
    """
    input_image: numpy array (H, W, 3)
    """
    pil_img = Image.fromarray(input_image).convert("RGB")
    temp_path = "temp_input.jpg"
    pil_img.save(temp_path)

    ela_image = convert_to_ela_image(temp_path)
    ela_resized = ela_image.resize(IMAGE_SIZE)

    x = np.array(ela_resized).astype("float32")
    x = np.expand_dims(x, axis=0)

    prob = model.predict(x)[0][0]
    forged_prob = float(prob)
    authentic_prob = float(1 - prob)

    return {"Authentic": authentic_prob, "Forged": forged_prob}, ela_resized

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="numpy", label="Upload an image"),
    outputs=[
        gr.Label(num_top_classes=2, label="Prediction"),
        gr.Image(type="pil", label="ELA Representation")
    ],
    title="Image Forgery Detection (ELA + CNN)",
    description="""
    <b>Team Members:</b><br>
    1. Loknaath P (Reg No: 212223240080)<br>
    2. Lokhnath J (Reg No: 212223240079)<br>
    <br>
    Upload an image. The model converts it to its Error Level Analysis (ELA) version and predicts whether it is Authentic or Forged.
    """,
)

if __name__ == "__main__":
    demo.launch()
