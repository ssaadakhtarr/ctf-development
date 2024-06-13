#!/bin/bash
docker rm -f web_onion
docker build -t web_onion .
docker run --network=host --name=web_onion --rm -p 5002:5002 -it web_onion