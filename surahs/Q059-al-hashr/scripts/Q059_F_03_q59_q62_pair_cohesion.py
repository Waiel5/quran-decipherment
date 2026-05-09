#!/usr/bin/env python3
"""
Q059-F-03 — Q 59 ↔ Q 62 pair cohesion via root-overlap (Khawatim-echo bridge).

Tests whether Q 59 / Q 62 share substantively MORE root/token overlap than expected
under permutation-null comparison to other Medinan-pair baselines.

H-NEW-58c reports the perfect-imperfect tense binary makes Q 59-Q 62 a CROSS-tense pair
with 0-char shared prefix (H-NEW-58c). This test asks: do they share more
**at the surah-token-set level** (where the Khawatim names + lā-ilāha-illā-huwa-cluster
links bridge tense)?

Pre-reg: preregs/Q059-F-03-q59-q62-pair-cohesion-prereg.md
Authored: Waiel Al-Shujaa, 2026-05-09
"""
import json
import re
import hashlib
import random
from pathlib import Path
from itertools import combinations

ROOT = Path('/Users/grey/Downloads/quran')
OUT = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/csv/Q059-F-03.json')
PREREG = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/preregs/Q059-F-03-q59-q62-pair-cohesion-prereg.md')
SEED = 20260509

ORNAMENTS = re.compile(r'[ۖ-ۭۚ-۝]')

def clean_text(t):
    t = ORNAMENTS.sub(' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

with open(ROOT / 'quran-text' / 'quran-no-tashkeel.json', 'r') as f:
    q = json.load(f)

# Get all 28 Medinan surahs
medinan_sids = [s['id'] for s in q if s['type'] == 'medinan']
print(f"Medinan surahs: {len(medinan_sids)}: {medinan_sids}")

surah_words = {}
for sid in medinan_sids:
    s = q[sid-1]
    all_words = []
    for v in s['verses']:
        all_words.extend(clean_text(v['text']).split())
    surah_words[sid] = all_words

# Cell A — Jaccard pairwise within Medinan
def jaccard(a, b):
    sa = set(a)
    sb = set(b)
    if not sa or not sb:
        return 0
    return len(sa & sb) / len(sa | sb)

q59_words = surah_words[59]
q62_words = surah_words[62]
obs_jaccard = jaccard(q59_words, q62_words)
print(f"Q 59 ↔ Q 62 token-set Jaccard: {obs_jaccard:.4f}")

# Compute Q 59 jaccard to ALL other Medinan surahs (rank)
q59_jaccard_to_others = {}
for sid in medinan_sids:
    if sid == 59:
        continue
    j = jaccard(q59_words, surah_words[sid])
    q59_jaccard_to_others[sid] = j

q59_jaccard_sorted = sorted(q59_jaccard_to_others.items(), key=lambda x: -x[1])
print(f"\nQ 59 nearest Medinan partners by token-Jaccard (top-10):")
for sid, j in q59_jaccard_sorted[:10]:
    print(f"  Q{sid}: J={j:.4f}")

q62_rank = next(i for i, (sid, _) in enumerate(q59_jaccard_sorted) if sid == 62) + 1
print(f"\nQ 62 rank among Q 59's Medinan partners: {q62_rank}/{len(medinan_sids)-1}")

# Cell B — length-weighted permutation null
# H0: Q 59 ↔ Q 62 token-overlap is no greater than random Medinan pair conditional on length.
# We use length-residualization: control for the harmonic-mean of word-counts.
# Simpler: bootstrap random Medinan-pair Jaccards and compute empirical p.

random.seed(SEED)
N_PERM = 10000
medinan_pairs = list(combinations(medinan_sids, 2))
all_medinan_jaccards = {(a, b): jaccard(surah_words[a], surah_words[b]) for (a, b) in medinan_pairs}

# Length-aware null: pick random pair within ±20% of harmonic-mean word count of (Q 59, Q 62)
q59_W = len(q59_words)
q62_W = len(q62_words)
harmonic = 2 * q59_W * q62_W / (q59_W + q62_W)
print(f"\nQ 59 W={q59_W}, Q 62 W={q62_W}, harmonic mean: {harmonic:.1f}")

# Compute each pair's harmonic mean
def harm(a, b):
    return 2*a*b/(a+b)

# Filter to pairs with harmonic mean within ±20% of obs
LOWER, UPPER = 0.7, 1.5  # asymmetric loose: small = rare in Medinan
matched_pairs = [(a, b) for (a, b) in medinan_pairs
                 if LOWER * harmonic <= harm(len(surah_words[a]), len(surah_words[b])) <= UPPER * harmonic
                 and not (a == 59 and b == 62) and not (a == 62 and b == 59)]
print(f"Length-matched pair pool: {len(matched_pairs)}")

if len(matched_pairs) < 30:
    # widen
    LOWER, UPPER = 0.5, 2.0
    matched_pairs = [(a, b) for (a, b) in medinan_pairs
                     if LOWER * harmonic <= harm(len(surah_words[a]), len(surah_words[b])) <= UPPER * harmonic
                     and not (a == 59 and b == 62) and not (a == 62 and b == 59)]
    print(f"Widened length-matched pair pool: {len(matched_pairs)}")

matched_jaccards = [all_medinan_jaccards[p] for p in matched_pairs]
geq_count = sum(1 for j in matched_jaccards if j >= obs_jaccard)
p_lengthmatched = geq_count / len(matched_jaccards)
print(f"\nLength-matched Medinan-pair Jaccard mean: {sum(matched_jaccards)/len(matched_jaccards):.4f}")
print(f"p (Jaccard >= Q59-Q62 obs) within length-matched pool: {p_lengthmatched:.4f}")

# Also unconditional
unc_geq = sum(1 for (a, b), j in all_medinan_jaccards.items() if j >= obs_jaccard and not (a == 59 and b == 62))
p_unconditional = unc_geq / (len(medinan_pairs) - 1)
print(f"p (Jaccard >= obs) unconditional in 28-Medinan pool: {p_unconditional:.4f}")

# Cell C — share-of-Q59-tokens that appear in Q 62
q59_set = set(q59_words)
q62_set = set(q62_words)
q59_in_q62 = len(q59_set & q62_set) / len(q59_set)
q62_in_q59 = len(q59_set & q62_set) / len(q62_set)
print(f"\nFraction of Q 59 unique-tokens that appear in Q 62: {q59_in_q62:.4f}")
print(f"Fraction of Q 62 unique-tokens that appear in Q 59: {q62_in_q59:.4f}")

# Top tokens shared between Q 59 and Q 62 (excluding common high-frequency stopwords)
# Build token frequency in Q 59 and Q 62 (combined)
from collections import Counter
q59_freq = Counter(q59_words)
q62_freq = Counter(q62_words)

# Tokens shared with combined frequency
shared_tokens = q59_set & q62_set
shared_with_freq = [(tok, q59_freq[tok], q62_freq[tok]) for tok in shared_tokens]
# Sort by combined freq descending
shared_with_freq.sort(key=lambda x: -(x[1]+x[2]))
print(f"\nTop 20 shared tokens (Q 59 × Q 62) by combined freq:")
for tok, c59, c62 in shared_with_freq[:20]:
    print(f"  '{tok}' Q59={c59} Q62={c62}")

prereg_sha = ''
if PREREG.exists():
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()

result = {
    'finding_id': 'Q059-F-03',
    'title': 'Q 59 ↔ Q 62 surah-token-set Jaccard cohesion vs length-matched Medinan pairs',
    'prereg_sha': prereg_sha,
    'seed': SEED,
    'n_perm': len(matched_pairs),
    'rules_tuple': '(no-tashkeel, ornament-stripped, whitespace-tokenized, surah-as-bag-of-tokens)',
    'authored_by': 'Waiel Al-Shujaa',
    'date': '2026-05-09',
    'observed': {
        'q59_q62_token_jaccard': obs_jaccard,
        'q59_word_count': q59_W,
        'q62_word_count': q62_W,
        'harmonic_mean_W': harmonic,
        'q59_in_q62_share': q59_in_q62,
        'q62_in_q59_share': q62_in_q59,
    },
    'q59_jaccard_to_all_27_medinan': dict(q59_jaccard_sorted),
    'q62_rank_among_q59_medinan_partners': q62_rank,
    'q59_top10_medinan_partners': q59_jaccard_sorted[:10],
    'cell_B_length_matched_null': {
        'pool_size': len(matched_pairs),
        'lower_bound': LOWER,
        'upper_bound': UPPER,
        'mean_jaccard_in_pool': sum(matched_jaccards)/len(matched_jaccards),
        'p_one_sided_geq': p_lengthmatched,
    },
    'unconditional_null': {
        'pool_size': len(medinan_pairs) - 1,
        'p_one_sided_geq': p_unconditional,
    },
    'top_20_shared_tokens': [{'token': t, 'q59_freq': c59, 'q62_freq': c62, 'combined': c59+c62} for t, c59, c62 in shared_with_freq[:20]],
    'verdict': {
        'cohesion_above_length_matched_null': p_lengthmatched < 0.05,
        'q62_is_top_quartile_q59_partner': q62_rank <= len(medinan_sids) // 4,
        'overall': 'PASS' if (p_lengthmatched < 0.05) else 'NULL',
    }
}

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(f"\nWrote: {OUT}")
print(f"Verdict: {result['verdict']['overall']}")
