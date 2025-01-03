import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Generating synthetic data
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Values between 0 and 10
y = 2.5 * X + np.random.randn(100, 1) * 2  # Linear relationship with noise

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Saving the trained model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved in 'model/model.pkl'")
