FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Install Hermes (Linux AMD64)
RUN curl -L https://github.com/HermesHQ/hermes/releases/latest/download/hermes-linux-amd64 \
    -o /usr/local/bin/hermes && chmod +x /usr/local/bin/hermes

# Install OpenClaw
RUN pip install openclaw

# Create workspace
WORKDIR /app

# Copy agent files
COPY agent/ ./agent/
COPY config.yaml .

# Default command: start Hermes supervisor
CMD ["hermes", "start", "--config", "config.yaml"]

