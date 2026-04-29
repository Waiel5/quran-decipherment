"""
Q045-F-04: Q 45 al-Jāthiyah judgment-vocabulary density vs corpus.

Pre-reg SHA256: a09016bcf64d81927458d393f2da0db7c7070100f9efc09928108cde532041c2
Pre-reg path: surahs/Q045-al-jathiyah/preregs/Q045-F-04-jathiya-judgment-vocabulary-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys
import re
from collections import Counter

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/preregs/Q045-F-04-jathiya-judgment-vocabulary-prereg.md"
EXPECTED_SHA = "a09016bcf64d81927458d393f2da0db7c7070100f9efc09928108cde532041c2"
QAC_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN_NO_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/csv/Q045-F-04.json"

# Locked judgment-cluster (Buckwalter root strings as used by QAC v0.4)
# Key: Buckwalter root; Value: gloss
# Buckwalter QAC convention: ج=j, ث=v, ز=z, ي=y, ح=H, س=s, ب=b, ك=k, م=m, ق=q, د=d, ن=n, ت=t, ع=E, ر=r, ل=l, خ=x, و=w
# QAC may use different root keys; primary attempts plus fallbacks.
JUDGMENT_CLUSTER = {
    "jzy": "recompense (jzy)",
    "jvw": "kneel (jvw, jāthiya)",
    "Hsb": "reckon (Hsb)",
    "Hkm": "judge (Hkm)",
    "qDy": "decree (qDy)",
    "dyn": "religion / judgment-debt (dyn)",
    "sAE": "the-Hour (sAE)",
    "qwm": "rise / qiyāma (qwm)",
    "bTl": "vain / null (bTl)",
    "xsr": "loss (xsr)",
    "xtm": "seal (xtm)",
    "nTq": "speak (nTq)",
    "nsx": "transcribe / record (nsx)",
}
# Fallback alternates the QAC may use (we accept any of these)
ROOT_ALIASES = {
    "jvw": ["jvw", "jvy", "jvA"],   # the kneeling-root may be encoded variantly
    "qDy": ["qDy", "qDA"],
    "qwm": ["qwm"],
    "sAE": ["sAE", "sEy", "sEA"],   # al-sāʿa root
    "bTl": ["bTl"],
    "nTq": ["nTq"],
}


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def parse_qac():
    """Return (per_surah_token_total, per_surah_per_root_count, root_observed_keys)."""
    surah_tokens = Counter()
    surah_root_counts = {}  # surah -> Counter(root -> count)
    observed_roots = set()
    with open(QAC_PATH) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)", loc)
            if not m:
                continue
            surah = int(m.group(1))
            seg = int(m.group(4))
            if seg == 1:
                surah_tokens[surah] += 1
            root_match = re.search(r"ROOT:([^|]+)", features)
            if root_match:
                root = root_match.group(1)
                observed_roots.add(root)
                if surah not in surah_root_counts:
                    surah_root_counts[surah] = Counter()
                surah_root_counts[surah][root] += 1
    return surah_tokens, surah_root_counts, observed_roots


def get_total_verses():
    with open(QURAN_NO_TASHKEEL) as f:
        qd = json.load(f)
    return {s["id"]: s["total_verses"] for s in qd}


def main():
    verify_prereg()
    surah_tokens, surah_root_counts, observed_roots = parse_qac()
    total_verses = get_total_verses()

    # Resolve each cluster root to the actual key in QAC (try aliases)
    cluster_keys_resolved = {}
    for root in JUDGMENT_CLUSTER:
        candidates = ROOT_ALIASES.get(root, [root])
        chosen = None
        for c in candidates:
            if c in observed_roots:
                chosen = c
                break
        cluster_keys_resolved[root] = chosen  # may be None if absent

    # Per-surah judgment density
    densities = {}
    per_surah_breakdown = {}
    for s in range(1, 115):
        toks = surah_tokens.get(s, 0)
        if toks == 0:
            densities[s] = 0.0
            continue
        rc = surah_root_counts.get(s, Counter())
        total_judgment = 0
        breakdown = {}
        for root, resolved in cluster_keys_resolved.items():
            if resolved is None:
                breakdown[root] = 0
                continue
            cnt = rc.get(resolved, 0)
            breakdown[root] = cnt
            total_judgment += cnt
        densities[s] = (total_judgment / toks) * 1000
        per_surah_breakdown[s] = {
            "tokens": toks,
            "judgment_count": total_judgment,
            "density_per_1000": round(densities[s], 4),
            "by_root": breakdown,
        }

    # Q 45 stats
    q45 = per_surah_breakdown[45]

    # Rank by density
    ranked = sorted(densities.items(), key=lambda kv: -kv[1])
    rank_q45 = next(i + 1 for i, (s, _) in enumerate(ranked) if s == 45)

    # Length-filtered subset n_verses ∈ [25, 60]
    filt = [s for s in range(1, 115) if 25 <= total_verses.get(s, 0) <= 60]
    filt_ranked = sorted([(s, densities[s]) for s in filt], key=lambda kv: -kv[1])
    rank_q45_filt = next((i + 1 for i, (s, _) in enumerate(filt_ranked) if s == 45), None)

    # Verdict
    h1_pass = rank_q45 <= 28
    h1b_pass = rank_q45_filt is not None and rank_q45_filt <= 11
    if rank_q45 > 86:
        verdict = "PRECOMMIT_VIOLATION"
    elif h1_pass and h1b_pass:
        verdict = "VINDICATED"
    elif h1_pass and not h1b_pass:
        verdict = "PARTIAL_VINDICATION_H1_ONLY"
    else:
        verdict = "NULL"

    out = {
        "prereg_id": "Q045-F-04",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260428,
        "rules_tuple": "(no-tashkeel, QAC-stem-roots-v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "judgment_cluster": JUDGMENT_CLUSTER,
        "cluster_keys_resolved": cluster_keys_resolved,
        "Q45_stats": q45,
        "Q45_rank_corpus_density": rank_q45,
        "Q45_rank_length_filtered_25_60": rank_q45_filt,
        "filter_subset_size": len(filt),
        "h1_threshold": 28,
        "h1_pass": h1_pass,
        "h1b_threshold": 11,
        "h1b_pass": h1b_pass,
        "top_10_judgment_density": [(int(s), round(d, 4)) for s, d in ranked[:10]],
        "top_10_in_filtered_subset": [(int(s), round(d, 4)) for s, d in filt_ranked[:10]],
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
