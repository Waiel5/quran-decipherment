#!/usr/bin/env python3
"""H-NEW-2710: title-density re-test against a topicality-matched null.

Runner only. Emits no interpretation. See
findings/phase-b-hypotheses/prereg-h-new-2710-title-density-retest.md
"""

import argparse
import hashlib
import json
import platform
import random
import re
import statistics
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# --- prereg §3.1 -----------------------------------------------------------
EXPECTED_PREREG_SHA = "c9d91fe656383016139271759c65ca7b306e3bc7fd0ee9054bd8f7beed100fc2"
EXPECTED_1820_SHA = "1a6282e451c1ff1d1cb5c0362fdfa22b6145a06bb286f66aa02a600987ea0842"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_QURAN_SHA = "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"

# --- prereg §4/§5 ----------------------------------------------------------
N_PERM = 10_000
TESTS_IN_FAMILY = 6
ALPHA_BON = 0.05 / TESTS_IN_FAMILY            # 0.008333
CORRECTED_GATE = 0.005
RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY   # 0.000833
SEED_NULL_B = 20260509
SEED_NULL_A = 20260510
REPLICATION_OFFSET = 10
# prereg §4.2: deterministic widening ladder, minimum candidate pool
WIDEN_LADDER = (2, 4, 8)
MIN_CANDIDATES = 5
RANK_K = (1, 2, 3, 5, 10, 20, 50)
LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")

# prereg §4.4: locked directions. True = observed greater than null.
LOCKED_GREATER = {"S1_rank1_count": True, "S2_median_rank": False, "S3_mrr": True}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def require(path, expected, label):
    actual = sha256(path)
    if actual != expected:
        raise SystemExit(f"ABORT: {label} SHA-256 mismatch\n  path={path}\n"
                         f"  expected={expected}\n  actual  ={actual}")
    return actual


def main():
    global N_PERM
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--perms", type=int, default=N_PERM)
    ap.add_argument("--out", default=None, help="SMOKE runs only")
    args = ap.parse_args()
    N_PERM = args.perms
    smoke = (N_PERM != 10_000)
    repo = Path(args.repo).resolve()
    rel = {"prereg": "findings/phase-b-hypotheses/prereg-h-new-2710-title-density-retest.md",
           "titles": "findings/phase-b-hypotheses/csv/h-new-1820.json",
           "qac": "data/morphology/quranic-corpus-morphology-0.4.txt",
           "quran": "quran-text/quran-no-tashkeel.json",
           "script": "findings/phase-b-hypotheses/scripts/h-new-2710.py"}
    P = {k: repo / v for k, v in rel.items()}
    hashes = {"prereg": require(P["prereg"], EXPECTED_PREREG_SHA, "prereg"),
              "h_new_1820_json": require(P["titles"], EXPECTED_1820_SHA, "h-new-1820.json"),
              "qac_v04": require(P["qac"], EXPECTED_QAC_SHA, "QAC"),
              "quran_no_tashkeel": require(P["quran"], EXPECTED_QURAN_SHA, "quran"),
              "script": sha256(P["script"])}

    res = {"id": "H-NEW-2710", "SMOKE_RUN": smoke, "prereg_sha256": hashes["prereg"],
           "n_perm": N_PERM, "tests_in_family": TESTS_IN_FAMILY,
           "alpha_bonferroni": ALPHA_BON, "raw_gate": RAW_GATE,
           "corrected_gate": CORRECTED_GATE,
           "seeds": {"null_b": SEED_NULL_B, "null_a": SEED_NULL_A,
                     "replication_offset": REPLICATION_OFFSET},
           "replaces": "H-NEW-1820 (Pillar 4)",
           "prior_art": "H-NEW-2680 D4 (20 draws, descriptive, per-STEM-root-token metric)"}

    # ---- corpus -----------------------------------------------------------
    quran = json.load(open(P["quran"], encoding="utf-8"))
    words = {s["id"]: sum(len(v["text"].split()) for v in s["verses"]) for s in quran}
    verses = {s["id"]: len(s["verses"]) for s in quran}
    SIDS = sorted(words)

    root_surah = defaultdict(Counter)
    with open(P["qac"], encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) != 4:
                continue
            m = LOC_RE.fullmatch(f[0])
            if not m:
                continue
            rm = re.search(r"(?:^|\|)ROOT:([^|]+)", f[3])
            if rm:
                root_surah[rm.group(1)][int(m[1])] += 1
    freq = {r: sum(c.values()) for r, c in root_surah.items()}
    disp = {r: len(c) for r, c in root_surah.items()}
    roots_in = defaultdict(set)
    for r, c in root_surah.items():
        for s in c:
            roots_in[s].add(r)

    # ---- prereg §3.2: the three metrics; T1 per-word density is primary ----
    DENOM = {"T1_per_word": words, "T2_raw_count": None, "T3_per_verse": verses}

    def ranks_for(root, metric):
        c = root_surah.get(root, {})
        d = DENOM[metric]
        val = {s: (c.get(s, 0) if d is None else c.get(s, 0) / d[s]) for s in SIDS}
        return val

    def rank_of(root, sid, metric):
        """prereg §3.3: rank = 1 + #{strictly greater}."""
        val = ranks_for(root, metric)
        v = val[sid]
        return 1 + sum(1 for s in SIDS if val[s] > v)

    # ---- prereg §3.4: eponymous set, verbatim ------------------------------
    t1820 = json.load(open(P["titles"], encoding="utf-8"))
    PAIRS = [(r["sid"], r["root"], r["title"]) for r in t1820["title_density_results"]]
    excluded = sorted(set(SIDS) - set(p[0] for p in PAIRS))
    res["eponymous_set"] = {
        "n": len(PAIRS), "source": rel["titles"] + " title_density_results[].{sid,root}",
        "taken_verbatim": True, "excluded_surahs": excluded, "n_excluded": len(excluded),
        "selection_rule_note": "H-NEW-1820 states al-Suyuti Itqan naw 22, minus 12 personal "
                               "names, 4 muqattaat, and unmapped; 9 of 25 exclusions are "
                               "not itemised there and could not be reproduced (prereg 3.4)",
        "all_title_roots_in_qac": all(r in freq for _, r, _ in PAIRS)}

    # ---- reproduction audit vs published ranks -----------------------------
    pub = {r["sid"]: r["title_density_rank"] for r in t1820["title_density_results"]}
    mine_t1 = {sid: rank_of(root, sid, "T1_per_word") for sid, root, _ in PAIRS}
    diffs = [{"sid": s, "published": pub[s], "recomputed": mine_t1[s]}
             for s in pub if pub[s] != mine_t1[s]]
    res["reproduction_audit"] = {
        "n_match": len(pub) - len(diffs), "n_total": len(pub), "discrepancies": diffs,
        "note": "prereg 3.4: Q112 published rank 112 is an error under the stated tie "
                "convention; 0 xlS tokens and 17 surahs with density>0 gives rank 18"}

    # ---- statistics (prereg §4.1) -----------------------------------------
    def stats(rank_list):
        n = len(rank_list)
        return {"S1_rank1_count": sum(1 for r in rank_list if r == 1),
                "S2_median_rank": statistics.median(rank_list),
                "S3_mrr": sum(1.0 / r for r in rank_list) / n}

    def rank_curve(rank_list):
        return {str(k): sum(1 for r in rank_list if r <= k) for k in RANK_K}

    # ---- prereg §4.2: Null-B candidate pools, deterministic ----------------
    pools, tiers = {}, {}
    for sid, root, _ in PAIRS:
        f0, d0 = freq[root], disp[root]
        pool = roots_in[sid] - {root}
        chosen, tier = None, "any"
        for m in WIDEN_LADDER:
            c = [r for r in pool
                 if f0 / m <= freq[r] <= f0 * m and d0 / m <= disp[r] <= d0 * m]
            if len(c) >= MIN_CANDIDATES:
                chosen, tier = sorted(c), f"x{m}"
                break
        if chosen is None:
            chosen = sorted(pool)
        pools[sid], tiers[sid] = chosen, tier
    res["null_b_matching"] = {
        "tier_counts": dict(Counter(tiers.values())),
        "pool_size_min": min(len(v) for v in pools.values()),
        "pool_size_median": statistics.median(len(v) for v in pools.values()),
        "pairs_with_empty_pool": [s for s, v in pools.items() if not v]}

    # ---- run one metric ----------------------------------------------------
    def run_metric(metric, pair_subset, gated):
        obs_ranks = [rank_of(root, sid, metric) for sid, root, _ in pair_subset]
        obs = stats(obs_ranks)
        out = {"n": len(pair_subset), "gated": gated, "observed": obs,
               "observed_rank_curve": rank_curve(obs_ranks),
               "observed_ranks": {sid: rank_of(root, sid, metric)
                                  for sid, root, _ in pair_subset}}
        if not gated:
            return out
        sids = [p[0] for p in pair_subset]
        roots = [p[1] for p in pair_subset]
        # precompute rank of each surah under every candidate control root
        cache = {}
        for sid in sids:
            for r in pools[sid]:
                if (r, sid) not in cache:
                    cache[(r, sid)] = rank_of(r, sid, metric)
        # Null A needs rank of each surah under every OTHER title root
        for sid in sids:
            for r in roots:
                if (r, sid) not in cache:
                    cache[(r, sid)] = rank_of(r, sid, metric)
        for nm, seed in (("null_b", SEED_NULL_B), ("null_a", SEED_NULL_A)):
            for tag, sd in [("", seed), ("_replication", seed + REPLICATION_OFFSET)]:
                rng = random.Random(sd)
                draws = {k: [] for k in LOCKED_GREATER}
                curves = []
                for _ in range(N_PERM):
                    if nm == "null_b":
                        rl = [cache[(rng.choice(pools[s]), s)] for s in sids]
                    else:
                        perm = roots[:]
                        rng.shuffle(perm)
                        rl = [cache[(r, s)] for s, r in zip(sids, perm)]
                    st = stats(rl)
                    for k in draws:
                        draws[k].append(st[k])
                    if len(curves) < 200:
                        curves.append(rank_curve(rl))
                blk = {"seed": sd}
                for k, greater in LOCKED_GREATER.items():
                    dr = draws[k]
                    o = obs[k]
                    hits = sum(1 for x in dr if x >= o) if greater else sum(1 for x in dr if x <= o)
                    p = (1 + hits) / (len(dr) + 1)
                    mu = statistics.mean(dr)
                    sd_ = statistics.pstdev(dr)
                    srt = sorted(dr)
                    blk[k] = {"null_mean": mu, "null_sd": sd_,
                              "null_q025": srt[int(0.025 * len(srt))],
                              "null_q500": srt[len(srt) // 2],
                              "null_q975": srt[min(len(srt) - 1, int(0.975 * len(srt)))],
                              "observed": o, "p_raw": p,
                              "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p),
                              "passes_gate": p < RAW_GATE,
                              "z_vs_null": (o - mu) / sd_ if sd_ > 0 else None,
                              "rate_ratio_obs_over_null_mean": (o / mu) if mu else None,
                              "rate_ratio_ci95": [o / srt[min(len(srt) - 1, int(0.975 * len(srt)))]
                                                  if srt[min(len(srt) - 1, int(0.975 * len(srt)))] else None,
                                                  o / srt[int(0.025 * len(srt))]
                                                  if srt[int(0.025 * len(srt))] else None]}
                if nm == "null_b" and tag == "":
                    blk["null_rank_curve_mean"] = {
                        str(k): statistics.mean(c[str(k)] for c in curves) for k in RANK_K}
                out[nm + tag] = blk
        # prereg §5: PASS iff direction matches lock AND both raw p < RAW_GATE
        for k, greater in LOCKED_GREATER.items():
            o = obs[k]
            mb = out["null_b"][k]["null_mean"]
            ma = out["null_a"][k]["null_mean"]
            dir_ok = ((o > mb and o > ma) if greater else (o < mb and o < ma))
            out.setdefault("verdict", {})[k] = {
                "direction_matches_lock": dir_ok,
                "PASS": bool(dir_ok and out["null_a"][k]["passes_gate"]
                             and out["null_b"][k]["passes_gate"])}
        return out

    res["T1_per_word_PRIMARY"] = run_metric("T1_per_word", PAIRS, gated=True)
    res["T2_raw_count"] = run_metric("T2_raw_count", PAIRS, gated=False)
    res["T3_per_verse"] = run_metric("T3_per_verse", PAIRS, gated=False)

    # ---- robustness (prereg §7) -------------------------------------------
    zero = [(s, r, t) for s, r, t in PAIRS if root_surah.get(r, {}).get(s, 0) == 0]
    nonzero = [p for p in PAIRS if p not in zero]
    strict = [p for p in PAIRS if tiers[p[0]] == "x2"]
    res["robustness"] = {
        "zero_attestation_pairs": [{"sid": s, "root": r, "title": t} for s, r, t in zero],
        "excl_zero_attestation": run_metric("T1_per_word", nonzero, gated=False),
        "strict_x2_matched_only": run_metric("T1_per_word", strict, gated=False),
        "per_surah": sorted(
            [{"sid": s, "title": t, "root": r, "freq": freq[r], "disp": disp[r],
              "match_tier": tiers[s], "pool": len(pools[s]),
              "rank_T1": rank_of(r, s, "T1_per_word"),
              "rank_T2": rank_of(r, s, "T2_raw_count"),
              "rank_T3": rank_of(r, s, "T3_per_verse")}
             for s, r, t in PAIRS], key=lambda x: x["rank_T1"]),
    }
    tert = sorted(PAIRS, key=lambda p: freq[p[1]])
    n3 = len(tert) // 3
    for i, lab in enumerate(("freq_low", "freq_mid", "freq_high")):
        sub = tert[i * n3:(i + 1) * n3] if i < 2 else tert[2 * n3:]
        rl = [rank_of(r, s, "T1_per_word") for s, r, _ in sub]
        res["robustness"][lab] = {"n": len(sub), **stats(rl)}
    r1 = [{"sid": s, "title": t, "root": r} for s, r, t in PAIRS
          if rank_of(r, s, "T1_per_word") == 1]
    res["robustness"]["rank1_set"] = r1
    res["robustness"]["non_rank1_count"] = len(PAIRS) - len(r1)

    res["verdict_inputs"] = res["T1_per_word_PRIMARY"]["verdict"]

    # ---- immutable run record (prereg §9) ---------------------------------
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    parent = Path(args.out) if args.out else repo / "findings/phase-b-hypotheses/runs/h-new-2710"
    outdir = parent / ts
    if outdir.exists():
        raise SystemExit(f"ABORT: run directory already exists: {outdir}")
    outdir.mkdir(parents=True)
    (outdir / "result.json").write_text(json.dumps(res, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
    try:
        commit = subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                                capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        commit = "UNAVAILABLE"
    manifest = {"id": "H-NEW-2710", "SMOKE_RUN": smoke, "utc": ts,
                "command": f"python3 {rel['script']} --repo . --perms {N_PERM}",
                "inputs_relative": rel, "git_commit": commit, "python": sys.version,
                "platform": platform.platform(), "n_perm": N_PERM,
                "seeds": res["seeds"], "sha256": hashes}
    (outdir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                          encoding="utf-8")
    print(f"run dir: {outdir}")
    print(json.dumps(res["verdict_inputs"], indent=2))


if __name__ == "__main__":
    main()
