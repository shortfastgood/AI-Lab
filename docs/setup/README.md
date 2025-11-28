# AI Development Environment

The tool by itself is of limited use and often causes significant frustration. The architect, developer, and DevOps operator must build the environment and ensure the AI always stays on the defined path.

The methodology used is more important than any tool. Without discipline and a clear vision of requirements and architecture, the project will go off track. The consequences are a loss of trust in the technology and poor practical results. The second priority is a language model suitable for the purpose. Third are the instructions we give to the AI, and only lastly comes the tool itself.

## BMAD Method

I chose the Breakthrough Method of Agile AI-Driven Development because it is well-structured. After four versions, it is mature enough to be used in a real project. It does not require using all its parts and is easily adaptable. BMAD is a good example of context engineering.

The project was developed using Visual Studio Code and GitHub Copilot; therefore, all references—particularly paths—refer to that environment. However, neither the project nor BMAD requires the use of this environment.

### Installation

    invest-ai> npx bmad-method install 

### AI Personas (BMAD Method)

The BMAD Method is a structured approach to AI-assisted development that defines specific personas or "chat modes" to guide GitHub Copilot's behavior in different contexts. This method enhances development productivity by providing role-based AI assistance tailored to specific tasks and responsibilities within the software development lifecycle.

The BMAD core framework is located in the `.bmad-core` directory, while the persona definitions are stored in `.github/chatmodes`. Each persona represents a specialized role with distinct capabilities, knowledge domains, and communication styles.

#### Available Personas

The project includes 10 specialized AI personas defined in [.github/chatmodes/](.github/chatmodes/), each with specific roles and capabilities:

**📊 Mary - Business Analyst** ([analyst.chatmode.md](.github/chatmodes/analyst.chatmode.md))
- **Role**: Insightful Analyst & Strategic Ideation Partner
- **When to Use**: Market research, brainstorming, competitive analysis, creating project briefs, initial project discovery, and documenting existing projects (brownfield)
- **Style**: Analytical, inquisitive, creative, facilitative, objective, data-informed

**🏗️ Winston - Architect** ([architect.chatmode.md](.github/chatmodes/architect.chatmode.md))
- **Role**: Holistic System Architect & Full-Stack Technical Leader
- **When to Use**: System design, architecture documents, technology selection, API design, and infrastructure planning
- **Style**: Comprehensive, pragmatic, user-centric, technically deep yet accessible

**💻 James - Full Stack Developer** ([dev.chatmode.md](.github/chatmodes/dev.chatmode.md))
- **Role**: Expert Senior Software Engineer & Implementation Specialist
- **When to Use**: Code implementation, debugging, refactoring, and development best practices
- **Style**: Implementation-focused with adherence to project development standards

**📋 John - Product Manager** ([pm.chatmode.md](.github/chatmodes/pm.chatmode.md))
- **Role**: Investigative Product Strategist & Market-Savvy PM
- **When to Use**: Creating PRDs, product strategy, feature prioritization, roadmap planning, and stakeholder communication
- **Style**: Analytical, inquisitive, data-driven, user-focused, pragmatic

**📝 Sarah - Product Owner** ([po.chatmode.md](.github/chatmodes/po.chatmode.md))
- **Role**: Technical Product Owner & Process Steward
- **When to Use**: Backlog management, story refinement, acceptance criteria, sprint planning, and prioritization decisions
- **Style**: Meticulous, analytical, detail-oriented, systematic, collaborative

**🧪 Quinn - Test Architect & Quality Advisor** ([qa.chatmode.md](.github/chatmodes/qa.chatmode.md))
- **Role**: Test Architect with Quality Advisory Authority
- **When to Use**: Comprehensive test architecture review, quality gate decisions, and code improvement. Provides thorough analysis including requirements traceability, risk assessment, and test strategy
- **Style**: Advisory only - teams choose their quality bar

**🏃 Bob - Scrum Master** ([sm.chatmode.md](.github/chatmodes/sm.chatmode.md))
- **Role**: Technical Scrum Master - Story Preparation Specialist
- **When to Use**: Story creation, epic management, retrospectives in party-mode, and agile process guidance
- **Style**: Task-oriented, efficient, precise, focused on clear developer handoffs

**🎨 Sally - UX Expert** ([ux-expert.chatmode.md](.github/chatmodes/ux-expert.chatmode.md))
- **Role**: User Experience Designer & UI Specialist
- **When to Use**: UI/UX design, wireframes, prototypes, front-end specifications, and user experience optimization
- **Style**: Empathetic, creative, detail-oriented, user-obsessed, data-informed

**🧙 BMad Master** ([bmad-master.chatmode.md](.github/chatmodes/bmad-master.chatmode.md))
- **Role**: Master Task Executor & BMad Method Expert
- **When to Use**: Comprehensive expertise across all domains, running one-off tasks that do not require a persona, or wanting to use the same agent for many things
- **Style**: Universal executor of all BMad-Method capabilities

**🎭 BMad Orchestrator** ([bmad-orchestrator.chatmode.md](.github/chatmodes/bmad-orchestrator.chatmode.md))
- **Role**: Master Orchestrator & BMad Method Expert
- **When to Use**: Workflow coordination, multi-agent tasks, role switching guidance, and when unsure which specialist to consult
- **Style**: Knowledgeable, guiding, adaptable, efficient, encouraging, technically brilliant yet approachable

Each persona can be activated through their respective chatmode files and provides specialized assistance tailored to their domain expertise and communication style.

## Visual Studio Code and GitHub Copilot - September 2025 (version 1.105)

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

### BMAD Chat Modes

Starting with Visual Studio Code version 1.104, the tools list must use full names (for example, use `search/codebase` instead of `codebase`). BMAD 4.44.1 has not yet been updated; therefore, the update must be performed manually or via a prompt.

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
    - **00_**: Creation (e.g. Environment set up)
    - **02_**: Persistence (e.g. Database, Files)
    - **03_**: Service (Business Logic)
    - **04_**: REST (e.g. API, Controllers)
    - **05_**: SOAP (e.g. API, Controllers)
    - **06_**: WEB Client (e.g. React, Angular)
    - **07_**: Endpoint full implementation (e.g. CRUD)
    - **09_**: Review  (lint, security, performance)
    - **10_**: Analysis
    - **20_**: DevOps (e.g. CI/CD, Infra as Code)
    - **30_**: Documentation (e.g. Markdown, Diagrams)
    - **40_**: Testing (e.g. Unit, Integration, E2E)
    - **50_**: MCP (e.g. Mini-Tower via MCP)
    - **60_**: User Interface / User Experience
    - **70_**: Reverse Engineering
    - **80_**: Interactive Tests
    - **90_**: Context Engineering
    - **99_**: Examples

## Interactive WEB Testing

Microsoft provides an MCP server to drive Playwright via artificial intelligence. To install it click on the first icon to the right (Configure Tools ...) in the chat input section. In the title bar of the Configure Tools dialog click on the second icon from left at the right of the title.