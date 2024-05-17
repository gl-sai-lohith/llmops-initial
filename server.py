# server.py
from flask import Flask, request
import mlflow.pyfunc
import yaml

app = Flask(__name__)

# Load model URI from config.yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
model_uri = config['model_uri']

model = mlflow.pyfunc.load_model(model_uri)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(data)
    return {'prediction': prediction.tolist()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)