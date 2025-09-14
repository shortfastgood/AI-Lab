#!/bin/bash
# markitdown.sh: Install and start the markitdown MCP server
# Requirements: Python 3.12 or higher must be installed on the system

set -e  # Exit on error

source ./instpy.sh  # Ensure the Python environment is set up

echo "Installing markitdown server..."

pip install markitdown-mcp

echo "Starting markitdown server..."

markitdown-mcp --http --host 127.0.0.1 --port 3001

