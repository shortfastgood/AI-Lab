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

### LLM Wiki

An LLM wiki is a concrete realisation of the persistent, verifiable context that context engineering calls for. Where the common RAG approach re-derives an answer from raw documents on every query, accumulating nothing, an LLM wiki is a persistent, compounding artefact: a structured, interlinked collection of markdown files that the LLM maintains incrementally and that sits between the user and the immutable raw sources. Each new source is read, distilled and integrated—updating entity and concept pages, revising summaries, and flagging where new data contradicts an old claim—so that cross-references, contradictions and synthesis are pre-computed once and then kept current, rather than re-derived on every question. The pattern, articulated in an idea file by Karpathy, descends in spirit from Vannevar Bush's *Memex* and stands as the persistent-knowledge counterpart to RAG.

Operationally it comprises three layers—raw sources (the immutable source of truth), the wiki itself (owned and maintained entirely by the LLM) and a schema file (e.g. `CLAUDE.md` for Claude Code or `AGENTS.md` for Codex) that codifies the conventions and workflows—and three recurring workflows: *ingest* (absorb and file a new source, touching many pages at once), *query* (synthesise a cited answer, filing good answers back into the wiki so exploration compounds) and *lint* (health-check for contradictions, superseded claims, orphan pages and missing cross-references). Two navigation aids keep it tractable without embedding-based infrastructure at moderate scale: `index.md`, a content-oriented catalog the LLM consults first, and `log.md`, an append-only chronicle of ingests, queries and lint passes. Its defining property is that the maintenance burden—cross-referencing, bookkeeping, cross-page consistency—which causes humans to abandon wikis, is offloaded to the LLM, for whom the cost of an edit is near zero; graph-based variants extend the pattern to larger, query-focused corpora.

References:

- Karpathy, *A pattern for building personal knowledge bases using LLMs* (idea file): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, arXiv:2005.11401 (2020): https://arxiv.org/abs/2005.11401
- Vannevar Bush, *As We May Think* (1945) and the Memex concept: https://en.wikipedia.org/wiki/Memex
- Edge et al. (Microsoft), *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*, arXiv:2404.16130 (2024): https://arxiv.org/abs/2404.16130

## Approach

Thus far, the methodologies proposed can be reduced to two categories: Vibe Coding, or the adaptation of an existing approach. Neither path convinces me. I start from the assumption that software must satisfy a small set of requirements: it must work correctly, it must have the minimum possible number of defects, it must not use resources beyond what is strictly necessary, and it must guarantee reasonable response times even under heavy load. The production cycle must be as simple and efficient as possible.

Starting from a fairly simple prompt and using a frontier model, I obtained an excellent implementation of a vintage game such as Tetris, without a single defect. Repeating the operation with a local model, the first implementation almost always has defects. The modifications or corrections prove difficult for every model, including the frontier ones. To catch an unclosed parenthesis, a large number of tokens and a great deal of time are consumed.

With the Pac-Man game I began by asking a frontier model to analyse a very simple and partial, yet working, implementation in Python. The model created a prompt that explained how to generate the code for a further implementation. The generated prompt was then modified to add several details that make the game more spectacular and closer to the one of old. The frontier model implements the game as a single file, without dependencies, for a browser, without defects, in at most ten minutes. Local models take between 30 and 90 minutes, and not all of them manage to generate usable code.

To obtain an identical result everywhere, with no defects and code tested to 100% coverage, I had to separate the instructions that generate the code from those that generate the tests. The result is two completely separate prompts. The prompt that generates the verifications is extremely detailed and demands a great deal of the artificial intelligence, but in the end both the code and the verifications are error-free. The execution times differ, and they depend on the engine and the model. The strategy makes it possible to use different models for generating the code and for the verifications; moreover, after each modification, one can first run a check with the existing suite (regression) and then move on to the one that also verifies the changes.

Splitting the two contexts code and test make it possible to better focus on the task to execute, this make also possible to produce instructions that lead to results which are repeatable and independent of the model or of its version. 