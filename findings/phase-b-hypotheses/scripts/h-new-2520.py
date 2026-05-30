#!/usr/bin/env python3
"""H-NEW-2520 — Pericope-onset / narrative-onset formula census.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2520-pericope-onset.md
SHA256:  3cb30e7cc34d567deaf20d8f9c694f9284d7558f799198edadeb844dcc148517

A GENERATOR enumerating, corpus-wide and with coordinates, every occurrence of the
classical narrative-onset markers that open story-pericopes (qasas episodes):

  idh    : wa-idh / idh  (waA-<i*o / <i*o, "and recall when...") — the qasas-onset.
           QAC: word-1 has a segment POS:T with LEM exactly <i*  (NOT <i*aA = idhA
           conditional, NOT <i*FA = idhan, NOT <i*on = idhn).  This is the
           QAC-disambiguated narrative-recall idh.
  lamma  : wa-lamma / lamma  (POS:T LEM:lam~aA) — narrative event-onset "and when".
  qalu   : wa-qalu / qalu  (POS:V ROOT:qwl LEM:qaAla PERF 3MP) — dialogue-onset
           "they said".

Primary direction-locked test (H1): idh recall-onset DENSITY is HIGHER in the LONG
narrative/legal surahs (s<=50) than in s>50 — the INVERSE of H-NEW-2250's idhA
juz'-30 (s>=78) concentration.  H1b (lamma) and H1c (qalu) lock the same direction.
10000-perm permutation null, seed 20260509, Bonferroni k=3 (alpha_cell=0.0167).
Reversal (Delta<=0) -> NULL with full prominence.

Rules-tuple: (QAC-v0.4 POS+LEM, verse-initial=word-1, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi).  All numbers computed from disk.
"""

import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-2520-pericope-onset.md"
EXPECTED_SHA = "3cb30e7cc34d567deaf20d8f9c694f9284d7558f799198edadeb844dcc148517"
QURAN_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
QAC_PATH = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-2520.json"

SEED_A = 20260509
SEED_B = 20260511
N_PERM = 10_000
BONF_K = 3
ALPHA_BON = 0.05 / BONF_K
TIWAL_CUT = 50          # primary: long surahs s<=50  vs  s>50
JUZ30_CUT = 78          # secondary lens: contrast with H-NEW-2250 idhA cut
MIN_RUN = 3

FAMILIES = ["idh", "lamma", "qalu"]


# ---------------------------------------------------------------------------
# 0. SHA self-verification (fail-fast)
# ---------------------------------------------------------------------------
def verify_sha():
    got = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if got != EXPECTED_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch.\n expected {EXPECTED_SHA}\n got      {got}")
    print(f"[ok] pre-reg SHA verified: {got}")


# ---------------------------------------------------------------------------
# 1. Load canonical verse list (ordered) from no-tashkeel JSON
# ---------------------------------------------------------------------------
def load_verses():
    data = json.load(open(QURAN_PATH, encoding="utf-8"))
    verses = []            # ordered list of (s, v, text)
    counts = {}            # s -> total_verses
    for surah in data:
        s = surah["id"]
        counts[s] = surah["total_verses"]
        for ver in surah["verses"]:
            verses.append((s, ver["id"], ver["text"]))
    assert len(verses) == 6236, f"verse count {len(verses)} != 6236"
    return verses, counts


# ---------------------------------------------------------------------------
# 2. Parse QAC word-1 segments per verse -> family heads
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]*)\t(.*)$")


def lem_exact(feats, lem):
    """LEM:<lem> followed by | or end-of-features (exact lemma match)."""
    return re.search(r"LEM:" + re.escape(lem) + r"(\||$)", feats) is not None


def parse_qac_heads():
    """Return dict (s,v) -> {family: bool, proclitic: 'wa'/'fa'/'bare'/None}."""
    word1 = defaultdict(dict)   # (s,v) -> {seg_idx: (form, tag, feats)}
    with open(QAC_PATH, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            m = LOC_RE.match(line.rstrip("\n"))
            if not m:
                continue
            s, v, w, seg = (int(m.group(i)) for i in range(1, 5))
            if w != 1:
                continue
            word1[(s, v)][seg] = (m.group(5), m.group(6), m.group(7))

    heads = {}
    for sv, segs in word1.items():
        seg1 = segs.get(1)
        # proclitic on word-1
        if seg1 and "PREFIX|w:" in seg1[2]:
            proc = "wa"
        elif seg1 and "PREFIX|f:" in seg1[2]:
            proc = "fa"
        else:
            proc = None

        # idh (narrative-recall): any seg POS:T with LEM exactly <i*
        is_idh = any(("POS:T" in t[2] and lem_exact(t[2], "<i*")) for t in segs.values())
        # lamma: any seg POS:T LEM lam~aA
        is_lamma = any(("POS:T" in t[2] and lem_exact(t[2], "lam~aA")) for t in segs.values())
        # qalu: any seg POS:V ROOT:qwl LEM:qaAla PERF 3MP
        is_qalu = any(("POS:V" in t[2] and "ROOT:qwl" in t[2] and "LEM:qaAla" in t[2]
                       and "PERF" in t[2] and "3MP" in t[2]) for t in segs.values())

        # proclitic relative to the matched stem: 'bare' iff seg1 IS the matched stem
        def stem_proc(is_fam, stem_test):
            if not is_fam:
                return None
            if seg1 and stem_test(seg1[2]):
                return "bare"
            return proc if proc else "other"

        heads[sv] = {
            "idh": is_idh,
            "lamma": is_lamma,
            "qalu": is_qalu,
            "idh_proc": stem_proc(is_idh, lambda f: "POS:T" in f and lem_exact(f, "<i*")),
            "lamma_proc": stem_proc(is_lamma, lambda f: "POS:T" in f and lem_exact(f, "lam~aA")),
            "qalu_proc": stem_proc(
                is_qalu,
                lambda f: "POS:V" in f and "ROOT:qwl" in f and "LEM:qaAla" in f
                and "PERF" in f and "3MP" in f),
        }
    return heads


# ---------------------------------------------------------------------------
# 3. Maximal-run enumeration per family
# ---------------------------------------------------------------------------
def enumerate_runs(verses, heads, family):
    by_surah = defaultdict(list)
    for (s, v, _) in verses:
        by_surah[s].append(v)
    runs = []
    for s in sorted(by_surah):
        seq = sorted(by_surah[s])
        i, n = 0, len(seq)
        while i < n:
            v = seq[i]
            if heads.get((s, v), {}).get(family):
                j = i
                while (j + 1 < n and seq[j + 1] == seq[j] + 1
                       and heads.get((s, seq[j + 1]), {}).get(family)):
                    j += 1
                if j - i + 1 >= MIN_RUN:
                    runs.append({"surah": s, "v_start": seq[i], "v_end": seq[j],
                                 "length": j - i + 1})
                i = j + 1
            else:
                i += 1
    runs.sort(key=lambda r: (-r["length"], r["surah"], r["v_start"]))
    return runs


# ---------------------------------------------------------------------------
# 4. Direction-locked density permutation test
# ---------------------------------------------------------------------------
def density_test(verses, heads, family, cut_le, seed):
    """Delta = density(s<=cut_le) - density(s>cut_le). One-sided locked (Delta>0).
    Permute the head indicator across all verse slots preserving total count."""
    flags = [1 if heads.get((s, v), {}).get(family) else 0 for (s, v, _) in verses]
    in_head_band = [1 if s <= cut_le else 0 for (s, v, _) in verses]
    N = len(flags)
    n_head = sum(in_head_band)
    n_tail = N - n_head
    total = sum(flags)

    def delta_from(fl):
        h_head = sum(f for f, b in zip(fl, in_head_band) if b)
        h_tail = sum(f for f, b in zip(fl, in_head_band) if not b)
        d_head = h_head / n_head if n_head else 0.0
        d_tail = h_tail / n_tail if n_tail else 0.0
        return d_head - d_tail, d_head, d_tail, h_head, h_tail

    obs_delta, d_head, d_tail, h_head, h_tail = delta_from(flags)

    rng = random.Random(seed)
    idx = list(range(N))
    ge = 0
    abs_ge = 0
    for _ in range(N_PERM):
        rng.shuffle(idx)
        head_set = set(idx[:total])
        pf = [1 if k in head_set else 0 for k in range(N)]
        pd, *_ = delta_from(pf)
        if pd >= obs_delta:
            ge += 1
        if abs(pd) >= abs(obs_delta):
            abs_ge += 1
    return {
        "family": family,
        "cut_le": cut_le,
        "obs_delta": obs_delta,
        "density_head_band": d_head,
        "density_tail_band": d_tail,
        "heads_in_head_band": h_head,
        "heads_in_tail_band": h_tail,
        "total_heads": total,
        "n_head_band": n_head,
        "n_tail_band": n_tail,
        "p_one_sided": (ge + 1) / (N_PERM + 1),
        "p_two_sided": (abs_ge + 1) / (N_PERM + 1),
        "seed": seed,
        "n_perm": N_PERM,
    }


def classify(test):
    d = test["obs_delta"]
    p = test["p_one_sided"]
    if d <= 0:
        return "NULL-PRE-COMMIT-REVERSAL"
    if p < ALPHA_BON:
        return "CONFIRMED-DIRECTED"
    if p < 0.05:
        return "DIRECTIONAL"
    return "NULL"


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    verify_sha()
    verses, counts = load_verses()
    heads = parse_qac_heads()

    covered = sum(1 for (s, v, _) in verses if (s, v) in heads)
    print(f"[info] verses={len(verses)}  with-QAC-word1={covered}")

    # head counts + proclitic sub-census
    head_counts = {}
    proc_census = {}
    for fam in FAMILIES:
        head_counts[fam] = sum(1 for (s, v, _) in verses if heads.get((s, v), {}).get(fam))
        pc = Counter()
        for (s, v, _) in verses:
            h = heads.get((s, v), {})
            if h.get(fam):
                pc[h.get(fam + "_proc")] += 1
        proc_census[fam] = dict(pc)

    # per-surah distribution
    per_surah = {fam: defaultdict(int) for fam in FAMILIES}
    for (s, v, _) in verses:
        h = heads.get((s, v), {})
        for fam in FAMILIES:
            if h.get(fam):
                per_surah[fam][s] += 1
    per_surah_out = {fam: dict(sorted(per_surah[fam].items())) for fam in FAMILIES}

    # narrative-onset density per surah (all 3 families combined) -> ranking
    onset_density = {}
    for s in counts:
        n_onset = per_surah["idh"].get(s, 0) + per_surah["lamma"].get(s, 0) + per_surah["qalu"].get(s, 0)
        onset_density[s] = {
            "idh": per_surah["idh"].get(s, 0),
            "lamma": per_surah["lamma"].get(s, 0),
            "qalu": per_surah["qalu"].get(s, 0),
            "total_onset": n_onset,
            "verses": counts[s],
            "density": n_onset / counts[s] if counts[s] else 0.0,
        }
    # rank surahs by total onset count and by density
    top_by_count = sorted(onset_density.items(), key=lambda kv: -kv[1]["total_onset"])[:20]
    top_by_density = sorted(
        [(s, d) for s, d in onset_density.items() if d["verses"] >= 10],
        key=lambda kv: -kv[1]["density"])[:20]

    # maximal runs
    runs = {fam: enumerate_runs(verses, heads, fam) for fam in FAMILIES}

    # density tests (primary cut s<=50), seed A + replication seed B
    tests = {}
    for fam in FAMILIES:
        tA = density_test(verses, heads, fam, TIWAL_CUT, SEED_A)
        tB = density_test(verses, heads, fam, TIWAL_CUT, SEED_B)
        tests[fam] = {"seedA": tA, "seedB": tB, "verdict": classify(tA)}
    # secondary lens: idh density at juz-30 cut (s<=78 vs s>78) for direct H-NEW-2250 contrast
    idh_juz30 = density_test(verses, heads, "idh", JUZ30_CUT, SEED_A)

    overall = tests["idh"]["verdict"]

    out = {
        "id": "H-NEW-2520",
        "prereg_sha256": EXPECTED_SHA,
        "seed_primary": SEED_A,
        "seed_replication": SEED_B,
        "n_perm": N_PERM,
        "bonferroni_k": BONF_K,
        "alpha_bonferroni": ALPHA_BON,
        "primary_cut_le": TIWAL_CUT,
        "rules_tuple": "QAC-v0.4 POS+LEM, verse-initial=word-1, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi",
        "verse_total": len(verses),
        "verses_with_qac_word1": covered,
        "head_counts": head_counts,
        "proclitic_census": proc_census,
        "per_surah": per_surah_out,
        "onset_density_top_by_count": [{"surah": s, **d} for s, d in top_by_count],
        "onset_density_top_by_density": [{"surah": s, **d} for s, d in top_by_density],
        "runs": runs,
        "run_summary": {fam: {
            "n_runs": len(runs[fam]),
            "max_len": (runs[fam][0]["length"] if runs[fam] else 0),
            "len_hist": dict(sorted(Counter(r["length"] for r in runs[fam]).items())),
        } for fam in FAMILIES},
        "density_tests": tests,
        "idh_secondary_juz30_cut": idh_juz30,
        "overall_verdict_primary_idh": overall,
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    # console
    print("\n=== HEAD COUNTS (verse-initial onset markers) ===")
    for fam in FAMILIES:
        print(f"  {fam:6s}: {head_counts[fam]:4d}  proclitic={proc_census[fam]}")
    print("\n=== MAXIMAL RUNS (>=3) ===")
    for fam in FAMILIES:
        rs = runs[fam]
        print(f"  {fam:6s}: {len(rs)} runs, max len = {rs[0]['length'] if rs else 0}")
        for r in rs[:5]:
            print(f"      Q{r['surah']}:{r['v_start']}-{r['v_end']}  len={r['length']}")
    print("\n=== TOP NARRATIVE-ONSET-DENSE SURAHS (by count) ===")
    for s, d in top_by_count[:12]:
        print(f"  Q{s:<3d}: total={d['total_onset']:3d} (idh={d['idh']} lammā={d['lamma']} qālū={d['qalu']}) /{d['verses']}v  dens={d['density']:.3f}")
    print("\n=== H1/H1b/H1c density tests (primary cut s<=50, LOCKED one-sided) ===")
    for fam in FAMILIES:
        t = tests[fam]["seedA"]
        tb = tests[fam]["seedB"]
        print(f"  {fam:6s}: dens(s<=50)={t['density_head_band']:.4f} dens(s>50)={t['density_tail_band']:.4f}"
              f"  Δ={t['obs_delta']:+.4f} p={t['p_one_sided']:.5f} (repl {tb['p_one_sided']:.5f}) -> {tests[fam]['verdict']}")
    print(f"  alpha_Bonferroni(k=3)={ALPHA_BON:.4f}")
    print(f"\n=== idh secondary lens (juz-30 contrast cut s<=78 vs s>78) ===")
    print(f"  dens(s<=78)={idh_juz30['density_head_band']:.4f} dens(s>78)={idh_juz30['density_tail_band']:.4f}"
          f"  Δ={idh_juz30['obs_delta']:+.4f} p_two={idh_juz30['p_two_sided']:.5f}")
    print(f"\n=== OVERALL (primary idh): {overall} ===")
    print(f"[ok] wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
