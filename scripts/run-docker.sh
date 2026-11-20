#!/bin/sh
# Run golive-checker inside the official Playwright image (no local browser install).
# Usage: scripts/run-docker.sh --csv examples/sites.csv --out out
# ANTHROPIC_API_KEY is passed by name only (docker -e VAR), so it never appears in the process list.
set -e
cd "$(dirname "$0")/.."
exec docker run --rm --init --ipc=host --memory 2g \
  -e ANTHROPIC_API_KEY \
  -v "$PWD":/app -w /app \
  mcr.microsoft.com/playwright/python:v1.65.2-noble \
  sh -c 'pip install -q --root-user-action=ignore --break-system-packages . >/dev/null 2>&1 && golive-checker "$@"; chown -R '"$(id -u):$(id -g)"' /app/out 2>/dev/null || true' -- "$@"
