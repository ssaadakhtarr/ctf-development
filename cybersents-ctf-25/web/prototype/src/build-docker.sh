#!/bin/bash
docker rm -f web_prototype
docker build -t web_prototype .
docker run --network=host --name=web_prototype --rm -p 5000:5000 -it web_prototype