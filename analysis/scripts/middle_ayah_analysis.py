"""Middle-ayah Al-Baqarah replication.

Tests the popular claim that Surah 2:143 (containing "wasatan") is the
middle verse of Al-Baqarah / of the Quran.

Run: python middle_ayah_analysis.py
"""

from __future__ import annotations

import json
import os
import re
import sys

# Make the toolkit importable
sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")

from tools.loader import load_quran
from tools.tokenize import real_words, graphemes


DATA_DIR = "/Users/grey/Downloads/quran/quran-text"


def fp(variant: str) -> str:
    """Short fingerprint for no/min/full-tashkeel."""
    return {
        "no-tashkeel": "nt",
        "min-tashkeel": "mt",
        "full-tashkeel": "ft",
    }[variant]


def print_section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------
# Task 1: middle-by-verse-index
# ----------------------------------------------------------------------

def task1_middle_verse_index():
    print_section("TASK 1: Middle-by-verse-index in Al-Baqarah")
    for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
        surahs = load_quran(variant)
        baqarah = surahs[1]
        assert baqarah.id == 2
        n = len(baqarah.verses)
        print(f"\n[{fp(variant)}] Al-Baqarah verse count = {n}")
        for idx in (143, 144):
            v = baqarah.verses[idx - 1]
            contains_wasat = bool(re.search(r"وسط", v.text))
            print(f"  2:{idx}  contains 'وسط'? {contains_wasat}")
            print(f"    text: {v.text}")


# ----------------------------------------------------------------------
# Task 2: middle-by-word-count within Al-Baqarah
# ----------------------------------------------------------------------

def find_verse_at_word(surah, target_word_index, tokenizer=real_words):
    """Return (verse_id, word_in_verse_idx, total_words_before) for the
    verse containing the target_word_index-th real word of the surah
    (1-indexed).
    """
    cumulative = 0
    for v in surah.verses:
        words = tokenizer(v.text)
        if cumulative + len(words) >= target_word_index:
            offset = target_word_index - cumulative
            return v.id, offset, words
        cumulative += len(words)
    raise ValueError(f"target {target_word_index} > total {cumulative}")


def task2_middle_word():
    print_section("TASK 2: Middle-by-word-count within Al-Baqarah")
    for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
        surahs = load_quran(variant)
        baqarah = surahs[1]
        total = sum(len(real_words(v.text)) for v in baqarah.verses)
        mid_low = (total + 1) // 2          # lower median (1-indexed)
        mid_high = total // 2 + 1           # upper median (1-indexed)
        print(f"\n[{fp(variant)}/real-words] total real-words in Al-Baqarah = {total}")
        print(f"  lower-median word index = {mid_low}")
        print(f"  upper-median word index = {mid_high}")
        for label, tgt in (("lower", mid_low), ("upper", mid_high)):
            vid, off, words = find_verse_at_word(baqarah, tgt)
            word = words[off - 1]
            print(f"  {label}: 2:{vid} word #{off} = {word!r}")


# ----------------------------------------------------------------------
# Task 3: middle-by-letter-count within Al-Baqarah
# ----------------------------------------------------------------------

def find_verse_at_letter(surah, target_letter_index):
    """Return verse_id of the verse containing the target_letter_index-th
    letter of the surah (1-indexed).
    """
    cumulative = 0
    for v in surah.verses:
        n = graphemes(v.text)
        if cumulative + n >= target_letter_index:
            offset = target_letter_index - cumulative
            return v.id, offset
        cumulative += n
    raise ValueError(f"target {target_letter_index} > total {cumulative}")


def task3_middle_letter():
    print_section("TASK 3: Middle-by-letter-count within Al-Baqarah")
    for variant in ("no-tashkeel", "min-tashkeel", "full-tashkeel"):
        surahs = load_quran(variant)
        baqarah = surahs[1]
        total = sum(graphemes(v.text) for v in baqarah.verses)
        mid_low = (total + 1) // 2
        mid_high = total // 2 + 1
        print(f"\n[{fp(variant)}/graphemes] total letters in Al-Baqarah = {total}")
        print(f"  lower-median letter index = {mid_low}")
        print(f"  upper-median letter index = {mid_high}")
        for label, tgt in (("lower", mid_low), ("upper", mid_high)):
            vid, off = find_verse_at_letter(baqarah, tgt)
            print(f"  {label}: 2:{vid} letter #{off}-in-verse")


# ----------------------------------------------------------------------
# Task 4: middle of the whole Quran
# ----------------------------------------------------------------------

def task4_whole_quran():
    print_section("TASK 4: Middle of the whole Quran")
    variant = "no-tashkeel"
    surahs = load_quran(variant)

    # 4a: middle by total verse index
    flat_verses = [(s.id, v.id, v.text) for s in surahs for v in s.verses]
    total_v = len(flat_verses)
    print(f"\n[{fp(variant)}] total verses = {total_v}")
    assert total_v == 6236
    # Two "middle" candidates for even count: positions 3118 and 3119
    for pos in (3118, 3119):
        s_id, v_id, text = flat_verses[pos - 1]
        contains = bool(re.search(r"وسط", text))
        print(f"  verse #{pos}: {s_id}:{v_id}  contains 'وسط'? {contains}")
        print(f"    text: {text}")

    # 4b: middle by total word count
    total_w = 0
    per_verse_words = []
    for s in surahs:
        for v in s.verses:
            w = real_words(v.text)
            per_verse_words.append((s.id, v.id, w))
            total_w += len(w)
    print(f"\n[{fp(variant)}/real-words] total real-words in Quran = {total_w}")
    # Find verse at lower and upper median
    mid_low_w = (total_w + 1) // 2
    mid_high_w = total_w // 2 + 1
    print(f"  lower-median word index = {mid_low_w}")
    print(f"  upper-median word index = {mid_high_w}")
    for label, tgt in (("lower", mid_low_w), ("upper", mid_high_w)):
        cumulative = 0
        for (sid, vid, words) in per_verse_words:
            if cumulative + len(words) >= tgt:
                offset = tgt - cumulative
                word = words[offset - 1]
                print(f"  {label}: {sid}:{vid} word #{offset} = {word!r}")
                break
            cumulative += len(words)

    # 4c: middle by total letter count
    total_l = 0
    per_verse_letters = []
    for s in surahs:
        for v in s.verses:
            n = graphemes(v.text)
            per_verse_letters.append((s.id, v.id, n))
            total_l += n
    print(f"\n[{fp(variant)}/graphemes] total letters in Quran = {total_l}")
    mid_low_l = (total_l + 1) // 2
    mid_high_l = total_l // 2 + 1
    print(f"  lower-median letter index = {mid_low_l}")
    print(f"  upper-median letter index = {mid_high_l}")
    for label, tgt in (("lower", mid_low_l), ("upper", mid_high_l)):
        cumulative = 0
        for (sid, vid, n) in per_verse_letters:
            if cumulative + n >= tgt:
                offset = tgt - cumulative
                print(f"  {label}: {sid}:{vid} letter #{offset}-in-verse")
                break
            cumulative += n


# ----------------------------------------------------------------------
# Task 7: null sanity check - positions of wasat-family surface forms
# ----------------------------------------------------------------------

def task7_wasat_surface_forms():
    print_section("TASK 7: Base-rate of wasat-family surface forms in Quran")
    variant = "no-tashkeel"
    surahs = load_quran(variant)
    # Surface forms to check
    forms = {
        "وسط": "wasat (stem/adjective)",
        "وسطا": "wasat-an (accusative indefinite)",
        "وسطى": "al-wustaa (feminine)",
        "أوسط": "awsat (elative)",
        "الوسطى": "al-wustaa (definite feminine)",
    }
    # Substring matches across all verses (no-tashkeel stem search)
    # Also do root-based: any token starting with و س ط consonant string
    print("\nSearching for substring occurrences in verse text (no-tashkeel):")
    hits = {form: [] for form in forms}
    for s in surahs:
        for v in s.verses:
            # tokens
            toks = real_words(v.text)
            for tok in toks:
                for form in forms:
                    if form == tok:
                        hits[form].append((s.id, v.id, tok))
    for form, label in forms.items():
        print(f"\n  exact-token '{form}' ({label}): {len(hits[form])} occurrences")
        for sid, vid, tok in hits[form]:
            print(f"    {sid}:{vid}  token={tok!r}")

    # Also do a "root-family substring" search
    print("\n--- Root-family substring search ---")
    root_re = re.compile(r"وس[ ]?ط")
    root_hits = []
    for s in surahs:
        for v in s.verses:
            # Find unique tokens matching
            for tok in real_words(v.text):
                # tokens containing consecutive و س ط
                if re.search(r"وسط", tok):
                    root_hits.append((s.id, v.id, tok))
    print(f"\nAll tokens containing substring 'وسط' in no-tashkeel:")
    for sid, vid, tok in root_hits:
        print(f"  {sid}:{vid}  token={tok!r}")
    print(f"\nTotal: {len(root_hits)} tokens in {len(set((sid,vid) for sid,vid,_ in root_hits))} unique verses")

    # Also check وسطى (different spelling w/ alif maksura)
    print("\nTokens containing substring 'وسطى':")
    for s in surahs:
        for v in s.verses:
            for tok in real_words(v.text):
                if "وسطى" in tok:
                    print(f"  {sid}:{vid}  token={tok!r}")


# ----------------------------------------------------------------------
# Task 8: counterfactual count across surahs with even verse counts
# ----------------------------------------------------------------------

def task8_counterfactual():
    print_section("TASK 8: Counterfactual — wasat near midpoint of all surahs")
    variant = "no-tashkeel"
    surahs = load_quran(variant)
    # Count even-verse surahs
    even = [s for s in surahs if len(s.verses) % 2 == 0]
    print(f"\n[{fp(variant)}] Surahs with even verse count: {len(even)} / 114")
    # For each, check middle verse(s) for wasat-substring
    near_hits = []
    broader_hits = []  # within +/- 2 verses of midpoint
    for s in surahs:
        n = len(s.verses)
        if n % 2 == 0:
            mids = [n // 2, n // 2 + 1]
        else:
            mids = [(n + 1) // 2]
        # strict: exactly at midpoint
        for mid in mids:
            v = s.verses[mid - 1]
            if re.search(r"وسط", v.text):
                near_hits.append((s.id, mid, n, v.text))
        # broader: +/- 2
        for i in range(max(1, min(mids) - 2), min(n, max(mids) + 2) + 1):
            v = s.verses[i - 1]
            if re.search(r"وسط", v.text):
                broader_hits.append((s.id, i, n, v.text))
    print(f"\nSurahs where a 'middle' verse literally contains 'وسط':")
    for sid, vid, n, text in near_hits:
        print(f"  {sid}:{vid}  (surah has {n} verses)  text: {text}")
    print(f"\nSurahs where any verse within +/- 2 of midpoint contains 'وسط':")
    for sid, vid, n, text in broader_hits:
        print(f"  {sid}:{vid}  (surah has {n} verses)  text: {text}")


if __name__ == "__main__":
    task1_middle_verse_index()
    task2_middle_word()
    task3_middle_letter()
    task4_whole_quran()
    task7_wasat_surface_forms()
    task8_counterfactual()
