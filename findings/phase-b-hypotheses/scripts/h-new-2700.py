#!/usr/bin/env python3
"""H-NEW-2700: does loanword donor language stratify by revelation phase?

Runner only. Emits no interpretation. See
findings/phase-b-hypotheses/prereg-h-new-2700-loanword-donor-strata.md
"""

import argparse
import csv
import hashlib
import json
import math
import platform
import random
import re
import shlex
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# --- prereg §3.1: frozen inputs -------------------------------------------
EXPECTED_PREREG_SHA = "6e5332da94d1fb6ce24261e34acd99d34f171215e810dbf639981b13c5736525"
EXPECTED_TSV_SHA = "d12ebac9d4bb62bbc1a8c810d7e2c069195e20113a77fb04505a84dfd4674b94"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_CHRON_SHA = "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7"
EXPECTED_QURAN_SHA = "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"

# --- prereg §4/§7 ----------------------------------------------------------
N_PERM = 10_000
TESTS_IN_FAMILY = 8
ALPHA_BON = 0.05 / TESTS_IN_FAMILY           # 0.00625
CORRECTED_GATE = 0.005
RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY  # 0.000625
SEED_NULL_A = 20260509
SEED_NULL_B = 20260510
REPLICATION_OFFSET = 10

PHASES = ["Early Meccan", "Middle Meccan", "Late Meccan", "Medinan"]
PHASE_IDX = {p: i + 1 for i, p in enumerate(PHASES)}

# --- prereg §3.3: donor families, taken from the registry as-is ------------
ARAM_NARROW = {"syriac", "syriac-aramaic-shared", "aramaic"}
ARAM_BROAD = ARAM_NARROW | {"hebrew-aramaic-shared"}
PERS = {"persian"}
HEB = {"hebrew", "hebrew-aramaic-shared"}

# --- prereg §3.2: Buckwalter -> Arabic, standard 1:1 map -------------------
BW = {"'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ", "A": "ا", "b": "ب",
      "p": "ة", "t": "ت", "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د", "*": "ذ",
      "r": "ر", "z": "ز", "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ",
      "E": "ع", "g": "غ", "_": "ـ", "f": "ف", "q": "ق", "k": "ك", "l": "ل", "m": "م",
      "n": "ن", "h": "ه", "w": "و", "Y": "ى", "y": "ي", "F": "ً", "N": "ٌ", "K": "ٍ",
      "a": "َ", "u": "ُ", "i": "ِ", "~": "ّ", "o": "ْ", "^": "ٓ", "#": "ٔ", "`": "ٰ",
      "{": "ٱ"}
SHORT = set("ًٌٍَُِّْٓٔ")
LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")


def bw2ar(s):
    return "".join(BW.get(c, c) for c in s)


def key(s, drop_dagger):
    """prereg §3.2. Tier 1: dagger alif -> alif. Tier 2: dagger alif deleted.
    Long-a-blind keys are REJECTED (prereg §3.2 rejected variant A)."""
    s = "".join(c for c in s if c not in SHORT and c != "ـ")
    s = s.replace("وٰ", "ا").replace("يٰ", "ا")
    s = s.replace("ٰ", "" if drop_dagger else "ا")
    for a, b in (("ٱ", "ا"), ("أ", "ا"), ("إ", "ا"), ("آ", "ا"),
                 ("ؤ", "ء"), ("ئ", "ء"), ("ة", "ه"), ("ى", "ي")):
        s = s.replace(a, b)
    return s.replace("ء", "")


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


# --- statistics ------------------------------------------------------------
def perm_p(obs, draws):
    return (1 + sum(1 for d in draws if d >= obs)) / (len(draws) + 1)


def ols_residuals(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    beta = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else 0.0
    return [y - (my + beta * (x - mx)) for x, y in zip(xs, ys)], beta


def load_qac():
    """Unique-lemma index. prereg §3.2 ambiguity gate needs the lemma multiset."""
    idx = {1: defaultdict(set), 2: defaultdict(set)}
    lemmas = {1: defaultdict(set), 2: defaultdict(set)}
    with open(QAC_PATH, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) != 4:
                continue
            m = LOC_RE.fullmatch(f[0])
            if not m:
                continue
            lm = re.search(r"(?:^|\|)LEM:([^|]+)", f[3])
            if not lm:
                continue
            ar = bw2ar(lm.group(1))
            loc = (int(m[1]), int(m[2]), int(m[3]))
            for tier, dd in ((1, False), (2, True)):
                k = key(ar, dd)
                idx[tier][k].add(loc)
                lemmas[tier][k].add(lm.group(1))
    return idx, lemmas


def main():
    global N_PERM, QAC_PATH
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--perms", type=int, default=N_PERM)
    ap.add_argument("--out", default=None,
                    help="override run-dir parent; used only for SMOKE runs so they are "
                         "not written into the registered path")
    args = ap.parse_args()
    N_PERM = args.perms
    smoke = (N_PERM != 10_000)
    repo = Path(args.repo).resolve()
    rel = {"prereg": "findings/phase-b-hypotheses/prereg-h-new-2700-loanword-donor-strata.md",
           "tsv": "data/loanwords/jeffery-1938-loanwords.tsv",
           "qac": "data/morphology/quranic-corpus-morphology-0.4.txt",
           "chron": "data/revelation-order.csv",
           "quran": "quran-text/quran-no-tashkeel.json",
           "script": "findings/phase-b-hypotheses/scripts/h-new-2700.py"}
    P = {k: repo / v for k, v in rel.items()}
    QAC_PATH = P["qac"]

    hashes = {
        "prereg": require(P["prereg"], EXPECTED_PREREG_SHA, "prereg"),
        "jeffery_tsv": require(P["tsv"], EXPECTED_TSV_SHA, "Jeffery TSV"),
        "qac_v04": require(P["qac"], EXPECTED_QAC_SHA, "QAC"),
        "revelation_order": require(P["chron"], EXPECTED_CHRON_SHA, "chronology"),
        "quran_no_tashkeel": require(P["quran"], EXPECTED_QURAN_SHA, "quran"),
        "script": sha256(P["script"]),
    }

    res = {"id": "H-NEW-2700", "SMOKE_RUN": smoke, "prereg_sha256": hashes["prereg"],
           "n_perm": N_PERM, "tests_in_family": TESTS_IN_FAMILY,
           "alpha_bonferroni": ALPHA_BON, "raw_gate": RAW_GATE,
           "corrected_gate": CORRECTED_GATE,
           "seeds": {"null_a": SEED_NULL_A, "null_b": SEED_NULL_B,
                     "replication_offset": REPLICATION_OFFSET}}

    # ---- corpus, chronology ----------------------------------------------
    quran = json.load(open(P["quran"], encoding="utf-8"))
    words_per_surah, verses_per_surah = {}, {}
    for s in quran:
        words_per_surah[s["id"]] = sum(len(v["text"].split()) for v in s["verses"])
        verses_per_surah[s["id"]] = len(s["verses"])
    phase_of = {}
    with open(P["chron"], encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            phase_of[int(row["mushaf_order"])] = row["noldeke_phase"]
    if set(phase_of.values()) != set(PHASES):
        raise SystemExit(f"ABORT: phase vocabulary differs from prereg: {set(phase_of.values())}")
    res["corpus"] = {"surahs": len(quran), "words": sum(words_per_surah.values()),
                     "phase_sizes": dict(Counter(phase_of.values())),
                     "words_per_phase": {p: sum(words_per_surah[s] for s in phase_of if phase_of[s] == p)
                                         for p in PHASES}}

    # ---- registry ---------------------------------------------------------
    lines = [l for l in open(P["tsv"], encoding="utf-8") if not l.startswith("#")]
    rows = list(csv.DictReader(lines, delimiter="\t"))
    res["registry"] = {"data_rows": len(rows),
                       "note": "frontier map reported 506; that is the line count "
                               "including 201 comment lines",
                       "by_source_language": dict(Counter(r["source_language"] for r in rows)),
                       "by_confidence": dict(Counter(r["confidence"] for r in rows))}

    # ---- match (prereg §3.2) ---------------------------------------------
    idx, lemmas = load_qac()
    eligible, ambiguous, unmatched, multiword = [], [], [], []
    for r in rows:
        a = r["arabic_lemma"].strip()
        if " " in a:
            multiword.append(a)
            continue
        for tier, dd in ((1, False), (2, True)):
            k = key(a, dd)
            if k in idx[tier]:
                cands = sorted(lemmas[tier][k])
                rec = {"arabic": a, "romanized": r["romanized"],
                       "donor": r["source_language"], "confidence": r["confidence"],
                       "suyuti38": r["suyuti_naw_38_attested"], "tier": tier,
                       "qac_lemmas": cands, "locs": sorted(idx[tier][k])}
                (eligible if len(cands) == 1 else ambiguous).append(rec)
                break
        else:
            unmatched.append({"arabic": a, "romanized": r["romanized"],
                              "donor": r["source_language"], "confidence": r["confidence"]})
    res["matching"] = {
        "eligible_unique_lemma": len(eligible), "excluded_ambiguous": len(ambiguous),
        "excluded_unmatched": len(unmatched), "excluded_multiword": len(multiword),
        "tier_used": dict(Counter(e["tier"] for e in eligible)),
        "eligible_by_donor": dict(Counter(e["donor"] for e in eligible)),
        "unmatched_by_donor": dict(Counter(u["donor"] for u in unmatched)),
        "ambiguous_entries": [{"arabic": a["arabic"], "romanized": a["romanized"],
                               "donor": a["donor"], "qac_lemmas": a["qac_lemmas"]}
                              for a in ambiguous],
        "unmatched_entries": unmatched,
        "multiword_entries": multiword,
        "rejected_variant_A_longa_blind": "rejected in prereg 3.2; matched qur'an to qarn",
    }

    # ---- per-type attestation --------------------------------------------
    for e in eligible:
        e["tokens"] = len(e["locs"])
        e["phase_counts"] = Counter(phase_of[l[0]] for l in e["locs"])
        e["phi"] = sum(PHASE_IDX[phase_of[l[0]]] for l in e["locs"]) / len(e["locs"])
        e["per_surah"] = Counter(l[0] for l in e["locs"])

    def fam(e, aram_set):
        if e["donor"] in aram_set:
            return "ARAM"
        if e["donor"] in PERS:
            return "PERS"
        return None

    # ---- statistics -------------------------------------------------------
    def stat_h1(types, phases_map, fam_of):
        c = defaultdict(Counter)
        for t in types:
            f = fam_of(t)
            if not f:
                continue
            for loc in t["locs"]:
                c[phases_map[loc[0]]][f] += 1
        def share(p):
            n = c[p]["ARAM"] + c[p]["PERS"]
            return c[p]["ARAM"] / n if n else float("nan")
        return share("Late Meccan") - share("Medinan"), c

    def stat_density(types, phases_map, fam_of, want, target_phase):
        per = defaultdict(int)
        for t in types:
            if fam_of(t) != want:
                continue
            for s, n in t["per_surah"].items():
                per[s] += n
        sids = sorted(words_per_surah)
        dens = [1000.0 * per[s] / words_per_surah[s] for s in sids]
        resid, beta = ols_residuals([math.log(words_per_surah[s]) for s in sids], dens)
        by = defaultdict(list)
        for s, r in zip(sids, resid):
            by[phases_map[s]].append(r)
        means = {p: (sum(by[p]) / len(by[p]) if by[p] else float("nan")) for p in PHASES}
        others = [means[p] for p in PHASES if p != target_phase]
        return means[target_phase] - max(others), means, beta

    def stat_h4(types, phases_map, fam_of):
        vals = defaultdict(list)
        for t in types:
            f = fam_of(t)
            if not f:
                continue
            phi = sum(PHASE_IDX[phases_map[l[0]]] for l in t["locs"]) / len(t["locs"])
            vals[f].append(phi)
        if not vals["ARAM"] or not vals["PERS"]:
            return float("nan"), vals
        return (sum(vals["PERS"]) / len(vals["PERS"])
                - sum(vals["ARAM"]) / len(vals["ARAM"])), vals

    def run_tuple(types, aram_set, gated):
        fam_of = lambda e: fam(e, aram_set)
        out = {"n_types": len(types),
               "n_ARAM_types": sum(1 for t in types if fam_of(t) == "ARAM"),
               "n_PERS_types": sum(1 for t in types if fam_of(t) == "PERS"),
               "n_ARAM_tokens": sum(t["tokens"] for t in types if fam_of(t) == "ARAM"),
               "n_PERS_tokens": sum(t["tokens"] for t in types if fam_of(t) == "PERS"),
               "gated": gated}
        h1, cmat = stat_h1(types, phase_of, fam_of)
        h2, m2, b2 = stat_density(types, phase_of, fam_of, "ARAM", "Late Meccan")
        h3, m3, b3 = stat_density(types, phase_of, fam_of, "PERS", "Medinan")
        h4, v4 = stat_h4(types, phase_of, fam_of)
        out["H1_composition"] = {"statistic": h1, "locked": "Delta > 0",
                                 "phase_counts": {p: dict(cmat[p]) for p in PHASES}}
        out["H2_aram_density"] = {"statistic": h2, "locked": "Delta > 0",
                                  "resid_means": m2, "ols_beta": b2}
        out["H3_pers_density"] = {"statistic": h3, "locked": "Delta > 0",
                                  "resid_means": m3, "ols_beta": b3}
        out["H4_type_level"] = {"statistic": h4, "locked": "Delta > 0",
                                "mean_phi_ARAM": (sum(v4["ARAM"]) / len(v4["ARAM"])) if v4["ARAM"] else None,
                                "mean_phi_PERS": (sum(v4["PERS"]) / len(v4["PERS"])) if v4["PERS"] else None}
        if not gated:
            return out

        donors = [t["donor"] for t in types]
        sids = sorted(words_per_surah)
        base_phase = [phase_of[s] for s in sids]
        for hkey, fn in (("H1_composition", lambda ts, pm, fo: stat_h1(ts, pm, fo)[0]),
                         ("H2_aram_density", lambda ts, pm, fo: stat_density(ts, pm, fo, "ARAM", "Late Meccan")[0]),
                         ("H3_pers_density", lambda ts, pm, fo: stat_density(ts, pm, fo, "PERS", "Medinan")[0]),
                         ("H4_type_level", lambda ts, pm, fo: stat_h4(ts, pm, fo)[0])):
            obs = out[hkey]["statistic"]
            for nm, seed in (("null_a", SEED_NULL_A), ("null_b", SEED_NULL_B)):
                for tag, sd in [("", seed), ("_replication", seed + REPLICATION_OFFSET)]:
                    rng = random.Random(sd)
                    draws = []
                    for _ in range(N_PERM):
                        if nm == "null_a":            # permute donor labels across types
                            perm = donors[:]
                            rng.shuffle(perm)
                            for t, d in zip(types, perm):
                                t["_d"] = d
                            fo = lambda e: ("ARAM" if e["_d"] in aram_set
                                            else ("PERS" if e["_d"] in PERS else None))
                            draws.append(fn(types, phase_of, fo))
                        else:                          # permute phase labels across surahs
                            pp = base_phase[:]
                            rng.shuffle(pp)
                            pm = dict(zip(sids, pp))
                            draws.append(fn(types, pm, fam_of))
                    for t in types:
                        t.pop("_d", None)
                    draws = [d for d in draws if not (isinstance(d, float) and math.isnan(d))]
                    p = perm_p(obs, draws)
                    out[hkey][nm + tag] = {"seed": sd, "n_valid_draws": len(draws),
                                           "p_raw": p,
                                           "p_bonferroni": min(1.0, TESTS_IN_FAMILY * p),
                                           "passes_gate": p < RAW_GATE}
            # prereg §7: PASS iff direction matches AND BOTH raw p < RAW_GATE
            direction_ok = (not math.isnan(obs)) and obs > 0
            out[hkey]["direction_matches_lock"] = direction_ok
            out[hkey]["PASS"] = (direction_ok
                                 and out[hkey]["null_a"]["passes_gate"]
                                 and out[hkey]["null_b"]["passes_gate"])
        return out

    # ---- T1 primary, T2/T3 sensitivities (prereg §5) ----------------------
    res["T1_primary"] = run_tuple(eligible, ARAM_NARROW, gated=True)
    res["T2_high_confidence_only"] = run_tuple(
        [e for e in eligible if e["confidence"] == "HIGH"], ARAM_NARROW, gated=False)
    res["T3_aram_broad"] = run_tuple(eligible, ARAM_BROAD, gated=False)

    # ---- robustness (prereg §6) -------------------------------------------
    fam_of = lambda e: fam(e, ARAM_NARROW)
    pool = [t for t in eligible if fam_of(t)]
    loto_h1 = []
    for drop in pool:
        keep = [t for t in eligible if t is not drop]
        loto_h1.append({"dropped": drop["romanized"],
                        "H1": stat_h1(keep, phase_of, fam_of)[0],
                        "H4": stat_h4(keep, phase_of, fam_of)[0]})
    h1v = [x["H1"] for x in loto_h1 if not math.isnan(x["H1"])]
    h4v = [x["H4"] for x in loto_h1 if not math.isnan(x["H4"])]
    res["robustness"] = {
        "LOTO": {"n": len(loto_h1), "H1_min": min(h1v), "H1_max": max(h1v),
                 "H1_crosses_zero": min(h1v) <= 0 <= max(h1v),
                 "H4_min": min(h4v), "H4_max": max(h4v),
                 "H4_crosses_zero": min(h4v) <= 0 <= max(h4v),
                 "detail": sorted(loto_h1, key=lambda x: x["H1"])},
        "per_type": sorted([{"romanized": t["romanized"], "arabic": t["arabic"],
                             "donor": t["donor"], "confidence": t["confidence"],
                             "suyuti38": t["suyuti38"], "tokens": t["tokens"],
                             "phi": t["phi"], "phase_counts": dict(t["phase_counts"])}
                            for t in pool], key=lambda x: -x["tokens"]),
        "all_donor_families_raw_density_per_1000w": {},
        "suyuti38_split": {},
    }
    for donor in sorted(set(e["donor"] for e in eligible)):
        per = defaultdict(int)
        for t in eligible:
            if t["donor"] == donor:
                for s, n in t["per_surah"].items():
                    per[s] += n
        res["robustness"]["all_donor_families_raw_density_per_1000w"][donor] = {
            p: (1000.0 * sum(per[s] for s in phase_of if phase_of[s] == p)
                / max(1, sum(words_per_surah[s] for s in phase_of if phase_of[s] == p)))
            for p in PHASES}
    for flag in ("yes", "no", "disputed"):
        sel = [t for t in pool if t["suyuti38"] == flag]
        res["robustness"]["suyuti38_split"][flag] = {
            "n_types": len(sel), "tokens": sum(t["tokens"] for t in sel),
            "mean_phi": (sum(t["phi"] for t in sel) / len(sel)) if sel else None}
    # ambiguous-key sensitivity (descriptive)
    amb_pool = []
    for a in ambiguous:
        if fam(a, ARAM_NARROW):
            amb_pool.append({"romanized": a["romanized"], "donor": a["donor"],
                             "n_candidate_lemmas": len(a["qac_lemmas"])})
    res["robustness"]["ambiguous_in_ARAM_or_PERS"] = amb_pool
    # parent-instrument comparison
    res["robustness"]["parent_comparison"] = {
        "h_new_125_method": "whole-word exact match on proclitic-expanded surface forms "
                            "(scripts/h_new_125_chronology_content.py:423-458)",
        "h_new_125_reported_loanword_tokens": 'see csv/h-new-125.json loanword_tokens',
        "this_test_total_eligible_tokens": sum(t["tokens"] for t in eligible)}

    # ---- verdict (prereg §7) ---------------------------------------------
    T1 = res["T1_primary"]
    # prereg §6.1: an H1 whose leave-one-type-out range crosses zero is demoted to CBM
    # regardless of its p-value. Surfaced by the runner rather than left to prose.
    # This can only demote, never promote.
    loto_zero = res["robustness"]["LOTO"]["H1_crosses_zero"]
    res["verdict_inputs"] = {k: {"direction": T1[k]["direction_matches_lock"],
                                 "PASS": T1[k]["PASS"]}
                             for k in ("H1_composition", "H2_aram_density",
                                       "H3_pers_density", "H4_type_level")}
    res["verdict_inputs"]["H1_composition"]["LOTO_crosses_zero"] = loto_zero
    res["verdict_inputs"]["H1_CBM_demotion_triggered"] = bool(
        T1["H1_composition"]["PASS"] and (loto_zero or not T1["H4_type_level"]["PASS"]))

    # ---- immutable run record (prereg §9) ---------------------------------
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    parent = Path(args.out) if args.out else repo / "findings/phase-b-hypotheses/runs/h-new-2700"
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
    # prereg §9: repo-relative paths only, so the record is committable as-is
    manifest = {"id": "H-NEW-2700", "SMOKE_RUN": smoke, "utc": ts,
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
