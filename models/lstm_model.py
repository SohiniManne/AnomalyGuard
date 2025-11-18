import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from feast import FeatureStore

store = FeatureStore(repo_path="../feature_store")
entity_df = pd.DataFrame({"user_id": [1, 2, 3]})

features = store.get_online_features(
    features=["user_engagement:feature1", "user_engagement:feature2"],
    entity_rows=entity_df.to_dict(orient="records")
).to_df()

X = features[["feature1", "feature2"]].values
y = np.array([0, 1, 0])  # Dummy labels
X = X.reshape((X.shape[0], 1, X.shape[1]))

model = Sequential()
model.add(LSTM(10, activation='relu', input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X, y, epochs=10, verbose=2)
model.save("lstm_user_engagement.h5")
print("LSTM Model trained and saved!")
