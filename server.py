# server.py
from flask import Flask, request, render_template
import mlflow.pyfunc
import yaml
import os

app = Flask(__name__)

# Load model URI from config.yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
model_name = config['model_name']
model_version = 3
mlflow.set_tracking_uri(config["tracking_uri"])

model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        data = [{'role': 'user', 'content': request.form['content']}]
        prediction = model.predict(data)
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)