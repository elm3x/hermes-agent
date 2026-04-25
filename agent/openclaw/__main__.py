import argparse
import sys
from pathlib import Path

from .core.config import load_config
from .core.runner import run_daily_digest
from .utils.logging import log


def main():
    parser = argparse.ArgumentParser(description="Reconstructed OpenClaw Runtime")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run the daily digest agent")
    run_parser.add_argument("--config", required=True, help="Path to config.yaml")

    args = parser.parse_args()

    if args.command == "run":
        config_path = Path(args.config)
        if not config_path.exists():
            log(f"❌ Config file not found: {config_path}")
            sys.exit(1)

        config = load_config(config_path)
        run_daily_digest(config)
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
