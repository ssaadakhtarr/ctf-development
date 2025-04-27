#!/bin/bash
docker rm -f web_phpone
docker build -t web_phpone .
docker run --network=host --name=web_phpone --rm -p 80:80 -it web_phpone