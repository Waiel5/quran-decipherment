#!/usr/bin/env python3
"""Q024-F-05: nūr-root density rank in Q 24 vs corpus (LOCKED pre-reg).

Tests two metrics in parallel:
  Metric A: raw nwr-token count rank (descending), all 114 surahs.
  Metric B: nwr density rank among surahs with ≥3 nwr attestations.

Pre-reg locks both to ≤ 3 for Q 24.

Data sources (rules-tuple: no-tashkeel, QAC-stem-roots, QAC v0.4,
basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order):
  - /Users/grey/Downloads/quran/data/morphology/root-index.json
  - /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
"""
import json, hashlib, os

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-05-nur-root-density-rank-prereg.md"
EXPECTED_SHA = "01766034a8b22cb200930747a199a448295c6c7e55385603b2d8e16bbb36ef99"
ROOT_INDEX = f"{PROJECT}/data/morphology/root-index.json"
QURAN = f"{PROJECT}/quran-text/quran-no-tashkeel.json"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-05.json"

SEED = 20260509
MUSHAF_MARKS = set('۞ۖۗۚۛۜ')

# 1. SHA-lock the pre-reg
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256:    {sha}")
print(f"Expected:          {EXPECTED_SHA}")
if sha != EXPECTED_SHA:
    raise SystemExit("FAIL: pre-reg SHA mismatch — abort.")
print("OK SHA verified.\n")

# 2. Load nwr root attestations
with open(ROOT_INDEX) as f:
    root_idx = json.load(f)
nwr_attestations = root_idx['nwr']  # list of [surah, verse, word]
per_count = {s: 0 for s in range(1, 115)}
for s, v, w in nwr_attestations:
    per_count[s] += 1

# 3. Per-surah word counts (no-tashkeel orthographic, excluding basmala in Q2-114, excluding mushaf marks)
with open(QURAN) as f:
    quran = json.load(f)
per_words = {}
for s in quran:
    sid = s['id']
    total = 0
    for v in s['verses']:
        if sid != 1 and v['id'] == 1 and v['text'].startswith('بسم الله'):
            continue
        for w in v['text'].split():
            if w and not all(c in MUSHAF_MARKS for c in w):
                total += 1
    per_words[sid] = total

# 4. Metric A — raw count rank, ties broken by surah-id ascending
raw_ranked = sorted(range(1, 115), key=lambda s: (-per_count[s], s))
rank_A = raw_ranked.index(24) + 1
print(f"Metric A (raw nwr-token-count rank): Q 24 rank = {rank_A} / 114")
print(f"  top-10: {[(s, per_count[s]) for s in raw_ranked[:10]]}")

# 5. Metric B — density rank among surahs with ≥3 nwr attestations
attesting = [s for s in range(1, 115) if per_count[s] >= 3]
densities = {s: per_count[s] / per_words[s] for s in attesting}
dens_ranked = sorted(attesting, key=lambda s: (-densities[s], s))
rank_B = dens_ranked.index(24) + 1 if 24 in attesting else None
print(f"\nMetric B (density rank among ≥3-attestation surahs, n={len(attesting)}): "
      f"Q 24 rank = {rank_B} / {len(attesting)}")
print("  top-10 by density:")
for s in dens_ranked[:10]:
    print(f"    Q{s:>3}: count={per_count[s]:>2} words={per_words[s]:>4} density={densities[s]:.5f}")

# 6. Verdict
pred_A_met = rank_A <= 3
pred_B_met = (rank_B is not None) and (rank_B <= 3)
if pred_A_met and pred_B_met:
    verdict = "CONFIRMED"
elif pred_A_met or pred_B_met:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"
print(f"\nVerdict: {verdict} (A pred ≤3: {pred_A_met}; B pred ≤3: {pred_B_met})")

# 7. Write JSON
out = {
    'finding_id': 'Q024-F-05',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'date': '2026-05-09',
    'rules_tuple': '(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)',
    'metric_A_raw_count': {
        'q24_count': per_count[24],
        'q24_rank': rank_A,
        'n_surahs': 114,
        'top10': [{'surah': s, 'count': per_count[s]} for s in raw_ranked[:10]],
        'prediction_met': pred_A_met,
    },
    'metric_B_density_attesting': {
        'q24_density': densities.get(24),
        'q24_rank': rank_B,
        'n_attesting': len(attesting),
        'top10': [{'surah': s, 'count': per_count[s], 'words': per_words[s],
                   'density': densities[s]} for s in dens_ranked[:10]],
        'prediction_met': pred_B_met,
    },
    'verdict': verdict,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(out, f, indent=2)
print(f"\nWrote {OUT}")
