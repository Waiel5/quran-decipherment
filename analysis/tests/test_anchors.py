"""Anchor tests — every locked value in methodology.md §8.

These tests are the contract between the counting tools and the
text-shape investigation. If any of them fails, either the code is
broken or the anchor is wrong — investigate which, don't silently
"adjust" the anchor to match a buggy tool.

Run from the repo root:
    python3 -m unittest analysis.tests.test_anchors -v
Or:
    python3 /Users/grey/Downloads/quran/analysis/tests/test_anchors.py
"""

from __future__ import annotations

import os
import sys
import unittest

# Make sure the ``tools`` package is importable no matter where this
# test is invoked from.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ANALYSIS = os.path.dirname(_HERE)
if _ANALYSIS not in sys.path:
    sys.path.insert(0, _ANALYSIS)

from tools.basmala import (  # noqa: E402
    BASMALA_NO_TASHKEEL,
    apply_basmala_policy,
    basmala_stats,
)
from tools.gematria import text_value  # noqa: E402
from tools.loader import load_quran  # noqa: E402
from tools.tokenize import (  # noqa: E402
    graphemes,
    graphemes_with_shadda_doubled,
    real_words,
    whitespace_tokens,
)


SHADDA = "\u0651"


def _joined(quran) -> str:
    """Join every verse in every surah with single ASCII spaces."""
    return " ".join(v.text for s in quran for v in s.verses)


class StructureAnchors(unittest.TestCase):
    """Surah and verse counts — must hold for every variant."""

    def test_surah_count_every_variant(self):
        for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
            with self.subTest(variant=variant):
                q = load_quran(variant)
                self.assertEqual(len(q), 114)

    def test_verse_count_every_variant(self):
        for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
            with self.subTest(variant=variant):
                q = load_quran(variant)
                total = sum(len(s.verses) for s in q)
                self.assertEqual(total, 6236)


class NoTashkeelAnchors(unittest.TestCase):
    """All anchors computed against quran-no-tashkeel.json."""

    @classmethod
    def setUpClass(cls):
        cls.q = load_quran("no-tashkeel")
        cls.joined = _joined(cls.q)

    def test_whitespace_tokens(self):
        self.assertEqual(len(whitespace_tokens(self.joined)), 82375)

    def test_real_words(self):
        self.assertEqual(len(real_words(self.joined)), 77797)

    def test_letter_graphemes(self):
        self.assertEqual(graphemes(self.joined), 330709)

    def test_recitation_mark_only_tokens(self):
        toks = whitespace_tokens(self.joined)
        n = sum(1 for t in toks if all(0x06D6 <= ord(c) <= 0x06ED for c in t))
        self.assertEqual(n, 4578)


class MinTashkeelAnchors(unittest.TestCase):
    """All anchors computed against quran-min-tashkeel.json."""

    @classmethod
    def setUpClass(cls):
        cls.q = load_quran("min-tashkeel")
        cls.joined = _joined(cls.q)

    def test_whitespace_tokens_raw(self):
        self.assertEqual(len(whitespace_tokens(self.joined)), 82008)

    def test_real_words(self):
        self.assertEqual(len(real_words(self.joined)), 77430)

    def test_recitation_mark_only_tokens(self):
        toks = whitespace_tokens(self.joined)
        n = sum(1 for t in toks if all(0x06D6 <= ord(c) <= 0x06ED for c in t))
        self.assertEqual(n, 4578)


class FullTashkeelAnchors(unittest.TestCase):
    """All anchors computed against quran-full-tashkeel.json."""

    @classmethod
    def setUpClass(cls):
        cls.q = load_quran("full-tashkeel")
        cls.joined = _joined(cls.q)

    def test_real_words(self):
        self.assertEqual(len(real_words(self.joined)), 77429)

    def test_letter_graphemes(self):
        self.assertEqual(graphemes(self.joined), 327038)

    def test_letter_plus_shadda(self):
        self.assertEqual(graphemes_with_shadda_doubled(self.joined), 349716)

    def test_shadda_count(self):
        self.assertEqual(self.joined.count(SHADDA), 22678)


class BasmalaAnchors(unittest.TestCase):
    """Basmala letter/word/abjad anchors under no-tashkeel."""

    def test_basmala_letters(self):
        self.assertEqual(graphemes(BASMALA_NO_TASHKEEL), 19)

    def test_basmala_real_words(self):
        self.assertEqual(len(real_words(BASMALA_NO_TASHKEEL)), 4)

    def test_basmala_abjad_mashriqi_is_786(self):
        # Famous canonical anchor: abjad(basmala) = 786.
        self.assertEqual(text_value(BASMALA_NO_TASHKEEL, "mashriqi"), 786)

    def test_basmala_stats_dict(self):
        stats = basmala_stats("no-tashkeel")
        self.assertEqual(stats["letters"], 19)
        self.assertEqual(stats["real_words"], 4)
        self.assertEqual(stats["abjad_mashriqi"], 786)


class BasmalaPolicyAdjustmentAnchors(unittest.TestCase):
    """Locked adjustments from methodology.md §8 and text-shape.

    counted-in-surah: +452 words, +2147 letters (= 113 × basmala).
    always-separator: -4 words, -19 letters (= -1 × basmala).
    """

    @classmethod
    def setUpClass(cls):
        cls.q = load_quran("no-tashkeel")
        cls.base_words = len(real_words(_joined(cls.q)))
        cls.base_letters = graphemes(_joined(cls.q))

    def test_counted_in_surah_word_delta(self):
        q2 = apply_basmala_policy(self.q, "counted-in-surah")
        delta = len(real_words(_joined(q2))) - self.base_words
        self.assertEqual(delta, 452)

    def test_counted_in_surah_letter_delta(self):
        q2 = apply_basmala_policy(self.q, "counted-in-surah")
        delta = graphemes(_joined(q2)) - self.base_letters
        self.assertEqual(delta, 2147)

    def test_always_separator_word_delta(self):
        q2 = apply_basmala_policy(self.q, "always-separator")
        delta = len(real_words(_joined(q2))) - self.base_words
        self.assertEqual(delta, -4)

    def test_always_separator_letter_delta(self):
        q2 = apply_basmala_policy(self.q, "always-separator")
        delta = graphemes(_joined(q2)) - self.base_letters
        self.assertEqual(delta, -19)


class UnknownVariantRejected(unittest.TestCase):
    def test_unknown_variant_raises_valueerror(self):
        with self.assertRaises(ValueError):
            load_quran("uthmani-rasm")


if __name__ == "__main__":
    unittest.main(verbosity=2)
