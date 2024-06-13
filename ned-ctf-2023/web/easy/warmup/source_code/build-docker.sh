#!/bin/bash
docker rm -f warmup_web
docker build -t warmup_web .
docker run --network=host --name=warmup_web --rm -p 5000:5000 -it warmup_web