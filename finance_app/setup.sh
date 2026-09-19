#!/bin/bash
set -e

echo "🚀 Setting up Finance App environment..."

PYTHON_BIN="${PYTHON_BIN:-python3.12}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    for candidate in python3.11 python3; do
        if command -v "$candidate" >/dev/null 2>&1; then
            PYTHON_BIN="$candidate"
            break
        fi
    done
fi

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    echo "❌ No compatible Python interpreter found. Please install Python 3.12 or 3.11." >&2
    exit 1
fi

echo "Using Python interpreter: $PYTHON_BIN"

deactivate >/dev/null 2>&1 || true
unset VIRTUAL_ENV
unset PYTHONPATH

# Recreate a broken/incompatible venv so the dependency install succeeds.
if [ -d "venv" ] && { [ ! -x "venv/bin/python" ] || ! venv/bin/python -c "import sys; raise SystemExit(0 if sys.version_info[:2] in ((3, 11), (3, 12)) else 1)" >/dev/null 2>&1; }; then
    echo "⚠️ Existing environment is missing or incompatible; recreating venv..."
    rm -rf venv
fi

# 1. Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    "$PYTHON_BIN" -m venv venv
    echo "✅ Virtual environment created."
fi

# 2. Activate environment and install pinned dependencies
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "✅ Dependencies installed successfully!"
echo "▶️  Run 'source venv/bin/activate' and then 'reflex run' to start the app."