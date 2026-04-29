#!/usr/bin/env python3
"""
Opening-compression-prediction test.

Pre-registered hypothesis:
    "Fatihat al-sura tadullu ala khatimatiha" — the opening of a surah
    indicates/compresses its closing. If the opening of a surah is a
    compressed form of the surah, then concatenating (opening_X, body_X)
    should gzip more tightly than concatenating (opening_X, body_Y) for
    foreign body Y.

Primary statistic: for each surah X (skipping Al-Fatiha, for which
opening ~= body), rank the self-concatenation (opening_X + body_X) by
gzip size against the 113 foreign concatenations (opening_X + body_Y
for Y != X). Self rank should be 1 (smallest gzip) if the opening
perfectly fits its own body.

Report:
    - distribution of self-ranks across 113 surahs
    - fraction in top-1 (expected 1/114 = 0.88% under null)
    - fraction in top-10 (expected 10/114 = 8.77% under null)
    - NCD (Normalized Compression Distance) form:
        NCD(x, y) = (C(xy) - min(C(x), C(y))) / max(C(x), C(y))
      where C = gzip size.
    - binomial tests against uniform-rank null.

Secondary test: last verse as "closing signature" predicting body.
Tertiary test: adjacent-surah coherence along canonical ordering.

Rules tuple:
    orthography: no-tashkeel (JSON)
    word_definition: not-applicable (this is compression-level)
    letter_definition: not-applicable
    basmala_policy: counted-only-in-surah-1 (amrayn default; basmala
        absent from surah-internal text except surah 1 verse 1)
    verse_numbering: hafs-kufan
    abjad_table: not-applicable
    null_model: uniform-rank-under-random-pairing (binomial k/113) +
        canonical-order shuffle (1000 perms) for tertiary test
"""
import json
import gzip
import csv
import math
import random
import re
from collections import Counter
from pathlib import Path
import sys

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"
OUT_DIR = ROOT / "findings" / "phase-b-hypotheses"
OUT_CSV = OUT_DIR / "csv"
OUT_CSV.mkdir(parents=True, exist_ok=True)

random.seed(42)

# ---------- Load corpus ----------
with open(CORPUS) as f:
    quran = json.load(f)

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

surahs = {}
for surah in quran:
    sid = surah["id"]
    verses = [v["text"] for v in surah["verses"]]
    surahs[sid] = {
        "name": surah["transliteration"],
        "type": surah["type"],
        "n_verses": len(verses),
        "verses": verses,
        "text": norm(" ".join(verses)),
        "first_verse": norm(verses[0]),
        "last_verse": norm(verses[-1]),
        # body = all verses except first (or except last for secondary test)
        "body_excl_first": norm(" ".join(verses[1:])) if len(verses) > 1 else "",
        "body_excl_last": norm(" ".join(verses[:-1])) if len(verses) > 1 else "",
    }

# Compression helper
def gz(s):
    return len(gzip.compress(s.encode("utf-8"), compresslevel=9))

# Cache individual compressed sizes (useful for NCD)
C_opening = {}
C_body = {}
C_last = {}
C_body_excl_last = {}
for sid in range(1, 115):
    C_opening[sid] = gz(surahs[sid]["first_verse"])
    C_body[sid] = gz(surahs[sid]["body_excl_first"])
    C_last[sid] = gz(surahs[sid]["last_verse"])
    C_body_excl_last[sid] = gz(surahs[sid]["body_excl_last"])

# ---------- Primary test: opening predicts body ----------
# For each surah X (2..114), concatenate opening_X + body_Y for Y in 2..114
# (but body_Y must have non-empty body). Compute gzip(concat). Rank them.

# We also include surah 1 bodies because foreign bodies can come from anywhere;
# the excluded surah is just surah 1 as the X-subject (since its "body" is
# effectively nothing — 7 verses and the "opening" IS the surah).

eligible_X = [s for s in range(1, 115) if len(surahs[s]["verses"]) >= 2]
eligible_Y_bodies = [s for s in range(1, 115) if surahs[s]["body_excl_first"]]

# Primary test: skip surah 1 as X per task instructions (opening is the whole surah)
primary_X = [s for s in eligible_X if s != 1]

print(f"Primary test: {len(primary_X)} surahs as X", file=sys.stderr)

primary_rows = []
for X in primary_X:
    opening_X = surahs[X]["first_verse"]
    cx = C_opening[X]
    # concatenate opening_X with each body Y; compute INCREMENTAL cost delta
    # (raw size is confounded by body length — a short foreign body always
    # yields smaller gzip). The length-controlled statistic is
    # delta(Y) = gz(opening_X + body_Y) - gz(body_Y)
    # which measures "how many extra bytes does opening_X add to body_Y".
    sizes = {}     # raw gz(opening + body_Y)
    deltas = {}    # incremental cost
    ncds = {}      # normalized compression distance
    for Y in eligible_Y_bodies:
        body_Y = surahs[Y]["body_excl_first"]
        concat = opening_X + " " + body_Y
        c_xy = gz(concat)
        sizes[Y] = c_xy
        deltas[Y] = c_xy - C_body[Y]
        cy = C_body[Y]
        ncd = (c_xy - min(cx, cy)) / max(cx, cy)
        ncds[Y] = ncd
    # Rank Y by each statistic (smallest = best fit)
    ranking_size = sorted(sizes.keys(), key=lambda y: sizes[y])
    ranking_delta = sorted(deltas.keys(), key=lambda y: deltas[y])
    ranking_ncd = sorted(ncds.keys(), key=lambda y: ncds[y])
    self_rank_size = ranking_size.index(X) + 1
    self_rank_delta = ranking_delta.index(X) + 1
    self_rank_ncd = ranking_ncd.index(X) + 1
    foreign_deltas = [deltas[y] for y in deltas if y != X]
    foreign_sizes = [sizes[y] for y in sizes if y != X]
    primary_rows.append({
        "surah": X,
        "name": surahs[X]["name"],
        "type": surahs[X]["type"],
        "n_verses": surahs[X]["n_verses"],
        "opening_chars": len(opening_X),
        "body_chars": len(surahs[X]["body_excl_first"]),
        "self_concat_gz": sizes[X],
        "self_delta": deltas[X],
        "self_ncd": ncds[X],
        "foreign_mean_gz": sum(foreign_sizes) / len(foreign_sizes),
        "foreign_mean_delta": sum(foreign_deltas) / len(foreign_deltas),
        "foreign_min_delta": min(foreign_deltas),
        "foreign_max_delta": max(foreign_deltas),
        "self_rank_size": self_rank_size,
        "self_rank_delta": self_rank_delta,
        "self_rank_ncd": self_rank_ncd,
        "n_candidates": len(sizes),
    })

# ---------- Secondary: last verse predicts body ----------
# "Khatimat al-sura tadullu ala siaqiha" — does the closing verse
# compress-predict the body?
secondary_X = [s for s in range(1, 115) if len(surahs[s]["verses"]) >= 2 and s != 1]
secondary_Y_bodies = [s for s in range(1, 115) if surahs[s]["body_excl_last"]]

print(f"Secondary test: {len(secondary_X)} surahs as X", file=sys.stderr)
secondary_rows = []
for X in secondary_X:
    last_X = surahs[X]["last_verse"]
    deltas = {}
    sizes = {}
    for Y in secondary_Y_bodies:
        body_Y = surahs[Y]["body_excl_last"]
        c_xy = gz(last_X + " " + body_Y)
        sizes[Y] = c_xy
        deltas[Y] = c_xy - C_body_excl_last[Y]
    ranking_delta = sorted(deltas.keys(), key=lambda y: deltas[y])
    ranking_size = sorted(sizes.keys(), key=lambda y: sizes[y])
    self_rank_delta = ranking_delta.index(X) + 1
    self_rank_size = ranking_size.index(X) + 1
    secondary_rows.append({
        "surah": X,
        "name": surahs[X]["name"],
        "type": surahs[X]["type"],
        "n_candidates": len(sizes),
        "self_rank_delta": self_rank_delta,
        "self_rank_size": self_rank_size,
        "self_delta": deltas[X],
        "foreign_mean_delta": sum(deltas[y] for y in deltas if y != X) / (len(deltas) - 1),
    })

# ---------- Tertiary: canonical-order adjacency coherence ----------
# Test: does opening_{N+1} compress-fit body_N better than expected under random order?
# For each adjacent pair (N, N+1), compute gzip(opening_{N+1} + body_N) and rank
# it among all 113 possible source openings for body_N.

# We quantify "does it rank better than chance (median 57)?"
adjacency_ranks_forward = []  # opening of N+1 vs body N
adjacency_ranks_reverse = []  # opening of N-1 vs body N

def rank_opening_for_body(source_X, body_Y):
    """How does opening_source rank among all 114 openings when concatenated
    with body_Y? Rank 1 = tightest fit."""
    opening = surahs[source_X]["first_verse"]
    body = surahs[body_Y]["body_excl_first"]
    base = gz(opening + " " + body)
    # Compute size for every possible source
    sizes = {}
    for s in range(1, 115):
        if s == body_Y:
            continue  # exclude self from the comparison pool
        if not surahs[s]["first_verse"]:
            continue
        sizes[s] = gz(surahs[s]["first_verse"] + " " + body)
    # Rank the specified source among candidates (including itself)
    sizes[source_X] = base
    ranking = sorted(sizes.keys(), key=lambda s: sizes[s])
    return ranking.index(source_X) + 1, len(sizes)

# Forward: opening of N+1 paired with body of N, for N=2..113 (skip surah 1)
for N in range(2, 114):
    if N + 1 > 114:
        break
    r, n = rank_opening_for_body(N + 1, N)
    adjacency_ranks_forward.append((N, N + 1, r, n))

# Reverse: opening of N-1 paired with body of N
for N in range(3, 115):
    r, n = rank_opening_for_body(N - 1, N)
    adjacency_ranks_reverse.append((N, N - 1, r, n))

# Null: permute surah labels 1000 times, recompute average adjacency rank.
# A real "adjacent surahs cohere" signal would show lower mean rank than null.

def mean_adjacent_rank(order):
    """Given permutation `order` (list of surah ids), compute mean rank
    of opening_{next} against body_{current}."""
    ranks = []
    for i in range(len(order) - 1):
        cur = order[i]
        nxt = order[i + 1]
        if cur == 1 or nxt == 1:
            continue
        if not surahs[cur]["body_excl_first"]:
            continue
        # Use cached concat sizes? No — we'll just re-gzip.
        ranks.append(rank_opening_for_body(nxt, cur)[0])
    return sum(ranks) / len(ranks) if ranks else float("nan")

# Observed
canonical_order = list(range(1, 115))
obs_mean_fwd = sum(r for (_, _, r, _) in adjacency_ranks_forward) / len(adjacency_ranks_forward)
obs_mean_rev = sum(r for (_, _, r, _) in adjacency_ranks_reverse) / len(adjacency_ranks_reverse)

# Null: shuffle canonical order, recompute. This is 1.5 (permutation of surah indices).
# To keep runtime reasonable, we precompute an NxN matrix of gz(opening_i + body_j).
print("Precomputing 114x114 gzip matrix for tertiary test...", file=sys.stderr)
# M[i][j] = delta = gz(opening_i + body_j) - gz(body_j)   (length-controlled)
M = [[None] * 115 for _ in range(115)]
for i in range(1, 115):
    op_i = surahs[i]["first_verse"]
    if not op_i:
        continue
    for j in range(1, 115):
        body_j = surahs[j]["body_excl_first"]
        if not body_j:
            continue
        M[i][j] = gz(op_i + " " + body_j) - C_body[j]

# Now: for body j, rank of opening i = count of k != j where M[k][j] < M[i][j], plus 1.
def rank_i_for_body_j(i, j):
    base = M[i][j]
    if base is None:
        return None
    c = 1
    for k in range(1, 115):
        if k == j or k == i:
            continue
        if M[k][j] is None:
            continue
        if M[k][j] < base:
            c += 1
    return c

# Re-check observed using matrix
fwd_ranks_matrix = []
for N in range(2, 114):
    if N + 1 > 114:
        break
    r = rank_i_for_body_j(N + 1, N)
    if r is not None:
        fwd_ranks_matrix.append(r)

rev_ranks_matrix = []
for N in range(3, 115):
    r = rank_i_for_body_j(N - 1, N)
    if r is not None:
        rev_ranks_matrix.append(r)

obs_fwd = sum(fwd_ranks_matrix) / len(fwd_ranks_matrix)
obs_rev = sum(rev_ranks_matrix) / len(rev_ranks_matrix)

# Null: shuffle canonical order 1000 times, compute mean adjacency rank
print("Running canonical-order shuffle null (1000 perms) for tertiary test...", file=sys.stderr)
NPERM = 1000
null_means_fwd = []
for _ in range(NPERM):
    order = list(range(2, 115))  # skip surah 1
    random.shuffle(order)
    ranks = []
    for idx in range(len(order) - 1):
        cur = order[idx]
        nxt = order[idx + 1]
        if not surahs[cur]["body_excl_first"]:
            continue
        r = rank_i_for_body_j(nxt, cur)
        if r is not None:
            ranks.append(r)
    null_means_fwd.append(sum(ranks) / len(ranks))

null_mean_fwd = sum(null_means_fwd) / NPERM
null_sd_fwd = math.sqrt(sum((x - null_mean_fwd) ** 2 for x in null_means_fwd) / NPERM)
z_fwd = (obs_fwd - null_mean_fwd) / null_sd_fwd if null_sd_fwd > 0 else 0
p_fwd_le = sum(1 for x in null_means_fwd if x <= obs_fwd) / NPERM
p_fwd_ge = sum(1 for x in null_means_fwd if x >= obs_fwd) / NPERM

# Compute primary-test summary stats — PRIMARY statistic is DELTA
# (length-controlled; raw gzip size is confounded by body length)
self_ranks_delta = [r["self_rank_delta"] for r in primary_rows]
self_ranks_size = [r["self_rank_size"] for r in primary_rows]
self_ranks_ncd = [r["self_rank_ncd"] for r in primary_rows]
self_ranks = self_ranks_delta  # primary statistic

n = len(self_ranks)
top1 = sum(1 for r in self_ranks if r == 1)
top5 = sum(1 for r in self_ranks if r <= 5)
top10 = sum(1 for r in self_ranks if r <= 10)
top25 = sum(1 for r in self_ranks if r <= 25)
top_half = sum(1 for r in self_ranks if r <= 57)
median_rank = sorted(self_ranks)[len(self_ranks) // 2]
mean_rank = sum(self_ranks) / len(self_ranks)

# Binomial p-values under uniform-null (rank uniform on [1, 114])
# P(rank <= k | uniform) = k/114
def binom_pval_one_tail_upper(k_obs, n_trials, p):
    """P(X >= k_obs | Binom(n, p))."""
    from math import comb
    return sum(comb(n_trials, i) * (p ** i) * ((1 - p) ** (n_trials - i))
               for i in range(k_obs, n_trials + 1))

p_top1 = binom_pval_one_tail_upper(top1, n, 1 / 114)
p_top5 = binom_pval_one_tail_upper(top5, n, 5 / 114)
p_top10 = binom_pval_one_tail_upper(top10, n, 10 / 114)
p_top25 = binom_pval_one_tail_upper(top25, n, 25 / 114)

# Secondary summary — use DELTA as primary
sec_ranks = [r["self_rank_delta"] for r in secondary_rows]
sec_top1 = sum(1 for r in sec_ranks if r == 1)
sec_top10 = sum(1 for r in sec_ranks if r <= 10)
sec_median = sorted(sec_ranks)[len(sec_ranks) // 2]

p_sec_top1 = binom_pval_one_tail_upper(sec_top1, len(sec_ranks), 1 / 114)
p_sec_top10 = binom_pval_one_tail_upper(sec_top10, len(sec_ranks), 10 / 114)

# Save per-surah primary rows
with open(OUT_CSV / "opening_compression_primary.csv", "w", newline="") as f:
    fieldnames = ["surah", "name", "type", "n_verses", "opening_chars", "body_chars",
                  "self_concat_gz", "self_delta", "self_ncd",
                  "foreign_mean_gz", "foreign_mean_delta", "foreign_min_delta",
                  "foreign_max_delta", "self_rank_size", "self_rank_delta",
                  "self_rank_ncd", "n_candidates"]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for r in primary_rows:
        w.writerow(r)

with open(OUT_CSV / "opening_compression_secondary.csv", "w", newline="") as f:
    fieldnames = ["surah", "name", "type", "n_candidates",
                  "self_rank_delta", "self_rank_size",
                  "self_delta", "foreign_mean_delta"]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for r in secondary_rows:
        w.writerow(r)

# Save rank histograms
with open(OUT_CSV / "opening_compression_primary_ranks.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["rank_bin", "primary_delta", "primary_size", "primary_ncd", "secondary_delta"])
    bins = [(1, 1), (2, 5), (6, 10), (11, 25), (26, 57), (58, 114)]
    for lo, hi in bins:
        c_d = sum(1 for r in self_ranks_delta if lo <= r <= hi)
        c_s = sum(1 for r in self_ranks_size if lo <= r <= hi)
        c_n = sum(1 for r in self_ranks_ncd if lo <= r <= hi)
        c_sec = sum(1 for r in sec_ranks if lo <= r <= hi)
        w.writerow([f"{lo}-{hi}", c_d, c_s, c_n, c_sec])

# Summary report
summary = {
    "primary": {
        "n_surahs_tested": n,
        "mean_self_rank": mean_rank,
        "median_self_rank": median_rank,
        "expected_mean_rank_under_null": (len(eligible_Y_bodies) + 1) / 2,
        "top_1_count": top1, "top_1_pct": 100 * top1 / n,
        "top_5_count": top5, "top_5_pct": 100 * top5 / n,
        "top_10_count": top10, "top_10_pct": 100 * top10 / n,
        "top_25_count": top25, "top_25_pct": 100 * top25 / n,
        "top_half_count": top_half, "top_half_pct": 100 * top_half / n,
        "binom_p_top_1": p_top1,
        "binom_p_top_5": p_top5,
        "binom_p_top_10": p_top10,
        "binom_p_top_25": p_top25,
    },
    "primary_statistic": "delta = gz(opening_X + body_Y) - gz(body_Y)",
    "primary_size_confounded": {
        "top_1_count": sum(1 for r in self_ranks_size if r == 1),
        "top_10_count": sum(1 for r in self_ranks_size if r <= 10),
        "median_rank": sorted(self_ranks_size)[len(self_ranks_size) // 2],
        "note": "raw gzip size ranking is confounded by body length",
    },
    "primary_ncd": {
        "top_1_count": sum(1 for r in self_ranks_ncd if r == 1),
        "top_10_count": sum(1 for r in self_ranks_ncd if r <= 10),
        "median_rank": sorted(self_ranks_ncd)[len(self_ranks_ncd) // 2],
    },
    "secondary": {
        "n_surahs_tested": len(sec_ranks),
        "top_1_count": sec_top1,
        "top_10_count": sec_top10,
        "median_self_rank": sec_median,
        "binom_p_top_1": p_sec_top1,
        "binom_p_top_10": p_sec_top10,
    },
    "tertiary": {
        "obs_mean_fwd_rank": obs_fwd,
        "obs_mean_rev_rank": obs_rev,
        "null_mean_fwd": null_mean_fwd,
        "null_sd_fwd": null_sd_fwd,
        "z_fwd": z_fwd,
        "empirical_p_fwd_le": p_fwd_le,
        "empirical_p_fwd_ge": p_fwd_ge,
        "n_perms": NPERM,
    },
}

with open(OUT_CSV / "opening_compression_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

# ---------- Console output ----------
print("\n=== PRIMARY: opening-X fit against body-Y via INCREMENTAL gzip cost ===")
print(f"  Statistic: delta(Y) = gz(opening_X + body_Y) - gz(body_Y)")
print(f"  N surahs tested (excl surah 1, with >=2 verses): {n}")
print(f"  Expected mean rank under uniform null: {(len(eligible_Y_bodies) + 1) / 2:.1f}")
print(f"  Observed mean self-rank (delta): {mean_rank:.1f}")
print(f"  Observed median self-rank (delta): {median_rank}")
print(f"  top-1 (self-best): {top1}/{n} = {100*top1/n:.1f}% (null 0.9%)  binom-p={p_top1:.3g}")
print(f"  top-5            : {top5}/{n} = {100*top5/n:.1f}% (null 4.4%)  binom-p={p_top5:.3g}")
print(f"  top-10           : {top10}/{n} = {100*top10/n:.1f}% (null 8.8%)  binom-p={p_top10:.3g}")
print(f"  top-25           : {top25}/{n} = {100*top25/n:.1f}% (null 21.9%) binom-p={p_top25:.3g}")
print(f"  top-half (<=57)  : {top_half}/{n} = {100*top_half/n:.1f}% (null 50%)")

print(f"\n  NCD variant (normalized compression distance):")
print(f"  top-1 (self-best): {sum(1 for r in self_ranks_ncd if r == 1)}/{n}")
print(f"  top-10           : {sum(1 for r in self_ranks_ncd if r <= 10)}/{n}")
print(f"  median           : {sorted(self_ranks_ncd)[len(self_ranks_ncd) // 2]}")

print(f"\n  Raw-size variant (length-confounded, for reference):")
print(f"  top-1: {sum(1 for r in self_ranks_size if r == 1)}/{n}")
print(f"  top-10: {sum(1 for r in self_ranks_size if r <= 10)}/{n}")
print(f"  median: {sorted(self_ranks_size)[len(self_ranks_size) // 2]}")

print("\n=== SECONDARY: last-verse fit against body-Y ===")
print(f"  top-1: {sec_top1}/{len(sec_ranks)} = {100*sec_top1/len(sec_ranks):.1f}% (null 0.9%)  binom-p={p_sec_top1:.3g}")
print(f"  top-10: {sec_top10}/{len(sec_ranks)} = {100*sec_top10/len(sec_ranks):.1f}% (null 8.8%) binom-p={p_sec_top10:.3g}")
print(f"  median self-rank: {sec_median}")

print("\n=== TERTIARY: canonical-order adjacency ===")
print(f"  Observed mean rank of opening_{{N+1}} against body_N: {obs_fwd:.2f}")
print(f"  Observed mean rank (reverse, opening_{{N-1}} against body_N): {obs_rev:.2f}")
print(f"  Null mean (1000 shuffled orders): {null_mean_fwd:.2f} ± {null_sd_fwd:.2f}")
print(f"  z = {z_fwd:+.2f},  p(obs <= null) = {p_fwd_le:.4f}")

# Print worst and best primary-test cases
print("\n=== Top 10 surahs with BEST self-rank (delta: opening fits its own body) ===")
best = sorted(primary_rows, key=lambda r: r["self_rank_delta"])
for r in best[:10]:
    print(f"  Q{r['surah']:>3} {r['name']:<20} self-rank={r['self_rank_delta']:>3}/{r['n_candidates']}  "
          f"self-delta={r['self_delta']}  foreign-mean-delta={r['foreign_mean_delta']:.1f}")

print("\n=== Top 10 surahs with WORST self-rank (delta) ===")
for r in best[-10:]:
    print(f"  Q{r['surah']:>3} {r['name']:<20} self-rank={r['self_rank_delta']:>3}/{r['n_candidates']}  "
          f"self-delta={r['self_delta']}  foreign-mean-delta={r['foreign_mean_delta']:.1f}")

print("\n=== DONE ===", file=sys.stderr)
