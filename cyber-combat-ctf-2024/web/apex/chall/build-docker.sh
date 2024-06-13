#!/bin/bash
docker rm -f web_apex
docker build -t web_apex .
docker run --network=host --name=web_apex --rm -p 5001:5001 -it web_apex