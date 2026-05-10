#!/usr/bin/env python3
"""H-NEW-1370 — Corpus top-10 longest-verses chronological + rhetorical-type profile.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1370-long-verse-top10.md
Rules-tuple: (no-tashkeel, whitespace tokenization, non-space-character graphemes,
              basmala-counted-only-in-Q1, Hafs-Kufan)
"""
import csv
import hashlib
import json
import sys
from math import comb
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1370-long-verse-top10.md"
EXPECTED_SHA = "6aab7c774dc28f32c5d2b7777180c3a16cfed83d25e1d529f6b0dbc82ba50ae2"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
REVELATION = ROOT / "data/revelation-order.csv"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1370.json"

# Pre-committed rhetorical-type taxonomy (9 labels)
TYPES = {
    "debt-and-contract",
    "inheritance-and-bequest",
    "ritual-instruction",
    "marital-and-family-law",
    "food-and-purity-law",
    "jihad-and-warfare",
    "polemical-narrative",
    "prophetic-address-vocative",
    "mixed-jurisprudential",
    "other",
}


def verify_sha():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: expected {EXPECTED_SHA}, got {actual}")


def binom_sf(k, n, p):
    """One-sided P(X >= k | n, p) using exact binomial CDF complement."""
    total = 0.0
    for i in range(k, n + 1):
        total += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return total


def classify(sid, aid):
    """Pre-committed rhetorical-type assignment based on the verse's primary content.

    Sourced from classical mufassirūn (al-Ṭabarī, al-Qurṭubī, al-Rāzī, Ibn Kathīr).
    Labels are from the locked 9-type taxonomy in the pre-reg.
    """
    table = {
        (2, 282): ("debt-and-contract",
                   "the longest verse — full contract-recording prescription with witnesses, scribes, exceptions"),
        (4, 12): ("inheritance-and-bequest",
                  "spousal-and-collateral inheritance shares + bequest preconditions"),
        (4, 11): ("inheritance-and-bequest",
                  "primary inheritance shares for children and parents + bequest precedence"),
        (73, 20): ("ritual-instruction",
                   "night-prayer revision + recitation-amount allowance + zakāt + qard hasan"),
        (3, 154): ("polemical-narrative",
                   "post-Uhud psychological-state narration + munāfiq exposure"),
        (2, 102): ("polemical-narrative",
                   "Solomon-Hārūt-Mārūt sorcery polemical narrative"),
        (24, 31): ("marital-and-family-law",
                   "female modesty prescription + permitted mahārim enumeration"),
        (2, 196): ("ritual-instruction",
                   "hajj-and-ʿumra ritual procedure + tamattuʿ + fidyah substitutions"),
        (24, 61): ("food-and-purity-law",
                   "permitted communal-eating relations + greeting + privacy etiquette"),
        (5, 41): ("polemical-narrative",
                   "Jewish-rejection rebuke + tahrīf accusation + judicial address"),
        (9, 100): ("other",
                   "muhājirūn-anṣār foremost-believers blessing + paradise promise"),
        (9, 117): ("other",
                   "post-Tabūk tawbah affirmation for prophet + muhājirūn + anṣār"),
        (2, 219): ("food-and-purity-law",
                   "khamr + maysir prohibition + spending question"),
        (2, 213): ("mixed-jurisprudential",
                   "single-umma origin + scriptural dispute + divine guidance"),
        (2, 217): ("jihad-and-warfare",
                   "sacred-month fighting question + fitnah-worse-than-killing principle"),
        (4, 176): ("inheritance-and-bequest",
                   "kalālah inheritance — closing verse of al-Nisāʾ"),
        (5, 6): ("ritual-instruction",
                   "wuḍūʾ + tayammum procedure"),
        (2, 233): ("marital-and-family-law",
                   "breastfeeding-duration + maintenance + wet-nurse permissions"),
        (4, 23): ("marital-and-family-law",
                   "mahārim enumeration — prohibited marriage relations"),
        (4, 24): ("marital-and-family-law",
                   "permitted marriage classes + mahr requirement"),
    }
    if (sid, aid) in table:
        return table[(sid, aid)]
    return ("other", "uncatalogued — needs classical-tafsir consultation")


def main():
    verify_sha()
    quran = json.loads(QURAN.read_text())

    # Build verse list with word and char counts
    verses = []
    for s in quran:
        for v in s["verses"]:
            text = v["text"]
            wc = len(text.split())
            cc = len(text.replace(" ", ""))  # non-space character count
            verses.append({
                "sid": s["id"],
                "aid": v["id"],
                "word_count": wc,
                "char_count": cc,
                "text": text,
            })

    # Load chronological tags
    period_by_sid = {}
    noldeke_by_sid = {}
    with REVELATION.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["mushaf_order"])
            period_by_sid[sid] = row["period"].strip()
            noldeke_by_sid[sid] = row["noldeke_phase"].strip()

    # Corpus Medinan-verse-share baseline
    n_total = len(verses)
    n_medinan = sum(1 for v in verses if period_by_sid.get(v["sid"]) == "Medinan")
    medinan_share = n_medinan / n_total

    # === Cell A: rank by word_count descending, ties broken by char_count ===
    by_words = sorted(verses, key=lambda v: (-v["word_count"], -v["char_count"]))
    top10_words = by_words[:10]

    def tag(v):
        rtype, rgloss = classify(v["sid"], v["aid"])
        return {
            "sid": v["sid"],
            "aid": v["aid"],
            "word_count": v["word_count"],
            "char_count": v["char_count"],
            "period": period_by_sid.get(v["sid"], "?"),
            "noldeke_phase": noldeke_by_sid.get(v["sid"], "?"),
            "rhetorical_type": rtype,
            "rhetorical_gloss": rgloss,
        }

    top10_words_tagged = [tag(v) for v in top10_words]
    k_medinan_words = sum(1 for v in top10_words_tagged if v["period"] == "Medinan")
    p_words = binom_sf(k_medinan_words, 10, medinan_share)
    cell_a_pass = (k_medinan_words >= 7) and (p_words <= 0.05)

    # === Cell B: rank by char_count descending, ties broken by word_count ===
    by_chars = sorted(verses, key=lambda v: (-v["char_count"], -v["word_count"]))
    top10_chars = by_chars[:10]
    top10_chars_tagged = [tag(v) for v in top10_chars]
    k_medinan_chars = sum(1 for v in top10_chars_tagged if v["period"] == "Medinan")
    p_chars = binom_sf(k_medinan_chars, 10, medinan_share)
    cell_b_pass = (k_medinan_chars >= 7) and (p_chars <= 0.05)

    # === Verdict (Cell A primary) ===
    if k_medinan_words == 0:
        verdict = "PRE-COMMIT VIOLATION (Medinan count = 0; direction reversed)"
    elif cell_a_pass:
        verdict = "PASS-DIRECTED"
    elif k_medinan_words >= 7:
        verdict = "DIRECTIONAL (count threshold met; p > 0.05)"
    elif k_medinan_words >= 5:
        verdict = "PARTIAL (under-powered toward direction)"
    else:
        verdict = "NULL"

    # Cross-tabulation: Medinan vs Meccan by ranking
    cross_tab = {
        "by_word_count": {
            "medinan": k_medinan_words,
            "meccan": 10 - k_medinan_words,
        },
        "by_char_count": {
            "medinan": k_medinan_chars,
            "meccan": 10 - k_medinan_chars,
        },
    }

    # Intersection of the two top-10 sets
    set_words = {(v["sid"], v["aid"]) for v in top10_words}
    set_chars = {(v["sid"], v["aid"]) for v in top10_chars}
    intersection = sorted(set_words & set_chars)
    word_only = sorted(set_words - set_chars)
    char_only = sorted(set_chars - set_words)

    out = {
        "id": "H-NEW-1370",
        "title": "Corpus top-10 longest-verses chronological + rhetorical-type profile",
        "prereg_sha": EXPECTED_SHA,
        "rules_tuple": {
            "orthography": "no-tashkeel",
            "tokenization": "whitespace",
            "letter_counting": "non-space-character",
            "basmala_policy": "counted-only-in-surah-1",
            "verse_numbering": "hafs-kufan",
        },
        "corpus_baseline": {
            "n_verses_total": n_total,
            "n_verses_medinan": n_medinan,
            "medinan_share": medinan_share,
        },
        "cell_A_word_count_primary": {
            "top10": top10_words_tagged,
            "k_medinan": k_medinan_words,
            "p_binomial_one_sided": p_words,
            "pass": cell_a_pass,
        },
        "cell_B_char_count_replication": {
            "top10": top10_chars_tagged,
            "k_medinan": k_medinan_chars,
            "p_binomial_one_sided": p_chars,
            "pass": cell_b_pass,
        },
        "cross_tabulation": cross_tab,
        "set_overlap": {
            "intersection_word_and_char": intersection,
            "word_only": word_only,
            "char_only": char_only,
        },
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    print(f"Verdict: {verdict}")
    print(f"  Corpus Medinan-verse-share = {medinan_share:.4f} ({n_medinan}/{n_total})")
    print(f"  Cell A (word-count): k_medinan = {k_medinan_words}/10, p = {p_words:.6f}, pass = {cell_a_pass}")
    print(f"  Cell B (char-count): k_medinan = {k_medinan_chars}/10, p = {p_chars:.6f}, pass = {cell_b_pass}")
    print(f"  Set intersection (both rankings): {len(intersection)} verses")
    print()
    print("  Top-10 by word-count:")
    for i, v in enumerate(top10_words_tagged, 1):
        print(f"    {i:2d}. Q {v['sid']:>3}:{v['aid']:<3}  wc={v['word_count']:<4} cc={v['char_count']:<4}  {v['period']:<7}  [{v['noldeke_phase']}]  type={v['rhetorical_type']}")
    print()
    print("  Top-10 by char-count:")
    for i, v in enumerate(top10_chars_tagged, 1):
        print(f"    {i:2d}. Q {v['sid']:>3}:{v['aid']:<3}  wc={v['word_count']:<4} cc={v['char_count']:<4}  {v['period']:<7}  [{v['noldeke_phase']}]  type={v['rhetorical_type']}")
    print(f"\n  Written to: {OUT}")


if __name__ == "__main__":
    main()
