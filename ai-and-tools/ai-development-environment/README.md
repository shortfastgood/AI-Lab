# AI Development Environment

The tool by itself is of limited use and often causes significant frustration. The architect, developer, and DevOps operator must build the environment and ensure the AI always stays on the defined path.

## Visual Studio Code and GitHub Copilot - August 2025 (version 1.104)

[Visual Studio Code](https://code.visualstudio.com/Download) is available from Microsoft for Linux, macOS, and Windows at no licensing cost. However, it is recommended to use a GitHub Copilot Pro license for development.

### Where and how to set base instructions

This guidance explains how to split and store the repository’s base instructions so Copilot and other assistants get consistent, maintainable direction.

#### Purpose
- Use a single concise global file for repository-wide rules and an `instructions/` folder for modular, scoped rules (languages, components, directories, or workflows).

#### copilot-instruction.md (single global file)
- Location: repository root (e.g., `/copilot-instruction.md`) or a central folder such as `/.github/` or `/.copilot/`.
- Role: provide high-level, always-applicable rules: project purpose, persona, tone, security constraints, license, and coding standards that apply everywhere.
- Content suggestions: one-line persona, prohibited behaviors (no leaking secrets, no changes to infra without approval), preferred style (naming, tests, comments), and where to find more specific rules.
- Format: plain Markdown; keep it short (preferably < 200–400 words) and explicit.

#### instructions/ folder (scoped, modular rules)
- Location: near repo root, e.g., `/instructions/`, `/.github/instructions/`, or `/.copilot/instructions/`.
- Role: hold per-language, per-package, or per-directory instruction files that extend or override the global file for specific contexts.
- Structure: one file per scope, named clearly (e.g., `python.md`, `frontend-react.md`, `security.md`, `docs-style.md`).
- Contents: concrete rules, examples, do/ don’t code snippets, linting or build commands, and any directory-specific expectations.
- Scope resolution: treat files in the nearest directory to the target code as more specific; use these to override or refine global rules.

#### Priority and maintenance
- Recommended precedence: nearest/specific instruction file > scoped files in `instructions/` > `copilot-instruction.md` (global).
- Keep instructions under version control and update via normal PR review.
- Review cadence: update instructions when coding standards, security policies, or CI requirements change.

#### Best practices
- Keep rules actionable and example-driven.
- Prefer short, declarative sentences and section headers: Persona, Constraints, Style, Examples.
- Avoid secrets and environment specifics in these files; link to secure docs for sensitive details.
- Add a short README inside `instructions/` explaining naming conventions and precedence.

By following this split, the global file gives consistent project-wide behavior while the folder enables precise, maintainable, and localized instruction sets.

## Managing and using prompts in .github/prompts

Purpose
- Centralize reusable prompt templates that drive Copilot, assistants, or automation workflows.
- Keep prompts discoverable, versioned, and reviewable via normal PRs.
- Folder .github/prompts/

File format and metadata
- Use a small YAML front matter at the top of each file, followed by the prompt text.
- Recommended metadata:
    - **description**: Short description of the prompt
    - **mode**: ask | edit | agent
    - **model**: Language model used when running the prompt. If not specified, the currently selected model in model picker is used.
    - **tools**:  Array of tool (set) names that can be used. Select Configure Tools to select the tools from the list of available tools in your workspace. If a given tool (set) is not available when running the prompt, it is ignored.

- Suggested prefixes:
    - **00_**: Environment set up
    - **01_**: Analysis
    - **70_**: Reverse Engineering
    - **80_**: Interactive Tests
    - **99_**: Examples

## Interactive WEB Testing

Microsoft provides an MCP server to drive Playwright via artificial intelligence. To install it click on the first icon to the right (Configure Tools ...) in the chat input section. In the title bar of the Configure Tools dialog click on the second icon from left at the right of the title.