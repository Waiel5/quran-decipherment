#!/usr/bin/env python3
"""H-NEW-2310 — Refrain / exact-repeated-verse structure.

Two deliverables:
  (1) CENSUS  — every normalized verse-string appearing >=2x in the corpus
                (intra- and cross-surah), with global count, intra-surah max,
                full (surah:ayah) positions, plus near-exact (edit-ratio >=0.90)
                supplement.  Descriptive, no p-value.
  (2) SPACING — for every (surah, refrain) pair where a string repeats >=4x in
                a surah, test whether the refrain occurrences are spaced MORE
                REGULARLY (lower gap-variance) than a uniform-random placement of
                m dividers among the surah's N verses.  Direction LOCKED: V_obs
                lower than null.  One-sided left-tail, 10000 perms, Bonferroni-k.

Pre-reg:  findings/phase-b-hypotheses/prereg-h-new-2310-refrain-structure.md
SHA-256:  6e4a571eea280ff83774659aa65845323730ddffd7e139ff0fe27b4661086935
Rules-tuple: (no-tashkeel, orthographic-token verse-string, NFC+ws-collapsed,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""

import hashlib
import json
import random
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median, pvariance, mean, pstdev

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-2310-refrain-structure.md"
EXPECTED_SHA = "6e4a571eea280ff83774659aa65845323730ddffd7e139ff0fe27b4661086935"
QURAN_NO = ROOT / "quran-text/quran-no-tashkeel.json"
QURAN_MIN = ROOT / "quran-text/quran-min-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-2310.json"
SEED = 20260509
SEED2 = 20260530
N_PERM = 10_000
REFRAIN_MIN = 4  # >=4 occurrences in a surah enters the inferential family


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}...")


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    return " ".join(s.split())


def edit_ratio(a: str, b: str) -> float:
    """Normalized Levenshtein similarity ratio in [0,1] (1 = identical)."""
    if a == b:
        return 1.0
    la, lb = len(a), len(b)
    if la == 0 or lb == 0:
        return 0.0
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        ca = a[i - 1]
        for j in range(1, lb + 1):
            cost = 0 if ca == b[j - 1] else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)
        prev = cur
    dist = prev[lb]
    return 1.0 - dist / max(la, lb)


def gap_variance(positions):
    gaps = [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]
    return pvariance(gaps), gaps


def cv_of_gaps(gaps):
    m = mean(gaps)
    if m == 0:
        return 0.0
    return pstdev(gaps) / m


def spacing_test(N, positions, seed, n_perm=N_PERM):
    """One-sided LEFT-tail (V_obs lower => more regular). Returns dict."""
    m = len(positions)
    v_obs, gaps_obs = gap_variance(positions)
    cv_obs = cv_of_gaps(gaps_obs)
    rng = random.Random(seed)
    all_pos = list(range(1, N + 1))
    le = 0           # perm variance <= observed (regularity)
    perm_vs = []
    cv_le = 0
    for _ in range(n_perm):
        draw = sorted(rng.sample(all_pos, m))
        v_perm, g_perm = gap_variance(draw)
        perm_vs.append(v_perm)
        if v_perm <= v_obs:
            le += 1
        if cv_of_gaps(g_perm) <= cv_obs:
            cv_le += 1
    p_left = (1 + le) / (n_perm + 1)
    p_cv = (1 + cv_le) / (n_perm + 1)
    null_med = median(perm_vs)
    return {
        "m": m,
        "N": N,
        "positions": positions,
        "gaps": gaps_obs,
        "v_obs": v_obs,
        "cv_obs": cv_obs,
        "null_median_v": null_med,
        "p_left_variance": p_left,
        "p_left_cv": p_cv,
        "direction_locked_met": v_obs < null_med,
    }


def main() -> None:
    verify_prereg()
    text = json.loads(QURAN_NO.read_text())

    # --- load verses, build positions ---
    surah_verses = {}          # surah -> list of normalized strings (verse order)
    surah_name = {}
    global_positions = defaultdict(list)   # norm-string -> [(surah, ayah), ...]
    for e in text:
        s = int(e["id"])
        surah_name[s] = e["transliteration"]
        vs = []
        for v in e["verses"]:
            ns = normalize(v["text"])
            vs.append(ns)
            global_positions[ns].append((s, int(v["id"])))
        surah_verses[s] = vs

    # --- (1) CENSUS: every string appearing >=2x globally ---
    census = []
    for string, atts in global_positions.items():
        if len(atts) >= 2:
            by_surah = Counter(a[0] for a in atts)
            census.append({
                "string": string,
                "global_count": len(atts),
                "n_surahs": len(by_surah),
                "intra_surah_max": max(by_surah.values()),
                "attestations": [f"{s}:{a}" for (s, a) in atts],
                "type": "intra-surah" if len(by_surah) == 1 else "cross-surah",
            })
    census.sort(key=lambda d: (-d["global_count"], -d["intra_surah_max"], d["string"]))

    n_repeated_strings = len(census)
    n_intra = sum(1 for c in census if c["type"] == "intra-surah")
    n_cross = sum(1 for c in census if c["type"] == "cross-surah")

    # --- (2) family: (surah, refrain) pairs with intra-surah count >= REFRAIN_MIN ---
    family = []  # ordered, family_index used for deterministic per-pair seeding
    for s in range(1, 115):
        vs = surah_verses[s]
        N = len(vs)
        c = Counter(vs)
        for string, cnt in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])):
            if cnt >= REFRAIN_MIN:
                positions = [i + 1 for i, t in enumerate(vs) if t == string]
                family.append({"surah": s, "string": string, "count": cnt,
                               "N": N, "positions": positions})
    k = len(family)
    alpha_bon = 0.05 / k if k else None

    # --- VERIFY anchor counts from disk (fail fast) ---
    q55_max = max(Counter(surah_verses[55]).values())
    q77_max = max(Counter(surah_verses[77]).values())
    q54_max = max(Counter(surah_verses[54]).values())
    assert q55_max == 31, f"Q55 max count expected 31, got {q55_max}"
    assert q77_max == 10, f"Q77 max count expected 10, got {q77_max}"
    assert q54_max == 4, f"Q54 max count expected 4, got {q54_max}"
    print(f"anchor counts verified: Q55={q55_max} Q77={q77_max} Q54={q54_max}")

    # --- run spacing test per family member ---
    results = []
    n_pass = n_directional = n_null = 0
    for idx, fm in enumerate(family):
        per_seed = SEED + fm["surah"] * 1000 + idx
        res = spacing_test(fm["N"], fm["positions"], per_seed)
        # verdict
        p = res["p_left_variance"]
        met = res["direction_locked_met"]
        if met and p <= alpha_bon:
            verdict = "PASS"
            n_pass += 1
        elif met and p <= 0.05:
            verdict = "DIRECTIONAL"
            n_directional += 1
        else:
            verdict = "NULL"
            n_null += 1
        cv_same_dir = res["p_left_cv"] <= 0.05 and met
        results.append({
            "surah": fm["surah"],
            "surah_name": surah_name[fm["surah"]],
            "string": fm["string"],
            "count": fm["count"],
            "verdict": verdict,
            "cv_robust": cv_same_dir,
            **res,
        })

    # --- MW-5 replication: Q55, Q77 at second seed ---
    repl = {}
    for fm in family:
        if fm["surah"] in (55, 77) and fm["count"] in (31, 10):
            r = spacing_test(fm["N"], fm["positions"], SEED2 + fm["surah"])
            repl[f"Q{fm['surah']}"] = {
                "p_left_variance": r["p_left_variance"],
                "direction_locked_met": r["direction_locked_met"],
                "v_obs": r["v_obs"],
                "null_median_v": r["null_median_v"],
            }

    # --- MW-6 instrument-control: phantom refrain in Q56 (no >=4 refrain) ---
    # place m=10 random dividers among Q56's 96 verses; should sit at null median.
    q56_N = len(surah_verses[56])
    rng_ctrl = random.Random(SEED + 999999)
    ctrl_pos = sorted(rng_ctrl.sample(range(1, q56_N + 1), 10))
    ctrl = spacing_test(q56_N, ctrl_pos, SEED + 555)
    control = {
        "surah": 56, "N": q56_N, "m": 10, "positions": ctrl_pos,
        "p_left_variance": ctrl["p_left_variance"],
        "v_obs": ctrl["v_obs"], "null_median_v": ctrl["null_median_v"],
        "passes_falsely": ctrl["p_left_variance"] <= (alpha_bon or 0.05),
    }

    # --- near-exact supplement (MW-7 capped) on the >=4 refrain strings vs all repeated ---
    # surface refrains differing by a single particle: among census strings, pairs with
    # 0.90 <= ratio < 1.0 .  Restrict left side to family refrain strings to keep tractable.
    near_exact = []
    family_strings = {fm["string"] for fm in family}
    repeated_strings = [c["string"] for c in census]
    for fs in family_strings:
        for rs in repeated_strings:
            if rs == fs:
                continue
            r = edit_ratio(fs, rs)
            if r >= 0.90:
                near_exact.append({"a": fs, "b": rs, "ratio": round(r, 4)})
    near_exact.sort(key=lambda d: -d["ratio"])

    # --- rules-tuple sensitivity: anchors on min-tashkeel ---
    text_min = json.loads(QURAN_MIN.read_text())
    min_max = {}
    for e in text_min:
        s = int(e["id"])
        if s in (55, 77, 54):
            cc = Counter(normalize(v["text"]) for v in e["verses"])
            min_max[s] = max(cc.values())
    rules_tuple_note = {
        "q55_no_tashkeel": q55_max, "q55_min_tashkeel": min_max.get(55),
        "q77_no_tashkeel": q77_max, "q77_min_tashkeel": min_max.get(77),
        "q54_no_tashkeel": q54_max, "q54_min_tashkeel": min_max.get(54),
    }

    out = {
        "id": "H-NEW-2310",
        "prereg_sha256": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, orthographic-token verse-string, NFC+ws-collapsed, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "census_summary": {
            "n_repeated_strings": n_repeated_strings,
            "n_intra_surah_repeated": n_intra,
            "n_cross_surah_repeated": n_cross,
            "n_surahs_with_intra_repeat": len({a[0] for c in census if c["type"] == "intra-surah" for a in [tuple(x.split(":")) for x in c["attestations"][:1]]}),
        },
        "census": census,
        "near_exact_supplement": near_exact,
        "spacing_family": {
            "k": k,
            "alpha_bonferroni": alpha_bon,
            "n_pass": n_pass,
            "n_directional": n_directional,
            "n_null": n_null,
            "results": results,
        },
        "replication_seed2": repl,
        "instrument_control_q56": control,
        "rules_tuple_sensitivity": rules_tuple_note,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"\ncensus: {n_repeated_strings} repeated strings "
          f"({n_intra} intra-surah, {n_cross} cross-surah)")
    print(f"spacing family k={k}, alpha_bon={alpha_bon:.6f}")
    print(f"  PASS={n_pass}  DIRECTIONAL={n_directional}  NULL={n_null}")
    for r in results:
        print(f"  Q{r['surah']:>3} {r['surah_name']:<14} m={r['count']:>2} "
              f"V_obs={r['v_obs']:.3f} null_med={r['null_median_v']:.3f} "
              f"p={r['p_left_variance']:.4f} cv_robust={r['cv_robust']} -> {r['verdict']}")
    print(f"\nMW-5 replication seed2: {repl}")
    print(f"MW-6 control Q56 passes_falsely={control['passes_falsely']} "
          f"(p={control['p_left_variance']:.4f})")
    print(f"rules-tuple sensitivity: {rules_tuple_note}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
