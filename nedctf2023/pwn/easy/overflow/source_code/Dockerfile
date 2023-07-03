# Use a minimal base image for security
FROM ubuntu:20.04

# Copy the challenge source code to the container
COPY overflow.c .
COPY flag.txt .

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y socat

RUN gcc -fno-pie -no-pie -z execstack overflow.c -o overflow

# Set the entrypoint command to run the challenge
ENTRYPOINT socat TCP-LISTEN:9001,reuseaddr,fork EXEC:'./overflow'
