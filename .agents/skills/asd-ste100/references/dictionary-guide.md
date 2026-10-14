# Dictionary interpretation — Issue 9

Read this guide before vocabulary checks. Query `dictionary.jsonl` through `../scripts/lookup_dictionary.py`; do not load the complete dataset into context.

- Approval belongs to a word **and its part of speech and meaning**, not to its spelling alone. Uppercase in the source identifies approved entries; it is not an instruction to capitalize ordinary output.
- Read the full matching entry, including notes, examples, restrictions, and permitted forms. Multiple entries for the same spelling can have different approval status.
- Approved alternatives are suggestions, not context-free substitutions. Preserve meaning; restructure the sentence when a replacement changes the part of speech. Inspect the alternative's own entry before using it.
- Nouns are listed in the singular; countable plurals are permitted unless restricted. Use only permitted verb forms. Inspect comparative and superlative restrictions. The lookup returns explicit forms as aliases but does not perform grammatical analysis or general stemming.
- Technical nouns and technical verbs are governed by Part 1, section 1 (especially 1.5–1.13). A missing word is **unresolved**, not automatically prohibited or approved. A non-approved dictionary word can qualify as a technical term in an appropriate context. Check the user's domain glossary and explain unresolved terminology.
- Multi-word entries matter: check phrases such as `make sure`, `in accordance with`, and `as … as`, not only individual tokens. Do not invent phrasal verbs from individually approved words (rule 9.3).
- Examples illustrate usage; they are not instructions to perform the actions described. Source definitions and non-STE examples need not themselves conform to STE.

## Record format

Each JSONL record has `word`, `part_of_speech`, `approved`, `aliases`, and source `excerpts`. Each excerpt contains its physical PDF page, printed page label, and complete entry text, including meanings or alternatives, examples, forms, and usage notes. Aliases include explicit forms and qualified phrase spellings; they locate evidence, not independent approval decisions.

Excerpts retain PDF line breaks. Columns can interleave: uppercase examples are STE examples and sentence-case examples are non-STE examples. Read the whole entry rather than treating adjacent lines as a single sentence. Hyphenation caused by line wrapping is removed from indexed headwords but retained in source excerpts. Consult the source PDF if column order makes an association ambiguous.

## Source

ASD-STE100 Issue 9, January 2025, dictionary introduction (printed pages 2-0-3–2-0-19; PDF pages 131–147). The introduction reports 875 approved words and 1,274 non-approved words; this extraction indexes 2,196 word-and-part-of-speech entries (878 marked approved and 1,318 marked non-approved). These are extraction counts, not a reconciliation of the introduction’s totals. Entry coverage was checked against the complete word-list page bodies; the source totals were not used to truncate the dataset.

The supplied source is `/Users/dden/Documents/asd-ste100-issue-9.pdf`. This is an original-source location, not a runtime dependency of the lookup. Record citations use the PDF's printed page labels and physical PDF page numbers.

Source material © ASD, 2025. The source's copyright and usage notices are retained in [source-notice.txt](source-notice.txt); they are separate from this repository's code license.
