#!/bin/bash

# Build the Docker image

docker rm -f pwn_overflow
docker build -t pwn_overflow .
docker run --network=host --name=pwn_overflow --rm -p 9001:9001 -it pwn_overflow
