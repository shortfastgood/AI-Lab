# AI and Tools

Setting up AI tools requires careful consideration of the environment and project constraints. This includes selecting models appropriate to the task, integrating them with development tools and configuring access and deployment processes. Setup may involve installing IDE plugins, configuring cloud APIs or deploying local models. A well-considered setup improves effectiveness while keeping cost and risk under control.

## Local vs. Remote

I have decided to prioritise the use of local models and to keep the use of models from online providers to the bare minimum.
Independence and discretion must take priority; speed and completeness of the result matter only if the work done locally is severely limited or of poor quality.

- [Engines](#engines)
- [Scripts](#scripts)
  - [Environment](#environment)
- [Tools](#tools)
  - [ComfyUI](../tools/comfyui.md)
  - [Mark It Down](#markitdown)
  - [MLXGen](../tools/mlxgen.md)
  - [NodeJS](#nodejs)
  - [Python](#python)

## Engines

### Ollama

[Ollama](https://ollama.com) is my first choice, already integrated in Claude Code, Codex and GitHub Copilot. Good overall performance. Large choice of local models. Based on Llama.cpp and MLX framework. [Open source available on GitHub](https://github.com/ollama/ollama), is backed up by a commercial organization with the same name. Solid contributors community, is also present on Discord. 

### oMLX

[oMLX](https://omlx.ai) is a good alternative to Ollama, good overall performance, large choice of models and based on the MLX framework. Additional good WEB interface for administration, statistics and monitoring. [Open Source available on GitHub](https://github.com/jundot/omlx). Solid contributors community.

### Slotstream

Slotstream has an interesting approach that uses the disk as memory extension. It is tailored for the model Qwen3.8-Flash-Next. Allows the run of oversized models maintaining a generation performance sligtly over 20 tok/s, enough for local development. Slotstream is a native implementation based on Apple's MLX and Metal. Is Ollama, OpenAI and Anthropic compatible. I use Slotstream as alternative to Ollama for comparisons. [Open Source available on GitHub](https://github.com/carloslfu/slotstream).

### Splash



## Scripts

Scripts are used primarily during development to implement repetitive processes, individual functions, or tests.

### Environment

| Name       | OS            | Intepreter  | Description |
|------------|---------------|-------------|-------------|
| comfyui.sh | Linux & macOS | Bash.       | Starts ComfyUI server in a dedicated environment |
| instmlx.sh | macOS         | Bash        | Installs the Python virtual environment for MLX scripts      |
| instpy.ps1 | Windows       | Powershell  | Installs the Python virtual environment for portable scripts |
| instpy.sh  | Linux & macOS | Bash        | Installs the Python virtual environment for portable scripts | 

## Tools

### MarkItDown

MarkItDown is a Microsoft tool designed to simplify the creation and editing of markdown files. It provides an intuitive interface, supports live preview, and integrates with popular development environments to streamline documentation workflows.

See also [MarkItDown Home Page](https://github.com/microsoft/markitdown)

### NodeJS

Use the following prompt to build an installation plan for your environment:

"*Show me a step by step how-to to install the last LTS version of nodejs on Linux (Ubuntu), macOS (using brew) and Windows 11 (official package). No alternative methods. Search on internet for actualized informations.*"

Example [Installation How-To](../../ai-and-tools/plan-nodejs-install-guide.md)

### Python

"*Show me a step by step how-to to install the last stable version of python 3 on Linux (Ubuntu), macOS (using brew) and Windows 11 (official package). No alternative methods. Search on internet for actualized informations.*"

Example [Installation How-To](../../ai-and-tools/plan-install-python3-guide.md)
