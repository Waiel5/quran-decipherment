#!/usr/bin/env python3
"""H-NEW-3000: the reception-residual rosters -- per-verse structure against formal hadith reception.

Cross findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv (per-verse structural
profile, 6,236 verses) against findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv
(per-verse formal hadith reception weight, from the full 50,884-record corpus).

THE TWO ROSTERS ARE THE DELIVERABLE and are written to disk BEFORE any inference is computed.
That ordering is prereg section 7 and is registered, not cosmetic.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3000-reception-residual-rosters.md
Expected verdict: NULL (prereg section 6.2).

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3000.py
"""

import csv
import hashlib
import json
import math
import os
import platform
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.stats import rankdata, t as tdist

REPO = Path(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")))
os.chdir(REPO)

# --------------------------------------------------------------------------------------
# Prereg section 1 -- embedded literals, verified at runtime. A mismatch aborts BEFORE any
# run directory is created.
# --------------------------------------------------------------------------------------
PREREG = "findings/phase-b-hypotheses/prereg-h-new-3000-reception-residual-rosters.md"
EXPECTED_PREREG_SHA = "6515fe1a12ebf742e3ab72d5c6e18e8c5a82d1c0a4f4fd894aa9397eed344789"

PROFILE = "findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv"
DECLARATIONS = "findings/phase-b-hypotheses/csv/h-new-2990-column-declarations.csv"
WEIGHTS = "findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv"
TEXT_TASHKEEL = "quran-text/quran-full-tashkeel.json"
TEXT_PLAIN = "quran-text/quran-no-tashkeel.json"

FROZEN = {
    PROFILE: "f4ca4377fe0fe4b7bf2b1cf34f8afa8632f61427e8bcd1d393d1afe8795d90de",
    DECLARATIONS: "61f7b6d12490214abb8857a5e76b532968ee64ae6c33018e29bc23769897a3a2",
    WEIGHTS: "f6bf5f744025d65d47d6b3f4d2ba7425531e56c048e5c75baa25f85f0f0b26c0",
    TEXT_TASHKEEL: "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    TEXT_PLAIN: "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
}

SEED_PRIMARY = 20260509
SEED_REPLICATION = 20260519
N_PERM = 10000

BONFERRONI_K = 6                      # prereg section 6
ALPHA = 0.05 / BONFERRONI_K           # 0.00833333
K_PRIMARY = 10                        # prereg section 4 -- deciles, the stricter setting
K_SECONDARY = 5
ROSTER_N = 30

# prereg section 2.2 -- the composite's four members, sign-aligned. Named here because
# "structurally extreme" is not a quantity (H-NEW-2990 section 8 condition 2).
MEMBERS = [
    ("frac_hapax_root_tokens", +1, "n_root_tokens"),
    ("mean_root_surprisal_bits", +1, "(per-root-token mean; invariant)"),
    ("frac_root_tokens_freq_le5", +1, "n_root_tokens"),
    ("rime_class_size", -1, "(corpus constant; not a rate)"),
]
# prereg section 2.1 -- excluded by the declarations file's own flag. Never used as structure.
LENGTH_DOMINATED = ["sum_root_surprisal_bits", "n_root_types"]


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def die(msg):
    print("ABORT: " + msg, file=sys.stderr)
    sys.exit(2)


def say(*a):
    print(" ".join(str(x) for x in a), flush=True)


def git_output(*args):
    try:
        return subprocess.run(["git", *args], cwd=REPO, capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


# ======================================================================================
# GATE -- before anything else exists (prereg section 7 step 1)
# ======================================================================================
_prereg_sha = sha256_file(PREREG)
if _prereg_sha != EXPECTED_PREREG_SHA:
    die(f"pre-registration SHA mismatch\n  expected {EXPECTED_PREREG_SHA}\n  actual   {_prereg_sha}")
say(f"[SHA-OK] pre-registration locked: {_prereg_sha}")
for _p, _want in FROZEN.items():
    _got = sha256_file(_p)
    if _got != _want:
        die(f"frozen input mismatch {_p}\n  expected {_want}\n  actual   {_got}")
say(f"[SHA-OK] {len(FROZEN)} frozen inputs verified")


# ======================================================================================
# Statistics -- rank only. No mean of n_hadith is computed anywhere (prereg section 3.2).
# ======================================================================================
def spearman(x, y):
    rx, ry = rankdata(x), rankdata(y)
    return float(np.corrcoef(rx, ry)[0, 1])


def midrank_percentile(values):
    """(midrank - 0.5) / n, in (0,1). Ties share their mid-rank."""
    n = len(values)
    return (rankdata(values, method="average") - 0.5) / n


def partial_spearman(x, y, z):
    """First-order partial correlation on mid-ranks (prereg section 6)."""
    rxy, rxz, ryz = spearman(x, y), spearman(x, z), spearman(y, z)
    denom = math.sqrt((1.0 - rxz ** 2) * (1.0 - ryz ** 2))
    if denom == 0:
        die("degenerate partial correlation denominator")
    return (rxy - rxz * ryz) / denom


def partial_spearman_via_ols(x, y, z):
    """Same quantity by an independent route: correlate the OLS residuals of the ranks."""
    rx, ry, rz = rankdata(x), rankdata(y), rankdata(z)
    design = np.column_stack([np.ones(len(rz)), rz])
    ex = rx - design @ np.linalg.lstsq(design, rx, rcond=None)[0]
    ey = ry - design @ np.linalg.lstsq(design, ry, rcond=None)[0]
    return float(np.corrcoef(ex, ey)[0, 1])


def partial_p_values(rho, n, n_controls=1):
    """Two-sided t-test on n - 2 - n_controls df, plus the two one-sided p-values."""
    df = n - 2 - n_controls
    if abs(rho) >= 1.0:
        return 0.0, 0.0, 0.0
    stat = rho * math.sqrt(df / (1.0 - rho ** 2))
    p_two = 2.0 * tdist.sf(abs(stat), df)
    p_pos = tdist.sf(stat, df)          # P(T >= stat): evidence for rho > 0
    p_neg = tdist.cdf(stat, df)         # P(T <= stat): evidence for rho < 0
    return float(p_two), float(p_pos), float(p_neg)


def decile_bins(values, k):
    """Value-based quantile cut. Verses of EQUAL LENGTH ARE NEVER SPLIT (prereg section 4)."""
    qs = np.quantile(values, [i / k for i in range(1, k)])
    edges = sorted(set(float(q) for q in qs))
    return np.searchsorted(np.array(edges, dtype=float), values, side="left"), edges


# ======================================================================================
# Self-tests (prereg section 7 step 2)
# ======================================================================================
def self_tests():
    rng = np.random.default_rng(SEED_PRIMARY)
    worst = 0.0
    for _ in range(20):
        n = 200
        z = rng.normal(size=n)
        x = 0.7 * z + rng.normal(size=n)
        y = 0.5 * z + rng.normal(size=n)
        worst = max(worst, abs(partial_spearman(x, y, z) - partial_spearman_via_ols(x, y, z)))
    if worst > 1e-9:
        die(f"partial-Spearman identity failed against OLS residuals: max |diff| = {worst:.3e}")
    say(f"[SELFTEST] partial-Spearman == OLS-residual route on 20 datasets, max |diff| = {worst:.2e}")

    pct = midrank_percentile([5, 5, 1, 9])
    expected = np.array([(2.5 - 0.5) / 4, (2.5 - 0.5) / 4, (1 - 0.5) / 4, (4 - 0.5) / 4])
    if not np.allclose(pct, expected):
        die(f"mid-rank percentile wrong: {pct} vs {expected}")
    if not math.isclose(spearman([1, 2, 3, 4], [1, 2, 3, 4]), 1.0):
        die("spearman identity failed")
    if not math.isclose(spearman([1, 2, 3, 4], [4, 3, 2, 1]), -1.0):
        die("spearman reversal failed")
    say("[SELFTEST] mid-rank percentile and Spearman endpoints verified")


# ======================================================================================
# Load
# ======================================================================================
def normalise_plain(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s).strip())


def load():
    profile = {}
    with open(PROFILE, encoding="utf-8") as handle:
        for r in csv.DictReader(handle):
            profile[(int(r["surah"]), int(r["verse"]))] = r
    weights = {}
    with open(WEIGHTS, encoding="utf-8") as handle:
        for r in csv.DictReader(handle):
            weights[(int(r["sura"]), int(r["aya"]))] = r
    if set(profile) != set(weights):
        die("the two instruments do not join on (surah, verse)")

    tashkeel, plain = {}, {}
    for surah in json.load(open(TEXT_TASHKEEL, encoding="utf-8")):
        for v in surah["verses"]:
            tashkeel[(surah["id"], v["id"])] = v["text"]
    for surah in json.load(open(TEXT_PLAIN, encoding="utf-8")):
        for v in surah["verses"]:
            plain[(surah["id"], v["id"])] = normalise_plain(v["text"])

    # prereg section 5.3 -- repetition annotations, computed corpus-wide over all 6,236 verses
    counts = Counter(plain.values())
    first_seen, repeats, later = {}, {}, {}
    for key in sorted(plain, key=lambda k: (int(profile[k]["mushaf_index"]),)):
        txt = plain[key]
        repeats[key] = counts[txt] > 1
        later[key] = txt in first_seen
        first_seen.setdefault(txt, key)
    return profile, weights, tashkeel, plain, repeats, later


def fnum(row, col):
    v = row.get(col, "")
    return None if v == "" else float(v)


def main():
    self_tests()
    profile, weights, tashkeel, plain, repeats, later = load()

    # ---- prereg section 3.3: the analysis set. Ineligible verses are EXCLUDED, never zeroed.
    all_keys = sorted(profile, key=lambda k: int(profile[k]["mushaf_index"]))
    keys = [k for k in all_keys if weights[k]["eligible"] == "1"]
    reasons = Counter(weights[k]["ineligible_reason"] for k in all_keys if weights[k]["eligible"] != "1")
    if any(profile[k]["struct_z_composite"] == "" for k in keys):
        die("struct_z_composite undefined on part of the analysis set")
    n = len(keys)
    say(f"[SET] analysis set n = {n} eligible; {len(all_keys) - n} excluded "
        f"({dict(reasons)}) -- excluded, never zeroed")

    comp = np.array([float(profile[k]["struct_z_composite"]) for k in keys])
    nh = np.array([int(weights[k]["n_hadith"]) for k in keys], dtype=float)
    nh17 = np.array([int(weights[k]["n_hadith_all17"]) for k in keys], dtype=float)
    nbooks = np.array([int(weights[k]["n_books"]) for k in keys], dtype=float)
    nw = np.array([int(profile[k]["n_words"]) for k in keys], dtype=float)          # LOCKED length control
    nw_alt = np.array([int(weights[k]["n_words"]) for k in keys], dtype=float)      # sensitivity S1
    mushaf = np.array([int(profile[k]["mushaf_index"]) for k in keys])

    member_vals = {}
    for name, sign, _denom in MEMBERS:
        raw = np.array([fnum(profile[k], name) for k in keys], dtype=float)
        if np.isnan(raw).any():
            die(f"composite member {name} has undefined values on the analysis set")
        member_vals[name] = sign * (np.log10(raw) if name == "rime_class_size" else raw)

    # ---- prereg section 4: length deciles over the analysis set
    dec, edges = decile_bins(nw, K_PRIMARY)
    bins = []
    for b in sorted(set(dec.tolist())):
        m = nw[dec == b]
        bins.append({"bin": int(b), "n": int((dec == b).sum()),
                     "words_min": int(m.min()), "words_max": int(m.max()),
                     "n_cited": int((nh[dec == b] > 0).sum())})
    say(f"[DECILES] k = {K_PRIMARY}, {len(bins)} non-empty bins, boundaries {edges}")
    for b in bins:
        say(f"    bin {b['bin']}: n={b['n']:5d}  words {b['words_min']}-{b['words_max']}  cited={b['n_cited']}")

    # ---- prereg section 5.1: S, R, M
    S = np.zeros(n)
    R = np.zeros(n)
    for b in sorted(set(dec.tolist())):
        idx = np.where(dec == b)[0]
        S[idx] = midrank_percentile(comp[idx])
        cited = idx[nh[idx] > 0]
        if len(cited):
            R[cited] = midrank_percentile(nh[cited])
    M = S - R

    struct_rank = rankdata(-comp, method="average")       # 1 = most structurally unusual
    reception_rank = rankdata(-nh, method="average")       # 1 = most cited

    word_range = {b["bin"]: f"{b['words_min']}-{b['words_max']}" for b in bins}
    surah_name = {}
    for k in all_keys:
        surah_name[k[0]] = weights[k]["surah_name"]

    def roster_row(i):
        k = keys[i]
        return {
            "surah": k[0], "verse": k[1], "reference": f"Q {k[0]}:{k[1]}",
            "surah_name": surah_name[k[0]],
            "verse_text": tashkeel[k],
            "n_words": int(nw[i]),
            "length_decile": int(dec[i]) + 1,
            "decile_word_range": word_range[int(dec[i])],
            "struct_z_composite": round(float(comp[i]), 6),
            "struct_rank": int(round(struct_rank[i])) if struct_rank[i] == int(struct_rank[i]) else round(float(struct_rank[i]), 1),
            "S_within_decile": round(float(S[i]), 6),
            "n_hadith": int(nh[i]),
            "reception_rank": int(round(reception_rank[i])) if reception_rank[i] == int(reception_rank[i]) else round(float(reception_rank[i]), 1),
            "R_within_decile": round(float(R[i]), 6),
            "M": round(float(M[i]), 6),
            "n_books": int(nbooks[i]),
            "n_hadith_all17": int(nh17[i]),
            "driver_span": weights[k]["driver_span"],
            "frac_hapax_root_tokens": profile[k]["frac_hapax_root_tokens"],
            "mean_root_surprisal_bits": profile[k]["mean_root_surprisal_bits"],
            "frac_root_tokens_freq_le5": profile[k]["frac_root_tokens_freq_le5"],
            "rime_class_size": profile[k]["rime_class_size"],
            "text_repeats": bool(repeats[k]),
            "is_later_occurrence": bool(later[k]),
        }

    order_desc = sorted(range(n), key=lambda i: (-M[i], mushaf[i]))   # roster 1
    order_asc = sorted(range(n), key=lambda i: (M[i], mushaf[i]))     # roster 2
    roster1 = [roster_row(i) for i in order_desc[:ROSTER_N]]
    roster2 = [roster_row(i) for i in order_asc[:ROSTER_N]]

    ROSTER_COLS = list(roster1[0].keys())

    # ---- prereg section 7 step 4: the immutable run directory
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = REPO / "findings/phase-b-hypotheses/runs/h-new-3000" / run_id
    os.makedirs(run_dir, exist_ok=False)
    say(f"[RUN] {run_dir.relative_to(REPO)}")

    # ---- prereg section 7 step 5: WRITE THE ROSTERS BEFORE ANY INFERENCE
    def write_csv(path, rows, columns):
        with open(path, "x", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
            writer.writeheader()
            for r in rows:
                writer.writerow(r)

    def publish(src, dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)

    r1_path = run_dir / "roster-1-structurally-unusual-rarely-cited.csv"
    r2_path = run_dir / "roster-2-heavily-cited-structurally-ordinary.csv"
    write_csv(r1_path, roster1, ROSTER_COLS)
    write_csv(r2_path, roster2, ROSTER_COLS)
    pub1 = REPO / "findings/phase-b-hypotheses/csv/h-new-3000-roster-1-structurally-unusual-rarely-cited.csv"
    pub2 = REPO / "findings/phase-b-hypotheses/csv/h-new-3000-roster-2-heavily-cited-structurally-ordinary.csv"
    publish(r1_path, pub1)
    publish(r2_path, pub2)
    say(f"[PERSIST] roster 1 -> {pub1.relative_to(REPO)} ({len(roster1)} rows)")
    say(f"[PERSIST] roster 2 -> {pub2.relative_to(REPO)} ({len(roster2)} rows)")
    say("[PERSIST] both rosters on disk. Nothing inferential has been computed.")

    # ==================================================================================
    # prereg section 7 step 6 -- ONLY NOW the inferences
    # ==================================================================================
    inferences = {}

    def register(label, values, outcome, control, note):
        rho = partial_spearman(values, outcome, control)
        check = partial_spearman_via_ols(values, outcome, control)
        if abs(rho - check) > 1e-9:
            die(f"{label}: partial-Spearman disagreed with its OLS route ({rho} vs {check})")
        p_two, p_pos, p_neg = partial_p_values(rho, len(values))
        bare = spearman(values, outcome)
        entry = {"statistic": "partial Spearman | n_words", "note": note,
                 "bare_rho": bare, "partial_rho": rho, "p_two_sided": p_two,
                 "p_one_sided_positive": p_pos, "p_one_sided_negative": p_neg,
                 "n": len(values),
                 "PASS": bool(rho > 0 and p_pos < ALPHA),
                 "REVERSE": bool(rho < 0 and p_neg < ALPHA)}
        inferences[label] = entry
        return entry

    register("I1", comp, nh, nw, "struct_z_composite")
    for label, (name, sign, _d) in zip(["I3", "I4", "I5", "I6"], MEMBERS):
        register(label, member_vals[name], nh, nw,
                 f"{'-' if sign < 0 else '+'}{'log10(' + name + ')' if name == 'rime_class_size' else name}")

    # ---- I2: the stratified permutation null
    #
    # Within-bin permutation rearranges POSITIONS only, so the multiset of outcome values is
    # unchanged and rank(permuted outcome) == permuted rank(outcome), exactly. The ranks are
    # therefore taken once and permuted, rather than re-ranked 10,000 times. This is an
    # identity, not an approximation -- and it is verified against the literal slow route on
    # the first 25 draws of every call, aborting on any disagreement.
    def stratified_perm(values, outcome, bins_arr, seed, n_perm=N_PERM):
        rho_obs = spearman(values, outcome)
        rng = np.random.default_rng(seed)
        groups = [np.where(bins_arr == b)[0] for b in sorted(set(bins_arr.tolist()))]
        rv = rankdata(values)
        rv = (rv - rv.mean()) / rv.std()
        ro = rankdata(outcome)
        work_rank = ro.copy()
        work_val = outcome.copy()
        draws = np.empty(n_perm)
        ge = le = 0
        for j in range(n_perm):
            for idx in groups:
                perm = rng.permutation(len(idx))
                work_rank[idx] = ro[idx][perm]
                if j < 25:
                    work_val[idx] = outcome[idx][perm]
            centred = work_rank - work_rank.mean()
            r = float((rv @ centred) / (len(rv) * centred.std()))
            if j < 25:
                slow = spearman(values, work_val)
                if abs(r - slow) > 1e-9:
                    die(f"fast permutation route disagreed with the literal route: {r} vs {slow}")
            draws[j] = r
            ge += r >= rho_obs
            le += r <= rho_obs
        return {"rho_obs": rho_obs,
                "p_one_sided_positive": (1 + int(ge)) / (1 + n_perm),
                "p_one_sided_negative": (1 + int(le)) / (1 + n_perm),
                "null_mean": float(draws.mean()), "null_sd": float(draws.std(ddof=1)),
                "n_perm": n_perm, "seed": seed,
                "fast_route_verified_on_draws": 25}

    say(f"[PERM] I2: {N_PERM} stratified permutations, k = {K_PRIMARY}, seed {SEED_PRIMARY} ...")
    i2 = stratified_perm(comp, nh, dec, SEED_PRIMARY)
    i2_rep = stratified_perm(comp, nh, dec, SEED_REPLICATION)
    dec5, edges5 = decile_bins(nw, K_SECONDARY)
    say(f"[PERM] S6: k = {K_SECONDARY}, boundaries {edges5} ...")
    i2_k5 = stratified_perm(comp, nh, dec5, SEED_PRIMARY)
    i2_k5_rep = stratified_perm(comp, nh, dec5, SEED_REPLICATION)
    inferences["I2"] = {
        "statistic": f"Spearman under stratified permutation, k = {K_PRIMARY} (PRIMARY)",
        "note": "struct_z_composite vs n_hadith",
        "primary_k10_seed_20260509": i2, "primary_k10_seed_20260519": i2_rep,
        "secondary_k5_seed_20260509": i2_k5, "secondary_k5_seed_20260519": i2_k5_rep,
        "PASS": bool(i2["rho_obs"] > 0 and i2["p_one_sided_positive"] < ALPHA),
        "REVERSE": bool(i2["rho_obs"] < 0 and i2["p_one_sided_negative"] < ALPHA),
    }

    # ---- prereg section 6.1: the verdict logic, PRINTED with the observed numbers substituted
    say("\n[VERDICT LOGIC] prereg section 6.1, alpha = 0.05/6 = %.8f" % ALPHA)
    passes, reverses = [], []
    for label in ["I1", "I2", "I3", "I4", "I5", "I6"]:
        e = inferences[label]
        if label == "I2":
            rho, p_pos, p_neg = e["primary_k10_seed_20260509"]["rho_obs"], \
                e["primary_k10_seed_20260509"]["p_one_sided_positive"], \
                e["primary_k10_seed_20260509"]["p_one_sided_negative"]
        else:
            rho, p_pos, p_neg = e["partial_rho"], e["p_one_sided_positive"], e["p_one_sided_negative"]
        say(f"  {label}: rho = {rho:+.4f}  p(+) = {p_pos:.4f}  p(-) = {p_neg:.4f}  "
            f"PASS <- rho>0 and p(+)<alpha : {e['PASS']}   REVERSE <- rho<0 and p(-)<alpha : {e['REVERSE']}"
            f"   [{e['note']}]")
        if e["PASS"]:
            passes.append(label)
        if e["REVERSE"]:
            reverses.append(label)
    verdict = "SUPPORTED" if passes else ("REVERSED" if reverses else "NULL")
    say(f"  passes = {passes}   reverses = {reverses}")
    say(f"  VERDICT = {verdict}")

    # ---- prereg section 6.3: sensitivities, NON-CONFIRMATORY
    sens = {}

    def sens_partial(label, values, outcome, control, subset=None, note=""):
        v, o, c = values, outcome, control
        if subset is not None:
            v, o, c = values[subset], outcome[subset], control[subset]
        rho = partial_spearman(v, o, c)
        p_two, p_pos, p_neg = partial_p_values(rho, len(v))
        sens[label] = {"note": note, "n": int(len(v)), "bare_rho": spearman(v, o),
                       "partial_rho": rho, "p_two_sided": p_two,
                       "p_one_sided_positive": p_pos, "p_one_sided_negative": p_neg}

    sens_partial("S1", comp, nh, nw_alt, note="length control = reception file's n_words (imla'i)")
    sens_partial("S2", comp, nh17, nw, note="reception = n_hadith_all17 (all seventeen books)")
    sens_partial("S3", comp, nbooks, nw, note="reception = n_books (breadth, 0-9)")
    first_only = np.array([not later[k] for k in keys])
    sens_partial("S4", comp, nh, nw, subset=first_only, note="first occurrences only")
    cited_only = nh > 0
    sens_partial("S5", comp, nh, nw, subset=cited_only, note="cited verses only (n_hadith >= 1)")
    sens["S6"] = {"note": f"stratified permutation at k = {K_SECONDARY} (prereg section 4)",
                  "seed_20260509": i2_k5, "seed_20260519": i2_k5_rep}

    say("\n[SENSITIVITIES] non-confirmatory")
    for label in ["S1", "S2", "S3", "S4", "S5"]:
        e = sens[label]
        say(f"  {label}: n = {e['n']:5d}  bare rho = {e['bare_rho']:+.4f}  "
            f"partial rho = {e['partial_rho']:+.4f}  p(2) = {e['p_two_sided']:.4f}   [{e['note']}]")
    say(f"  S6: rho = {i2_k5['rho_obs']:+.4f}  p(+) = {i2_k5['p_one_sided_positive']:.4f}  "
        f"p(-) = {i2_k5['p_one_sided_negative']:.4f}")

    # ---- descriptive census, rank-only
    top20 = sorted(range(n), key=lambda i: (-nh[i], mushaf[i]))[:20]
    census = {
        "n_verses_total": len(all_keys),
        "n_eligible": n,
        "n_excluded": len(all_keys) - n,
        "exclusion_reasons": dict(reasons),
        "n_cited": int((nh > 0).sum()),
        "frac_cited": float((nh > 0).mean()),
        "total_citations": int(nh.sum()),
        "max_citations": int(nh.max()),
        "top20_share_of_citations": float(sum(nh[i] for i in top20) / nh.sum()),
        "top20": [{"reference": f"Q {keys[i][0]}:{keys[i][1]}", "n_hadith": int(nh[i]),
                   "n_books": int(nbooks[i]), "n_words": int(nw[i]),
                   "struct_z_composite": float(comp[i]),
                   "struct_rank": float(struct_rank[i]),
                   "S_within_decile": float(S[i])} for i in top20],
        "length_drift": {
            "rho_n_hadith_vs_n_words": spearman(nh, nw),
            "rho_struct_z_composite_vs_n_words": spearman(comp, nw),
            "rho_profile_n_words_vs_reception_n_words": spearman(nw, nw_alt),
            "n_words_disagreements": int((nw != nw_alt).sum()),
        },
        "repetition": {
            "roster1_text_repeats": sum(1 for r in roster1 if r["text_repeats"]),
            "roster1_later_occurrence": sum(1 for r in roster1 if r["is_later_occurrence"]),
            "roster2_text_repeats": sum(1 for r in roster2 if r["text_repeats"]),
            "roster2_later_occurrence": sum(1 for r in roster2 if r["is_later_occurrence"]),
            "analysis_set_text_repeats": int(sum(1 for k in keys if repeats[k])),
        },
        "roster1_surah_spread": dict(Counter(r["surah"] for r in roster1)),
        "roster2_surah_spread": dict(Counter(r["surah"] for r in roster2)),
        "roster1_decile_spread": dict(Counter(r["length_decile"] for r in roster1)),
        "roster2_decile_spread": dict(Counter(r["length_decile"] for r in roster2)),
    }
    say(f"\n[CENSUS] {census['n_cited']} of {n} eligible verses cited "
        f"({100*census['frac_cited']:.1f}%); top 20 hold "
        f"{100*census['top20_share_of_citations']:.1f}% of {census['total_citations']} citations")
    say(f"[DRIFT] rho(n_hadith, n_words) = {census['length_drift']['rho_n_hadith_vs_n_words']:+.4f}; "
        f"rho(struct_z_composite, n_words) = {census['length_drift']['rho_struct_z_composite_vs_n_words']:+.4f}")
    say(f"[REPETITION] roster 1: {census['repetition']['roster1_text_repeats']}/30 repeated text, "
        f"{census['repetition']['roster1_later_occurrence']}/30 later occurrence")

    # ---- prereg section 7 step 7: write result.json ONCE, at completion
    payload = {
        "hypothesis": "H-NEW-3000",
        "verdict": verdict,
        "passes": passes, "reverses": reverses,
        "bonferroni_k": BONFERRONI_K, "alpha": ALPHA,
        "structural_score": {
            "primary": "struct_z_composite",
            "members": [{"column": nm, "sign": sg, "denominator": dn} for nm, sg, dn in MEMBERS],
            "excluded_length_dominated": LENGTH_DOMINATED,
            "excluded_other": ["struct_z_composite_resid (H-NEW-2990 section 3.3)",
                               "the six IS_LENGTH columns"],
            "length_control": "n_words as published in h-new-2990-verse-profile.csv",
        },
        "reception_score": {"primary": "n_hadith",
                            "definition": "H-NEW-860.1 locked N=5 verse-level distinctive quotation, nine canonical books"},
        "deciles": {"k": K_PRIMARY, "boundaries": edges, "bins": bins},
        "inferences": inferences,
        "sensitivities": sens,
        "census": census,
        "roster_1": roster1,
        "roster_2": roster2,
    }
    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True, default=float)

    manifest = {
        "hypothesis": "H-NEW-3000",
        "run_id": run_id,
        "run_directory": str(run_dir.relative_to(REPO)),
        "script": str(Path(__file__).resolve().relative_to(REPO)),
        "prereg": PREREG,
        "prereg_sha256": _prereg_sha,
        "inputs": [{"path": p, "sha256": s} for p, s in sorted(FROZEN.items())],
        "outputs": [
            {"path": str(r1_path.relative_to(REPO)), "role": "roster 1, write-once"},
            {"path": str(r2_path.relative_to(REPO)), "role": "roster 2, write-once"},
            {"path": str((run_dir / "result.json").relative_to(REPO)), "role": "result, written once at completion"},
            {"path": str(pub1.relative_to(REPO)), "role": "published roster 1 (outside the run directory; replaceable)"},
            {"path": str(pub2.relative_to(REPO)), "role": "published roster 2 (outside the run directory; replaceable)"},
        ],
        "git_commit": git_output("rev-parse", "HEAD"),
        "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION},
        "n_permutations": N_PERM,
        "python": sys.version, "numpy": np.__version__, "platform": platform.platform(),
        "utc": datetime.now(timezone.utc).isoformat(),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)

    say(f"\n[RUN DIR] {run_dir.relative_to(REPO)}")
    say(f"[VERDICT] {verdict}")


if __name__ == "__main__":
    main()
