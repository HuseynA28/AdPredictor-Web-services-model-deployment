# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the entire project into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for the model path
ENV MODEL_PATH=/app/models/advertising_model.pkl

# Run FastAPI.py when the container launches, adjust the path as necessary
CMD ["uvicorn", "scripts.FastAPI:app", "--host", "0.0.0.0", "--port", "8000"]