# List all commands.
default:
  @just --list

# Do a dev install.
dev:
  pip install -e '.[dev]'

# Run code checks.
check:
  #!/usr/bin/env bash

  error=0
  trap error=1 ERR

  echo
  (set -x; ruff check src/ tests/ )
  test $? = 0

  echo
  ( set -x; ruff format --check src/ tests/ )
  test $? = 0

  echo
  ( set -x; mypy src/ tests/ )
  test $? = 0

  echo
  ( set -x; make -C tests html )
  test $? = 0

  test $error = 0

# Auto-fix code issues.
fix:
  black .
  ruff --fix .
