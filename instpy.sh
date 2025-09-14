#!/bin/bash
# instpy.sh: Install and set up Python virtual environment for ai-development/ai-python
# Requirements: Python 3.12 or higher must be installed on the system

set -e  # Exit on error

echo "Starting Python virtual environment setup..."

# Determine Python command
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Neither python3 nor python found. Please install Python 3.12 or higher."
    exit 1
fi

echo "Using Python command: $PYTHON_CMD"

# Check Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"

# Extract major and minor version
MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$MAJOR" -lt 3 ] || ([ "$MAJOR" -eq 3 ] && [ "$MINOR" -lt 12 ]); then
    echo "Error: Python version $PYTHON_VERSION is less than 3.12. Please upgrade Python."
    exit 1
fi

echo "Python version is sufficient."

# Venv path
VENV_PATH="./ai-development/ai-python/.venv"

# Check if venv exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Creating virtual environment at $VENV_PATH..."
    $PYTHON_CMD -m venv "$VENV_PATH"
else
    echo "Virtual environment already exists at $VENV_PATH."
fi

# Activate venv
echo "Activating virtual environment..."
source "$VENV_PATH/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
REQ_FILE="ai-development/ai-python/requirements.txt"
if [ -f "$REQ_FILE" ]; then
    echo "Installing packages from $REQ_FILE..."
    pip install -r "$REQ_FILE"
else
    echo "Warning: $REQ_FILE not found. Skipping package installation."
fi

echo "Setup complete!"

# Activate venv at the end
source "$VENV_PATH/bin/activate"