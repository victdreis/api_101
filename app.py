from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Carregar modelos treinados
rank_model = joblib.load('model/rank_model.pkl')
win_model = joblib.load('model/win_model.pkl')

# Criar aplicação FastAPI
app = FastAPI(title="Horse Racing Prediction API", description="Predição de ranking e probabilidade de vitória.", version="1.0")

# Definir esquema de entrada para validação
class PredictionInput(BaseModel):
    Country: str
    Jockey: str
    Track: str
    Surface: str

# Rota para predizer ranking e probabilidade de vitória
@app.post("/predict", summary="Faz predição de ranking e probabilidade de vitória")
def predict(input_data: PredictionInput):
    # Converter input para DataFrame
    input_df = pd.DataFrame([input_data.dict()])

    # Transformar dados para os modelos
    input_df = pd.get_dummies(input_df, drop_first=True)

    # Garantir que colunas ausentes sejam preenchidas (durante o uso de novos dados)
    for col in rank_model.feature_names_in_:
        if col not in input_df:
            input_df[col] = 0

    # Predições
    rank_pred = rank_model.predict(input_df)
    win_prob = win_model.predict_proba(input_df)[:, 1]

    # Resposta JSON
    return {
        "ranking_prediction": float(rank_pred[0]),
        "win_probability": float(win_prob[0])
    }

# Rota inicial (saudação)
@app.get("/", summary="Endpoint inicial")
def home():
    return {"message": "Bem-vindo à API de predição de corridas de cavalos!"}
