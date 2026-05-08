#!/usr/bin/env python3
"""Q024-F-02: Light-verse vs Throne-verse empirical comparison."""
import json, re, hashlib, os
from collections import Counter

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-02-aya-al-nur-vs-aya-al-kursi-prereg.md"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-02.json"

LIGHT = {'nwr', 'SbH', 'wqd', 'srj', 'qbs', 'shhb', 'mskw', 'zjj',
         'kwkb', '$jr', 'zyt', 'brk', '$kw', 'drr', 'DwA', 'mvl'}
ATTRIBUTES = {'Hyy', 'qwm', 'Elw', 'EZm', 'Hkm', 'Elm', 'rHm', 'qdr', 'gfr',
              'qhr', 'flq', 'wHd', 'Ezz'}  # divine-attribute roots

sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()

# Parse QAC for verses 24:35 and 2:255
v_data = {}
with open(f'{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('('): continue
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)\s+(\S+)\s+(\S+)\s+(.*)', line)
        if not m: continue
        s, v = int(m.group(1)), int(m.group(2))
        if (s, v) not in [(24, 35), (2, 255)]: continue
        feat = m.group(7)
        rm = re.search(r'ROOT:([^|\s]+)', feat)
        d = v_data.setdefault((s, v), {'tokens': 0, 'roots': Counter()})
        d['tokens'] += 1
        if rm:
            d['roots'][rm.group(1)] += 1


def strip(t):
    return re.sub(r'[ؐ-ًؚ-ٰٟۖ-ۜ۟-۪ۨ-ۭ۝۩ۮۯ؜ـ۞۠ۗ]', '', t).strip()


# Get word/letter counts and surah positions
data = json.load(open(f'{PROJECT}/quran-text/quran-no-tashkeel.json'))


def verse_word_count(s, v):
    surah = data[s - 1]
    text = strip(surah['verses'][v - 1]['text'])
    return len(text.split())


def verse_letter_count(s, v):
    surah = data[s - 1]
    text = strip(surah['verses'][v - 1]['text'])
    return sum(1 for c in text if c != ' ')


def midpoint_position_ratio(s, v_target):
    """Return (mid_word_position_in_surah, total_words). Mid-position = midpoint
    word of v_target in surah's running word index."""
    surah = data[s - 1]
    cum = 0
    for v in surah['verses']:
        n = len(strip(v['text']).split())
        if v['id'] == v_target:
            return (cum + n / 2) / sum(len(strip(vv['text']).split()) for vv in surah['verses'])
        cum += n
    return None


# Compute
metrics = {}
for label, (s, v) in [('aya_al_nur', (24, 35)), ('aya_al_kursi', (2, 255))]:
    d = v_data[(s, v)]
    light_count = sum(d['roots'].get(r, 0) for r in LIGHT)
    attr_count = sum(d['roots'].get(r, 0) for r in ATTRIBUTES)
    allah_count = d['roots'].get('Alh', 0)
    word_count = verse_word_count(s, v)
    letter_count = verse_letter_count(s, v)
    midpos = midpoint_position_ratio(s, v)
    metrics[label] = {
        'verse': f'Q{s}:{v}',
        'words_no_tashkeel': word_count,
        'letters_no_tashkeel': letter_count,
        'qac_tokens': d['tokens'],
        'qac_distinct_roots': len(d['roots']),
        'light_cluster_count': light_count,
        'divine_attribute_count': attr_count,
        'allah_count': allah_count,
        'allah_density': allah_count / word_count,
        'midpoint_position_ratio_in_surah': midpos,
    }
    print(f"\n=== {label} ({metrics[label]['verse']}) ===")
    for k, val in metrics[label].items():
        print(f"  {k}: {val}")

# Direction A: light count Q24:35 > Q2:255 (≥7 vs ≤2)
direction_A = (metrics['aya_al_nur']['light_cluster_count'] >= 7
               and metrics['aya_al_kursi']['light_cluster_count'] <= 2)
# Direction B: Q24:35 in [0.33, 0.67]; Q2:255 outside
direction_B = (0.33 <= metrics['aya_al_nur']['midpoint_position_ratio_in_surah'] <= 0.67
               and not (0.33 <= metrics['aya_al_kursi']['midpoint_position_ratio_in_surah'] <= 0.67))

# Lexical overlap
roots_v35 = set(v_data[(24, 35)]['roots'])
roots_v255 = set(v_data[(2, 255)]['roots'])
shared = sorted(roots_v35 & roots_v255)
v35_only = sorted(roots_v35 - roots_v255)
v255_only = sorted(roots_v255 - roots_v35)

result = {
    'finding_id': 'Q024-F-02',
    'pre_reg_sha256': sha,
    'metrics': metrics,
    'direction_A_pass': direction_A,
    'direction_B_pass': direction_B,
    'shared_roots': shared,
    'v35_only_roots': v35_only,
    'v255_only_roots': v255_only,
    'verdict': 'CONFIRMED' if (direction_A and direction_B) else 'DIRECTIONAL' if (direction_A or direction_B) else 'NULL'
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, default=str, ensure_ascii=False)

print(f"\nDirection A pass: {direction_A}")
print(f"Direction B pass: {direction_B}")
print(f"Verdict: {result['verdict']}")
print(f"\nFull output written to {OUT}")
