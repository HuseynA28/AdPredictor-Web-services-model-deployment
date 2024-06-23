
# AdPredictor Web Service (Deploying ML Model Automatically with GitHub Actions to Docker Hub)

## Overview

The AdPredictor Web Service is a cutting-edge solution designed by Huseyn Abdullayev, aimed at revolutionizing the advertising industry. This project leverages a machine learning model to predict advertising sales based on investment across various channels such as TV, radio, and newspapers. Hosted using FastAPI and containerized with Docker, the service ensures scalability and ease of deployment.

## Business Problem Solved

This service addresses the critical business need of optimizing advertising spend. By predicting the sales outcomes based on advertising investments, businesses can allocate their budgets more efficiently, maximizing ROI and reducing wastage in underperforming channels.

## Project Structure

```
AdPredictor-Web-Service/
├── .github/
│   └── workflows/
│       └── train_and_deploy.yml  # CI/CD pipeline for automating training and deployment
├── data/
│   └── advertising.csv            # Dataset for model training
├── models/
│   └── advertising_model.pkl      # Trained predictive model
├── scripts/
│   ├── FastAPI.py                 # FastAPI application for API service
│   └── train_model.py             # Script to train the predictive model
├── Dockerfile                     # Docker configuration for building the service
└── requirements.txt               # Dependencies required for the project
```

## Key Features

- **Automated Model Training**: Utilizes GitHub Actions to retrain the machine learning model whenever updates are pushed, ensuring the model evolves with new data.
- **Robust API Service**: Deployed via FastAPI, providing a responsive and scalable service for real-time prediction requests.
- **Containerization with Docker**: Guarantees consistent environments from development to production, simplifying deployments and testing.

## Getting Started

### Prerequisites

- Docker installed on your machine
- Git for cloning the repository

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/AdPredictor-Web-Service.git
   cd AdPredictor-Web-Service
   ```

2. **Build the Docker Image**:
   ```bash
   docker build -t adpredictor-web-service .
   ```

3. **Run the Docker Container**:
   ```bash
   docker run -p 8000:8000 adpredictor-web-service
   ```

4. **Access the API**:
   Navigate to `http://localhost:8000` in your web browser to interact with the API.

## API Documentation

- **POST /predict**: Receives advertising spend data (TV, radio, newspaper) and returns sales predictions.
  ```bash
  curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"tv": 150, "radio": 25, "newspaper": 15}'
  ```
- **GET /status**: Provides the current status of the API.
  ```bash
  curl http://localhost:8000/status
  ```

## Technologies Used

- **FastAPI**: For building a highly efficient and scalable API service.
- **Docker**: For containerizing the application and ensuring environment consistency.
- **GitHub Actions**: For continuous integration and continuous deployment (CI/CD), automating the model training and deployment process.

## Author

- **Huseyn Abdullayev**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
