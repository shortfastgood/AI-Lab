# OKF authoring rules

Implementation guidance for [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), inspected 2026-10-21. The upstream specification is in Google's knowledge-catalog repository, distributed under [Apache 2.0](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/LICENSE.md). These notes describe the format; the product directory arrangement is a local convention.

Consult the linked specification for details not covered here. Do not silently upgrade an existing bundle's declared version when the upstream specification changes.

## Documents and navigation

- Every `.md` file inside a bundle is a concept except `index.md` and `log.md`, reserved at every directory level. This includes Markdown in `references/`; an imported Markdown source needs valid concept frontmatter, or must be retained as a non-Markdown asset with a separate concept describing it.
- Concepts require parseable YAML frontmatter with a nonempty `type`. Choose a descriptive string; the vocabulary is open. Unknown types and extra metadata are allowed and must survive edits. No universal body headings are required.
- Useful optional fields are `title`, `description`, `tags`, and `resource`. The last identifies the described asset; it is not automatically the provenance of every claim. Avoid adding empty optional fields.
- Index files have no frontmatter, except a bundle-root index may declare `okf_version: "0.2"`. Use heading sections and Markdown links with short descriptions. Nested indices do not get version frontmatter.
- Logs use newest-first date groups headed with `YYYY-MM-DD` and prose entries describing changes. Logs and indices are optional under OKF; this skill maintains them for discovery and history.
- Concept IDs are paths from the bundle root without `.md`. Renaming therefore changes identity.

## Sources, trust, and freshness

Use `sources` as a list. Each entry requires `resource`; give it a stable `id` when a claim needs attribution. Optional details include `title`, `author`, `last_modified`, and observed `usage_count`. A source resource may identify a URL, a local resource, or a population/scope description; do not interpret every descriptive value as a missing file.

Attribute sourced claims with Markdown footnotes whose labels match `sources[].id`. Provide the corresponding footnote definition. Keep IDs stable when sorting or editing the source list. Express derivation through links to other concepts rather than inventing a standard `derived_from` field.

If reporting usage counts, include the actual observation period in `usage_window: {from: ..., to: ...}` at concept level or as a source-specific override. Do not infer credibility scores from counts.

`generated` records production, with required `by` when the mapping is present and `at` for the last meaningful content change. Use an actual known producer/version, or the responsible process identity; omit optional metadata rather than inventing a model version.

`verified` records confirmation against evidence, usually as a list of `{by, at}` events. A single mapping is also valid. Structural validation is not factual verification. Never mark an entry human-reviewed merely because a human requested its creation. Preserve older verification events but explain when a later edit has not been reconfirmed.

Actors use `human:<identity>` for people, `process:<identity>` for processes, and `<producer>/<version>` for agents/tools. Verification determines advisory trust: absent verification is unverified; nonhuman events are machine confirmation; a human event records human review. Missing trust metadata does not invalidate a concept.

`status` may be `draft`, `stable`, or `deprecated`; omission means stable. `stale_after` is an absolute instant, not a duration. All timestamp-valued fields use ISO 8601 datetimes with an explicit UTC offset, for example `2026-10-21T10:00:00Z`. A stale concept should be surfaced for review, not automatically deleted.

## Links and dependency boundaries

A Markdown destination beginning with `/` resolves from the current bundle root, not from `docs/` or the filesystem root. Relative links resolve from the containing document. Use bundle-root links for stable internal concept references; relative links are also supported. Apply the same distinction to path-valued metadata: `resource`, `sources[].resource`, `computation`, `executor.resource`, and `attester.resource`. Absolute URIs can remain external.

Check destinations after normalizing `..`, URL escapes, and symlinks. A path that escapes the bundle is a product-isolation issue even if it resolves on the author's machine. Include images, attachments, code dependencies, reference-style Markdown links, and metadata paths in the review, not just inline links.

Broken links are permitted by OKF. Report them as missing knowledge or delivery dependencies, not as a blanket format error. Likewise, absent optional metadata or indices and unfamiliar types or fields are not grounds to reject an existing bundle.

## Attested Computation — read when this type occurs

Use a separate `type: Attested Computation` concept with required `runtime`. A `parameters` list describes entries with `name`, `type`, and `required`. Other concepts link to it normally.

The sanctioned computation is either one fenced code block beneath `# Computation`, or a file named by `computation`; do not maintain competing inline and file definitions. `executor.resource` identifies execution instructions/code and `executor.receipt` declares the returned evidence fields. `attester.resource` identifies deterministic verification code, not an LLM judgment.

Ingestion preserves the supplied sanctioned computation. Do not invent, rewrite, or execute it while maintaining knowledge. A consumer supplies declared parameter values rather than changing the computation. Runtime receipts and attestation verdicts are not stored as bundle knowledge. Document-level `verified` events and per-run attestation are separate.

Consult specification section 10 before creating or changing a computation contract; maintaining a wiki alone does not authorize executing its executor or attester.
