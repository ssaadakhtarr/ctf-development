FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc python3-dev libjpeg-dev zlib1g-dev \
    php php-cli curl && \
    rm -rf /var/lib/apt/lists/*


RUN groupadd -r pokemon && useradd -r -g pokemon -d /app pokemon

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

WORKDIR /app

COPY --chown=pokemon:pokemon python-app/requirements.txt ./python-app/
RUN pip install --no-cache-dir -r python-app/requirements.txt

COPY --chown=pokemon:pokemon . .

RUN mkdir -p /app/python-app /app/php-app && \
    chown pokemon:pokemon /app/python-app /app/php-app && \
    chmod 755 /app && \
    chmod 750 /app/python-app /app/php-app && \
    chmod 644 /app/python-app/app.py

RUN mv /app/flag.txt /flag.txt && \
    chown root:root /flag.txt && chmod 444 /flag.txt

USER pokemon

EXPOSE 5000

CMD ["sh", "-c", "php -S 127.0.0.1:8000 -t /app/php-app > /dev/null 2>&1 & python /app/python-app/app.py"]