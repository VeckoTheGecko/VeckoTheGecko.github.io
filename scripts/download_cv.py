#!/usr/bin/env python3
"""Download the latest cv.pdf from the VeckoTheGecko/resume GitHub release."""

import argparse
import subprocess
import sys

import requests

REPO = "VeckoTheGecko/resume"
ASSET_NAME = "cv.pdf"
API_URL = f"https://api.github.com/repos/{REPO}/releases/latest"


def get_token(provided: str | None) -> str:
    if provided:
        return provided
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit("No --token provided and `gh auth token` failed. Run `gh auth login` first.")
    return result.stdout.strip()


def download_cv(token: str, output: str) -> None:
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()
    release = response.json()

    try:
        asset = next(a for a in release["assets"] if a["name"] == ASSET_NAME)
    except StopIteration:
        sys.exit(f"No asset named '{ASSET_NAME}' found in latest release.")

    asset_response = requests.get(
        asset["url"],
        headers={**headers, "Accept": "application/octet-stream"},
        allow_redirects=True,
    )
    asset_response.raise_for_status()

    with open(output, "wb") as f:
        f.write(asset_response.content)

    print(f"Downloaded {ASSET_NAME} -> {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token", help="GitHub personal access token")
    parser.add_argument(
        "--output",
        default="docs/assets/Nick Hodgskin CV.pdf",
        help="Output file path (default: docs/assets/Nick Hodgskin CV.pdf)",
    )
    args = parser.parse_args()

    token = get_token(args.token)
    download_cv(token, args.output)


if __name__ == "__main__":
    main()
