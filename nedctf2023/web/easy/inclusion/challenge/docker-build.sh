#!/bin/bash

# Build the Docker image

docker rm -f web_inclusion
docker build -t web_inclusion .
docker run --network=host --name=web_inclusion --rm -p 5001:5001 -it web_inclusion
