#!/usr/bin/env python3
"""
Q089-F-03 — 4-element wa-coordinated oath-architecture taxonomy.
Pre-reg SHA256 lock: da8f6b6d67c07200cf460c061140f18dc7bb75756a071216699872bf3b2c4817
Seed: 20260509
"""
import json
import hashlib
import re
import sys
from pathlib import Path

PREREG_PATH = Path(__file__).resolve().parent.parent / "preregs" / "Q089-F-03-oath-architecture-taxonomy-prereg.md"
PREREG_SHA = "da8f6b6d67c07200cf460c061140f18dc7bb75756a071216699872bf3b2c4817"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "csv" / "Q089-F-03.json"
SEED = 20260509

QURAN_PATH = "/Users/grey/Downloads/quran/data/alt-text/quran-uthmani-consonantal.json"

OATH_CLUSTER = [37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103]


def verify_sha():
    h = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"PREREG SHA MISMATCH: expected {PREREG_SHA}, got {h}")
    print(f"PREREG SHA verified: {h}")


def normalize(s: str) -> str:
    s = s.replace("إ", "ا").replace("أ", "ا").replace("آ", "ا")
    s = s.replace("ى", "ي")
    s = s.replace("ؤ", "و").replace("ئ", "ي")
    return s


def count_oath_particles(verses_iter):
    """Walk verses (in order); count wa- and fa- oath particles at the head of phrases.

    Heuristic: at v.1, split tokens; for each token, check whether it begins with
    `و` (wa-) or `ف` (fa-) + one of {`ال`, `ل`, indefinite-noun-ending-with-tanwin
    fragment}. The pre-reg locks the rule: count `wa-` and `fa-` particles whose
    immediate following morpheme is a noun-phrase head (definite article,
    indefinite tanwin-marked noun like *layālin*).

    Continue counting through subsequent verses until either:
      (a) a verse not starting with wa-/fa-, OR
      (b) a verse starting with `إنّ`, `هل`, or imperative-verb signaling the
          purpose-clause.
    """
    n_wa = 0
    n_fa = 0
    elements = []
    stop = False
    for vid, vt in verses_iter:
        if stop:
            break
        text = normalize(vt).strip()
        # Detect purpose-clause stop
        if text.startswith("ان ") or text.startswith("إنّ") or text.startswith("هل "):
            stop = True
            break
        # Tokenize
        toks = text.split()
        if not toks:
            continue
        # Check whether v.1 token begins with wa- or fa-
        head = toks[0]
        if head.startswith("و"):
            # consume oath element from v.1
            n_wa += 1
            elements.append(("wa-", vid, head))
        elif head.startswith("ف"):
            n_fa += 1
            elements.append(("fa-", vid, head))
        else:
            stop = True
            break
        # Check additional conjunctions inside v.1 (e.g., wa-l-shafʿ wa-l-witr)
        for tok in toks[1:]:
            if tok.startswith("و") and len(tok) > 1 and tok[1] in ("ا", "ل"):
                # Only count `wa-` that introduces another definite-noun
                if tok.startswith("وال"):
                    n_wa += 1
                    elements.append(("wa-", vid, tok))
            elif tok.startswith("ف") and len(tok) > 1 and tok[1] == "ا":
                if tok.startswith("فال"):
                    n_fa += 1
                    elements.append(("fa-", vid, tok))
    return n_wa, n_fa, elements


def main():
    verify_sha()

    with open(QURAN_PATH) as f:
        corpus = json.load(f)

    taxonomy = {}
    for sid in OATH_CLUSTER:
        s = next(s for s in corpus if s["id"] == sid)
        verses = [(v["id"], v["text"]) for v in s["verses"]]
        n_wa, n_fa, elements = count_oath_particles(verses)
        taxonomy[sid] = {
            "name_ar": s["name"],
            "transliteration": s["transliteration"],
            "n_wa": n_wa,
            "n_fa": n_fa,
            "n_total": n_wa + n_fa,
            "elements": [{"particle": p, "verse": v, "token": t} for p, v, t in elements]
        }

    # H1 — Q 89 has 4 wa-elements (and 0 fa)
    q89_n_wa = taxonomy[89]["n_wa"]
    q89_n_fa = taxonomy[89]["n_fa"]
    h1_pass = (q89_n_wa == 4 and q89_n_fa == 0)

    # H2 — META-OATH closing: scan ALL surahs (corpus-wide) for the
    # rhetorical *hal fī dhālika qasamun li-X* form.
    pat = re.compile(normalize(r"هل\s+في\s+ذلك\s+قسم"))
    h2_hits = []
    for s in corpus:
        for v in s["verses"]:
            if pat.search(normalize(v["text"])):
                h2_hits.append({"surah": s["id"], "verse": v["id"], "text": v["text"]})
    h2_pass = (len(h2_hits) == 1 and h2_hits[0]["surah"] == 89 and h2_hits[0]["verse"] == 5)

    if h1_pass and h2_pass:
        verdict = "CONFIRMED"
    elif h1_pass or h2_pass:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    out = {
        "test_id": "Q089-F-03",
        "prereg_sha256": PREREG_SHA,
        "seed": SEED,
        "h1": {
            "q89_n_wa": q89_n_wa,
            "q89_n_fa": q89_n_fa,
            "pre_locked_direction": "Q 89 = 4 wa, 0 fa",
            "pass": h1_pass
        },
        "h2": {
            "pattern_regex": r"هل\s+في\s+ذلك\s+قسم",
            "n_corpus_occurrences": len(h2_hits),
            "hits": h2_hits,
            "pass": h2_pass
        },
        "taxonomy": taxonomy,
        "summary_table": [
            {"surah": sid,
             "name": taxonomy[sid]["transliteration"],
             "n_wa": taxonomy[sid]["n_wa"],
             "n_fa": taxonomy[sid]["n_fa"],
             "n_total": taxonomy[sid]["n_total"]}
            for sid in OATH_CLUSTER
        ],
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "verdict": verdict
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"VERDICT: {verdict}")
    print("\nTaxonomy of H-NEW-1070 oath-cluster (n_wa, n_fa, total):")
    for row in out["summary_table"]:
        print(f"  Q {row['surah']:3d} {row['name']:<14}  wa={row['n_wa']:2d}  fa={row['n_fa']:2d}  total={row['n_total']:2d}")
    print(f"\nQ 89: n_wa={q89_n_wa}, n_fa={q89_n_fa}; H1 pass={h1_pass}")
    print(f"META-OATH closing pattern hits: {len(h2_hits)} ({h2_hits}); H2 pass={h2_pass}")


if __name__ == "__main__":
    main()
