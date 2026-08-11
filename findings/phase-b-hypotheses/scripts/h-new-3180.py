#!/usr/bin/env python3
"""
H-NEW-3180 — Do the Sajawandi pause grades order the length of the unit they close?

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3180-waqf-boundary.md
The SHA-256 of that file is embedded below and verified at runtime; mismatch is SystemExit.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3180.py
"""
import collections
import hashlib
import json
import os
import subprocess
import sys
import datetime

import numpy as np

# --------------------------------------------------------------------------------------
# Locks
# --------------------------------------------------------------------------------------
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-3180-waqf-boundary.md")
EXPECTED_PREREG_SHA = "047ccde36fb53e500882fa4959e877b6481d292b663bc111b803d09e2d33a86a"

FROZEN_INPUTS = {
    "quran-text/quran-full-tashkeel.json": "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    "quran-text/quran-min-tashkeel.json":  "87aaab41f78d1b148c8051b8afc1ee5fa66fd6d45f2f7a2984e3f9192c458b36",
    "quran-text/quran-no-tashkeel.json":   "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
}

N_PERM = 10000
TESTS_IN_FAMILY = 12                      # prereg section 6: 2 arms x 3 channels x 2 nulls
ALPHA_BONFERRONI = 0.05 / TESTS_IN_FAMILY
RAW_GATE = 0.005 / TESTS_IN_FAMILY        # 0.0004166666666666667

SEEDS = {
    "H1_nullA": 20260509, "H1_nullB": 20260510,
    "H2_nullA": 20260511, "H2_nullB": 20260512,
    "MDE": 20260513, "VARIANTS": 20260514,
}
REPL = 10                                  # replication offset


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_locks():
    got = sha256(PREREG)
    if got != EXPECTED_PREREG_SHA:
        raise SystemExit(
            "PREREG LOCK BREACH: expected %s got %s\n"
            "The pre-registration has changed since this script was written. "
            "Corrections belong in the finding, never in the pre-registration." % (EXPECTED_PREREG_SHA, got))
    for rel, want in FROZEN_INPUTS.items():
        got = sha256(os.path.join(ROOT, rel))
        if got != want:
            raise SystemExit("FROZEN INPUT CHANGED: %s expected %s got %s" % (rel, want, got))


# --------------------------------------------------------------------------------------
# Instrument  (prereg section 3)
# --------------------------------------------------------------------------------------
MARKS = {0x6D6: "sla", 0x6D7: "qla", 0x6D8: "meem", 0x6D9: "la",
         0x6DA: "jim", 0x6DB: "muanaqa", 0x6DC: "saktah"}
UNGRADED = {"muanaqa", "saktah"}                                   # prereg 3.1
DIAC = set(range(0x064B, 0x0660)) | {0x0670} | set(range(0x06D6, 0x06EE)) | {0x0640}

RANK4 = {"sla": 1, "jim": 2, "qla": 3, "meem": 4}                  # prereg 3.2
RANK5 = {"la": 1, "sla": 2, "jim": 3, "qla": 4, "meem": 5}


def parse(path):
    """-> list of (surah, verse, words, marks[(word_idx_it_follows, grade)], n_word_internal)"""
    out = []
    for s in json.load(open(path, encoding="utf-8")):
        for v in s["verses"]:
            words, marks, internal = [], [], 0
            for tok in v["text"].split(" "):
                cps = [ord(c) for c in tok]
                if cps and all(c in MARKS for c in cps):            # standalone mark token
                    for c in cps:
                        marks.append((len(words) - 1, MARKS[c]))
                    continue
                core, trail = tok, []
                while core and ord(core[-1]) in MARKS:              # mark attached at token end
                    trail.append(MARKS[ord(core[-1])])
                    core = core[:-1]
                inner = sum(1 for c in core if ord(c) in MARKS)      # word-internal saktah: excluded
                internal += inner
                if inner:
                    core = "".join(c for c in core if ord(c) not in MARKS)
                if core:
                    words.append(core)
                for g in reversed(trail):
                    marks.append((len(words) - 1, g))
            out.append((s["id"], v["id"], words, marks, internal))
    return out


def skel(w):
    return "".join(c for c in w if ord(c) not in DIAC)


def segments(rows, ranks, boundary_grades=None, orientation="closes"):
    """Segment terminated by (default) / opened by each graded mark.  prereg 3.1, 3.3, P4, P6."""
    bset = set(ranks) if boundary_grades is None else set(boundary_grades)
    out = []
    for su, ve, words, marks, _ in rows:
        bm = sorted([(i, g) for i, g in marks if g in bset], key=lambda t: t[0])
        cuts = [-1] + [i for i, _ in bm] + [len(words) - 1]
        for k, (i, g) in enumerate(bm):
            if g not in ranks:
                continue
            if orientation == "closes":
                seg = words[cuts[k] + 1: i + 1]
            else:                                                    # "opens"
                seg = words[i + 1: cuts[k + 2] + 1]
            out.append((su, ve, g,
                        len(seg),
                        sum(len(skel(w)) for w in seg),
                        sum(len(w) for w in seg),
                        len(words)))
    return out


# --------------------------------------------------------------------------------------
# Statistic  (prereg section 3.4, 4.3 -- permutation only, tie-corrected midranks)
# --------------------------------------------------------------------------------------
def midranks(x):
    x = np.asarray(x, dtype=float)
    o = np.argsort(x, kind="stable")
    sx = x[o]
    r = np.empty(len(x))
    i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and sx[j + 1] == sx[i]:
            j += 1
        r[o[i:j + 1]] = (i + j) / 2.0 + 1
        i = j + 1
    return r


def pearson(a, b):
    a = a - a.mean()
    b = b - b.mean()
    d = np.sqrt((a * a).sum() * (b * b).sum())
    return float((a * b).sum() / d) if d > 0 else 0.0


def spearman(g, l):
    return pearson(midranks(g), midranks(l))


def perm_rhos(grank_sorted, lranks_sorted, group_sorted, seed, n_perm):
    """Within-group label permutation.  Returns {channel: array of rho}.
    Grade midranks are invariant under within-group permutation (the global multiset is fixed),
    so we permute the precomputed midranks directly."""
    rng = np.random.default_rng(seed)
    n = len(grank_sorted)
    out = {c: np.empty(n_perm) for c in lranks_sorted}
    lc = {c: (v - v.mean()) for c, v in lranks_sorted.items()}
    ld = {c: np.sqrt((v * v).sum()) for c, v in lc.items()}
    for t in range(n_perm):
        idx = np.lexsort((rng.random(n), group_sorted))
        gp = grank_sorted[idx]
        gc = gp - gp.mean()
        gd = np.sqrt((gc * gc).sum())
        for c in out:
            out[c][t] = (gc * lc[c]).sum() / (gd * ld[c])
    return out


def rho_extremes(g, lengths, groups):
    """Exact rho_MAX / rho_MIN under within-group relabelling (prereg 4.4).
    Optimal because the global grade-rank multiset is invariant, so the objective separates."""
    gr = midranks(g)
    byg = collections.defaultdict(list)
    for k, gid in enumerate(groups):
        byg[gid].append(k)
    res = {}
    for c, L in lengths.items():
        gmax, gmin = gr.copy(), gr.copy()
        for idxs in byg.values():
            labs = sorted(gr[i] for i in idxs)
            order = sorted(idxs, key=lambda i: L[i])
            for pos, i in enumerate(order):
                gmax[i] = labs[pos]
                gmin[i] = labs[len(labs) - 1 - pos]
        lr = midranks(L)
        res[c] = {"rho_max": pearson(gmax, lr), "rho_min": pearson(gmin, lr)}
    return res


# --------------------------------------------------------------------------------------
# Verdict  (prereg section 7.1 -- transcribed line by line, see finding for the diff)
# --------------------------------------------------------------------------------------
CHANNELS = ("L1_words", "L2_skeleton", "L3_raw")


def verdict(rho_obs, p_locked, p_opp, rho_max, rho_crit):
    """rho_obs/rho_max/rho_crit: {channel: float}.  p_locked/p_opp: {channel: {'A':p,'B':p}}."""
    worst_p = max(p_locked[c][N] for c in CHANNELS for N in ("A", "B"))
    worst_p_opp = max(p_opp[c][N] for c in CHANNELS for N in ("A", "B"))
    sign_ok = all(rho_obs[c] > 0 for c in CHANNELS)
    sign_rev = all(rho_obs[c] < 0 for c in CHANNELS)
    untestable = any(rho_max[c] < rho_crit[c] for c in CHANNELS)
    if untestable:
        v = "UNTESTABLE"
    elif sign_ok and worst_p < RAW_GATE:
        v = "PASS"
    elif sign_rev and worst_p_opp < RAW_GATE:
        v = "REVERSED"
    else:
        v = "NULL"
    return {"verdict": v, "worst_p_locked": worst_p, "worst_p_opposite": worst_p_opp,
            "sign_ok": sign_ok, "sign_reversed": sign_rev, "untestable": untestable,
            "raw_gate": RAW_GATE}


# --------------------------------------------------------------------------------------
# Arm runner
# --------------------------------------------------------------------------------------
def build(path, ranks, boundary_grades=None, orientation="closes"):
    rows = parse(path)
    S = segments(rows, ranks, boundary_grades, orientation)
    g = np.array([ranks[s[2]] for s in S], dtype=float)
    lengths = {"L1_words": np.array([s[3] for s in S], dtype=float),
               "L2_skeleton": np.array([s[4] for s in S], dtype=float),
               "L3_raw": np.array([s[5] for s in S], dtype=float)}
    host = np.array([s[6] for s in S], dtype=float)
    verse_g = np.array([s[0] * 10000 + s[1] for s in S])
    surah_g = np.array([s[0] for s in S])
    return rows, S, g, lengths, host, verse_g, surah_g


def run_arm(name, path, ranks, seed_a, seed_b, n_perm=N_PERM):
    rows, S, g, lengths, host, verse_g, surah_g = build(path, ranks)
    n = len(S)

    census = collections.Counter(s[2] for s in S)
    by_grade = {ranks[k]: v for k, v in census.items()}

    ties = {}
    for c, L in lengths.items():
        cnt = collections.Counter(L.tolist())
        ties[c] = {"tie_fraction": sum(v for v in cnt.values() if v > 1) / n,
                   "distinct": len(cnt), "min": float(L.min()), "max": float(L.max()),
                   "mean": float(L.mean()), "median": float(np.median(L))}

    rho_obs = {c: spearman(g, L) for c, L in lengths.items()}
    ext = rho_extremes(g, lengths, verse_g)
    rho_max = {c: ext[c]["rho_max"] for c in CHANNELS}

    gr = midranks(g)
    lr = {c: midranks(L) for c, L in lengths.items()}

    res_nulls, p_locked, p_opp, rho_crit = {}, {}, {}, {}
    for c in CHANNELS:
        p_locked[c], p_opp[c] = {}, {}
    for tag, groups, seed in (("A", verse_g, seed_a), ("B", surah_g, seed_b)):
        order = np.argsort(groups, kind="stable")
        dist = perm_rhos(gr[order], {c: lr[c][order] for c in CHANNELS}, groups[order], seed, n_perm)
        res_nulls[tag] = {}
        for c in CHANNELS:
            d = dist[c]
            p_locked[c][tag] = (1 + int((d >= rho_obs[c]).sum())) / (1 + n_perm)
            p_opp[c][tag] = (1 + int((d <= rho_obs[c]).sum())) / (1 + n_perm)
            res_nulls[tag][c] = {"null_mean": float(d.mean()), "null_sd": float(d.std()),
                                 "q_1_minus_gate": float(np.quantile(d, 1 - RAW_GATE))}
            if tag == "A":
                rho_crit[c] = float(np.quantile(d, 1 - RAW_GATE))

    V = verdict(rho_obs, p_locked, p_opp, rho_max, rho_crit)

    # prereg 7.4 -- reducibility: length residualised on host-verse word count
    reduced = {}
    for c, L in lengths.items():
        X = np.vstack([np.ones(n), host]).T
        beta, *_ = np.linalg.lstsq(X, L, rcond=None)
        reduced[c] = spearman(g, L - X @ beta)

    permutable = sum(len(idxs) for idxs in _groups(verse_g).values() if len({g[i] for i in idxs}) >= 2)

    return {
        "arm": name, "source_file": os.path.relpath(path, ROOT), "n_segments": n,
        "by_grade_rank": by_grade, "grade_census": dict(census),
        "n_verses_with_marks": len(_groups(verse_g)),
        "loci_in_permutable_verses": permutable,
        "permutable_fraction": permutable / n,
        "length_channels": ties,
        "rho_observed": rho_obs,
        "rho_extremes_within_verse_relabel": ext,
        "rho_crit_nullA_at_gate": rho_crit,
        "p_locked_direction": p_locked, "p_opposite_tail": p_opp,
        "null_summaries": res_nulls,
        "rho_residualised_on_host_verse_wordcount": reduced,
        **V,
    }


def _groups(gid):
    d = collections.defaultdict(list)
    for k, v in enumerate(gid):
        d[v].append(k)
    return d


# --------------------------------------------------------------------------------------
# MDE  (prereg 4.4)
# --------------------------------------------------------------------------------------
def mde(path, ranks, crit, seed, n_seeds=20):
    """crit is the Null-A (1 - RAW_GATE) quantile already computed by the arm, at N_PERM."""
    rows, S, g, lengths, host, verse_g, surah_g = build(path, ranks)
    n = len(S)
    gr = midranks(g)
    L = lengths["L1_words"]
    lr = midranks(L)
    groups = _groups(verse_g)
    perm_verses = [v for v, idxs in groups.items() if len({g[i] for i in idxs}) >= 2]
    rng0 = np.random.default_rng(seed)
    curve = []
    for f in (0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.75, 1.00):
        hits = 0
        for s in range(n_seeds):
            rng = np.random.default_rng(int(rng0.integers(1 << 30)))
            gg = gr.copy()
            for v, idxs in groups.items():                       # start from a null draw
                lab = gg[idxs]
                rng.shuffle(lab)
                gg[idxs] = lab
            chosen = rng.choice(perm_verses, size=max(1, int(round(f * len(perm_verses)))), replace=False)
            for v in chosen:                                     # then length-order fraction f
                idxs = groups[v]
                labs = sorted(gg[i] for i in idxs)
                for pos, i in enumerate(sorted(idxs, key=lambda i: L[i])):
                    gg[i] = labs[pos]
            if pearson(gg, lr) > crit:
                hits += 1
        curve.append({"f": f, "detected": hits, "of": n_seeds, "power": hits / n_seeds})
        if hits == n_seeds and len(curve) >= 1:
            break
    detected = [c["f"] for c in curve if c["power"] >= 0.80]
    return {"nullA_crit_at_gate": crit, "n_permutable_verses": len(perm_verses),
            "curve": curve, "MDE_f_at_power_0.80": (min(detected) if detected else None),
            "n_perm_for_crit": N_PERM, "n_seeds": n_seeds,
            "definition": ("smallest fraction f of permutable verses that must be perfectly "
                           "length-ordered, starting from a Null-A draw, for rho to exceed the "
                           "Null-A critical value at the raw gate (prereg 4.4)")}


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------
def main():
    verify_locks()

    utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-3180", utc)
    os.makedirs(rundir, exist_ok=False)

    FULL = os.path.join(ROOT, "quran-text/quran-full-tashkeel.json")
    MIN = os.path.join(ROOT, "quran-text/quran-min-tashkeel.json")
    NO = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")

    # ---- instrument control (prereg 4.6): reproduce H-NEW-2610's published loci counts ----
    ctrl = {}
    _, S4, g4, *_ = build(FULL, RANK4)
    got4 = {RANK4[k]: v for k, v in collections.Counter(s[2] for s in S4).items()}
    want4 = {1: 1651, 2: 2083, 3: 511, 4: 21}
    _, S5, g5, *_ = build(MIN, RANK5)
    got5 = {RANK5[k]: v for k, v in collections.Counter(s[2] for s in S5).items()}
    want5 = {1: 68, 2: 1682, 3: 1972, 4: 603, 5: 22}
    ctrl["full_tashkeel_by_grade"] = {"expected_h_new_2610": want4, "observed": got4, "n": len(S4)}
    ctrl["min_tashkeel_by_grade"] = {"expected_h_new_2610": want5, "observed": got5, "n": len(S5)}
    if got4 != want4 or len(S4) != 4266 or got5 != want5 or len(S5) != 4347:
        raise SystemExit("INSTRUMENT CONTROL FAILED (prereg 4.6): %s / %s" % (ctrl, "abort"))
    ctrl["passed"] = True

    result = {
        "id": "H-NEW-3180", "prereg_sha256": EXPECTED_PREREG_SHA, "SMOKE_RUN": False,
        "n_perm": N_PERM, "tests_in_family": TESTS_IN_FAMILY,
        "alpha_bonferroni": ALPHA_BONFERRONI, "raw_gate": RAW_GATE,
        "seeds": SEEDS, "replication_offset": REPL,
        "exact_test_note": ("every p-value is a permutation p-value; no asymptotic distribution is "
                            "used anywhere (prereg 4.3, tie fractions ~0.99)"),
        "instrument_control": ctrl,
        "frozen_input_sha256": FROZEN_INPUTS,
    }

    result["H1"] = run_arm("H1_full_tashkeel_4rung", FULL, RANK4, SEEDS["H1_nullA"], SEEDS["H1_nullB"])
    result["H2"] = run_arm("H2_min_tashkeel_5rung", MIN, RANK5, SEEDS["H2_nullA"], SEEDS["H2_nullB"])
    result["H1_replication"] = run_arm("H1_repl", FULL, RANK4, SEEDS["H1_nullA"] + REPL, SEEDS["H1_nullB"] + REPL)
    result["H2_replication"] = run_arm("H2_repl", MIN, RANK5, SEEDS["H2_nullA"] + REPL, SEEDS["H2_nullB"] + REPL)

    # prereg 7.2
    for arm in ("H1", "H2"):
        result[arm]["replication_agrees"] = (result[arm]["verdict"] == result[arm + "_replication"]["verdict"])
        if not result[arm]["replication_agrees"]:
            result[arm]["verdict"] = "NULL-UNSTABLE"

    result["MDE_H1"] = mde(FULL, RANK4, result["H1"]["rho_crit_nullA_at_gate"]["L1_words"], SEEDS["MDE"])

    # ---- declared ungated variants (prereg section 5) ----
    var = {}
    #  P1 third tuple
    _, Sn, gn, ln, _, vn, _ = build(NO, RANK5)
    var["P1_no_tashkeel_third_tuple"] = {
        "n": len(Sn), "by_grade": {RANK5[k]: v for k, v in collections.Counter(s[2] for s in Sn).items()},
        "rho": {c: spearman(gn, L) for c, L in ln.items()}, "gated": False}
    #  P4 all marks (incl. saktah/muanaqa) as segmentation boundaries
    allb = set(RANK5) | UNGRADED
    for tag, path, ranks in (("full", FULL, RANK4), ("min", MIN, RANK5)):
        _, Sv, gv, lv, *_ = build(path, ranks, boundary_grades=allb)
        var["P4_all_marks_boundaries_" + tag] = {
            "n": len(Sv), "rho": {c: spearman(gv, L) for c, L in lv.items()}, "gated": False}
    #  P6 segment the mark OPENS
    for tag, path, ranks in (("full", FULL, RANK4), ("min", MIN, RANK5)):
        _, Sv, gv, lv, *_ = build(path, ranks, orientation="opens")
        var["P6_segment_opened_" + tag] = {
            "n": len(Sv), "rho": {c: spearman(gv, L) for c, L in lv.items()}, "gated": False}
    result["declared_variants_ungated"] = var

    result["family_verdict"] = family_verdict(result["H1"]["verdict"], result["H2"]["verdict"])

    with open(os.path.join(rundir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1, sort_keys=True)

    manifest = {
        "id": "H-NEW-3180", "utc": utc,
        "command": " ".join([sys.executable, os.path.relpath(os.path.abspath(__file__), ROOT)]),
        "prereg": os.path.relpath(PREREG, ROOT), "prereg_sha256": EXPECTED_PREREG_SHA,
        "script_sha256": sha256(os.path.abspath(__file__)),
        "inputs": FROZEN_INPUTS,
        "git_commit": subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"],
                                     capture_output=True, text=True).stdout.strip(),
        "numpy": np.__version__, "python": sys.version.split()[0],
    }
    with open(os.path.join(rundir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1, sort_keys=True)

    print("run:", os.path.relpath(rundir, ROOT))
    for arm in ("H1", "H2"):
        a = result[arm]
        print("%-4s %-34s n=%d  verdict=%s  worst_p=%.5f  repl_agrees=%s"
              % (arm, a["arm"], a["n_segments"], a["verdict"], a["worst_p_locked"], a["replication_agrees"]))
        for c in CHANNELS:
            print("      %-12s rho=%+.4f  pA=%.5f pB=%.5f  rho_max=%+.4f rho_crit=%+.4f  resid_rho=%+.4f"
                  % (c, a["rho_observed"][c], a["p_locked_direction"][c]["A"], a["p_locked_direction"][c]["B"],
                     a["rho_extremes_within_verse_relabel"][c]["rho_max"], a["rho_crit_nullA_at_gate"][c],
                     a["rho_residualised_on_host_verse_wordcount"][c]))
    print("family:", result["family_verdict"])
    print("MDE:", result["MDE_H1"]["MDE_f_at_power_0.80"], result["MDE_H1"]["curve"][:4])


def family_verdict(v1, v2):
    """prereg 7.3"""
    if v1 == "PASS" and v2 == "PASS":
        return "GRADE ORDERS SEGMENT LENGTH (parser-free channel) - not independent of H-NEW-2610 H1b"
    if v1 == "NULL" and v2 == "NULL":
        return "SECOND CLEAN-CHANNEL NULL"
    if v1 == "REVERSED" or v2 == "REVERSED":
        return "REVERSED - report at full prominence"
    if v1 != v2:
        return "ARMS DISAGREE - the inventory is the deciding parameter"
    return "MIXED: H1=%s H2=%s" % (v1, v2)


if __name__ == "__main__":
    main()
