#!/usr/bin/env python3
"""H-NEW-3100: is the F-9 rasm divergence census decided by the dagger-alef convention?

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3100-rasm-divergence.md
Its SHA-256 is verified at runtime; mismatch is a SystemExit.
"""

import difflib
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import arabic_normaliser as AN  # noqa: E402

EXPECTED_PREREG_SHA = "18b76c99153931db928757eb81752145232da6929bf15c77dcaddca030929ae7"
PREREG = "findings/phase-b-hypotheses/prereg-h-new-3100-rasm-divergence.md"

SEED = 20260509
N_PERM = 10_000
TESTS_IN_FAMILY = 2                      # prereg §4: one test per convention
CORRECTED_GATE = 0.005
RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY      # 0.0025
REFERENCE_RR = 1.27                      # prereg §4.4, cross-finding-029 anchor 3

INPUTS = {
    "uthmani":  "data/alt-text/quran-uthmani-txt.txt",
    "simple":   "data/alt-text/quran-simple-txt.txt",
    "refs":     "quran-text/quran-no-tashkeel.json",
    "genre":    "findings/phase-b-hypotheses/csv/h-new-2500.json",
    "itqan":    "data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt",
    "prereg":   PREREG,
    "normaliser": "scripts/arabic_normaliser.py",
}


def sha256(path):
    h = hashlib.sha256()
    with open(os.path.join(ROOT, path), "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------- conventions
def bare_letter(tok):
    """Convention A: dagger alef is a LETTER. This is arabic_normaliser.bare."""
    return AN.bare(tok)


def bare_mark(tok):
    """Convention B: dagger alef is a MARK and is deleted (H-NEW-2740's reading)."""
    t = tok.replace("ٓ", "").replace(AN.TATWEEL + "ٔ", "ء")
    t = t.replace(AN.ALEF_WASLA, AN.ALEF)
    t = t.replace(AN.SUPERSCRIPT_ALEF, "")            # <- the whole difference
    t = unicodedata.normalize("NFC", t)
    out = []
    for ch in t:
        if ch in AN.TASHKEEL or ch in AN.QURANIC_ANNOTATION or ch == AN.TATWEEL:
            continue
        out.append("ءا" if ch == "آ" else ch)
    return "".join(out)


def dot_ya(s):
    """N2: undotted word-final yeh. Exceptionlessness is verified in arm 1."""
    return s.replace("ى", "ي")


CONVENTIONS = {"A_dagger_is_letter": bare_letter, "B_dagger_is_mark": bare_mark}


# ---------------------------------------------------------------- alignment
MAXK = 5
INF = float("inf")


def _keys(toks):
    return ([AN.bare(w) for w in toks],
            [dot_ya(AN.bare(w.replace("ۥ", "و").replace("ۦ", "ي"))) for w in toks],
            [AN.skeleton(w.replace("ۥ", "و").replace("ۦ", "ي")) for w in toks])


def align(ut, st):
    """DP token alignment. Levels: exact bare, rewritten bare, skeleton."""
    n, m = len(ut), len(st)
    KU, KS = _keys(ut), _keys(st)
    best = [[INF] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    best[n][m] = 0
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i == n and j == m:
                continue
            cands = []
            if i < n and j < m:
                for lv in range(3):
                    if KU[lv][i] == KS[lv][j]:
                        cands.append((lv, "MATCH", 1, 1)); break
                for lv in range(3):
                    acc, hit = "", None
                    for k in range(1, MAXK + 1):
                        if j + k > m: break
                        acc += KS[lv][j + k - 1]
                        if k > 1 and KU[lv][i] == acc: hit = k; break
                    if hit:
                        cands.append((1 + lv, f"MERGE_{lv}_{hit}", 1, hit)); break
                for lv in range(3):
                    acc, hit = "", None
                    for k in range(1, MAXK + 1):
                        if i + k > n: break
                        acc += KU[lv][i + k - 1]
                        if k > 1 and KS[lv][j] == acc: hit = k; break
                    if hit:
                        cands.append((1 + lv, f"SPLIT_{lv}_{hit}", hit, 1)); break
                cands.append((10, "SUBST", 1, 1))
            if i < n: cands.append((15, "DEL_U", 1, 0))
            if j < m: cands.append((15, "INS_S", 0, 1))
            for c, kind, di, dj in cands:
                nxt = best[i + di][j + dj]
                if nxt == INF: continue
                if c + nxt < best[i][j]:
                    best[i][j] = c + nxt; back[i][j] = (kind, di, dj)
    ops, i, j = [], 0, 0
    while (i, j) != (n, m):
        b = back[i][j]
        if b is None: break
        kind, di, dj = b
        ops.append((kind, i, di, j, dj)); i += di; j += dj
    return ops


# ---------------------------------------------------------------- typology
def _only_differ_in(u, s, ch):
    return u.replace(ch, "") == s.replace(ch, "")


HAMZA_ALL = "ءآأإؤئ"


def _fold_hamza(s):
    out = []
    for c in s:
        out.append("ء" if c in HAMZA_ALL else c)
    return "".join(out)


TYPES = [
    ("T1_HADHF_ALIF",   lambda u, s: _only_differ_in(u, s, "ا") and u.count("ا") < s.count("ا")),
    ("T2_HADHF_YA",     lambda u, s: _only_differ_in(u, s, "ي") and u.count("ي") < s.count("ي")),
    ("T3_HADHF_WAW",    lambda u, s: _only_differ_in(u, s, "و") and u.count("و") < s.count("و")),
    ("T4_HADHF_LAM",    lambda u, s: _only_differ_in(u, s, "ل") and u.count("ل") < s.count("ل")),
    ("T5_ZIYADA_ALIF",  lambda u, s: _only_differ_in(u, s, "ا") and u.count("ا") > s.count("ا")),
    ("T6_ZIYADA_WAW",   lambda u, s: _only_differ_in(u, s, "و") and u.count("و") > s.count("و")),
    ("T7_ZIYADA_YA",    lambda u, s: _only_differ_in(u, s, "ي") and u.count("ي") > s.count("ي")),
    ("T8_BADAL_YA_ALIF", lambda u, s: u.replace("ي", "ا") == s.replace("ي", "ا")),
    ("T9_BADAL_WAW_ALIF", lambda u, s: u.replace("و", "ا") == s.replace("و", "ا")),
    ("T10_HAMZ",        lambda u, s: _fold_hamza(u) == _fold_hamza(s)),
    ("T11_BADAL_OTHER", lambda u, s: len(u) == len(s)
                        and sum(a != b for a, b in zip(u, s)) == 1
                        and all(c not in "اويى" + HAMZA_ALL
                                for a, b in zip(u, s) if a != b for c in (a, b))),
]

COMBINED = (lambda u, s: _fold_hamza(u.replace("ي", "ا").replace("و", "ا").replace("ل", ""))
            == _fold_hamza(s.replace("ي", "ا").replace("و", "ا").replace("ل", "")))


def classify(u, s):
    fired = [name for name, pred in TYPES if pred(u, s)]
    if len(fired) == 1:
        return fired[0], "unambiguous"
    if len(fired) > 1:
        return fired[0], "ambiguous"
    if COMBINED(u, s):
        return "T12_MIXED", "mixed"
    return "UNASSIGNED", "unassigned"


def edit_signature(u, s):
    sm = difflib.SequenceMatcher(None, u, s, autojunk=False)
    return "|".join(f"{t}:{u[i1:i2]}>{s[j1:j2]}"
                    for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal")


def adjusted_rand(a, b):
    tab = defaultdict(int); ra = Counter(); rb = Counter()
    for x, y in zip(a, b):
        tab[(x, y)] += 1; ra[x] += 1; rb[y] += 1
    n = len(a)
    c2 = lambda k: k * (k - 1) / 2
    sij = sum(c2(v) for v in tab.values())
    sa = sum(c2(v) for v in ra.values()); sb = sum(c2(v) for v in rb.values())
    exp = sa * sb / c2(n); mx = (sa + sb) / 2
    return (sij - exp) / (mx - exp) if mx != exp else 1.0


# ---------------------------------------------------------------- inference
def hypergeom_null(strata, rng, n_perm):
    """Null distribution of the divergent-final count.

    Within a stratum, permuting divergence labels across its tokens makes the
    divergent-final count Hypergeometric(n, d, f). Strata are independent, so the
    total is a sum of hypergeometrics -- sampled exactly, not approximated.
    Strata with d == 0, d == n, f == 0 or f == n are invariant and contribute a
    constant; they are the uninformative ones and are counted as such.
    """
    const, ngood, nbad, nsamp = 0, [], [], []
    informative_tokens = 0
    for n, d, f in strata:
        if d == 0 or d == n or f == 0 or f == n:
            const += (d * f) // n if (d == 0 or f == 0) else (f if d == n else d)
            continue
        ngood.append(d); nbad.append(n - d); nsamp.append(f)
        informative_tokens += n
    if not ngood:
        return np.full(n_perm, const), const, 0, 0.0, 0.0
    ngood = np.array(ngood); nbad = np.array(nbad); nsamp = np.array(nsamp)
    # chunked over strata so the draw matrix never exceeds ~4M cells
    tot = np.full(n_perm, const, dtype=np.int64)
    step = max(1, 4_000_000 // n_perm)
    for a in range(0, len(ngood), step):
        b = min(a + step, len(ngood))
        tot += rng.hypergeometric(ngood[a:b], nbad[a:b], nsamp[a:b],
                                  size=(n_perm, b - a)).sum(axis=1)
    nn = ngood + nbad
    mu = float((ngood * nsamp / nn).sum()) + const
    var = float((ngood * nsamp * nbad * (nn - nsamp) / (nn * nn * (nn - 1))).sum())
    return tot, const, informative_tokens, mu, math.sqrt(var)


def rr_from_x(x, D, Nf, Nnf):
    if x <= 0 or D - x <= 0 or Nf == 0 or Nnf == 0:
        return float("nan")
    return (x / Nf) / ((D - x) / Nnf)


def run_arm2(pairs, conv_name, keyfn, channels, rng, log):
    """prereg 4: within-lexeme permutation, three length channels, worst is headline."""
    div = [keyfn(u) != keyfn(s) for _, _, u, s, _, _ in pairs]
    fin = [f for _, _, _, _, f, _ in pairs]
    lex = [AN.bare(s) for _, _, _, s, _, _ in pairs]
    D = sum(div); Nf = sum(fin); Nnf = len(pairs) - Nf
    x_obs = sum(1 for d, f in zip(div, fin) if d and f)
    rr_obs = rr_from_x(x_obs, D, Nf, Nnf)
    out = {"convention": conv_name, "n_pairs": len(pairs), "n_divergent": D,
           "n_final": Nf, "n_nonfinal": Nnf, "x_obs": x_obs, "RR_obs": rr_obs,
           "unconditioned_rate_final": x_obs / Nf,
           "unconditioned_rate_nonfinal": (D - x_obs) / Nnf,
           "channels": {}}
    for ch_name, ch_vals in channels.items():
        if ch_vals is None:
            key = lex
        else:
            q = np.quantile(np.array(ch_vals, dtype=float), [.2, .4, .6, .8])
            binned = np.searchsorted(q, np.array(ch_vals, dtype=float))
            key = [f"{l}|{b}" for l, b in zip(lex, binned)]
        agg = defaultdict(lambda: [0, 0, 0])
        for k, d, f in zip(key, div, fin):
            a = agg[k]; a[0] += 1; a[1] += d; a[2] += f
        strata = [tuple(v) for v in agg.values()]
        null, const, info_tok, mu, sd = hypergeom_null(strata, rng, N_PERM)
        ge = int((null >= x_obs).sum()); eq = int((null == x_obs).sum())
        p = (1 + ge) / (1 + N_PERM)
        tie_fraction = eq / N_PERM
        s_max = sum(min(d, f) for n, d, f in strata)
        rho = float(np.corrcoef(np.array(div, dtype=float),
                                np.array(ch_vals, dtype=float))[0, 1]) if ch_vals else None
        out["channels"][ch_name] = {
            "n_strata": len(strata), "informative_tokens": info_tok,
            "p": p, "tie_fraction": tie_fraction,
            "null_mean": mu, "null_sd": sd,
            "S_star": x_obs, "S_max": s_max,
            "rho_control_treatment": rho,
            "degenerate": tie_fraction > 0.5,
        }
        log(f"    [{conv_name}] {ch_name:22s} p={p:.4f} tie={tie_fraction:.4f} "
            f"info_tok={info_tok} S*={x_obs} S_max={s_max} rho={rho}")
    live = {k: v for k, v in out["channels"].items() if not v["degenerate"]}
    out["headline_p"] = max(v["p"] for v in live.values()) if live else None
    out["headline_channel"] = max(live, key=lambda k: live[k]["p"]) if live else None
    out["dominant_channel"] = max(
        (k for k in live if live[k]["rho_control_treatment"] is not None),
        key=lambda k: abs(live[k]["rho_control_treatment"]), default=None)
    # NULL branch: analytic MDE / power / S* vs S_max on the headline channel
    if out["headline_p"] is not None and out["headline_p"] >= RAW_GATE:
        hc = out["channels"][out["headline_channel"]]
        sd = hc["null_sd"]; mu = hc["null_mean"]
        from statistics import NormalDist
        z_a = NormalDist().inv_cdf(1 - RAW_GATE); z_b = NormalDist().inv_cdf(0.80)
        x_crit = mu + z_a * sd
        x_mde = mu + (z_a + z_b) * sd
        # RR corresponding to REFERENCE_RR, solved for x
        r = REFERENCE_RR
        x_ref = r * D * Nf / (Nnf + r * Nf)
        out["null_branch"] = {
            "MDE_x": x_mde, "MDE_RR": rr_from_x(x_mde, D, Nf, Nnf),
            "critical_x": x_crit,
            "power_at_reference_RR": float(NormalDist().cdf((x_ref - x_crit) / sd)),
            "reference_RR": r,
            "S_star": hc["S_star"], "S_max": hc["S_max"],
            "design_can_reject": bool(hc["S_max"] > x_crit),
        }
    return out


def verdict(a, b):
    """Transcribed line by line from prereg 4.3."""
    pa, pb = a["headline_p"], b["headline_p"]
    ra, rb = a["RR_obs"], b["RR_obs"]
    if pa is None or pb is None:
        return "DEGENERATE — a convention had no non-degenerate channel"
    ca = pa < RAW_GATE and ra > 1
    cb = pb < RAW_GATE and rb > 1
    if pa < RAW_GATE and ra < 1:
        return "REVERSE under convention A"
    if pb < RAW_GATE and rb < 1:
        return "REVERSE under convention B"
    if ca and cb:
        return "CONVENTION-STABLE PASS"
    if pa >= RAW_GATE and pb >= RAW_GATE:
        return "CONVENTION-STABLE NULL"
    return ("CONVENTION-DECIDED — clears under "
            + ("A_dagger_is_letter" if ca else "B_dagger_is_mark"))


# ---------------------------------------------------------------- main
def main():
    if sha256(PREREG) != EXPECTED_PREREG_SHA:
        raise SystemExit(f"PREREG SHA MISMATCH\n  expected {EXPECTED_PREREG_SHA}\n"
                         f"  actual   {sha256(PREREG)}")
    gate = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "arabic_normaliser.py")],
                          capture_output=True, text=True)
    if gate.returncode != 0:
        raise SystemExit("NORMALISER SELF-TEST FAILED — refusing to run\n" + gate.stdout)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(ROOT, "runs", "h-new-3100", stamp)
    os.makedirs(rundir, exist_ok=False)
    logf = open(os.path.join(rundir, "run.log"), "x", encoding="utf-8")

    def log(msg):
        print(msg); logf.write(msg + "\n"); logf.flush()

    log(f"H-NEW-3100  run {stamp}")
    log(f"prereg sha256 {EXPECTED_PREREG_SHA} VERIFIED")
    log("normaliser self-test PASS (exit 0)")
    manifest = {"id": "H-NEW-3100", "run": stamp, "seed": SEED, "n_perm": N_PERM,
                "prereg_sha256": EXPECTED_PREREG_SHA,
                "tests_in_family": TESTS_IN_FAMILY, "raw_gate": RAW_GATE,
                "input_sha256": {k: sha256(v) for k, v in INPUTS.items()},
                "python": platform.python_version(),
                "normaliser_selftest_stdout": gate.stdout}

    def load(p):
        return [l for l in open(os.path.join(ROOT, p), encoding="utf-8").read().splitlines()
                if l.strip() and not l.startswith("#")]

    U, S = load(INPUTS["uthmani"]), load(INPUTS["simple"])
    qj = json.load(open(os.path.join(ROOT, INPUTS["refs"]), encoding="utf-8"))
    R = [(s["id"], v["id"]) for s in qj for v in s["verses"]]
    genre = json.load(open(os.path.join(ROOT, INPUTS["genre"]),
                           encoding="utf-8"))["genre_proxy"]["surah_genre"]
    assert len(U) == len(S) == len(R), (len(U), len(S), len(R))
    log(f"verse lines {len(U)}  uthmani tokens {sum(len(l.split()) for l in U)}  "
        f"simple tokens {sum(len(l.split()) for l in S)}")

    # ---- align once, reuse everywhere
    pairs, merges = [], []
    for i, (ul, sl) in enumerate(zip(U, S)):
        ut, st = ul.split(), sl.split()
        vlen = len(ut)
        for kind, ii, di, jj, dj in align(ut, st):
            if di == 1 and dj == 1:
                pairs.append((i, ii, ut[ii], st[jj], ii == vlen - 1, vlen))
            elif kind.startswith("MERGE"):
                merges.append((i, f"{R[i][0]}:{R[i][1]}", kind, ut[ii],
                               " ".join(st[jj:jj + dj])))
    log(f"1:1 aligned pairs {len(pairs)}   merge sites {len(merges)}")

    # ---- ARM 1: descriptive census
    log("\n=== ARM 1 — descriptive census ===")
    arm1 = {"n_pairs": len(pairs), "n_merge_sites": len(merges), "conventions": {}}
    divsets = {}
    for cname, fn in CONVENTIONS.items():
        d = [(i, ii, u, s) for i, ii, u, s, _, _ in pairs if fn(u) != fn(s)]
        divsets[cname] = set((x[0], x[1]) for x in d)
        skel = set((fn(u), fn(s)) for _, _, u, s in d)
        arm1["conventions"][cname] = {"n_divergent": len(d),
                                      "rate": len(d) / len(pairs),
                                      "n_distinct_skeleton_pairs": len(skel)}
        log(f"  {cname:22s} divergent {len(d):6d}  rate {len(d)/len(pairs):.4%}  "
            f"distinct skeleton-pairs {len(skel)}")
    A, B = divsets["A_dagger_is_letter"], divsets["B_dagger_is_mark"]
    arm1["A_minus_B"], arm1["B_minus_A"], arm1["A_and_B"] = len(A - B), len(B - A), len(A & B)
    arm1["A_subset_of_B"] = (len(A - B) == 0)
    log(f"  A\\B {len(A-B)}   B\\A {len(B-A)}   A&B {len(A&B)}   A subset of B: {len(A-B)==0}")

    # N2 exceptionlessness, verified not assumed (prereg 5.2 / dot_ya)
    uth_final = Counter(); sim_final = Counter()
    for _, _, u, s, _, _ in pairs:
        bu, bs = AN.bare(u), AN.bare(s)
        if bu: uth_final[bu[-1]] += 1
        if bs: sim_final[bs[-1]] += 1
    arm1["N2_check"] = {"uthmani_final_maqsura": uth_final["ى"],
                        "uthmani_final_yeh": uth_final["ي"],
                        "simple_final_maqsura": sim_final["ى"],
                        "simple_final_yeh": sim_final["ي"]}
    log(f"  N2 check — uthmani word-final ى {uth_final['ى']} / ي {uth_final['ي']} ; "
        f"simple ى {sim_final['ى']} / ي {sim_final['ي']}")

    # lexical determinism, both conventions (H-NEW-2740's 95.74%)
    for cname, fn in CONVENTIONS.items():
        by_type = defaultdict(list)
        for _, _, u, s, _, _ in pairs:
            by_type[AN.bare(s)].append(fn(u) != fn(s))
        never = sum(1 for v in by_type.values() if not any(v))
        always = sum(1 for v in by_type.values() if all(v))
        alt = len(by_type) - never - always
        dv_tokens = sum(sum(v) for v in by_type.values())
        dv_invariant = sum(sum(v) for v in by_type.values() if all(v))
        arm1["conventions"][cname].update(
            {"types_total": len(by_type), "types_never": never,
             "types_always": always, "types_alternating": alt,
             "divergent_tokens": dv_tokens,
             "divergent_tokens_in_invariant_types": dv_invariant,
             "lexical_determinism": dv_invariant / dv_tokens if dv_tokens else None})
        log(f"  {cname:22s} types {len(by_type)}  never {never}  always {always}  "
            f"alternating {alt}  lexical determinism "
            f"{dv_invariant/dv_tokens:.4%}")

    # ---- ARM 3: typology over convention B
    log("\n=== ARM 3 — typology (convention B) ===")
    trows = []
    for i, ii, u, s, _, _ in pairs:
        bu, bs = dot_ya(bare_mark(u)), dot_ya(bare_mark(s))
        if bu == bs: continue
        t, status = classify(bu, bs)
        trows.append({"ref": f"{R[i][0]}:{R[i][1]}", "u": bu, "s": bs,
                      "type": t, "status": status, "sig": edit_signature(bu, bs),
                      "visible_under_A": (i, ii) in A})
    ntot = len(trows)
    cnt = Counter(r["type"] for r in trows)
    stat = Counter(r["status"] for r in trows)
    arm3 = {"n_divergent_B_after_N2": ntot,
            "n_types_defined": 12,
            "by_type": dict(cnt), "by_status": dict(stat),
            "unambiguous_fraction": stat["unambiguous"] / ntot,
            "ambiguous_fraction": stat["ambiguous"] / ntot,
            "mixed_fraction": stat["mixed"] / ntot,
            "unassigned_fraction": stat["unassigned"] / ntot}
    log(f"  divergent under B after N2: {ntot}")
    for t, n in cnt.most_common():
        vis = sum(1 for r in trows if r["type"] == t and r["visible_under_A"])
        arm3.setdefault("visible_under_A", {})[t] = vis
        log(f"    {t:22s} {n:6d}   visible under convention A: {vis}")
    log(f"  unambiguous {stat['unambiguous']/ntot:.4%}  ambiguous "
        f"{stat['ambiguous']/ntot:.4%}  mixed {stat['mixed']/ntot:.4%}  "
        f"unassigned {stat['unassigned']/ntot:.4%}")
    ua = [r for r in trows if r["status"] == "unambiguous"]
    arm3["ARI_vs_edit_signature"] = adjusted_rand([r["type"] for r in ua],
                                                  [r["sig"] for r in ua])
    bysig = defaultdict(Counter)
    for r in ua: bysig[r["sig"]][r["type"]] += 1
    arm3["purity"] = sum(c.most_common(1)[0][1] for c in bysig.values()) / len(ua)
    log(f"  ARI vs parameter-free edit-signature partition: "
        f"{arm3['ARI_vs_edit_signature']:.4f}   purity {arm3['purity']:.4f}")

    # ---- ARM 2: the registered inference
    log("\n=== ARM 2 — within-lexeme verse-final enrichment, both conventions ===")
    vlen = [v for _, _, _, _, _, v in pairs]
    surah_of = [R[i][0] for i, _, _, _, _, _ in pairs]
    mvl = {}
    for sid in set(surah_of):
        idx = [k for k, s in enumerate(surah_of) if s == sid]
        mvl[sid] = float(np.mean([vlen[k] for k in idx]))
    channels = {"C0_lexeme_only": None,
                "C1_verse_tokens": vlen,
                "C2_log_verse_tokens": [math.log(v) for v in vlen],
                "C3_surah_mean_verse_len": [mvl[s] for s in surah_of]}
    rng = np.random.default_rng(SEED)
    arm2 = {}
    for cname, fn in CONVENTIONS.items():
        arm2[cname] = run_arm2(pairs, cname, fn, channels, rng, log)
        log(f"  [{cname}] RR_obs={arm2[cname]['RR_obs']:.4f} "
            f"final rate {arm2[cname]['unconditioned_rate_final']:.4%} vs "
            f"{arm2[cname]['unconditioned_rate_nonfinal']:.4%} ; headline p="
            f"{arm2[cname]['headline_p']} on {arm2[cname]['headline_channel']} ; "
            f"dominant channel {arm2[cname]['dominant_channel']}")

    v = verdict(arm2["A_dagger_is_letter"], arm2["B_dagger_is_mark"])
    log(f"\n=== VERDICT: {v} ===")

    out = {"manifest": manifest, "arm1_census": arm1, "arm2_inference": arm2,
           "arm3_typology": arm3, "verdict": v,
           "merge_sites": [{"ref": r, "kind": k, "u": u, "s": s}
                           for _, r, k, u, s in merges]}
    with open(os.path.join(rundir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(rundir, "typology_rows.json"), "x", encoding="utf-8") as fh:
        json.dump(trows, fh, ensure_ascii=False, indent=1)
    log(f"\nartefacts written to runs/h-new-3100/{stamp}/")
    logf.close()


if __name__ == "__main__":
    main()
