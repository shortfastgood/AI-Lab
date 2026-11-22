"""Run with: python3 -S -B -m unittest discover -s scripts/tests -v."""

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import validate


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.bundle = Path(self.temp.name) / "bundle"
        self.bundle.mkdir()
        self.write("index.md", '---\nokf_version: "0.3"\ntitle: Test\n---\n# Test\n')

    def write(self, path, text):
        dest = self.bundle / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        return dest

    def concept(self, frontmatter, body="", path="concept.md"):
        return self.write(path, "---\n" + frontmatter + "\n---\n" + body)

    def run_validator(self, *args, expected=0):
        env = dict(os.environ, PYTHONPATH="", PYTHONNOUSERSITE="1")
        result = subprocess.run(
            [sys.executable, "-S", "-B", str(SCRIPTS / "validate.py"),
             str(self.bundle), "--json", "--now", "2026-11-22T12:00:00Z", *args],
            cwd=self.temp.name, env=env, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        return json.loads(result.stdout)

    def codes(self, result):
        return {f["code"] for f in result["findings"]}

    def test_runs_without_site_packages_and_does_not_modify_bundle(self):
        self.concept("type: Reference\ndescription: A sample reference.")
        before = {p: p.read_bytes() for p in self.bundle.rglob("*") if p.is_file()}
        result = self.run_validator("--strict")
        self.assertEqual((result["errors"], result["warnings"], result["info"]), (0, 0, 0))
        self.assertEqual(before, {p: p.read_bytes() for p in self.bundle.rglob("*") if p.is_file()})
        self.assertNotIn("yaml", sys.modules)
        self.assertTrue(Path(validate.yaml.__file__).is_relative_to(SCRIPTS))

    def test_nested_flow_block_scalars_unicode_and_aliases(self):
        text = '''---
type: Reference
title: "Quoted: café #1"
description: >-
  First line
  second line
sources:
  - &source {id: manual, resource: "https://example.com/manual"}
x-test-source: *source
x-test-config:
  nested: [one, {two: 2}]
  literal: |
    line one
    line two
---
Claim.[^manual]

[^manual]: Manual.
'''
        self.write("concept.md", text)
        state, meta, _, _ = validate.split_frontmatter(text)
        self.assertEqual(state, "ok")
        self.assertEqual(meta["description"], "First line second line")
        self.assertEqual(meta["x-test-config"]["literal"], "line one\nline two\n")
        self.assertEqual(meta["sources"][0], meta["x-test-source"])
        self.assertEqual(self.run_validator("--strict")["warnings"], 0)

    def test_yaml_12_core_scalars(self):
        state, meta, _, _ = validate.split_frontmatter('''---
type: Reference
x-test: [yes, no, on, off, 012, 0o12, 0x10, 1e3, true, NULL, 2026-11-22, 1:20, 1_000, 0b10]
---
''')
        self.assertEqual(state, "ok")
        self.assertEqual(meta["x-test"], ["yes", "no", "on", "off", 12, 10, 16, 1000.0, True, None, "2026-11-22", "1:20", "1_000", "0b10"])
        self.assertIsInstance(meta["x-test"][7], float)

    def test_duplicate_keys_at_root_and_nested_levels(self):
        for fields in ("type: Reference\ntype: Metric", "type: Reference\nx-test: {same: 1, same: 2}"):
            with self.subTest(fields=fields):
                self.concept(fields)
                self.assertIn("E007", self.codes(self.run_validator(expected=1)))

    def test_malformed_yaml_and_unsafe_tags_report_errors(self):
        for fields in ("type: [broken", "type: Reference\nx-test: !!bool invalid", "? [a, b]\n: value", "type: Reference\nx-test: !!python/object/apply:os.system [echo forbidden]"):
            with self.subTest(fields=fields):
                self.concept(fields)
                self.assertIn("E002", self.codes(self.run_validator(expected=1)))

    def test_non_mapping_frontmatter_and_missing_delimiter(self):
        for text in ("---\n- item\n---\n", "---\ntype: Reference\n"):
            with self.subTest(text=text):
                self.write("concept.md", text)
                self.assertIn("E002", self.codes(self.run_validator(expected=1)))

    def test_ordinary_markdown_warns_without_failing_conformance(self):
        self.write("README.md", "# Documentation\n")
        self.assertIn("W120", self.codes(self.run_validator()))
        self.assertEqual(self.run_validator("--strict", expected=1)["errors"], 0)

    def test_reserved_files(self):
        self.write("nested/index.md", "---\ntitle: Wrong place\n---\n# Index\n")
        self.write("log.md", "---\ntitle: Wrong place\n---\n# Log\n## Yesterday\n")
        codes = self.codes(self.run_validator(expected=1))
        self.assertTrue({"E004", "E005", "E006"}.issubset(codes))

    def test_staleness_and_old_verification(self):
        self.concept('''type: Reference
generated: {by: "process:writer", at: "2026-11-21T12:00:00Z"}
verified: {by: "human:reviewer", at: "2026-11-20T12:00:00Z"}
stale_after: 2026-11-22''')
        codes = self.codes(self.run_validator("--strict"))
        self.assertTrue({"I201", "I204"}.issubset(codes))

    def test_explicit_timestamp_and_current_verification(self):
        self.concept('''type: Reference
generated: {by: "process:writer", at: !!timestamp 2026-11-22T12:00:00Z}
verified: {by: "human:reviewer", at: "2026-11-22T13:00:00+01:00"}''')
        self.assertNotIn("I204", self.codes(self.run_validator("--strict")))

    def test_malformed_staleness_is_not_fresh(self):
        self.concept('type: Reference\nstale_after: "2026-11-22T12:00:00"')
        result = self.run_validator()
        self.assertIn("W101", self.codes(result))
        self.assertIn("never treat the concept as fresh", result["findings"][0]["message"])

    def test_path_resolution_and_percent_encoding(self):
        self.write("references/manual file.txt", "Source evidence.\n")
        self.concept("type: Reference\nresource: /references/manual%20file.txt", "[Source](../references/manual%20file.txt#section)\n", "topics/concept.md")
        self.assertEqual(self.run_validator("--strict")["warnings"], 0)

    def test_legacy_path_fallback_is_version_specific(self):
        self.write("references/manual.txt", "Source evidence.\n")
        self.concept("type: Reference\nresource: references/manual.txt", path="topics/concept.md")
        self.assertIn("W116", self.codes(self.run_validator()))
        self.write("index.md", '---\nokf_version: "0.2"\n---\n# Test\n')
        self.assertIn("W119", self.codes(self.run_validator()))

    def test_deprecation_and_source_attribution(self):
        self.concept("type: Reference\nstatus: deprecated\nsuperseded_by: /missing.md", "Claim.[^unknown]\n")
        codes = self.codes(self.run_validator())
        self.assertTrue({"W116", "W108"}.issubset(codes))

    def test_computation_at_nested_heading_level(self):
        self.concept("type: Attested Computation\nruntime: python\nparameters: [{name: count, type: integer}]", "## Computation\n```python\nprint(count)\n```\n")
        result = self.run_validator("--strict")
        self.assertEqual(result["warnings"], 0)
        self.assertIn("I205", self.codes(result))

    def test_hidden_files_and_external_symlinks_are_not_read(self):
        outside = Path(self.temp.name) / "outside.md"
        outside.write_bytes(b"\xffinvalid UTF-8 that must never be read")
        self.write(".hidden/invalid.md", "---\n[invalid\n---\n")
        (self.bundle / "index.md").unlink()
        (self.bundle / "index.md").symlink_to(outside)
        (self.bundle / "escape.md").symlink_to(outside)
        self.assertEqual(self.run_validator()["files_checked"], 0)
        checker = validate.Checker(self.bundle, validate.parse_timestamp("2026-11-22"))
        self.assertEqual(checker.resolve_path(self.bundle / "concept.md", "escape.md", True)[0], "external")

    def test_missing_bundle_is_setup_error(self):
        result = subprocess.run([sys.executable, "-S", "-B", str(SCRIPTS / "validate.py"), str(self.bundle / "missing")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("not a directory", result.stderr)


if __name__ == "__main__":
    unittest.main()
