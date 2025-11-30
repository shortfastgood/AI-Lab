# AI-Lab

## Table of contents

- [AI-Lab](#ai-lab)
  - [Table of contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Technology adoption risks](#technology-adoption-risks)
  - [Experiences and outcomes of artificial intelligence adoption](#experiences-and-outcomes-of-artificial-intelligence-adoption)
    - [AI-assisted architecture](#ai-assisted-architecture)
      - [Ai-assisted reseach](#ai-assisted-reseach)
      - [Replatforming](#replatforming)
    - [AI-assisted development](#ai-assisted-development)
      - [AI in the Java ecosystem](#ai-in-the-java-ecosystem)
      - [AI in the Python ecosystem](#ai-in-the-python-ecosystem)
      - [AI in the JavaScript ecosystem](#ai-in-the-javascript-ecosystem)
  - [AI and tools setup](#ai-and-tools-setup)
  - [Prompt engineering](#prompt-engineering)
  - [Context engineering](#context-engineering)

## Introduction

This project began in 2023, the year conversational AI entered mainstream consciousness. Chat-based interfaces, with ChatGPT at the fore, altered how people interact with artificial intelligence. What began as curiosity about conversational capabilities has become a sustained examination of AI-augmented development workflows and their practical potential.

Originally, this repository collected experiences with GitHub Copilot and OpenAI's ChatGPT. These tools formed the first wave of AI integration into daily workflows, providing code suggestions and conversational assistance that noticeably improved productivity. As the technology matured, attention shifted from single-turn chat interactions to more capable autonomous agents and advanced language models able to reason and execute multi-step tasks.

In this context, an agent is an autonomous system that perceives its environment, makes decisions and acts to achieve defined goals. Unlike a one-off chat response, agents preserve state across interactions, plan complex activities, and can utilise tools and APIs to complete work with limited human intervention. They break problems into manageable subtasks, iterate on solutions and—when appropriately designed—collaborate with other agents. This represents a transition from reactive assistance to proactive collaboration.

The move from chat-centric systems to intelligent agents mirrors AI's broader shift from impressive demonstrations to production-capable tools. Where early ChatGPT use was largely conversational, modern agents can generate code, debug applications, manage infrastructure, conduct research and co-ordinate other systems to resolve complex problems. This evolution affects not only individual productivity but also organisational approaches to software engineering and operations.

Through 2023 and into 2024 the exploratory phase expanded to include local language-model deployment for scenarios that cannot rely on cloud-hosted data. Initially such experiments were resource intensive, constrained by hardware and model size. The release of capable models such as DeepSeek‑R1 (14b and 32b variants) showed that substantial LLM capabilities can run on standard laptops, albeit with slower turnaround than cloud services.

These advances have implications for how digital work is organised. The shift from keyboard-centric development to natural-language-driven interactions is more than a tooling change: it redefines human–computer collaboration. Developers are increasingly moving beyond IDE constraints to more interactive, creative relationships with intelligent systems.

This repository serves both as a historical record of that transition and as a practical guide for teams adopting AI-augmented workflows. It explores benefits, challenges, and strategic considerations, while providing examples and pragmatic guidance for integrating AI agents into development processes.

The question is no longer whether AI will transform software development, but how rapidly organisations can adapt to exploit these capabilities while managing associated risks. This repository documents that ongoing transformation.

## Technology adoption risks

AI offers significant advantages but introduces new risks that require careful management. These threats differ from traditional cybersecurity concerns and demand updated controls and awareness.

**Prompt injection** is a critical vulnerability in which adversaries embed instructions within seemingly benign inputs to manipulate AI behaviour. For instance, a document submitted for analysis may contain hidden directives instructing a model to ignore safety constraints or to exfiltrate sensitive data.

**Jailbreaking** denotes techniques that bypass model safety mechanisms. Attackers employ psychological manipulation or technical prompts to elicit disallowed outputs, reveal proprietary information or cause models to act outside their intended remit.

Other risks include data poisoning (where training or fine-tuning data is corrupted to influence model behaviour) and model extraction (where proprietary capabilities are probed and replicated). Organisations must also contend with hallucinations—plausible but incorrect outputs—privacy breaches and operational dependencies on brittle models.

The [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) is a valuable reference for mitigations. For security-sensitive use‑cases, hosting models locally in protected environments is increasingly viable and can reduce exposure to data-leakage risks while preserving capability.

## Experiences and outcomes of artificial intelligence adoption

Adopting AI within AI‑Lab has produced practical results. Integrating tools such as Copilot and ChatGPT improved productivity, simplified coding tasks and helped resolve complex problems. The team experimented with various AI-driven workflows, automating repetitive work, improving code quality and accelerating delivery cycles. These experiments demonstrate how AI can be a productive collaborator, supporting routine tasks and enabling more creative engineering work.

### AI-assisted architecture

AI tools help architects evaluate design alternatives, generate diagrams and analyse requirements more rapidly. Automating repetitive modelling tasks and surfacing risks earlier contributes to more robust, scalable and maintainable systems.

#### Ai-assisted reseach

This section was called reverse engineering in earlier versions. The term research better captures the broader goal of understanding existing systems to inform future development.

When a project lacks adequate documentation, reverse engineering is essential for understanding structure and behaviour. Techniques include static analysis, runtime inspection and automated tooling to reconstruct architecture diagrams and dependency graphs. Systematic decomposition reveals hidden dependencies and clarifies ambiguous logic, producing documentation that supports maintenance and future work.

Continue **[here](docs/architecture/research/README.md)**

#### Replatforming

Replatforming migrates legacy systems to modern platforms while preserving core behaviour. Using artefacts from reverse engineering—dependency maps and architectural diagrams—teams can map legacy components to contemporary equivalents, refactor code for new frameworks and automate data migration. This approach reduces disruption, mitigates technical debt and enables adoption of scalable solutions.

### AI-assisted development

AI-assisted development changes how code is written, reviewed and maintained. Machine learning models can generate code, suggest tests and highlight defects, which shortens development cycles and improves code quality. Offloading routine coding tasks allows developers to focus on higher-level design and problem-solving.

See [AI-Assisted Development Section](ai-and-tools/README.md) for further detail.

#### AI in the Java ecosystem

AI features in IDEs such as IntelliJ IDEA and Eclipse provide predictive code completion and contextual suggestions that increase developer throughput. AI-driven test-generation tools can improve coverage and reduce manual effort.

#### AI in the Python ecosystem

Python benefits from AI integration across data science and web development. Jupyter environments and ML libraries (TensorFlow, PyTorch) increasingly incorporate assistant features that speed experimentation and visualisation. AI-based code review tools help maintain consistency across projects.

#### AI in the JavaScript ecosystem

JavaScript tooling—particularly in Visual Studio Code—leverages AI to offer completion, refactoring and error-detection features. Frameworks such as TensorFlow.js enable in‑browser ML and streamline development of interactive experiences.

## AI and tools setup

Setting up AI tools requires careful consideration of the environment and project constraints. Choose models appropriate to the task, integrate them with development tools and configure access and deployment processes. Setup may involve installing IDE plugins, configuring cloud APIs or deploying local models. A considered setup maximises effectiveness while managing cost and risk.


## Prompt engineering

Prompt engineering has emerged as a recognised discipline that exploits LLMs' ability to interpret natural language and map requests to appropriate outputs. A robust introduction is provided by the [Prompt Engineering Guide](https://www.promptingguide.ai/), which is useful for practitioners who wish to specialise in crafting effective prompts.

See [Prompt Engineering Section](prompts/prompts.md) for examples.

## Context engineering

Prompt engineering is necessary but increasingly insufficient on its own. As models and workflows grow more sophisticated, simply refining prompts reaches diminishing returns—especially for complex, stateful tasks that require reliable, auditable behaviour. To bridge this gap we need a broader discipline: context engineering.

Context engineering treats the environment, data and execution fabric around a model as first‑class artefacts. It encompasses:

- persistent and verifiable context (memory, knowledge bases and provenance); 
- structured orchestration (agents, tool‑use and stepwise plans); 
- input validation and sanitisation (defences against prompt injection and adversarial inputs);
- traceability and audit trails (who/what supplied context and why a decision was made);
- governance and safety controls (policy enforcement, access controls and monitoring).

Context engineering recognises that reliable AI behaviour depends as much on the systems that supply context as on the wording of the prompt itself. In production settings this means engineering pipelines that curate, version and verify context before it reaches a model.

BMAD (Breakthrough Method of Agile AI‑Driven Development) is an example of a context engineering approach. BMAD provides a structured methodology for integrating AI into software development by combining:

- explicit context artefacts (sharded documents, architectural traces, and reproducible evidence),
- agent frameworks (well-defined roles, templates and execution rules),
- deterministic quality gates (traceability, risk assessment and NFR validation), and
- elicitation workflows (controlled human-in-the-loop prompts that avoid ad hoc guessing).

Applied correctly, BMAD shifts effort away from endlessly tuning prompts and toward building resilient context—the repeatable data, processes and artefacts that enable AI agents to act reliably, safely and transparently in real projects.

If you are planning to adopt AI in production, consider investing as much in context engineering as in prompt design. The former provides the scaffolding that makes the latter predictable and auditable.
