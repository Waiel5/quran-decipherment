#!/usr/bin/env python3
"""H-NEW-2250 — Particle-cascade structures: verse-initial fa- / thumma- / wa-idhā chains.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2250-particle-cascade.md
SHA256:  723c02aaee549e6ca4d4a0b8de9fcea74e07bebaac3c4949883920b9a188a4ff

A GENERATOR that enumerates every maximal run (>=3 consecutive verses, within one
surah) sharing the same verse-initial particle CLASS, for three families:
  fa-      : verse word-1 segment 1 is a fa prefix  PREFIX|f:*+
  thumma   : verse word-1 segment 1 is the stem vum~a  POS:CONJ LEM:vum~
  idhA     : verse word-1 STEM is the time-adverb <i*aA  POS:T LEM:<i*aA
             (with or without a wa-/fa- proclitic = the eschatological "when..." head)
Also enumerates the strict literal surface form wa-idhA as a sub-report.

Primary direction-locked test (H1): idhA-headed-verse DENSITY is HIGHER in
juz'-30 / short-mufassal (s>=78) than corpus mean. 10000-perm permutation null,
seed 20260509, Bonferroni k=3 (alpha_cell=0.0167). Reversal -> NULL with prominence.

Rules-tuple: (QAC-v0.4 POS, verse-initial = word index 1, Hafs-Kufan, Mashriqi).
All numbers computed from disk.
"""

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-2250-particle-cascade.md"
EXPECTED_SHA = "723c02aaee549e6ca4d4a0b8de9fcea74e07bebaac3c4949883920b9a188a4ff"
QURAN_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
QAC_PATH = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-2250.json"

SEED_A = 20260509
SEED_B = 20260511
N_PERM = 10_000
ALPHA_BON = 0.05 / 3
JUZ30_CUT = 78          # primary short-mufassal cut: s >= 78
QISAR_CUT = 94          # secondary "mufassal qisar" cut: s >= 94
MIN_RUN = 3


# ---------------------------------------------------------------------------
# 0. SHA self-verification (fail-fast)
# ---------------------------------------------------------------------------
def verify_sha():
    got = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if got != EXPECTED_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch.\n expected {EXPECTED_SHA}\n got      {got}")
    print(f"[ok] pre-reg SHA verified: {got}")


# ---------------------------------------------------------------------------
# 1. Load canonical verse list (ordered, surah:verse) from no-tashkeel JSON
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
# 2. Parse QAC: for each (s,v) get word-1 segment tokens -> family head
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]*)\t(.*)$")


def parse_qac_heads():
    """Return dict (s,v) -> dict of family booleans + descriptive head string.
    Only word-index 1 segments are inspected."""
    # collect segments of word 1 per verse
    word1 = defaultdict(dict)   # (s,v) -> {seg_idx: (form, tag, features)}
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
            form, tag, feats = m.group(5), m.group(6), m.group(7)
            word1[(s, v)][seg] = (form, tag, feats)

    heads = {}
    for sv, segs in word1.items():
        seg1 = segs.get(1)
        seg2 = segs.get(2)
        is_fa = bool(seg1 and "PREFIX|f:" in seg1[2])
        is_thumma = bool(seg1 and seg1[2].startswith("STEM|POS:CONJ") and "LEM:vum~" in seg1[2])
        # idhA head = any segment of word-1 is the time-adverb stem <i*aA
        is_idha = any(("POS:T" in t[2] and "LEM:<i*aA" in t[2]) for t in segs.values())
        # strict literal wa-idhA: seg1 is w: prefix AND seg2 stem is <i*aA
        is_wa_idha = bool(
            seg1 and "PREFIX|w:" in seg1[2]
            and seg2 and "POS:T" in seg2[2] and "LEM:<i*aA" in seg2[2]
        )
        # bare idhA (no proclitic on word-1): seg1 itself is the <i*aA stem
        is_bare_idha = bool(seg1 and "POS:T" in seg1[2] and "LEM:<i*aA" in seg1[2])
        heads[sv] = {
            "fa": is_fa,
            "thumma": is_thumma,
            "idha": is_idha,
            "wa_idha": is_wa_idha,
            "bare_idha": is_bare_idha,
        }
    return heads


# ---------------------------------------------------------------------------
# 3. Maximal-run enumeration per family
# ---------------------------------------------------------------------------
def enumerate_runs(verses, heads, family_key, counts):
    """Find maximal runs of >=MIN_RUN consecutive verses (within one surah) whose
    head[family_key] is True. Returns list of dicts."""
    # group verses by surah, preserve verse order
    by_surah = defaultdict(list)
    for (s, v, txt) in verses:
        by_surah[s].append((v, txt))
    runs = []
    for s in sorted(by_surah):
        seq = sorted(by_surah[s])  # (v, txt) by verse id
        i = 0
        n = len(seq)
        while i < n:
            v, _ = seq[i]
            if heads.get((s, v), {}).get(family_key):
                j = i
                # extend while consecutive verse ids AND flag true
                while (j + 1 < n
                       and seq[j + 1][0] == seq[j][0] + 1
                       and heads.get((s, seq[j + 1][0]), {}).get(family_key)):
                    j += 1
                run_len = j - i + 1
                if run_len >= MIN_RUN:
                    runs.append({
                        "surah": s,
                        "v_start": seq[i][0],
                        "v_end": seq[j][0],
                        "length": run_len,
                    })
                i = j + 1
            else:
                i += 1
    runs.sort(key=lambda r: (-r["length"], r["surah"], r["v_start"]))
    return runs


# ---------------------------------------------------------------------------
# 4. Permutation density test (direction-locked for idhA)
# ---------------------------------------------------------------------------
def density_test(verses, heads, family_key, cut, seed, locked_direction=True):
    """Delta = density(s>=cut) - density(s<cut). Permute the head indicator across
    all verse slots (preserving total count). One-sided (locked) if locked_direction."""
    flags = [1 if heads.get((s, v), {}).get(family_key) else 0 for (s, v, _) in verses]
    in_juz = [1 if s >= cut else 0 for (s, v, _) in verses]
    N = len(flags)
    n_juz = sum(in_juz)
    n_rest = N - n_juz
    total_heads = sum(flags)

    def delta_from(fl):
        h_juz = sum(f for f, j in zip(fl, in_juz) if j)
        h_rest = sum(f for f, j in zip(fl, in_juz) if not j)
        d_juz = h_juz / n_juz if n_juz else 0.0
        d_rest = h_rest / n_rest if n_rest else 0.0
        return d_juz - d_rest, d_juz, d_rest, h_juz, h_rest

    obs_delta, d_juz, d_rest, h_juz, h_rest = delta_from(flags)

    # permutation: shuffle which slots are heads (preserve total_heads)
    import random
    rng = random.Random(seed)
    idx = list(range(N))
    ge = 0          # one-sided locked: permuted Delta >= observed
    abs_ge = 0      # two-sided: |permuted Delta| >= |observed|
    for _ in range(N_PERM):
        rng.shuffle(idx)
        # first total_heads indices are "heads"
        head_set = set(idx[:total_heads])
        pf = [1 if k in head_set else 0 for k in range(N)]
        pd, *_ = delta_from(pf)
        if pd >= obs_delta:
            ge += 1
        if abs(pd) >= abs(obs_delta):
            abs_ge += 1
    p_one = (ge + 1) / (N_PERM + 1)
    p_two = (abs_ge + 1) / (N_PERM + 1)
    return {
        "family": family_key,
        "cut": cut,
        "obs_delta": obs_delta,
        "density_juz30": d_juz,
        "density_rest": d_rest,
        "heads_in_juz30": h_juz,
        "heads_in_rest": h_rest,
        "total_heads": total_heads,
        "n_juz30": n_juz,
        "n_rest": n_rest,
        "p_one_sided": p_one,
        "p_two_sided": p_two,
        "seed": seed,
        "n_perm": N_PERM,
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    verify_sha()
    verses, counts = load_verses()
    heads = parse_qac_heads()

    # coverage check: how many verses have a QAC word-1 record
    covered = sum(1 for (s, v, _) in verses if (s, v) in heads)
    print(f"[info] verses={len(verses)}  with-QAC-word1={covered}")

    fam_keys = ["fa", "thumma", "idha", "wa_idha"]
    head_counts = {k: sum(1 for (s, v, _) in verses if heads.get((s, v), {}).get(k))
                   for k in fam_keys + ["bare_idha"]}

    runs = {k: enumerate_runs(verses, heads, k, counts) for k in fam_keys}

    # Density tests
    # Primary (locked, one-sided): idhA, cut=78
    idha_primary = density_test(verses, heads, "idha", JUZ30_CUT, SEED_A, True)
    idha_primary_rep = density_test(verses, heads, "idha", JUZ30_CUT, SEED_B, True)
    # Secondary cut (s>=94)
    idha_qisar = density_test(verses, heads, "idha", QISAR_CUT, SEED_A, True)
    # Controls (fa, thumma) at cut=78 — exploratory two-sided
    fa_dens = density_test(verses, heads, "fa", JUZ30_CUT, SEED_A, False)
    thumma_dens = density_test(verses, heads, "thumma", JUZ30_CUT, SEED_A, False)

    # Verdict
    confirmed = (idha_primary["obs_delta"] > 0 and idha_primary["p_one_sided"] < ALPHA_BON)
    reversed_ = (idha_primary["obs_delta"] <= 0)
    if confirmed:
        verdict = "CONFIRMED-DIRECTED"
    elif idha_primary["obs_delta"] > 0 and idha_primary["p_one_sided"] < 0.05:
        verdict = "DIRECTIONAL"
    elif reversed_:
        verdict = "NULL-PRE-COMMIT-REVERSAL"
    else:
        verdict = "NULL"

    out = {
        "id": "H-NEW-2250",
        "prereg_sha256": EXPECTED_SHA,
        "seed_primary": SEED_A,
        "seed_replication": SEED_B,
        "n_perm": N_PERM,
        "alpha_bonferroni": ALPHA_BON,
        "bonferroni_k": 3,
        "rules_tuple": "QAC-v0.4 POS, verse-initial=word-1, Hafs-Kufan, Mashriqi",
        "verse_total": len(verses),
        "verses_with_qac_word1": covered,
        "head_counts": head_counts,
        "runs": runs,
        "run_summary": {k: {
            "n_runs": len(runs[k]),
            "max_len": (runs[k][0]["length"] if runs[k] else 0),
            "len_hist": dict(sorted(Counter(r["length"] for r in runs[k]).items())),
        } for k in fam_keys},
        "density_idha_primary_cut78_seedA": idha_primary,
        "density_idha_primary_cut78_seedB": idha_primary_rep,
        "density_idha_secondary_cut94_seedA": idha_qisar,
        "density_fa_cut78_control": fa_dens,
        "density_thumma_cut78_control": thumma_dens,
        "verdict": verdict,
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    # console summary
    print(f"\n=== HEAD COUNTS (verses) ===")
    for k, c in head_counts.items():
        print(f"  {k:10s}: {c}")
    print(f"\n=== MAXIMAL RUNS (>= {MIN_RUN}) ===")
    for k in fam_keys:
        rs = runs[k]
        print(f"  {k:8s}: {len(rs)} runs, max len = {rs[0]['length'] if rs else 0}")
        for r in rs[:6]:
            print(f"      Q{r['surah']}:{r['v_start']}-{r['v_end']}  len={r['length']}")
    print(f"\n=== H1 idhA density (cut s>=78, LOCKED one-sided) ===")
    print(f"  density juz30={idha_primary['density_juz30']:.4f}  rest={idha_primary['density_rest']:.4f}")
    print(f"  Delta={idha_primary['obs_delta']:+.4f}  p_one={idha_primary['p_one_sided']:.5f}"
          f"  (rep seedB p_one={idha_primary_rep['p_one_sided']:.5f})")
    print(f"  alpha_Bonferroni(k=3)={ALPHA_BON:.4f}")
    print(f"  secondary cut s>=94: Delta={idha_qisar['obs_delta']:+.4f} p_one={idha_qisar['p_one_sided']:.5f}")
    print(f"\n=== controls (cut s>=78, two-sided) ===")
    print(f"  fa-    : Delta={fa_dens['obs_delta']:+.4f} p_two={fa_dens['p_two_sided']:.5f}")
    print(f"  thumma : Delta={thumma_dens['obs_delta']:+.4f} p_two={thumma_dens['p_two_sided']:.5f}")
    print(f"\n=== VERDICT: {verdict} ===")
    print(f"[ok] wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
