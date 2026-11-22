# Bundled sources

The validator runs with Python 3.9+ and its standard library. No pip packages,
compiled extensions, network access, or package installation are required.
The YAML parser is bundled third-party code, not a new YAML implementation.

- `../validate.py` is adapted from the OKF validator at commit
  [`c4df7bab129884a19673c7098dd8a5c55bf06c86`](https://github.com/open-knowledge-format/open-knowledge-format/blob/c4df7bab129884a19673c7098dd8a5c55bf06c86/skills/okf-generate/scripts/validate.py).
  Copyright 2026 Google LLC; Apache 2.0, reproduced in `../LICENSE.okf`.
  Local changes use the bundled parser, resolve scalars using YAML 1.2 core
  rules, preserve the trailing newline in multiline scalars, report malformed
  YAML without constructor tracebacks, and guard root-index reads and path
  resolution against escaping symlinks.
- `pyyaml/` contains eleven unchanged pure-Python loading modules from
  [PyYAML 6.0.3](https://github.com/yaml/pyyaml/tree/6.0.3/lib/yaml): `composer`,
  `constructor`, `error`, `events`, `loader`, `nodes`, `parser`, `reader`,
  `resolver`, `scanner`, and `tokens`. Copyright Ingy döt Net and Kirill
  Simonov; MIT license reproduced in `pyyaml/LICENSE`. Its local `__init__.py`
  exposes only the loading interface needed by the validator. Dumping,
  serialization, and C-extension modules are not included.

Keep the bundled files and licenses together when copying the validator.
Update vendored sources deliberately against their pinned upstream versions,
then run `python3 -S -B -m unittest discover -s scripts/tests -v` from the
skill directory. Do not load these modules as skill instructions.
