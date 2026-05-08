#!/usr/bin/env python3
"""
Q033 novel-findings runner — Q033-F-01..F-05.

Pre-reg SHAs locked at top.  fail-fast on mismatch.
"""

import json
import hashlib
import os
import random
import re
import sys
from collections import Counter

BASE = "/Users/grey/Downloads/quran"

PREREG_SHAS = {
    "Q033-F-01": "f5310dd00d323c21b902f04324238aa2ba082c2e3d95552c5e84aaaf8bfb652b",
    "Q033-F-02": "57cdc302068c03d3d7b6a12f9ed5dba722f390cb9b612a6431236f0cfde48a63",
    "Q033-F-03": "7ccfd983c97c34b692dd2a4469ac974e756628fc306139082f42c29e3af1e2bf",
    "Q033-F-04": "6665a12ef7d3626036aec78871d0479a56bb4ec35994dd4ab71a821efccf2a6d",
    "Q033-F-05": "7e0633691e733885161e220cfdf4c5f5f18eb4bbc219a828f48f9a9e7e7d7e93",
}

PREREG_DIR = os.path.join(BASE, "surahs/Q033-al-ahzab/preregs")
PREREG_FILES = {
    "Q033-F-01": "Q033-F-01-alif-monorhyme-prereg.md",
    "Q033-F-02": "Q033-F-02-position-test-prereg.md",
    "Q033-F-03": "Q033-F-03-hijab-cohesion-prereg.md",
    "Q033-F-04": "Q033-F-04-amana-distinctness-prereg.md",
    "Q033-F-05": "Q033-F-05-wives-cluster-prereg.md",
}


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_preregs():
    for tid, fname in PREREG_FILES.items():
        actual = sha256_file(os.path.join(PREREG_DIR, fname))
        expected = PREREG_SHAS[tid]
        assert actual == expected, f"SHA mismatch for {tid}: actual={actual} expected={expected}"
    print(f"[OK] All {len(PREREG_FILES)} pre-reg SHAs verified.", file=sys.stderr)


# ---------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------

TASHKEEL = re.compile(r"[ً-ٰٟۖ-ۭـ]")  # tashkeel + tatweel + Quran marks
ARABIC_LETTER = re.compile(r"[ء-غف-يٱ-ۓ]")


def load_quran(variant="no"):
    p = {"no": "quran-text/quran-no-tashkeel.json",
         "min": "quran-text/quran-min-tashkeel.json"}[variant]
    return json.load(open(os.path.join(BASE, p), encoding="utf-8"))


def strip_tashkeel(text):
    return TASHKEEL.sub("", text)


def last_letter(text):
    """Return the last Arabic letter character of a verse, ignoring tashkeel/marks/whitespace/punct."""
    t = strip_tashkeel(text)
    # Remove pause marks ۖ ۚ ۗ ۛ ۜ ۘ ۙ ۝ ۞ etc.
    t = re.sub(r"[ۖ-ۿ\s\.,!\?]", "", t)
    for ch in reversed(t):
        if ARABIC_LETTER.match(ch):
            return ch
    return None


def tokens(text):
    t = strip_tashkeel(text)
    # split on whitespace
    return [w for w in re.split(r"\s+", t) if w and ARABIC_LETTER.search(w)]


def jaccard(a, b):
    A = set(a)
    B = set(b)
    if not A and not B:
        return 1.0
    if not A or not B:
        return 0.0
    return len(A & B) / len(A | B)


# ---------------------------------------------------------------------
# Q033-F-01: alif-monorhyme purity
# ---------------------------------------------------------------------

ALIF_FINALS = {"ا", "آ", "أ", "إ", "ى", "ٰ"}  # ا آ أ إ ى ٰ


def run_F01():
    q = load_quran("min")
    rates = {}
    for s in q:
        sid = s["id"]
        verses = s["verses"]
        # For Q1, classical convention: basmala counted as v.1 (we follow the JSON's structure).
        n = len(verses)
        alif_n = 0
        for v in verses:
            ll = last_letter(v["text"])
            if ll in ALIF_FINALS:
                alif_n += 1
        rates[sid] = {
            "alif_final_n": alif_n,
            "n_verses": n,
            "alif_final_rate": alif_n / n,
            "name": s["transliteration"],
            "type": s["type"],
        }
    # rank
    sorted_by_rate = sorted(rates.items(), key=lambda kv: (-kv[1]["alif_final_rate"], kv[0]))
    rank_of_q33 = next(i + 1 for i, (sid, _) in enumerate(sorted_by_rate) if sid == 33)
    top10 = [
        {"rank": i + 1, "surah": sid, **rates[sid]}
        for i, (sid, _) in enumerate(sorted_by_rate[:15])
    ]

    # cross-corpus poetry baseline
    poetry_files = [
        "muallaqa-amr-bin-kulthum.txt",
        "muallaqa-antara.txt",
        "muallaqa-harith.txt",
        "muallaqa-imru-al-qais.txt",
        "muallaqa-labid.txt",
        "muallaqa-tarafa.txt",
    ]
    poetry_rates = {}
    raw_dir = os.path.join(BASE, "data/baseline-corpora/raw")
    for pf in poetry_files:
        path = os.path.join(raw_dir, pf)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            text = f.read()
        # split on newlines as line/verse boundaries; drop empties
        lines = [ln.strip() for ln in text.splitlines() if ln.strip() and len(ln.strip()) > 5]
        if not lines:
            continue
        alif_n = 0
        n = 0
        for ln in lines:
            # In a qaṣīda, each *bayt* hemistich often shares the rāwī.  We take last letter of each line.
            ll = last_letter(ln)
            if ll is not None:
                n += 1
                if ll in ALIF_FINALS:
                    alif_n += 1
        if n > 0:
            poetry_rates[pf] = {"n_lines": n, "alif_final_n": alif_n, "alif_final_rate": alif_n / n}

    out = {
        "id": "Q033-F-01",
        "rules_tuple": "(min-tashkeel, last-letter, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "q33_rank": rank_of_q33,
        "q33": rates[33],
        "top15_quran": top10,
        "poetry_baseline_per_text": poetry_rates,
        "verdict": "VINDICATED" if rank_of_q33 == 1 else (
            "TIED-VINDICATION" if rates[sorted_by_rate[0][0]]["alif_final_rate"] == rates[33]["alif_final_rate"] else
            "DIRECTIONAL" if rank_of_q33 <= 3 else "FALSIFIED"
        ),
    }
    return out


# ---------------------------------------------------------------------
# Q033-F-02: Q33:40 word-midpoint test
# ---------------------------------------------------------------------

def run_F02():
    q = load_quran("no")
    q33 = [s for s in q if s["id"] == 33][0]
    word_counts = [len(tokens(v["text"])) for v in q33["verses"]]
    total = sum(word_counts)
    cum = []
    s = 0
    for w in word_counts:
        s += w
        cum.append(s)
    cum_pos = [c / total for c in cum]  # cum_pos[i] = fraction up to and INCLUDING verse i+1
    # rank verses by |cum_pos − 0.5|
    distances = [(i + 1, abs(cp - 0.5)) for i, cp in enumerate(cum_pos)]
    distances_sorted = sorted(distances, key=lambda kv: kv[1])
    rank_v40 = next(i + 1 for i, (vno, _) in enumerate(distances_sorted) if vno == 40)
    cum_pos_v40 = cum_pos[39]
    out = {
        "id": "Q033-F-02",
        "total_words": total,
        "n_verses": 73,
        "verse_index_midpoint": 40 / 73,
        "cum_pos_v40": cum_pos_v40,
        "abs_diff_from_half_v40": abs(cum_pos_v40 - 0.5),
        "rank_v40_by_proximity_to_word_midpoint": rank_v40,
        "top5_closest_to_midpoint": [
            {"verse": vno, "abs_diff": d, "cum_pos": cum_pos[vno - 1]}
            for vno, d in distances_sorted[:5]
        ],
        "verdict": (
            "VINDICATION" if abs(cum_pos_v40 - 0.5) < 0.05 else
            "DIRECTIONAL-TIE-RANK" if rank_v40 <= 5 else
            "FALSIFICATION" if abs(cum_pos_v40 - 0.5) > 0.10 else
            "RULES-TUPLE-FRAGILE"
        ),
    }
    return out


# ---------------------------------------------------------------------
# Q033-F-03: hijab-cluster cohesion (permutation null)
# ---------------------------------------------------------------------

def cohesion_jaccard(token_sets):
    sets = [set(ts) for ts in token_sets]
    n = len(sets)
    if n < 2:
        return None
    s = 0.0
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            A, B = sets[i], sets[j]
            if not A and not B:
                jac = 1.0
            elif not A or not B:
                jac = 0.0
            else:
                jac = len(A & B) / len(A | B)
            s += jac
            pairs += 1
    return s / pairs


def run_F03():
    q = load_quran("no")
    q33 = [s for s in q if s["id"] == 33][0]
    verse_tokens = {v["id"]: tokens(v["text"]) for v in q33["verses"]}
    HIJAB = [28, 29, 30, 31, 32, 33, 34, 53, 59]
    obs = cohesion_jaccard([verse_tokens[v] for v in HIJAB])

    rng = random.Random(20260428)
    n_perm = 10000
    all_verse_ids = list(verse_tokens.keys())
    n_ge = 0
    sample_cohesions = []
    for _ in range(n_perm):
        smp = rng.sample(all_verse_ids, len(HIJAB))
        c = cohesion_jaccard([verse_tokens[v] for v in smp])
        sample_cohesions.append(c)
        if c >= obs:
            n_ge += 1
    p = (n_ge + 1) / (n_perm + 1)
    mean = sum(sample_cohesions) / n_perm
    out = {
        "id": "Q033-F-03",
        "hijab_set": HIJAB,
        "observed_cohesion": obs,
        "perm_n": n_perm,
        "perm_p": p,
        "perm_mean_cohesion": mean,
        "perm_max_cohesion": max(sample_cohesions),
        "verdict": (
            "VINDICATED" if p < 0.05 else
            "FALSIFIED" if p > 0.50 else
            "RULES-TUPLE-FRAGILE/NULL"
        ),
    }
    return out


# ---------------------------------------------------------------------
# Q033-F-04: amāna verse distinctness
# ---------------------------------------------------------------------

def run_F04():
    q = load_quran("no")
    q33 = [s for s in q if s["id"] == 33][0]
    verse_tokens = {v["id"]: tokens(v["text"]) for v in q33["verses"]}
    distinct = {}
    for vid, toks in verse_tokens.items():
        # mean Jaccard over other verses
        s = 0.0
        n = 0
        ts = set(toks)
        for vid2, toks2 in verse_tokens.items():
            if vid2 == vid:
                continue
            ts2 = set(toks2)
            if not ts and not ts2:
                jac = 1.0
            elif not ts or not ts2:
                jac = 0.0
            else:
                jac = len(ts & ts2) / len(ts | ts2)
            s += jac
            n += 1
        distinct[vid] = 1 - (s / n)

    sorted_d = sorted(distinct.items(), key=lambda kv: -kv[1])
    rank_v72 = next(i + 1 for i, (vid, _) in enumerate(sorted_d) if vid == 72)

    # Length-controlled distinctness: linear regression of distinctness on word-count, residual
    word_counts = {vid: len(verse_tokens[vid]) for vid in verse_tokens}
    n = len(distinct)
    xs = [word_counts[vid] for vid in distinct]
    ys = [distinct[vid] for vid in distinct]
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    num = sum((xs[i] - mean_x) * (ys[i] - mean_y) for i in range(n))
    den = sum((xs[i] - mean_x) ** 2 for i in range(n))
    slope = num / den if den != 0 else 0
    intercept = mean_y - slope * mean_x
    residuals = {vid: distinct[vid] - (intercept + slope * word_counts[vid]) for vid in distinct}
    sorted_r = sorted(residuals.items(), key=lambda kv: -kv[1])
    rank_v72_residual = next(i + 1 for i, (vid, _) in enumerate(sorted_r) if vid == 72)

    out = {
        "id": "Q033-F-04",
        "n_verses": 73,
        "v72_distinctness": distinct[72],
        "v72_word_count": word_counts[72],
        "v72_distinctness_rank_raw": rank_v72,
        "v72_distinctness_rank_length_controlled": rank_v72_residual,
        "top10_distinct_verses_raw": [{"verse": vid, "distinct": d} for vid, d in sorted_d[:10]],
        "top10_distinct_verses_residual": [{"verse": vid, "residual": r} for vid, r in sorted_r[:10]],
        "verdict_raw": "VINDICATED" if rank_v72 <= 8 else ("FALSIFIED" if rank_v72 > 30 else "DIRECTIONAL"),
        "verdict_length_controlled": "VINDICATED" if rank_v72_residual <= 8 else ("FALSIFIED" if rank_v72_residual > 30 else "DIRECTIONAL"),
    }
    return out


# ---------------------------------------------------------------------
# Q033-F-05: wives-cluster vs other Medinan-legal clusters
# ---------------------------------------------------------------------

def get_verse_tokens(q, surah_id, verse_ids):
    s = [x for x in q if x["id"] == surah_id][0]
    out = []
    for v in s["verses"]:
        if v["id"] in verse_ids:
            out.append(tokens(v["text"]))
    return out


def run_F05():
    q = load_quran("no")
    clusters = {
        "Q33:28-34 (wives-of-Prophet)": (33, list(range(28, 35))),
        "Q2:280-283 (debt)": (2, list(range(280, 284))),
        "Q4:11-14 (inheritance)": (4, list(range(11, 15))),
        "Q65:1-7 (divorce)": (65, list(range(1, 8))),
        "Q24:2-9 (zinā/liʿān)": (24, list(range(2, 10))),
    }
    results = {}
    for name, (sid, vids) in clusters.items():
        ts = get_verse_tokens(q, sid, vids)
        coh = cohesion_jaccard(ts)
        results[name] = {"cohesion": coh, "n_verses": len(ts), "surah": sid, "verses": vids}

    sorted_clusters = sorted(results.items(), key=lambda kv: -kv[1]["cohesion"])
    wives_rank = next(i + 1 for i, (name, _) in enumerate(sorted_clusters) if name.startswith("Q33:28-34"))
    out = {
        "id": "Q033-F-05",
        "clusters": results,
        "ranking_by_cohesion": [{"rank": i + 1, "name": name, "cohesion": r["cohesion"]} for i, (name, r) in enumerate(sorted_clusters)],
        "wives_cluster_rank": wives_rank,
        "verdict": (
            "VINDICATED" if wives_rank == 1 else
            "DIRECTIONAL" if wives_rank == 2 else
            "FALSIFIED" if wives_rank >= 4 else
            "RULES-TUPLE-FRAGILE"
        ),
    }
    return out


# ---------------------------------------------------------------------
# Position-test bonus: word-count + divine-attribute density of Q33:40, :56, :72
# (for classical-claim audit)
# ---------------------------------------------------------------------

def divine_attribute_density():
    q = load_quran("no")
    # asma-al-husna list
    names = []
    with open(os.path.join(BASE, "data/asma-al-husna.txt"), encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            names.append(ln)
    # Map each name's CONSONANTAL-no-tashkeel form to a search token (strip definite article ال optionally)
    name_norms = set()
    for nm in names:
        nm_n = strip_tashkeel(nm)
        name_norms.add(nm_n)
        if nm_n.startswith("ال"):
            name_norms.add(nm_n[2:])
    # For each verse compute count of token-matches & density
    out = {}
    for s in q:
        for v in s["verses"]:
            toks = tokens(v["text"])
            divine_n = sum(1 for t in toks if t in name_norms)
            density = divine_n / max(1, len(toks))
            out[(s["id"], v["id"])] = {"n_tokens": len(toks), "divine_n": divine_n, "density": density}
    return out


def classical_claim_q33_v40_v56_v72(div_density):
    # Word-count + divine-density rank of v40, v56, v72 vs all 6,236 verses
    all_verses = list(div_density.items())
    # Rank by divine_density (descending)
    sorted_by_density = sorted(all_verses, key=lambda kv: (-kv[1]["density"], kv[0]))
    rank = {}
    for i, ((sid, vid), info) in enumerate(sorted_by_density):
        rank[(sid, vid)] = i + 1
    out = {}
    for vid in [40, 56, 72]:
        info = div_density[(33, vid)]
        out[f"Q33:{vid}"] = {
            "n_tokens": info["n_tokens"],
            "divine_attribute_count": info["divine_n"],
            "divine_attribute_density": info["density"],
            "density_rank_among_6236": rank[(33, vid)],
        }
    return out


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

if __name__ == "__main__":
    verify_preregs()

    out_dir = os.path.join(BASE, "surahs/Q033-al-ahzab/csv")
    os.makedirs(out_dir, exist_ok=True)

    f01 = run_F01()
    json.dump(f01, open(os.path.join(out_dir, "Q033-F-01.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"[F-01] Q33 alif-final-rate rank: {f01['q33_rank']}/114; verdict: {f01['verdict']}")
    print(f"        Q33: {f01['q33']['alif_final_rate']:.4f} ({f01['q33']['alif_final_n']}/{f01['q33']['n_verses']})")

    f02 = run_F02()
    json.dump(f02, open(os.path.join(out_dir, "Q033-F-02.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"[F-02] cum_pos(v40)={f02['cum_pos_v40']:.4f}; |diff from 0.5|={f02['abs_diff_from_half_v40']:.4f}; rank={f02['rank_v40_by_proximity_to_word_midpoint']}; verdict: {f02['verdict']}")

    f03 = run_F03()
    json.dump(f03, open(os.path.join(out_dir, "Q033-F-03.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"[F-03] hijab cohesion={f03['observed_cohesion']:.4f} (rand mean={f03['perm_mean_cohesion']:.4f}, p={f03['perm_p']:.4f}); verdict: {f03['verdict']}")

    f04 = run_F04()
    json.dump(f04, open(os.path.join(out_dir, "Q033-F-04.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"[F-04] v72 distinctness rank: raw={f04['v72_distinctness_rank_raw']}/73; length-ctrl={f04['v72_distinctness_rank_length_controlled']}/73; verdict-raw: {f04['verdict_raw']}, verdict-residual: {f04['verdict_length_controlled']}")

    f05 = run_F05()
    json.dump(f05, open(os.path.join(out_dir, "Q033-F-05.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"[F-05] wives cluster rank: {f05['wives_cluster_rank']}/5; verdict: {f05['verdict']}")
    for r in f05["ranking_by_cohesion"]:
        print(f"        {r['rank']}. {r['name']}: cohesion={r['cohesion']:.4f}")

    # Classical-claim audit support
    dd = divine_attribute_density()
    classical = classical_claim_q33_v40_v56_v72(dd)
    json.dump(classical, open(os.path.join(out_dir, "Q033-divine-density-v40-v56-v72.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    for k, v in classical.items():
        print(f"[CLASSICAL-AUDIT] {k}: words={v['n_tokens']}, divine_n={v['divine_attribute_count']}, density={v['divine_attribute_density']:.3f}, rank={v['density_rank_among_6236']}/6236")
