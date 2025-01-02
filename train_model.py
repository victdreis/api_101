import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Gerando dados fictícios
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Valores entre 0 e 10
y = 2.5 * X + np.random.randn(100, 1) * 2  # Relação linear com ruído

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Salvando o modelo treinado
with open("model/modelo.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo treinado e salvo em 'model/modelo.pkl'")