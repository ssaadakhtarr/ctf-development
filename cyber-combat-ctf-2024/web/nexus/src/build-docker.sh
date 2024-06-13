#!/bin/bash
docker rm -f web_nexus
docker build -t web_nexus .
docker run --network=host --name=web_nexus --rm -p 5003:5003 -it web_nexus