import tensorflow as tf
from tensorflow.keras import layers, models

IMAGE_SIZE = (128, 128)

def build_forgery_model():
    """
    Build a binary classifier (authentic vs forged) using EfficientNetB0.
    """
    base_model = tf.keras.applications.EfficientNetB0(
        include_top=False,
        weights="imagenet",
        input_shape=(*IMAGE_SIZE, 3),
        pooling="avg"
    )

    base_model.trainable = False  # freeze base for initial training

    inputs = layers.Input(shape=(*IMAGE_SIZE, 3))
    x = tf.keras.applications.efficientnet.preprocess_input(inputs)
    x = base_model(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(1, activation="sigmoid")(x)

    model = models.Model(inputs, outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model
