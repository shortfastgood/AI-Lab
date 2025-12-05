---
description: Generate a prompt for pyenv installation and setup for Linux and macOS.
agent: dev
model: Grok Code Fast 1
tools: ['runCommands', 'runTasks', 'edit/createFile', 'edit/createDirectory', 'edit/editFiles', 'search', 'todos', 'problems', 'fetch']
---
1. Create or update the Linux and macOS compatible script instpy.sh to install ai-development/ai-python/.venv. 
2. The script assumes python or python3 is already available on the system. Simply try to use python3 first, then fallback to python.
3. The script should check the installed Python version and ensure it is at least 3.12. If not, the script should exit with an informative message.
4. The script should be idempotent, meaning it can be run multiple times without causing issues.
5. The script checks if the folder ai-development/ai-python/.venv exists. If not, it creates a virtual environment there using Python 3.12+.
6. The script activates the virtual environment and installs the packages listed in ai-development/ai-python/requirements.txt.
7. The script upgrades pip to the latest version.
8. Ensure the script includes error handling and informative output messages to guide the user through the installation and setup process.
9. .venv/activate cannot be executed directly, must be executed using bash source command. Ensure the script handles this correctly.
10. At the end the script should activate the virtual environment.
11. Save the script in the root directory of the repository.
12. Execute the script to verify its functionality.