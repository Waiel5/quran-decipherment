"""Seeded null-model shufflers for Phase B hypothesis testing.

See ``docs/statistical-rigor-protocol.md`` §1.1, §1.2, §1.5. These
shufflers implement the three primitive null models that the Phase B
hypothesis-hunting work will need:

- :func:`shuffle_characters` — within-verse character shuffle (§1.1).
- :func:`shuffle_words` — within-verse word-order shuffle; also the
  primitive for §1.2's "within-surah word shuffle" when composed over
  concatenated surah text.
- :func:`shuffle_verse_order` — within-surah verse-order shuffle.
- :func:`shuffle_surah_indices` — §1.5 surah-index permutation: the
  set of surahs is reordered; no verse content is touched.

All shufflers are **seeded via ``random.Random(seed)``** for strict
reproducibility. None of them mutates the input; each returns a new
object. This is important for pre-registration: given a fixed seed and
a fixed input, the output is byte-identical across runs.

Rules tuple fields: these functions produce surrogates that a caller
then re-tokenizes / re-letter-counts using :mod:`tools.tokenize` under
whatever orthography / word_definition / letter_definition the claim
uses. The shufflers themselves are rule-agnostic — they operate on
raw strings or loaded :class:`tools.loader.Surah` objects.
"""

from __future__ import annotations

import copy
import random
from typing import List

from .loader import Surah, Verse

__all__ = [
    "shuffle_characters",
    "shuffle_words",
    "shuffle_verse_order",
    "shuffle_surah_indices",
]


def shuffle_characters(text: str, seed: int) -> str:
    """Return ``text`` with its characters shuffled, preserving length.

    Implements the §1.1 within-verse character shuffle primitive.
    Every character (including whitespace, tashkeel, and recitation
    marks) is included in the permutation; the output string has the
    same length and multiset of characters as the input.

    Callers who want to shuffle only letters (e.g. to preserve word
    boundaries) should pre-split into words and call
    :func:`shuffle_characters` on each word.

    Args:
        text: the input string (typically a single verse).
        seed: integer seed for :class:`random.Random`.

    Returns:
        A new string of the same length.
    """
    rng = random.Random(seed)
    chars = list(text)
    rng.shuffle(chars)
    return "".join(chars)


def shuffle_words(verse_text: str, seed: int) -> str:
    """Return ``verse_text`` with its whitespace tokens re-ordered.

    Implements the word-shuffle primitive for §1.2. Tokens are
    re-assembled with single ASCII spaces between them. If the input
    has multiple internal spaces or tabs, they are normalized to
    single spaces in the output.

    Args:
        verse_text: the input verse string.
        seed: integer seed for :class:`random.Random`.

    Returns:
        A new string: the tokens in permuted order, joined by single
        spaces.
    """
    rng = random.Random(seed)
    tokens = verse_text.split()
    rng.shuffle(tokens)
    return " ".join(tokens)


def shuffle_verse_order(surah: Surah, seed: int) -> Surah:
    """Return a new :class:`Surah` with its verses in shuffled order.

    The verses themselves are deep-copied and otherwise unchanged; only
    the order of the ``verses`` list is permuted. Verse ``id`` fields
    are **preserved** on each verse (so a verse that was id=7 remains
    id=7 even if it's now in the first position). Downstream code that
    wants a "re-numbered" output should re-assign ids itself.

    Args:
        surah: the input :class:`Surah`.
        seed: integer seed for :class:`random.Random`.

    Returns:
        A new :class:`Surah` with the same metadata and a permuted
        ``verses`` list.
    """
    rng = random.Random(seed)
    new_surah = copy.deepcopy(surah)
    rng.shuffle(new_surah.verses)
    return new_surah


def shuffle_surah_indices(quran: List[Surah], seed: int) -> List[Surah]:
    """Return a new Quran with the surahs in shuffled order.

    Implements the §1.5 surah-index permutation null. No verse
    content is touched; the set of :class:`Surah` objects is the same,
    only their order in the returned list is permuted. Each surah's
    own ``id`` field is **preserved** — callers that want to model
    "the surah at position N now has index N" should re-assign ids
    after calling this function.

    Args:
        quran: the input list of 114 :class:`Surah` objects.
        seed: integer seed for :class:`random.Random`.

    Returns:
        A new list of :class:`Surah` in permuted order.
    """
    rng = random.Random(seed)
    new_quran = copy.deepcopy(quran)
    rng.shuffle(new_quran)
    return new_quran
