FROM python:3.9

# RUN useradd -m ctfuser

WORKDIR /app

COPY app.py init_db.py /app/
COPY templates /app/templates

RUN pip install flask

RUN python init_db.py

# USER ctfuser

EXPOSE 5000

CMD ["python", "app.py"]
