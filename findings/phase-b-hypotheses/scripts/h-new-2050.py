#!/usr/bin/env python3
"""
H-NEW-2050 — Within-surah verse-length symmetry + central-pivot detection.

Rules-tuple:
  (no-tashkeel, word=whitespace-token, words-per-verse,
   basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)

For each surah, build the verse-length sequence L = (L_1, ..., L_n) where
L_i = whitespace-token count of verse i. Compute three POSITION-DEPENDENT
statistics that prior verse-length tests (H-NEW-35 ACF, H-NEW-43 FFT,
H-NEW-181 Ljung-Box) are blind to:

  S_pal  = Pearson r between L and reverse(L)            (length-palindrome)
  S_piv  = 1 - min(centre-dist of longest, of shortest)  (central-pivot)
  S_grad = |Spearman rho(index, length)|                 (monotone gradient)

Null = verse-order shuffle (same length multiset, scrambled order), 10,000
perms per surah, seed 20260509. One-tailed p per surah per statistic.

Verdict (PRE-COMMIT):
  H1 = >=3 surahs significant palindrome OR pivot (Bonferroni-corrected)
  H2 = >=3 surahs significant gradient (Bonferroni-corrected)

Named targets: Q 55, Q 78, Q 81 (reported regardless).

Outputs JSON to findings/phase-b-hypotheses/csv/h-new-2050.json
Runtime: a few minutes (114 surahs x 10,000 perms, vectorised in numpy).
"""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

PRE_REG_PATH = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/"
    "prereg-h-new-2050-verse-length-symmetry.md"
)
EXPECTED_SHA = "a3215dc92eb91c8519aa3ba12eddebb729731400705e1d0d1707ef361f79221a"

QURAN_PATH = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
OUT_PATH = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-2050.json"
)

SEED = 20260509
SEED_REPL = 20260510
N_PERM = 10000
MIN_N_PAL = 7   # palindrome needs >=3 mirror pairs + a centre
MIN_N_PIV = 5
MIN_N_GRAD = 5
NAMED_TARGETS = (55, 78, 81)


def verify_prereg_sha():
    h = hashlib.sha256(PRE_REG_PATH.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH:\n  expected: {EXPECTED_SHA}\n  observed: {h}\n"
        )
        sys.exit(1)
    return h


def load_surahs():
    """Return list of dicts: {id, name, translit, type, lengths_words, lengths_letters}.

    L_i = number of whitespace tokens in verse i (no-tashkeel).
    Letters = grapheme count with whitespace stripped (sensitivity replication).
    Basmala: Q 1 v.1 counts as a verse (it is in the JSON). For Q 2..114 the
    JSON verse list already follows Hafs numbering (no separate basmala verse).
    """
    data = json.loads(QURAN_PATH.read_text())
    out = []
    for s in data:
        words = []
        letters = []
        for v in s["verses"]:
            t = v["text"].strip()
            toks = t.split()
            words.append(len(toks))
            letters.append(len(t.replace(" ", "")))
        out.append({
            "id": s["id"],
            "name": s["name"],
            "translit": s.get("transliteration", ""),
            "type": s.get("type", ""),
            "n": len(words),
            "lengths_words": np.array(words, dtype=float),
            "lengths_letters": np.array(letters, dtype=float),
        })
    return out


# ---------------------------------------------------------------------------
# Position statistics (vectorised over a (P, n) matrix of orderings)
# ---------------------------------------------------------------------------

def s_pal_vec(M):
    """Mirror Pearson r for each row of M (P x n). Returns length-P array.

    r between row and its reverse. Constant rows -> 0 (no symmetry signal)."""
    rev = M[:, ::-1]
    a = M - M.mean(axis=1, keepdims=True)
    b = rev - rev.mean(axis=1, keepdims=True)
    num = (a * b).sum(axis=1)
    den = np.sqrt((a * a).sum(axis=1) * (b * b).sum(axis=1))
    out = np.zeros(M.shape[0])
    nz = den > 0
    out[nz] = num[nz] / den[nz]
    return out


def s_piv_vec(M):
    """Central-pivot statistic for each row. 1 = an extremum sits dead-centre.

    Tie-rule: among argmax/argmin candidates pick the one closest to centre."""
    P, n = M.shape
    c = (n + 1) / 2.0           # 1-indexed centre
    half = (n - 1) / 2.0 if n > 1 else 1.0
    idx = np.arange(1, n + 1)   # 1-indexed positions
    centredist = np.abs(idx - c)  # length n

    out = np.empty(P)
    for r in range(P):
        row = M[r]
        # longest: among all argmax positions, pick min centre-distance
        mx = row.max()
        cand_long = centredist[row == mx]
        d_long = cand_long.min() / half
        mn = row.min()
        cand_short = centredist[row == mn]
        d_short = cand_short.min() / half
        out[r] = 1.0 - min(d_long, d_short)
    return out


def s_grad_vec(M):
    """|Spearman rho(index, length)| for each row. index is fixed 1..n."""
    P, n = M.shape
    idx_rank = np.arange(1, n + 1, dtype=float)  # ranks of fixed index 1..n
    idx_rank_c = idx_rank - idx_rank.mean()
    idx_den = np.sqrt((idx_rank_c * idx_rank_c).sum())
    # rank each row (average ranks for ties)
    out = np.empty(P)
    for r in range(P):
        lr = rankdata_avg(M[r])
        lrc = lr - lr.mean()
        den = idx_den * np.sqrt((lrc * lrc).sum())
        out[r] = 0.0 if den == 0 else abs((idx_rank_c * lrc).sum() / den)
    return out


def rankdata_avg(a):
    """Average-rank (ties get mean rank). Pure-numpy, like scipy.stats.rankdata."""
    a = np.asarray(a)
    order = a.argsort(kind="mergesort")
    ranks = np.empty(len(a), dtype=float)
    sa = a[order]
    i = 0
    n = len(a)
    while i < n:
        j = i
        while j + 1 < n and sa[j + 1] == sa[i]:
            j += 1
        avg = (i + j) / 2.0 + 1.0  # 1-indexed average rank
        ranks[order[i:j + 1]] = avg
        i = j + 1
    return ranks


def shuffled_matrix(L, n_perm, rng):
    """(n_perm+1, n) matrix: row0 = observed L, rows 1.. = shuffled orderings."""
    n = len(L)
    M = np.empty((n_perm + 1, n))
    M[0] = L
    for p in range(1, n_perm + 1):
        M[p] = rng.permutation(L)
    return M


def one_tailed_p(obs, null_vals):
    return (1 + int(np.sum(null_vals >= obs))) / (len(null_vals) + 1)


def analyse_surah(L, n_perm, rng):
    """Return dict of obs stats + one-tailed p per statistic (where defined)."""
    n = len(L)
    M = shuffled_matrix(L, n_perm, rng)
    res = {"n": n}

    if n >= MIN_N_PAL:
        v = s_pal_vec(M)
        res["S_pal"] = float(v[0])
        res["p_pal"] = one_tailed_p(v[0], v[1:])
    else:
        res["S_pal"] = None
        res["p_pal"] = None

    if n >= MIN_N_PIV:
        v = s_piv_vec(M)
        res["S_piv"] = float(v[0])
        res["p_piv"] = one_tailed_p(v[0], v[1:])
        # descriptive: which extremum, and its position
        c = (n + 1) / 2.0
        half = (n - 1) / 2.0 if n > 1 else 1.0
        idx = np.arange(1, n + 1)
        cd = np.abs(idx - c)
        mx = L.max(); mn = L.min()
        d_long = cd[L == mx].min() / half
        d_short = cd[L == mn].min() / half
        res["pivot_kind"] = "longest" if d_long <= d_short else "shortest"
        res["longest_pos"] = int(np.argmax(L) + 1)
        res["shortest_pos"] = int(np.argmin(L) + 1)
        res["d_long"] = float(d_long)
        res["d_short"] = float(d_short)
    else:
        res["S_piv"] = None
        res["p_piv"] = None

    if n >= MIN_N_GRAD:
        v = s_grad_vec(M)
        res["S_grad"] = float(v[0])
        res["p_grad"] = one_tailed_p(v[0], v[1:])
        rho_signed = signed_spearman(np.arange(1, n + 1, dtype=float), L)
        res["grad_sign"] = "lengthening" if rho_signed > 0 else "shortening"
    else:
        res["S_grad"] = None
        res["p_grad"] = None

    return res


def signed_spearman(x, y):
    xr = rankdata_avg(x); yr = rankdata_avg(y)
    xc = xr - xr.mean(); yc = yr - yr.mean()
    den = np.sqrt((xc * xc).sum() * (yc * yc).sum())
    return 0.0 if den == 0 else (xc * yc).sum() / den


def main():
    print("[H-NEW-2050] verifying pre-reg SHA...")
    h = verify_prereg_sha()
    print(f"  SHA OK: {h}")

    print("[H-NEW-2050] loading corpus...")
    surahs = load_surahs()
    total_verses = sum(s["n"] for s in surahs)
    print(f"  n_surahs = {len(surahs)}, total verses = {total_verses}")
    assert len(surahs) == 114, "expected 114 surahs"
    assert total_verses == 6236, f"expected 6236 verses, got {total_verses}"

    # eligible set sizes for Bonferroni
    k_pal = sum(1 for s in surahs if s["n"] >= MIN_N_PAL)
    k_piv = sum(1 for s in surahs if s["n"] >= MIN_N_PIV)
    k_grad = sum(1 for s in surahs if s["n"] >= MIN_N_GRAD)
    k_max = max(k_pal, k_piv, k_grad)
    alpha_bon = 0.05 / (3 * k_max)
    print(f"  eligible: pal={k_pal} piv={k_piv} grad={k_grad}; k_max={k_max}")
    print(f"  alpha_bonferroni = 0.05/(3*{k_max}) = {alpha_bon:.3e}")

    results = {
        "finding_id": "H-NEW-2050",
        "prereg_sha256": EXPECTED_SHA,
        "rules_tuple": "(no-tashkeel, word=whitespace-token, words-per-verse, "
                       "basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)",
        "seed": SEED,
        "n_perm": N_PERM,
        "min_n": {"pal": MIN_N_PAL, "piv": MIN_N_PIV, "grad": MIN_N_GRAD},
        "n_surahs": len(surahs),
        "total_verses": total_verses,
        "eligible": {"pal": k_pal, "piv": k_piv, "grad": k_grad},
        "k_max": k_max,
        "alpha_bonferroni": alpha_bon,
        "per_surah": {},
    }

    rng = np.random.default_rng(SEED)
    print("[H-NEW-2050] running per-surah (words-per-verse)...")
    for s in surahs:
        r = analyse_surah(s["lengths_words"], N_PERM, rng)
        r["name"] = s["name"]
        r["translit"] = s["translit"]
        r["type"] = s["type"]
        results["per_surah"][s["id"]] = r

    # ---- Verdict assembly -------------------------------------------------
    def fires(r, stat):
        p = r.get(f"p_{stat}")
        return p is not None and p < alpha_bon

    pal_hits = [sid for sid, r in results["per_surah"].items() if fires(r, "pal")]
    piv_hits = [sid for sid, r in results["per_surah"].items() if fires(r, "piv")]
    grad_hits = [sid for sid, r in results["per_surah"].items() if fires(r, "grad")]
    h1_set = sorted(set(pal_hits) | set(piv_hits))
    h1 = len(h1_set) >= 3
    h2 = len(grad_hits) >= 3

    if h1 and h2:
        verdict = "PASS — within-surah length-architecture CONFIRMED"
    elif h1 or h2:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL — no within-surah positional length-architecture beyond chance"

    results["verdict"] = {
        "H1_palindrome_or_pivot_hits": h1_set,
        "H1_fires": h1,
        "H2_gradient_hits": sorted(grad_hits),
        "H2_fires": h2,
        "palindrome_hits": sorted(pal_hits),
        "pivot_hits": sorted(piv_hits),
        "verdict": verdict,
    }
    print(f"  H1 hits (pal|piv): {h1_set}  -> H1={h1}")
    print(f"  H2 hits (grad):    {sorted(grad_hits)}  -> H2={h2}")
    print(f"  VERDICT: {verdict}")

    # ---- Rankings (descriptive) ------------------------------------------
    def rank_by(stat):
        rows = [(sid, r[f"S_{stat}"], r[f"p_{stat}"], r["n"], r["translit"])
                for sid, r in results["per_surah"].items()
                if r.get(f"S_{stat}") is not None]
        rows.sort(key=lambda x: -x[1])
        return [{"surah": sid, "S": round(S, 4), "p": p, "n": n, "name": nm}
                for sid, S, p, n, nm in rows[:15]]
    results["rankings"] = {
        "palindrome_top15": rank_by("pal"),
        "pivot_top15": rank_by("piv"),
        "gradient_top15": rank_by("grad"),
    }

    # ---- Named targets (Q55/78/81) ---------------------------------------
    named = {}
    for sid in NAMED_TARGETS:
        r = results["per_surah"][sid]
        named[sid] = {
            "name": r["name"], "translit": r["translit"], "n": r["n"],
            "S_pal": r["S_pal"], "p_pal": r["p_pal"],
            "S_piv": r["S_piv"], "p_piv": r["p_piv"],
            "S_grad": r["S_grad"], "p_grad": r["p_grad"],
            "grad_sign": r.get("grad_sign"),
            "pivot_kind": r.get("pivot_kind"),
            "longest_pos": r.get("longest_pos"),
            "shortest_pos": r.get("shortest_pos"),
            "fires_pal": fires(r, "pal"),
            "fires_piv": fires(r, "piv"),
            "fires_grad": fires(r, "grad"),
        }
    results["named_targets"] = named

    # ---- MW-5 replication: named targets at seed2 + letters --------------
    print("[H-NEW-2050] MW-5 replication (seed2 + letters) on named + hits...")
    repl_ids = sorted(set(NAMED_TARGETS) | set(h1_set) | set(grad_hits))
    smap = {s["id"]: s for s in surahs}
    repl = {}
    rng2 = np.random.default_rng(SEED_REPL)
    for sid in repl_ids:
        s = smap[sid]
        r2 = analyse_surah(s["lengths_words"], N_PERM, rng2)        # seed2, words
        rl = analyse_surah(s["lengths_letters"], N_PERM,
                           np.random.default_rng(SEED))             # letters
        repl[sid] = {
            "words_seed2": {"p_pal": r2["p_pal"], "p_piv": r2["p_piv"], "p_grad": r2["p_grad"]},
            "letters_seed1": {"p_pal": rl["p_pal"], "p_piv": rl["p_piv"], "p_grad": rl["p_grad"]},
        }
    results["replication"] = repl

    # ---- MW-6 negative control -------------------------------------------
    # random-length-multiset surah drawn iid from corpus verse-length dist.
    print("[H-NEW-2050] MW-6 negative control...")
    all_lengths = np.concatenate([s["lengths_words"] for s in surahs])
    ctrl_rng = np.random.default_rng(SEED + 1)
    ctrl_ps = {"pal": [], "piv": [], "grad": []}
    for _ in range(20):
        n_ctrl = int(ctrl_rng.integers(20, 120))
        Lc = ctrl_rng.choice(all_lengths, size=n_ctrl, replace=True)
        rc = analyse_surah(Lc, 2000, ctrl_rng)
        ctrl_ps["pal"].append(rc["p_pal"])
        ctrl_ps["piv"].append(rc["p_piv"])
        ctrl_ps["grad"].append(rc["p_grad"])
    results["negative_control"] = {
        "n_control_surahs": 20,
        "min_p_pal": min(ctrl_ps["pal"]),
        "min_p_piv": min(ctrl_ps["piv"]),
        "min_p_grad": min(ctrl_ps["grad"]),
        "any_fires_at_bonferroni": any(
            (p is not None and p < alpha_bon)
            for lst in ctrl_ps.values() for p in lst
        ),
    }
    print(f"  control min-p: pal={results['negative_control']['min_p_pal']} "
          f"piv={results['negative_control']['min_p_piv']} "
          f"grad={results['negative_control']['min_p_grad']}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(results, ensure_ascii=False, indent=2))
    print(f"[H-NEW-2050] wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
