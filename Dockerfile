FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Install OpenClaw and all required dependencies manually
RUN pip install openclaw tenacity httpx pydantic aiohttp python-telegram-bot tavily-python openrouter

# Create workspace
WORKDIR /app

# Copy agent files
COPY agent/ ./agent/
COPY config.yaml .

# Start OpenClaw (which starts Hermes internally)
CMD ["python", "-m", "openclaw", "run", "--config", "config.yaml"]
