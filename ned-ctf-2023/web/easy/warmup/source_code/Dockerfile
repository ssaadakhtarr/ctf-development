# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application files to the working directory
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Set the entrypoint command to run the Flask application
CMD ["python", "app.py"]
