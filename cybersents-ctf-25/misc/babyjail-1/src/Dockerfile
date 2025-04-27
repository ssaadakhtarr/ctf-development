FROM python:3.10-slim

# Install socat
RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

# Add low-privileged user
RUN useradd -m ctf

# Set working directory
WORKDIR /home/ctf

# Copy challenge files
COPY --chown=ctf:ctf jail.py start.sh .
COPY flag.txt /flag.txt

RUN chmod 444 /flag.txt

# Make sure start.sh is executable
RUN chmod +x start.sh

# Expose challenge port
EXPOSE 1337

# Switch to low-privileged user
USER ctf

# Start the jail
CMD ["./start.sh"]
