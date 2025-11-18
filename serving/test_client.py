import requests
import numpy as np

input_data = np.array([[0.3, 0.8]]).reshape((1, 1, 2)).tolist()
response = requests.post("http://localhost:3000/predict", json={"inputs": input_data})
print("Prediction:", response.json())
