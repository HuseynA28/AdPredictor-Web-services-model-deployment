# AdPredictor Web Service (Automating ML Model Deployment with GitHub Actions to Docker Hub)..

## Introduction

The AdPredictor Web Service automates the lifecycle of a machine learning model that predicts advertising sales based on expenditures in different media channels (TV, radio, and newspapers). This project utilizes GitHub Actions to automate the training and deployment of the machine learning model, seamlessly updating the Docker image on Docker Hub whenever the underlying model or dataset changes.

## Workflow Description

The workflow of this project is designed to enhance collaboration between two key departments:

- **Data Science Department**: Responsible for training and updating the machine learning model. Whenever the model's code or the dataset is updated, these changes trigger GitHub Actions.
- **Deployment and Operations Department**: Utilizes the updated model for prediction tasks. The automated pipeline ensures that they always have access to the latest version of the model via Docker Hub, without needing to manually handle updates.

## Problem Solved

This automated system addresses the challenge of ensuring that the predictive model is always up-to-date with the latest data and improvements, without manual intervention. The automation pipeline does the following:

1. **Trains the Model Automatically**: Whenever there are updates to the dataset or the model's code, GitHub Actions automatically trigger the retraining process.
2. **Creates a Docker Image**: Post-training, a Docker image encapsulating the trained model is automatically created.
3. **Deploys to Docker Hub**: The new Docker image is then pushed to Docker Hub, making it readily available for deployment.
4. **Easy Access and Deployment**: Stakeholders and the Deployment Department can pull the updated Docker image from Docker Hub at any time to make accurate predictions based on the latest model.

## Benefits

- **Continuous Integration and Deployment**: Any changes in the dataset or model logic trigger a new cycle of integration and deployment, ensuring that the model is never outdated.
- **Decentralization of Tasks**: Frees up the Data Science team from deployment tasks by automating model updates and image creation, allowing them to focus on model improvement and research.
- **Seamless Access to Latest Model**: Ensures that all stakeholders have instant access to the most recent model without any need for manual updating or intervention.



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

## Continuous Integration and Deployment with GitHub Actions
To automate the training of your model and deployment to Docker Hub, follow these steps:

Add Docker Credentials to GitHub Secrets:

Go to your repository on GitHub.
Navigate to Settings > Secrets and variables > Actions.
Add the following secrets:
DOCKERUSERNAME: Your Docker Hub username.
PASSWORD: Your Docker Hub password.
Push the Dataset to Your GitHub Repository:

Ensure your dataset is included in the repository so it can be accessed during the training process.
GitHub Actions Workflow:
Create a .github/workflows/deploy.yml file in your repository with the following content:

## Technologies Used

- **FastAPI**: For building a highly efficient and scalable API service.
- **Docker**: For containerizing the application and ensuring environment consistency.
- **GitHub Actions**: For continuous integration and continuous deployment (CI/CD), automating the model training and deployment process.

## Conclusion

By automating the training and deployment of the AdPredictor model with GitHub Actions to Docker Hub, this project efficiently bridges the gap between data science and operational deployment. It ensures that the predictive service is robust, up-to-date, and readily available for making accurate predictions, thus maximizing the advertising spend ROI for businesses.


## Author

- **Huseyn Abdullayev**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
