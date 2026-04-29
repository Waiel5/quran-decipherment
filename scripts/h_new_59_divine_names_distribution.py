#!/usr/bin/env python3
"""H-NEW-59 — Comprehensive distribution analysis of the 99 divine names.

Pre-reg: findings/phase-b-hypotheses/h-new-59-99-names-distribution-prereg.md

Cells:
  1. Per-name table (descriptive + MW-5 8-Khawātim positive control)
  2. Surah-exclusive name count
  3. Fātiḥa-as-encoding test (sliding-window null over 7-verse windows)
  4. Top-K verse-density ranking (MW-5 control: Q 59:23 must be top-3)
  5. Surah density ranking (MW-5 control: Q 59 must be top-5)
  6. Muqaṭṭaʿāt vs non-muq surah-density permutation test (100k perms)

Bonferroni k=6; α_bon = 0.00833.
Seed: 20260415.

Rules tuple: (no-tashkeel; substring search of definite-singular ال + name;
hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi).
"""
import json
import random
import re
import sys
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260415
N_PERM = 100_000
BON_K = 6
ALPHA_BON = 0.05 / BON_K  # 0.00833...

random.seed(SEED)

# ---------- Locked muqaṭṭaʿāt set (from H-NEW-46 / H-NEW-49) ----------
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
assert len(MUQ_SURAHS) == 29

# ---------- Locked 8 Khawātim al-Ḥashr names (MW-5 positive control) ----------
KHAWATIM_NAMES = {
    'القدوس', 'السلام', 'المؤمن', 'المهيمن',
    'الجبار', 'المتكبر', 'البارئ', 'المصور'
}

# ---------- Load corpus ----------
with open(ROOT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    corpus = json.load(f)

assert len(corpus) == 114, f"Expected 114 surahs, got {len(corpus)}"

# Build verse list: (surah_id, verse_id, text, word_count)
verses = []
for surah in corpus:
    sid = surah['id']
    for v in surah['verses']:
        text = v['text']
        words = text.split()
        verses.append({
            'sid': sid,
            'vid': v['id'],
            'text': text,
            'words': words,
            'wc': len(words),
        })
total_verses = len(verses)
print(f"[H-NEW-59] Loaded {len(corpus)} surahs, {total_verses} verses", file=sys.stderr)

# ---------- Load canonical 99 names ----------
NAMES = []
with open(ROOT / 'data/asma-al-husna.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        NAMES.append(line)
assert len(NAMES) == 99, f"Expected 99 names, got {len(NAMES)}"
print(f"[H-NEW-59] Loaded {len(NAMES)} canonical divine names", file=sys.stderr)

# Strip diacritics for safe substring matching (already no-tashkeel corpus)
DIACRITICS = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
def normalize(s):
    return DIACRITICS.sub('', s).strip()

NAMES = [normalize(n) for n in NAMES]

# ---------- Match function ----------
# A name occurs in a verse if:
#   1. It appears as an entire word (perfect match), OR
#   2. It appears with proclitic prefix (و, ف, ب, ل, ك, س) preceding ال,
#      i.e., the verse-word ends with the name string.
# We tokenize each verse into words, then for each word check exact-match
# and also stripped-prefix match.
PROCLITIC_PREFIXES = {'و', 'ف', 'ب', 'ل', 'ك', 'س', 'فب', 'وب', 'فل', 'ول', 'وس', 'فس'}

def word_matches_name(word, name):
    """Return True if word == name OR word == prefix + name with prefix in {و,ف,ب,ل,ك,س, ...}."""
    if word == name:
        return True
    # Try stripping each prefix
    if name.startswith('ال') or name.startswith('م') or name.startswith('ذ'):
        for pre in PROCLITIC_PREFIXES:
            if word == pre + name:
                return True
    return False

def count_name_in_verse(verse_words, name):
    """Count occurrences of name in the verse's word list."""
    if ' ' in name:
        # Multi-word name (Mālik al-Mulk, Dhū al-Jalāl wa-l-Ikrām)
        verse_text = ' ' + ' '.join(verse_words) + ' '
        # Exact substring match with whitespace boundaries
        target = ' ' + name + ' '
        count = 0
        idx = 0
        while True:
            pos = verse_text.find(target, idx)
            if pos == -1:
                break
            count += 1
            idx = pos + 1
        return count
    else:
        return sum(1 for w in verse_words if word_matches_name(w, name))

# ---------- Cell 1: per-name table ----------
print("[H-NEW-59] Cell 1: building per-name table...", file=sys.stderr)
name_table = []
for name in NAMES:
    surah_counts = Counter()
    verse_set = set()
    total_tokens = 0
    for v in verses:
        c = count_name_in_verse(v['words'], name)
        if c > 0:
            surah_counts[v['sid']] += c
            verse_set.add((v['sid'], v['vid']))
            total_tokens += c
    surahs = sorted(surah_counts.keys())
    if surah_counts:
        top_surah = max(surah_counts, key=lambda s: (surah_counts[s], -s))
        top_surah_count = surah_counts[top_surah]
    else:
        top_surah = None
        top_surah_count = 0
    name_table.append({
        'name': name,
        'tokens': total_tokens,
        'verses': len(verse_set),
        'surahs': len(surahs),
        'surah_list': surahs,
        'top_surah': top_surah,
        'top_surah_count': top_surah_count,
        'exclusivity_class': len(surahs),
        'attested': total_tokens > 0,
    })

# MW-5 positive control: 8 Khawātim
khawatim_check = []
for name in KHAWATIM_NAMES:
    matches = [n for n in name_table if n['name'] == name]
    if not matches:
        # Also try with hamza variants
        norm = name.replace('ئ', 'ء').replace('ؤ', 'ء')
        matches = [n for n in name_table if normalize(n['name']) == name]
    if matches:
        n = matches[0]
        khawatim_check.append({
            'name': name,
            'tokens': n['tokens'],
            'surahs': n['surahs'],
            'top_surah': n['top_surah'],
            'mw5_pass': n['surahs'] == 1 and n['top_surah'] == 59,
        })
    else:
        khawatim_check.append({'name': name, 'tokens': 0, 'surahs': 0, 'top_surah': None, 'mw5_pass': False})

khawatim_passed = sum(1 for k in khawatim_check if k['mw5_pass'])
khawatim_total = len(khawatim_check)
print(f"[H-NEW-59] MW-5 Khawātim check: {khawatim_passed}/{khawatim_total} passed", file=sys.stderr)
for k in khawatim_check:
    if not k['mw5_pass']:
        print(f"   FAIL: {k['name']} tokens={k['tokens']} surahs={k['surahs']} top={k['top_surah']}", file=sys.stderr)

# ---------- Cell 2: surah-exclusive count ----------
print("[H-NEW-59] Cell 2: surah-exclusive count...", file=sys.stderr)
surah_exclusive_attested = [n for n in name_table if n['surahs'] == 1 and n['tokens'] > 0]
bi_surah_attested = [n for n in name_table if n['surahs'] == 2 and n['tokens'] > 0]
tri_surah_attested = [n for n in name_table if n['surahs'] == 3 and n['tokens'] > 0]
zero_attested = [n for n in name_table if n['tokens'] == 0]
print(f"   Surah-exclusive (1-surah): {len(surah_exclusive_attested)}", file=sys.stderr)
print(f"   2-surah: {len(bi_surah_attested)}", file=sys.stderr)
print(f"   3-surah: {len(tri_surah_attested)}", file=sys.stderr)
print(f"   Zero-attested: {len(zero_attested)}", file=sys.stderr)

# ---------- Cell 3: Fātiḥa-as-encoding test ----------
print("[H-NEW-59] Cell 3: Fātiḥa as encoding...", file=sys.stderr)

# F = number of distinct names appearing in a 7-verse window
# Compute F for Q 1 first
def names_in_verse_range(start_idx, end_idx):
    """Return set of distinct names present in verses[start_idx:end_idx]."""
    names_present = set()
    for i in range(start_idx, end_idx):
        v = verses[i]
        for name in NAMES:
            if name in names_present:
                continue
            if count_name_in_verse(v['words'], name) > 0:
                names_present.add(name)
    return names_present

# Find Q 1 verse range
fatiha_start = None
fatiha_end = None
for i, v in enumerate(verses):
    if v['sid'] == 1:
        if fatiha_start is None:
            fatiha_start = i
        fatiha_end = i + 1
fatiha_names = names_in_verse_range(fatiha_start, fatiha_end)
F_fatiha = len(fatiha_names)
print(f"   Fātiḥa (Q 1 verses {fatiha_start}-{fatiha_end-1}): F = {F_fatiha}", file=sys.stderr)
print(f"   Names in Fātiḥa: {sorted(fatiha_names)}", file=sys.stderr)

# Sliding-window null: all 7-verse windows
# 6236 - 7 + 1 = 6230 windows
print("   Computing sliding-window null distribution (6230 windows of size 7)...", file=sys.stderr)
window_F = []
for i in range(0, total_verses - 7 + 1):
    names_in_window = names_in_verse_range(i, i + 7)
    window_F.append(len(names_in_window))

window_F.sort()
# Q1's percentile
n_at_or_below = sum(1 for f in window_F if f <= F_fatiha)
n_above = sum(1 for f in window_F if f > F_fatiha)
n_equal = sum(1 for f in window_F if f == F_fatiha)
percentile = n_at_or_below / len(window_F)
p_one_sided = n_above / len(window_F)  # P(F_window >= F_fatiha + 1) under uniform sampling
# Strict one-sided: P(F_window >= F_fatiha)
p_one_sided_geq = sum(1 for f in window_F if f >= F_fatiha) / len(window_F)
print(f"   Fātiḥa F = {F_fatiha}; null mean = {statistics.mean(window_F):.2f}, max = {max(window_F)}", file=sys.stderr)
print(f"   percentile = {percentile:.4f}; p(F_window >= {F_fatiha}) = {p_one_sided_geq:.4f}", file=sys.stderr)

# Top windows by F
top_windows = sorted(range(len(window_F)), key=lambda i: -window_F[i])[:20]
top_window_info = []
for wi in top_windows:
    start_v = verses[wi]
    end_v = verses[wi + 6]
    top_window_info.append({
        'start_sid': start_v['sid'], 'start_vid': start_v['vid'],
        'end_sid': end_v['sid'], 'end_vid': end_v['vid'],
        'F': window_F[wi],
    })

# ---------- Cell 4: top-K verse-density ranking ----------
print("[H-NEW-59] Cell 4: verse density ranking...", file=sys.stderr)
verse_densities = []
for v in verses:
    name_tokens_in_verse = 0
    names_found = []
    for name in NAMES:
        c = count_name_in_verse(v['words'], name)
        if c > 0:
            name_tokens_in_verse += c
            names_found.append((name, c))
    density = name_tokens_in_verse / max(v['wc'], 1)
    verse_densities.append({
        'sid': v['sid'],
        'vid': v['vid'],
        'wc': v['wc'],
        'name_tokens': name_tokens_in_verse,
        'density': density,
        'names': names_found,
    })

verse_densities.sort(key=lambda x: (-x['density'], -x['name_tokens'], x['sid'], x['vid']))
top20_verses = verse_densities[:20]
print(f"   Top verse density: Q {top20_verses[0]['sid']}:{top20_verses[0]['vid']} = {top20_verses[0]['density']:.3f}", file=sys.stderr)

# MW-5 control: Q 59:23 must be in top-3
top3_keys = [(v['sid'], v['vid']) for v in top20_verses[:3]]
mw5_q59_23 = (59, 23) in top3_keys
print(f"   MW-5: Q 59:23 in top-3? {mw5_q59_23}", file=sys.stderr)

# ---------- Cell 5: surah density ranking ----------
print("[H-NEW-59] Cell 5: surah density ranking...", file=sys.stderr)
surah_stats = {}
for surah in corpus:
    sid = surah['id']
    s_verses = [v for v in verses if v['sid'] == sid]
    total_words = sum(v['wc'] for v in s_verses)
    total_name_tokens = 0
    for v in s_verses:
        for name in NAMES:
            total_name_tokens += count_name_in_verse(v['words'], name)
    density = total_name_tokens / max(total_words, 1)
    surah_stats[sid] = {
        'sid': sid,
        'name': surah['name'],
        'translit': surah['transliteration'],
        'type': surah['type'],
        'total_verses': surah['total_verses'],
        'total_words': total_words,
        'name_tokens': total_name_tokens,
        'density': density,
        'is_muq': sid in MUQ_SURAHS,
    }

surah_ranked = sorted(surah_stats.values(), key=lambda x: -x['density'])
top20_surahs = surah_ranked[:20]
mw5_q59 = any(s['sid'] == 59 for s in surah_ranked[:5])
print(f"   Top surah density: Q {surah_ranked[0]['sid']} ({surah_ranked[0]['translit']}) = {surah_ranked[0]['density']:.4f}", file=sys.stderr)
print(f"   MW-5: Q 59 in top-5? {mw5_q59}", file=sys.stderr)

# ---------- Cell 6: muqaṭṭaʿāt vs non-muq permutation ----------
print("[H-NEW-59] Cell 6: muq vs non-muq permutation test...", file=sys.stderr)
muq_densities = [s['density'] for s in surah_stats.values() if s['is_muq']]
nmq_densities = [s['density'] for s in surah_stats.values() if not s['is_muq']]
muq_mean = statistics.mean(muq_densities)
nmq_mean = statistics.mean(nmq_densities)
obs_diff = muq_mean - nmq_mean
print(f"   Mean muq density = {muq_mean:.5f} (n={len(muq_densities)})", file=sys.stderr)
print(f"   Mean non-muq density = {nmq_mean:.5f} (n={len(nmq_densities)})", file=sys.stderr)
print(f"   Observed diff = {obs_diff:.5f}", file=sys.stderr)

all_dens = [s['density'] for s in surah_stats.values()]
n_muq = len(muq_densities)
n_total = len(all_dens)
extreme = 0
for _ in range(N_PERM):
    sample_indices = random.sample(range(n_total), n_muq)
    sample_muq = [all_dens[i] for i in sample_indices]
    sample_nmq = [all_dens[i] for i in range(n_total) if i not in set(sample_indices)]
    perm_diff = statistics.mean(sample_muq) - statistics.mean(sample_nmq)
    if abs(perm_diff) >= abs(obs_diff):
        extreme += 1
p_perm = (extreme + 1) / (N_PERM + 1)
print(f"   p_perm (two-sided, |diff| >= |obs_diff|) = {p_perm:.5f}", file=sys.stderr)

# Compute z under permutation null
import math
perm_diffs = []
random.seed(SEED)
for _ in range(10000):
    sample_indices = random.sample(range(n_total), n_muq)
    sample_muq = [all_dens[i] for i in sample_indices]
    sample_nmq = [all_dens[i] for i in range(n_total) if i not in set(sample_indices)]
    perm_diffs.append(statistics.mean(sample_muq) - statistics.mean(sample_nmq))
perm_mean = statistics.mean(perm_diffs)
perm_sd = statistics.stdev(perm_diffs)
z_score = (obs_diff - perm_mean) / perm_sd if perm_sd > 0 else 0
print(f"   z (vs perm null mean/sd over 10k) = {z_score:+.3f}", file=sys.stderr)

# ---------- Build JSON output ----------
out = {
    'meta': {
        'id': 'H-NEW-59',
        'date': '2026-04-15',
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': BON_K,
        'alpha_bon': ALPHA_BON,
        'rules_tuple': '(no-tashkeel; substring search of definite-singular ال + name; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)',
    },
    'corpus_stats': {
        'n_surahs': len(corpus),
        'n_verses': total_verses,
        'n_total_words': sum(v['wc'] for v in verses),
    },
    'cell_1_per_name_table': name_table,
    'cell_1_mw5_khawatim': {
        'passed': khawatim_passed,
        'total': khawatim_total,
        'detail': khawatim_check,
    },
    'cell_2_exclusivity_distribution': {
        'surah_exclusive_n': len(surah_exclusive_attested),
        'surah_exclusive_names': [n['name'] for n in surah_exclusive_attested],
        'surah_exclusive_top_surahs': [(n['name'], n['top_surah'], n['tokens']) for n in surah_exclusive_attested],
        'bi_surah_n': len(bi_surah_attested),
        'bi_surah_names': [(n['name'], n['surah_list']) for n in bi_surah_attested],
        'tri_surah_n': len(tri_surah_attested),
        'tri_surah_names': [(n['name'], n['surah_list']) for n in tri_surah_attested],
        'zero_attested_n': len(zero_attested),
        'zero_attested_names': [n['name'] for n in zero_attested],
    },
    'cell_3_fatiha_encoding': {
        'F_fatiha': F_fatiha,
        'fatiha_names': sorted(fatiha_names),
        'window_size': 7,
        'n_windows': len(window_F),
        'null_mean': statistics.mean(window_F),
        'null_sd': statistics.stdev(window_F),
        'null_max': max(window_F),
        'null_min': min(window_F),
        'percentile_at_or_below': percentile,
        'p_one_sided_geq': p_one_sided_geq,
        'p_one_sided_strict_gt': p_one_sided,
        'top_20_windows_by_F': top_window_info,
        'pass_at_alpha_bon': p_one_sided_geq < ALPHA_BON,
    },
    'cell_4_top_verse_density': {
        'top_20': [
            {
                'sid': v['sid'], 'vid': v['vid'],
                'wc': v['wc'], 'name_tokens': v['name_tokens'],
                'density': v['density'],
                'names': v['names'],
            }
            for v in top20_verses
        ],
        'mw5_q59_23_in_top3': mw5_q59_23,
    },
    'cell_5_top_surah_density': {
        'top_20': top20_surahs,
        'mw5_q59_in_top5': mw5_q59,
        'all_114_ranked': surah_ranked,
    },
    'cell_6_muq_vs_nonmuq': {
        'muq_n': len(muq_densities),
        'nmq_n': len(nmq_densities),
        'muq_mean_density': muq_mean,
        'nmq_mean_density': nmq_mean,
        'obs_diff': obs_diff,
        'perm_null_mean': perm_mean,
        'perm_null_sd': perm_sd,
        'z_score': z_score,
        'p_perm_two_sided': p_perm,
        'pass_at_alpha_bon': p_perm < ALPHA_BON,
        'direction': 'muq>nonmuq' if obs_diff > 0 else 'nonmuq>muq',
    },
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-59.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=str)
print(f"[H-NEW-59] Wrote {out_path}", file=sys.stderr)

# ---------- Console summary ----------
print()
print("=" * 70)
print("H-NEW-59 SUMMARY")
print("=" * 70)
print(f"Cell 1 MW-5 (8 Khawātim 1-surah/Q59): {khawatim_passed}/{khawatim_total}")
print(f"Cell 2 surah-exclusive names attested: {len(surah_exclusive_attested)}")
print(f"Cell 3 Fātiḥa F = {F_fatiha}; p_geq = {p_one_sided_geq:.4f}")
print(f"Cell 4 top-3 verses: {[(v['sid'], v['vid'], round(v['density'], 3)) for v in top20_verses[:3]]}")
print(f"Cell 5 top-5 surahs: {[(s['sid'], s['translit'], round(s['density'], 4)) for s in surah_ranked[:5]]}")
print(f"Cell 6 muq={muq_mean:.5f} nonmuq={nmq_mean:.5f} z={z_score:+.3f} p={p_perm:.4f}")
print()
print("TOP-10 SURAH-EXCLUSIVE NAMES:")
for n in sorted(surah_exclusive_attested, key=lambda x: (-x['tokens'], x['top_surah']))[:10]:
    print(f"  {n['name']:<20} surah={n['top_surah']:>3}  tokens={n['tokens']}")
print()
print("TOP-10 VERSES BY DIVINE-NAME DENSITY:")
for v in top20_verses[:10]:
    name_str = ', '.join(f"{n}×{c}" for n, c in v['names'][:5])
    print(f"  Q {v['sid']:>3}:{v['vid']:<3}  wc={v['wc']:>3}  d={v['density']:.3f}  [{v['name_tokens']} names: {name_str}]")
