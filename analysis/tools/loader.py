"""Loader for the amrayn/quran-text JSON corpora.

Produces a list of :class:`Surah` dataclasses carrying the raw verse texts,
leaving all counting / normalization decisions to downstream tools.

Rules tuple field operated on: ``orthography`` (one of
``no-tashkeel``, ``min-tashkeel``, ``full-tashkeel``).

Basmala policy (IMPORTANT):
    The amrayn dataset stores the basmala **only as verse 1 of surah 1
    (Al-Fatiha)**. No other surah carries its opening basmala as text.
    By construction, therefore, the raw loaded data already implements
    the methodology's ``basmala-counted-only-in-surah-1`` policy. To
    obtain a different ``basmala_policy`` value (e.g.
    ``counted-in-surah`` or ``always-separator``), call
    :func:`tools.basmala.apply_basmala_policy` on the loaded data.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import List

__all__ = ["Verse", "Surah", "load_quran", "DATA_DIR", "VARIANTS"]


DATA_DIR = "/Users/grey/Downloads/quran/quran-text"

VARIANTS = {
    "no-tashkeel": "quran-no-tashkeel.json",
    "min-tashkeel": "quran-min-tashkeel.json",
    "full-tashkeel": "quran-full-tashkeel.json",
}


@dataclass
class Verse:
    """A single verse.

    Attributes:
        id: 1-indexed verse number within its surah (hafs-kufan numbering).
        surah_id: 1-indexed surah number (1..114).
        text: raw verse text in the chosen orthography, unmodified from
            the JSON source.
    """

    id: int
    surah_id: int
    text: str


@dataclass
class Surah:
    """A single surah.

    Attributes:
        id: 1-indexed surah number (1..114).
        name: Arabic name from the JSON source.
        transliteration: Latinized name from the JSON source.
        type: "meccan" or "medinan" as declared in the JSON.
        total_verses: declared verse count from the JSON source.
        verses: list of :class:`Verse` in canonical order.
    """

    id: int
    name: str
    transliteration: str
    type: str
    total_verses: int
    verses: List[Verse] = field(default_factory=list)


def load_quran(variant: str = "no-tashkeel") -> List[Surah]:
    """Load the Quran JSON for the given orthography variant.

    Args:
        variant: one of ``'no-tashkeel'``, ``'min-tashkeel'``,
            ``'full-tashkeel'``. This sets the ``orthography`` field
            of the rules tuple for any downstream counting.

    Returns:
        A list of 114 :class:`Surah` objects in canonical mushaf order.
        Verse texts are returned exactly as stored in the JSON: no
        normalization, no basmala injection, no recitation-mark
        filtering. The basmala appears only as surah 1 verse 1, so the
        data is in the ``basmala-counted-only-in-surah-1`` state by
        construction.

    Raises:
        ValueError: if ``variant`` is not one of the known variants.
        FileNotFoundError: if the JSON file is missing.
    """
    if variant not in VARIANTS:
        raise ValueError(
            f"unknown variant {variant!r}; expected one of {sorted(VARIANTS)}"
        )

    path = os.path.join(DATA_DIR, VARIANTS[variant])
    with open(path, "r", encoding="utf-8") as fh:
        raw = json.load(fh)

    surahs: List[Surah] = []
    for s in raw:
        verses = [
            Verse(id=v["id"], surah_id=s["id"], text=v["text"])
            for v in s["verses"]
        ]
        surahs.append(
            Surah(
                id=s["id"],
                name=s["name"],
                transliteration=s["transliteration"],
                type=s["type"],
                total_verses=s["total_verses"],
                verses=verses,
            )
        )
    return surahs
