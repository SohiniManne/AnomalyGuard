import bentoml
from bentoml.io import NumpyNdarray
import numpy as np

model_ref = bentoml.tensorflow.load_model("lstm_user_engagement.h5")
svc = bentoml.Service("user_engagement_lstm", runners=[model_ref])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def predict(input_arr: np.ndarray) -> np.ndarray:
    return svc.runners[0].run(input_arr)
