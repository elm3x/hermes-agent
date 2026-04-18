FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl unzip file && apt-get clean

# Install Rust (for building Hermes)
RUN apt-get update && apt-get install -y curl unzip build-essential pkg-config libssl-dev && apt-get clean

# Install Rust toolchain
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Build and install Hermes from source
RUN cargo install hermes-cli



# Install OpenClaw
RUN pip install openclaw

# Create workspace
WORKDIR /app

# Copy agent files
COPY agent/ ./agent/
COPY config.yaml .

# Default command: start Hermes supervisor
CMD ["hermes", "start", "--config", "config.yaml"]
