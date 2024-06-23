# AdPredictor Web Service

This project hosts a machine learning model using FastAPI, which predicts advertising sales based on TV, radio, and newspaper spend. The service is containerized using Docker for easy deployment and scalability.

## Project Structure

AdPredictor-Web-Service/
├── .github/
│ └── workflows/
│ └── train_and_deploy.yml # CI/CD pipeline for training and deploying the model
├── data/
│ └── advertising.csv # Dataset used for training the model
├── models/
│ └── advertising_model.pkl # Trained machine learning model
├── scripts/
│ ├── FastAPI.py # FastAPI application file
│ └── train_model.py # Script for training the machine learning model
├── Dockerfile # Dockerfile for building the container image
└── requirements.txt # Python dependencies required for the project


## Features

- **Model Training**: Automatically retrain the model using GitHub Actions upon pushing changes.
- **API Service**: A FastAPI application that serves the trained model predictions.
- **Dockerization**: Containerized application for easy deployment and environment consistency.

## How to Run Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/AdPredictor-Web-Service.git
   cd AdPredictor-Web-Service
```bash


Build the Docker Image:
 ```bash
docker build -t adpredictor-web-service .
 ```bash

 Run the Container:
 ```bash
docker run -p 8000:8000 adpredictor-web-service
  ```bash


Access the API:
Open your web browser and navigate to:
 ```bash
 http://localhost:8000
  ```bash

API Endpoints
- /predict - POST method; accepts JSON input with TV, radio, and newspaper advertising budgets and returns the sales prediction.
   ```bash
   curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"tv": 150, "radio": 25, "newspaper": 15}'
   ```bash

- /status - GET method; returns the status of the API service
  ```bash
  curl http://localhost:8000/status
   ```bash

How to Use the API
Interact with the API using tools like curl or Postman. Example cURL requests are provided above for the /predict and /status endpoints.


### Explanation

- The **API Endpoints** section is now clearly formatted with Markdown code blocks to showcase how one might interact with the API using cURL.
- Ensure you replace `<your-username>` with your actual GitHub username in the clone URL.
- This format should make it easy for users to understand and interact with your web service effectively.

By formatting your README.md with these details, you make it much more user-friendly and functional for developers who may want to use or contribute to your project.
