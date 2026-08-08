# MLOps FastAPI Docker

A containerized machine learning API built using FastAPI and Docker. The application serves a trained machine learning model through REST API endpoints.

---

# Docker Setup

## 1. Build the Docker Image

Navigate to the `ex4` directory and run:

```bash
docker build -t shree8806/mlops-fastapi-docker:latest .
```

---

## 2. Run the Docker Container

```bash
docker run -p 8000:8000 shree8806/mlops-fastapi-docker:latest
```

The API will now be available at:

```text
http://localhost:8000
```

Interactive API documentation is available at:

```text
http://localhost:8000/docs
```

---

## 3. Push the Image to Docker Hub

Login to Docker Hub:

```bash
docker login
```

Push the image:

```bash
docker push shree8806/mlops-fastapi-docker:latest
```

---

## 4. Pull the Image

Anyone can pull the Docker image using:

```bash
docker pull shree8806/mlops-fastapi-docker:latest
```

---

## 5. Run the Pulled Image

```bash
docker run -p 8000:8000 shree8806/mlops-fastapi-docker:latest
```

The API can then be accessed at:

```text
http://localhost:8000
```

---

# API Endpoints

## Home

**GET**

```text
/
```

---

## Health Check

**GET**

```text
/health
```

### Response

```json
{
    "status": "ok"
}
```

---

## Prediction

**POST**

```text
/predict
```

### Request

The API expects four features corresponding to the trained classification model.

```json
{
    "features": [
        5.1,
        3.5,
        1.4,
        0.2
    ]
}
```

### Example Response

```json
{
    "predicted_class": "setosa",
    "confidence": 0.99,
    "probabilities": {
        "setosa": 0.99,
        "versicolor": 0.01,
        "virginica": 0.00
    }
}
```

---

# Project Structure

```text
ex4/
├── Dockerfile
├── README.md
├── app.py
├── model.joblib
└── requirements.txt
```

---

# Docker Hub Repository

[shree8806/mlops-fastapi-docker](https://hub.docker.com/r/shree8806/mlops-fastapi-docker)

---

# Technologies Used

- Python
- FastAPI
- Scikit-learn
- Docker
- Uvicorn