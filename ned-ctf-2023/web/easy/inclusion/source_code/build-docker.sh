#!/bin/bash

# Build the Docker image

docker rm -f web_inclusion
docker build -t web_inclusion .
docker run --name=web_inclusion --rm -p5000:5000 -it web_inclusion
