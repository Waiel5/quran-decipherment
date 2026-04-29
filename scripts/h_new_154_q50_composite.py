#!/usr/bin/env python3
"""H-NEW-154 — Q 50 composite hub-mechanism score.

Pre-committed feature set (binary, equal-weight):
  F1: position-centrality (Q 40-60)
  F2: book-reflexive opening (qrA/ktb in v1-3)
  F3: muqaṭṭāʿat-opened (29 canonical)
  F4: oath-opener (22 classical list)
  F5: mufaṣṣal-start position (Q 49-60)

Test: Q 50 rank in composite score ≤ 3 AND p_perm < 0.05.
MW-5: shuffle each feature vector independently; Q 50 rank distribution.
Seed 20260417. 10K permutations.
"""
import hashlib, json, random, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERMS = 10000

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-154-q50-composite-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-154.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Feature F1: position centrality (Q 40-60)
# ---------------------------------------------------------------------------
F1 = {s: 1 if 40 <= s <= 60 else 0 for s in range(1, 115)}

# ---------------------------------------------------------------------------
# 2. Feature F2: book-reflexive opening (qrA/ktb in v1-3)
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')
verse_roots = defaultdict(lambda: defaultdict(set))
with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        p = line.rstrip().split('\t')
        if len(p) < 4: continue
        m = LOC_RE.match(p[0])
        if not m: continue
        sid, vid = int(m.group(1)), int(m.group(2))
        if 'STEM' not in p[3]: continue
        rm = ROOT_RE.search(p[3])
        if not rm: continue
        verse_roots[sid][vid].add(rm.group(1))

F2 = {}
for s in range(1, 115):
    any_book = any(
        ('qrA' in verse_roots[s].get(v, set())) or ('ktb' in verse_roots[s].get(v, set()))
        for v in [1, 2, 3] if v in verse_roots[s]
    )
    F2[s] = 1 if any_book else 0

# ---------------------------------------------------------------------------
# 3. Feature F3: muqaṭṭāʿat-opened
# ---------------------------------------------------------------------------
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
              31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
F3 = {s: 1 if s in MUQ_SURAHS else 0 for s in range(1, 115)}

# ---------------------------------------------------------------------------
# 4. Feature F4: oath-opener (22 classical list, locked in pre-reg)
# ---------------------------------------------------------------------------
OATH_OPENERS = {36, 37, 43, 44, 50, 51, 52, 53, 68, 75, 77, 79, 85, 86, 89, 90,
                91, 92, 93, 95, 100, 103}
F4 = {s: 1 if s in OATH_OPENERS else 0 for s in range(1, 115)}

# ---------------------------------------------------------------------------
# 5. Feature F5: mufaṣṣal-start position (Q 49-60)
# ---------------------------------------------------------------------------
F5 = {s: 1 if 49 <= s <= 60 else 0 for s in range(1, 115)}

# ---------------------------------------------------------------------------
# 6. Composite score
# ---------------------------------------------------------------------------
def composite(F1, F2, F3, F4, F5):
    return {s: F1[s] + F2[s] + F3[s] + F4[s] + F5[s] for s in range(1, 115)}

scores = composite(F1, F2, F3, F4, F5)
sorted_scores = sorted(scores.items(), key=lambda x: -x[1])

print("\nComposite score distribution:", file=sys.stderr)
from collections import Counter
score_dist = Counter(scores.values())
for sc, cnt in sorted(score_dist.items(), reverse=True):
    print(f"  score={sc}: {cnt} surahs", file=sys.stderr)

# Rank Q 50
q50_score = scores[50]
print(f"\nQ 50 composite score: {q50_score}/5", file=sys.stderr)
print(f"  F1 (position Q40-60): {F1[50]}", file=sys.stderr)
print(f"  F2 (book-ref v1-3):   {F2[50]}", file=sys.stderr)
print(f"  F3 (muq-opened):      {F3[50]}", file=sys.stderr)
print(f"  F4 (oath-opener):     {F4[50]}", file=sys.stderr)
print(f"  F5 (mufaṣṣal-start):  {F5[50]}", file=sys.stderr)

# Tied rank: how many surahs have ≥ q50_score?
n_at_or_above = sum(1 for _, sc in sorted_scores if sc >= q50_score)
q50_rank_bottom = n_at_or_above  # bottom of tied rank
# top of tied rank:
n_strictly_above = sum(1 for _, sc in sorted_scores if sc > q50_score)
q50_rank_top = n_strictly_above + 1
print(f"  Q 50 rank: {q50_rank_top}-{q50_rank_bottom} (ties)", file=sys.stderr)

# Top-10 showcase
print(f"\nTop-10 by composite score:", file=sys.stderr)
for s, sc in sorted_scores[:15]:
    print(f"  Q {s}: score={sc} (F1={F1[s]} F2={F2[s]} F3={F3[s]} F4={F4[s]} F5={F5[s]})", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. MW-5 shuffle-null
# ---------------------------------------------------------------------------
rng = random.Random(SEED)
def shuffle_feature(F):
    surahs = list(F.keys())
    values = list(F.values())
    rng.shuffle(values)
    return {surahs[i]: values[i] for i in range(len(surahs))}

null_ranks = []
for _ in range(N_PERMS):
    sh1 = shuffle_feature(F1)
    sh2 = shuffle_feature(F2)
    sh3 = shuffle_feature(F3)
    sh4 = shuffle_feature(F4)
    sh5 = shuffle_feature(F5)
    sh_scores = composite(sh1, sh2, sh3, sh4, sh5)
    # rank of Q 50
    q50_sh = sh_scores[50]
    null_ranks.append(sum(1 for s in sh_scores if sh_scores[s] >= q50_sh))

# p_perm: fraction of shuffles with Q 50 rank ≤ observed (lower rank = better)
p_perm = sum(1 for r in null_ranks if r <= q50_rank_bottom) / N_PERMS

# Verdict
if q50_rank_top == 1 and p_perm < 0.05:
    verdict = "COMPOSITE-CONFIRMED — Q 50 is strict top-1 hub by composite"
elif q50_rank_bottom <= 3 and p_perm < 0.05:
    verdict = "COMPOSITE-TOP — Q 50 shares top-3 with other composite-hubs"
elif q50_rank_bottom <= 10 and p_perm < 0.05:
    verdict = "COMPOSITE-HIGH — in top-10 but not top-3; H-NEW-146 NULL verdict stands"
else:
    verdict = "NULL — composite test fails to distinguish Q 50 from baseline"

print(f"\n" + "=" * 70, file=sys.stderr)
print(f"Q 50 composite score: {q50_score}/5", file=sys.stderr)
print(f"Q 50 rank: {q50_rank_top}-{q50_rank_bottom}", file=sys.stderr)
print(f"p_perm (≤ observed rank): {p_perm:.4f}", file=sys.stderr)
print(f"VERDICT: {verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

summary = {
    'finding_id': 'h-new-154',
    'title': 'Q 50 composite hub-mechanism score',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 1, 'alpha_bon': 0.05, 'family': 'h-new-154-q50-composite'},
    'features': {
        'F1_position_40_60': F1,
        'F2_book_ref_v1_3': F2,
        'F3_muq_opened': F3,
        'F4_oath_opener': F4,
        'F5_mufassal_start_49_60': F5,
    },
    'composite_scores': scores,
    'q50_score': q50_score,
    'q50_feature_values': {'F1': F1[50], 'F2': F2[50], 'F3': F3[50], 'F4': F4[50], 'F5': F5[50]},
    'q50_rank_top_of_tie': q50_rank_top,
    'q50_rank_bottom_of_tie': q50_rank_bottom,
    'score_distribution': dict(sorted(score_dist.items())),
    'top_15_by_score': [(s, sc, {'F1':F1[s],'F2':F2[s],'F3':F3[s],'F4':F4[s],'F5':F5[s]}) for s, sc in sorted_scores[:15]],
    'mw5_null_rank_mean': sum(null_ranks)/len(null_ranks),
    'p_permutation': p_perm,
    'n_perms': N_PERMS,
    'verdict': verdict,
}
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
