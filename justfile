# List all commands.
default:
  @just --list

# Do a dev install.
dev:
  uv sync --all-extras --dev

# Run code checks.
check:
  #!/usr/bin/env bash

  error=0
  trap error=1 ERR

  echo
  (set -x; uv run ruff check src/ tests/ )
  test $? = 0

  echo
  ( set -x; uv run ruff format --check src/ tests/ )
  test $? = 0

  echo
  ( set -x; uv run mypy src/ tests/ )
  test $? = 0

  echo
  ( set -x; uv run make -C tests html )
  test $? = 0

  test $error = 0

# Build test docs
test-docs:
  rm -r ./tests/build
  uv run make -C tests html
  echo Your docs are in: $PWD/tests/build/html/index.html

# Auto-fix code issues.
fix:
  black .
  ruff --fix .
