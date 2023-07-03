FROM python:3.9-alpine

WORKDIR /app
COPY app.py /app/
COPY flag.txt /

RUN pip install flask

EXPOSE 5000
CMD ["python3", "app.py"]

