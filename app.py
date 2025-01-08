from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import pickle
import numpy as np
from typing import List

# Define the FastAPI app
app = FastAPI()

# Load the trained model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Example data storage for management
stored_data = {}

# Define a Pydantic model for input validation
class PredictRequest(BaseModel):
    values: List[float]

@app.get("/")
def home():
    return RedirectResponse(url="/docs")

# Route for predicting results (POST)
@app.post("/predict")
def predict(request: PredictRequest):
    try:
        # Convert input data to numpy array and reshape
        values = np.array(request.values).reshape(-1, 1)
        
        # Make predictions
        predictions = model.predict(values).tolist()
        
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route for listing data (GET)
@app.get("/data")
def list_data():
    try:
        return {"stored_data": stored_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
