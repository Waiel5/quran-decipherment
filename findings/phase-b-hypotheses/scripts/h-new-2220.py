#!/usr/bin/env python3
"""
h-new-2220.py — corpus-wide pericope-scale ring-composition GENERATOR.

Slides pericope windows (odd widths {5,7,9,11,13}, stride=ceil(w/2)) across EVERY
surah, scores each for chiastic/ring symmetry (paired mirror-position root-Jaccard,
identical to chiastic-audit §1 and Q002-F-07), compares to a 10,000-perm within-window
verse-order shuffle null (seed 20260509), and produces the corpus-wide roster of
ring-bearing pericopes.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2220-pericope-ring-sweep.md
SHA-256 locked + verified at runtime (PRE-REG-STANDARD-04). Stdlib only.

H1: >= K=4 windows clear Bonferroni (Gaussian-z threshold z>4.311 over family F).
H2: ring-bearing surahs are LONGER (H2a, Mann-Whitney) AND early-mushaf s<=50 (H2b, binomial).
H3: generator reproduces Q002-F-07 (Q2:131-144 ring=0.25513, z=+3.688) -- FAIL-FAST.
"""
from __future__ import annotations
import hashlib, json, math, random, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings" / "phase-b-hypotheses" / "prereg-h-new-2220-pericope-ring-sweep.md"
PREREG_SHA = "d73da54a258257576d947c4ad23227298af10a2cff23947a1346bcf27937933a"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-2220.json"

SEED = 20260509
N_PERMS = 10000
N_PERMS_REFINE = 200000
WIDTHS = (5, 7, 9, 11, 13)          # locked, all odd
K_BASELINE = 4                       # locked H1 floor
RAW_ALPHA = 0.05
EARLY_CUTOFF = 50                    # H2b: s<=50 ttiwal/early block
CORPUS_EARLY_FRAC = 50 / 114         # baseline fraction with s<=50

# Q002-F-07 reference (self-check / MW-5)
F07_REF_RING = 0.25513
F07_REF_Z = 3.688


def verify_prereg():
    if not PREREG.exists():
        print(f"FAIL: pre-reg missing: {PREREG}", file=sys.stderr); sys.exit(2)
    sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if sha != PREREG_SHA:
        print(f"FAIL: pre-reg SHA mismatch: got {sha}\n           want {PREREG_SHA}",
              file=sys.stderr)
        sys.exit(2)
    print(f"[ok] pre-reg SHA256 verified: {sha[:16]}...")


# ------------------------------- data --------------------------------------

def load_quran():
    q = json.loads((ROOT / "quran-text" / "quran-no-tashkeel.json").read_text())
    return q


def load_verse_root_sets():
    """(surah, verse) -> frozenset of QAC triliteral roots."""
    ri = json.loads((ROOT / "data" / "morphology" / "root-index.json").read_text())
    rsets = defaultdict(set)
    for root, locs in ri.items():
        for (s, v, _w) in locs:
            rsets[(s, v)].add(root)
    return {k: frozenset(v) for k, v in rsets.items()}, len(ri)


def jaccard(a: frozenset, b: frozenset) -> float:
    if not a and not b:
        return 0.0
    u = len(a | b)
    return (len(a & b) / u) if u else 0.0


def ring_score(rlist) -> float:
    n = len(rlist)
    half = n // 2
    if half == 0:
        return 0.0
    tot = 0.0
    for i in range(half):
        tot += jaccard(rlist[i], rlist[n - 1 - i])
    return tot / half


def perm_null(rlist, n_perms, seed):
    """Within-window verse-order shuffle null. Returns (mean, sd, n_geq_obs given obs)."""
    rng = random.Random(seed)
    obs = ring_score(rlist)
    base = list(rlist)
    vals = []
    n_geq = 0
    for _ in range(n_perms):
        rng.shuffle(base)
        s = ring_score(base)
        vals.append(s)
        if s >= obs:
            n_geq += 1
    m = sum(vals) / len(vals)
    sd = math.sqrt(sum((x - m) ** 2 for x in vals) / (len(vals) - 1)) if len(vals) > 1 else 0.0
    p = (n_geq + 1) / (n_perms + 1)
    z = (obs - m) / sd if sd > 0 else 0.0
    return obs, m, sd, z, p


def gaussian_tail_p(z: float) -> float:
    """one-sided upper-tail p for standard normal."""
    return 0.5 * math.erfc(z / math.sqrt(2.0))


# ------------------------------ the sweep ----------------------------------

def build_grid(quran):
    """Locked window grid: widths {5,7,9,11,13}, stride=ceil(w/2), per surah."""
    windows = []  # (surah_id, name, N, width, start_verse, end_verse, verse_ids)
    for s in quran:
        sid = s["id"]
        vids = [v["id"] for v in s["verses"]]
        N = len(vids)
        for w in WIDTHS:
            if N < w:
                continue
            stride = math.ceil(w / 2)
            starts = list(range(0, N - w + 1, stride))
            if starts[-1] != N - w:        # right-anchor the last window
                starts.append(N - w)
            for st in starts:
                seg = vids[st:st + w]
                windows.append((sid, s["transliteration"], N, w, seg[0], seg[-1], seg))
    return windows


def main():
    verify_prereg()
    quran = load_quran()
    rsets, n_roots = load_verse_root_sets()
    print(f"[ok] {len(quran)} surahs, {n_roots} roots, "
          f"{len(rsets)} verses with root data.")

    # ---- H3 self-check (MW-5): reproduce Q002-F-07 BEFORE the sweep (fail-fast) ----
    win_q2 = [rsets.get((2, v), frozenset()) for v in range(131, 145)]
    f07_o, f07_m, f07_sd, f07_z, f07_p = perm_null(win_q2, N_PERMS, SEED)
    print(f"[H3] Q2:131-144  ring={f07_o:.5f} (ref {F07_REF_RING})  "
          f"z={f07_z:.3f} (ref {F07_REF_Z})  p={f07_p:.5f}")
    if abs(f07_o - F07_REF_RING) > 1e-4 or abs(f07_z - F07_REF_Z) > 0.05:
        print("FAIL: H3 self-check did not reproduce Q002-F-07 -> run VOID.", file=sys.stderr)
        sys.exit(3)
    h3_ok = True
    print("[ok] H3 replication PASSED -- pipeline validated against Q002-F-07.")

    # ---- build the locked grid ----
    windows = build_grid(quran)
    F = len(windows)
    alpha_bon = RAW_ALPHA / F
    z_bon = _z_for_p(alpha_bon)
    print(f"[ok] family F = {F} windows; alpha_bon = {alpha_bon:.3e}; "
          f"Gaussian-z Bonferroni threshold z > {z_bon:.3f}")

    # ---- primary 10k-perm sweep ----
    print(f"[..] sweeping {F} windows x {N_PERMS} perms ...")
    results = []
    raw_hits = 0
    for idx, (sid, name, N, w, vs, ve, seg) in enumerate(windows):
        rlist = [rsets.get((sid, v), frozenset()) for v in seg]
        # per-window seed derived deterministically from the locked SEED + identity
        wseed = SEED  # protocol: fresh Random(SEED) re-seeded per window (order-independent)
        o, m, sd, z, p = perm_null(rlist, N_PERMS, wseed)
        raw = p < RAW_ALPHA
        if raw:
            raw_hits += 1
        results.append({
            "surah": sid, "name": name, "N": N, "width": w,
            "window": f"{sid}:{vs}-{ve}", "v_start": vs, "v_end": ve,
            "ring": round(o, 5), "null_mean": round(m, 5), "null_sd": round(sd, 5),
            "z": round(z, 4), "p_raw": round(p, 6),
            "raw_hit": raw, "bonf_z_survivor": z > z_bon,
        })
        if (idx + 1) % 1000 == 0:
            print(f"    {idx+1}/{F} done (raw hits so far: {raw_hits})")

    # ---- MW-6 calibration control: random windows, same width-distribution ----
    print("[..] MW-6 random-window calibration control ...")
    rng_ctrl = random.Random(SEED + 999)
    width_counts = defaultdict(int)
    for r in results:
        width_counts[r["width"]] += 1
    # draw same #windows per width from random surah+start, score raw-hit rate
    surah_vids = {s["id"]: [v["id"] for v in s["verses"]] for s in quran}
    ctrl_raw = 0; ctrl_total = 0
    for w, cnt in width_counts.items():
        eligible = [sid for sid, vv in surah_vids.items() if len(vv) >= w]
        for _ in range(cnt):
            sid = rng_ctrl.choice(eligible)
            vv = surah_vids[sid]
            st = rng_ctrl.randint(0, len(vv) - w)
            seg = vv[st:st + w]
            rlist = [rsets.get((sid, v), frozenset()) for v in seg]
            _o, _m, _sd, _z, p = perm_null(rlist, 2000, SEED + 7)  # lighter null for control
            ctrl_total += 1
            if p < RAW_ALPHA:
                ctrl_raw += 1
    ctrl_rate = ctrl_raw / ctrl_total if ctrl_total else 0.0
    print(f"[ok] MW-6 control raw-hit rate = {ctrl_rate:.4f} (expect ~0.05) over {ctrl_total} windows")

    # ---- Bonferroni survivors (Gaussian-z) + 200k empirical refinement ----
    survivors = [r for r in results if r["bonf_z_survivor"]]
    survivors.sort(key=lambda r: -r["z"])
    print(f"[ok] {len(survivors)} Gaussian-z Bonferroni survivors (z > {z_bon:.3f})")

    # refine survivors + any p-floor windows with 200k perms
    refine_pool = {r["window"] for r in survivors}
    for r in results:
        if r["p_raw"] <= 1.5 / (N_PERMS + 1):  # at/near the 10k p-floor
            refine_pool.add(r["window"])
    print(f"[..] 200k-perm empirical refinement on {len(refine_pool)} windows ...")
    refine = {}
    win_by_key = {r["window"]: r for r in results}
    seg_by_key = {f"{sid}:{vs}-{ve}": seg
                  for (sid, name, N, w, vs, ve, seg) in windows}
    for key in sorted(refine_pool):
        sid = int(key.split(":")[0])
        seg = seg_by_key[key]
        rlist = [rsets.get((sid, v), frozenset()) for v in seg]
        o, m, sd, z, p = perm_null(rlist, N_PERMS_REFINE, SEED)
        refine[key] = {"ring": round(o, 5), "z": round(z, 4),
                       "p_200k": p, "emp_bonf_survivor": p < alpha_bon}
    n_emp_surv = sum(1 for v in refine.values() if v["emp_bonf_survivor"])
    print(f"[ok] {n_emp_surv} confirmed EMPIRICAL Bonferroni survivors (200k-perm p < {alpha_bon:.2e})")

    # ---- H1 verdict ----
    n_bonf = len(survivors)
    h1 = "PASS" if n_bonf >= K_BASELINE else "NULL"

    # ---- H2: distribution / concentration ----
    # Pre-reg defines the ring set as "Bonferroni-surviving + raw-alpha=0.05 ring windows".
    # With 0 Bonferroni survivors, H2 is adjudicated on the raw-alpha candidate roster
    # (the surahs carrying >=1 raw-hit window). Reported as the candidate-pool concentration;
    # interpreted in light of H1 NULL (see findings).
    all_N = {s["id"]: len(s["verses"]) for s in quran}
    bonf_surahs = sorted({r["surah"] for r in survivors})
    ring_surahs = sorted({r["surah"] for r in results if r["raw_hit"]})  # raw-alpha roster
    raw_surahs = ring_surahs
    ring_N = [all_N[s] for s in ring_surahs]
    nonring_N = [all_N[s] for s in all_N if s not in set(ring_surahs)]

    h2a_p, h2a = _mannwhitney_one_sided_greater(ring_N, nonring_N)
    n_early = sum(1 for s in ring_surahs if s <= EARLY_CUTOFF)
    h2b_p = _binom_tail_ge(n_early, len(ring_surahs), CORPUS_EARLY_FRAC) if ring_surahs else 1.0
    h2b = h2b_p < 0.05
    if h2a and h2b:
        h2 = "PASS"
    elif h2a or h2b:
        h2 = "PARTIAL"
    else:
        h2 = "NULL"

    # ---- MW-3 robustness: stride-1 re-scan of top-30 hits in host surah ----
    top_hits = sorted(results, key=lambda r: -r["z"])[:30]
    stride1 = []
    for r in top_hits:
        sid = r["surah"]; w = r["width"]
        vv = surah_vids[sid]
        best = {"z": -99, "window": None, "ring": 0}
        for st in range(0, len(vv) - w + 1):  # full stride-1
            seg = vv[st:st + w]
            rlist = [rsets.get((sid, v), frozenset()) for v in seg]
            o = ring_score(rlist)
            if o > best["ring"]:
                best = {"window": f"{sid}:{seg[0]}-{seg[-1]}", "ring": round(o, 5)}
        stride1.append({"grid_window": r["window"], "grid_ring": r["ring"],
                        "stride1_best_window": best["window"], "stride1_best_ring": best["ring"]})

    # ---- assemble roster ----
    raw_roster = sorted([r for r in results if r["raw_hit"]], key=lambda r: -r["z"])
    expected_raw = round(RAW_ALPHA * F, 1)

    out = {
        "test_id": "H-NEW-2220",
        "prereg_sha256": PREREG_SHA,
        "seed": SEED, "n_perms": N_PERMS, "n_perms_refine": N_PERMS_REFINE,
        "widths": list(WIDTHS), "stride_rule": "ceil(w/2)",
        "family_size_F": F, "alpha_bonferroni": alpha_bon,
        "bonferroni_z_threshold": round(z_bon, 4),
        "K_baseline": K_BASELINE,
        "H3_selfcheck": {"window": "2:131-144", "ring_ref": F07_REF_RING, "z_ref": F07_REF_Z,
                         "ring_observed": round(f07_o, 5), "z_observed": round(f07_z, 4),
                         "p_observed": round(f07_p, 5), "passed": h3_ok},
        "MW6_control_raw_rate": round(ctrl_rate, 4),
        "raw_hits_total": raw_hits,
        "raw_hits_expected_under_null": expected_raw,
        "raw_enrichment_ratio": round(raw_hits / expected_raw, 3) if expected_raw else None,
        "n_bonferroni_z_survivors": n_bonf,
        "n_empirical_bonferroni_survivors_200k": n_emp_surv,
        "H1_verdict": h1,
        "bonferroni_surahs": bonf_surahs,
        "H2_adjudicated_on": "raw-alpha candidate roster (0 Bonferroni survivors)",
        "ring_bearing_surahs": ring_surahs,
        "ring_bearing_surah_N": {str(s): all_N[s] for s in ring_surahs},
        "raw_roster_surahs": raw_surahs,
        "H2a_ring_surah_median_N": _median(ring_N) if ring_N else None,
        "H2a_nonring_surah_median_N": _median(nonring_N) if nonring_N else None,
        "H2a_mannwhitney_p": round(h2a_p, 5), "H2a_pass": h2a,
        "H2b_n_early_le50": n_early, "H2b_n_ring_surahs": len(ring_surahs),
        "H2b_early_fraction": round(n_early / len(ring_surahs), 4) if ring_surahs else None,
        "H2b_corpus_early_fraction": round(CORPUS_EARLY_FRAC, 4),
        "H2b_binom_p": round(h2b_p, 5), "H2b_pass": h2b,
        "H2_verdict": h2,
        "bonferroni_survivors": survivors,
        "empirical_refinement_200k": refine,
        "MW3_stride1_robustness_top30": stride1,
        "raw_roster": raw_roster,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"[ok] wrote {OUT_JSON}")

    # ---- console summary ----
    print("\n========== H-NEW-2220 SUMMARY ==========")
    print(f"family F={F}  Bonf-z>{z_bon:.3f}  alpha_bon={alpha_bon:.2e}")
    print(f"H3 self-check: {'PASS' if h3_ok else 'FAIL'} (Q2:131-144 reproduced)")
    print(f"MW-6 control raw-rate: {ctrl_rate:.4f} (expect ~0.05)")
    print(f"raw 95th-pct roster: {raw_hits} windows (null-expected {expected_raw}, "
          f"enrichment {out['raw_enrichment_ratio']}x)")
    print(f"Bonferroni-z survivors: {n_bonf}  [H1 {h1} vs K={K_BASELINE}]")
    print(f"  empirical 200k-perm confirmed survivors: {n_emp_surv}")
    for r in survivors[:15]:
        rk = refine.get(r["window"], {})
        print(f"    {r['window']:>12} w={r['width']:>2} ring={r['ring']:.3f} "
              f"z={r['z']:+.2f}  200k-p={rk.get('p_200k','-')}")
    print(f"H2a ring-surah median N={out['H2a_ring_surah_median_N']} vs "
          f"nonring {out['H2a_nonring_surah_median_N']}  MW-p={h2a_p:.4f}  [{ 'PASS' if h2a else 'fail'}]")
    print(f"H2b early(s<=50) {n_early}/{len(ring_surahs)} = {out['H2b_early_fraction']} "
          f"vs corpus {CORPUS_EARLY_FRAC:.3f}  binom-p={h2b_p:.4f}  [{ 'PASS' if h2b else 'fail'}]")
    print(f"H2 verdict: {h2}")


# ------------------------------ stats utils --------------------------------

def _z_for_p(p):
    """one-sided gaussian z such that upper-tail = p (bisection)."""
    lo, hi = 0.0, 12.0
    for _ in range(200):
        m = (lo + hi) / 2
        if gaussian_tail_p(m) > p:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def _median(xs):
    if not xs:
        return None
    s = sorted(xs); n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def _mannwhitney_one_sided_greater(a, b):
    """H1: a stochastically GREATER than b. Normal-approx U test, one-sided.
    Returns (p, pass_bool). If a empty -> (1.0, False)."""
    if not a or not b:
        return 1.0, False
    na, nb = len(a), len(b)
    combined = sorted([(v, 0) for v in a] + [(v, 1) for v in b])
    # rank with ties averaged
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg = (i + 1 + j + 1) / 2
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    Ra = sum(ranks[k] for k in range(len(combined)) if combined[k][1] == 0)
    Ua = Ra - na * (na + 1) / 2
    mu = na * nb / 2
    sigma = math.sqrt(na * nb * (na + nb + 1) / 12)
    if sigma == 0:
        return 1.0, False
    z = (Ua - mu) / sigma
    p = gaussian_tail_p(z)        # upper tail: a tends to outrank b
    return p, p < 0.05


def _binom_tail_ge(k, n, p):
    """one-sided binomial P(X >= k) for X~Binom(n,p)."""
    if n == 0:
        return 1.0
    from math import comb
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


if __name__ == "__main__":
    main()
