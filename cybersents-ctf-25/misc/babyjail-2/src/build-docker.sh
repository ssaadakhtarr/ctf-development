#!/bin/bash
docker rm -f misc_babyjail2
docker build -t misc_babyjail2 .
docker run --network=host --name=misc_babyjail2 --rm -p 1337:1337 -it misc_babyjail2