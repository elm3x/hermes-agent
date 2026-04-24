FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Pin cmdop + OpenClaw to the last known compatible versions
RUN pip install "cmdop==0.1.43" "openclaw==0.1.9"

# Install your other dependencies
RUN pip install tenacity httpx pydantic aiohttp python-telegram-bot tavily-python openrouter

WORKDIR /app

COPY agent/ ./agent/
COPY config.yaml .

CMD ["python", "-m", "openclaw", "run", "--config", "config.yaml"]
