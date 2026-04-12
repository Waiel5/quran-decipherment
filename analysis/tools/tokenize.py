"""Tokenization and letter-counting primitives.

All counting functions in this module operate on **already-loaded text**
(a ``str``). They do not take raw JSON. Callers compose these with
:mod:`tools.loader` and, where needed, :mod:`tools.basmala`.

Rules tuple fields these functions operate on:
    - ``word_definition``: :func:`whitespace_tokens` implements
      ``orthographic-token``; :func:`real_words` implements the same
      with recitation-mark-only tokens filtered (still
      ``orthographic-token`` per the methodology, but with the
      data-cleaning filter the text-shape investigation mandated).
    - ``letter_definition``: :func:`graphemes` implements ``graphemes``;
      :func:`graphemes_with_shadda_doubled` implements
      ``with-shadda-doubled``.

The recitation marks (U+06D6..U+06ED) are NOT Arabic letters; in the
amrayn ``no-tashkeel``/``min-tashkeel`` JSONs they are stored as
standalone space-separated tokens, which inflates naive whitespace
counts by ~4578. :func:`real_words` strips those pseudo-tokens.
"""

from __future__ import annotations

from typing import List, Tuple

__all__ = [
    "RECITATION_MARKS",
    "LETTER_RANGES",
    "SHADDA",
    "whitespace_tokens",
    "real_words",
    "is_letter",
    "is_recitation_mark",
    "graphemes",
    "graphemes_with_shadda_doubled",
]


# U+06D6..U+06ED inclusive: Arabic small high ligatures and pause markers.
# Note: range() is half-open, so this stops at U+06ED.
RECITATION_MARKS = range(0x06D6, 0x06EE)

# Arabic letter graphemes used by the text-shape anchors. Excludes
# tashkeel (U+064B..U+065F), tatweel (U+0640), recitation marks
# (U+06D6..U+06ED), and Arabic digits. The two ranges cover:
#   U+0621..U+064A — the 28 core letters plus hamza variants.
#   U+0671..U+06D3 — Uthmani orthography extras (alif-with-wasla, etc.).
LETTER_RANGES: List[Tuple[int, int]] = [(0x0621, 0x064A), (0x0671, 0x06D3)]

SHADDA = "\u0651"  # U+0651 ARABIC SHADDA


def _in_any_range(codepoint: int, ranges: List[Tuple[int, int]]) -> bool:
    for lo, hi in ranges:
        if lo <= codepoint <= hi:
            return True
    return False


def is_letter(ch: str) -> bool:
    """Return True if ``ch`` is an Arabic letter grapheme.

    Implements the ``letter_definition = graphemes`` rule: a character
    is a letter iff its code point falls inside any of
    :data:`LETTER_RANGES`. Tashkeel, tatweel, recitation marks,
    whitespace, ASCII, and digits all return ``False``.
    """
    if len(ch) != 1:
        return False
    return _in_any_range(ord(ch), LETTER_RANGES)


def is_recitation_mark(ch: str) -> bool:
    """Return True if ``ch`` is a recitation mark (U+06D6..U+06ED)."""
    if len(ch) != 1:
        return False
    return ord(ch) in RECITATION_MARKS


def whitespace_tokens(text: str) -> List[str]:
    """Return ``text.split()`` — raw whitespace tokens.

    Implements ``word_definition = orthographic-token`` without any
    data cleaning. On the amrayn ``no-tashkeel`` JSON this will
    include recitation-mark-only pseudo-tokens; use :func:`real_words`
    if those should be filtered.
    """
    return text.split()


def real_words(text: str) -> List[str]:
    """Return whitespace tokens with recitation-mark-only tokens removed.

    Implements ``word_definition = orthographic-token`` with the
    text-shape data cleaning applied: any token consisting **entirely**
    of characters in :data:`RECITATION_MARKS` is dropped. A token that
    contains at least one letter survives untouched, even if it also
    contains a recitation mark.
    """
    out: List[str] = []
    for tok in text.split():
        if all(ord(ch) in RECITATION_MARKS for ch in tok):
            continue
        out.append(tok)
    return out


def graphemes(text: str) -> int:
    """Count Arabic letter graphemes in ``text``.

    Implements ``letter_definition = graphemes``. Counts every
    character that satisfies :func:`is_letter`. Tashkeel, tatweel,
    spaces, recitation marks, and anything outside the Arabic letter
    ranges are ignored.
    """
    return sum(1 for ch in text if _in_any_range(ord(ch), LETTER_RANGES))


def graphemes_with_shadda_doubled(text: str) -> int:
    """Count letter graphemes, counting shadda'd letters twice.

    Implements ``letter_definition = with-shadda-doubled``: equal to
    :func:`graphemes` plus the count of :data:`SHADDA` characters in
    ``text``. Each shadda in the text means the preceding consonant is
    doubled, so we simply add one extra letter per shadda.
    """
    return graphemes(text) + text.count(SHADDA)
