FROM python:3.9-slim-buster
WORKDIR /app
COPY templates templates
COPY app.py .
COPY requirements.txt .
COPY flag.txt /
RUN pip install --no-cache-dir -r requirements.txt
RUN adduser --system --group appuser
RUN chmod -R 755 /app
USER appuser
EXPOSE 5001
CMD ["python3", "app.py"]