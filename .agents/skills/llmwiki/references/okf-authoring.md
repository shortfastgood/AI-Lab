# OKF authoring rules

Implementation guidance for [Open Knowledge Format v0.3](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md), inspected 2026-11-22. The canonical repository is `open-knowledge-format/open-knowledge-format`, distributed under [Apache 2.0](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/LICENSE.md). These notes describe the format; the product directory arrangement is a local convention.

Consult the linked specification for details not covered here. Do not silently upgrade an existing bundle's declared version when the upstream specification changes.

## Documents and navigation

- A non-reserved `.md` file with frontmatter containing a nonempty string `type` is a concept. Markdown without frontmatter or without `type` is ordinary documentation, including imported sources, `README.md`, and `AGENTS.md`; exclude it from concept discovery and report it as a warning, not a conformance failure. It may still supply source evidence. Never add `type` merely to silence that warning. `index.md` and `log.md` are reserved at every level and never concepts.
- Non-`.md` files are assets. Dot-prefixed files and directories are outside the bundle. Do not follow symlinks outside its root.
- Frontmatter starts on the first line with exactly `---`, ends at the next exact `---` line, and parses as a YAML 1.2 core-schema mapping. Do not write duplicate keys or custom YAML tags. Quote timestamps and values that resemble numbers or booleans. Preserve unchanged values without re-serializing them where possible. Any frontmatter in ordinary Markdown must also parse as a mapping.
- Choose a descriptive `type`; the vocabulary is open. Preserve unknown keys at every nesting level. Prefer `x-<producer>-<name>` for new custom keys; the `x-` prefix is reserved for extensions. Use CommonMark with GFM tables and footnotes; no universal body headings are required.
- Useful optional fields are `title`, `description`, `tags`, and `resource`. The last identifies the described asset; it is not automatically the provenance of every claim. Avoid adding empty optional fields.
- Index files below the bundle root have no frontmatter. A root index may contain `okf_version: "0.3"`, `title`, `description`, `license`, and extension keys. Preserve its existing frontmatter when regenerating navigation. Bundle metadata does not apply to individual concepts. Use heading sections and Markdown links with short descriptions.
- Logs have no frontmatter. Use newest-first date groups headed with `YYYY-MM-DD` and prose entries describing changes. Logs and indices are optional under OKF; this skill maintains them for discovery and history.
- Concept IDs are paths from the bundle root without `.md`. Renaming therefore changes identity.

## Sources, trust, and freshness

Use `sources` as a list. Each entry requires `resource`; give it a stable `id` when a claim needs attribution. Optional details include `title`, `author`, `last_modified`, and observed `usage_count`. A source resource may identify a URL, a local resource, or a population/scope description; do not interpret every descriptive value as a missing file.

Attribute sourced claims with Markdown footnotes whose labels match `sources[].id`. Provide the corresponding footnote definition. Keep IDs stable when sorting or editing the source list. Express derivation through links to other concepts rather than inventing a standard `derived_from` field.

If reporting usage counts, include the actual observation period in `usage_window: {from: ..., to: ...}` at concept level or as a source-specific override. Do not infer credibility scores from counts.

`generated` records production, with required `by` when the mapping is present and `at` for the last meaningful content change. Formatting, whitespace, and link repairs do not advance `generated.at`. Use an actual known producer/version, or the responsible process identity; omit optional metadata rather than inventing a model version.

`verified` records confirmation against evidence as a list of `{by, at}` events; both keys are required in an event. A single mapping is also valid. Ignore incomplete events and report them. Structural validation is not factual verification. Never mark an entry human-reviewed merely because a human requested its creation.

Only current verification events establish trust: `verified.at >= generated.at`, or `generated` is absent. Keep earlier events as history and report when an edit lowers the trust tier. If malformed metadata prevents the comparison, report the uncertainty rather than asserting current verification. No current events means unverified; current nonhuman events mean machine-confirmed; a current `human:` event means human-reviewed. Missing trust metadata does not invalidate a concept.

Actors use `<producer>/<version>` for agents/tools and `<scheme>:<identity>` for other actors, including `human:`, `team:`, and `process:`. Accept other schemes as nonhuman. Only `human:` can establish human-reviewed trust; `team:` does not identify an individual reviewer. This convention also applies to `sources[].author`.

`status` may be `draft`, `stable`, or `deprecated`; omission means stable. Preserve unknown status values, report them, and exclude them from filters to current knowledge. Use `superseded_by` only with `status: deprecated`, pointing to the replacement concept. On a rename, keep a short deprecated concept at the old path with this field; a move alone does not change the moved content's generation or verification metadata.

Timestamp fields accept RFC 3339 datetimes with an offset or dates (`"2026-11-22"` means midnight UTC). Accept quoted strings and YAML-native timestamp values. Prefer quoted datetimes for `generated.at` and `verified[].at`. A datetime without an offset is invalid; do not guess its time zone.

Only `stale_after` determines freshness: stale when `now >= stale_after`. It is an absolute instant, not a duration. Omit it when no review date is known. A nonempty value that cannot be parsed must never count as fresh; report it as malformed. Stale means review is needed, not that the content is false or should be deleted.

When reading optional fields, treat nulls, empty strings, and empty lists as absent. Accept one item where a list is expected (`tags`, `sources`, `verified`, `parameters`); a scalar tag containing commas is one tag, not several. Ignore incomplete family entries and warn without rejecting the bundle. Prefer explicit lists when authoring.

## Links and dependency boundaries

A Markdown destination beginning with `/` resolves from the current bundle root, not from `docs/` or the filesystem root. Other local links resolve from the containing document's directory. Apply the same rules to path-valued metadata: `resource`, `sources[].resource`, `computation`, `executor.resource`, `attester.resource`, and `superseded_by`; a path-valued bundle `license` follows these rules too. Absolute URIs can remain external.

Prefer relative body links for GitHub rendering and `/`-rooted metadata paths for clarity. These are authoring preferences, not conformance requirements; preserve working existing links. Percent-encode spaces and reserved characters in URI paths. Paths are case-sensitive; avoid names differing only by case. Standard inline and reference-style links are supported; `[[wikilinks]]` are not OKF links. Path fields resolving to concepts also form graph edges.

Check destinations after normalizing `..`, URL escapes, and symlinks. Do not read local targets outside the bundle; they also prevent standalone product delivery. Include images, attachments, code dependencies, reference-style Markdown links, and metadata paths in the review, not just inline links. Separate `#fragments` when resolving file targets.

Broken links are permitted by OKF. Report them as missing knowledge or delivery dependencies, not as a blanket format error. Likewise, absent optional metadata or indices and unfamiliar types or fields are not grounds to reject an existing bundle.

## Attested Computation — read when this type occurs

Use a separate `type: Attested Computation` concept with required `runtime`. A `parameters` list describes entries with required `name` and `type`; optional `required` defaults to `false`. Other concepts link to it normally.

The sanctioned computation is either a file named by `computation`, or the first fenced code block in a section headed `Computation` at any ATX heading level. The section ends at the next heading of the same or a higher level. Prefer exactly one fenced block; do not maintain competing inline and file definitions. When reading, `computation` takes precedence. Missing computation content is not attestable.

`executor.resource` identifies execution instructions/code and `executor.receipt` declares the returned evidence fields. `attester.resource` identifies deterministic verification code, not an LLM judgment. Never label a value attested without `runtime` and `attester`, or without successful run evidence. The informative runtime flow uses a verdict with boolean `ok` and optional `reason`.

Ingestion preserves the supplied sanctioned computation. Do not invent, rewrite, or execute it while maintaining knowledge. A consumer supplies declared parameter values rather than changing the computation. Runtime receipts and attestation verdicts are not stored as bundle knowledge. Document-level `verified` events and per-run attestation are separate.

Consult specification section 10 before creating or changing a computation contract; maintaining a wiki alone does not authorize executing its executor or attester.

## Compatibility and migration

Read the existing bundle's declared version before editing. The rules above target v0.3; do not apply its relaxed concept classification to a bundle retained at v0.2. For v0.2 conformance, every non-reserved `.md` file still needs concept frontmatter. Pre-1.0 minor versions can contain breaking changes. Consult [specification sections 12–13](https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md#12-versioning) for compatibility, and do not silently change a version declaration.

When consuming v0.2, earlier, or unversioned bundles, an unresolved metadata path without a leading `/` may be retried from the bundle root. Do this only after file-relative resolution fails; do not use this fallback for v0.3. For v0.1, legacy `timestamp` and `# Citations` may be read as fallbacks. Preserve them during ordinary edits.

When migration is requested or already authorized:

1. Audit existing path fields before changing the version. Rewrite confirmed bundle-root paths with a leading `/`, preserving their actual targets. Resolve ambiguities rather than guessing.
2. Preserve metadata, verification history, and custom fields. Check YAML syntax, reserved index/log structure, and timestamps; ask only when a required time zone cannot be established. Do not split comma-containing tags without evidence that they mean separate tags.
3. Add `superseded_by` where a deprecated concept has a known replacement. For v0.1, convert `timestamp` to `generated` only with a known producer, and turn supported citations into source entries and matching footnotes without inventing attribution.
4. Set the root index to `okf_version: "0.3"`, with an accurate title and scope description. Retain existing license and extension fields; add a license only when known. Keep the existing bundle boundaries and product assignments.
5. Validate as v0.3 and report unresolved dependencies and any lowered trust tiers. Migration itself is not factual verification.

## Validation

For v0.3, use the bundled [validator](../scripts/validate.py), adapted from the upstream OKF validator. It needs only Python 3.9+ and its standard library: the required pure-Python YAML loading modules are included under `scripts/_vendor/`, with no pip installation or LibYAML requirement. Keep that directory beside the script. See [bundled-source notices](../scripts/_vendor/NOTICE.md) for pinned versions, local changes, and licenses. Do not read vendored parser source as part of routine wiki maintenance.

Run `python3 /path/to/llmwiki/scripts/validate.py /path/to/bundle --json` using the actual skill and bundle paths. Errors indicate conformance failures; warnings include non-concept Markdown and field-shape issues; informational findings include stale content and old verifications. Fix errors and explain retained warnings. `--strict` also fails on warnings, so an intentional ordinary Markdown file can make it fail without invalidating the bundle. Exit codes are 0 for passing checks, 1 for errors (or strict-mode warnings), and 2 for usage/setup errors.

The bundled loader uses YAML 1.2 core scalar resolution and rejects duplicate keys. The checker retains the upstream scope: it is not a complete Markdown parser or export audit. Separately review reference-style links, images, footnote definitions, index navigation, and all delivery dependencies described in [the export checklist](layout-and-examples.md#standalone-product-delivery). Validator success establishes neither factual accuracy nor standalone completeness. If Python is unavailable, check specification §11.1 manually and state that limitation. Do not use the v0.3 checker as proof of v0.2 conformance.
