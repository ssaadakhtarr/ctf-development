#!/bin/bash

# Build the Docker image

docker rm -f pwn_variable
docker build -t pwn_variable .
docker run --network=host --name=pwn_jeeves --rm -p 9003:9003 -it pwn_variable
