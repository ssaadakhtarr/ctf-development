#!/bin/bash
docker rm -f web_weak
docker build -t web_weak .
docker run --name=web_weak --rm -p5000:5000 -it web_weak