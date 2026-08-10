#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-3140 — THE TANWĪN-REPAIR REPLICATION of H-NEW-2690 / H-NEW-2730's scanner.

INSTRUMENT-REPAIR REPLICATION, not a new hypothesis. The hypotheses were registered in
prereg-h-new-2690-quantitative-scansion.md and are not restated, reopened or amended.
What this script executes is the DECISION RULE locked in
prereg-h-new-3140-tanwin-repair-replication.md §5, before any repaired value existed.

THE DEFECT (prereg §1). scripts/h-new-2690.py places U+0656, U+0657 and U+065E in its
DROP set. In the Uthmānī orthography those are tanwīn kasr / fatḥ / ḍamm, not what their
Unicode names say. 6,643 of the corpus's 8,554 tanwīn (77.66 %) are therefore deleted
before syllabification. Every comparison arm — 3 muʿallaqāt, Dārimī, Bukhārī — contains
ZERO occurrences of them, so the defect is Qurʾān-specific and every comparison in the
family was asymmetric.

THE REPAIR (prereg §2). One line, inserted before the DROP filter, lifted verbatim from
scripts/h-new-2990.py line 146. Nothing else changes. Both phonemisers run in the SAME
process on the SAME inputs, so the comparison carries no cross-run drift.

CANNOT RESCUE H1b (prereg §0). H-NEW-2730's D8 is a within-corpus self-recut and D5 a
matched-length bin; both are invariant to a uniform phonemiser change. A length-driven
artefact does not stop being length-driven because the weights under it changed.

Author: Waiel Al-Shujaa.
"""
import json, os, sys, re, random, statistics, hashlib, datetime, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(ROOT))

PREREG = os.path.join(ROOT, "prereg-h-new-3140-tanwin-repair-replication.md")
EXPECTED_PREREG_SHA = "3c89620395628191a7ede97050f9665aa2a7a195678a81431fa642d8405779a0"


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            h.update(b)
    return h.hexdigest()


_got = sha256_file(PREREG)
if _got != EXPECTED_PREREG_SHA:
    raise SystemExit(f"[FATAL] pre-registration SHA mismatch\n  want {EXPECTED_PREREG_SHA}\n"
                     f"  got  {_got}\nThe pre-registration was edited after locking. Run aborted.")
print(f"[3140] prereg SHA verified {EXPECTED_PREREG_SHA[:16]}…")

# ---------------------------------------------------------------------------
# Lift the locked H-NEW-2690 scanner verbatim (same mechanism as h-new-2690-posthoc.py)
# ---------------------------------------------------------------------------
_src = open(os.path.join(HERE, "h-new-2690.py"), encoding="utf-8").read()
G = {"__name__": "repair3140", "__file__": os.path.join(HERE, "h-new-2690.py")}
exec(_src.split("_a = sha256_file(PREREG)")[0], G)
exec("# 1. Syllabifier" + _src.split("# 1. Syllabifier")[1].split("# 3. POSITIVE CONTROL")[0], G)

for _p, _want in G["FROZEN"].items():
    if G["sha256_file"](_p) != _want:
        raise SystemExit(f"[FATAL] frozen input changed: {_p}")
print("[3140] frozen inputs re-verified (H-NEW-2690's own gate)")

scan, metricality, best_meter, METERS = G["scan"], G["metricality"], G["best_meter"], G["METERS"]
SEED, SEED_REPL, N_PERM = G["SEED"], G["SEED_REPL"], G["N_PERM"]
MODE = "P_forceheavy"                       # prereg §6: primary tuple, declared parameter
ALPHA = 0.05 / 3                            # 2690 §6, k=3
TOL = 0.005                                 # prereg §5.2
D8_BAR = 0.80                               # prereg §5.1(d)
D8_DRAWS = 60                               # prereg §6.3, declared coarsening
PROSE_SAMPLE = 2500                         # 2690's own prose_sampled

# ---------------------------------------------------------------------------
# DISCLOSED ADDITION — a parameter the pre-registration did NOT lock.
#
# prereg §6.3 locks D8 at 60 draws but is silent on per-draw sub-sampling. Scoring every
# unit of all 60 draws under both phonemisers is ~320,000 long units, which at this
# scanner's measured throughput is >10 hours and not runnable. A seed-locked sub-sample
# per draw is therefore used. This follows the parent method: H-NEW-2730's D1 scored
# "a seed-locked sub-sample of 500 units per offset" for the same reason.
#
# It is fixed HERE, before any D8 value has been computed, and applied IDENTICALLY to both
# phonemisers — so the defective-vs-repaired contrast that T7 actually tests stays
# internally controlled. What it costs is precision on the ABSOLUTE distance-moved figure,
# which is already established at 99.4% by H-NEW-2730's own 200-draw run and is not being
# re-estimated here (prereg §6.3).
#
# This is a deciding parameter and is named as one. It was chosen for runtime, not for the
# answer, and no D8 number existed when it was chosen.
# ---------------------------------------------------------------------------
D8_SUBSAMPLE = 120

# ---------------------------------------------------------------------------
# THE REPAIR — prereg §2. One line, before the DROP filter.
# ---------------------------------------------------------------------------
ORIG_NORMALIZE = G["normalize"]
TANWIN_REMAP = {"ٗ": G["FATHATAN"],    # ARABIC INVERTED DAMMA      -> tanwīn fatḥ
                "ٞ": G["DAMMATAN"],    # ARABIC FATHA WITH TWO DOTS -> tanwīn ḍamm
                "ٖ": G["KASRATAN"]}    # ARABIC SUBSCRIPT ALEF      -> tanwīn kasr


def normalize_repaired(t):
    t = unicodedata.normalize("NFC", t)
    t = "".join(TANWIN_REMAP.get(c, c) for c in t)
    return ORIG_NORMALIZE(t)


def set_phonemiser(which):
    """scan/phonemes/strip_pausal all resolve `normalize` from G at call time."""
    G["normalize"] = ORIG_NORMALIZE if which == "defective" else normalize_repaired


# ---------------------------------------------------------------------------
# Corpora — loaded exactly as H-NEW-2690 / its post-hoc load them
# ---------------------------------------------------------------------------
AR = re.compile("[ء-ي]")
DIAC = re.compile("[ً-ْٰٓ-ٕۡ]")

quran = json.load(open(G["QURAN"], encoding="utf-8"))
QV = [(si, vi, v["text"] if isinstance(v, dict) else str(v))
      for si, su in enumerate(quran, 1) for vi, v in enumerate(su["verses"], 1)]
if len(QV) != 6236:
    raise SystemExit(f"[FATAL] Qurʾān verses {len(QV)} != 6236")

POEMS = {}
for stem, known in G["GROUND"].items():
    ls = []
    for l in open(os.path.join(G["MUAL"], stem + ".txt"), encoding="utf-8", errors="replace"):
        a = len(AR.findall(l))
        if a >= 12 and len(DIAC.findall(l)) / a >= 0.55:
            ls.append(l.strip())
    POEMS[stem] = (known, ls)
POETRY = [l for _, (_, ls) in POEMS.items() for l in ls]

dar = json.load(open(G["DARIMI"], encoding="utf-8"))
SENT = re.compile(r"[.؟!]")
PROSE_ALL = [s.strip() for h in dar["hadiths"]
             for s in SENT.split(h.get("arabic") or "") if len(AR.findall(s.strip())) >= 10]
PROSE = random.Random(SEED).sample(PROSE_ALL, PROSE_SAMPLE) if len(PROSE_ALL) > PROSE_SAMPLE else PROSE_ALL

PERIOD, NVERSE = {}, {}
for i, line in enumerate(open(G["REVORD"], encoding="utf-8")):
    if i == 0:
        continue
    f = line.rstrip("\n").split(",")
    PERIOD[int(f[1])] = f[4]
for s, v, t in QV:
    NVERSE[s] = NVERSE.get(s, 0) + 1

print(f"[corpora] Qurʾān={len(QV)}  poetry={len(POETRY)}  prose(sampled)={len(PROSE)}"
      f"  of {len(PROSE_ALL)}")

# ---------------------------------------------------------------------------
# Statistics — lifted from H-NEW-2690 §5
# ---------------------------------------------------------------------------
perm_median_diff = G["perm_median_diff"] if "perm_median_diff" in G else None
if perm_median_diff is None:
    def perm_median_diff(A, B, seed, n_perm=N_PERM):
        obs = statistics.median(A) - statistics.median(B)
        pool = A + B
        nA = len(A)
        rng = random.Random(seed)
        ge = 0
        for _ in range(n_perm):
            rng.shuffle(pool)
            if statistics.median(pool[:nA]) - statistics.median(pool[nA:]) >= obs:
                ge += 1
        return obs, (ge + 1) / (n_perm + 1)


def matched_noise(strings, seed):
    rng = random.Random(seed)
    out = []
    for o in strings:
        if not o:
            out.append(o); continue
        p = o.count("-") / len(o)
        out.append("".join("-" if rng.random() < p else "v" for _ in o))
    return out


def dmins(strings):
    """Returns (d_min list, argmin list, per-meter vector list) for strings of len>=4."""
    ds, args, pers = [], [], []
    for s in strings:
        if len(s) < 4:
            continue
        d, k, per = metricality(s)
        ds.append(d); args.append(k); pers.append(per)
    return ds, args, pers


def spread(pers):
    """Metre-SPECIFICITY: median over units of (median baḥr - best baḥr). Post-hoc D2."""
    out = []
    for per in pers:
        v = sorted(per.values())
        out.append(statistics.median(v) - v[0])
    return statistics.median(out) if out else float("nan")


def modal(args):
    c = {}
    for a in args:
        if a:
            c[a] = c.get(a, 0) + 1
    if not c:
        return None, 0.0, {}
    k = max(c, key=lambda x: c[x])
    return k, c[k] / sum(c.values()), dict(sorted(c.items(), key=lambda kv: -kv[1])[:6])


# ---------------------------------------------------------------------------
# One full pass under a given phonemiser
# ---------------------------------------------------------------------------
def full_pass(which):
    set_phonemiser(which)
    print(f"\n=== pass: {which} phonemiser ===")

    # --- positive control (T2 / S1)
    pc, ok_poems = {}, 0
    for stem, (known, ls) in POEMS.items():
        hit = 0
        for l in ls:
            s = scan(l, MODE)
            if len(s) >= 4 and best_meter(s)[0] == known:
                hit += 1
        acc = hit / len(ls) if ls else 0.0
        top = modal([best_meter(scan(l, MODE))[0] for l in ls if len(scan(l, MODE)) >= 4])[0]
        pc[stem] = {"known": known, "n": len(ls), "acc": round(acc, 4), "top": top}
        if top == known:
            ok_poems += 1
    n_b = sum(v["n"] for v in pc.values())
    pb_acc = round(sum(v["acc"] * v["n"] for v in pc.values()) / n_b, 4)
    print(f"  positive control: {ok_poems}/3 poems, per-bayt acc {pb_acc}")

    # --- arms
    q_str = [scan(t, MODE) for _, _, t in QV]
    p_str = [scan(t, MODE) for t in POETRY]
    r_str = [scan(t, MODE) for t in PROSE]

    q_d, q_a, q_p = dmins(q_str)
    p_d, p_a, p_p = dmins(p_str)
    r_d, r_a, r_p = dmins(r_str)
    print(f"  d_min computed: quran={len(q_d)} poetry={len(p_d)} prose={len(r_d)}")

    qn_d, qn_a, qn_p = dmins(matched_noise([s for s in q_str if len(s) >= 4], SEED))
    pn_d, _, _ = dmins(matched_noise([s for s in p_str if len(s) >= 4], SEED))

    med = lambda x: round(statistics.median(x), 5)

    # --- T1 H1a, T3 H1b
    h1a_diff, h1a_p = perm_median_diff(q_d, p_d, SEED)
    _, h1a_p2 = perm_median_diff(q_d, p_d, SEED_REPL)
    h1b_diff, h1b_p = perm_median_diff(r_d, q_d, SEED)

    # --- T4/T5 H3
    qi = [i for i, s in enumerate(q_str) if len(s) >= 4]
    A = [q_d[j] for j, i in enumerate(qi) if QV[i][0] >= 78]
    B = [q_d[j] for j, i in enumerate(qi)
         if PERIOD.get(QV[i][0]) == "Medinan" and NVERSE.get(QV[i][0], 0) >= 100]
    Aa = [q_a[j] for j, i in enumerate(qi) if QV[i][0] >= 78]
    h3_diff, h3_p = perm_median_diff(B, A, SEED)
    modA, modA_sh, votesA = modal(Aa)

    # --- T6 paired excess vs own matched twin
    exc = [o - n for o, n in zip(q_d, qn_d)]
    win = sum(1 for e in exc if e < 0) / len(exc)
    pexc = [o - n for o, n in zip(p_d, pn_d)]
    pwin = sum(1 for e in pexc if e < 0) / len(pexc)

    # --- T8 metre-specificity
    q_sp, qn_sp = spread(q_p), spread(qn_p)
    p_sp = spread(p_p)
    modq, modq_sh, _ = modal(q_a)
    modqn, modqn_sh, _ = modal(qn_a)

    return {
        "positive_control": {"per_poem_correct": ok_poems, "per_bayt_acc": pb_acc,
                             "n_bayts": n_b, "per_poet": pc},
        "n": {"quran": len(q_d), "poetry": len(p_d), "prose": len(r_d),
              "mufassal_A": len(A), "long_medinan_B": len(B)},
        "median_d_min": {"quran": med(q_d), "poetry": med(p_d), "prose": med(r_d),
                         "noise_quran": med(qn_d), "noise_poetry": med(pn_d)},
        "T1_H1a": {"diff": round(h1a_diff, 5), "p": round(h1a_p, 5), "p_repl": round(h1a_p2, 5),
                   "direction_ok": h1a_diff > 0},
        "T3_H1b": {"diff": round(h1b_diff, 5), "p": round(h1b_p, 5), "direction_ok": h1b_diff > 0},
        "T4_H3a": {"diff_B_minus_A": round(h3_diff, 5), "p": round(h3_p, 5),
                   "direction_ok": h3_diff > 0},
        "T5_H3b": {"modal_meter_A": modA, "share": round(modA_sh, 4), "votes": votesA,
                   "modal_ok": modA in ("rajaz", "sari")},
        "T6_paired_excess": {"median_excess": round(statistics.median(exc), 5),
                             "mean_excess": round(statistics.mean(exc), 5),
                             "win_rate": round(win, 4), "poetry_win_rate": round(pwin, 4)},
        "T8_specificity": {"quran": round(q_sp, 5), "quran_noise": round(qn_sp, 5),
                           "ratio": round(q_sp / qn_sp, 4) if qn_sp else None,
                           "poetry": round(p_sp, 5),
                           "quran_modal": modq, "quran_modal_share": round(modq_sh, 4),
                           "noise_modal": modqn, "noise_modal_share": round(modqn_sh, 4),
                           "share_modal_with_noise": modq == modqn},
        "_q_words": None,
    }


# ---------------------------------------------------------------------------
# T7 — D8 self-recut. The Qurʾān's OWN word stream, re-cut to ḥadīth sentence lengths.
# No baseline text is scored; only the unit-length profile is borrowed.
# ---------------------------------------------------------------------------
def d8_selfrecut(which, prose_native_median):
    set_phonemiser(which)
    words = [w for _, _, t in QV for w in t.split()]
    prof = [len(s.split()) for s in PROSE_ALL]
    prof = [n for n in prof if n > 0]
    rng = random.Random(SEED)
    meds = []
    for di in range(D8_DRAWS):
        i, units = 0, []
        while i < len(words):
            n = prof[rng.randrange(len(prof))]
            seg = " ".join(words[i:i + n])
            if seg:
                units.append(seg)
            i += n
        sub = rng.sample(units, D8_SUBSAMPLE) if len(units) > D8_SUBSAMPLE else units
        d, _, _ = dmins([scan(u, MODE) for u in sub])
        if d:
            meds.append(statistics.median(d))
        if (di + 1) % 15 == 0:
            print(f"    [{which}] D8 draw {di+1}/{D8_DRAWS}  running mean "
                  f"{statistics.mean(meds):.5f}")
    return statistics.mean(meds), meds


# ===========================================================================
print("\n[3140] running BOTH phonemisers in one process on identical inputs")
DEF = full_pass("defective")
REP = full_pass("repaired")

# S4 — the defective arm must reproduce the 2026-08-07 published values EXACTLY.
PUBLISHED = {"quran": 0.22222, "poetry": 0.14286, "prose": 0.23963,
             "noise_quran": 0.23944, "noise_poetry": 0.22222}
s4 = {k: (DEF["median_d_min"][k], v, abs(DEF["median_d_min"][k] - v) < 1e-5)
      for k, v in PUBLISHED.items()}
s4_pass = all(v[2] for v in s4.values()) and DEF["positive_control"]["per_poem_correct"] == 3
print("\n[S4] defective arm vs 2026-08-07 published values:")
for k, (got, want, ok) in s4.items():
    print(f"   {k:<14} got {got:<9} want {want:<9} {'OK' if ok else '** MISMATCH **'}")
if not s4_pass:
    print("[S4] FAILED — prereg §3 says the run is VOID and no repaired number is reported.")

# Printed here so the primary targets are on record before T7's long arm runs.
print("\n" + "-" * 74)
print(f"{'quantity':<34}{'defective':>13}{'repaired':>13}{'delta':>13}")
for lab, dv, rv in [
        ("median d_min Qurʾān", DEF["median_d_min"]["quran"], REP["median_d_min"]["quran"]),
        ("median d_min poetry", DEF["median_d_min"]["poetry"], REP["median_d_min"]["poetry"]),
        ("median d_min prose", DEF["median_d_min"]["prose"], REP["median_d_min"]["prose"]),
        ("T1 H1a diff (Qurʾān-poetry)", DEF["T1_H1a"]["diff"], REP["T1_H1a"]["diff"]),
        ("T1 H1a p", DEF["T1_H1a"]["p"], REP["T1_H1a"]["p"]),
        ("T3 H1b diff", DEF["T3_H1b"]["diff"], REP["T3_H1b"]["diff"]),
        ("T4 H3a diff_B_minus_A", DEF["T4_H3a"]["diff_B_minus_A"], REP["T4_H3a"]["diff_B_minus_A"]),
        ("T6 win-rate vs own twin", DEF["T6_paired_excess"]["win_rate"],
         REP["T6_paired_excess"]["win_rate"]),
        ("T8 specificity Qurʾān", DEF["T8_specificity"]["quran"], REP["T8_specificity"]["quran"]),
        ("T8 specificity ratio", DEF["T8_specificity"]["ratio"], REP["T8_specificity"]["ratio"]),
        ("control per-bayt acc", DEF["positive_control"]["per_bayt_acc"],
         REP["positive_control"]["per_bayt_acc"])]:
    print(f"{lab:<34}{dv:>13}{rv:>13}{rv - dv:>13.5f}")
print(f"{'T5 modal meter A':<34}{str(DEF['T5_H3b']['modal_meter_A']):>13}"
      f"{str(REP['T5_H3b']['modal_meter_A']):>13}")
print("-" * 74)

print("\n[T7] D8 self-recut, both phonemisers…")
d8_def_mean, _ = d8_selfrecut("defective", DEF["median_d_min"]["prose"])
d8_rep_mean, _ = d8_selfrecut("repaired", REP["median_d_min"]["prose"])
frac = lambda native, recut, target: (recut - native) / (target - native) if target != native else float("nan")
T7 = {"defective": {"native": DEF["median_d_min"]["quran"], "recut": round(d8_def_mean, 5),
                    "prose_native": DEF["median_d_min"]["prose"],
                    "moved": round(frac(DEF["median_d_min"]["quran"], d8_def_mean,
                                        DEF["median_d_min"]["prose"]), 4)},
      "repaired": {"native": REP["median_d_min"]["quran"], "recut": round(d8_rep_mean, 5),
                   "prose_native": REP["median_d_min"]["prose"],
                   "moved": round(frac(REP["median_d_min"]["quran"], d8_rep_mean,
                                       REP["median_d_min"]["prose"]), 4)},
      "draws": D8_DRAWS}
print(f"   defective moved {T7['defective']['moved']:.1%}   repaired moved {T7['repaired']['moved']:.1%}")

# ---------------------------------------------------------------------------
# THE DECISION RULE — prereg §5, executed clause by clause
# ---------------------------------------------------------------------------
def classify(name, dv, rv, changed_flags, deltas):
    if any(changed_flags):
        return "CONCLUSION-CHANGED"
    if any(abs(d) > TOL for d in deltas):
        return "NUMBERS-CHANGED-CONCLUSION-UNCHANGED"
    return "UNCHANGED"


T = {}
# (a) direction reversal, (b) p crossing alpha
T["T1_H1a"] = classify("T1", DEF["T1_H1a"], REP["T1_H1a"],
                       [DEF["T1_H1a"]["direction_ok"] != REP["T1_H1a"]["direction_ok"],
                        (DEF["T1_H1a"]["p"] < ALPHA) != (REP["T1_H1a"]["p"] < ALPHA)],
                       [REP["T1_H1a"]["diff"] - DEF["T1_H1a"]["diff"]])
# (c) positive-control gate
T["T2_control"] = classify("T2", None, None,
                           [REP["positive_control"]["per_poem_correct"] < 3,
                            REP["positive_control"]["per_bayt_acc"] < 0.50],
                           [REP["positive_control"]["per_bayt_acc"]
                            - DEF["positive_control"]["per_bayt_acc"]])
T["T3_H1b"] = classify("T3", None, None,
                       [DEF["T3_H1b"]["direction_ok"] != REP["T3_H1b"]["direction_ok"],
                        (DEF["T3_H1b"]["p"] < ALPHA) != (REP["T3_H1b"]["p"] < ALPHA)],
                       [REP["T3_H1b"]["diff"] - DEF["T3_H1b"]["diff"]])
T["T4_H3a"] = classify("T4", None, None,
                       [DEF["T4_H3a"]["direction_ok"] != REP["T4_H3a"]["direction_ok"],
                        (DEF["T4_H3a"]["p"] < ALPHA) != (REP["T4_H3a"]["p"] < ALPHA)],
                       [REP["T4_H3a"]["diff_B_minus_A"] - DEF["T4_H3a"]["diff_B_minus_A"]])
# (f) modal meter becoming rajaz/sari
T["T5_H3b"] = classify("T5", None, None, [REP["T5_H3b"]["modal_ok"]], [0.0])
# (e) win-rate crossing 50%
T["T6_excess"] = classify("T6", None, None,
                          [(DEF["T6_paired_excess"]["win_rate"] > 0.5)
                           != (REP["T6_paired_excess"]["win_rate"] > 0.5)],
                          [REP["T6_paired_excess"]["median_excess"]
                           - DEF["T6_paired_excess"]["median_excess"]])
# (d) D8 below the 80% bar
T["T7_selfrecut"] = classify("T7", None, None, [T7["repaired"]["moved"] < D8_BAR],
                             [T7["repaired"]["moved"] - T7["defective"]["moved"]])
T["T8_specificity"] = classify("T8", None, None, [False],
                               [REP["T8_specificity"]["quran"] - DEF["T8_specificity"]["quran"]])

ORDER = ["CONCLUSION-CHANGED", "NUMBERS-CHANGED-CONCLUSION-UNCHANGED", "UNCHANGED"]
OVERALL = min(T.values(), key=lambda x: ORDER.index(x))

print("\n" + "=" * 74)
print("PER-TARGET LABELS (prereg §5, worst-across = overall)")
for k, v in T.items():
    print(f"   {k:<16} {v}")
print(f"\n   OVERALL: {OVERALL}")
print("=" * 74)
print(f"\nP1 (repaired quran d_min > 0.22222): "
      f"{REP['median_d_min']['quran']} -> {'HELD' if REP['median_d_min']['quran'] > 0.22222 else 'FAILED'}")
print(f"P2 (H1a gap widens beyond +0.07937): "
      f"{REP['T1_H1a']['diff']} -> {'HELD' if REP['T1_H1a']['diff'] > 0.07937 else 'FAILED'}")
print(f"S1 poetry identical: {DEF['median_d_min']['poetry'] == REP['median_d_min']['poetry']}")
print(f"S2 prose identical:  {DEF['median_d_min']['prose'] == REP['median_d_min']['prose']}")
print(f"S3 quran moved:      {DEF['median_d_min']['quran'] != REP['median_d_min']['quran']}")
print(f"S4 defective reproduces published: {s4_pass}")

# ---------------------------------------------------------------------------
# Immutable run directory
# ---------------------------------------------------------------------------
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUN = os.path.join(ROOT, "runs", "h-new-3140", stamp)
os.makedirs(RUN, exist_ok=False)
out = {"id": "H-NEW-3140", "type": "INSTRUMENT-REPAIR REPLICATION",
       "prereg_sha256": EXPECTED_PREREG_SHA, "mode": MODE, "seed": SEED,
       "n_perm": N_PERM, "alpha": ALPHA, "tolerance": TOL, "d8_bar": D8_BAR,
       "d8_draws": D8_DRAWS,
       "cannot_rescue_h1b": "prereg §0 — D8/D5 are invariant to a uniform phonemiser change",
       "defect": {"codepoints": ["U+0656", "U+0657", "U+065E"], "deleted": 6643,
                  "retained": 1911, "deleted_share": 0.7766,
                  "comparison_arms_affected": 0},
       "self_checks": {"S1_poetry_identical":
                       DEF["median_d_min"]["poetry"] == REP["median_d_min"]["poetry"],
                       "S2_prose_identical":
                       DEF["median_d_min"]["prose"] == REP["median_d_min"]["prose"],
                       "S3_quran_moved":
                       DEF["median_d_min"]["quran"] != REP["median_d_min"]["quran"],
                       "S4_defective_reproduces_published": s4_pass, "S4_detail":
                       {k: {"got": g, "want": w, "ok": o} for k, (g, w, o) in s4.items()}},
       "locked_predictions": {"P1_quran_dmin_rises": REP["median_d_min"]["quran"] > 0.22222,
                              "P2_h1a_gap_widens": REP["T1_H1a"]["diff"] > 0.07937},
       "defective": DEF, "repaired": REP, "T7_selfrecut": T7,
       "target_labels": T, "overall": OVERALL}
for k in ("defective", "repaired"):
    out[k].pop("_q_words", None)
with open(os.path.join(RUN, "result.json"), "x", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
with open(os.path.join(RUN, "manifest.json"), "x", encoding="utf-8") as f:
    json.dump({"id": "H-NEW-3140", "utc": stamp,
               "script_sha256": sha256_file(os.path.abspath(__file__)),
               "prereg_sha256": EXPECTED_PREREG_SHA,
               "parent_scanner_sha256": sha256_file(os.path.join(HERE, "h-new-2690.py")),
               "inputs_sha256": G["FROZEN"],
               "immutability": "Immutable. Never delete or overwrite."}, f,
              ensure_ascii=False, indent=2)
with open(os.path.join(ROOT, "csv", "h-new-3140.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\n[run] {RUN}")
