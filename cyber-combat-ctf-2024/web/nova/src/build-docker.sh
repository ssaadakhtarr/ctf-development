#!/bin/bash
docker rm -f web_nova
docker build -t web_nova .
docker run --network=host --name=web_nova --rm -p 5000:5000 -it web_nova