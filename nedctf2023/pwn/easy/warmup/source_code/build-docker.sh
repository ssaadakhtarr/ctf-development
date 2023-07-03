#!/bin/bash

# Build the Docker image

docker rm -f pwn_warmup
docker build -t pwn_warmup .
docker run --network=host --name=pwn_warmup --rm -p 9000:9000 -it pwn_warmup
