#!/bin/bash

# Build the Docker image

docker rm -f pwn_pie
docker build -t pwn_pie .
docker run --network=host --name=pwn_pie --rm -p 9004:9004 -it pwn_pie
