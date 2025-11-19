import bentoml
import tensorflow as tf

model = tf.keras.models.load_model("lstm_user_engagement_v2.h5")
bentoml.keras.save_model("lstm_user_engagement_v2", model)
