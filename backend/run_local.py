"""Start the foundation API on loopback, without loading private configuration."""

import argparse

import uvicorn


def port_number(value: str) -> int:
    port = int(value)
    if not 1024 <= port <= 65535:
        raise argparse.ArgumentTypeError("Port must be between 1024 and 65535.")
    return port


def main() -> None:
    parser = argparse.ArgumentParser(description="Run CPA locally on 127.0.0.1.")
    parser.add_argument("--port", type=port_number, default=8000)
    args = parser.parse_args()
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=args.port,
        access_log=False,
        log_level="critical",
        server_header=False,
        proxy_headers=False,
    )


if __name__ == "__main__":
    main()
