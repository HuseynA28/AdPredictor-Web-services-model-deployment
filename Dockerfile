name: Train Model and Deploy

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  workflow_dispatch:

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Train model
      run: python scripts/train_model.py

    - name: Log in to Docker Hub
      run: echo "${{ secrets.PASSWORD }}" | docker login -u "${{ secrets.DOCKERUSERNAME }}" --password-stdin

    - name: Build Docker image
      run: docker build -t your-docker-username/adpredictor-web-service:latest .

    - name: Push Docker image
      run: docker push your-docker-username/adpredictor-web-service:latest
