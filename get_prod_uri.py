import mlflow
import os
import yaml

def pull_model_uri(model_name):
    # Create an MLflow client
    client = mlflow.tracking.MlflowClient()

    # Get the latest version of the model in the 'Production' stage
    latest_version = client.get_latest_versions(model_name, stages=['Production'])

    if not latest_version:
        raise Exception("No model found in production.")

    # Get the model URI
    model_uri = f"models:/{model_name}/Production"

    return model_uri

if __name__ == "__main__":
    # Load the config file
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Set the tracking URI
    mlflow.set_tracking_uri(config["tracking_uri"])
    print("Tracking URI:", config["tracking_uri"])

    # Get the model URI
    try:
        model_uri = pull_model_uri(config["model_name"])
        print("Model URI:", model_uri)
    except Exception as e:
        print("Error:", str(e))