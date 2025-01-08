# Machine Learning API with FastAPI

This API uses **FastAPI** to serve a simple Machine Learning model trained with sklearn. The model predicts values based on provided inputs.

---

## **Project Structure**

```
api_ml/
├── app.py               # Main FastAPI code
├── train_model.py       # Code to train and save the model
├── use_model.py         # Script to use the model via the API
├── model/
│   └── model.pkl        # Trained model file
├── pyproject.toml       # Poetry configuration file
├── poetry.lock          # Poetry lock file
└── README.md            # This file
```

---

## **1. Environment Setup**

### **1.1 Prerequisites**

- **Git** installed: [Installation instructions](https://git-scm.com/).
- **Conda** installed: [Download Conda](https://docs.conda.io/en/latest/miniconda.html).
- **Poetry** installed: [Poetry installation](https://python-poetry.org/docs/#installation).

### **1.2 Cloning the Repository**

1. Clone the repository:

   ```bash
   git clone <git@github.com:victdreis/api_101.git>
   cd api_101
   ```

2. Create the Conda environment:

   ```bash
   conda create -n api_101 python=3.9 -y
   conda activate api_101
   ```

3. Install dependencies with Poetry:

   ```bash
   poetry install
   ```

---

## **2. Training the Model**

If needed, train the model by running:

```bash
python train_model.py
```

This will generate the `model.pkl` file inside the `model/` directory.

---

## **3. Running the API**

Start the FastAPI server using Uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 5000 --reload
```

The API will be accessible at:

- Locally: `http://127.0.0.1:5000`
- On the local network: `http://192.168.0.18:5000`.

---

## **4. Using the Model via API**

### **4.1 Testing with the Script**

Use the `use_model.py` script to send data and get predictions:

```bash
python use_model.py
```

Expected output:

```
Model predictions: [[value1], [value2], [value3]]
```

### **4.2 Testing with `curl`**

Send a POST request directly from the terminal:

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"values": [0, 2, 3]}'
```

---

