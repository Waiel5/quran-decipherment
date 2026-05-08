#!/usr/bin/env python3
"""Q024-F-03: al-ifk cohesion + Q 24:35 structural midpoint."""
import json, re, hashlib, os, random, bisect
from collections import Counter

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-03-ifk-cohesion-and-midpoint-prereg.md"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-03.json"

sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()

# Parse QAC roots per verse
verses_roots = {}
with open(f'{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('('): continue
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)\s+\S+\s+\S+\s+(.*)', line)
        if not m: continue
        s, v = int(m.group(1)), int(m.group(2))
        rm = re.search(r'ROOT:([^|\s]+)', m.group(5))
        if rm:
            verses_roots.setdefault((s, v), Counter())[rm.group(1)] += 1


def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa or not sb: return 0.0
    return len(sa & sb) / len(sa | sb)


def passage_cohesion(scope):
    keys = sorted(scope)
    if len(keys) < 2: return None
    sims = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            r1 = verses_roots.get(keys[i], {})
            r2 = verses_roots.get(keys[j], {})
            sims.append(jaccard(r1, r2))
    return sum(sims) / len(sims), len(sims)


# Hypothesis A: al-ifk Q24:11-20
ifk_scope = [(24, v) for v in range(11, 21)]
ifk_coh, n_pairs = passage_cohesion(ifk_scope)

# Random control
rng = random.Random(2024)
all_keys = sorted(verses_roots.keys())
control_cohs = []
for _ in range(2000):
    base = rng.choice(all_keys)
    s, v = base
    span_len = rng.randint(5, 10)
    same_surah = [k for k in all_keys if k[0] == s and v <= k[1] < v + span_len]
    if len(same_surah) >= 5:
        c, _ = passage_cohesion(same_surah[:span_len])
        control_cohs.append(c)

control_cohs.sort()
ifk_pct = bisect.bisect_left(control_cohs, ifk_coh) / len(control_cohs) * 100

# Hypothesis B: Q 24:35 structural midpoint
data = json.load(open(f'{PROJECT}/quran-text/quran-no-tashkeel.json'))
q24 = data[23]


def strip(t):
    # Strip mushaf marks and tashkeel only (avoid stripping the actual Arabic letters)
    # ۞ ۚ ۖ ۗ ۙ ۛ ۠ are sajda/recitation marks; tashkeel range ً-ٟ + ٰ; tatweel ـ
    return re.sub(r'[ً-ٰٟـۖ-ۭ۞۟]', '', t).strip()


cum_words = 0
word_boundaries = {}
for v in q24['verses']:
    n = len(strip(v['text']).split())
    word_boundaries[v['id']] = (cum_words, cum_words + n)
    cum_words += n
total_words = cum_words

cum_letters = 0
letter_boundaries = {}
for v in q24['verses']:
    s = strip(v['text']).replace(' ', '')
    n = len(s)
    letter_boundaries[v['id']] = (cum_letters, cum_letters + n)
    cum_letters += n
total_letters = cum_letters

# Word-median: index total_words // 2 (0-based: which verse contains word at index total_words/2)
word_median_idx = total_words / 2.0
v35_word_span = word_boundaries[35]
word_in_v35 = v35_word_span[0] <= word_median_idx < v35_word_span[1]

letter_median_idx = total_letters / 2.0
v35_letter_span = letter_boundaries[35]
letter_in_v35 = v35_letter_span[0] <= letter_median_idx < v35_letter_span[1]

# Verdicts
if ifk_pct >= 80:
    verdict_A = 'CONFIRMED'
elif ifk_pct >= 50:
    verdict_A = 'DIRECTIONAL'
else:
    verdict_A = 'NULL'

if word_in_v35 and letter_in_v35:
    verdict_B = 'CONFIRMED'
elif word_in_v35 or letter_in_v35:
    verdict_B = 'DIRECTIONAL'
else:
    verdict_B = 'NULL'

result = {
    'finding_id': 'Q024-F-03',
    'pre_reg_sha256': sha,
    'hypothesis_A': {
        'al_ifk_passage': 'Q24:11-20',
        'al_ifk_cohesion': ifk_coh,
        'n_pairs': n_pairs,
        'control_n_samples': len(control_cohs),
        'control_mean': sum(control_cohs) / len(control_cohs),
        'control_median': control_cohs[len(control_cohs) // 2],
        'al_ifk_percentile': ifk_pct,
        'verdict': verdict_A,
    },
    'hypothesis_B': {
        'q24_total_words': total_words,
        'q24_total_letters': total_letters,
        'word_median_idx': word_median_idx,
        'letter_median_idx': letter_median_idx,
        'q24_35_word_span': v35_word_span,
        'q24_35_letter_span': v35_letter_span,
        'q24_35_contains_word_median': word_in_v35,
        'q24_35_contains_letter_median': letter_in_v35,
        'verdict': verdict_B,
    },
    'overall_verdict': verdict_A if verdict_A == verdict_B else f'A:{verdict_A}/B:{verdict_B}',
}

# Also include other passage cohesions as descriptive
for label, scope in [('zina_qadhf_1_10', [(24, v) for v in range(1, 11)]),
                      ('home_entry_hijab_27_31', [(24, v) for v in range(27, 32)]),
                      ('light_cluster_34_40', [(24, v) for v in range(34, 41)]),
                      ('hypocrites_47_57', [(24, v) for v in range(47, 58)])]:
    c, n = passage_cohesion(scope)
    pct = bisect.bisect_left(control_cohs, c) / len(control_cohs) * 100
    result.setdefault('descriptive_passages', {})[label] = {
        'cohesion': c, 'n_pairs': n, 'percentile': pct
    }

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, default=str, ensure_ascii=False)

print(json.dumps(result, indent=2, default=str))
print(f"\nWritten to {OUT}")
