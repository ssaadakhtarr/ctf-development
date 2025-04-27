#!/bin/bash
docker rm -f web_flagshop
docker build -t web_flagshop .
docker run --network=host --name=web_flagshop --rm -p 3000:3000 -it web_flagshop