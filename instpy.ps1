param()

Write-Host "Starting Python virtual environment setup..."

# Determine Python command
$pythonCmd = $null
if (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonCmd = "python3"
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} else {
    Write-Host "Python not found. Please install Python 3.12 or later."
    exit 1
}

# Check version
$versionOutput = & $pythonCmd --version 2>&1
if ($versionOutput -match "Python (\d+)\.(\d+)") {
    $major = [int]$matches[1]
    $minor = [int]$matches[2]
    if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 12)) {
        Write-Host "Python version $major.$minor is too old. Please install Python 3.12 or later."
        exit 1
    }
} else {
    Write-Host "Unable to determine Python version."
    exit 1
}

Write-Host "Python version is $major.$minor, which is acceptable."

# Venv path
$venvPath = "ai-development/ai-python/.venv"

# Create directories if needed
$venvDir = Split-Path $venvPath
if (!(Test-Path $venvDir)) {
    New-Item -ItemType Directory -Path $venvDir -Force
}

# Create venv if not exists
if (!(Test-Path $venvPath)) {
    Write-Host "Creating virtual environment at $venvPath..."
    & $pythonCmd -m venv $venvPath
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to create virtual environment."
        exit 1
    }
} else {
    Write-Host "Virtual environment already exists at $venvPath."
}

# Activate
Write-Host "Activating virtual environment..."
& "$venvPath\Scripts\Activate.ps1"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to activate virtual environment."
    exit 1
}

# Upgrade pip
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip
if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to upgrade pip."
    exit 1
}

# Install requirements
$reqPath = "ai-development/ai-python/requirements.txt"
if (Test-Path $reqPath) {
    Write-Host "Installing packages from $reqPath..."
    pip install -r $reqPath
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install packages."
        exit 1
    }
} else {
    Write-Host "Requirements file not found at $reqPath. Skipping package installation."
}

# Activate at the end
Write-Host "Activating virtual environment for the session..."
& "$venvPath\Scripts\Activate.ps1"

Write-Host "Setup complete."