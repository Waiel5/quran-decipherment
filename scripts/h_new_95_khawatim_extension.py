#!/usr/bin/env python3
"""H-NEW-95 — Khawātim al-Ḥashr second-look extension.

Pre-reg: findings/phase-b-hypotheses/h-new-95-khawatim-extension-prereg.md

Cells:
  A. 1-name echo verses (descriptive)
  B. 2-name echo verses (descriptive, H-NEW-63 extension to 9-name inventory)
  C. Co-occurrence network + high-degree attractor verses (verse-permutation null)
  D. Surah-level aggregation top-5 concentration (verse-permutation null)
  E. Reverse direction: Q 59:22-24 dense-rank across all 99 names over 3-verse
     sliding windows (MW-5 positive control)

Bonferroni k=5; α_bon = 0.01.
Seed: 20260417.

Rules tuple: (no-tashkeel; substring search of definite-singular ال + name;
word-matching with proclitic-prefix tolerance; hafs-kufan; 6236 verses;
basmala-counted-only-in-surah-1; mashriqi).
"""
import json
import random
import re
import sys
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERM = 10_000
BON_K = 5
ALPHA_BON = 0.05 / BON_K  # 0.01

# ---------- Locked 9-name Extended Khawātim inventory ----------
# 8 classical + al-Khāliq (per H-NEW-59 Cell 2: Q 59-exclusive under substring rule)
KHAWATIM_9 = [
    'القدوس',   # al-Quddūs
    'السلام',   # al-Salām
    'المؤمن',   # al-Muʾmin
    'المهيمن',  # al-Muhaymin
    'الجبار',   # al-Jabbār
    'المتكبر',  # al-Mutakabbir
    'الخالق',   # al-Khāliq
    'البارئ',   # al-Bāriʾ
    'المصور',   # al-Muṣawwir
]

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
assert total_verses == 6236, f"Expected 6236 verses, got {total_verses}"
print(f"[H-NEW-95] Loaded {len(corpus)} surahs, {total_verses} verses", file=sys.stderr)

# ---------- Load canonical 99 names (for Cell E) ----------
NAMES_99 = []
with open(ROOT / 'data/asma-al-husna.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        NAMES_99.append(line)
assert len(NAMES_99) == 99, f"Expected 99 names, got {len(NAMES_99)}"

DIACRITICS = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
def normalize(s):
    return DIACRITICS.sub('', s).strip()
NAMES_99 = [normalize(n) for n in NAMES_99]

# ---------- Match function (replicated from H-NEW-59) ----------
PROCLITIC_PREFIXES = {'و', 'ف', 'ب', 'ل', 'ك', 'س', 'فب', 'وب', 'فل', 'ول', 'وس', 'فس'}

def word_matches_name(word, name):
    if word == name:
        return True
    if name.startswith('ال') or name.startswith('م') or name.startswith('ذ'):
        for pre in PROCLITIC_PREFIXES:
            if word == pre + name:
                return True
    return False

def count_name_in_verse(verse_words, name):
    if ' ' in name:
        verse_text = ' ' + ' '.join(verse_words) + ' '
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

# ---------- Build per-name verse-occurrence table for the 9 Khawātim ----------
print("[H-NEW-95] Building per-name Khawātim verse-occurrence table...", file=sys.stderr)
khawatim_occurrences = {}   # name -> list of (sid, vid, count)
for name in KHAWATIM_9:
    occs = []
    for v in verses:
        c = count_name_in_verse(v['words'], name)
        if c > 0:
            occs.append({'sid': v['sid'], 'vid': v['vid'], 'count': c})
    khawatim_occurrences[name] = occs
    print(f"   {name}: {len(occs)} verses, {sum(o['count'] for o in occs)} tokens", file=sys.stderr)

# ---------- Cell A: 1-name echo verses (descriptive) ----------
print("[H-NEW-95] Cell A: 1-name echo verses...", file=sys.stderr)
verse_to_names = defaultdict(list)  # (sid, vid) -> [name, ...]
for name, occs in khawatim_occurrences.items():
    for o in occs:
        key = (o['sid'], o['vid'])
        verse_to_names[key].append({'name': name, 'count': o['count']})

one_name_verses = sorted(verse_to_names.keys())
cell_A_count = len(one_name_verses)
cell_A_list = []
for key in one_name_verses:
    sid, vid = key
    names_here = verse_to_names[key]
    cell_A_list.append({
        'sid': sid,
        'vid': vid,
        'n_names': len(names_here),
        'names': [x['name'] for x in names_here],
        'total_tokens': sum(x['count'] for x in names_here),
    })
print(f"   Cell A: {cell_A_count} verses contain ≥1 Khawātim name", file=sys.stderr)

# Per-name count summary
per_name_counts = {name: {
    'verses': len(occs),
    'tokens': sum(o['count'] for o in occs),
    'surahs': len(set(o['sid'] for o in occs)),
    'surah_list': sorted(set(o['sid'] for o in occs)),
} for name, occs in khawatim_occurrences.items()}

# ---------- Cell B: 2-name echo verses (H-NEW-63 extension) ----------
print("[H-NEW-95] Cell B: 2-name echo verses...", file=sys.stderr)
two_name_verses = [k for k in one_name_verses if len(verse_to_names[k]) >= 2]
cell_B_count = len(two_name_verses)
cell_B_list = []
for key in two_name_verses:
    sid, vid = key
    names_here = verse_to_names[key]
    # Recover verse text
    vtext = None
    for v in verses:
        if v['sid'] == sid and v['vid'] == vid:
            vtext = v['text']
            break
    cell_B_list.append({
        'sid': sid,
        'vid': vid,
        'n_khawatim_names': len(names_here),
        'names': [x['name'] for x in names_here],
        'total_tokens': sum(x['count'] for x in names_here),
        'verse_text': vtext,
    })
print(f"   Cell B: {cell_B_count} verses contain ≥2 Khawātim names", file=sys.stderr)
for entry in cell_B_list:
    print(f"     Q {entry['sid']}:{entry['vid']} → {entry['names']}", file=sys.stderr)

# ---------- Cell C: co-occurrence network + verse-permutation null ----------
print("[H-NEW-95] Cell C: co-occurrence network permutation null...", file=sys.stderr)
# Verse-degree distribution
degree_dist = Counter()
for key, namelist in verse_to_names.items():
    degree_dist[len(namelist)] += 1
# High-degree verses (degree >= 2)
K_obs = cell_B_count  # number of verses with ≥2 Khawātim names

# Null: for each of the 9 names, re-draw its verse occurrences at random, with
# probability proportional to verse word-count (to approximate "where names
# could have landed"), keeping the per-name token count fixed.
total_words = sum(v['wc'] for v in verses)
verse_wc_array = [v['wc'] for v in verses]
cum_wc = []
acc = 0
for wc in verse_wc_array:
    acc += wc
    cum_wc.append(acc)

def sample_verse_indices(n, rng):
    """Sample n verse indices with replacement weighted by word-count."""
    out = []
    for _ in range(n):
        r = rng.random() * total_words
        # binary search
        lo, hi = 0, total_verses - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if cum_wc[mid] < r:
                lo = mid + 1
            else:
                hi = mid
        out.append(lo)
    return out

# For the null, we need the "number of occurrences" per name — i.e., how many
# verse-slots to sample. We use the observed number of verses carrying that name
# (not token count, since a single verse with a name "twice" still counts once
# in the network). Actually per-name number of distinct verses is appropriate
# for degree counting.
per_name_verse_counts = {name: len(occs) for name, occs in khawatim_occurrences.items()}

rng = random.Random(SEED)
null_K_geq2 = []
null_K_geq3 = []
null_top5_share = []

# For Cell D: total Khawātim tokens per surah
obs_khawatim_tokens_per_surah = Counter()
for name, occs in khawatim_occurrences.items():
    for o in occs:
        obs_khawatim_tokens_per_surah[o['sid']] += o['count']

# Observed per-surah density
obs_surah_density = {}
surah_total_words = {}
for surah in corpus:
    sid = surah['id']
    sw = sum(v['wc'] for v in verses if v['sid'] == sid)
    surah_total_words[sid] = sw
    tokens = obs_khawatim_tokens_per_surah.get(sid, 0)
    obs_surah_density[sid] = (tokens / sw) if sw else 0

# Observed top-5 share (of total Khawātim tokens)
ranked_surahs = sorted(obs_surah_density.items(), key=lambda x: -x[1])
top5_surahs_ids = [s for s, d in ranked_surahs[:5]]
total_khawatim_tokens = sum(obs_khawatim_tokens_per_surah.values())
obs_top5_token_share = sum(obs_khawatim_tokens_per_surah[s] for s in top5_surahs_ids) / max(total_khawatim_tokens, 1)

# Also observed concentration of tokens: what share of total tokens is in top-5 by token count (not density)?
ranked_by_tokens = sorted(obs_khawatim_tokens_per_surah.items(), key=lambda x: -x[1])
top5_by_tokens_ids = [s for s, t in ranked_by_tokens[:5]]
obs_top5_tokens = sum(t for s, t in ranked_by_tokens[:5])
obs_top5_token_concentration = obs_top5_tokens / max(total_khawatim_tokens, 1)

print(f"   K_obs (verses with ≥2 Khawātim): {K_obs}", file=sys.stderr)
print(f"   top-5 by density: {top5_surahs_ids}", file=sys.stderr)
print(f"   top-5 density share of Khawātim tokens: {obs_top5_token_share:.4f}", file=sys.stderr)
print(f"   top-5 by token count: {top5_by_tokens_ids}, total {obs_top5_tokens} / {total_khawatim_tokens} = {obs_top5_token_concentration:.4f}", file=sys.stderr)

# Run permutation null
print(f"   Running {N_PERM} permutations...", file=sys.stderr)
for perm_i in range(N_PERM):
    # For each name, redraw its verses
    null_verse_to_count = Counter()   # idx -> count of distinct names hitting this verse
    null_surah_tokens = Counter()     # sid -> sum of tokens for each name assignment
    for name, n_verses in per_name_verse_counts.items():
        # Need to assign n_verses DISTINCT verse-indices (since each name occurs
        # in n_verses distinct verses in observed). But token counts per verse
        # may be >1 for names like al-Quddūs (1 token per verse for all 9 names
        # in practice). To stay faithful: sample distinct verses by word-count.
        # Use Fisher-style weighted sampling without replacement.
        # Since n_verses is small (<=7), use rejection sampling.
        chosen = set()
        attempts = 0
        while len(chosen) < n_verses and attempts < 200:
            r = rng.random() * total_words
            lo, hi = 0, total_verses - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if cum_wc[mid] < r:
                    lo = mid + 1
                else:
                    hi = mid
            chosen.add(lo)
            attempts += 1
        if len(chosen) < n_verses:
            # Fallback: fill with uniform random
            while len(chosen) < n_verses:
                chosen.add(rng.randrange(total_verses))
        # Use per-verse token count (observed) to preserve token totals roughly.
        # For simplicity, each distinct verse gets 1 token in the null (this
        # slightly deflates al-Quddūs which has 2 tokens but al-Quddūs appears
        # in 2 distinct verses, so 2 distinct-verse samples at 1 each = 2 tokens).
        # Confirm this matches observed: sum tokens per name ~= n_verses for all 9.
        name_total_tokens = sum(o['count'] for o in khawatim_occurrences[name])
        per_verse_token = name_total_tokens / n_verses   # ~1.0 for all Khawātim
        for idx in chosen:
            null_verse_to_count[idx] += 1
            null_surah_tokens[verses[idx]['sid']] += per_verse_token

    # Count verses with degree ≥ 2, ≥ 3
    null_K_geq2.append(sum(1 for c in null_verse_to_count.values() if c >= 2))
    null_K_geq3.append(sum(1 for c in null_verse_to_count.values() if c >= 3))

    # Top-5 by token concentration
    null_surah_token_counts = sorted(null_surah_tokens.values(), reverse=True)
    top5_null_tokens = sum(null_surah_token_counts[:5])
    null_total_tokens_this_perm = sum(null_surah_tokens.values())
    null_top5_share.append(top5_null_tokens / max(null_total_tokens_this_perm, 1))

    if (perm_i + 1) % 2000 == 0:
        print(f"     perm {perm_i + 1}/{N_PERM}", file=sys.stderr)

# Cell C inferential test
p_C_geq2 = sum(1 for x in null_K_geq2 if x >= K_obs) / len(null_K_geq2)
K_geq3_obs = sum(1 for k in one_name_verses if len(verse_to_names[k]) >= 3)
p_C_geq3 = sum(1 for x in null_K_geq3 if x >= K_geq3_obs) / len(null_K_geq3)
null_K_geq2_mean = statistics.mean(null_K_geq2)
null_K_geq2_sd = statistics.stdev(null_K_geq2) if len(null_K_geq2) > 1 else 0
null_K_geq3_mean = statistics.mean(null_K_geq3)
null_K_geq3_sd = statistics.stdev(null_K_geq3) if len(null_K_geq3) > 1 else 0
print(f"   Cell C (K≥2): obs={K_obs}, null mean={null_K_geq2_mean:.3f}, sd={null_K_geq2_sd:.3f}", file=sys.stderr)
print(f"   Cell C (K≥2): p_one_sided = {p_C_geq2:.5f} — PASS? {p_C_geq2 < ALPHA_BON}", file=sys.stderr)
print(f"   Cell C (K≥3): obs={K_geq3_obs}, null mean={null_K_geq3_mean:.3f}, sd={null_K_geq3_sd:.3f}", file=sys.stderr)
print(f"   Cell C (K≥3): p_one_sided = {p_C_geq3:.5f}", file=sys.stderr)

# Cell D inferential test (top-5 token concentration)
p_D = sum(1 for x in null_top5_share if x >= obs_top5_token_concentration) / len(null_top5_share)
null_top5_mean = statistics.mean(null_top5_share)
null_top5_sd = statistics.stdev(null_top5_share) if len(null_top5_share) > 1 else 0
print(f"   Cell D: obs top-5 token concentration = {obs_top5_token_concentration:.4f}", file=sys.stderr)
print(f"   Cell D: null mean = {null_top5_mean:.4f}, sd = {null_top5_sd:.4f}", file=sys.stderr)
print(f"   Cell D: p_one_sided = {p_D:.5f} — PASS? {p_D < ALPHA_BON}", file=sys.stderr)

# ---------- Cell D descriptive: surah ranking by Khawātim density ----------
surah_ranking = []
for sid in range(1, 115):
    info = {
        'sid': sid,
        'name': corpus[sid-1]['name'],
        'translit': corpus[sid-1]['transliteration'],
        'type': corpus[sid-1]['type'],
        'total_words': surah_total_words[sid],
        'khawatim_tokens': obs_khawatim_tokens_per_surah.get(sid, 0),
        'density': obs_surah_density[sid],
    }
    surah_ranking.append(info)
surah_ranking.sort(key=lambda x: (-x['density'], -x['khawatim_tokens'], x['sid']))
top5_surahs_info = surah_ranking[:5]
print(f"   Top-5 surahs by Khawātim density:", file=sys.stderr)
for s in top5_surahs_info:
    print(f"     Q {s['sid']:>3} {s['translit']:<20} density={s['density']:.6f}  tokens={s['khawatim_tokens']}", file=sys.stderr)

# ---------- Cell E: Q 59:22-24 density across ALL 99 names over 3-verse windows ----------
print("[H-NEW-95] Cell E: Q 59:22-24 total-99-name density rank...", file=sys.stderr)

# Pre-compute per-verse 99-name token count
print(f"   Pre-computing per-verse 99-name token counts...", file=sys.stderr)
per_verse_99_tokens = []
for v in verses:
    total = 0
    for name in NAMES_99:
        total += count_name_in_verse(v['words'], name)
    per_verse_99_tokens.append(total)

# 3-verse sliding windows
n_windows = total_verses - 3 + 1  # 6234
window_F = []
for i in range(n_windows):
    F = per_verse_99_tokens[i] + per_verse_99_tokens[i+1] + per_verse_99_tokens[i+2]
    window_F.append(F)

# Find Q 59:22-24 window index
q59_22_idx = None
for i, v in enumerate(verses):
    if v['sid'] == 59 and v['vid'] == 22:
        q59_22_idx = i
        break
assert q59_22_idx is not None, "Q 59:22 not found"
# Confirm 22-24 are consecutive
assert verses[q59_22_idx + 1]['sid'] == 59 and verses[q59_22_idx + 1]['vid'] == 23
assert verses[q59_22_idx + 2]['sid'] == 59 and verses[q59_22_idx + 2]['vid'] == 24
q59_window_F = window_F[q59_22_idx]
print(f"   Q 59:22-24 window index = {q59_22_idx}; F = {q59_window_F}", file=sys.stderr)

# Percentile
n_at_or_above = sum(1 for F in window_F if F >= q59_window_F)
n_strictly_above = sum(1 for F in window_F if F > q59_window_F)
percentile = 1 - (n_at_or_above / len(window_F))
p_one_sided_geq = n_at_or_above / len(window_F)
p_one_sided_strict = n_strictly_above / len(window_F)
null_mean_F = statistics.mean(window_F)
null_sd_F = statistics.stdev(window_F)
null_max_F = max(window_F)
print(f"   Null: mean F = {null_mean_F:.2f}, sd = {null_sd_F:.2f}, max = {null_max_F}", file=sys.stderr)
print(f"   Q 59:22-24 percentile = {percentile:.4f}; p(F_window ≥ F_q59) = {p_one_sided_geq:.5f}", file=sys.stderr)
print(f"   Cell E: PASS (top 1%)? {p_one_sided_geq < 0.01}", file=sys.stderr)

# Top-20 windows
top_indices = sorted(range(len(window_F)), key=lambda i: -window_F[i])[:20]
top_windows = []
for wi in top_indices:
    sv = verses[wi]
    ev = verses[wi + 2]
    top_windows.append({
        'start_sid': sv['sid'], 'start_vid': sv['vid'],
        'end_sid': ev['sid'], 'end_vid': ev['vid'],
        'F': window_F[wi],
    })

# ---------- Build JSON output ----------
# Get verse text for cell A top entries
def get_verse_text(sid, vid):
    for v in verses:
        if v['sid'] == sid and v['vid'] == vid:
            return v['text']
    return None

# Add verse text to cell A for top 20 by n_names, then all descriptive
cell_A_list_sorted = sorted(cell_A_list, key=lambda x: (-x['n_names'], -x['total_tokens'], x['sid'], x['vid']))

out = {
    'meta': {
        'id': 'H-NEW-95',
        'date': '2026-04-17',
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': BON_K,
        'bonferroni_family': 'h-new-95-khawatim-extension',
        'alpha_bon': ALPHA_BON,
        'rules_tuple': '(no-tashkeel; substring search of definite-singular ال + name; word-matching with proclitic-prefix tolerance; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)',
        'khawatim_9_names': KHAWATIM_9,
    },
    'corpus_stats': {
        'n_surahs': len(corpus),
        'n_verses': total_verses,
        'n_total_words': total_words,
    },
    'per_name_khawatim_counts': per_name_counts,
    'cell_A_one_name_echo_verses': {
        'count': cell_A_count,
        'verse_list_sorted_by_n_names': cell_A_list_sorted,
        'total_tokens_across_corpus': sum(x['total_tokens'] for x in cell_A_list),
    },
    'cell_B_two_name_echo_verses': {
        'count': cell_B_count,
        'verse_list': cell_B_list,
    },
    'cell_C_network': {
        'degree_distribution': dict(degree_dist),
        'K_obs_geq2': K_obs,
        'K_obs_geq3': K_geq3_obs,
        'null_n_perm': N_PERM,
        'null_K_geq2_mean': null_K_geq2_mean,
        'null_K_geq2_sd': null_K_geq2_sd,
        'null_K_geq3_mean': null_K_geq3_mean,
        'null_K_geq3_sd': null_K_geq3_sd,
        'p_one_sided_K_geq2': p_C_geq2,
        'p_one_sided_K_geq3': p_C_geq3,
        'pass_at_alpha_bon_K_geq2': p_C_geq2 < ALPHA_BON,
        'pass_at_alpha_bon_K_geq3': p_C_geq3 < ALPHA_BON,
        'null_K_geq2_max': max(null_K_geq2),
        'null_K_geq3_max': max(null_K_geq3),
    },
    'cell_D_surah_aggregation': {
        'top_5_by_density': top5_surahs_info,
        'top_20_ranking': surah_ranking[:20],
        'all_114_ranking': surah_ranking,
        'top_5_token_concentration_obs': obs_top5_token_concentration,
        'top_5_token_concentration_null_mean': null_top5_mean,
        'top_5_token_concentration_null_sd': null_top5_sd,
        'p_one_sided_top_5': p_D,
        'pass_at_alpha_bon_top_5': p_D < ALPHA_BON,
        'top_5_by_tokens': top5_by_tokens_ids,
        'total_khawatim_tokens_corpus': total_khawatim_tokens,
    },
    'cell_E_reverse_direction': {
        'Q_59_22_24_F': q59_window_F,
        'n_windows': len(window_F),
        'null_mean_F': null_mean_F,
        'null_sd_F': null_sd_F,
        'null_max_F': null_max_F,
        'percentile_Q_59_22_24': percentile,
        'p_one_sided_geq': p_one_sided_geq,
        'p_one_sided_strict': p_one_sided_strict,
        'pass_top_1_percent': p_one_sided_geq < 0.01,
        'pass_at_alpha_bon': p_one_sided_geq < ALPHA_BON,
        'top_20_3verse_windows': top_windows,
    },
}

# ---------- Robustness: H-NEW-63 broader inventory (all names in Q 59:22-24) ----------
print("[H-NEW-95] Robustness: H-NEW-63 broader inventory...", file=sys.stderr)
# All distinct divine names present in Q 59:22-24, per H-NEW-59 Cell 4 Table.
# Q 59:22: al-Raḥmān, al-Raḥīm
# Q 59:23: al-Malik, al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-ʿAzīz, al-Jabbār, al-Mutakabbir
# Q 59:24: al-ʿAzīz, al-Khāliq, al-Bāriʾ, al-Muṣawwir (al-Ḥakīm also appears)
# Broader Khawātim inventory = union of all names in these 3 verses
BROADER_KHAWATIM = [
    'الرحمن', 'الرحيم',
    'الملك', 'القدوس', 'السلام', 'المؤمن', 'المهيمن', 'العزيز', 'الجبار', 'المتكبر',
    'الخالق', 'البارئ', 'المصور', 'الحكيم',
]
# Dedupe while preserving order
seen = set()
BROADER_KHAWATIM = [n for n in BROADER_KHAWATIM if not (n in seen or seen.add(n))]
print(f"   Broader inventory: {len(BROADER_KHAWATIM)} names", file=sys.stderr)

broader_verse_to_names = defaultdict(list)
for name in BROADER_KHAWATIM:
    for v in verses:
        c = count_name_in_verse(v['words'], name)
        if c > 0:
            broader_verse_to_names[(v['sid'], v['vid'])].append({'name': name, 'count': c})

broader_2_name = sorted(
    [k for k, namelist in broader_verse_to_names.items() if len(namelist) >= 2]
)
broader_3_name = sorted(
    [k for k, namelist in broader_verse_to_names.items() if len(namelist) >= 3]
)
broader_5_name = sorted(
    [k for k, namelist in broader_verse_to_names.items() if len(namelist) >= 5]
)
print(f"   Broader ≥2-name verses: {len(broader_2_name)}", file=sys.stderr)
print(f"   Broader ≥3-name verses: {len(broader_3_name)}", file=sys.stderr)
print(f"   Broader ≥5-name verses: {len(broader_5_name)}", file=sys.stderr)

broader_2_name_list = []
for key in broader_2_name:
    sid, vid = key
    namelist = broader_verse_to_names[key]
    vtext = get_verse_text(sid, vid)
    broader_2_name_list.append({
        'sid': sid, 'vid': vid,
        'n_names': len(namelist),
        'names': [x['name'] for x in namelist],
        'verse_text': vtext,
    })

# Attach
out['robustness_broader_inventory'] = {
    'description': 'Secondary inventory: 14 distinct divine names in Q 59:22-24 (includes al-Malik, al-Raḥmān, al-Raḥīm, al-ʿAzīz, al-Ḥakīm — all non-exclusive). This is the inventory H-NEW-63 used implicitly when counting Q 62:1 as a 3-name echo.',
    'inventory': BROADER_KHAWATIM,
    'verses_with_geq_2': len(broader_2_name),
    'verses_with_geq_3': len(broader_3_name),
    'verses_with_geq_5': len(broader_5_name),
    'verses_with_geq_2_list': broader_2_name_list,
    'interpretation': 'Under the strict 9-name exclusive inventory (Cell B), only Q 59:23 and Q 59:24 qualify. Q 62:1 is a 1-name echo (al-Quddūs only) under the strict inventory. Under the broader 14-name Q 59:22-24 inventory, Q 62:1 becomes a 3-name echo, matching H-NEW-63.',
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-95.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=str)
print(f"[H-NEW-95] Wrote {out_path}", file=sys.stderr)

# ---------- Console summary ----------
print()
print("=" * 70)
print("H-NEW-95 SUMMARY")
print("=" * 70)
print(f"Cell A (1-name echo verses): {cell_A_count}")
print(f"Cell B (2-name echo verses): {cell_B_count}")
print(f"  {[(e['sid'], e['vid'], e['n_khawatim_names']) for e in cell_B_list]}")
print(f"Cell C: K_obs(≥2)={K_obs}, null_mean={null_K_geq2_mean:.2f}, p={p_C_geq2:.5f} ({'PASS' if p_C_geq2 < ALPHA_BON else 'NULL'})")
print(f"Cell D: top-5 density = {[s['sid'] for s in top5_surahs_info]}")
print(f"  top-5 token concentration obs={obs_top5_token_concentration:.3f} null={null_top5_mean:.3f} p={p_D:.5f} ({'PASS' if p_D < ALPHA_BON else 'NULL'})")
print(f"Cell E: Q 59:22-24 F={q59_window_F} null_mean={null_mean_F:.2f} p={p_one_sided_geq:.5f} ({'PASS (top 1%)' if p_one_sided_geq < 0.01 else 'NULL'})")
print()
print("TOP-5 KHAWĀTIM-RICH SURAHS:")
for s in top5_surahs_info:
    print(f"  Q {s['sid']:>3} {s['translit']:<20} density={s['density']:.6f}  tokens={s['khawatim_tokens']}")
print()
print("2-NAME ECHO VERSES (Cell B):")
for e in cell_B_list:
    print(f"  Q {e['sid']:>3}:{e['vid']:<3}  names={e['names']}")
