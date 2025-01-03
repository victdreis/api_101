from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Example data storage for management
stored_data = {}

@app.route("/")
def home():
    return "Machine Learning API with multiple functionalities is running!"

# Route for predicting results (POST)
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Receive data in JSON format
        data = request.get_json()
        values = np.array(data["values"]).reshape(-1, 1)
        
        # Make predictions
        predictions = model.predict(values).tolist()
        
        return jsonify({"predictions": predictions})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route for listing data (GET)
@app.route("/data", methods=["GET"])
def list_data():
    try:
        return jsonify({"stored_data": stored_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Make the API accessible to other computers on the same network
    app.run(host="0.0.0.0", port=5000, debug=True)


