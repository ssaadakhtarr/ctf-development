#!/bin/bash
docker rm -f web_weak
docker build -t web_weak .
docker run --network=host --name=web_weak --rm -p 5002:5002 -it web_weak