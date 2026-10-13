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

## Approaches

### Vibe Coding vs. Adaptation

Thus far, the methodologies proposed can be reduced to two categories: Vibe Coding, or the adaptation of an existing approach. Neither path convinces me. I start from the assumption that software must satisfy a small set of requirements: it must work correctly, it must have the minimum possible number of defects, it must not use resources beyond what is strictly necessary, and it must guarantee reasonable response times even under heavy load. The production cycle must be as simple and efficient as possible.

Starting from a fairly simple prompt and using a frontier model, I obtained an excellent implementation of a vintage game such as Tetris, without a single defect. Repeating the operation with a local model, the first implementation almost always has defects. The modifications or corrections prove difficult for every model, including the frontier ones. To catch an unclosed parenthesis, a large number of tokens and a great deal of time are consumed.

Conversely, the structured approaches—more or less inspired by established methodologies—rapidly produced such a large volume of text that I quickly lost control of it.

### Hypotheses for an alternative path

For the development of a simple program, module or function, the most direct and least expensive route remains vibe coding: a prompt of one, at most two, paragraphs. To succeed requires a certain amount of experience in writing prompts and a reliable model. The kind of results one can obtain are programs such as [Tetris](https://github.com/shortfastgood/one-prompt-apps/blob/main/apps/tetris/TETRIS-APPLICATION.md) or simple scripts to run in a terminal. The risks one runs are excessive cost, if a frontier model is used, and long runtimes if an unsuitable or unreliable local model is used. It is a simple, immediate and effective approach for generating scripts and utilities to use in a terminal or in automation.

Far more often than not, the developer is dealing with existing code that must be modified, improved or extended. The documentation, when it exists, has not been written and organised in an optimal way for use with artificial intelligence. The best results are obtained through a direct analysis of the code. To study the analysis, documentation, modification and reimplementation cycle, I used an already existing game—[PacMan](https://github.com/shortfastgood/one-prompt-apps/blob/main/apps/pac-man/PAC-MAN-APPLICATION.md)—written and generated in Python.

Initially I used a frontier model to generate a prompt containing all the information necessary for a reimplementation in the form of a single file to run in a web browser. With the same model I generated a first version for the web. The game was reproduced faithfully and without errors, but it was unsatisfying from a gameplay standpoint. I therefore made several changes to make it more like the original vintage PC game. The process is the interactive one I have used often over the past three years with frontier models; it leads quite rapidly to the desired result.

With this material, which ideally I should have written by hand, I began testing with local models. Generating PacMan involves giving access to all the existing material, including the reference implementation, but on the condition that the code is generated and not copied. The results obtained are always a complete application, but with defects more or less serious. Not all models are then able to correct the defects they have introduced; the constant is the use of an enormous amount of time and resources, and sometimes the work ends abruptly with a fatal error. I have observed this same syndrome in frontier models too, where it appears more rarely, but when it does the costs can rise dramatically.

As a first correction I split the task into two: a first prompt, specialised in generating the game, specifies that no verification is to be undertaken at the end of coding. The second is specialised in verification and generates the test code. There is an immediate improvement: all models manage to finish the work, yet the time and resources used remain substantial. The benefit is that one has two independent sessions that can be entrusted to different models.

The second correction consists in obliging the model to generate an implementation plan before starting to generate the tests. The plan must be strictly incremental and begin with the definition of the scaffolding and the data necessary to carry out the checks. Then each test is generated, verified and run in isolation until it passes. The model must not move on to the next test until the previous one passes. In this way the model behaves in an orderly, predictable manner, with a more linear use of resources. In the end, although the code is not identical, the various applications are indistinguishable from one another. All the implementations work and have 100% test coverage.