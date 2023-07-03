#!/bin/bash
docker rm -f web_authforgery
docker build -t web_authforgery .
docker run --network=host --name=web_authforgery --rm -p5000:5000 -it web_authforgery