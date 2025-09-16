param()

Write-Host "markitdown.ps1: Install and start the markitdown MCP server"
Write-Host "Requirements: Python 3.12 or higher must be installed on the system"

# Source the equivalent of instpy.sh
Write-Host "Setting up Python environment..."
try {
    & .\instpy.ps1
} catch {
    Write-Host "Failed to set up Python environment: $_"
    exit 1
}

Write-Host "Installing markitdown server..."

try {
    pip install markitdown-mcp
    if ($LASTEXITCODE -ne 0) {
        throw "pip install failed"
    }
} catch {
    Write-Host "Failed to install markitdown-mcp: $_"
    exit 1
}

Write-Host "Starting markitdown server..."

try {
    markitdown-mcp --http --host 127.0.0.1 --port 3001
} catch {
    Write-Host "Failed to start markitdown server: $_"
    exit 1
}