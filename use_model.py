import requests

def use_model():
    # API URL - Update with the IP of the machine where the API is running
    url = "http://192.168.0.18:5000/predict"

    # Data to be predicted (replace with your values)
    data = {"values": [100, 200, 300]}

    try:
        # Sending the POST request to the API
        response = requests.post(url, json=data)

        # Checking if the response was successful
        if response.status_code == 200:
            predictions = response.json()["predictions"]
            print("Model predictions:", predictions)
        else:
            print("API error:", response.status_code, response.json())
    except Exception as e:
        print("Error connecting to the API:", e)

if __name__ == "__main__":
    use_model()

