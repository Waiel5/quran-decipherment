#!/usr/bin/env python3
"""
H-NEW-950 — per-surah spectral analysis of divine-name occurrences.

Pre-reg: findings/phase-b-hypotheses/h-new-950-divine-name-spectral-prereg.md
Pre-reg SHA-256 (locked): db3bfec9306696f71a46484d182313039b32dcac19ea68234993c26bad236668
Seed: 20260507
N perms per surah: 1000
Bonferroni k = 150 (50 long surahs × top-3 peaks)
"""

import hashlib
import json
import math
import os
import random
import re
import sys
from collections import Counter

import numpy as np
from scipy.signal import lombscargle

PROJECT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(PROJECT, "findings/phase-b-hypotheses/h-new-950-divine-name-spectral-prereg.md")
EXPECTED_SHA = "db3bfec9306696f71a46484d182313039b32dcac19ea68234993c26bad236668"
QURAN = os.path.join(PROJECT, "quran-text/quran-no-tashkeel.json")
NAMES = os.path.join(PROJECT, "data/asma-al-husna.txt")
OUT_JSON = os.path.join(PROJECT, "findings/phase-b-hypotheses/csv/h-new-950.json")

SEED = 20260507
N_PERM = 1000
TOP_K = 3
ALPHA_BON = 0.05 / 150
LONG_THRESHOLD = 50

# Verify pre-reg SHA
with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f"FATAL: pre-reg SHA mismatch. expected={EXPECTED_SHA}, got={actual}")
print(f"[OK] pre-reg SHA verified: {actual}")

# Load divine names
names = []
with open(NAMES) as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        names.append(line)
print(f"[OK] loaded {len(names)} divine names")

# Build a regex of all names with proclitic prefixes
PROCLITICS = ["", "و", "ف", "ب", "ل", "ك", "س", "فب", "وب", "فل", "ول", "وس", "فس"]
patterns = []
for name in names:
    for p in PROCLITICS:
        patterns.append(re.escape(p + name))
# Sort by length desc so longer patterns match first
patterns.sort(key=len, reverse=True)
RE_NAME = re.compile(r"(?<![ء-ي])(" + "|".join(patterns) + r")(?![ء-ي])")
# The (?<! ... ) (?! ... ) ensures word-boundary on Arabic letters

# Load Quran
with open(QURAN) as f:
    quran = json.load(f)

# Build per-surah verse-text list
surahs = {}  # surah_id -> list of verse texts (1-indexed by position)
if isinstance(quran, dict) and "data" in quran:
    quran = quran["data"]
for s_obj in quran:
    sid = s_obj.get("number") or s_obj.get("id") or s_obj.get("index")
    if sid is None:
        # try other shapes
        continue
    verses = s_obj.get("verses") or s_obj.get("ayahs") or s_obj.get("ayat")
    if verses is None:
        continue
    surahs[int(sid)] = []
    for v in verses:
        text = v.get("text") or v.get("ayah") or v.get("content") or ""
        surahs[int(sid)].append(text)


# Sanity check — should be 114 surahs
print(f"[OK] loaded {len(surahs)} surahs")
# Q1 should have 7 verses
print(f"[OK] Q1 has {len(surahs.get(1, []))} verses")
# Verify Q2 has 286
print(f"[OK] Q2 has {len(surahs.get(2, []))} verses")


def count_names_per_verse(verses):
    return [len(RE_NAME.findall(v)) for v in verses]


# Cluster typology mapping
CLUSTER = {}
for q in [40, 41, 42, 43, 44, 45, 46]:
    CLUSTER[q] = "HM"
for q in [10, 11, 12, 13, 14, 15]:
    CLUSTER[q] = "ALR"
for q in [2, 3, 29, 30, 31, 32]:
    CLUSTER[q] = "ALM"
for q in [7, 19, 20, 26, 27, 28, 36, 38, 50, 68]:
    CLUSTER[q] = "OTHER_MUQ"

def cluster_for(qid):
    return CLUSTER.get(qid, "NO_MUQ")


# Compute periodogram and identify top-K peaks
def lomb_periodogram(f_series):
    n = len(f_series)
    if n < 6:
        return [], np.array([]), np.array([])
    t = np.arange(1, n + 1, dtype=float)
    # Frequency grid: T in [2, n/2] step 0.5
    T_grid = np.arange(2.0, math.floor(n / 2.0) + 0.5, 0.5)
    omega = 2 * math.pi / T_grid
    y = np.array(f_series, dtype=float)
    # Subtract mean (Lomb-Scargle convention)
    y = y - y.mean()
    if y.std() == 0:
        return [], T_grid, np.zeros_like(T_grid)
    pgram = lombscargle(t, y, omega, normalize=False)
    return T_grid, omega, pgram


def find_top_peaks(T_grid, pgram, k=TOP_K):
    if len(pgram) == 0:
        return []
    order = np.argsort(pgram)[::-1]
    selected_idx = []
    for i in order:
        if all(abs(i - j) >= 1 for j in selected_idx):
            selected_idx.append(int(i))
        if len(selected_idx) >= k:
            break
    return [(T_grid[i], pgram[i], i) for i in selected_idx]


# Permutation null: for each surah, shuffle f_series N_PERM times
def perm_p_values(f_series, observed_peaks, n_perm=N_PERM, seed=SEED):
    if not observed_peaks or len(f_series) < 6:
        return [(1.0, 1.0)] * len(observed_peaks), 1.0
    n = len(f_series)
    t = np.arange(1, n + 1, dtype=float)
    T_grid = np.arange(2.0, math.floor(n / 2.0) + 0.5, 0.5)
    omega = 2 * math.pi / T_grid
    rng = np.random.default_rng(seed)
    y = np.array(f_series, dtype=float)
    if y.std() == 0:
        return [(1.0, 1.0)] * len(observed_peaks), 1.0
    # Per-frequency null counts at each peak's index
    per_freq_count = [0] * len(observed_peaks)
    le_count = 0  # look-elsewhere: any perm peak >= obs max-power
    obs_max = max(p[1] for p in observed_peaks)
    for r in range(n_perm):
        y_shuf = rng.permutation(y)
        y_shuf = y_shuf - y_shuf.mean()
        if y_shuf.std() == 0:
            continue
        pgram = lombscargle(t, y_shuf, omega, normalize=False)
        for k, (_, obs_power, idx) in enumerate(observed_peaks):
            if pgram[idx] >= obs_power:
                per_freq_count[k] += 1
        if pgram.max() >= obs_max:
            le_count += 1
    p_per_freq = [(c + 1) / (n_perm + 1) for c in per_freq_count]
    p_le = (le_count + 1) / (n_perm + 1)
    return p_per_freq, p_le


# Main loop
print(f"\n[RUN] Spectral analysis on long surahs (N_s >= {LONG_THRESHOLD})...")
results = {}
long_surahs = [(s, v) for s, v in surahs.items() if len(v) >= LONG_THRESHOLD]
long_surahs.sort()
print(f"[OK] {len(long_surahs)} long surahs qualify")

for sid, verses in long_surahs:
    f_series = count_names_per_verse(verses)
    n = len(f_series)
    total_names = sum(f_series)
    if total_names == 0:
        results[sid] = {"n_verses": n, "total_names": 0, "skipped": True}
        continue
    T_grid, omega, pgram = lomb_periodogram(f_series)
    peaks = find_top_peaks(T_grid, pgram, TOP_K)
    p_per_freq, p_le = perm_p_values(f_series, peaks, n_perm=N_PERM, seed=SEED + sid)
    peak_records = []
    survives_bon = False
    for (T_val, power, idx), p_freq in zip(peaks, p_per_freq):
        survived = (p_le <= ALPHA_BON) and (p_freq <= ALPHA_BON)
        if survived:
            survives_bon = True
        peak_records.append({
            "period_verses": T_val,
            "power": power,
            "p_per_freq": p_freq,
            "p_look_elsewhere_for_max": p_le,  # same for whole surah
            "survives_bonferroni_150": survived,
        })
    results[sid] = {
        "n_verses": n,
        "total_names": total_names,
        "name_density": total_names / n,
        "cluster": cluster_for(sid),
        "top_peaks": peak_records,
        "p_look_elsewhere": p_le,
        "any_peak_survives_bon": survives_bon,
    }
    print(f"  Q{sid:3d} (N={n:3d}, names={total_names:4d}): "
          f"top-T={peaks[0][0]:.1f} power={peaks[0][1]:.3f} "
          f"p_LE={p_le:.4f}  survives_bon={survives_bon}")

# Aggregate
n_pass = sum(1 for r in results.values() if r.get("any_peak_survives_bon", False))
n_total = len(results)
print(f"\n[AGG] {n_pass}/{n_total} long surahs have ANY peak surviving Bonferroni-150 (α_bon = {ALPHA_BON:.6f})")

# H2: cluster typology
cluster_counts = Counter()
cluster_pass = Counter()
for sid, r in results.items():
    c = r.get("cluster", "NO_MUQ")
    cluster_counts[c] += 1
    if r.get("any_peak_survives_bon"):
        cluster_pass[c] += 1
print(f"\n[H2] Pass-rate by cluster:")
for c in sorted(cluster_counts):
    n_c = cluster_counts[c]
    p_c = cluster_pass[c]
    print(f"  {c:10s}: {p_c}/{n_c} pass")

# H2 chi-square
clusters_list = sorted(cluster_counts.keys())
observed = [cluster_pass[c] for c in clusters_list]
expected = []
overall_pass_rate = n_pass / n_total if n_total > 0 else 0
for c in clusters_list:
    expected.append(cluster_counts[c] * overall_pass_rate)
if all(e > 0 for e in expected) and n_pass > 0:
    chi2 = sum((o - e) ** 2 / e for o, e in zip(observed, expected))
    df = len(clusters_list) - 1
    h2_chi2 = chi2
    h2_df = df
else:
    h2_chi2 = None
    h2_df = None

# MW-5 instrument-control: shuffle Q 2
print(f"\n[MW-5] Instrument-control: shuffle Q 2 once and re-run...")
q2 = surahs[2]
f2 = count_names_per_verse(q2)
rng = np.random.default_rng(SEED)
f2_shuf = list(rng.permutation(f2))
T_grid, omega, pgram = lomb_periodogram(f2_shuf)
peaks_shuf = find_top_peaks(T_grid, pgram, TOP_K)
p_per_freq_shuf, p_le_shuf = perm_p_values(f2_shuf, peaks_shuf, n_perm=N_PERM, seed=SEED + 1)
mw5_pass_count = sum(1 for p in p_per_freq_shuf if p <= ALPHA_BON and p_le_shuf <= ALPHA_BON)
print(f"  Q2-shuffle: top-T={peaks_shuf[0][0]:.1f}, p_LE={p_le_shuf:.4f}, peaks_surviving_bon={mw5_pass_count}")
mw5_clean = (mw5_pass_count == 0)
print(f"  MW-5 instrument-control: {'CLEAN' if mw5_clean else 'BROKEN'}")

# Verdict
if n_pass == 0:
    verdict = "NULL: divine-name placement is spectrally-RANDOM (H3 falsifier triggered)"
elif n_pass >= 1:
    verdict = f"PASS-DIRECTED: {n_pass} long-surah(s) show Bonferroni-surviving spectral peak"

print(f"\n[VERDICT] {verdict}")

# Write JSON
out = {
    "finding_id": "h-new-950",
    "title": "Per-surah spectral analysis of divine-name occurrences (Lomb-Scargle)",
    "pre_reg_sha256": EXPECTED_SHA,
    "seed": SEED,
    "n_perm_per_surah": N_PERM,
    "n_long_surahs": n_total,
    "long_surah_threshold": LONG_THRESHOLD,
    "alpha_bon_150": ALPHA_BON,
    "names_count": len(names),
    "results": {str(k): v for k, v in results.items()},
    "h1_n_pass": n_pass,
    "h1_n_total": n_total,
    "h2_cluster_counts": dict(cluster_counts),
    "h2_cluster_pass": dict(cluster_pass),
    "h2_chi2": h2_chi2,
    "h2_df": h2_df,
    "mw5_q2_shuffle_clean": mw5_clean,
    "mw5_q2_shuffle_pass_count": mw5_pass_count,
    "verdict": verdict,
}

os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, "w") as f:
    json.dump(out, f, indent=2, ensure_ascii=False, default=str)
print(f"\n[OK] wrote {OUT_JSON}")
