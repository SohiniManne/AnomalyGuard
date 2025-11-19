import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Generate enough synthetic data
n_samples = 100
n_timesteps = 1
n_features = 2

# Randomly generate float features between 0 and 1
X = np.random.rand(n_samples, n_timesteps, n_features)

# Random binary labels (0=normal, 1=anomaly)
y = np.random.randint(0, 2, size=n_samples).astype(np.float32)

print("Shapes:", X.shape, y.shape)
print("Any NaN in X?", np.isnan(X).any())
print("Any NaN in y?", np.isnan(y).any())
print("Any Inf in X?", np.isinf(X).any())

# Build, compile, and train simple LSTM model
model = Sequential()
model.add(LSTM(10, activation='relu', input_shape=(n_timesteps, n_features)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy')
history = model.fit(X, y, epochs=10, verbose=2)

print("Loss values per epoch:", history.history['loss'])
model.save("lstm_user_engagement.h5")
print("LSTM Model trained and saved!")
