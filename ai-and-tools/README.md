# AI and Tools

This directory contains resources and tools for developing AI applications. It includes code samples, libraries, and documentation to help you get started with AI development.
ß
## Contents

- [AI Development Environment](../docs/setup/README.md) - Instructions and setup for creating an AI development environment.
- [Tools](#tools)
  - [MarkItDown](#markitdown) Markdown file editing
- [Software Requirements](../docs/setup/software/README.md) - List of required software and tools for AI development.

## Tools

### MarkItDown

MarkItDown is a Microsoft tool designed to simplify the creation and editing of markdown files. It provides an intuitive interface, supports live preview, and integrates with popular development environments to streamline documentation workflows.

See also [MarkItDown Home Page](https://github.com/microsoft/markitdown)

#### MarkItDown MCP Server

The MarkItDown MCP Server is a backend service that enables collaborative editing of markdown documents. It handles user sessions, manages document storage, and offers APIs for real-time synchronization and integration with MarkItDown AI agents.

See also [MarkItDown MCP Server](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)

If you want to start the MCP server locally use `./markitdown.sh` on Linux and Mac or `markitdown.ps1` on Windows. Before running the script check if your environment meets the **[software requirements](software/README.md)**.
