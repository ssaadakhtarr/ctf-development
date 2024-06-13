# Use a minimal base image for security
FROM ubuntu:20.04

# Copy the challenge source code to the container
COPY challenge.c .

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y socat

RUN gcc challenge.c -o challenge

# Set the entrypoint command to run the challenge
ENTRYPOINT socat TCP-LISTEN:9000,reuseaddr,fork EXEC:'./challenge'
