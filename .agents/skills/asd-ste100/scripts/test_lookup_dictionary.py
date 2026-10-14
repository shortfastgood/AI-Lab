"""Regression checks for dictionary retrieval and source preservation."""

import unittest

from lookup_dictionary import load_entries, lookup


class DictionaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = load_entries()

    def test_part_of_speech_changes_approval(self):
        for word in ("test", "check", "damage"):
            self.assertTrue(lookup(self.entries, word, "n")["entries"][0]["approved"])
            self.assertFalse(lookup(self.entries, word, "v")["entries"][0]["approved"])

    def test_explicit_forms_and_case(self):
        for query, headword in (("REMOVED", "REMOVE"), ("were", "BE"), ("made sure", "MAKE SURE")):
            self.assertIn(headword, [e["word"] for e in lookup(self.entries, query)["entries"]])

    def test_phrases_and_qualified_entries(self):
        for query in ("make sure", "as … as", "in case of", "in the process of", "matte"):
            self.assertEqual(lookup(self.entries, query)["status"], "found")

    def test_line_wrapping_does_not_break_headwords(self):
        for query in ("electromagnetically", "counterclockwise", "interchangeable", "unsatisfactorily"):
            self.assertEqual(lookup(self.entries, query)["status"], "found")

    def test_unknown_is_unresolved(self):
        result = lookup(self.entries, "unlisted-project-widget")
        self.assertEqual(result, {"query": "unlisted-project-widget", "status": "unresolved", "entries": []})

    def test_search_is_bounded_and_marked(self):
        result = lookup(self.entries, "a", search=True)
        self.assertEqual(result["status"], "index_only")
        self.assertTrue(result["truncated"])
        self.assertEqual(len(result["matches"]), 20)
        self.assertGreater(result["total_matches"], 20)

    def test_restricted_meanings_and_forms_retained(self):
        above = lookup(self.entries, "above")["entries"][0]
        text = " ".join(p["text"].replace("\n", " ") for p in above["excerpts"])
        self.assertIn("MORE THAN", text)
        be = lookup(self.entries, "be")["entries"][0]
        self.assertIn("No other verb forms.", " ".join(p["text"].replace("\n", " ") for p in be["excerpts"]))
        self.assertNotIn("been", be["aliases"])

    def test_entries_are_unique_and_sourced(self):
        keys = {(e["word"], e["part_of_speech"]) for e in self.entries}
        self.assertEqual(len(keys), len(self.entries))
        self.assertEqual(len(self.entries), 2196)
        for entry in self.entries:
            self.assertTrue(entry["word"])
            self.assertTrue(entry["excerpts"])
            for excerpt in entry["excerpts"]:
                self.assertTrue(excerpt["text"].strip())
                self.assertRegex(excerpt["printed_page"], r"^2-1-[A-Z]+\d+$")

    def test_entries_with_nonsequential_pdf_text_order(self):
        for word in ("ALTHOUGH", "alternatively", "conduct", "confirm", "retain", "retorque", "rewind", "rework", "uncoil", "uncontaminated"):
            entry = lookup(self.entries, word)["entries"][0]
            text = " ".join(p["text"] for p in entry["excerpts"])
            self.assertIn(word, text)
        retained = lookup(self.entries, "retain")["entries"][0]["excerpts"][0]["text"]
        self.assertNotIn("retorque", retained)


if __name__ == "__main__":
    unittest.main()
