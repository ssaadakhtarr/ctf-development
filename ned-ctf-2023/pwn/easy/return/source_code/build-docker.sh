#!/bin/bash

# Build the Docker image

docker rm -f pwn_return
docker build -t pwn_return .
docker run --network=host --name=pwn_return --rm -p 9002:9002 -it pwn_return
