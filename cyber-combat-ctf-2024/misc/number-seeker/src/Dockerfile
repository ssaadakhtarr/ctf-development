# Dockerfile

# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && \
    apt-get install -y socat 

# Install any dependencies needed for your script
# For example, if you have dependencies listed in requirements.txt:
# RUN pip install --no-cache-dir -r requirements.txt
# Create a non-root user
RUN useradd -ms /bin/bash appuser

# Set permissions
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Make port 1234 available to the world outside this container
EXPOSE 9000

# Run challenge.py when the container launches
ENTRYPOINT socat TCP-LISTEN:9000,reuseaddr,fork EXEC:"python3 gen.py"
# CMD ["python", "t4.py"]
