#!/usr/bin/env python3
"""
Q059-F-05 — Q 59:22-24 within-surah uniqueness test.

Of the 22 internal 3-verse windows within Q 59 (v1-3 ... v22-24), how dominant is
v22-24 by 99-name token count? Within-surah-permutation null.

Pre-reg: preregs/Q059-F-05-within-surah-uniqueness-prereg.md
Authored: Waiel Al-Shujaa, 2026-05-09
"""
import json
import re
import hashlib
import random
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
OUT = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/csv/Q059-F-05.json')
PREREG = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/preregs/Q059-F-05-within-surah-uniqueness-prereg.md')
SEED = 20260509

ORNAMENTS = re.compile(r'[ۖ-ۭۚ-۝]')
def clean_text(t):
    t = ORNAMENTS.sub(' ', t)
    return re.sub(r'\s+', ' ', t).strip()

names = []
with open(ROOT / 'data' / 'asma-al-husna.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            names.append(line)

with open(ROOT / 'quran-text' / 'quran-no-tashkeel.json', 'r') as f:
    q = json.load(f)

PROCLITICS = ['', 'و', 'ف', 'ل', 'ب', 'ك', 'فل', 'ول', 'وب', 'فب', 'فال', 'وال', 'ولل', 'فلل', 'بال', 'كال']

def count_names(words, name_set):
    cnt = 0
    matched = []
    for w in words:
        for n in name_set:
            for p in PROCLITICS:
                if w == p + n:
                    cnt += 1
                    matched.append(n)
                    break
            else:
                continue
            break
    return cnt, matched

# Q 59
q59 = q[58]
verse_data = []
for v in q59['verses']:
    txt = clean_text(v['text'])
    words = txt.split()
    c, _ = count_names(words, names)
    verse_data.append({'vid': v['id'], 'words': words, 'n_words': len(words), 'count': c})

# 22 internal windows
windows = []
for i in range(len(verse_data) - 2):
    F = sum(verse_data[i+k]['count'] for k in range(3))
    W = sum(verse_data[i+k]['n_words'] for k in range(3))
    windows.append({
        'start_vid': verse_data[i]['vid'],
        'end_vid': verse_data[i+2]['vid'],
        'F': F,
        'words': W,
        'density': F/W if W else 0,
    })

# Sort and rank
windows_sorted = sorted(windows, key=lambda w: -w['F'])
print("=== All 22 internal 3-verse windows in Q 59 by F (99-name count) ===")
for w in windows_sorted:
    print(f"  v{w['start_vid']}-v{w['end_vid']}: F={w['F']} W={w['words']} dens={w['density']:.4f}")

# v22-24 rank
v22_24 = next(w for w in windows if w['start_vid'] == 22)
v22_24_rank_F = next(i for i, w in enumerate(windows_sorted) if w['start_vid'] == 22) + 1
print(f"\nQ 59:22-24 F-rank: {v22_24_rank_F}/{len(windows)}")

# Within-surah permutation: shuffle name-counts across the 24 verses, recompute max-window F
random.seed(SEED)
N_PERM = 10000
counts = [vd['count'] for vd in verse_data]
n_words_arr = [vd['n_words'] for vd in verse_data]
total_q59 = sum(counts)
print(f"\nTotal 99-name tokens in Q 59: {total_q59}")

null_max_F = []
null_max_density = []
for _ in range(N_PERM):
    # word-count-weighted permutation: redistribute total_q59 tokens across verses with prob ~ word-count
    null_counts = [0] * len(verse_data)
    weights_q59 = [w/sum(n_words_arr) for w in n_words_arr]
    cum = []
    running = 0
    for w in weights_q59:
        running += w
        cum.append(running)
    import bisect
    for _t in range(total_q59):
        r = random.random()
        idx = bisect.bisect_left(cum, r)
        null_counts[idx] += 1
    mx_F = 0
    mx_d = 0
    for i in range(len(verse_data) - 2):
        Fn = null_counts[i] + null_counts[i+1] + null_counts[i+2]
        Wn = n_words_arr[i] + n_words_arr[i+1] + n_words_arr[i+2]
        if Fn > mx_F:
            mx_F = Fn
        if Wn > 0:
            d = Fn / Wn
            if d > mx_d:
                mx_d = d
    null_max_F.append(mx_F)
    null_max_density.append(mx_d)

obs_F = v22_24['F']
obs_d = v22_24['density']
p_F = sum(1 for x in null_max_F if x >= obs_F) / N_PERM
p_d = sum(1 for x in null_max_density if x >= obs_d) / N_PERM

print(f"\nWithin-surah permutation null (N={N_PERM}, seed={SEED}):")
print(f"  null_max_F mean: {sum(null_max_F)/N_PERM:.2f}, max: {max(null_max_F)}")
print(f"  null_max_density mean: {sum(null_max_density)/N_PERM:.4f}, max: {max(null_max_density):.4f}")
print(f"  p (max_F >= {obs_F}): {p_F:.4f}")
print(f"  p (max_density >= {obs_d:.4f}): {p_d:.4f}")

prereg_sha = ''
if PREREG.exists():
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()

result = {
    'finding_id': 'Q059-F-05',
    'title': 'Q 59:22-24 within-surah window uniqueness',
    'prereg_sha': prereg_sha,
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': '(no-tashkeel, ornament-stripped, whitespace-tokenized, 99-name-substring-with-proclitic-tolerance, word-count-weighted-within-surah-permutation)',
    'authored_by': 'Waiel Al-Shujaa',
    'date': '2026-05-09',
    'observed_v22_24': {
        'F99': obs_F,
        'words': v22_24['words'],
        'density': obs_d,
        'rank_among_22_internal_windows_by_F': v22_24_rank_F,
    },
    'all_22_windows_sorted_by_F': windows_sorted,
    'q59_total_99name_tokens': total_q59,
    'null_summary': {
        'null_max_F_mean': sum(null_max_F)/N_PERM,
        'null_max_F_max': max(null_max_F),
        'null_max_density_mean': sum(null_max_density)/N_PERM,
        'null_max_density_max': max(null_max_density),
    },
    'p_one_sided': {
        'F_geq_obs': p_F,
        'density_geq_obs': p_d,
    },
    'verdict': {
        'within_surah_uniqueness_F': 'PASS' if p_F < 0.01 else ('PASS-DIRECTED' if p_F < 0.05 else 'NULL'),
        'within_surah_uniqueness_density': 'PASS' if p_d < 0.01 else ('PASS-DIRECTED' if p_d < 0.05 else 'NULL'),
    }
}

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(f"\nWrote: {OUT}")
