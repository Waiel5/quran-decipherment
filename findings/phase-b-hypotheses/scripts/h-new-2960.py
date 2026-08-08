#!/usr/bin/env python3
"""H-NEW-2960: the spatial-deixis census, and whether proximal/distal tracks this-world vs Hereafter.

Two deliverables, deliberately separated (prereg §0):
  1. The proximal/distal census over QAC POS:DEM. Documentary; no null model.
  2. A verse-clustered permutation test of deixis x topical frame. Prereg §§3-9.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-2960.py
      python3 findings/phase-b-hypotheses/scripts/h-new-2960.py --self-check
"""

import argparse
import hashlib
import json
import math
import os
import platform
import random
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# Prereg §9 — embedded literals, verified at runtime; mismatch aborts before any run directory.
EXPECTED_PREREG_SHA = "bb7934bd69f8a8d283b44b70fc7fd472fbd291496ab09f38d0fca0db92bc430e"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"

SEED_PRIMARY = 20260509
SEED_REPLICATION = 20260519
N_DRAWS = 200_000

TESTS_IN_FAMILY = 3  # prereg §7 — C1, C2, C3
ALPHA_BONFERRONI = 0.05 / TESTS_IN_FAMILY
NOVELTY_GATE = 0.005

LOCATION_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")

# Prereg §2 — the deixis rule, as a function. Addressee-kaf enclitic, anchored to end of FORM.
KAF_KHITAB_RE = re.compile(r"(?:ka|ki|kumo|kumu|kumaA|kum|kun~a)$")

# Prereg §2 — the independent lemma partition, used ONLY as a check on the regex.
LEMMA_PROXIMAL = {"ha`*aA", "*aA", "ha`*a`n", "ha`tayon", "hunaA", "ha`ka*aA"}
LEMMA_DISTAL = {"*a`lik", ">uwla`^}ik", ">uwlaA^'", "tilokum", "*a`nik"}

# Prereg §4.1 — the closed antonym pair. Two lemma strings, and nothing else.
LEM_ESCH = "A^xir"
LEM_DUNYA = "d~unoyaA"
ESCH_RESTRICTED_PREFIX = "'aAxirap"  # prereg §4.1 sensitivity S1: feminine-singular form class

# Prereg §4.2 — generated lexicon
LEXICON_POS = ("N", "PN", "ADJ", "V")
DIRICHLET_ALPHA0 = 100.0
K_VALUES = (25, 50)  # C2, C3

D3_M_VALUES = (1, 2, 3, 5, 10)  # prereg §3


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_output(repo_root, *args):
    try:
        return subprocess.run(
            ["git", *args], cwd=repo_root, capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception:
        return None


# --------------------------------------------------------------------------------------
# Instrument
# --------------------------------------------------------------------------------------

def load_qac(path):
    """Rows of (surah, verse, word, segment, form, tag, features)."""
    rows = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            match = LOCATION_RE.match(parts[0])
            if not match:
                continue
            s, v, w, g = (int(x) for x in match.groups())
            rows.append(
                {"s": s, "v": v, "w": w, "g": g, "form": parts[1], "tag": parts[2], "feat": parts[3]}
            )
    return rows


def lemma_of(features):
    match = re.search(r"LEM:([^|]*)", features)
    return match.group(1) if match else None


def pos_of(features):
    match = re.search(r"POS:(\w+)", features)
    return match.group(1) if match else None


def deixis_of(form):
    """Prereg §2 — the registered rule."""
    return "DISTAL" if KAF_KHITAB_RE.search(form) else "PROXIMAL"


# --------------------------------------------------------------------------------------
# Deliverable 1 — the census (prereg §0: documentary, no null model)
# --------------------------------------------------------------------------------------

def build_census(rows):
    dem = [r for r in rows if "POS:DEM" in r["feat"]]
    by_word = defaultdict(list)
    for r in rows:
        by_word[(r["s"], r["v"], r["w"])].append(r)

    inventory = Counter()
    for r in dem:
        inventory[(deixis_of(r["form"]), lemma_of(r["feat"]), r["form"])] += 1

    # Independent check: lemma partition vs regex partition (prereg §2).
    disagreements = []
    for r in dem:
        lem = lemma_of(r["feat"])
        by_lemma = "PROXIMAL" if lem in LEMMA_PROXIMAL else ("DISTAL" if lem in LEMMA_DISTAL else None)
        if by_lemma is None or by_lemma != deixis_of(r["form"]):
            disagreements.append({"loc": f"({r['s']}:{r['v']}:{r['w']}:{r['g']})",
                                  "form": r["form"], "lemma": lem,
                                  "by_regex": deixis_of(r["form"]), "by_lemma": by_lemma})

    # Prefix profile of DEM-bearing words.
    prefixes = Counter()
    ka_prefixed = 0
    for r in dem:
        pres = [x for x in by_word[(r["s"], r["v"], r["w"])] if x["g"] < r["g"]]
        tags = tuple(x["feat"].split("|")[1] if x["feat"].startswith("PREFIX|") else x["feat"]
                     for x in pres)
        prefixes[tags] += 1
        if any("ka+" in x["feat"] for x in pres):
            ka_prefixed += 1

    inl_surahs = sorted({r["s"] for r in rows if "POS:INL" in r["feat"]})

    return {
        "n_segments_total": len(rows),
        "n_dem_segments": len(dem),
        "n_proximal": sum(1 for r in dem if deixis_of(r["form"]) == "PROXIMAL"),
        "n_distal": sum(1 for r in dem if deixis_of(r["form"]) == "DISTAL"),
        "inventory": [
            {"deixis": d, "lemma": lem, "form": f, "n": n}
            for (d, lem, f), n in sorted(inventory.items(), key=lambda kv: (-kv[1], kv[0]))
        ],
        "lemma_partition_disagreements": disagreements,
        "prefix_profile": [{"prefixes": list(k), "n": n} for k, n in prefixes.most_common()],
        "n_ka_prefixed": ka_prefixed,
        "n_verses_with_dem": len({(r["s"], r["v"]) for r in dem}),
        "n_surahs_with_dem": len({r["s"] for r in dem}),
        "inl_surahs": inl_surahs,
        "n_inl_surahs": len(inl_surahs),
        "feature_strings_matched": {
            "inventory": "FEATURES contains literal substring 'POS:DEM'",
            "deixis_rule": KAF_KHITAB_RE.pattern + "   (match against FORM)",
            "esch_marker_C1": f"LEM:{LEM_ESCH}",
            "esch_marker_S1": f"LEM:{LEM_ESCH} and FORM startswith {ESCH_RESTRICTED_PREFIX!r}",
            "dunya_marker": f"LEM:{LEM_DUNYA}",
            "muqattaat_rule": "surah contains a segment whose FEATURES contains 'POS:INL'",
        },
    }, dem, by_word


# --------------------------------------------------------------------------------------
# Deliverable 2 — frames
# --------------------------------------------------------------------------------------

def c1_frames(rows, restricted):
    """Prereg §4.1. Returns dict (s,v) -> 'ESCH' | 'DUNYA' for classified verses only."""
    esch, dunya = set(), set()
    for r in rows:
        lem = lemma_of(r["feat"])
        if lem == LEM_ESCH and (not restricted or r["form"].startswith(ESCH_RESTRICTED_PREFIX)):
            esch.add((r["s"], r["v"]))
        elif lem == LEM_DUNYA:
            dunya.add((r["s"], r["v"]))
    frames = {}
    for key in esch - dunya:
        frames[key] = "ESCH"
    for key in dunya - esch:
        frames[key] = "DUNYA"
    return frames


def build_lexicon(rows, seed_frames, k):
    """Prereg §4.2 — Monroe-Colaresi-Quinn informative-Dirichlet log-odds, top-k per side."""
    counts = {"ESCH": Counter(), "DUNYA": Counter()}
    corpus = Counter()
    for r in rows:
        if pos_of(r["feat"]) not in LEXICON_POS:
            continue
        lem = lemma_of(r["feat"])
        if lem is None or lem in (LEM_ESCH, LEM_DUNYA):
            continue
        corpus[lem] += 1
        frame = seed_frames.get((r["s"], r["v"]))
        if frame:
            counts[frame][lem] += 1

    total_corpus = sum(corpus.values())
    n_e, n_d = sum(counts["ESCH"].values()), sum(counts["DUNYA"].values())
    scores = {}
    for lem in set(counts["ESCH"]) | set(counts["DUNYA"]):
        a0 = DIRICHLET_ALPHA0 * corpus[lem] / total_corpus
        y_e, y_d = counts["ESCH"][lem], counts["DUNYA"][lem]
        # guard: an all-zero prior mass would divide by zero; corpus[lem] >= 1 here so a0 > 0.
        d_e = math.log((y_e + a0) / (n_e + DIRICHLET_ALPHA0 - y_e - a0))
        d_d = math.log((y_d + a0) / (n_d + DIRICHLET_ALPHA0 - y_d - a0))
        var = 1.0 / (y_e + a0) + 1.0 / (y_d + a0)
        scores[lem] = (d_e - d_d) / math.sqrt(var)

    ranked = sorted(scores.items(), key=lambda kv: kv[1])
    return {"ESCH": {lem for lem, _ in ranked[-k:]},
            "DUNYA": {lem for lem, _ in ranked[:k]},
            "top_esch": [[lem, round(z, 4)] for lem, z in ranked[-k:][::-1]],
            "top_dunya": [[lem, round(z, 4)] for lem, z in ranked[:k]]}


def lexicon_frames(rows, lexicon):
    """Prereg §4.2 step 5."""
    tally = defaultdict(lambda: [0, 0])
    for r in rows:
        if pos_of(r["feat"]) not in LEXICON_POS:
            continue
        lem = lemma_of(r["feat"])
        if lem in lexicon["ESCH"]:
            tally[(r["s"], r["v"])][0] += 1
        elif lem in lexicon["DUNYA"]:
            tally[(r["s"], r["v"])][1] += 1
    frames = {}
    for key, (e, d) in tally.items():
        if e > d:
            frames[key] = "ESCH"
        elif d > e:
            frames[key] = "DUNYA"
    return frames


# --------------------------------------------------------------------------------------
# Deliverable 2 — the test
# --------------------------------------------------------------------------------------

def contingency(tokens, frames):
    """2x2 as a dict; rows = deixis, cols = frame."""
    table = {"PROXIMAL": {"DUNYA": 0, "ESCH": 0}, "DISTAL": {"DUNYA": 0, "ESCH": 0}}
    for t in tokens:
        frame = frames.get((t["s"], t["v"]))
        if frame:
            table[deixis_of(t["form"])][frame] += 1
    return table


def odds_ratio(table):
    a = table["DISTAL"]["ESCH"]
    b = table["DISTAL"]["DUNYA"]
    c = table["PROXIMAL"]["ESCH"]
    d = table["PROXIMAL"]["DUNYA"]
    if b == 0 or c == 0:
        return None if (a == 0 or d == 0) else float("inf")
    return (a * d) / (b * c)


def fisher_one_sided_upper(table):
    """P(X >= a) under the hypergeometric, conditioning on both margins."""
    a = table["DISTAL"]["ESCH"]
    b = table["DISTAL"]["DUNYA"]
    c = table["PROXIMAL"]["ESCH"]
    d = table["PROXIMAL"]["DUNYA"]
    row1, row2, col1 = a + b, c + d, a + c
    total = row1 + row2
    if total == 0:
        return None
    lo, hi = max(0, col1 - row2), min(row1, col1)
    denom = math.comb(total, col1)
    return sum(math.comb(row1, x) * math.comb(row2, col1 - x) for x in range(a, hi + 1)) / denom


EXACT_DP_STATE_CAP = 20_000_000


def exact_subset_p(values, n_choose, observed):
    """Exact P(S* >= observed) when S* is the sum of a uniform size-n_choose subset.

    Dynamic programme over the multiset, in exact Python integers. Returns None when the
    state space is too large; the Monte-Carlo permutation then stands alone.
    """
    total = sum(values)
    if n_choose == 0 or n_choose == len(values):
        return 1.0
    if len(values) * n_choose * (total + 1) > EXACT_DP_STATE_CAP:
        return None
    # counts[j][s] = number of size-j subsets summing to s
    counts = [[0] * (total + 1) for _ in range(n_choose + 1)]
    counts[0][0] = 1
    for value in values:
        for j in range(min(n_choose, len(values)) - 1, -1, -1):
            row, nxt = counts[j], counts[j + 1]
            for s in range(total - value, -1, -1):
                if row[s]:
                    nxt[s + value] += row[s]
    final = counts[n_choose]
    return sum(final[observed:]) / sum(final)


def permutation_test(tokens, frames, seed, n_draws):
    """Prereg §5 — permute frame labels ACROSS VERSES; tokens travel with their verse.

    Implemented as a batched uniform permutation of the verse labels. `numpy.Generator.permuted`
    shuffles each row independently, so each row is one draw of the registered null.
    """
    import numpy as np

    verses = sorted({(t["s"], t["v"]) for t in tokens if (t["s"], t["v"]) in frames})
    if not verses:
        return None
    distal = Counter()
    for t in tokens:
        key = (t["s"], t["v"])
        if key in frames and deixis_of(t["form"]) == "DISTAL":
            distal[key] += 1
    distal_per_verse = [distal[key] for key in verses]
    labels = [frames[key] for key in verses]
    n_esch = labels.count("ESCH")
    observed = sum(n for n, lab in zip(distal_per_verse, labels) if lab == "ESCH")

    values = np.asarray(distal_per_verse, dtype=np.int32)
    rng = np.random.default_rng(seed)
    ge, done = 0, 0
    batch = max(1, min(20_000, n_draws))
    while done < n_draws:
        take = min(batch, n_draws - done)
        tiled = np.tile(values, (take, 1))
        sums = rng.permuted(tiled, axis=1)[:, :n_esch].sum(axis=1)
        ge += int((sums >= observed).sum())
        done += take

    return {
        "n_verses": len(verses),
        "n_esch_verses": n_esch,
        "n_dunya_verses": len(verses) - n_esch,
        "observed_S": observed,
        "null_mean_S": round(sum(distal_per_verse) * n_esch / len(verses), 4),
        "n_ge": ge,
        "p": (1 + ge) / (1 + n_draws),
        "exact_p": exact_subset_p(distal_per_verse, n_esch, observed),
        "seed": seed,
        "n_draws": n_draws,
    }


def run_arm(name, tokens, frames, seed, n_draws=N_DRAWS):
    table = contingency(tokens, frames)
    n = sum(v for row in table.values() for v in row.values())
    perm = permutation_test(tokens, frames, seed, n_draws) if n else None
    return {
        "arm": name,
        "n_tokens": n,
        "table": table,
        "odds_ratio": odds_ratio(table),
        "fisher_one_sided_upper": fisher_one_sided_upper(table) if n else None,
        "permutation": perm,
    }


def phrase_types(dem, rows):
    """Prereg §3 D3 — (DEM form, next word's first STEM form), ranked corpus-wide."""
    stems = defaultdict(list)
    for r in rows:
        if "STEM" in r["feat"]:
            stems[(r["s"], r["v"], r["w"])].append(r)
    types = {}
    counts = Counter()
    for r in dem:
        nxt = stems.get((r["s"], r["v"], r["w"] + 1))
        follower = min(nxt, key=lambda x: x["g"])["form"] if nxt else "∅"
        key = (r["form"], follower)
        types[(r["s"], r["v"], r["w"], r["g"])] = key
        counts[key] += 1
    return types, counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    prereg = repo_root / "findings/phase-b-hypotheses/prereg-h-new-2960-spatial-deixis.md"
    qac = repo_root / "data/morphology/quranic-corpus-morphology-0.4.txt"

    prereg_sha, qac_sha = sha256(prereg), sha256(qac)
    if prereg_sha != EXPECTED_PREREG_SHA:
        sys.exit(f"ABORT: prereg SHA mismatch\n  expected {EXPECTED_PREREG_SHA}\n  got      {prereg_sha}")
    if qac_sha != EXPECTED_QAC_SHA:
        sys.exit(f"ABORT: QAC SHA mismatch\n  expected {EXPECTED_QAC_SHA}\n  got      {qac_sha}")

    rows = load_qac(qac)
    census, dem, _ = build_census(rows)

    if args.self_check:
        assert census["n_dem_segments"] == 1059, census["n_dem_segments"]
        assert census["n_proximal"] + census["n_distal"] == 1059
        assert not census["lemma_partition_disagreements"]
        assert census["n_inl_surahs"] == 29
        # Fisher against a hand-checkable 2x2: a=3,b=1,c=1,d=3 -> P(X>=3) = (16+1)/70
        t = {"DISTAL": {"ESCH": 3, "DUNYA": 1}, "PROXIMAL": {"ESCH": 1, "DUNYA": 3}}
        assert abs(fisher_one_sided_upper(t) - 17 / 70) < 1e-12, fisher_one_sided_upper(t)
        assert abs(odds_ratio(t) - 9.0) < 1e-12
        assert deixis_of("ha`ka*aA") == "PROXIMAL" and deixis_of("*a`lika") == "DISTAL"
        assert deixis_of("ha`^&ulaA^'i") == "PROXIMAL" and deixis_of(">uw@la`^}ikumo") == "DISTAL"
        print("self-check OK — census 1059 =", census["n_proximal"], "prox +",
              census["n_distal"], "distal; 0 lemma disagreements; 29 INL surahs")
        return

    # ---- token sets: the full inventory and the four registered robustness arms (prereg §3)
    by_word = defaultdict(list)
    for r in rows:
        by_word[(r["s"], r["v"], r["w"])].append(r)
    inl_surahs = set(census["inl_surahs"])
    ptypes, pcounts = phrase_types(dem, rows)
    ranked_types = [t for t, _ in pcounts.most_common()]

    def key_of(r):
        return (r["s"], r["v"], r["w"], r["g"])

    ka_set = {key_of(r) for r in dem
              if any("ka+" in x["feat"] for x in by_word[(r["s"], r["v"], r["w"])] if x["g"] < r["g"])}
    open_set = {key_of(r) for r in dem if r["s"] in inl_surahs and r["v"] <= 3}

    token_sets = {"FULL": dem,
                  "D1_no_muqattaat_openings": [r for r in dem if key_of(r) not in open_set],
                  "D2_no_ka_prefixed": [r for r in dem if key_of(r) not in ka_set],
                  "D4_no_openings_no_ka": [r for r in dem
                                           if key_of(r) not in open_set and key_of(r) not in ka_set]}
    for m in D3_M_VALUES:
        drop = set(ranked_types[:m])
        token_sets[f"D3_drop_top{m}_phrase_types"] = [r for r in dem if ptypes[key_of(r)] not in drop]

    # ---- frames
    frames = {"C1": c1_frames(rows, restricted=False),
              "S1_restricted": c1_frames(rows, restricted=True)}
    seed_frames = frames["C1"]
    lexicons = {}
    for k in K_VALUES:
        lexicons[k] = build_lexicon(rows, seed_frames, k)
        frames[f"C{2 if k == 25 else 3}_k{k}"] = lexicon_frames(rows, lexicons[k])

    # ---- registered primary family + robustness arms
    results = {"primary_family": {}, "robustness": {}, "replication": {}}
    for fname in ("C1", "C2_k25", "C3_k50"):
        results["primary_family"][fname] = run_arm(f"{fname}|FULL", dem, frames[fname], SEED_PRIMARY)
        results["replication"][fname] = run_arm(f"{fname}|FULL", dem, frames[fname], SEED_REPLICATION)
    results["sensitivity_S1"] = run_arm("S1_restricted|FULL", dem, frames["S1_restricted"], SEED_PRIMARY)

    for fname in ("C1", "C2_k25", "C3_k50"):
        for tname, toks in token_sets.items():
            if tname == "FULL":
                continue
            results["robustness"][f"{fname}|{tname}"] = run_arm(f"{fname}|{tname}", toks,
                                                                frames[fname], SEED_PRIMARY)

    # ---- registered Screen-B diagnostic (prereg §6): verse length by frame
    words_per_verse = Counter()
    for r in rows:
        words_per_verse[(r["s"], r["v"])] = max(words_per_verse[(r["s"], r["v"])], r["w"])
    length_diag = {}
    for fname in ("C1", "C2_k25", "C3_k50"):
        eligible = {(t["s"], t["v"]) for t in dem if (t["s"], t["v"]) in frames[fname]}
        for lab in ("ESCH", "DUNYA"):
            vs = [words_per_verse[v] for v in eligible if frames[fname][v] == lab]
            length_diag[f"{fname}_{lab}"] = {"n_verses": len(vs),
                                             "mean_words": round(sum(vs) / len(vs), 3) if vs else None}

    # ---- verdict, per the locked logic (prereg §7)
    c1 = results["primary_family"]["C1"]
    c1_p = c1["permutation"]["p"]
    c1_passes = c1_p < ALPHA_BONFERRONI
    d3m5 = results["robustness"]["C1|D3_drop_top5_phrase_types"]
    d3m5_passes = d3m5["permutation"]["p"] < ALPHA_BONFERRONI if d3m5["permutation"] else False
    direction_ok = c1["permutation"]["observed_S"] > c1["permutation"]["null_mean_S"]
    if not direction_ok and not c1_passes:
        verdict = "NULL"
    elif c1_passes and d3m5_passes:
        verdict = "CONFIRMED"
    elif c1_passes:
        verdict = "CONFIRMED-BUT-FORMULAIC"
    else:
        verdict = "NULL"
    secondary_pass = all(results["primary_family"][f]["permutation"]["p"] < ALPHA_BONFERRONI
                         for f in ("C2_k25", "C3_k50"))

    # ---- write once, into a fresh immutable directory (prereg §9)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo_root / "findings/phase-b-hypotheses/runs/h-new-2960" / run_id
    os.makedirs(run_dir, exist_ok=False)

    payload = {
        "hypothesis": "H-NEW-2960",
        "census": census,
        "phrase_types_top20": [{"dem_form": t[0], "next_form": t[1], "n": n}
                               for t, n in pcounts.most_common(20)],
        "token_set_sizes": {k: len(v) for k, v in token_sets.items()},
        "frame_coverage": {k: {"n_verses_classified": len(v),
                               "n_esch": sum(1 for x in v.values() if x == "ESCH"),
                               "n_dunya": sum(1 for x in v.values() if x == "DUNYA")}
                           for k, v in frames.items()},
        "lexicons": {str(k): {"top_esch": v["top_esch"], "top_dunya": v["top_dunya"]}
                     for k, v in lexicons.items()},
        "results": results,
        "length_diagnostic": length_diag,
        "gates": {"alpha_bonferroni": ALPHA_BONFERRONI, "tests_in_family": TESTS_IN_FAMILY,
                  "novelty_gate": NOVELTY_GATE},
        "verdict": {"headline": verdict, "c1_p": c1_p, "c1_passes_gate": c1_passes,
                    "direction_as_locked": direction_ok,
                    "d3_m5_passes_gate": d3m5_passes,
                    "secondary_C2_and_C3_both_pass": secondary_pass,
                    "novelty_gate_met": min(1.0, TESTS_IN_FAMILY * c1_p) < NOVELTY_GATE},
    }
    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)

    manifest = {
        "hypothesis": "H-NEW-2960",
        "run_id": run_id,
        "run_directory": str(run_dir.relative_to(repo_root)),
        "script": str(Path(__file__).resolve().relative_to(repo_root)),
        "prereg": str(prereg.relative_to(repo_root)),
        "prereg_sha256": prereg_sha,
        "inputs": [{"path": str(qac.relative_to(repo_root)), "sha256": qac_sha}],
        "git_commit": git_output(repo_root, "rev-parse", "HEAD"),
        "git_status_porcelain": git_output(repo_root, "status", "--porcelain"),
        "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION},
        "n_draws": N_DRAWS,
        "python": sys.version,
        "platform": platform.platform(),
        "utc": datetime.now(timezone.utc).isoformat(),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)

    print(json.dumps({"run_dir": str(run_dir.relative_to(repo_root)),
                      "census": {"n_dem": census["n_dem_segments"],
                                 "proximal": census["n_proximal"],
                                 "distal": census["n_distal"]},
                      "verdict": payload["verdict"]}, indent=2))


if __name__ == "__main__":
    main()
