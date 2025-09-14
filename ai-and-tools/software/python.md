# Python Setup Guide

This guide provides step-by-step instructions for installing Python 3.12 or later on Windows, macOS, and Linux systems. Python 3.12 is the minimum required version for this project.

## Prerequisites

- A computer running Windows 10 or later, macOS 10.12 or later, or a modern Linux distribution
- Internet connection for downloading the installer
- Administrator/root privileges for installation

## Installation Instructions

### Windows

1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python 3.12.x installer (Windows installer (64-bit) recommended)
3. Run the downloaded `.exe` file
4. **Important**: Check the box "Add Python to PATH" during installation
5. Follow the installation wizard, accepting the default settings
6. Restart your command prompt/terminal if it was open during installation

### macOS

#### Option 1: Official Installer (Recommended for beginners)

1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python 3.12.x installer for macOS
3. Open the downloaded `.pkg` file
4. Follow the installation wizard
5. Python will be installed in `/Library/Frameworks/Python.framework/Versions/3.12/`

#### Option 2: Homebrew (Recommended for developers)

If you have Homebrew installed:

```bash
brew install python@3.12
```

### Linux

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-pip
```

#### Fedora/CentOS/RHEL

```bash
sudo dnf install python3.12 python3-pip
```

or

```bash
sudo yum install python3.12 python3-pip
```

#### Arch Linux

```bash
sudo pacman -S python
```

#### Alternative: Install from source (all distributions)

1. Visit [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python 3.12.x source code
3. Extract and compile:

```bash
tar -xf Python-3.12.x.tar.xz
cd Python-3.12.x
./configure --enable-optimizations
make
sudo make install
```

## Verifying Installation

After installation, verify Python is correctly installed:

1. Open a terminal/command prompt
2. Run the following command:

```bash
python --version
```

or

```bash
python3 --version
```

You should see output similar to:
```
Python 3.12.x
```

If you see a version lower than 3.12, you may need to use `python3` instead of `python`, or reinstall with a newer version.

## Setting Up Virtual Environments

Virtual environments are recommended for Python development to isolate project dependencies.

### Creating a Virtual Environment

```bash
# Linux/macOS
python3 -m venv myproject_env

# Windows
python -m venv myproject_env
```

### Activating a Virtual Environment

```bash
# Linux/macOS
source myproject_env/bin/activate

# Windows
myproject_env\Scripts\activate
```

You should see `(myproject_env)` at the beginning of your command prompt.

### Deactivating a Virtual Environment

```bash
deactivate
```

## Installing Python Packages

Use pip to install packages. Always activate your virtual environment first.

```bash
pip install package_name
```

### Upgrading pip

```bash
python -m pip install --upgrade pip
```

### Installing from requirements.txt

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Troubleshooting

### Python command not found

- On Windows: Ensure Python was added to PATH during installation
- On Linux/macOS: Try using `python3` instead of `python`
- Restart your terminal/command prompt

### Permission errors during installation

- On Windows: Run the installer as Administrator
- On Linux/macOS: Use `sudo` for system-wide installation

### Multiple Python versions

If you have multiple Python versions installed, you can use `py` launcher on Windows:

```bash
py -3.12
```

Or set up aliases in your shell configuration.

### PATH issues

If Python commands aren't recognized, you may need to add Python to your system PATH:

- **Windows**: Add `C:\Python312\` and `C:\Python312\Scripts\` to your PATH environment variable
- **macOS/Linux**: Add `/usr/local/bin` or the installation directory to your PATH

## Next Steps

Once Python is set up, you can:
- Install development tools like VS Code or PyCharm
- Set up your first Python project
- Learn Python basics through tutorials and documentation

For more information, visit the official Python documentation at [https://docs.python.org/3/](https://docs.python.org/3/).