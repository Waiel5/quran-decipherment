#!/usr/bin/env python3
"""H-NEW-3150 — is sighat al-mubalagha over-represented at the fasila beyond rhyme
shape, divine-name presence and the hapax slot?

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3150-mubalagha-fasila.md
The SHA-256 of that file is embedded below and verified at runtime.
"""

import bisect
import collections
import hashlib
import json
import math
import os
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-3150-mubalagha-fasila.md"
EXPECTED_PREREG_SHA = "968cbdf44294b451dae11727ca4463880142970047816a407f20d0f5ccb25437"

QAC = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
NAMES = ROOT / "data/asma-al-husna.txt"
WAZN_TSV = ROOT / "findings/classical-sources/99-names-wazn-classification.tsv"

SEED = 20260509
N_PERM = 10000
K_CONFIRMATORY = 6
ALPHA_BONF = 0.05 / K_CONFIRMATORY          # 0.008333
RAW_GATE = 0.001                            # binding
RARE_ROOT_MAX = 3
N_BINS = 5                                  # quintiles (prereg sec.4)


def verify_prereg():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_PREREG_SHA:
        raise SystemExit(
            f"PRE-REG SHA MISMATCH — refusing to run.\n"
            f"  expected = {EXPECTED_PREREG_SHA}\n  actual   = {actual}"
        )
    print(f"pre-reg SHA verified: {EXPECTED_PREREG_SHA[:16]}...")


# --------------------------------------------------------------------------- #
# Buckwalter / Arabic
# --------------------------------------------------------------------------- #
BW2AR = {"'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ",
         "}": "ئ", "A": "ا", "b": "ب", "p": "ة", "t": "ت",
         "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د",
         "*": "ذ", "r": "ر", "z": "ز", "s": "س", "$": "ش",
         "S": "ص", "D": "ض", "T": "ط", "Z": "ظ", "E": "ع",
         "g": "غ", "_": "ـ", "f": "ف", "q": "ق", "k": "ك",
         "l": "ل", "m": "م", "n": "ن", "h": "ه", "w": "و",
         "Y": "ى", "y": "ي", "F": "ً", "N": "ٌ", "K": "ٍ",
         "a": "َ", "u": "ُ", "i": "ِ", "~": "ّ", "o": "ْ",
         "`": "ٰ", "{": "ٱ"}
DIAC = set("ًٌٍَُِّْٰ")
DAGGER = "ٰ"


def bw2ar(s):
    return "".join(BW2AR.get(c, c) for c in s)


def norm_lemma(lem):
    """Strip sun-letter assimilation: '~' straight after radical 1, no vowel between."""
    return lem[0] + lem[2:] if len(lem) > 1 and lem[1] == "~" else lem


def bare(ar, dagger_as="ا"):
    s = ar.replace(DAGGER, dagger_as)
    s = "".join(c for c in s if c not in DIAC)
    for a, b in (("ٱ", "ا"), ("أ", "ا"), ("إ", "ا"),
                 ("آ", "ا"), ("ى", "ي"), ("ة", "ه"),
                 ("ـ", "")):
        s = s.replace(a, b)
    return s


def strip_al(w):
    return w[2:] if w.startswith("ال") else w


# --------------------------------------------------------------------------- #
# Machine wazn (prereg sec.3.2)
# --------------------------------------------------------------------------- #
MUBALAGHA6 = {"Fa''al", "Fa'ul", "Fu'ul", "Mif'al", "Fa'il_long", "Fu''al"}
MUB_STRICT = MUBALAGHA6 - {"Fa'il_long"}
LABEL = {"Fa''al": "Faʿʿāl", "Fa'ul": "Faʿūl",
         "Fu'ul": "Fuʿūl", "Mif'al": "Mifʿāl",
         "Fa'il_long": "Faʿīl", "Fu''al": "Fuʿʿāl",
         "Fa'il_short": "Faʿil", "Fa'l": "Faʿl", "Fa'al": "Faʿal",
         "Fa'lan": "Faʿlān", "Fa''ul": "Faʿʿūl",
         "Fu''ul": "Fuʿʿūl", "Fa'il_act": "Fāʿil",
         "Muf'il": "Mufʿil", "Mufa''il": "Mufaʿʿil",
         "Mutafa''il": "Mutafaʿʿil", "Mufa'il": "Mufāʿil",
         "Mufta'il": "Muftaʿil", "Af'al": "Afʿal"}


def templates(a, b, c, gem):
    t = {
        "Fa'il_long":  [f"{a}a{b}iy{c}"],
        "Fa''al":      [f"{a}a{b}~aA{c}"],
        "Fa'ul":       [f"{a}a{b}uw{c}"],
        "Fu'ul":       [f"{a}u{b}uw{c}"],
        "Fu''ul":      [f"{a}u{b}~uw{c}"],
        "Fu''al":      [f"{a}u{b}~aA{c}"],
        "Fa''ul":      [f"{a}a{b}~uw{c}"],
        "Mif'al":      [f"mi{a}o{b}aA{c}"],
        "Fa'il_act":   [f"{a}aA{b}i{c}"],
        "Muf'il":      [f"mu{a}o{b}i{c}"],
        "Mufa''il":    [f"mu{a}a{b}~i{c}"],
        "Mutafa''il":  [f"muta{a}a{b}~i{c}"],
        "Mufa'il":     [f"mu{a}aA{b}i{c}"],
        "Mufta'il":    [f"mu{a}ota{b}i{c}"],
        "Af'al":       [f">a{a}o{b}a{c}"],
        "Fa'l":        [f"{a}a{b}o{c}"],
        "Fa'al":       [f"{a}a{b}a{c}"],
        "Fa'il_short": [f"{a}a{b}i{c}"],
        "Fa'lan":      [f"{a}a{b}o{c}aAn"],
    }
    if gem:  # c2 == c3 : the identical radicals merge under a shadda
        t["Fa'l"].append(f"{a}a{b}~")
        t["Fa'al"].append(f"{a}a{b}~")
        t["Fa'il_short"].append(f"{a}a{b}~")
        t["Af'al"].append(f">a{a}a{b}~")
        t["Fa'il_act"].append(f"{a}aA{b}~")
        t["Muf'il"].append(f"mu{a}i{b}~")
        t["Mufta'il"].append(f"mu{a}ota{b}~")
    return t


_wcache = {}


def machine_wazn(lem, root):
    """(label, n_template_hits); label None unless exactly one template matches."""
    k = (lem, root)
    if k in _wcache:
        return _wcache[k]
    if not root or len(root) != 3:
        _wcache[k] = (None, 0)
        return _wcache[k]
    a, b, c = root
    L = norm_lemma(lem)
    hits = sorted({n for n, f in templates(a, b, c, b == c).items() if L in f})
    _wcache[k] = (hits[0], 1) if len(hits) == 1 else (None, len(hits))
    return _wcache[k]


# --------------------------------------------------------------------------- #
# Rime class (prereg sec.5.2)
# --------------------------------------------------------------------------- #
LONGV = {"ا": "aa", "و": "uu", "ي": "ii"}
CONSGRP = {"ن": "N", "م": "M", "ر": "R", "ل": "L", "د": "D",
           "ب": "B", "ز": "Z", "ه": "H", "س": "S", "ع": "E",
           "ق": "Q", "ك": "K", "ت": "T"}


def rime_class(rime2):
    if len(rime2) < 2:
        return ("_", "_")
    return (LONGV.get(rime2[0], "-"), CONSGRP.get(rime2[1], "X"))


# --------------------------------------------------------------------------- #
# Data
# --------------------------------------------------------------------------- #
def load_frame():
    import re
    segs = []
    with open(QAC, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 4:
                continue
            loc = p[0].strip("()").split(":")
            feats = p[3]

            def g(pat):
                m = re.search(pat, feats)
                return m.group(1) if m else None

            segs.append(dict(s=int(loc[0]), v=int(loc[1]), w=int(loc[2]),
                             pos=g(r"POS:(\w+)"), lem=g(r"LEM:([^|]+)"),
                             root=g(r"ROOT:([^|]+)")))

    wmax, nseg = collections.defaultdict(int), collections.Counter()
    for x in segs:
        k = (x["s"], x["v"])
        wmax[k] = max(wmax[k], x["w"])
        nseg[k] += 1

    names = set()
    for raw in open(NAMES, encoding="utf-8"):
        l = " ".join(raw.strip().split())
        if l and not l.startswith("#") and len(l.split()) == 1:
            names.add(strip_al(l))

    rootfreq = collections.Counter(x["root"] for x in segs if x["root"])

    rows = []
    for x in segs:
        if x["pos"] not in ("N", "ADJ") or not x["lem"] or not x["root"]:
            continue
        wz, _ = machine_wazn(x["lem"], x["root"])
        if not wz:
            continue
        k = (x["s"], x["v"])
        ar = bw2ar(norm_lemma(x["lem"]))
        keys = {bare(ar, d) for d in ("ا", "")}
        keys |= {strip_al(z) for z in keys}
        b = bare(ar)
        rows.append(dict(s=x["s"], v=x["v"], w=x["w"], wazn=wz,
                         mub=int(wz in MUBALAGHA6), mub5=int(wz in MUB_STRICT),
                         final=int(x["w"] == wmax[k]),
                         nwords=wmax[k], nsegs=nseg[k],
                         divine=int(bool(keys & names)),
                         rime=b[-2:], rc=rime_class(b[-2:]),
                         root=x["root"], rootfreq=rootfreq[x["root"]],
                         pos=x["pos"]))
    nnom = collections.Counter((r["s"], r["v"]) for r in rows)
    for r in rows:
        r["nnom"] = nnom[(r["s"], r["v"])]
        r["rare"] = int(r["rootfreq"] <= RARE_ROOT_MAX)
    return rows, len(segs), len(wmax), collections.Counter(
        x["pos"] for x in segs if x["pos"])


def qbin(vals, k):
    s = sorted(vals)
    cuts = [s[int(len(s) * i / k)] for i in range(1, k)]
    return [bisect.bisect_left(cuts, v) for v in vals], cuts


# --------------------------------------------------------------------------- #
# Stratified permutation test
# --------------------------------------------------------------------------- #
def run_arm(rows, keys, labelfield, seed, n_perm):
    """Stratified label-shuffle. Returns the full result dict for one arm."""
    by = collections.defaultdict(list)
    for r, k in zip(rows, keys):
        by[k].append(r)

    obs = 0.0
    exp = 0.0
    var = 0.0
    smax = 0
    n_inf = 0
    n_tok = 0
    pools = []
    for k, grp in by.items():
        n = len(grp)
        m = sum(r[labelfield] for r in grp)
        f = sum(r["final"] for r in grp)
        if n < 2 or m in (0, n) or f in (0, n):
            continue
        n_inf += 1
        n_tok += n
        obs += sum(r[labelfield] * r["final"] for r in grp)
        exp += m * f / n
        var += (m * f * (n - f) * (n - m)) / (n * n * (n - 1))
        smax += min(m, f)
        pools.append(([r["final"] for r in grp], m))

    if n_inf == 0:
        return dict(n_inf=0, n_tok=0, obs=None, exp=None, sd=None, smax=0,
                    p_perm=None, p_perm_two=None, z_param=None, verdict="NO-INFORMATIVE-STRATA")

    sd = math.sqrt(var)
    rng = random.Random(seed)
    ge = 0
    le = 0
    null = []
    for _ in range(n_perm):
        tot = 0
        for finals, m in pools:
            idx = rng.sample(range(len(finals)), m)
            tot += sum(finals[i] for i in idx)
        null.append(tot)
        if tot >= obs:
            ge += 1
        if tot <= obs:
            le += 1
    p_hi = (1 + ge) / (1 + n_perm)
    p_lo = (1 + le) / (1 + n_perm)
    null.sort()
    return dict(
        n_inf=n_inf, n_tok=n_tok, obs=obs, exp=exp, sd=sd, smax=smax,
        p_perm=p_hi, p_perm_lo=p_lo, p_perm_two=min(1.0, 2 * min(p_hi, p_lo)),
        z_param=(obs - exp) / sd if sd > 0 else None,
        null_mean=sum(null) / len(null), null_sd=math.sqrt(
            sum((x - sum(null) / len(null)) ** 2 for x in null) / (len(null) - 1)),
        null_p025=null[int(0.025 * len(null))], null_p975=null[int(0.975 * len(null))],
        excess=obs - exp, rel_excess=(obs - exp) / exp if exp else None,
    )


def zq(p):
    lo, hi = -10.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if 0.5 * (1 + math.erf(mid / math.sqrt(2))) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main():
    verify_prereg()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outdir = ROOT / "findings/phase-b-hypotheses/runs/h-new-3150" / stamp
    os.makedirs(outdir, exist_ok=False)
    print(f"run dir: {outdir}")

    rows, n_segs, n_verses, posc = load_frame()
    print(f"QAC segments {n_segs}  verses {n_verses}  "
          f"ADJ {posc['ADJ']}  PN {posc['PN']}  N {posc['N']}")
    print(f"analysis frame: {len(rows)} machine-labelled nominal tokens")

    # ---- channel bins ------------------------------------------------------
    for ch, key in (("CH-W", "nwords"), ("CH-S", "nsegs"), ("CH-N", "nnom")):
        b, _ = qbin([r[key] for r in rows], N_BINS)
        for r, bi in zip(rows, b):
            r["bin_" + ch] = bi

    dv = {(r["s"], r["v"]) for r in rows if r["divine"]}
    sub = [r for r in rows if (r["s"], r["v"]) not in dv]
    for ch, key in (("CH-W", "nwords"), ("CH-S", "nsegs"), ("CH-N", "nnom")):
        b, _ = qbin([r[key] for r in sub], N_BINS)
        for r, bi in zip(sub, b):
            r["subbin_" + ch] = bi

    results = {}

    # ---- descriptive ladder A1..A5 ----------------------------------------
    for ch in ("CH-W", "CH-S", "CH-N"):
        for lvl in (1, 2, 3, 4, 5):
            keys = []
            for r in rows:
                k = []
                if lvl >= 2:
                    k.append(r["bin_" + ch])
                if lvl >= 3:
                    k.append(r["rare"])
                if lvl >= 4:
                    k.append(r["divine"])
                if lvl >= 5:
                    k.append(r["rc"])
                keys.append(tuple(k))
            results[f"A{lvl}|{ch}"] = run_arm(rows, keys, "mub", SEED, N_PERM)

    # ---- confirmatory C1..C6 ----------------------------------------------
    CONF = {}
    for i, ch in enumerate(("CH-W", "CH-S", "CH-N"), start=1):
        CONF[f"C{i}"] = ("A5|" + ch, results["A5|" + ch])
    for i, ch in enumerate(("CH-W", "CH-S", "CH-N"), start=4):
        keys = [(r["subbin_" + ch], r["rare"], r["rc"]) for r in sub]
        res = run_arm(sub, keys, "mub", SEED, N_PERM)
        results[f"A5DF|{ch}"] = res
        CONF[f"C{i}"] = ("A5DF|" + ch, res)

    # ---- sensitivity -------------------------------------------------------
    sens = {}
    for i, ch in enumerate(("CH-W", "CH-S", "CH-N"), start=1):   # S1 strict-5
        keys = [(r["bin_" + ch], r["rare"], r["divine"], r["rc"]) for r in rows]
        sens[f"S1|C{i}"] = run_arm(rows, keys, "mub5", SEED, N_PERM)
    for i, ch in enumerate(("CH-W", "CH-S", "CH-N"), start=4):
        keys = [(r["subbin_" + ch], r["rare"], r["rc"]) for r in sub]
        sens[f"S1|C{i}"] = run_arm(sub, keys, "mub5", SEED, N_PERM)

    for ch in ("CH-W", "CH-S", "CH-N"):                          # S2 deciles
        b, _ = qbin([r["nwords" if ch == "CH-W" else "nsegs" if ch == "CH-S"
                       else "nnom"] for r in rows], 10)
        keys = [(bi, r["rare"], r["divine"], r["rc"]) for r, bi in zip(rows, b)]
        sens[f"S2|{ch}"] = run_arm(rows, keys, "mub", SEED, N_PERM)

    for ch in ("CH-W", "CH-S", "CH-N"):                          # S3 raw rime
        keys = [(r["bin_" + ch], r["rare"], r["divine"], r["rime"]) for r in rows]
        sens[f"S3|{ch}"] = run_arm(rows, keys, "mub", SEED, N_PERM)

    adj = [r for r in rows if r["pos"] == "ADJ"]                 # S5 ADJ-only
    for ch in ("CH-W", "CH-S", "CH-N"):
        b, _ = qbin([r["nwords" if ch == "CH-W" else "nsegs" if ch == "CH-S"
                       else "nnom"] for r in adj], N_BINS)
        keys = [(bi, r["rare"], r["divine"], r["rc"]) for r, bi in zip(adj, b)]
        sens[f"S5|{ch}"] = run_arm(adj, keys, "mub", SEED, N_PERM)

    # S6 within-verse uniform-slot null (H-NEW-23 comparable), descriptive
    s6 = {}
    for name, pool in (("all", rows), ("divine_free", sub)):
        for lab in ("mub", "mub5"):
            toks = [r for r in pool if r[lab]]
            o = sum(r["final"] for r in toks)
            e = sum(1.0 / r["nwords"] for r in toks)
            var = sum((1.0 / r["nwords"]) * (1 - 1.0 / r["nwords"]) for r in toks)
            s6[f"{name}|{lab}"] = dict(n=len(toks), obs=o, exp=e,
                                       sd=math.sqrt(var),
                                       z=(o - e) / math.sqrt(var) if var else None,
                                       ratio=o / e if e else None)

    # ---- VERDICT (diffed line-by-line against prereg sec.7) ----------------
    z999, z80 = zq(1 - RAW_GATE), zq(0.80)
    conf_rows = []
    for cid in ("C1", "C2", "C3", "C4", "C5", "C6"):
        arm, r = CONF[cid]
        mde = (z999 + z80) * r["sd"]
        sstar = r["exp"] + z999 * r["sd"]
        untestable = sstar > r["smax"]
        positive = r["obs"] > r["exp"]
        passes = (positive and r["p_perm"] <= RAW_GATE and r["p_perm"] <= ALPHA_BONF)
        reversed_ = (r["obs"] < r["exp"] and r["p_perm_two"] <= ALPHA_BONF)
        conf_rows.append(dict(id=cid, arm=arm, obs=r["obs"], exp=r["exp"], sd=r["sd"],
                              excess=r["excess"], rel_excess=r["rel_excess"],
                              z_param=r["z_param"], p_perm=r["p_perm"],
                              p_perm_two=r["p_perm_two"], smax=r["smax"],
                              sstar=sstar, mde=mde, n_inf=r["n_inf"], n_tok=r["n_tok"],
                              untestable=untestable, positive=positive,
                              passes=passes, reversed=reversed_))

    n_pass = sum(c["passes"] for c in conf_rows)
    c13 = [c for c in conf_rows if c["id"] in ("C1", "C2", "C3")]
    c46 = [c for c in conf_rows if c["id"] in ("C4", "C5", "C6")]
    # prereg sec.7 final row: an UNTESTABLE arm "does not count as a NULL",
    # so the NULL determination is made over testable arms only.
    testable = [c for c in conf_rows if not c["untestable"]]
    verdicts = []
    if n_pass == 6:
        verdicts.append("CONFIRMED (PASS-RESIDUAL)")
    if all(c["passes"] for c in c13) and not all(c["passes"] for c in c46):
        verdicts.append("PASS-DIVINE-DEPENDENT")
    if 0 < n_pass < 6 and not (all(c["passes"] for c in c13)
                               and not all(c["passes"] for c in c46)):
        verdicts.append("PASS-PARTIAL")
    if testable and not any(c["passes"] for c in testable):
        verdicts.append("NULL")
    if any(c["reversed"] for c in conf_rows):
        verdicts.append("REVERSED -> EQUAL PROMINENCE")
    for c in conf_rows:
        if c["untestable"]:
            verdicts.append(f"UNTESTABLE-AT-THIS-N ({c['id']})")

    headline = max(conf_rows, key=lambda c: c["p_perm"])
    # "furthest from the others" operationalised as furthest from the upper median p
    _med = sorted(x["p_perm"] for x in conf_rows)[len(conf_rows) // 2]
    dominant = max(conf_rows, key=lambda c: abs(c["p_perm"] - _med))

    # ---- diagnostics -------------------------------------------------------
    diag = dict(
        n_segments=n_segs, n_verses=n_verses,
        pos_counts={k: v for k, v in posc.most_common(15)},
        frame_n=len(rows),
        n_final=sum(r["final"] for r in rows),
        tie_fraction_is_final=1 - sum(r["final"] for r in rows) / len(rows),
        n_mub=sum(r["mub"] for r in rows), n_mub5=sum(r["mub5"] for r in rows),
        n_divine=sum(r["divine"] for r in rows),
        n_divine_verses=len(dv), n_rare=sum(r["rare"] for r in rows),
        divine_free_tokens=len(sub),
        wazn_counts=dict(collections.Counter(LABEL[r["wazn"]] for r in rows)),
        rime_classes=len({r["rc"] for r in rows}),
    )

    payload = dict(
        finding="H-NEW-3150", utc=stamp, seed=SEED, n_perm=N_PERM,
        prereg_sha256=EXPECTED_PREREG_SHA, alpha_bonferroni=ALPHA_BONF,
        raw_gate=RAW_GATE, diagnostics=diag, ladder=results,
        confirmatory=conf_rows, sensitivity=sens, s6_uniform_slot=s6,
        verdicts=verdicts, headline=headline["id"],
        headline_p=headline["p_perm"], dominant_channel=dominant["arm"],
    )
    with open(outdir / "results.json", "x") as fh:
        json.dump(payload, fh, indent=2, default=str)
    with open(outdir / "frame.json", "x") as fh:
        json.dump(rows, fh, default=str)

    lines = []
    lines.append(f"H-NEW-3150  {stamp}  seed={SEED} n_perm={N_PERM}")
    lines.append(f"prereg sha {EXPECTED_PREREG_SHA}")
    lines.append("")
    lines.append(f"frame {len(rows)} tokens | final {diag['n_final']} "
                 f"({diag['n_final']/len(rows):.3%}) | tie fraction "
                 f"{diag['tie_fraction_is_final']:.1%}")
    lines.append(f"mub6 {diag['n_mub']} | strict5 {diag['n_mub5']} | "
                 f"divine {diag['n_divine']} | divine verses {diag['n_divine_verses']}")
    lines.append("")
    lines.append("LADDER (descriptive)")
    lines.append(f"{'arm':<12}{'n_inf':>6}{'n_tok':>7}{'obs':>8}{'exp':>9}"
                 f"{'excess':>8}{'rel':>8}{'z':>8}{'p_perm':>10}")
    for k in sorted(results):
        r = results[k]
        if r["obs"] is None:
            continue
        lines.append(f"{k:<12}{r['n_inf']:>6}{r['n_tok']:>7}{r['obs']:>8.0f}"
                     f"{r['exp']:>9.1f}{r['excess']:>8.1f}"
                     f"{r['rel_excess']:>8.1%}{r['z_param']:>8.2f}{r['p_perm']:>10.5f}")
    lines.append("")
    lines.append("CONFIRMATORY (k=6, raw gate 0.001, bonferroni 0.008333)")
    lines.append(f"{'id':<4}{'arm':<14}{'obs':>7}{'exp':>9}{'excess':>8}{'rel':>8}"
                 f"{'z':>7}{'p_perm':>10}{'S*':>8}{'S_max':>7}{'MDE':>7}  pass")
    for c in conf_rows:
        lines.append(f"{c['id']:<4}{c['arm']:<14}{c['obs']:>7.0f}{c['exp']:>9.1f}"
                     f"{c['excess']:>8.1f}{c['rel_excess']:>8.1%}{c['z_param']:>7.2f}"
                     f"{c['p_perm']:>10.5f}{c['sstar']:>8.1f}{c['smax']:>7}"
                     f"{c['mde']:>7.1f}  {c['passes']}")
    lines.append("")
    lines.append(f"HEADLINE (worst of C1-C6) = {headline['id']} p={headline['p_perm']:.5f}")
    lines.append(f"DOMINANT CHANNEL = {dominant['arm']}")
    lines.append(f"VERDICT = {' + '.join(verdicts)}")
    lines.append("")
    lines.append("SENSITIVITY")
    for k in sorted(sens):
        r = sens[k]
        if r["obs"] is None:
            lines.append(f"{k:<12} NO-INFORMATIVE-STRATA")
            continue
        lines.append(f"{k:<12} n_tok={r['n_tok']:>5} obs={r['obs']:>6.0f} "
                     f"exp={r['exp']:>7.1f} excess={r['excess']:>7.1f} "
                     f"rel={r['rel_excess']:>7.1%} z={r['z_param']:>6.2f} "
                     f"p={r['p_perm']:.5f}")
    lines.append("")
    lines.append("S6 within-verse uniform-slot null (H-NEW-23 comparable)")
    for k, r in s6.items():
        lines.append(f"  {k:<20} n={r['n']:>5} obs={r['obs']:>5} exp={r['exp']:>8.1f} "
                     f"ratio={r['ratio']:.3f} z={r['z']:+.2f}")
    txt = "\n".join(lines)
    with open(outdir / "report.txt", "x") as fh:
        fh.write(txt + "\n")
    print(txt)


if __name__ == "__main__":
    main()
