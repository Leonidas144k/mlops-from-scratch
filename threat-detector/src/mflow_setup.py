# Imports
import mlflow

# Define helper function
def init_mlflow(experiment_name = "Threat Detector", tracking_uri = "http://localhost:5000"):
    mlflow.set_experiment(experiment_name)
    mlflow.set_tracking_uri(tracking_uri)

    print("MLflow Initialized")
    print(f"Experiment Name : {experiment_name}")
    print(f"Tracking URI : {tracking_uri}")