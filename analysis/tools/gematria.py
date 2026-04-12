"""Abjad (gematria) value calculation.

Rules tuple field operated on: ``abjad_table`` (one of
``mashriqi``, ``maghribi``). ``mashriqi`` is the default in this
codebase; switch to ``maghribi`` only when a specific claim requires it.

Both tables assign values to the 28 core Arabic consonants. Non-letter
characters (tashkeel, spaces, punctuation, recitation marks, digits)
are silently ignored with no contribution to the sum. Letters that
appear in the text but not in the chosen table emit a ``warnings.warn``
message but still contribute zero.

Canonical anchor: :func:`text_value` of ``'بسم الله الرحمن الرحيم'``
under ``mashriqi`` is **786**.
"""

from __future__ import annotations

import warnings
from typing import Dict

from .tokenize import is_letter, LETTER_RANGES

__all__ = [
    "ABJAD_MASHRIQI",
    "ABJAD_MAGHRIBI",
    "abjad_value",
    "word_value",
    "text_value",
]


# Eastern (Mashriqi) table. See methodology.md §6.
ABJAD_MASHRIQI: Dict[str, int] = {
    "ا": 1,
    "ب": 2,
    "ج": 3,
    "د": 4,
    "ه": 5,
    "و": 6,
    "ز": 7,
    "ح": 8,
    "ط": 9,
    "ي": 10,
    "ك": 20,
    "ل": 30,
    "م": 40,
    "ن": 50,
    "س": 60,
    "ع": 70,
    "ف": 80,
    "ص": 90,
    "ق": 100,
    "ر": 200,
    "ش": 300,
    "ت": 400,
    "ث": 500,
    "خ": 600,
    "ذ": 700,
    "ض": 800,
    "ظ": 900,
    "غ": 1000,
}

# Western (Maghribi) table. Five letters differ from Mashriqi:
#   ص=60, ض=90, س=300, ظ=800, غ=900, ش=1000 — and the two letters
#   ث=500 and خ=600 trade into the positions freed up. The standard
#   Maghribi assignments below are the widely cited set; any claim
#   that depends on Maghribi must cite its source table explicitly.
ABJAD_MAGHRIBI: Dict[str, int] = {
    "ا": 1,
    "ب": 2,
    "ج": 3,
    "د": 4,
    "ه": 5,
    "و": 6,
    "ز": 7,
    "ح": 8,
    "ط": 9,
    "ي": 10,
    "ك": 20,
    "ل": 30,
    "م": 40,
    "ن": 50,
    "ص": 60,
    "ع": 70,
    "ف": 80,
    "ض": 90,
    "ق": 100,
    "ر": 200,
    "س": 300,
    "ت": 400,
    "ث": 500,
    "خ": 600,
    "ذ": 700,
    "ظ": 800,
    "غ": 900,
    "ش": 1000,
}

_TABLES = {"mashriqi": ABJAD_MASHRIQI, "maghribi": ABJAD_MAGHRIBI}

# Characters we silently skip without warning: tashkeel, tatweel,
# hamza-on-alif / hamza-on-waw / hamza-on-ya (carriers that have no
# independent abjad value in the classical tables), standalone hamza,
# alif-maqsura, ta-marbuta, alif-with-wasla, dagger-alif, and all
# recitation marks. Anything else that isn't in the table and isn't
# silently-skipped triggers a warning.
_SILENT_SKIP = set(
    [
        "\u0621",  # ء hamza standalone
        "\u0622",  # آ alif with madda
        "\u0623",  # أ alif with hamza above
        "\u0624",  # ؤ waw with hamza
        "\u0625",  # إ alif with hamza below
        "\u0626",  # ئ ya with hamza
        "\u0629",  # ة ta marbuta
        "\u0640",  # ـ tatweel
        "\u0649",  # ى alif maqsura
        "\u0671",  # ٱ alif wasla (Uthmani)
        "\u0670",  # ٰ dagger alif
    ]
)
# Tashkeel U+064B..U+0652 and small-letter marks U+0653..U+065F.
for _cp in range(0x064B, 0x0660):
    _SILENT_SKIP.add(chr(_cp))
# Arabic-Indic digits U+0660..U+0669 and extended digits U+06F0..U+06F9.
for _cp in list(range(0x0660, 0x066A)) + list(range(0x06F0, 0x06FA)):
    _SILENT_SKIP.add(chr(_cp))
# Recitation marks U+06D6..U+06ED.
for _cp in range(0x06D6, 0x06EE):
    _SILENT_SKIP.add(chr(_cp))


def _get_table(name: str) -> Dict[str, int]:
    if name not in _TABLES:
        raise ValueError(
            f"unknown abjad table {name!r}; expected one of {sorted(_TABLES)}"
        )
    return _TABLES[name]


def abjad_value(letter: str, table: str = "mashriqi") -> int:
    """Return the abjad value of a single Arabic letter.

    Rules tuple field: ``abjad_table``.

    Args:
        letter: a single-character string.
        table: ``'mashriqi'`` (default) or ``'maghribi'``.

    Returns:
        The integer value from the selected table, or ``0`` if the
        character has no table entry. A warning is emitted for
        letter-like characters not in the table; silently-skipped
        characters (tashkeel, hamza carriers, etc.) return 0 without
        warning.
    """
    tbl = _get_table(table)
    if not letter:
        return 0
    ch = letter[0]
    if ch in tbl:
        return tbl[ch]
    if ch in _SILENT_SKIP or ch.isspace():
        return 0
    if is_letter(ch):
        warnings.warn(
            f"abjad_value: letter {ch!r} (U+{ord(ch):04X}) not in table {table!r}; "
            f"contributing 0"
        )
    return 0


def word_value(word: str, table: str = "mashriqi") -> int:
    """Return the abjad sum of all letters in ``word``.

    Rules tuple field: ``abjad_table``. Non-letter characters and
    letters absent from the table contribute zero. This is the
    standard "numerical value of a word" in Quranic numerology.
    """
    tbl = _get_table(table)
    total = 0
    for ch in word:
        if ch in tbl:
            total += tbl[ch]
        elif ch in _SILENT_SKIP or ch.isspace():
            continue
        elif is_letter(ch):
            warnings.warn(
                f"word_value: letter {ch!r} (U+{ord(ch):04X}) not in table "
                f"{table!r}; contributing 0"
            )
    return total


def text_value(text: str, table: str = "mashriqi") -> int:
    """Return the abjad sum of every letter in ``text``.

    Rules tuple field: ``abjad_table``. Equivalent to summing
    :func:`word_value` over ``text.split()``, but more efficient —
    walks the string once.
    """
    tbl = _get_table(table)
    total = 0
    for ch in text:
        if ch in tbl:
            total += tbl[ch]
        elif ch in _SILENT_SKIP or ch.isspace():
            continue
        elif is_letter(ch):
            warnings.warn(
                f"text_value: letter {ch!r} (U+{ord(ch):04X}) not in table "
                f"{table!r}; contributing 0"
            )
    return total
