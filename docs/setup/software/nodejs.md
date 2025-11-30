# Node.js Setup Guide

This guide provides step-by-step instructions for installing Node.js 22 or later on Windows, macOS, and Linux systems. Node.js 22 is the minimum required version for this project.

## Prerequisites

- A computer running Windows 10 or later, macOS 10.12 or later, or a modern Linux distribution
- Internet connection for downloading the installer
- Administrator/root privileges for installation

## Installation Instructions

### Windows

1. Visit the official Node.js website: [https://nodejs.org/](https://nodejs.org/)
2. Download the latest Node.js 22.x LTS installer (Windows Installer (.msi) 64-bit recommended)
3. Run the downloaded `.msi` file
4. Follow the installation wizard, accepting the default settings
5. Node.js and npm will be installed automatically
6. Restart your command prompt/terminal if it was open during installation

### macOS

#### Option 1: Official Installer (Recommended for beginners)

1. Visit the official Node.js website: [https://nodejs.org/](https://nodejs.org/)
2. Download the latest Node.js 22.x installer for macOS
3. Open the downloaded `.pkg` file
4. Follow the installation wizard
5. Node.js will be installed in `/usr/local/bin/`

#### Option 2: Homebrew (Recommended for developers)

If you have Homebrew installed:

```bash
brew install node@22
```

#### Option 3: Node Version Manager (nvm) (Recommended for managing multiple versions)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 22
nvm use 22
```

### Linux

#### Ubuntu/Debian

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Fedora/CentOS/RHEL

```bash
curl -fsSL https://rpm.nodesource.com/setup_22.x | sudo bash -
sudo yum install nodejs -y
```

or

```bash
curl -fsSL https://rpm.nodesource.com/setup_22.x | sudo bash -
sudo dnf install nodejs -y
```

#### Arch Linux

```bash
sudo pacman -S nodejs npm
```

#### Alternative: Node Version Manager (nvm) (Recommended for all distributions)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install 22
nvm use 22
```

## Verifying Installation

After installation, verify Node.js and npm are correctly installed:

1. Open a terminal/command prompt
2. Run the following commands:

```bash
node --version
npm --version
```

You should see output similar to:
```
v22.x.x
10.x.x
```

If you see a version lower than 22 for Node.js, you may need to reinstall or use nvm to switch versions.

## Package Management with npm

npm is the default package manager for Node.js.

### Installing Packages

```bash
npm install package_name
```

### Installing Packages Globally

```bash
npm install -g package_name
```

### Installing from package.json

If you have a `package.json` file:

```bash
npm install
```

### Creating a package.json

```bash
npm init -y
```

## Using Yarn (Alternative Package Manager)

Yarn is a popular alternative to npm.

### Installing Yarn

```bash
npm install -g yarn
```

### Using Yarn

```bash
yarn add package_name
yarn install
```

## Setting Up a Development Environment

### Creating a New Project

```bash
mkdir my-node-project
cd my-node-project
npm init -y
```

### Basic Project Structure

```
my-node-project/
├── node_modules/
├── package.json
├── package-lock.json
└── index.js
```

### Running a Node.js Application

```bash
node index.js
```

## Managing Node.js Versions

If you need to manage multiple Node.js versions, use nvm:

```bash
nvm install 22
nvm use 22
nvm list
```

## Troubleshooting

### Node command not found

- Ensure Node.js is added to your PATH
- On Linux/macOS: Try using `node` or check installation directory
- Restart your terminal/command prompt

### Permission errors during installation

- On Windows: Run the installer as Administrator
- On Linux/macOS: Use `sudo` for system-wide installation

### npm install fails

- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`
- Check network connectivity

### Port already in use

When running a server, if port 3000 is in use:

```bash
lsof -ti:3000 | xargs kill -9
```

### Updating Node.js

Using nvm:

```bash
nvm install node --latest-npm
nvm use node
```

Using npm:

```bash
npm install -g n
sudo n latest
```

## Next Steps

Once Node.js is set up, you can:
- Install development tools like VS Code or WebStorm
- Set up your first Node.js project
- Learn Node.js basics through tutorials and documentation
- Explore frameworks like Express.js, React, or Vue.js

For more information, visit the official Node.js documentation at [https://nodejs.org/docs/](https://nodejs.org/docs/).