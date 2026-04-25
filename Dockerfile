FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl unzip && apt-get clean

# Install only what your vendored runtime actually needs
RUN pip install requests pyyaml

WORKDIR /app

COPY agent/ ./agent/
COPY config.yaml .

CMD ["python", "-m", "agent.openclaw", "run", "--config", "config.yaml"]
