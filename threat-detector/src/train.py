# Imports
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import mlflow
import mlflow.sklearn
from mflow_setup import init_mlflow

# Initialize MLflow
init_mlflow()

mlflow.set_experiment("Threat Detector")

# Load training set ( train.csv )
train_df = pd.read_csv("data/processed/train.csv")
X_train = train_df["command"]
print(f"Raw commands before : {X_train}")
y_train = train_df["label"]

# Vectorize commands with CountVectorizer
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
print(f"Vetorized Data : {X_train_vec}")

# Assign model to variable
model = LogisticRegression()

# Start up MLflow
with mlflow.start_run():
    model.fit(X_train_vec, y_train)
    predictions = model.predict(X_train_vec)
    accuracy = accuracy_score(y_train, predictions)

    # Log Metrics with MLflow
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")
    mlflow.sklearn.log_model(vectorizer, "vectorizer")

    print(f"Model accuracy : {accuracy:.2f}")
    print("Model and Vectorizer logged to MLflow")








    






