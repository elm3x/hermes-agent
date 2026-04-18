FROM debian:bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv \
    curl unzip build-essential pkg-config libssl-dev file \
    && apt-get clean

# Install Rust toolchain
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Build and install Hermes from source
RUN cargo install hermes-cli

# Install OpenClaw
RUN pip3 install openclaw

# Create workspace
WORKDIR /app

# Copy agent files
COPY agent/ ./agent/
COPY config.yaml .

CMD ["hermes-cli", "start", "--config", "config.yaml"]
