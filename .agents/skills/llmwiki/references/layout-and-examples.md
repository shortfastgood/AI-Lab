# Layout and examples

## Minimal initialization

These are complete initial files; initialization creates no concepts or log.

`docs/index.md` is collection navigation, not an OKF bundle-root index:

```markdown
# Documentation

<!-- llmwiki:start -->
## LLMWiki

Each linked product directory is a separate OKF bundle. Interpret its links from that bundle's root.

* [Library](products/library/index.md) - General knowledge shared across subjects.
<!-- llmwiki:end -->
```

If the file already exists, preserve its content and frontmatter; add this marked section once or update only the existing marked section. Never replace the whole file to regenerate wiki navigation. Inspect preexisting wiki navigation before introducing duplicate links.

`docs/products/library/index.md`:

```markdown
---
okf_version: "0.2"
---
# Library

General knowledge. No concepts have been added yet.
```

For a named product, use the same root-index structure with its display name and scope. Add its collection-index link. Do not create an intermediate product index or empty topic directories unless useful navigation warrants them.

## Example after a product is populated

```text
docs/
  index.md
  products/
    library/
      index.md
    example-pump/
      index.md
      log.md
      operation/
        index.md
        operating-range.md
      references/
        manual.pdf
```

`example-pump/operation/operating-range.md`, with illustrative facts only:

```markdown
---
type: Product Specification
title: Operating temperature range
description: Permitted ambient temperature for the Example Pump.
status: draft
sources:
  - id: operating-manual
    resource: /references/manual.pdf
    title: Example Pump operating manual, section 3
---
# Operating temperature range

The Example Pump operates at ambient temperatures from 5 °C to 35 °C.[^operating-manual]

[^operating-manual]: Operating manual, section 3.
```

Use actual evidence instead of copying these example facts. Add optional generation metadata only with accurate identity and time. Inside this bundle, `/references/manual.pdf` refers to `example-pump/references/manual.pdf`.

The product root index can link to `operation/index.md`. That nested index has no frontmatter and links to `operating-range.md` with its description. A first content-change log might be:

```markdown
# Product Update Log

## 2026-10-21
* **Creation**: Added [operating temperature range](/operation/operating-range.md) from the operating manual.
```

Use the actual change date. Consolidate same-day entries beneath one date heading and keep newer groups first.

## Standalone product delivery

The unit of delivery is `docs/products/<slug>/`, not `docs/`. Library is deliverable by the same procedure.

1. Enumerate only the selected bundle. Check every Markdown concept's frontmatter and reserved index/log structure. Inspect the complete bundle for export, even though routine edits read only relevant concepts.
2. Resolve local links, images, reference-style destinations, and metadata resource paths from their proper bases. Review required code/configuration dependencies if present. Reject escaping symlinks and local paths that rely on the repository, Library, or another product. Do not follow or dereference escaping symlinks into the package.
3. Resolve required missing dependencies by including a permitted, product-scoped local copy with provenance and adjusting references. Check copied material for unrelated product information. If ownership or inclusion is unclear, ask before copying it. Recheck dependencies transitively.
4. Report unresolved optional links and externally hosted resources. A provenance URL need not be mirrored, but the package must contain the knowledge and assets needed for its stated purpose. If an essential dependency cannot be included, report the incomplete delivery rather than declaring it self-contained. OKF conformance and delivery completeness are separate conclusions.
5. Copy or archive only this directory to the requested destination without overwriting an existing delivery. Keep its internal paths unchanged. Do not include the collection index, other bundles, or repository metadata. Do not place the output inside the source bundle. A directory named after the product can be the archive's single top-level directory.
6. Inspect the resulting copy or archive contents and recheck local resolution with that copied directory as the only bundle root. Report the artifact location and remaining external dependencies. Creating an artifact does not authorize sending or publishing it.

An existing nonstandard wiki can still be valid OKF. Preserve its paths during routine maintenance; product separation that requires moving existing concepts is a migration decision to resolve with the user.
