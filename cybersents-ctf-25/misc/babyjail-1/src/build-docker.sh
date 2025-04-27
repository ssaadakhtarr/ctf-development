#!/bin/bash
docker rm -f misc_babyjail1
docker build -t misc_babyjail1 .
docker run --network=host --name=misc_babyjail1 --rm -p 1337:1337 -it misc_babyjail1