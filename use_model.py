import requests

def usar_modelo():
    # URL da API - Atualize conforme o IP da máquina onde a API está rodando
    url = "http://192.168.0.18:5000/predict"

    # Dados que queremos prever (substitua pelos seus valores)
    dados = {"valores": [1.5, 2.5, 3.5]}

    try:
        # Enviando a requisição POST para a API
        response = requests.post(url, json=dados)

        # Verificando se a resposta foi bem-sucedida
        if response.status_code == 200:
            previsoes = response.json()["previsoes"]
            print("Previsões do modelo:", previsoes)
        else:
            print("Erro na API:", response.status_code, response.json())
    except Exception as e:
        print("Erro ao se conectar com a API:", e)

if __name__ == "__main__":
    usar_modelo()
