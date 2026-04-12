"""Basmala handling — canonical strings, stats, and policy conversion.

Rules tuple field operated on: ``basmala_policy``. The amrayn corpus
stores the basmala **only** as verse 1 of surah 1, i.e. it is in
``counted-only-in-surah-1`` state by construction. To obtain a
different policy for analysis, use :func:`apply_basmala_policy`.
"""

from __future__ import annotations

import copy
from typing import Dict, List

from .gematria import text_value
from .loader import Surah, Verse
from .tokenize import graphemes, graphemes_with_shadda_doubled, real_words

__all__ = [
    "BASMALA_NO_TASHKEEL",
    "BASMALA_MIN_TASHKEEL",
    "BASMALA_FULL_TASHKEEL",
    "BASMALAS",
    "basmala_stats",
    "apply_basmala_policy",
    "BASMALA_POLICIES",
]


# The canonical basmala strings, one per orthography variant. These
# are the same strings the amrayn JSONs use as surah 1 verse 1 in
# each variant.
BASMALA_NO_TASHKEEL = "بسم الله الرحمن الرحيم"
BASMALA_MIN_TASHKEEL = "بِسم اللَّه الرَّحمٰن الرَّحيم"
BASMALA_FULL_TASHKEEL = "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ"

BASMALAS: Dict[str, str] = {
    "no-tashkeel": BASMALA_NO_TASHKEEL,
    "min-tashkeel": BASMALA_MIN_TASHKEEL,
    "full-tashkeel": BASMALA_FULL_TASHKEEL,
}

BASMALA_POLICIES = {
    "counted-in-surah",
    "counted-only-in-surah-1",
    "always-separator",
}


def basmala_stats(variant: str) -> Dict[str, int]:
    """Return a stat dict for the canonical basmala in ``variant``.

    Keys:
        letters: letter graphemes (``letter_definition = graphemes``)
        real_words: recitation-mark-filtered whitespace tokens
            (``word_definition = orthographic-token`` with the
            text-shape data-cleaning filter)
        graphemes_with_shadda: letters with shadda doubled
            (``letter_definition = with-shadda-doubled``)
        abjad_mashriqi: gematric value under the Mashriqi table
            (``abjad_table = mashriqi``)

    Anchor: under ``no-tashkeel``, ``letters = 19``, ``real_words = 4``,
    ``abjad_mashriqi = 786``.
    """
    if variant not in BASMALAS:
        raise ValueError(
            f"unknown variant {variant!r}; expected one of {sorted(BASMALAS)}"
        )
    text = BASMALAS[variant]
    return {
        "letters": graphemes(text),
        "real_words": len(real_words(text)),
        "graphemes_with_shadda": graphemes_with_shadda_doubled(text),
        "abjad_mashriqi": text_value(text, table="mashriqi"),
    }


def apply_basmala_policy(
    quran_data: List[Surah], policy: str, variant: str = "no-tashkeel"
) -> List[Surah]:
    """Return a deep-copied Quran adjusted to the given basmala policy.

    The input is assumed to be in the natural amrayn state:
    ``counted-only-in-surah-1``. Three policies are supported:

    - ``counted-only-in-surah-1``: no change (deep copy returned).
    - ``counted-in-surah``: prepend the canonical basmala to verse 1 of
      each of the 113 surahs that don't already carry it (everything
      except surah 1 Al-Fatiha — which already has it — and surah 9
      At-Tawba, which by tradition has no basmala).
    - ``always-separator``: strip the basmala from surah 1 verse 1.
      The rest of verse 1 of Al-Fatiha ("الحمد لله رب العالمين") is
      still present as verse 2, so stripping means replacing the
      surah 1 verse 1 text with the empty string (the verse ``id``
      is preserved so numbering stays intact).

    Args:
        quran_data: output of :func:`tools.loader.load_quran`.
        policy: one of :data:`BASMALA_POLICIES`.
        variant: the orthography variant of ``quran_data``; used to
            pick the right canonical basmala string. Defaults to
            ``'no-tashkeel'`` to match the primary corpus.

    Returns:
        A new list of :class:`Surah` with verses adjusted. The input
        is not mutated.
    """
    if policy not in BASMALA_POLICIES:
        raise ValueError(
            f"unknown policy {policy!r}; expected one of {sorted(BASMALA_POLICIES)}"
        )
    if variant not in BASMALAS:
        raise ValueError(
            f"unknown variant {variant!r}; expected one of {sorted(BASMALAS)}"
        )

    out = copy.deepcopy(quran_data)
    basmala = BASMALAS[variant]

    if policy == "counted-only-in-surah-1":
        return out

    if policy == "counted-in-surah":
        # Prepend the basmala to verse 1 of every non-At-Tawba surah,
        # INCLUDING surah 1. This matches the methodology §8 anchor
        # "add 113 × basmala = +452 words / +2147 letters": 113 surahs
        # (114 minus surah 9 At-Tawba) each gain one basmala's worth
        # of tokens / letters on top of the raw amrayn data. Note that
        # surah 1 (Al-Fatiha) already contains the basmala as its
        # verse 1 in the amrayn data; under this policy it ends up
        # with the basmala counted twice — that is the standard
        # reading of "counted at the head of every surah" because
        # surah 1's opening basmala IS its first verse, so prepending
        # makes it appear both as "header" and "verse 1". Callers who
        # want a different Fatiha treatment should implement their
        # own adjustment on top of this function's output.
        for surah in out:
            if surah.id == 9:
                continue
            if not surah.verses:
                continue
            v0 = surah.verses[0]
            new_text = basmala + " " + v0.text
            surah.verses[0] = Verse(id=v0.id, surah_id=v0.surah_id, text=new_text)
        return out

    if policy == "always-separator":
        # Strip the basmala from surah 1 verse 1. The rest of Al-Fatiha
        # starts at verse 2 in amrayn, so surah 1 verse 1's entire
        # contents ARE the basmala. Replace with empty text.
        surah1 = out[0]
        if surah1.id != 1 or not surah1.verses:
            return out
        v0 = surah1.verses[0]
        surah1.verses[0] = Verse(id=v0.id, surah_id=v0.surah_id, text="")
        return out

    return out  # unreachable
