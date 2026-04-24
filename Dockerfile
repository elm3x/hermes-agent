FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Install OpenClaw + all required deps
RUN pip install openclaw tenacity httpx pydantic aiohttp python-telegram-bot tavily-python openrouter

WORKDIR /app

COPY agent/ ./agent/
COPY config.yaml .

CMD ["python", "-m", "openclaw", "run", "--config", "config.yaml"]
