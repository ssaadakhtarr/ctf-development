#!/bin/bash
docker rm -f misc_number_seeker
docker build -t misc_number_seeker .
docker run --network=host --name=misc_number_seeker --rm -p 9000:9000 -it misc_number_seeker