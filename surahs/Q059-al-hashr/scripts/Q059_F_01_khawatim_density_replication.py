#!/usr/bin/env python3
"""
Q059-F-01 — Replicate H-NEW-95 Cell E within Q 59 specialist context.

Test: Q 59:22-24 per-token divine-name density vs all 6,234 corpus 3-verse windows.

Q 59:22-24 should be the corpus RANK-1 3-verse window by total 99-name token count
(replicating H-NEW-95's F=19 result), AND additionally tested under per-token-DENSITY
(F / total_words_in_window) — which the H-NEW-95 used absolute count.

Pre-reg: preregs/Q059-F-01-khawatim-density-replication-prereg.md
Authored: Waiel Al-Shujaa, 2026-05-09
"""

import json
import os
import re
import hashlib
import random
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
OUT = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/csv/Q059-F-01.json')
PREREG = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/preregs/Q059-F-01-khawatim-density-replication-prereg.md')
SEED = 20260509

ORNAMENTS = re.compile(r'[ۖ-ۭۚ-۝]')

def clean_text(t):
    t = ORNAMENTS.sub(' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

# Load 99 names
names = []
with open(ROOT / 'data' / 'asma-al-husna.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            names.append(line)
assert len(names) == 99, f"Expected 99 names, got {len(names)}"

# Load corpus
with open(ROOT / 'quran-text' / 'quran-no-tashkeel.json', 'r', encoding='utf-8') as f:
    q = json.load(f)

# Build a flat list of (sid, vid, words_list, text) per verse
flat = []
for s in q:
    for v in s['verses']:
        txt = clean_text(v['text'])
        words = txt.split()
        flat.append({'sid': s['id'], 'vid': v['id'], 'words': words, 'text': txt})

assert len(flat) == 6236, f"Expected 6236 verses, got {len(flat)}"

# Precompute per-verse name-token-count under H-NEW-95 substring rule
# Match: word equals NAME exactly, or word equals (proclitic-prefix + NAME)
# Proclitics: ف و ل ب ك (al-Faraq prefixes)
PROCLITICS = ['', 'و', 'ف', 'ل', 'ب', 'ك', 'فل', 'ول', 'وب', 'فب', 'فال', 'وال', 'ولل', 'فلل', 'بال', 'كال']

def count_names_in_words(words, name_set):
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

# H-NEW-95 strict 9-name Khawatim inventory
KHAWATIM_9 = ['القدوس', 'السلام', 'المؤمن', 'المهيمن', 'الجبار', 'المتكبر', 'الخالق', 'البارئ', 'المصور']

# H-NEW-95 broader 14-name inventory (all names in Q 59:22-24)
KHAWATIM_14 = ['الرحمن', 'الرحيم', 'الملك', 'القدوس', 'السلام', 'المؤمن', 'المهيمن',
                'العزيز', 'الجبار', 'المتكبر', 'الخالق', 'البارئ', 'المصور', 'الحكيم']

# Per-verse counts under each inventory + 99-name
per_verse_count_99 = []
per_verse_count_14 = []
per_verse_count_9 = []
per_verse_words = []
for fv in flat:
    c99, _ = count_names_in_words(fv['words'], names)
    c14, _ = count_names_in_words(fv['words'], KHAWATIM_14)
    c9, _ = count_names_in_words(fv['words'], KHAWATIM_9)
    per_verse_count_99.append(c99)
    per_verse_count_14.append(c14)
    per_verse_count_9.append(c9)
    per_verse_words.append(len(fv['words']))

# Sanity: Q 59:23 should have many names
i_59_23 = next(i for i, fv in enumerate(flat) if fv['sid']==59 and fv['vid']==23)
i_59_24 = next(i for i, fv in enumerate(flat) if fv['sid']==59 and fv['vid']==24)
i_59_22 = next(i for i, fv in enumerate(flat) if fv['sid']==59 and fv['vid']==22)

print(f"Q 59:22 99-name count: {per_verse_count_99[i_59_22]}, 14-inv: {per_verse_count_14[i_59_22]}")
print(f"Q 59:23 99-name count: {per_verse_count_99[i_59_23]}, 14-inv: {per_verse_count_14[i_59_23]}")
print(f"Q 59:24 99-name count: {per_verse_count_99[i_59_24]}, 14-inv: {per_verse_count_14[i_59_24]}")

# 3-verse sliding windows: build (start_idx, end_idx, F_99, F_density)
# Constraint: stay within mushaf order (overlap surah boundaries OK per H-NEW-95)
windows = []
for start in range(len(flat) - 2):
    end = start + 2
    F99 = per_verse_count_99[start] + per_verse_count_99[start+1] + per_verse_count_99[start+2]
    W = per_verse_words[start] + per_verse_words[start+1] + per_verse_words[start+2]
    density = F99 / W if W > 0 else 0
    windows.append({
        'start_sid': flat[start]['sid'],
        'start_vid': flat[start]['vid'],
        'end_sid': flat[end]['sid'],
        'end_vid': flat[end]['vid'],
        'F99': F99,
        'words': W,
        'density': density,
    })

assert len(windows) == 6234, f"Expected 6234 windows, got {len(windows)}"

# Identify Q 59:22-24 window
q59_window = next(w for w in windows if w['start_sid']==59 and w['start_vid']==22)
print(f"\nQ 59:22-24: F99={q59_window['F99']}, words={q59_window['words']}, density={q59_window['density']:.4f}")

# Cell A: rank by F99 (absolute count) - replication of H-NEW-95 Cell E
windows_by_F = sorted(windows, key=lambda w: -w['F99'])
rank_F_q59 = next(i for i, w in enumerate(windows_by_F) if w['start_sid']==59 and w['start_vid']==22) + 1
print(f"Rank by F99 absolute: {rank_F_q59}/6234")

# Cell B: rank by per-token density (NEW axis under Q 59 specialist context)
# Restrict to windows with W >= 10 to avoid trivially-small denominators
DENSITY_MIN_WORDS = 10
windows_dense = [w for w in windows if w['words'] >= DENSITY_MIN_WORDS]
windows_by_density = sorted(windows_dense, key=lambda w: -w['density'])
rank_dens_q59 = next((i for i, w in enumerate(windows_by_density) if w['start_sid']==59 and w['start_vid']==22), -1) + 1
print(f"Rank by density (W>={DENSITY_MIN_WORDS}): {rank_dens_q59}/{len(windows_dense)}")

# Top-20 by density
top20_density = windows_by_density[:20]

# Permutation null for density: shuffle name-counts across verses (keep verse word-counts fixed)
# Replicate H-NEW-95's word-count-weighted null: draw verse positions for each name token
random.seed(SEED)
N_PERM = 10000
total_99_tokens = sum(per_verse_count_99)
print(f"Total 99-name tokens corpus-wide: {total_99_tokens}")

# Verse word-count weights
total_W = sum(per_verse_words)
weights = [w/total_W for w in per_verse_words]

# Cumulative weights for sampling
cum = []
running = 0.0
for w in weights:
    running += w
    cum.append(running)

import bisect
def sample_verse():
    r = random.random()
    return bisect.bisect_left(cum, r)

# null: how often does ANY 3-verse window achieve density >= observed_density
observed_density = q59_window['density']
observed_F99 = q59_window['F99']

null_max_F = []
null_max_density = []
for _ in range(N_PERM):
    null_counts = [0] * len(flat)
    for _t in range(total_99_tokens):
        idx = sample_verse()
        null_counts[idx] += 1
    # find max F across windows AND max density (W>=10)
    mx_F = 0
    mx_d = 0.0
    for start in range(len(flat) - 2):
        Fn = null_counts[start] + null_counts[start+1] + null_counts[start+2]
        Wn = per_verse_words[start] + per_verse_words[start+1] + per_verse_words[start+2]
        if Fn > mx_F:
            mx_F = Fn
        if Wn >= DENSITY_MIN_WORDS:
            d = Fn / Wn
            if d > mx_d:
                mx_d = d
    null_max_F.append(mx_F)
    null_max_density.append(mx_d)

# p-value: fraction of nulls where max(F) >= observed AND max(density) >= observed
p_F_geq = sum(1 for x in null_max_F if x >= observed_F99) / N_PERM
p_density_geq = sum(1 for x in null_max_density if x >= observed_density) / N_PERM

print(f"\nPermutation null (N={N_PERM}, seed={SEED}):")
print(f"  null_max_F mean: {sum(null_max_F)/N_PERM:.2f}, max: {max(null_max_F)}")
print(f"  null_max_density mean: {sum(null_max_density)/N_PERM:.4f}, max: {max(null_max_density):.4f}")
print(f"  p (F>=obs): {p_F_geq:.4f}")
print(f"  p (density>=obs): {p_density_geq:.4f}")

# Build prereg SHA
prereg_sha = ''
if PREREG.exists():
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()

result = {
    'finding_id': 'Q059-F-01',
    'title': 'Khawatim al-Hashr per-token-density replication of H-NEW-95',
    'prereg_sha': prereg_sha,
    'seed': SEED,
    'n_perm': N_PERM,
    'rules_tuple': '(no-tashkeel, ornament-stripped, whitespace-tokenized, proclitic-prefix-tolerant, basmala-counted-only-in-Q1, Hafs-Kufan, mashriqi)',
    'authored_by': 'Waiel Al-Shujaa',
    'date': '2026-05-09',
    'observed': {
        'window': 'Q 59:22-24',
        'F99_absolute': observed_F99,
        'words': q59_window['words'],
        'density_per_token': observed_density,
    },
    'corpus_total_99name_tokens': total_99_tokens,
    'rank_by_F99_absolute': rank_F_q59,
    'rank_by_density_W_geq_10': rank_dens_q59,
    'n_windows_total': len(windows),
    'n_windows_W_geq_10': len(windows_dense),
    'top_5_by_F99': [{'start_sid': w['start_sid'], 'start_vid': w['start_vid'], 'end_sid': w['end_sid'], 'end_vid': w['end_vid'], 'F99': w['F99'], 'words': w['words'], 'density': w['density']} for w in windows_by_F[:5]],
    'top_5_by_density': [{'start_sid': w['start_sid'], 'start_vid': w['start_vid'], 'end_sid': w['end_sid'], 'end_vid': w['end_vid'], 'F99': w['F99'], 'words': w['words'], 'density': w['density']} for w in windows_by_density[:5]],
    'top_20_by_density': [{'start_sid': w['start_sid'], 'start_vid': w['start_vid'], 'end_sid': w['end_sid'], 'end_vid': w['end_vid'], 'F99': w['F99'], 'words': w['words'], 'density': w['density']} for w in top20_density],
    'permutation_null': {
        'method': 'word-count-weighted verse re-draw of 99-name tokens (H-NEW-95-replicate); for each perm, max F and max density across all 6234 windows',
        'null_max_F_mean': sum(null_max_F)/N_PERM,
        'null_max_F_sd': (sum((x - sum(null_max_F)/N_PERM)**2 for x in null_max_F)/N_PERM) ** 0.5,
        'null_max_F_max_observed': max(null_max_F),
        'null_max_density_mean': sum(null_max_density)/N_PERM,
        'null_max_density_max_observed': max(null_max_density),
    },
    'p_one_sided': {
        'F99_geq_obs': p_F_geq,
        'density_geq_obs': p_density_geq,
    },
    'verdict': {
        'cell_A_F99_replication': 'PASS' if rank_F_q59 == 1 and p_F_geq < 0.01 else 'PARTIAL',
        'cell_B_density_extension': 'PASS' if rank_dens_q59 == 1 and p_density_geq < 0.01 else 'PARTIAL',
        'overall': 'CONFIRMED' if (rank_F_q59 == 1 and rank_dens_q59 == 1 and p_F_geq < 0.01 and p_density_geq < 0.01) else 'PARTIAL',
    }
}

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(f"\nWrote: {OUT}")
print(f"Verdict: {result['verdict']['overall']}")
