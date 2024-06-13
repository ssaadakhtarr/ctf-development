# Use the official Python 3.8 image as the base image
FROM python:3.8

# Optional: Set the working directory inside the container
WORKDIR /app

# Optional: Copy the contents of your local directory into the container
COPY . /app

# Optional: Install additional dependencies, if needed
RUN pip install uncompyle6

# Optional: Expose any ports your application may need
# EXPOSE 8000

# Optional: Specify a command to run when the container starts
CMD ["/bin/bash"]
