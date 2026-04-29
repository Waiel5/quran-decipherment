#!/usr/bin/env python3
"""H-NEW-71 — Comprehensive distribution analysis of the word "Allah" (الله).

Pre-reg: findings/phase-b-hypotheses/h-new-71-allah-distribution-prereg.md

Cells:
  1. Per-surah descriptive table + MW-5 (Q1 must contain >=1 Allah-token)
  2. Zero-Allah surahs vs uniform null
  3. Verse-position distribution (OPEN/MID/CLOSE) chi^2 + Cell-3a fasila-exact
  4. Surah-position distribution (S_OPEN/S_MID/S_CLOSE) chi^2
  5. Density-crown verses + MW-5 anchors (Q 2:255, Q 24:35-37, Q 59:22-24)
  6. Surah density ranking + Spearman rho with length
  7. Nöldeke phase Kruskal-Wallis + Cell 7a muq vs non-muq Mann-Whitney

Bonferroni k=7; alpha_bon = 0.007143.
Seed: 20260417.

Rules tuple: (no-tashkeel; word-token match of {الله, لله, اللهم, آلله} +
locked proclitic prefixes {و, ف, ب, ت, أب, أف, أو, وت, فت, فب} for الله +
{و, ف} for لله; hafs-kufan; canonical-114; 6236 verses;
basmala-counted-only-in-surah-1; mashriqi).
"""
import csv
import json
import math
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERM = 100_000
BON_K = 7
ALPHA_BON = 0.05 / BON_K  # 0.007142857...

random.seed(SEED)

# ---------- Locked muqaṭṭaʿāt set ----------
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
assert len(MUQ_SURAHS) == 29

# ---------- Locked Allah-counting rule ----------
ALLOWED_PREFIXES_ALLAH = {'و','ف','ب','ت','أب','أف','أو','وت','فت','فب'}
ALLOWED_PREFIXES_LILLAH = {'و','ف'}

def is_allah_token(w):
    """Return (True, form_label) if w is an Allah-token under the locked rule, else (False, None)."""
    w = w.strip()
    if not w:
        return False, None
    # Form 1: bare الله
    if w == 'الله':
        return True, 'الله'
    # Form 2: vocative
    if w == 'اللهم':
        return True, 'اللهم'
    # Form 3: interrogative آلله
    if w == 'آلله':
        return True, 'آلله'
    # Form 4: لله (li- + Allah, alif elided)
    if w == 'لله':
        return True, 'لله'
    # Form 5: prefix + الله
    if w.endswith('الله') and len(w) > 4:
        prefix = w[:-len('الله')]
        if prefix in ALLOWED_PREFIXES_ALLAH:
            return True, f'{prefix}+الله'
        return False, None
    # Form 6: prefix + لله (excluding ل which would re-derive لله itself)
    if w.endswith('لله') and not w.endswith('الله') and len(w) > 3:
        prefix = w[:-len('لله')]
        if prefix in ALLOWED_PREFIXES_LILLAH:
            return True, f'{prefix}+لله'
        return False, None
    return False, None

# ---------- Load corpus ----------
with open(ROOT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    corpus = json.load(f)
assert len(corpus) == 114, f"Expected 114 surahs, got {len(corpus)}"

verses = []  # (sid, vid, text, words, wc)
for surah in corpus:
    sid = surah['id']
    for v in surah['verses']:
        words = v['text'].split()
        verses.append({
            'sid': sid,
            'vid': v['id'],
            'text': v['text'],
            'words': words,
            'wc': len(words),
        })
TOTAL_VERSES = len(verses)
TOTAL_WORDS = sum(v['wc'] for v in verses)
print(f"[H-NEW-71] Loaded {len(corpus)} surahs, {TOTAL_VERSES} verses, {TOTAL_WORDS} words", file=sys.stderr)

# ---------- Load chronology ----------
chronology = {}
with open(ROOT / 'data/revelation-order.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = int(row['mushaf_order'])
        chronology[sid] = {
            'rev_order': int(row['revelation_order']),
            'period': row['period'],
            'noldeke_order': int(row['noldeke_order']),
            'noldeke_phase': row['noldeke_phase'],
        }
assert len(chronology) == 114, f"Expected 114 chronology rows, got {len(chronology)}"

# ---------- Identify Allah-tokens with positions ----------
print("[H-NEW-71] Locating Allah-tokens...", file=sys.stderr)
allah_tokens = []  # list of dicts: sid, vid, word_pos (1-indexed), wc, n_v (surah verse count), surah_v_pos, form
verse_allah_count = defaultdict(int)  # (sid, vid) -> count
surah_allah_count = defaultdict(int)  # sid -> count
form_counter = Counter()
edge_check = []  # tokens we skipped that ended in الله/لله for audit

# precompute n_v per surah
n_v_map = {s['id']: s['total_verses'] for s in corpus}

for v in verses:
    sid = v['sid']
    vid = v['vid']
    wc = v['wc']
    n_v = n_v_map[sid]
    for word_pos, w in enumerate(v['words'], start=1):
        ok, form = is_allah_token(w)
        if ok:
            allah_tokens.append({
                'sid': sid,
                'vid': vid,
                'word_pos': word_pos,
                'wc': wc,
                'n_v': n_v,
                'surah_v_pos': vid,
                'form': form,
                'token': w,
            })
            verse_allah_count[(sid, vid)] += 1
            surah_allah_count[sid] += 1
            form_counter[form] += 1
        elif w.endswith('الله') or w.endswith('لله'):
            edge_check.append({'sid': sid, 'vid': vid, 'word': w})

N_ALLAH = len(allah_tokens)
print(f"[H-NEW-71] Total Allah-tokens (locked rule): {N_ALLAH}", file=sys.stderr)
print(f"[H-NEW-71] Form distribution:", file=sys.stderr)
for form, c in sorted(form_counter.items(), key=lambda x: -x[1]):
    print(f"   {form}: {c}", file=sys.stderr)
print(f"[H-NEW-71] Edge-cases excluded: {len(edge_check)}", file=sys.stderr)
for e in edge_check:
    print(f"   Q{e['sid']}:{e['vid']}  {e['word']}", file=sys.stderr)

# ---------- Cell 1 — per-surah table + MW-5 ----------
print("[H-NEW-71] Cell 1: per-surah table + MW-5...", file=sys.stderr)
surah_table = []
for s in corpus:
    sid = s['id']
    s_verses = [v for v in verses if v['sid'] == sid]
    s_word_count = sum(v['wc'] for v in s_verses)
    s_allah_count = surah_allah_count.get(sid, 0)
    n_allah_bearing_verses = sum(1 for v in s_verses if verse_allah_count.get((sid, v['vid']), 0) > 0)
    density_per_word = s_allah_count / max(s_word_count, 1)
    density_per_verse = s_allah_count / len(s_verses)
    bearing_frac = n_allah_bearing_verses / len(s_verses)
    surah_table.append({
        'sid': sid,
        'name': s['name'],
        'translit': s['transliteration'],
        'type': s['type'],  # meccan/medinan
        'noldeke_phase': chronology[sid]['noldeke_phase'],
        'rev_order': chronology[sid]['rev_order'],
        'n_verses': len(s_verses),
        'n_words': s_word_count,
        'allah_count': s_allah_count,
        'n_allah_verses': n_allah_bearing_verses,
        'density_per_word': density_per_word,
        'density_per_verse': density_per_verse,
        'bearing_frac': bearing_frac,
        'is_muq': sid in MUQ_SURAHS,
    })

# MW-5: Q1 must have >=1 Allah-token
q1_count = surah_allah_count.get(1, 0)
mw5_q1_ok = q1_count >= 1
print(f"[H-NEW-71] MW-5 Cell 1: Q1 Allah count = {q1_count}; pass = {mw5_q1_ok}", file=sys.stderr)
assert mw5_q1_ok, "EXTRACTOR_BROKEN: Q 1 has no Allah-tokens!"

# ---------- Cell 2 — zero-Allah surahs vs uniform null ----------
print("[H-NEW-71] Cell 2: zero-Allah surahs vs uniform null...", file=sys.stderr)
zero_allah_surahs = [s for s in surah_table if s['allah_count'] == 0]
nonzero_count = len(surah_table) - len(zero_allah_surahs)
print(f"   Observed zero-Allah surahs: {len(zero_allah_surahs)}", file=sys.stderr)

# Uniform null: assume each Allah-token is uniformly placed across TOTAL_WORDS positions
# A surah of n_w words has expected p(zero Allah) = (1 - n_w/TOTAL_WORDS)^N_ALLAH
expected_zero_count = 0.0
per_surah_p_zero = []
for s in surah_table:
    p_no_token_per_draw = 1 - (s['n_words'] / TOTAL_WORDS)
    p_zero = p_no_token_per_draw ** N_ALLAH
    expected_zero_count += p_zero
    per_surah_p_zero.append({'sid': s['sid'], 'translit': s['translit'], 'n_words': s['n_words'],
                             'p_zero_uniform': p_zero, 'observed_zero': s['allah_count'] == 0})

print(f"   Expected (uniform null): {expected_zero_count:.4f}", file=sys.stderr)

# Two-sided exact test: simulate (each surah drops Allah-tokens i.i.d. uniform; count zero surahs)
# Use binomial-like simulation
print("   Simulating uniform null (10000 sims)...", file=sys.stderr)
extreme_count = 0
n_sim = 10000
sim_zero_counts = []
for _ in range(n_sim):
    # For each surah, simulate (1 - n_w/W)^N_ALLAH probability of zero — Bernoulli
    sim_zero = sum(1 for ps in per_surah_p_zero if random.random() < ps['p_zero_uniform'])
    sim_zero_counts.append(sim_zero)
    if abs(sim_zero - expected_zero_count) >= abs(len(zero_allah_surahs) - expected_zero_count):
        extreme_count += 1
p_uniform_zero = (extreme_count + 1) / (n_sim + 1)
print(f"   p(uniform null, two-sided) = {p_uniform_zero:.4f}", file=sys.stderr)

# ---------- Cell 3 — verse-position distribution ----------
print("[H-NEW-71] Cell 3: verse-position distribution...", file=sys.stderr)
def classify_verse_pos(p, wc):
    """OPEN if p <= ceil(wc/4); MID if up to ceil(3wc/4); CLOSE otherwise."""
    if wc <= 0:
        return 'NA'
    q1 = math.ceil(wc / 4)
    q3 = math.ceil(3 * wc / 4)
    if p <= q1:
        return 'OPEN'
    if p <= q3:
        return 'MID'
    return 'CLOSE'

pos_counter = Counter()
fasila_exact_count = 0
for tok in allah_tokens:
    pc = classify_verse_pos(tok['word_pos'], tok['wc'])
    pos_counter[pc] += 1
    if tok['word_pos'] == tok['wc']:
        fasila_exact_count += 1
print(f"   Position counts (locked Allah-tokens): {dict(pos_counter)}", file=sys.stderr)

# Compute expected counts under uniform-position null
# For a verse with wc words, expected fraction OPEN = ceil(wc/4)/wc, etc.
# But Allah-tokens are not iid; we should compute the EXPECTED fraction by:
# For each Allah-bearing verse-instance, the position is uniform over (1..wc).
# Sum of expected OPEN/MID/CLOSE per token = sum over all tokens of their per-verse uniform probabilities.
exp_open = 0.0
exp_mid = 0.0
exp_close = 0.0
for tok in allah_tokens:
    wc = tok['wc']
    if wc <= 0:
        continue
    q1 = math.ceil(wc / 4)
    q3 = math.ceil(3 * wc / 4)
    n_open = q1
    n_mid = q3 - q1
    n_close = wc - q3
    exp_open += n_open / wc
    exp_mid += n_mid / wc
    exp_close += n_close / wc
print(f"   Expected (uniform-within-verse): OPEN={exp_open:.1f} MID={exp_mid:.1f} CLOSE={exp_close:.1f}", file=sys.stderr)

# Chi^2 goodness-of-fit
chi2 = 0.0
for cls, exp in [('OPEN', exp_open), ('MID', exp_mid), ('CLOSE', exp_close)]:
    obs = pos_counter[cls]
    if exp > 0:
        chi2 += (obs - exp) ** 2 / exp
df = 2

# Compute p-value from chi^2 (k=2 df) — survival = exp(-x/2) * (1 + x/2) for k=2
# Wait, that's for k=2 exponential. Chi^2 with df=2 has CDF F(x) = 1 - exp(-x/2)
def chi2_sf(x, df):
    """Survival function for chi^2; uses incomplete gamma."""
    return upper_inc_gamma_reg(df / 2, x / 2)

def upper_inc_gamma_reg(s, x):
    """Regularized upper incomplete gamma Q(s, x)."""
    if x < 0:
        return 1.0
    if x == 0:
        return 1.0
    # Use series for x < s+1 or continued fraction otherwise
    if x < s + 1:
        return 1.0 - lower_inc_gamma_reg(s, x)
    # Continued fraction
    # Lentz-style for upper incomplete gamma
    EPS = 1e-15
    FPMIN = 1e-300
    b = x + 1.0 - s
    c = 1.0 / FPMIN
    d = 1.0 / b
    h = d
    for i in range(1, 1001):
        an = -i * (i - s)
        b += 2.0
        d = an * d + b
        if abs(d) < FPMIN:
            d = FPMIN
        c = b + an / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return math.exp(-x + s * math.log(x) - math.lgamma(s)) * h

def lower_inc_gamma_reg(s, x):
    """Regularized lower incomplete gamma P(s, x) via series."""
    if x < 0:
        return 0.0
    if x == 0:
        return 0.0
    # Series
    ap = s
    sum_ = 1.0 / s
    delta = sum_
    for _ in range(1, 1001):
        ap += 1.0
        delta *= x / ap
        sum_ += delta
        if abs(delta) < abs(sum_) * 1e-15:
            break
    return sum_ * math.exp(-x + s * math.log(x) - math.lgamma(s))

p_chi2_pos = chi2_sf(chi2, df)
print(f"   chi^2 = {chi2:.3f} df=2; p = {p_chi2_pos:.4e}", file=sys.stderr)
print(f"   PASS at α_bon? {p_chi2_pos < ALPHA_BON}", file=sys.stderr)

# Cell 3a — fāṣila exact
exp_fasila = sum(1.0 / tok['wc'] for tok in allah_tokens if tok['wc'] > 0)
# Two-sided binomial test approximation via normal
# n = N_ALLAH, sum of Bernoullis with varying p; under null E = exp_fasila, Var = sum(p_i (1-p_i))
var_fasila = sum((1.0 / tok['wc']) * (1 - 1.0 / tok['wc']) for tok in allah_tokens if tok['wc'] > 0)
sd_fasila = math.sqrt(var_fasila) if var_fasila > 0 else 1.0
z_fasila = (fasila_exact_count - exp_fasila) / sd_fasila
# Two-sided normal p
p_fasila = 2 * (1 - 0.5 * (1 + math.erf(abs(z_fasila) / math.sqrt(2))))
print(f"   Cell 3a fāṣila-exact: obs={fasila_exact_count} exp={exp_fasila:.1f} z={z_fasila:+.2f} p={p_fasila:.4e}", file=sys.stderr)

# ---------- Cell 4 — surah-position distribution ----------
print("[H-NEW-71] Cell 4: surah-position distribution...", file=sys.stderr)
def classify_surah_pos(j, n_v):
    if n_v <= 0:
        return 'NA'
    q1 = math.ceil(n_v / 4)
    q3 = math.ceil(3 * n_v / 4)
    if j <= q1:
        return 'S_OPEN'
    if j <= q3:
        return 'S_MID'
    return 'S_CLOSE'

s_pos_counter = Counter()
exp_s_open = 0.0
exp_s_mid = 0.0
exp_s_close = 0.0
for tok in allah_tokens:
    sc = classify_surah_pos(tok['surah_v_pos'], tok['n_v'])
    s_pos_counter[sc] += 1
    n_v = tok['n_v']
    q1 = math.ceil(n_v / 4)
    q3 = math.ceil(3 * n_v / 4)
    n_open = q1
    n_mid = q3 - q1
    n_close = n_v - q3
    exp_s_open += n_open / n_v
    exp_s_mid += n_mid / n_v
    exp_s_close += n_close / n_v
print(f"   Surah-position counts: {dict(s_pos_counter)}", file=sys.stderr)
print(f"   Expected: S_OPEN={exp_s_open:.1f} S_MID={exp_s_mid:.1f} S_CLOSE={exp_s_close:.1f}", file=sys.stderr)

chi2_s = 0.0
for cls, exp in [('S_OPEN', exp_s_open), ('S_MID', exp_s_mid), ('S_CLOSE', exp_s_close)]:
    obs = s_pos_counter[cls]
    if exp > 0:
        chi2_s += (obs - exp) ** 2 / exp
p_chi2_s = chi2_sf(chi2_s, 2)
print(f"   chi^2 = {chi2_s:.3f} df=2; p = {p_chi2_s:.4e}", file=sys.stderr)
print(f"   PASS at α_bon? {p_chi2_s < ALPHA_BON}", file=sys.stderr)

# ---------- Cell 5 — density-crown verses + MW-5 anchors ----------
print("[H-NEW-71] Cell 5: density-crown verses...", file=sys.stderr)
verse_density = []
for v in verses:
    sid, vid, wc = v['sid'], v['vid'], v['wc']
    n_allah = verse_allah_count.get((sid, vid), 0)
    d = n_allah / max(wc, 1)
    verse_density.append({
        'sid': sid, 'vid': vid, 'wc': wc, 'n_allah': n_allah,
        'density': d, 'text_excerpt': v['text'][:100],
    })
verse_density.sort(key=lambda x: (-x['density'], -x['n_allah'], x['sid'], x['vid']))
top30_verses = verse_density[:30]

# MW-5 anchors
top50_keys = set((v['sid'], v['vid']) for v in verse_density[:50])
top100_keys = set((v['sid'], v['vid']) for v in verse_density[:100])
mw5_kursi = (2, 255) in top50_keys
mw5_light_cluster = any((24, vid) in top100_keys for vid in [35, 36, 37])
mw5_khawatim = any((59, vid) in top50_keys for vid in [22, 23, 24])
mw5_passes = sum([mw5_kursi, mw5_light_cluster, mw5_khawatim])
print(f"   MW-5: Kursī(2:255) in top-50? {mw5_kursi}", file=sys.stderr)
print(f"   MW-5: Light(24:35-37) in top-100? {mw5_light_cluster}", file=sys.stderr)
print(f"   MW-5: Khawātim(59:22-24) in top-50? {mw5_khawatim}", file=sys.stderr)
print(f"   MW-5 anchor count: {mw5_passes}/3 (need >=2)", file=sys.stderr)

# Find ranks for the MW-5 anchors specifically
def find_rank(sid, vid):
    for i, vd in enumerate(verse_density, 1):
        if vd['sid'] == sid and vd['vid'] == vid:
            return i
    return None

mw5_ranks = {
    'Q2:255_Kursi': find_rank(2, 255),
    'Q24:35_Light': find_rank(24, 35),
    'Q24:36_Light': find_rank(24, 36),
    'Q24:37_Light': find_rank(24, 37),
    'Q59:22_Khawatim': find_rank(59, 22),
    'Q59:23_Khawatim': find_rank(59, 23),
    'Q59:24_Khawatim': find_rank(59, 24),
}
for k, v in mw5_ranks.items():
    print(f"   Rank {k}: {v}", file=sys.stderr)

# ---------- Cell 6 — surah density ranking + Spearman ρ with length ----------
print("[H-NEW-71] Cell 6: surah density + Spearman ρ...", file=sys.stderr)
surah_ranked = sorted(surah_table, key=lambda x: -x['density_per_word'])
top15_surahs = surah_ranked[:15]
bottom15_surahs = surah_ranked[-15:]

def spearman_rho(xs, ys):
    """Spearman correlation; returns (rho, p_two_sided_normal_approx)."""
    n = len(xs)
    if n < 3:
        return 0.0, 1.0
    # Rank
    def rankdata(arr):
        sorted_pairs = sorted(enumerate(arr), key=lambda x: x[1])
        ranks = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and sorted_pairs[j+1][1] == sorted_pairs[i][1]:
                j += 1
            avg_rank = (i + j) / 2.0 + 1.0  # 1-indexed
            for k in range(i, j+1):
                ranks[sorted_pairs[k][0]] = avg_rank
            i = j + 1
        return ranks
    rx = rankdata(xs)
    ry = rankdata(ys)
    mean_x = sum(rx) / n
    mean_y = sum(ry) / n
    num = sum((rx[i]-mean_x) * (ry[i]-mean_y) for i in range(n))
    denom_x = math.sqrt(sum((rx[i]-mean_x)**2 for i in range(n)))
    denom_y = math.sqrt(sum((ry[i]-mean_y)**2 for i in range(n)))
    if denom_x == 0 or denom_y == 0:
        return 0.0, 1.0
    rho = num / (denom_x * denom_y)
    # t-test for rho
    t = rho * math.sqrt((n - 2) / (1 - rho**2)) if abs(rho) < 1.0 else 1e9
    # two-sided p via t-distribution; use normal approximation for simplicity
    # better: incomplete beta. For df=n-2 large, normal approx is fine
    z = t * (1 - 0.25 / (n - 2))  # mild small-sample correction
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return rho, p

n_words_arr = [s['n_words'] for s in surah_table]
n_verses_arr = [s['n_verses'] for s in surah_table]
density_arr = [s['density_per_word'] for s in surah_table]

rho_words, p_words = spearman_rho(density_arr, n_words_arr)
rho_verses, p_verses = spearman_rho(density_arr, n_verses_arr)
print(f"   Spearman ρ(density, n_words) = {rho_words:+.3f}; p = {p_words:.4e}", file=sys.stderr)
print(f"   Spearman ρ(density, n_verses) = {rho_verses:+.3f}; p = {p_verses:.4e}", file=sys.stderr)
print(f"   PASS (n_words) at α_bon? {p_words < ALPHA_BON}", file=sys.stderr)

# ---------- Cell 7 — Nöldeke phase Kruskal-Wallis + Cell 7a muq vs non-muq ----------
print("[H-NEW-71] Cell 7: Nöldeke phase Kruskal-Wallis...", file=sys.stderr)
phase_groups = defaultdict(list)
for s in surah_table:
    phase_groups[s['noldeke_phase']].append(s['density_per_word'])
phase_summary = {phase: {
    'n': len(vals),
    'mean_density': statistics.mean(vals),
    'median_density': statistics.median(vals),
} for phase, vals in phase_groups.items()}
for phase, summ in phase_summary.items():
    print(f"   {phase}: n={summ['n']} mean_density={summ['mean_density']:.4f} median={summ['median_density']:.4f}", file=sys.stderr)

def kruskal_wallis(groups):
    """Compute KW H statistic + chi^2 df=k-1 p."""
    all_vals = []
    for g_id, g in enumerate(groups):
        for v in g:
            all_vals.append((v, g_id))
    n_total = len(all_vals)
    # Rank
    sorted_vals = sorted(all_vals, key=lambda x: x[0])
    ranks = {}  # index -> rank
    i = 0
    rank_assignments = [0.0] * n_total
    sorted_idx_to_orig = []
    for sv_i, (val, gid) in enumerate(sorted_vals):
        sorted_idx_to_orig.append(sv_i)
    # Average ranks for ties
    i = 0
    while i < n_total:
        j = i
        while j + 1 < n_total and sorted_vals[j+1][0] == sorted_vals[i][0]:
            j += 1
        avg_r = (i + j) / 2.0 + 1.0
        for k in range(i, j+1):
            rank_assignments[k] = avg_r
        i = j + 1
    group_rank_sums = defaultdict(float)
    group_ns = defaultdict(int)
    for sv_i, (val, gid) in enumerate(sorted_vals):
        group_rank_sums[gid] += rank_assignments[sv_i]
        group_ns[gid] += 1
    H = 12.0 / (n_total * (n_total + 1)) * sum(
        (group_rank_sums[gid] ** 2) / group_ns[gid] for gid in group_ns
    ) - 3 * (n_total + 1)
    df_kw = len(groups) - 1
    p = chi2_sf(H, df_kw) if df_kw >= 1 else 1.0
    return H, df_kw, p

# Order phases canonically
PHASE_ORDER = ['Early Meccan', 'Middle Meccan', 'Late Meccan', 'Medinan']
groups_for_kw = [phase_groups[p] for p in PHASE_ORDER]
H_kw, df_kw, p_kw = kruskal_wallis(groups_for_kw)
print(f"   Kruskal-Wallis H = {H_kw:.3f} df={df_kw} p = {p_kw:.4e}", file=sys.stderr)
print(f"   PASS at α_bon? {p_kw < ALPHA_BON}", file=sys.stderr)

# Cell 7a — muq vs non-muq Mann-Whitney
print("[H-NEW-71] Cell 7a: muq vs non-muq Mann-Whitney...", file=sys.stderr)
muq_dens = [s['density_per_word'] for s in surah_table if s['is_muq']]
nmq_dens = [s['density_per_word'] for s in surah_table if not s['is_muq']]
def mann_whitney_u(xs, ys):
    """U statistic + asymptotic two-sided p."""
    nx = len(xs)
    ny = len(ys)
    combined = [(v, 0) for v in xs] + [(v, 1) for v in ys]
    combined.sort(key=lambda x: x[0])
    # Average ranks for ties
    n = len(combined)
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and combined[j+1][0] == combined[i][0]:
            j += 1
        avg_r = (i + j) / 2.0 + 1.0
        for k in range(i, j+1):
            ranks[k] = avg_r
        i = j + 1
    R1 = sum(ranks[i] for i in range(n) if combined[i][1] == 0)
    U1 = R1 - nx * (nx + 1) / 2.0
    U2 = nx * ny - U1
    U = min(U1, U2)
    # Asymptotic two-sided
    mean_U = nx * ny / 2.0
    sd_U = math.sqrt(nx * ny * (nx + ny + 1) / 12.0)
    z = (U - mean_U) / sd_U if sd_U > 0 else 0.0
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return U, z, p

U_mw, z_mw, p_mw = mann_whitney_u(muq_dens, nmq_dens)
print(f"   muq mean = {statistics.mean(muq_dens):.4f}; non-muq mean = {statistics.mean(nmq_dens):.4f}", file=sys.stderr)
print(f"   Mann-Whitney U = {U_mw:.1f} z = {z_mw:+.3f} p = {p_mw:.4e}", file=sys.stderr)

# ---------- Build JSON output ----------
out = {
    'meta': {
        'id': 'H-NEW-71',
        'date': '2026-04-15',
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': BON_K,
        'alpha_bon': ALPHA_BON,
        'rules_tuple': '(no-tashkeel; word-token match of {الله, لله, اللهم, آلله} + locked proclitic prefixes; hafs-kufan; canonical-114; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)',
    },
    'corpus_stats': {
        'n_surahs': len(corpus),
        'n_verses': TOTAL_VERSES,
        'n_total_words': TOTAL_WORDS,
        'n_allah_tokens': N_ALLAH,
        'n_allah_bearing_verses': len([k for k, v in verse_allah_count.items() if v > 0]),
        'allah_per_word_overall': N_ALLAH / TOTAL_WORDS,
        'form_distribution': dict(form_counter),
        'edge_cases_excluded': edge_check,
    },
    'cell_1_per_surah_table': surah_table,
    'cell_1_mw5_q1_pass': mw5_q1_ok,
    'cell_1_q1_count': q1_count,
    'cell_2_zero_allah_surahs': {
        'observed_zero_count': len(zero_allah_surahs),
        'observed_zero_surahs': [(s['sid'], s['translit'], s['n_verses'], s['n_words'], s['noldeke_phase']) for s in zero_allah_surahs],
        'expected_zero_count_uniform_null': expected_zero_count,
        'p_uniform_null_two_sided': p_uniform_zero,
        'pass_at_alpha_bon': p_uniform_zero < ALPHA_BON,
        'sim_zero_count_mean': statistics.mean(sim_zero_counts),
        'sim_zero_count_sd': statistics.stdev(sim_zero_counts) if len(sim_zero_counts) > 1 else 0,
    },
    'cell_3_verse_position': {
        'observed': dict(pos_counter),
        'expected': {'OPEN': exp_open, 'MID': exp_mid, 'CLOSE': exp_close},
        'chi2': chi2,
        'df': df,
        'p': p_chi2_pos,
        'pass_at_alpha_bon': p_chi2_pos < ALPHA_BON,
    },
    'cell_3a_fasila_exact': {
        'observed': fasila_exact_count,
        'expected_uniform': exp_fasila,
        'sd_uniform': sd_fasila,
        'z': z_fasila,
        'p_two_sided': p_fasila,
        'fraction_at_fasila': fasila_exact_count / N_ALLAH,
    },
    'cell_4_surah_position': {
        'observed': dict(s_pos_counter),
        'expected': {'S_OPEN': exp_s_open, 'S_MID': exp_s_mid, 'S_CLOSE': exp_s_close},
        'chi2': chi2_s,
        'df': 2,
        'p': p_chi2_s,
        'pass_at_alpha_bon': p_chi2_s < ALPHA_BON,
    },
    'cell_5_density_crown_verses': {
        'top_30': top30_verses,
        'mw5_kursi_in_top50': mw5_kursi,
        'mw5_light_cluster_in_top100': mw5_light_cluster,
        'mw5_khawatim_in_top50': mw5_khawatim,
        'mw5_anchors_passed': mw5_passes,
        'mw5_pass': mw5_passes >= 2,
        'anchor_ranks': mw5_ranks,
    },
    'cell_6_surah_density': {
        'top_15': top15_surahs,
        'bottom_15': bottom15_surahs,
        'spearman_rho_density_vs_n_words': rho_words,
        'spearman_p_density_vs_n_words': p_words,
        'spearman_rho_density_vs_n_verses': rho_verses,
        'spearman_p_density_vs_n_verses': p_verses,
        'pass_at_alpha_bon': p_words < ALPHA_BON,
        'all_114_ranked': surah_ranked,
    },
    'cell_7_noldeke_kruskal_wallis': {
        'phase_summary': phase_summary,
        'phase_order': PHASE_ORDER,
        'H': H_kw,
        'df': df_kw,
        'p': p_kw,
        'pass_at_alpha_bon': p_kw < ALPHA_BON,
    },
    'cell_7a_muq_mannwhitney': {
        'muq_n': len(muq_dens),
        'nmq_n': len(nmq_dens),
        'muq_mean_density': statistics.mean(muq_dens),
        'nmq_mean_density': statistics.mean(nmq_dens),
        'muq_median_density': statistics.median(muq_dens),
        'nmq_median_density': statistics.median(nmq_dens),
        'U': U_mw,
        'z': z_mw,
        'p': p_mw,
        'pass_at_alpha_bon': p_mw < ALPHA_BON,
    },
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-71.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=str)
print(f"[H-NEW-71] Wrote {out_path}", file=sys.stderr)

# ---------- Console summary ----------
print()
print("=" * 70)
print("H-NEW-71 SUMMARY")
print("=" * 70)
print(f"Total Allah-tokens: {N_ALLAH}")
print(f"Allah-bearing verses: {len([k for k, v in verse_allah_count.items() if v > 0])}/{TOTAL_VERSES}")
print(f"Surahs with zero Allah: {len(zero_allah_surahs)}/114")
print(f"Cell 1 MW-5 (Q1 has Allah): {mw5_q1_ok}")
print(f"Cell 2 zero-surahs uniform p={p_uniform_zero:.4f} (obs={len(zero_allah_surahs)}, exp={expected_zero_count:.2f})")
print(f"Cell 3 verse-position: {dict(pos_counter)} chi^2={chi2:.2f} p={p_chi2_pos:.3e}")
print(f"Cell 3a fāṣila-exact: {fasila_exact_count}/{N_ALLAH} ({100*fasila_exact_count/N_ALLAH:.1f}%) z={z_fasila:+.2f} p={p_fasila:.3e}")
print(f"Cell 4 surah-position: {dict(s_pos_counter)} chi^2={chi2_s:.2f} p={p_chi2_s:.3e}")
print(f"Cell 5 MW-5 anchors: {mw5_passes}/3")
print(f"Cell 6 ρ(density, n_words) = {rho_words:+.3f} p={p_words:.3e}")
print(f"Cell 7 KW H = {H_kw:.2f} p={p_kw:.3e}")
print(f"Cell 7a muq z={z_mw:+.2f} p={p_mw:.3e}")
print()

print("ZERO-ALLAH SURAHS:")
for s in zero_allah_surahs:
    print(f"  Q {s['sid']:>3}  {s['translit']:<20}  v={s['n_verses']:>3} w={s['n_words']:>4} {s['noldeke_phase']}")
print()

print("TOP-10 HIGHEST-DENSITY SURAHS:")
for s in surah_ranked[:10]:
    print(f"  Q {s['sid']:>3}  {s['translit']:<20}  d_per_word={s['density_per_word']:.4f}  Allah={s['allah_count']:>3}  v={s['n_verses']:>3} w={s['n_words']:>4} {s['noldeke_phase']}")
print()

print("BOTTOM-10 LOWEST-DENSITY SURAHS (excluding zeros):")
nonzero_ranked = [s for s in surah_ranked if s['allah_count'] > 0]
for s in nonzero_ranked[-10:]:
    print(f"  Q {s['sid']:>3}  {s['translit']:<20}  d_per_word={s['density_per_word']:.5f}  Allah={s['allah_count']:>3}  v={s['n_verses']:>3} w={s['n_words']:>4} {s['noldeke_phase']}")
print()

print("TOP-15 DENSITY-CROWN VERSES:")
for v in top30_verses[:15]:
    print(f"  Q {v['sid']:>3}:{v['vid']:<3}  wc={v['wc']:>3}  Allah={v['n_allah']:>2}  d={v['density']:.3f}  {v['text_excerpt'][:80]}")
