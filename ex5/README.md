# Experiment 5 - CI/CD Pipeline for Boston Housing Regression using GitHub Actions

## Overview

This experiment demonstrates an end-to-end **MLOps CI/CD pipeline** for a machine learning regression model using **GitHub Actions** and **Hugging Face Hub**. Every push to the `main` branch automatically executes the complete machine learning workflow, validates model performance, and deploys the trained model only if it satisfies the predefined quality gate.

---

## Modification from the Original Implementation

The original project was designed for the **Breast Cancer Wisconsin** dataset as a **binary classification** problem.

This implementation has been modified to use the **Boston Housing** dataset, converting the workflow into a **regression** pipeline.

The following modifications were made:

- Replaced the Breast Cancer dataset with the Boston Housing dataset.
- Updated the model from **RandomForestClassifier** to **RandomForestRegressor**.
- Replaced classification metrics (Accuracy, Precision, Recall, F1-Score) with regression metrics:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - R² Score
- Updated the CI/CD quality gate to validate the minimum R² score before deployment.
- Modified the Hugging Face model card to represent a regression model.

---

## CI/CD Pipeline

Every push to the **main** branch triggers the following workflow:

```
Push to GitHub
      │
      ▼
Run Unit Tests (pytest)
      │
      ▼
Prepare Dataset
      │
      ▼
Train Random Forest Regressor
      │
      ▼
Evaluate Model
      │
      ▼
Quality Gate (Minimum R²)
      │
      ▼
Deploy to Hugging Face Hub
```

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
├── src/
│   ├── prepare.py
│   ├── train.py
│   ├── evaluate.py
│   └── register.py
├── tests/
│   └── test_pipeline.py
├── params.yaml
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- GitHub Actions
- Scikit-learn
- Random Forest Regressor
- Pandas
- NumPy
- PyTest
- Hugging Face Hub
- YAML

---

## Pipeline Stages

### 1. Data Preparation
- Loads the Boston Housing dataset.
- Splits the data into training and testing datasets.
- Stores processed datasets for subsequent stages.

### 2. Model Training
- Trains a Random Forest Regressor.
- Saves the trained model and feature metadata.

### 3. Model Evaluation
Evaluates the trained model using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The pipeline proceeds only if the model satisfies the predefined R² threshold.

### 4. Model Registration
After successfully passing the quality gate, the trained model, feature metadata, and model card are automatically uploaded to Hugging Face Hub.

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Execute the pipeline:

```bash
python src/prepare.py
python src/train.py
python src/evaluate.py
```

Run unit tests:

```bash
pytest
```

---

## Learning Outcomes

- Build an automated CI/CD pipeline for machine learning.
- Integrate GitHub Actions with an MLOps workflow.
- Automate model training, evaluation, and deployment.
- Implement quality gates for regression models.
- Deploy trained models to Hugging Face Hub.

---

## Note

This implementation has been adapted from the original classification-based workflow to support **Boston Housing Price Prediction** as a regression problem. The same implementation is also included as **Experiment 5 (Ex5)** in the consolidated **DevOps Lab** repository.