# Install Python 3 - Step by Step Guide

## Current Latest Stable Version

**Python 3.14.6** — released June 10, 2026

---

## 1. Linux (Ubuntu) — Using Official Packages

```bash
# Add the deadsnakes PPA (provides newer Python versions)
sudo add-apt-repository ppa:deadsnakes/ppa

# Update package list
sudo apt-get update

# Install Python 3.14
sudo apt-get install python3.14

# Verify installation
python3.14 --version
```

> **Note:** On Ubuntu 24.04+, Python 3.12 is available in the default repositories:
> ```bash
> sudo apt update
> sudo apt install python3 python3-full python3-dev
> python3 --version
> ```

---

## 2. macOS — Using Homebrew (brew)

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Update package list and install Python
brew update
brew install python

# Verify installation
python3 --version
```

Or install a specific version:
```bash
brew install python@3.14
python3.14 --version
```

---

## 3. Windows 11 — Using Official Installer from python.org

**Method A: Download and run the installer (recommended)**

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Click **"Download Python 3.14.6"** (or the latest version shown)
3. Run the downloaded `python-3.14.6-amd64.exe` installer
4. **Important**: Check ✅ **"Add python.exe to PATH"** before installing
5. Click **"Install Now"** (for all users) or **"Customize installation"** for options
6. After installation completes, click **"Close"**

**Method B: Using winget (Windows Package Manager — built into Win 11)**

```powershell
winget install --id Python.Python.3.14 --source winget
```

---

## Verification Across All Platforms

After installation on any platform, verify it works:

```bash
python3 --version      # macOS/Linux
python --version       # Windows (or "python3" if alias needed)
python -c "import sys; print(sys.version)"
```

Created using VSCode, GitHub Copilot, Ollama, Qwen3.6:35b-a3b-nvfp4, 2026-07-26.