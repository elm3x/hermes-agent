FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Install OpenClaw (includes Hermes runtime)
RUN pip install openclaw

# Create workspace
WORKDIR /app

# Copy agent files
COPY agent/ ./agent/
COPY config.yaml .

# Start the OpenClaw Hermes runtime
CMD ["openclaw", "run", "--config", "config.yaml"]
