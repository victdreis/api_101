# API de Machine Learning com Flask

Esta API utiliza Flask para servir um modelo de Machine Learning simples treinado com sklearn. O modelo prevê valores baseados em entradas fornecidas.

---

## **Estrutura do Projeto**

```
api_ml/
├── app.py               # Código principal da API Flask
├── train_model.py       # Código para treinar e salvar o modelo
├── use_model.py         # Script para usar o modelo via API
├── model/
│   └── modelo.pkl       # Arquivo do modelo treinado
├── requirements.txt     # Lista de dependências
└── README.md            # Este arquivo
```

---

## **1. Configuração do Ambiente**

### **1.1 Pré-requisitos**
- **Git** instalado: [Instruções de instalação](https://git-scm.com/).
- **Conda** instalado: [Baixar Conda](https://docs.conda.io/en/latest/miniconda.html).

### **1.2 Clonando o Repositório**
1. Clone o repositório:
   ```bash
   git clone <git@github.com:victdreis/api_101.git>
   cd api_101
   ```

2. Crie o ambiente Conda:
   ```bash
   conda create -n api_101 python=3.9 -y
   conda activate api_101
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## **2. Treinando o Modelo**

Se necessário, treine o modelo executando:
```bash
python train_model.py
```
Isso gerará o arquivo `modelo.pkl` dentro da pasta `model/`.

---

## **3. Executando a API**

Inicie o servidor Flask executando:
```bash
python app.py
```
A API estará acessível no endereço:
- Localmente: `http://127.0.0.1:5000`
- Na rede local: `http://192.168.0.18:5000` .

---

## **4. Usando o Modelo via API**

### **4.1 Testando com o Script**
Use o script `use_model.py` para enviar dados e obter previsões:
```bash
python use_model.py
```
Saída esperada:
```
Previsões do modelo: [[valor1], [valor2], [valor3]]
```

### **4.2 Testando com `curl`**
Envie uma requisição POST diretamente pelo terminal:
```bash
curl -X POST http://http://192.168.0.18:5000/predict \
-H "Content-Type: application/json" \
-d '{"valores": [0, 2, 3]}'
```

---



