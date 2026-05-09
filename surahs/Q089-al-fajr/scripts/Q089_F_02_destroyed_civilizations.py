#!/usr/bin/env python3
"""
Q089-F-02 — Q 89:6-14 destroyed-civilizations catalog root-overlap.
Pre-reg SHA256 lock: a0fbb868280cb29041ee8cab845a0f0197dbdcdc93a67c9ec67ccd7e9ee1d438
Seed: 20260509
"""
import json
import hashlib
import re
import sys
import random
from pathlib import Path
from collections import Counter
import math

PREREG_PATH = Path(__file__).resolve().parent.parent / "preregs" / "Q089-F-02-destroyed-civilizations-prereg.md"
PREREG_SHA = "a0fbb868280cb29041ee8cab845a0f0197dbdcdc93a67c9ec67ccd7e9ee1d438"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "csv" / "Q089-F-02.json"
SEED = 20260509
N_PERM = 10000

QURAN_PATH = "/Users/grey/Downloads/quran/data/alt-text/quran-uthmani-consonantal.json"
QAC_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"


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


def load_qac_roots():
    """Return dict {(surah, verse): list[root] (Buckwalter)}, allowing duplicates so
    Counter-based bag-of-roots is meaningful."""
    out = {}
    with open(QAC_PATH, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]  # (s:v:w:p)
            features = parts[3]
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)", loc)
            if not m:
                continue
            s, v = int(m.group(1)), int(m.group(2))
            for feat in features.split("|"):
                if feat.startswith("ROOT:"):
                    root = feat[5:]
                    out.setdefault((s, v), []).append(root)
    return out


def block_root_bag(qac_roots, sid, vstart, vend):
    """Return Counter of roots over [sid:vstart .. sid:vend]."""
    c = Counter()
    for v in range(vstart, vend + 1):
        for r in qac_roots.get((sid, v), []):
            c[r] += 1
    return c


def cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    keys = set(a) | set(b)
    dot = sum(a[k] * b[k] for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def all_blocks_of_size(corpus, n_verses, exclude_block=None):
    """Yield (sid, vstart, vend) for all contiguous n_verses spans."""
    out = []
    for s in corpus:
        sid = s["id"]
        nv = s["total_verses"]
        for vs in range(1, nv - n_verses + 2):
            ve = vs + n_verses - 1
            block = (sid, vs, ve)
            if exclude_block and block == exclude_block:
                continue
            out.append(block)
    return out


def main():
    verify_sha()
    random.seed(SEED)

    with open(QURAN_PATH) as f:
        corpus = json.load(f)

    qac_roots = load_qac_roots()

    # Q 89 block
    q89_block = (89, 6, 14)
    q89_bag = block_root_bag(qac_roots, *q89_block)

    # Reference blocks
    ref_blocks = {
        "Q7:65-102 (Hūd-ʿĀd through Pharaoh-Mūsā)": (7, 65, 102),
        "Q11:25-99 (Nūḥ through Pharaoh)": (11, 25, 99),
        "Q26:105-191 (Nūḥ through Shuʿayb)": (26, 105, 191)
    }
    ref_bags = {n: block_root_bag(qac_roots, *blk) for n, blk in ref_blocks.items()}
    ref_cosines = {n: cosine(q89_bag, b) for n, b in ref_bags.items()}
    ref_mean = sum(ref_cosines.values()) / len(ref_cosines)

    # Control blocks (non-prophet-narrative, locked in pre-reg)
    ctrl_blocks = {
        "Q56:1-9": (56, 1, 9),
        "Q87:1-9": (87, 1, 9),
        "Q92:1-9": (92, 1, 9)
    }
    ctrl_bags = {n: block_root_bag(qac_roots, *blk) for n, blk in ctrl_blocks.items()}
    ctrl_cosines = {n: cosine(q89_bag, b) for n, b in ctrl_bags.items()}
    ctrl_mean = sum(ctrl_cosines.values()) / len(ctrl_cosines)

    # H1 — perm-null over random 9-verse spans (mean-cos to 3 reference blocks)
    all_9_blocks = all_blocks_of_size(corpus, 9, exclude_block=q89_block)
    null_means = []
    sample = random.sample(all_9_blocks, min(N_PERM, len(all_9_blocks)))
    for blk in sample:
        bag = block_root_bag(qac_roots, *blk)
        if not bag:
            null_means.append(0.0)
            continue
        m = sum(cosine(bag, b) for b in ref_bags.values()) / len(ref_bags)
        null_means.append(m)
    n_ge = sum(1 for x in null_means if x >= ref_mean)
    p_h1 = n_ge / len(null_means) if null_means else 1.0

    # H2 — reference vs control mean
    h2_diff = ref_mean - ctrl_mean

    # H3 — corpus-wide 4-proper-noun joint signature scan
    PN_PATTERNS = ["عاد", "إرم", "ثمود", "فرعون"]
    PN_NORM = [normalize(p) for p in PN_PATTERNS]

    def block_text_normalized(sid, vstart, vend):
        s = next(s for s in corpus if s["id"] == sid)
        return " ".join(normalize(v["text"]) for v in s["verses"] if vstart <= v["id"] <= vend)

    # Scan all 9-verse spans corpus-wide for joint presence of the 4 PNs;
    # exclude any span overlapping Q 89:6-14 (the target block).
    matches = []
    for blk in all_blocks_of_size(corpus, 9):
        sid, vs, ve = blk
        if sid == 89 and not (ve < 6 or vs > 14):
            continue  # exclude any window overlapping the target
        text = block_text_normalized(sid, vs, ve)
        if all(pn in text for pn in PN_NORM):
            matches.append(list(blk))
    h3_pass = (len(matches) == 0)

    # Sub-test passes
    h1_pass = p_h1 < 0.01667
    h2_pass = h2_diff > 0

    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass >= 2:
        verdict = "CONFIRMED"
    elif n_pass == 1:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"
    if h2_diff < 0:
        verdict += " (PRE-COMMIT-VIOLATION on H2)"

    out = {
        "test_id": "Q089-F-02",
        "prereg_sha256": PREREG_SHA,
        "seed": SEED,
        "n_perm": len(null_means),
        "h1": {
            "ref_mean_cosine": ref_mean,
            "ref_cosines_per_block": ref_cosines,
            "null_mean_of_means": sum(null_means) / max(1, len(null_means)),
            "null_max": max(null_means) if null_means else 0,
            "perm_p_one_sided": p_h1,
            "alpha_bon": 0.01667,
            "pass": h1_pass
        },
        "h2": {
            "ref_mean": ref_mean,
            "ctrl_mean": ctrl_mean,
            "ctrl_cosines_per_block": ctrl_cosines,
            "ref_minus_ctrl": h2_diff,
            "pass": h2_pass
        },
        "h3": {
            "proper_nouns": PN_PATTERNS,
            "n_other_9verse_blocks_with_all_4_PNs": len(matches),
            "matches": matches,
            "pass": h3_pass
        },
        "bonferroni_k": 3,
        "alpha_bon": 0.01667,
        "verdict": verdict
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"VERDICT: {verdict}")
    print(json.dumps({k: v for k, v in out.items() if k not in ()}, ensure_ascii=False, indent=2)[:3000])


if __name__ == "__main__":
    main()
