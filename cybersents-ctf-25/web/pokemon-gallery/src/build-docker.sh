#!/bin/bash
docker rm -f web_pika
docker build -t web_pika .
docker run --network=host --name=web_pika --rm -p 5000:5000 -it web_pika