#!/bin/bash
echo "🚀 Setting up Finance App environment..."

# 1. Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created."
fi

# 2. Activate environment and install pinned dependencies
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Dependencies installed successfully!"
echo "▶️  Run 'source venv/bin/activate' and then 'reflex run' to start the app."