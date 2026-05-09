#!/usr/bin/env python3
"""
Q089-F-01 — al-nafs al-muṭmaʾinna corpus-EXACT phrase + soul-classification cohort
Pre-reg SHA256 lock: ae86d807f11de909e13025996c9310c04b29c43d78c03f74d05f222f57561b5f
Seed: 20260509
"""
import json
import hashlib
import re
import sys
from pathlib import Path

PREREG_PATH = Path(__file__).resolve().parent.parent / "preregs" / "Q089-F-01-nafs-mutmainna-prereg.md"
PREREG_SHA = "ae86d807f11de909e13025996c9310c04b29c43d78c03f74d05f222f57561b5f"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "csv" / "Q089-F-01.json"
SEED = 20260509

QURAN_PATH = "/Users/grey/Downloads/quran/data/alt-text/quran-uthmani-consonantal.json"


def verify_sha():
    h = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"PREREG SHA MISMATCH: expected {PREREG_SHA}, got {h}")
    print(f"PREREG SHA verified: {h}")


def normalize(s: str) -> str:
    """Hamza + final-yā normalization."""
    s = s.replace("إ", "ا").replace("أ", "ا").replace("آ", "ا")
    s = s.replace("ى", "ي")
    s = s.replace("ؤ", "و").replace("ئ", "ي")
    return s


def load_corpus():
    with open(QURAN_PATH) as f:
        return json.load(f)


def find_phrase(corpus, pattern):
    """Locate verses containing a normalized regex pattern."""
    pat = re.compile(normalize(pattern))
    hits = []
    for s in corpus:
        for v in s["verses"]:
            t = normalize(v["text"])
            if pat.search(t):
                hits.append({"surah": s["id"], "verse": v["id"], "text": v["text"]})
    return hits


def main():
    verify_sha()
    corpus = load_corpus()

    # H1 — al-nafs al-muṭmaʾinna corpus-EXACT
    mutmainna_hits = find_phrase(corpus, r"النفس\s+المطمينة")
    n_mutmainna = len(mutmainna_hits)

    # H2 — soul-classification cohort
    lawwama_hits = find_phrase(corpus, r"النفس\s+اللوامة")
    # ammara form may have variant – use looser regex around "الامارة" + "بالسوء"
    ammara_hits = find_phrase(corpus, r"الامارة\s+بالسوء")
    if not ammara_hits:
        # fallback: look for النفس...بالسوء jointly
        ammara_hits = find_phrase(corpus, r"للنفس\s+الامارة")
    if not ammara_hits:
        ammara_hits = find_phrase(corpus, r"النفس\s+لامارة")  # last fallback

    cohort_surahs = sorted({h["surah"] for h in mutmainna_hits + lawwama_hits + ammara_hits})

    h1_pass = (n_mutmainna == 1)
    h2_pass = (cohort_surahs == [12, 75, 89])

    if h1_pass and h2_pass:
        verdict = "CONFIRMED"
    elif h1_pass or h2_pass:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    out = {
        "test_id": "Q089-F-01",
        "prereg_sha256": PREREG_SHA,
        "seed": SEED,
        "h1": {
            "phrase": "al-nafs al-muṭmaʾinna",
            "regex": r"النفس\s+المطمينة",
            "n_corpus_occurrences": n_mutmainna,
            "hits": mutmainna_hits,
            "pre_locked_direction": "exactly 1",
            "pass": h1_pass
        },
        "h2": {
            "cohort": {
                "muṭmaʾinna": [{"surah": h["surah"], "verse": h["verse"]} for h in mutmainna_hits],
                "lawwāma": [{"surah": h["surah"], "verse": h["verse"]} for h in lawwama_hits],
                "ammāra_bi-l-sūʾ": [{"surah": h["surah"], "verse": h["verse"]} for h in ammara_hits]
            },
            "cohort_surahs": cohort_surahs,
            "pre_locked_direction": "exactly {Q 12, Q 75, Q 89}",
            "pass": h2_pass
        },
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "verdict": verdict
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"VERDICT: {verdict}")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
