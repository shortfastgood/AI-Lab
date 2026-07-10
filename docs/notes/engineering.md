# Engineering

Alongside conventional software engineering, the rise of artificial intelligence (AI) has given rise to new engineering disciplines that move software production to a higher logical level, one that is closer to the way people naturally think and reason.


## Prompt engineering

Prompt engineering has emerged as a recognised discipline that exploits LLMs' ability to interpret natural language and map requests to appropriate outputs. A robust introduction is provided by the [Prompt Engineering Guide](https://www.promptingguide.ai/), which is useful for practitioners who wish to specialise in crafting effective prompts.

## Context engineering

Prompt engineering is necessary but increasingly insufficient on its own. As models and workflows grow more sophisticated, simply refining prompts reaches diminishing returns, especially for complex, stateful tasks that require reliable, auditable behaviour. Addressing this gap requires a broader discipline: context engineering.

Context engineering treats the environment, data and execution fabric around a model as first‑class artefacts. It encompasses:

- persistent and verifiable context (memory, knowledge bases and provenance);
- structured orchestration (agents, tool‑use and stepwise plans);
- input validation and sanitisation (defences against prompt injection and adversarial inputs);
- traceability and audit trails (who/what supplied context and why a decision was made);
- governance and safety controls (policy enforcement, access controls and monitoring).

Context engineering recognises that reliable AI behaviour depends as much on the systems that supply context as on the wording of the prompt itself. In production settings this means engineering pipelines that curate, version and verify context before it reaches a model.

### BMAD

BMAD (Breakthrough Method of Agile AI‑Driven Development) is an example of a context engineering approach. BMAD provides a structured methodology for integrating AI into software development by combining:

- explicit context artefacts (sharded documents, architectural traces and reproducible evidence),
- agent frameworks (well-defined roles, templates and execution rules),
- deterministic quality gates (traceability, risk assessment and NFR validation), and
- elicitation workflows (controlled human-in-the-loop prompts that avoid ad hoc guessing).

Applied correctly, BMAD shifts effort away from endlessly tuning prompts and toward building resilient context—the repeatable data, processes and artefacts that enable AI agents to act reliably, safely and transparently in real projects.

Production adoption of AI calls for as much investment in context engineering as in prompt design. The former provides the scaffolding that makes the latter predictable and auditable.
