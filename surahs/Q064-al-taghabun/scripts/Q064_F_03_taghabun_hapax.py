#!/usr/bin/env python3
"""
Q064-F-03: *taghābun* root g-b-n hapax-status — corpus-EXACT root attestation count.

Pre-reg: preregs/Q064-F-03-taghabun-hapax-prereg.md
Source: data/morphology/root-index.json (QAC v0.4) + quran-text/quran-no-tashkeel.json
Seed: n/a (deterministic)
Bonferroni k=1, α_bon = 0.05
"""
import json
import re
import hashlib
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG = PROJECT_ROOT / "surahs" / "Q064-al-taghabun" / "preregs" / "Q064-F-03-taghabun-hapax-prereg.md"
ROOT_INDEX = PROJECT_ROOT / "data" / "morphology" / "root-index.json"
QURAN_TEXT = PROJECT_ROOT / "quran-text" / "quran-no-tashkeel.json"
OUT = PROJECT_ROOT / "surahs" / "Q064-al-taghabun" / "csv" / "Q064-F-03.json"

def sha256_of_file(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def normalize(s):
    return re.sub(r"[ۖۚۗۘ۠ۙ]", "", s).strip()

def main():
    ri = json.load(open(ROOT_INDEX))
    qt = json.load(open(QURAN_TEXT))

    # H1: QAC root g-b-n attestation count
    root_key = "gbn"  # Buckwalter for غ-ب-ن
    locs = ri.get(root_key, [])
    n_root_attestations = len(locs)
    h1_pass = n_root_attestations == 1

    # H2: location verification
    h2_loc = locs[0] if locs else None
    h2_pass = h2_loc is not None and tuple(h2_loc) == (64, 9, 7)

    # H3: surface-form substring scan across corpus.
    # The root g-b-n (غ-ب-ن) admits surface forms with internal alif/etc. between root letters
    # (e.g., تَغَابُن with medial alif). We scan for any of the canonical g-b-n surface skeletons.
    # Patterns: "غبن" (no medial), "غابن" (medial alif), "تغابن" (CV stem with prefix).
    patterns = ["غبن", "غابن", "تغابن"]
    surface_hits = []
    seen_locations = set()
    for surah in qt:
        # build verse-level word list excluding pause marks (so word indices match QAC)
        for v in surah["verses"]:
            words_raw = v["text"].split()
            # filter pause marks
            words = [w for w in words_raw if normalize(w)]
            for w_idx, w in enumerate(words, start=1):
                wn = normalize(w)
                if not wn:
                    continue
                # match any pattern
                matched = [p for p in patterns if p in wn]
                if matched:
                    key = (surah["id"], v["id"], w_idx)
                    if key not in seen_locations:
                        seen_locations.add(key)
                        surface_hits.append({
                            "surah": surah["id"],
                            "verse": v["id"],
                            "word_idx": w_idx,
                            "token": wn,
                            "matched_patterns": matched,
                        })
    n_surface = len(surface_hits)
    h3_pass = (
        n_surface == 1
        and surface_hits[0]["surah"] == 64
        and surface_hits[0]["verse"] == 9
    )

    # Cross-reference with QAC: are root- and surface-counts consistent?
    consistent = (n_root_attestations == n_surface)

    # Verdict
    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3:
        verdict = "CORPUS-EXACT-HAPAX-CONFIRMED"
    elif n_pass >= 1:
        verdict = "PARTIAL"
    else:
        verdict = "REFUTED"

    out = {
        "test_id": "Q064-F-03",
        "title": "Q 64:9 *taghābun* root g-b-n hapax-status",
        "prereg_sha256": sha256_of_file(PREREG),
        "seed": None,
        "n_perm": 0,
        "bonferroni_k": 1,
        "alpha_bon": 0.05,
        "rules_tuple": "(no-tashkeel, QAC-v0.4-root-index, basmala-counted-only-in-Q1, Hafs-Kufan)",
        "data_source": [str(ROOT_INDEX.relative_to(PROJECT_ROOT)), str(QURAN_TEXT.relative_to(PROJECT_ROOT))],
        "root_key_buckwalter": root_key,
        "root_arabic": "غ-ب-ن",
        "n_root_attestations_qac_v04": n_root_attestations,
        "root_locations": locs,
        "surface_form_substring_hits": surface_hits,
        "n_surface_hits": n_surface,
        "qac_surface_consistency": consistent,
        "H1_corpus_exact_root_hapax": h1_pass,
        "H2_unique_location_q64_9_w7": h2_pass,
        "H3_surface_form_unique": h3_pass,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(f"Wrote {OUT}")
    print(f"  N QAC root g-b-n attestations: {n_root_attestations}")
    print(f"  Location: {locs}")
    print(f"  N surface 'غبن' hits: {n_surface}")
    print(f"  VERDICT: {verdict}")

if __name__ == "__main__":
    main()
