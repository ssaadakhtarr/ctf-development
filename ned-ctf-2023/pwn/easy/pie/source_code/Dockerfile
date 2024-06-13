# Use a minimal base image for security
FROM ubuntu:20.04

# Copy the challenge source code to the container
COPY pie.c .
COPY flag.txt .

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y socat 

# RUN echo 0 | tee /proc/sys/kernel/randomize_va_space

RUN gcc -fno-stack-protector pie.c -o pie

# Set the entrypoint command to run the challenge
ENTRYPOINT socat TCP-LISTEN:9004,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./pie"
