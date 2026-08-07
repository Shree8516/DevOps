"""
Stage 5: Model Evaluation
-------------------------
Loads the trained model and test set, computes regression evaluation
metrics, and writes them to metrics.json.

Input:
    model.pkl
    data/features/test.csv

Output:
    metrics.json
"""

import json
import joblib
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def load_model(path: str = "model.pkl"):
    """Load the trained model."""
    model = joblib.load(path)
    print(f"[model_evaluation] Loaded model <- {path}")
    return model


def load_test_data(path: str = "data/features/test.csv") -> pd.DataFrame:
    """Load the test dataset."""
    df = pd.read_csv(path)
    print(f"[model_evaluation] Loaded test data (shape={df.shape})")
    return df


def evaluate(model, df: pd.DataFrame) -> dict:
    """Evaluate the regression model."""

    X_test = df.drop(columns=["price"])
    y_test = df["price"]

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)

    metrics = {
        "mae": mean_absolute_error(y_test, y_pred),
        "mse": mse,
        "rmse": mse ** 0.5,
        "r2_score": r2_score(y_test, y_pred),
    }

    return metrics


def save_metrics(metrics: dict, path: str = "metrics.json") -> None:
    """Save evaluation metrics."""
    with open(path, "w") as f:
        json.dump(metrics, f, indent=4)

    print(f"[model_evaluation] Saved metrics -> {path}")
    print(json.dumps(metrics, indent=4))


def main():
    model = load_model()
    df = load_test_data()

    metrics = evaluate(model, df)

    save_metrics(metrics)


if __name__ == "__main__":
    main()