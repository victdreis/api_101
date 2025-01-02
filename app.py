from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Carregar o modelo treinado
with open("model/modelo.pkl", "rb") as f:
    modelo = pickle.load(f)

@app.route("/")
def home():
    return "API de Machine Learning funcionando!"

# Rota para prever resultados
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Receber dados em formato JSON
        dados = request.get_json()
        valores = np.array(dados["valores"]).reshape(-1, 1)
        
        # Fazer previsão
        previsao = modelo.predict(valores).tolist()
        
        return jsonify({"previsoes": previsao})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

if __name__ == "__main__":
    # Torna a API acessível para outros computadores na mesma rede
    app.run(host="0.0.0.0", port=5000, debug=True)
