from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import tensorflow as tf

# Load the trained model (make sure the .h5 path is correct!)
model = tf.keras.models.load_model("lstm_user_engagement_v2.h5")

app = FastAPI()

# Define input schema
class DataModel(BaseModel):
    data: list  # Expect a nested list: [[[feature1, feature2, ...]], ...]

@app.post("/predict")
def predict(input_data: DataModel):
    x = np.array(input_data.data, dtype=np.float32)  # Shape: (samples, timesteps, features)
    preds = model.predict(x)
    return {"predictions": preds.tolist()}
