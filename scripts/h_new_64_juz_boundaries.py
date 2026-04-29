"""H-NEW-64: Do canonical juz' (30-part) boundaries correspond to natural structural breaks?

Pre-reg: findings/phase-b-hypotheses/h-new-64-juz-boundaries-prereg.md
Rules tuple: (no-tashkeel; canonical 1..114 mushaf order; whitespace tokenization;
              verse-id = 1-indexed within surah; basmala-counted-only-in-surah-1)

Four axes:
  A - Topic shift (lexical Jaccard divergence)
  B - Rhyme-class shift (TV distance on last-2-char buckets)
  C - Narrative-pivot (proper-noun occurrence asymmetry)
  D - Length discontinuity (mean verse token-count asymmetry)

Null: 1000 random sets of 29 within-corpus boundaries, excluding surah seams.
Bonferroni 5 tests (4 axes + 1 joint), alpha_bon = 0.01.
MW-5 positive control: sample 29 surah-boundary positions.
Seed 20260416.
"""

from __future__ import annotations

import json
import os
import random
import re
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, "/Users/grey/Downloads/quran")
from analysis.tools.loader import load_quran

SEED = 20260416
N_PERM = 1000
W = 10
ALPHA_BON = 0.01
N_JUZ_INTERNAL = 29
N_TOTAL_VERSES = 6236

OUT_JSON = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-64.json"

# ---------------------------------------------------------------------------
# LOCKED: 30-juz' starts (from pre-reg). Converted to global verse positions.
# ---------------------------------------------------------------------------

JUZ_STARTS = [
    (1, 1, 1),
    (2, 2, 142),
    (3, 2, 253),
    (4, 3, 93),
    (5, 4, 24),
    (6, 4, 148),
    (7, 5, 82),
    (8, 6, 111),
    (9, 7, 88),
    (10, 8, 41),
    (11, 9, 93),
    (12, 11, 6),
    (13, 12, 53),
    (14, 15, 1),
    (15, 17, 1),
    (16, 18, 75),
    (17, 21, 1),
    (18, 23, 1),
    (19, 25, 21),
    (20, 27, 56),
    (21, 29, 46),
    (22, 33, 31),
    (23, 36, 28),
    (24, 39, 32),
    (25, 41, 47),
    (26, 46, 1),
    (27, 51, 31),
    (28, 58, 1),
    (29, 67, 1),
    (30, 78, 1),
]

# Surah-aligned juz' starts (from pre-reg): juz' 14, 15, 17, 18, 26, 29, 30.
# (Note: juz' 1 is also at surah 1 v1 but is not an INTERNAL boundary.)
JUZ_SURAH_ALIGNED = {14, 15, 17, 18, 26, 29, 30}

# Proper-noun list (LOCKED in pre-reg), normalized-skeleton form (no-tashkeel).
PROPER_NOUNS = [
    # Prophets
    "محمد", "آدم", "نوح", "ابراهيم", "اسماعيل", "اسحاق", "يعقوب", "يوسف",
    "موسى", "هارون", "داود", "سليمان", "عيسى", "يحيى", "زكريا", "ايوب",
    "يونس", "شعيب", "صالح", "هود", "لوط", "ادريس", "ذو الكفل", "الياس",
    # People/groups
    "بنو اسرائيل", "فرعون", "عاد", "ثمود", "قريش", "القارون", "السامري",
    "ياجوج", "ماجوج",
    # Places
    "مكة", "بكة", "يثرب", "المدينة", "طور", "سيناء", "مصر", "بابل",
    "الكعبة", "البيت العتيق",
]

# Arabic letter range (for rhyme bucket extraction)
ARABIC_LETTERS_RE = re.compile(r"[\u0621-\u064A\u0671-\u06D3]")


# ---------------------------------------------------------------------------
# Corpus construction
# ---------------------------------------------------------------------------


def build_corpus() -> Tuple[List[str], List[int], List[int], List[int]]:
    """Return (verses_text, verse_surah, verse_id_in_surah, surah_start_positions).

    Global positions are 1-indexed (1..6236). Surah-start positions are
    1-indexed global positions where each surah begins.
    """
    surahs = load_quran("no-tashkeel")
    verses_text: List[str] = []
    verse_surah: List[int] = []
    verse_id: List[int] = []
    surah_start_positions: List[int] = []
    g = 0
    for s in surahs:
        surah_start_positions.append(g + 1)
        for v in s.verses:
            g += 1
            verses_text.append(v.text)
            verse_surah.append(s.id)
            verse_id.append(v.id)
    assert g == N_TOTAL_VERSES, f"expected {N_TOTAL_VERSES}, got {g}"
    return verses_text, verse_surah, verse_id, surah_start_positions


def juz_positions(verse_surah: List[int], verse_id: List[int]) -> List[int]:
    """Return 30 global 1-indexed start positions (one per juz')."""
    pos_of = {}
    for i, (sid, vid) in enumerate(zip(verse_surah, verse_id), start=1):
        pos_of[(sid, vid)] = i
    positions = []
    for (_juz, sid, vid) in JUZ_STARTS:
        key = (sid, vid)
        if key not in pos_of:
            raise RuntimeError(f"juz start {key} not found in corpus")
        positions.append(pos_of[key])
    return positions


# ---------------------------------------------------------------------------
# Per-verse precomputation
# ---------------------------------------------------------------------------


def tokenize(text: str) -> List[str]:
    return text.split()


def last_token(text: str) -> str:
    toks = tokenize(text)
    if not toks:
        return ""
    # strip any sajda / pause markers from last token
    last = toks[-1]
    # remove any non-Arabic-letter chars
    letters = ARABIC_LETTERS_RE.findall(last)
    return "".join(letters)


def rhyme_bucket(last_tok: str) -> str:
    if len(last_tok) >= 2:
        return last_tok[-2:]
    return last_tok


def count_proper_nouns(text: str) -> int:
    # substring matches on the raw (no-tashkeel) text
    n = 0
    for pn in PROPER_NOUNS:
        # count non-overlapping occurrences
        start = 0
        while True:
            i = text.find(pn, start)
            if i < 0:
                break
            n += 1
            start = i + len(pn)
    return n


def precompute(verses_text: List[str]):
    tokens_per_verse = [tokenize(t) for t in verses_text]
    lengths = [len(toks) for toks in tokens_per_verse]
    rhymes = [rhyme_bucket(last_token(t)) for t in verses_text]
    pn_counts = [count_proper_nouns(t) for t in verses_text]
    return tokens_per_verse, lengths, rhymes, pn_counts


# ---------------------------------------------------------------------------
# Per-boundary axis statistics
# ---------------------------------------------------------------------------


def window_slices(p: int, n: int, w: int) -> Tuple[int, int, int, int]:
    """1-indexed p = 'cut between verse p-1 and verse p'.

    Return (b_lo, b_hi, a_lo, a_hi) as 0-indexed half-open intervals into
    the verse arrays. b = before window, a = after window. Truncate at
    corpus edges.
    """
    b_lo = max(0, (p - 1) - w)
    b_hi = p - 1
    a_lo = p - 1
    a_hi = min(n, (p - 1) + w)
    return b_lo, b_hi, a_lo, a_hi


def axis_A(p, tokens_per_verse, n, w):
    b_lo, b_hi, a_lo, a_hi = window_slices(p, n, w)
    T_before = set()
    for toks in tokens_per_verse[b_lo:b_hi]:
        T_before.update(toks)
    T_after = set()
    for toks in tokens_per_verse[a_lo:a_hi]:
        T_after.update(toks)
    union = T_before | T_after
    inter = T_before & T_after
    if not union:
        return 0.0
    return 1.0 - (len(inter) / len(union))


def axis_B(p, rhymes, n, w):
    b_lo, b_hi, a_lo, a_hi = window_slices(p, n, w)
    def freq(items):
        d: Dict[str, float] = {}
        if not items:
            return d
        step = 1.0 / len(items)
        for x in items:
            d[x] = d.get(x, 0.0) + step
        return d
    f_b = freq(rhymes[b_lo:b_hi])
    f_a = freq(rhymes[a_lo:a_hi])
    keys = set(f_b) | set(f_a)
    if not keys:
        return 0.0
    return 0.5 * sum(abs(f_b.get(k, 0.0) - f_a.get(k, 0.0)) for k in keys)


def axis_C(p, pn_counts, n, w):
    b_lo, b_hi, a_lo, a_hi = window_slices(p, n, w)
    n_b = sum(pn_counts[b_lo:b_hi])
    n_a = sum(pn_counts[a_lo:a_hi])
    return abs(n_b - n_a) / (n_b + n_a + 1)


def axis_D(p, lengths, n, w):
    b_lo, b_hi, a_lo, a_hi = window_slices(p, n, w)
    before = lengths[b_lo:b_hi]
    after = lengths[a_lo:a_hi]
    if not before or not after:
        return 0.0
    mu_b = sum(before) / len(before)
    mu_a = sum(after) / len(after)
    denom = max(mu_b, mu_a) + 1
    return abs(mu_b - mu_a) / denom


def compute_all_axes(positions, tokens_per_verse, lengths, rhymes, pn_counts, n, w):
    A, B, C, D = [], [], [], []
    for p in positions:
        A.append(axis_A(p, tokens_per_verse, n, w))
        B.append(axis_B(p, rhymes, n, w))
        C.append(axis_C(p, pn_counts, n, w))
        D.append(axis_D(p, lengths, n, w))
    return A, B, C, D


# ---------------------------------------------------------------------------
# Null model
# ---------------------------------------------------------------------------


def build_valid_positions(surah_start_positions: List[int], n: int) -> List[int]:
    surah_starts = set(surah_start_positions)
    valid = [p for p in range(2, n + 1) if p not in surah_starts]
    return valid


def mean_sd(xs: List[float]) -> Tuple[float, float]:
    if not xs:
        return 0.0, 0.0
    m = sum(xs) / len(xs)
    v = sum((x - m) ** 2 for x in xs) / len(xs)
    sd = v ** 0.5
    return m, sd


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    random.seed(SEED)

    verses_text, verse_surah, verse_id, surah_start_positions = build_corpus()
    n = len(verses_text)
    tokens_per_verse, lengths, rhymes, pn_counts = precompute(verses_text)

    # Observed juz' positions (30 positions; internal = positions[1:30])
    juz_pos = juz_positions(verse_surah, verse_id)
    juz_internal = juz_pos[1:]  # 29 positions starting at juz' 2..30
    assert len(juz_internal) == N_JUZ_INTERNAL

    obs_A, obs_B, obs_C, obs_D = compute_all_axes(
        juz_internal, tokens_per_verse, lengths, rhymes, pn_counts, n, W
    )

    SUM_A_obs = sum(obs_A)
    SUM_B_obs = sum(obs_B)
    SUM_C_obs = sum(obs_C)
    SUM_D_obs = sum(obs_D)

    # Null distribution
    valid_positions = build_valid_positions(surah_start_positions, n)
    null_SUM_A = []
    null_SUM_B = []
    null_SUM_C = []
    null_SUM_D = []

    for _ in range(N_PERM):
        sample = random.sample(valid_positions, N_JUZ_INTERNAL)
        A, B, C, D = compute_all_axes(
            sample, tokens_per_verse, lengths, rhymes, pn_counts, n, W
        )
        null_SUM_A.append(sum(A))
        null_SUM_B.append(sum(B))
        null_SUM_C.append(sum(C))
        null_SUM_D.append(sum(D))

    # Z-normalize observed per-axis and compute joint
    def z_norm(obs_val, null_vals):
        m, sd = mean_sd(null_vals)
        if sd == 0:
            return 0.0, m, sd
        return (obs_val - m) / sd, m, sd

    zA, mA, sA = z_norm(SUM_A_obs, null_SUM_A)
    zB, mB, sB = z_norm(SUM_B_obs, null_SUM_B)
    zC, mC, sC = z_norm(SUM_C_obs, null_SUM_C)
    zD, mD, sD = z_norm(SUM_D_obs, null_SUM_D)

    # Null joint
    null_JOINT = []
    for a, b, c, d in zip(null_SUM_A, null_SUM_B, null_SUM_C, null_SUM_D):
        za = (a - mA) / sA if sA > 0 else 0.0
        zb = (b - mB) / sB if sB > 0 else 0.0
        zc = (c - mC) / sC if sC > 0 else 0.0
        zd = (d - mD) / sD if sD > 0 else 0.0
        null_JOINT.append(za + zb + zc + zd)
    obs_JOINT = zA + zB + zC + zD

    # One-sided p-values (right tail)
    def p_right(obs_val, null_vals):
        return (1 + sum(1 for x in null_vals if x >= obs_val)) / (len(null_vals) + 1)

    pA = p_right(SUM_A_obs, null_SUM_A)
    pB = p_right(SUM_B_obs, null_SUM_B)
    pC = p_right(SUM_C_obs, null_SUM_C)
    pD = p_right(SUM_D_obs, null_SUM_D)
    pJ = p_right(obs_JOINT, null_JOINT)

    passA = pA < ALPHA_BON
    passB = pB < ALPHA_BON
    passC = pC < ALPHA_BON
    passD = pD < ALPHA_BON
    passJ = pJ < ALPHA_BON

    n_axis_pass = sum([passA, passB, passC, passD])
    if n_axis_pass >= 2 and passJ:
        verdict = "STRONG-PASS"
    elif n_axis_pass == 1 or passJ:
        verdict = "WEAK-PASS"
    else:
        verdict = "NULL"

    # ------------------------------------------------------------------
    # Per-boundary S_joint ranking
    # ------------------------------------------------------------------
    # Use null-mean / null-sd of per-boundary distributions (averaged).
    # For per-position ranking use axis means/sd from the whole null sample:
    # we need per-POSITION null distributions? Pre-reg spec says z_X(p) against
    # null_mean_X, null_sd_X — where the null distribution is over SUM_X. But
    # for RANKING per-boundary naturalness we need a per-boundary z-score.
    # Reasonable reading: use mean/sd of raw D_X(p) across ALL random boundary
    # samples as the null for a single boundary. Compute from the flat list.

    # Collect raw per-boundary stats from null
    flat_A = []
    flat_B = []
    flat_C = []
    flat_D = []
    # Re-seed and re-sample deterministically for this (must be reproducible)
    random.seed(SEED)
    for _ in range(N_PERM):
        sample = random.sample(valid_positions, N_JUZ_INTERNAL)
        A, B, C, D = compute_all_axes(
            sample, tokens_per_verse, lengths, rhymes, pn_counts, n, W
        )
        flat_A.extend(A)
        flat_B.extend(B)
        flat_C.extend(C)
        flat_D.extend(D)
    mfA, sfA = mean_sd(flat_A)
    mfB, sfB = mean_sd(flat_B)
    mfC, sfC = mean_sd(flat_C)
    mfD, sfD = mean_sd(flat_D)

    per_boundary = []
    for i, p in enumerate(juz_internal):
        juz_k = i + 2  # boundary starts juz' (i+2)
        zAp = (obs_A[i] - mfA) / sfA if sfA > 0 else 0.0
        zBp = (obs_B[i] - mfB) / sfB if sfB > 0 else 0.0
        zCp = (obs_C[i] - mfC) / sfC if sfC > 0 else 0.0
        zDp = (obs_D[i] - mfD) / sfD if sfD > 0 else 0.0
        s_joint_p = zAp + zBp + zCp + zDp
        surah_aligned = juz_k in JUZ_SURAH_ALIGNED
        per_boundary.append({
            "juz_start": juz_k,
            "global_pos": p,
            "surah": JUZ_STARTS[juz_k - 1][1],
            "verse_id": JUZ_STARTS[juz_k - 1][2],
            "surah_aligned": surah_aligned,
            "D_A": obs_A[i],
            "D_B": obs_B[i],
            "D_C": obs_C[i],
            "D_D": obs_D[i],
            "z_A": zAp,
            "z_B": zBp,
            "z_C": zCp,
            "z_D": zDp,
            "S_joint": s_joint_p,
        })

    ranked = sorted(per_boundary, key=lambda r: r["S_joint"], reverse=True)
    top5 = ranked[:5]
    bot5 = ranked[-5:]

    # Aligned-vs-intra mean S_joint
    aligned_scores = [r["S_joint"] for r in per_boundary if r["surah_aligned"]]
    intra_scores = [r["S_joint"] for r in per_boundary if not r["surah_aligned"]]
    aligned_mean = sum(aligned_scores) / len(aligned_scores) if aligned_scores else 0.0
    intra_mean = sum(intra_scores) / len(intra_scores) if intra_scores else 0.0

    # ------------------------------------------------------------------
    # MW-5 positive control: sample 29 surah-boundary positions
    # ------------------------------------------------------------------
    # Surah internal seams = surah_start_positions[1..] (113 positions)
    random.seed(SEED)
    surah_seam_positions = surah_start_positions[1:]  # 113 positions
    pc_sample = random.sample(surah_seam_positions, N_JUZ_INTERNAL)
    pcA, pcB, pcC, pcD = compute_all_axes(
        pc_sample, tokens_per_verse, lengths, rhymes, pn_counts, n, W
    )
    pc_SUM_A = sum(pcA)
    pc_SUM_B = sum(pcB)
    pc_SUM_C = sum(pcC)
    pc_SUM_D = sum(pcD)

    pc_pA = p_right(pc_SUM_A, null_SUM_A)
    pc_pB = p_right(pc_SUM_B, null_SUM_B)
    pc_pC = p_right(pc_SUM_C, null_SUM_C)
    pc_pD = p_right(pc_SUM_D, null_SUM_D)

    # Count axes where surah-positive-control > juz' observed
    pc_exceed = {
        "A": pc_SUM_A > SUM_A_obs,
        "B": pc_SUM_B > SUM_B_obs,
        "C": pc_SUM_C > SUM_C_obs,
        "D": pc_SUM_D > SUM_D_obs,
    }
    pc_exceed_count = sum(pc_exceed.values())
    pc_valid = pc_exceed_count >= 3

    # ------------------------------------------------------------------
    # Compile JSON
    # ------------------------------------------------------------------
    null_pct = lambda null_vals, q: sorted(null_vals)[int(q * len(null_vals))]

    out = {
        "hypothesis": "H-NEW-64",
        "seed": SEED,
        "n_perm": N_PERM,
        "window_w": W,
        "alpha_bon": ALPHA_BON,
        "verdict": verdict,
        "positive_control_valid": pc_valid,
        "positive_control": {
            "SUM_A": pc_SUM_A, "SUM_B": pc_SUM_B,
            "SUM_C": pc_SUM_C, "SUM_D": pc_SUM_D,
            "p_A": pc_pA, "p_B": pc_pB, "p_C": pc_pC, "p_D": pc_pD,
            "exceed_vs_juz": pc_exceed,
            "exceed_count": pc_exceed_count,
        },
        "axes": {
            "A": {
                "SUM_obs": SUM_A_obs,
                "null_mean": mA, "null_sd": sA,
                "null_p95": null_pct(null_SUM_A, 0.95),
                "null_p99": null_pct(null_SUM_A, 0.99),
                "z": zA, "p": pA, "pass": passA,
            },
            "B": {
                "SUM_obs": SUM_B_obs,
                "null_mean": mB, "null_sd": sB,
                "null_p95": null_pct(null_SUM_B, 0.95),
                "null_p99": null_pct(null_SUM_B, 0.99),
                "z": zB, "p": pB, "pass": passB,
            },
            "C": {
                "SUM_obs": SUM_C_obs,
                "null_mean": mC, "null_sd": sC,
                "null_p95": null_pct(null_SUM_C, 0.95),
                "null_p99": null_pct(null_SUM_C, 0.99),
                "z": zC, "p": pC, "pass": passC,
            },
            "D": {
                "SUM_obs": SUM_D_obs,
                "null_mean": mD, "null_sd": sD,
                "null_p95": null_pct(null_SUM_D, 0.95),
                "null_p99": null_pct(null_SUM_D, 0.99),
                "z": zD, "p": pD, "pass": passD,
            },
            "joint": {
                "obs": obs_JOINT,
                "null_p95": null_pct(null_JOINT, 0.95),
                "null_p99": null_pct(null_JOINT, 0.99),
                "p": pJ, "pass": passJ,
            },
        },
        "per_boundary": per_boundary,
        "top5_natural": top5,
        "bot5_natural": bot5,
        "surah_aligned_mean_Sjoint": aligned_mean,
        "intra_surah_mean_Sjoint": intra_mean,
        "surah_aligned_n": len(aligned_scores),
        "intra_surah_n": len(intra_scores),
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    # Console summary
    print(f"H-NEW-64 verdict: {verdict}")
    print(f"Positive control valid: {pc_valid} (exceed {pc_exceed_count}/4)")
    print(f"  axis A: SUM={SUM_A_obs:.4f}, p={pA:.4f}, pass={passA}")
    print(f"  axis B: SUM={SUM_B_obs:.4f}, p={pB:.4f}, pass={passB}")
    print(f"  axis C: SUM={SUM_C_obs:.4f}, p={pC:.4f}, pass={passC}")
    print(f"  axis D: SUM={SUM_D_obs:.4f}, p={pD:.4f}, pass={passD}")
    print(f"  joint:  obs={obs_JOINT:.4f}, p={pJ:.4f}, pass={passJ}")
    print(f"surah-aligned mean S_joint = {aligned_mean:.4f} (n={len(aligned_scores)})")
    print(f"intra-surah   mean S_joint = {intra_mean:.4f} (n={len(intra_scores)})")
    print("\nTop-5 most-natural juz' boundaries:")
    for r in top5:
        print(f"  juz' {r['juz_start']} @ Q{r['surah']}:{r['verse_id']}  "
              f"S_joint={r['S_joint']:.3f}  surah_aligned={r['surah_aligned']}")
    print("\nBot-5 least-natural juz' boundaries:")
    for r in bot5:
        print(f"  juz' {r['juz_start']} @ Q{r['surah']}:{r['verse_id']}  "
              f"S_joint={r['S_joint']:.3f}  surah_aligned={r['surah_aligned']}")


if __name__ == "__main__":
    main()
