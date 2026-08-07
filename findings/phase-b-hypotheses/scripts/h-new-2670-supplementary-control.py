#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2670 SUPPLEMENTARY CONTROL — the property-selection guard.

POST-OBSERVATION. MW-7-CAPPED. This control was written AFTER the primary run and can
only DEMOTE the locked verdict, never promote it. The pre-registration
(prereg-h-new-2670-joint-conjunction.md, SHA d6c5a481…fe7c) is NOT modified; its gate is
re-verified here unchanged.

WHY IT EXISTS. The pre-registered control (pre-reg §6) holds the eleven property KINDS
fixed and asks whether a random 14-subset, described on those same eleven axes, becomes
comparably unique. It passed at q = 0.018. But that control cannot see the loophole that
matters most: **the eleven axes were not chosen at random.** They are the survivors of a
long series of prior tests run against this one letter-set — H-NEW-44, 44.2, 44.2.1, 45,
46, 51, 53, 55, 56, 57, 60, 69, 165, 600, 1810, 2550. Holding those axes fixed hands the
attested set an advantage no random subset gets: its axes were picked because it is
extreme on them.

THE FAIR CONTEST. Give every subset the same privilege. Assemble a MENU of letter-class
axes, every one of them independently attested in a classical source or a prior
pre-registered finding of this project. Let each reference set — the muqaṭṭaʿāt and each
random subset alike — choose the ELEVEN axes on which it is most exceptional, and on each
chosen axis claim whichever of the two attested property-kinds serves it better:

  TAIL     — enrichment / depletion, "at least as extreme as X"    (the kind H-NEW-60,
             H-NEW-69 and H-NEW-44.2.1 use)
  BALANCE  — "at least as close to half as X"                      (the kind al-Zamakhshari
             and H-NEW-2550 use)

Then count, exactly over all 40,116,600 subsets, how many satisfy the resulting
eleven-property profile. If a random 14-subset allowed to pick its own axes reaches the
attested set's level of uniqueness about as often as not, then near-uniqueness is
manufactured by the method and the joint count means nothing.

Author: Waiel Al-Shujaa
"""

import hashlib
import json
import math
import os
import random
import time
from datetime import datetime, timezone

import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
PREREG = os.path.join(ROOT, "findings", "phase-b-hypotheses",
                      "prereg-h-new-2670-joint-conjunction.md")
PREREG_SHA256 = "d6c5a48179585f665c5563f7357629ebb616bb00d075bf4fac2032034615fe7c"
PRIMARY_JSON = os.path.join(ROOT, "findings", "phase-b-hypotheses", "csv", "h-new-2670.json")
OUT_JSON = os.path.join(ROOT, "findings", "phase-b-hypotheses",
                        "csv", "h-new-2670-supplementary-control.json")

SEED = 20260509
SEED_REPLICATION = 20260519
N_CONTROL = 1000
N_PICK = 11                     # same budget as the declared property list
N_SUBSETS = 40116600

ALPHABET28 = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
MUQ14 = set("احرسصطعقكلمنهي")


# ---------------------------------------------------------------------------
# THE MENU — every axis independently attested; nothing invented here
# ---------------------------------------------------------------------------

MENU = [
    # al-Zamakhshari's sifat, al-Kashshaf ad Q 2:1 (complements omitted: an
    # at-least-as-extreme / at-least-as-balanced event on C is the SAME event on C^c)
    ("mahmusa",            "احخ", "ت ث ح خ س ش ص ف ك ه",   "al-Zamakhshari, al-Kashshaf ad Q 2:1"),
    ("shadida",            "",    "ا ب ت ج د ط ق ك",        "al-Zamakhshari, al-Kashshaf ad Q 2:1"),
    ("mutbaqa",            "",    "ص ض ط ظ",                "al-Zamakhshari; = H-NEW-69 G8 itbaq"),
    ("mustaliya",          "",    "خ ص ض ط ظ غ ق",          "al-Zamakhshari; = H-NEW-165 tafkhim"),
    ("qalqala",            "",    "ب ج د ط ق",              "al-Zamakhshari / Ibn al-Jazari"),
    ("bayniyya",           "",    "ر ع ل م ن",              "later tripartite tajwid; H-NEW-2550 T-C"),
    ("shamsiyyah",         "",    "ت ث د ذ ر ز س ش ص ض ط ظ ل ن", "al-Zamakhshari, al-Mufassal §82; H-NEW-69 G1"),
    ("modern_voiced",      "",    "ا ب ج د ذ ر ز ض ظ ع غ ل م ن و ي", "Watson 2002; H-NEW-69 G5"),
    ("safir",              "",    "ز س ص",                  "Sibawayh / al-Khalil; H-NEW-69 G7"),
    # al-Khalil's 8 places of articulation, H-NEW-44.2
    ("poa_pharyngeal_glottal", "", "ا ه ع ح",               "al-Khalil POA; H-NEW-44.2 / 44.2.1"),
    ("poa_velar_uvular",   "",    "غ خ ق ك",                "al-Khalil POA; H-NEW-44.2"),
    ("poa_palatal",        "",    "ج ش ي ض",                "al-Khalil POA; H-NEW-44.2"),
    ("poa_coronal_sibilant", "",  "ص ز س",                  "al-Khalil POA; H-NEW-44.2"),
    ("poa_coronal_stop",   "",    "ط د ت",                  "al-Khalil POA; H-NEW-44.2"),
    ("poa_interdental",    "",    "ظ ذ ث",                  "al-Khalil POA; H-NEW-44.2"),
    ("poa_coronal_sonorant", "",  "ر ل ن",                  "al-Khalil POA; H-NEW-44.2"),
    ("poa_labial",         "",    "ف ب م و",                "al-Khalil POA; H-NEW-44.2"),
    # orthographic i'jam classes, H-NEW-60
    ("dotless",            "",    "ا ح د ر س ص ط ع ك ل م ه و", "H-NEW-60 i'jam table"),
    ("one_dot",            "",    "ب ج خ ذ ز ض ظ غ ف ن",    "H-NEW-60 i'jam table"),
    ("two_dot",            "",    "ت ق ي",                  "H-NEW-60 i'jam table"),
    ("three_dot",          "",    "ث ش",                    "H-NEW-60 i'jam table"),
    # phonotactic classes, H-NEW-69 side-test
    ("sonorant",           "",    "ر ل م ن و ي",            "H-NEW-69 phonotactic side-test"),
    ("stops_69",           "",    "ا ب ت د ط ك ق",          "H-NEW-69 side-test; = H-NEW-165 stops"),
    ("fricatives_69",      "",    "ث ح خ ذ ز س ش ص ض ظ ع غ ف ه", "H-NEW-69 phonotactic side-test"),
    # corpus frequency strata, H-NEW-1810
    ("freq_top14",         "",    "ا ل ن م ي و ه ت ر ب ك ع ف ق", "H-NEW-1810 rank 1-14"),
    ("freq_top7",          "",    "ا ل ن م ي و ه",          "H-NEW-1810 rank 1-7"),
    ("freq_bottom7",       "",    "ض ز ث ط غ ظ ص",          "H-NEW-1810 rank 22-28"),
    # H-NEW-165 locked codebook
    ("idhlaq",             "",    "ف ر م ن ل ب",            "al-Khalil's 6 fluent letters; H-NEW-165"),
    ("pharyngealized_165", "",    "خ ص ض ط ظ غ ق ع ح",      "H-NEW-165 locked codebook"),
    ("mahmus_165",         "",    "ص ك ه س ح ق ش ث ف ت خ",  "H-NEW-165 locked codebook"),
    # al-Suyuti's makharij, al-Itqan nawʿ 38 (groups of >=2 not already listed)
    ("makhraj_wasat_al_halq", "", "ع ح",                    "al-Suyuti, al-Itqan nawʿ 38"),
    ("makhraj_adna_al_halq",  "", "غ خ",                    "al-Suyuti, al-Itqan nawʿ 38"),
    ("makhraj_wasat_al_lisan", "", "ج ش ي",                 "al-Suyuti, al-Itqan nawʿ 38"),
    ("makhraj_shafatan",   "",    "ب م و",                  "al-Suyuti, al-Itqan nawʿ 38"),
]


def build_menu():
    """Deduplicate by identity and by complement; a tail/balance event on C is the
    identical event on C^c, so keeping both would let a set claim one axis twice."""
    univ = set(ALPHABET28)
    seen, axes = {}, []
    for name, _sp, letters, src in MENU:
        c = frozenset(letters.replace(" ", ""))
        assert c <= univ and c, f"{name}: letters outside the 28-letter alphabet"
        canon = min(tuple(sorted(c)), tuple(sorted(univ - c)))
        if canon in seen:
            axes[seen[canon]]["aliases"].append(name)
            continue
        seen[canon] = len(axes)
        axes.append({"name": name, "letters": "".join(sorted(c)), "size": len(c),
                     "source": src, "set": c, "aliases": []})
    return axes


def hyper(k, K, N=28, n=14):
    return math.comb(K, k) * math.comb(N - K, n - k) / math.comb(N, n)


def axis_events(K):
    """For every attainable k, the TAIL and BALANCE acceptance sets and their exact
    probabilities. E = K/2 by symmetry (n/N = 1/2)."""
    lo, hi = max(0, 14 - (28 - K)), min(K, 14)
    ks = list(range(lo, hi + 1))
    pmf = {k: hyper(k, K) for k in ks}
    E = K / 2.0
    ev = {}
    for k in ks:
        tail = [j for j in ks if j >= k] if k >= E else [j for j in ks if j <= k]
        bal = [j for j in ks if abs(j - E) <= abs(k - E) + 1e-12]
        ev[k] = {"tail": (frozenset(tail), sum(pmf[j] for j in tail)),
                 "balance": (frozenset(bal), sum(pmf[j] for j in bal))}
    return ev


def best_claim(k, ev):
    """The reference set's better claim on this axis: whichever event is rarer."""
    t_set, t_p = ev[k]["tail"]
    b_set, b_p = ev[k]["balance"]
    return ("tail", t_set, t_p) if t_p <= b_p else ("balance", b_set, b_p)


# ---------------------------------------------------------------------------
# EXACT per-axis count columns over all C(28,14) subsets
# ---------------------------------------------------------------------------

def build_columns(axes):
    A, B = ALPHABET28[:14], ALPHABET28[14:]
    T = len(axes)

    def half(letters):
        memb = np.zeros((14, T), dtype=np.int8)
        for i, ch in enumerate(letters):
            for t, ax in enumerate(axes):
                if ch in ax["set"]:
                    memb[i, t] = 1
        by = {}
        for j in range(15):
            idx = list(__import__("itertools").combinations(range(14), j))
            by[j] = (memb[np.array(idx, dtype=np.int64)].sum(axis=1)
                     if idx else np.zeros((1, T), np.int8))
        return by

    ha, hb = half(A), half(B)
    cols = [np.empty(N_SUBSETS, dtype=np.int8) for _ in range(T)]
    pos = 0
    for j in range(15):
        a, b = ha[j], hb[14 - j]
        na, nb = a.shape[0], b.shape[0]
        for t in range(T):
            blk = (a[:, t][:, None] + b[:, t][None, :]).ravel()
            cols[t][pos:pos + blk.size] = blk
        pos += na * nb
    assert pos == N_SUBSETS, f"enumerated {pos}, expected {N_SUBSETS}"
    return cols


def profile_survivors(cols, claims):
    """claims: list of (axis_index, acceptance_frozenset, p), most restrictive first."""
    t0, acc0, _ = claims[0]
    c0 = cols[t0]
    mask = np.zeros(c0.shape[0], dtype=bool)
    for v in acc0:
        mask |= (c0 == v)
    sel = np.flatnonzero(mask)
    for t, acc, _ in claims[1:]:
        if sel.size == 0:
            break
        col = cols[t][sel]
        m = np.zeros(sel.size, dtype=bool)
        for v in acc:
            m |= (col == v)
        sel = sel[m]
    return int(sel.size)


def pick_and_count(cols, axes, EV, X):
    ks = [len(X & ax["set"]) for ax in axes]
    claims = []
    for t, (ax, k) in enumerate(zip(axes, ks)):
        kind, acc, p = best_claim(k, EV[t])
        claims.append((t, acc, p, kind, ax["name"], k))
    claims.sort(key=lambda c: c[2])
    chosen = claims[:N_PICK]
    w = profile_survivors(cols, [(c[0], c[1], c[2]) for c in chosen])
    return w, [{"axis": c[4], "size": axes[c[0]]["size"], "k": c[5], "kind": c[3],
                "p": c[2]} for c in chosen]


def main():
    t0 = time.time()
    with open(PREREG, "rb") as fh:
        got = hashlib.sha256(fh.read()).hexdigest()
    if got != PREREG_SHA256:
        raise SystemExit(f"PRE-REG SHA MISMATCH — refusing to run.\n  expected {PREREG_SHA256}"
                         f"\n  actual   {got}\nThe locked pre-registration must be untouched.")
    print(f"[gate] pre-reg SHA-256 unchanged: {got}")
    primary = json.load(open(PRIMARY_JSON, encoding="utf-8"))
    assert primary["joint"]["W_all_11"] == 7, "primary run W changed"
    assert set(primary["muqattaat"]["letters"]) == MUQ14, "muqattaat-14 mismatch"

    axes = build_menu()
    print(f"[menu] {len(MENU)} listed axes -> {len(axes)} after complement/identity dedup")
    for ax in axes:
        if ax["aliases"]:
            print(f"    {ax['name']} absorbs {ax['aliases']} (identical or complementary)")
    EV = [axis_events(ax["size"]) for ax in axes]

    t = time.time()
    cols = build_columns(axes)
    print(f"[exact] {len(axes)} count-columns over {N_SUBSETS:,} subsets in {time.time()-t:.1f}s")

    # sanity: the muqattaat's own values must reproduce the published ones
    kmap = {ax["name"]: len(MUQ14 & ax["set"]) for ax in axes}
    for nm, want in (("dotless", 11), ("poa_pharyngeal_glottal", 4), ("sonorant", 5),
                     ("freq_top14", 10), ("mahmusa", 5), ("mutbaqa", 2), ("bayniyya", 5)):
        assert kmap[nm] == want, f"axis {nm}: {kmap[nm]} != {want}"
    print("[check] muqattaat axis values reproduce H-NEW-60 / 44.2.1 / 69 / 1810 / 2550")

    W_obs, obs_picks = pick_and_count(cols, axes, EV, MUQ14)
    print(f"\n[OBS] muqattaat-14, free choice of its own best {N_PICK} axes: W' = {W_obs:,}")
    for p in obs_picks:
        print(f"    {p['axis']:<24} |f|={p['size']:>2}  k={p['k']:>2}  {p['kind']:<7} "
              f"p={p['p']:.6f}")

    results = {}
    for sd in (SEED, SEED_REPLICATION):
        rr = random.Random(sd)
        Ws = []
        for _ in range(N_CONTROL):
            R = set(rr.sample(ALPHABET28, 14))
            w, _ = pick_and_count(cols, axes, EV, R)
            Ws.append(w)
        Wa = np.array(Ws, dtype=np.int64)
        q = float((Wa <= W_obs).sum()) / N_CONTROL
        results[str(sd)] = {
            "q_frac_random_at_least_as_unique": q,
            "n_random_le_W_obs": int((Wa <= W_obs).sum()),
            "min": int(Wa.min()), "q1": float(np.percentile(Wa, 25)),
            "median": float(np.median(Wa)), "q3": float(np.percentile(Wa, 75)),
            "max": int(Wa.max()), "mean": float(Wa.mean()),
            "n_eq_1": int((Wa == 1).sum()), "n_le_7": int((Wa <= 7).sum()),
            "n_le_10": int((Wa <= 10).sum()), "n_le_100": int((Wa <= 100).sum()),
        }
        print(f"[control'] seed {sd}: q'={q:.3f}  random W': min={Wa.min():,} "
              f"med={np.median(Wa):,.0f} max={Wa.max():,}  #(W'=1)={int((Wa==1).sum())}  "
              f"#(W'<=7)={int((Wa<=7).sum())}")

    q_primary = results[str(SEED)]["q_frac_random_at_least_as_unique"]
    verdict = "SUPPLEMENTARY-CONTROL-PASSED" if q_primary < 0.05 else \
              "SUPPLEMENTARY-CONTROL-FAILED — near-uniqueness is an artefact of free axis choice"
    print(f"\n[SUPPLEMENTARY VERDICT] q' = {q_primary:.3f}  ->  {verdict}")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = os.path.join(ROOT, "runs", "h-new-2670", stamp + "-supplementary-control")
    os.makedirs(run_dir, exist_ok=True)
    payload = {
        "finding_id": "H-NEW-2670",
        "component": "SUPPLEMENTARY CONTROL (post-observation, MW-7-capped, demote-only)",
        "date": "2026-08-07", "author": "Waiel Al-Shujaa",
        "run_utc": stamp, "prereg_sha256_unchanged": got,
        "menu": [{k: v for k, v in ax.items() if k != "set"} for ax in axes],
        "n_menu_axes": len(axes), "n_picked": N_PICK,
        "muqattaat_axis_values": kmap,
        "W_obs_free_choice": W_obs, "obs_picks": obs_picks,
        "W_obs_declared_11_primary_run": primary["joint"]["W_all_11"],
        "control": results, "q_primary": q_primary, "verdict": verdict,
        "runtime_seconds": round(time.time() - t0, 1),
    }
    for p in (OUT_JSON, os.path.join(run_dir, "supplementary-control.json")):
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
    print(f"[done] {OUT_JSON}\n[done] {run_dir}  ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()
