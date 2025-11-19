import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score

n_samples = 500
n_timesteps = 5
n_features = 3

X = np.random.rand(n_samples, n_timesteps, n_features)
anomaly_threshold = X[:,:,0].mean()  # Calculate mean for smart threshold
y = (X[:,:,0].mean(axis=1) > anomaly_threshold).astype(np.float32)
print("Class balance:", np.bincount(y.astype(int)))

split = int(0.8 * n_samples)
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = Sequential()
model.add(LSTM(32, activation='relu', input_shape=(n_timesteps, n_features)))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X_train, y_train, epochs=15, verbose=2)

y_pred_prob = model.predict(X_test).flatten()
y_pred = (y_pred_prob > 0.5).astype(np.float32)

print("\n=== Improved Model Evaluation ===")
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_pred_prob))
print("Class balance (test):", np.bincount(y_test.astype(int)))
print("Sample predictions:", y_pred[:10])
