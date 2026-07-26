# Install Node.js v24.18.0 (Latest LTS) — Step by Step

## 1️⃣ Linux (Ubuntu)

**Option A — Using `apt` with NodeSource official repository:**

```bash
# Step 1: Install prerequisites
sudo apt update
sudo apt install -y ca-certificates curl gnupg

# Step 2: Download and run the NodeSource setup script
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/debian-gpg-key@nodesource.list | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_24.x nodist main" | \
  sudo tee /etc/apt/sources.list.d/nodesource.list

# Step 3: Install Node.js LTS
sudo apt update
sudo apt install -y nodejs

# Step 4: Verify installation
node -v    # Should print v24.18.0
npm -v     # Should print 11.16.0
```

---

## 2️⃣ macOS (using Homebrew)

```bash
# Step 1: Ensure Homebrew is up to date
brew update

# Step 2: Install Node.js (the `node` formula installs the latest stable LTS, currently v24.x)
brew install node

# Step 3: Verify installation
node -v    # Should print v24.18.0
npm -v     # Should print 11.16.0
```

> **Note:** The `node` formula in Homebrew currently provides the latest stable version (v26.x), while `node@24` specifically gives you v24.18.0 LTS. If you want to pin to the exact LTS, use:
> ```bash
> brew install node@24
> ```

---

## 3️⃣ Windows 11 (Official Installer)

```powershell
# Step 1: Download the official installer
# Visit https://nodejs.org/en/download and download the v24.18.0 LTS "Windows Installer (.msi)"
# For 64-bit systems, look for node-v24.18.0-x64.msi

# Step 2: Run the downloaded .msi installer
# Double-click the file or run from PowerShell:
Start-Process msiexec.exe -ArgumentList "/I", "node-v24.18.0-x64.msi", "/quiet" -Wait

# Step 3: Verify installation (open a NEW terminal window)
node -v    # Should print v24.18.0
npm -v     # Should print 11.16.0
```

> **Manual installer download link:**
> https://nodejs.org/dist/v24.18.0/node-v24.18.0-x64.msi (64-bit)  
> https://nodejs.org/dist/v24.18.0/node-v24.18.0-arm64.msi (ARM64)

---

## Verification Summary (all platforms)

After installation on any platform, verify with:
```
node -v      → v24.18.0
npm -v       → 11.16.0
npx -v       → 11.16.0
```

---

## Key Decisions

| Item | Detail |
|------|--------|
| **LTS Version** | Node.js v24.18.0 ("Jod") — Current LTS as of July 2026 |
| **npm bundled** | v11.16.0 |
| **Ubuntu method** | Official NodeSource `apt` repository (maintained by NodeSource, the official Linux distributor) |
| **macOS method** | Homebrew (`brew install node` or `brew install node@24`) |
| **Windows method** | Official `.msi` installer from nodejs.org/dist |

Created using VSCode, GitHub Copilot, Ollama, Qwen3.6:35b-a3b-nvfp4, 2026-07-26.
