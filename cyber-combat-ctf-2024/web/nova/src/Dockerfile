FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Create a low privileged user
# RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN adduser --system --group appuser

# Set ownership and permissions for the application files
# RUN chown -R appuser:appgroup /app
RUN chmod -R 755 /app

# Set the user to run the application
USER appuser

EXPOSE 5000

CMD ["python3", "app.py"]
