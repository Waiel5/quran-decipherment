"""Robustness verification for middle-ayah claim.

Key fix: strip tashkeel before substring matching, so the same surface
form is detected across orthographies.
"""

from __future__ import annotations

import re
import sys
import unicodedata

sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")

from tools.loader import load_quran
from tools.tokenize import real_words, graphemes


# Tashkeel ranges to strip for substring matching:
#   U+064B..U+065F (standard tashkeel)
#   U+0670 (dagger alif / superscript alif)
#   U+06D6..U+06ED (recitation marks)
#   U+0640 (tatweel)
TASHKEEL_RE = re.compile(
    r"[\u064B-\u065F\u0670\u06D6-\u06ED\u0640]"
)


def strip_tashkeel(s: str) -> str:
    return TASHKEEL_RE.sub("", s)


def normalize_uthmani(s: str) -> str:
    """Normalize Uthmani-orthography to skeleton.

    - Replace alif-with-wasla (U+0671) → plain alif (U+0627)
    - Replace hamza variants with plain alif/waw/ya (optional)
    - Strip tashkeel
    """
    s = strip_tashkeel(s)
    s = s.replace("\u0671", "\u0627")  # alif wasla → alif
    return s


def task1_verify():
    print("=" * 78)
    print("Task 1 robustness: does 2:143 contain 'وسط' in ALL orthographies?")
    print("=" * 78)
    for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
        surahs = load_quran(variant)
        baqarah = surahs[1]
        v143 = baqarah.verses[142]
        v144 = baqarah.verses[143]
        stripped143 = normalize_uthmani(v143.text)
        stripped144 = normalize_uthmani(v144.text)
        print(f"\n[{variant}]")
        print(f"  2:143 (stripped): {stripped143}")
        print(f"  2:143 contains 'وسط'? {'وسط' in stripped143}")
        print(f"  2:144 contains 'وسط'? {'وسط' in stripped144}")


def task8_verify():
    """Counterfactual with tashkeel-stripped matching across variants."""
    print("\n" + "=" * 78)
    print("Task 8 robustness: wasat near midpoint across all surahs, all variants")
    print("=" * 78)
    for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
        surahs = load_quran(variant)
        print(f"\n[{variant}]")
        strict_hits = []
        broad_hits = []
        for s in surahs:
            n = len(s.verses)
            if n % 2 == 0:
                mids = [n // 2, n // 2 + 1]
            else:
                mids = [(n + 1) // 2]
            for mid in mids:
                text = normalize_uthmani(s.verses[mid - 1].text)
                if "وسط" in text:
                    strict_hits.append((s.id, mid, n))
            # Broader window +/- 2 around mids
            lo = max(1, min(mids) - 2)
            hi = min(n, max(mids) + 2)
            for i in range(lo, hi + 1):
                text = normalize_uthmani(s.verses[i - 1].text)
                if "وسط" in text:
                    broad_hits.append((s.id, i, n))
        print(f"  Strictly at midpoint verse(s): {len(strict_hits)} surahs hit")
        for sid, vid, n in strict_hits:
            print(f"    {sid}:{vid} (n={n})")
        print(f"  Within +/- 2 of midpoint: {len(broad_hits)} hits")
        for sid, vid, n in broad_hits:
            print(f"    {sid}:{vid} (n={n})")


def task7_verify():
    """Base-rate: all occurrences of wasat-family across variants."""
    print("\n" + "=" * 78)
    print("Task 7 robustness: wasat-family base rate across variants")
    print("=" * 78)
    for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
        surahs = load_quran(variant)
        total_hits = []
        for s in surahs:
            for v in s.verses:
                text = normalize_uthmani(v.text)
                for tok in text.split():
                    # tokens with substring 'وسط' in the skeleton
                    if "وسط" in tok:
                        total_hits.append((s.id, v.id, tok))
        print(f"\n[{variant}] wasat-substring tokens: {len(total_hits)}")
        for sid, vid, tok in total_hits:
            print(f"  {sid}:{vid}  token={tok!r}")


def additional_quran_midpoints():
    """Show more context: which verses span the middle-word and middle-letter
    of the whole Quran, and what those verses are."""
    print("\n" + "=" * 78)
    print("Additional: full text of whole-Quran middle candidates")
    print("=" * 78)
    surahs = load_quran("no-tashkeel")
    # get verses 26:186, 26:187, 18:73, 18:77
    def get(sid, vid):
        return surahs[sid - 1].verses[vid - 1].text
    for (sid, vid) in [(26, 186), (26, 187), (18, 73), (18, 77)]:
        print(f"\n  {sid}:{vid}: {get(sid, vid)}")


if __name__ == "__main__":
    task1_verify()
    task8_verify()
    task7_verify()
    additional_quran_midpoints()
