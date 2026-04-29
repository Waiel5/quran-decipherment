#!/usr/bin/env python3
"""H-NEW-25 — Phonotactic consonant-trigram entropy vs matched Arabic.

Operationalizes al-Khalīl / Ibn Jinnī / al-Rummānī qualitative *talāʾum
al-ḥurūf* as a conditional-entropy + same-makhraj test. Quran vs matched
classical baselines. Lower H_3 = more predictable letter-order = more
phonotactic structure. Same-makhraj depression = articulatory dispersion.

Sub-tests (Bonferroni k=5, α_bon=0.01, threshold z < -2.326):
  (a) H_3 PRIMARY: Quran H_3 < baseline mean
  (b) H_2 bigram sanity: directionally same
  (c) H_4 quadgram + trend H_2 > H_3 > H_4
  (d) Shuffle-control: shuffled Quran must return to baseline
  (e) AL-KHALĪL SAME-MAKHRAJ depression test (verified 8-group partition
      per Kitāb al-ʿAyn, ed. Makhzūmī/Sāmarrāʾī 1980-85 vol.1 pp. 57-60)

Sub-test (e') EXPLORATORY (does NOT count toward Bonferroni k):
  (e') Same test under Ibn al-Jazarī 17-makhraj tajwīd scheme for
       partition-sensitivity sensitivity.

Rules: (no-tashkeel, rasm-consonant, hamza normalized to alif for H_n tests
       in (a)-(d); hamza+alif jointly in hawāʾiyya for (e) so normalization
       is lossless for sub-test (e)). 28-symbol alphabet. Seed 20260413.
"""
import json, math, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

AR_LETTER = re.compile(r'[\u0621-\u064A]')
# Rasm-level normalization: hamza variants → alif, ى → ي, ة → ه (word-boundary marker kept as separate letter ه)
# Keep 28-letter Arabic alphabet
NORMALIZE = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا',
    'ء': 'ا',  # hamza → alif (rasm-level)
    'ؤ': 'و', 'ئ': 'ي',
    'ى': 'ي', 'ة': 'ه',
}

def clean_consonants(text):
    out = []
    for ch in text:
        if AR_LETTER.match(ch):
            out.append(NORMALIZE.get(ch, ch))
    return ''.join(out)

# ---- Load Quran ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
quran_raw = []
for s in sorted(Q, key=lambda x: x['id']):
    for v in s['verses']:
        quran_raw.append(v['text'])
quran_str = clean_consonants(' '.join(quran_raw))
N_quran = len(quran_str)
print(f"Quran consonants: {N_quran}", file=sys.stderr)

# Derive alphabet from Quran (should be 28-29 after normalization)
alphabet_set = set(quran_str)
print(f"Quran alphabet size: {len(alphabet_set)}", file=sys.stderr)

# ---- Load baselines ----
BASELINE_FILES = {
    'bukhari': 'bukhari-noquran.txt',
    'jahiz': 'jahiz-hayawan.txt',
    'sira': 'sira-ibn-hisham.txt',
    'mutanabbi': 'mutanabbi-diwan.txt',
    'muallaqat_7': None,  # concatenated below
}

baseline_strs = {}
for name, fn in BASELINE_FILES.items():
    if name == 'muallaqat_7':
        parts = []
        for m in ['muallaqa-imru-al-qais.txt', 'muallaqa-antara.txt',
                  'muallaqa-amr-bin-kulthum.txt', 'muallaqa-harith.txt',
                  'muallaqa-labid.txt', 'muallaqa-tarafa.txt', 'muallaqa-zuhayr.txt']:
            p = ROOT / 'data/baseline-corpora/raw' / m
            if p.exists():
                parts.append(p.read_text(encoding='utf-8', errors='replace'))
        txt = '\n'.join(parts)
    else:
        p = ROOT / 'data/baseline-corpora/raw' / fn
        if not p.exists():
            print(f"missing: {fn}", file=sys.stderr)
            continue
        txt = p.read_text(encoding='utf-8', errors='replace')
    # Strip tashkeel
    txt = re.sub(r'[\u064B-\u065F\u0670]', '', txt)
    cleaned = clean_consonants(txt)
    baseline_strs[name] = cleaned
    print(f"{name}: {len(cleaned)} consonants", file=sys.stderr)

# ---- Conditional entropy H_n ----
def cond_entropy(text, n):
    """H(c_i | c_{i-n+1}...c_{i-1}) using add-one Laplace smoothing.
    For n=2: H(c | prev). For n=3: H(c | prev2, prev1).
    """
    if len(text) < n:
        return 0.0
    # Context of length (n-1) → next char
    context_to_next = defaultdict(Counter)
    for i in range(n - 1, len(text)):
        ctx = text[i - (n - 1):i]
        nxt = text[i]
        context_to_next[ctx][nxt] += 1
    # Full alphabet — use union of symbols in this text
    V = len(set(text))
    H = 0.0
    total_tokens = sum(sum(c.values()) for c in context_to_next.values())
    for ctx, counter in context_to_next.items():
        ctx_total = sum(counter.values()) + V  # add-one smoothing
        p_ctx = sum(counter.values()) / total_tokens
        h_ctx = 0
        for sym in set(text):
            count = counter.get(sym, 0)
            p = (count + 1) / ctx_total
            if p > 0:
                h_ctx -= p * math.log2(p)
        H += p_ctx * h_ctx
    return H

def bootstrap_H_sd(text, n, n_boot=100, block_size=1000):
    """Block bootstrap SD for H_n."""
    H_samples = []
    for _ in range(n_boot):
        # Randomly sample blocks with replacement
        n_blocks = len(text) // block_size
        resampled = []
        for _ in range(n_blocks):
            start = random.randint(0, len(text) - block_size)
            resampled.append(text[start:start + block_size])
        resampled_str = ''.join(resampled)
        H_samples.append(cond_entropy(resampled_str, n))
    if len(H_samples) < 2:
        return 0.0
    mean = sum(H_samples) / len(H_samples)
    sd = (sum((x - mean) ** 2 for x in H_samples) / (len(H_samples) - 1)) ** 0.5
    return sd

# ---- Compute for each corpus at multiple n ----
print("\n=== Computing H_2, H_3, H_4 per corpus ===", file=sys.stderr)
ns = [2, 3, 4]
# Subsample each baseline to the same length as Quran for fairness
def trim_or_pad(text, target):
    if len(text) >= target:
        # Sample random contiguous window
        start = random.randint(0, len(text) - target)
        return text[start:start + target]
    return text

results = {}
# Quran first
print(f"Quran (N={N_quran})", file=sys.stderr)
qr = {}
for n in ns:
    H = cond_entropy(quran_str, n)
    sd = bootstrap_H_sd(quran_str, n, n_boot=50, block_size=2000)
    qr[f'H_{n}'] = H
    qr[f'H_{n}_sd'] = sd
    print(f"  H_{n} = {H:.4f} ± {sd:.4f}", file=sys.stderr)
results['quran'] = qr

# Baselines trimmed to N_quran
for name, text in baseline_strs.items():
    trimmed = trim_or_pad(text, N_quran)
    print(f"{name} (N={len(trimmed)})", file=sys.stderr)
    row = {}
    for n in ns:
        H = cond_entropy(trimmed, n)
        sd = bootstrap_H_sd(trimmed, n, n_boot=50, block_size=2000)
        row[f'H_{n}'] = H
        row[f'H_{n}_sd'] = sd
        print(f"  H_{n} = {H:.4f} ± {sd:.4f}", file=sys.stderr)
    results[name] = row

# ---- Sub-test (a): H_3 primary ----
print("\n=== Sub-test (a): H_3 Quran vs baseline mean ===", file=sys.stderr)
baseline_names = [n for n in results if n != 'quran']
baseline_H3 = [results[bn]['H_3'] for bn in baseline_names]
base_mean_H3 = sum(baseline_H3) / len(baseline_H3)
base_sd_H3 = (sum((x - base_mean_H3) ** 2 for x in baseline_H3) / max(len(baseline_H3) - 1, 1)) ** 0.5
z_a = (results['quran']['H_3'] - base_mean_H3) / base_sd_H3 if base_sd_H3 > 0 else 0
from math import erf, sqrt
p_a = 0.5 * (1 + erf(z_a / sqrt(2)))  # one-sided LOWER
print(f"baseline H_3: mean={base_mean_H3:.4f}, sd={base_sd_H3:.4f}", file=sys.stderr)
print(f"Quran H_3: {results['quran']['H_3']:.4f}", file=sys.stderr)
print(f"z_a = {z_a:.3f}, one-sided p (lower) = {p_a:.5f}", file=sys.stderr)

# Also compute z against pooled baseline bootstrap distribution
# (H_3 bootstraps concatenated across baselines)
pooled_base_H3 = []
for bn in baseline_names:
    # Use bootstrap samples from this baseline
    trimmed = trim_or_pad(baseline_strs[bn], N_quran)
    for _ in range(30):
        n_blocks = len(trimmed) // 2000
        resampled = []
        for _ in range(n_blocks):
            start = random.randint(0, len(trimmed) - 2000)
            resampled.append(trimmed[start:start + 2000])
        pooled_base_H3.append(cond_entropy(''.join(resampled), 3))
pool_mean = sum(pooled_base_H3) / len(pooled_base_H3)
pool_sd = (sum((x - pool_mean) ** 2 for x in pooled_base_H3) / (len(pooled_base_H3) - 1)) ** 0.5
z_a_pool = (results['quran']['H_3'] - pool_mean) / pool_sd
p_a_pool = 0.5 * (1 + erf(z_a_pool / sqrt(2)))
print(f"pooled bootstrap baseline H_3 mean={pool_mean:.4f} sd={pool_sd:.4f}", file=sys.stderr)
print(f"z_a (pooled) = {z_a_pool:.3f}, p = {p_a_pool:.5f}", file=sys.stderr)

# ---- Sub-test (b): H_2 bigram sanity ----
print("\n=== Sub-test (b): H_2 sanity ===", file=sys.stderr)
base_H2 = [results[bn]['H_2'] for bn in baseline_names]
base_mean_H2 = sum(base_H2) / len(base_H2)
base_sd_H2 = (sum((x - base_mean_H2) ** 2 for x in base_H2) / max(len(base_H2) - 1, 1)) ** 0.5
z_b = (results['quran']['H_2'] - base_mean_H2) / base_sd_H2 if base_sd_H2 > 0 else 0
p_b = 0.5 * (1 + erf(z_b / sqrt(2)))
print(f"baseline H_2: mean={base_mean_H2:.4f}, sd={base_sd_H2:.4f}", file=sys.stderr)
print(f"Quran H_2: {results['quran']['H_2']:.4f}", file=sys.stderr)
print(f"z_b = {z_b:.3f}, p = {p_b:.5f}", file=sys.stderr)

# ---- Sub-test (c): H_4 + monotone trend ----
print("\n=== Sub-test (c): H_4 + trend ===", file=sys.stderr)
base_H4 = [results[bn]['H_4'] for bn in baseline_names]
base_mean_H4 = sum(base_H4) / len(base_H4)
base_sd_H4 = (sum((x - base_mean_H4) ** 2 for x in base_H4) / max(len(base_H4) - 1, 1)) ** 0.5
z_c = (results['quran']['H_4'] - base_mean_H4) / base_sd_H4 if base_sd_H4 > 0 else 0
p_c = 0.5 * (1 + erf(z_c / sqrt(2)))
print(f"baseline H_4: mean={base_mean_H4:.4f}, sd={base_sd_H4:.4f}", file=sys.stderr)
print(f"Quran H_4: {results['quran']['H_4']:.4f}", file=sys.stderr)
print(f"z_c = {z_c:.3f}, p = {p_c:.5f}", file=sys.stderr)

# Trend check: {H_2_delta, H_3_delta, H_4_delta} should be monotone decreasing
quran_deltas = [results['quran'][f'H_{n}'] - (sum(results[bn][f'H_{n}'] for bn in baseline_names) / len(baseline_names)) for n in ns]
print(f"Quran - baseline_mean deltas [H_2, H_3, H_4]: {[round(x, 4) for x in quran_deltas]}", file=sys.stderr)

# ---- Sub-test (d): shuffle control ----
print("\n=== Sub-test (d): shuffle control ===", file=sys.stderr)
shuffled = list(quran_str)
random.shuffle(shuffled)
shuffled_str = ''.join(shuffled)
H_3_shuf = cond_entropy(shuffled_str, 3)
print(f"shuffled Quran H_3 = {H_3_shuf:.4f}", file=sys.stderr)
z_d = (H_3_shuf - base_mean_H3) / base_sd_H3 if base_sd_H3 > 0 else 0
# Shuffle control PASSES if shuffled returns to or above baseline
# (must not remain below)
d_passes = H_3_shuf >= base_mean_H3 - base_sd_H3
print(f"shuffled z vs baseline: {z_d:.3f}", file=sys.stderr)
print(f"passes (shuffled ≥ baseline - 1sd): {d_passes}", file=sys.stderr)

# ---- Sub-test (e): al-Khalīl same-makhraj depression ----
# VERIFIED PARTITION per classical-scholar 2026-04-14
# Kitāb al-ʿAyn ed. Makhzūmī/Sāmarrāʾī Baghdad 1980-1985 vol.1 pp. 57-60
print("\n=== Sub-test (e): al-Khalīl 8-makhraj same-makhraj depression ===", file=sys.stderr)

AL_KHALIL_8 = {
    'halqiyya':   set('عحهخغقك'),       # throat: 7 letters, ʿayn-first
    'shajariyya': set('جشض'),            # palatal: ḍ is HERE per al-Khalīl
    'asaliyya':   set('صسز'),            # sibilant: ṣ is HERE (not niṭʿī)
    'nit_iyya':   set('طدت'),            # gum-ridge
    'lithawiyya': set('ظذث'),            # gums
    'dhalaqiyya': set('رلن'),            # tongue-tip
    'shafawiyya': set('فبم'),            # labial
    'hawaiyya':   set('ويءا'),           # air-cavity (hamza HERE per al-Khalīl)
}
# Verify 28-letter partition
_all = set()
for g, letters in AL_KHALIL_8.items():
    assert _all.isdisjoint(letters), f"overlap in al-Khalīl partition at {g}"
    _all |= letters
assert len(_all) == 28, f"al-Khalīl partition size {len(_all)} != 28 (got {sorted(_all)})"
print(f"al-Khalīl partition verified: 8 groups, {len(_all)} letters", file=sys.stderr)

# Build letter → group lookup
letter_to_khalil = {}
for g, letters in AL_KHALIL_8.items():
    for ch in letters:
        letter_to_khalil[ch] = g

# NOTE on rules-tuple: the main (a)-(d) pipeline normalizes hamza (ء) → alif (ا).
# For sub-test (e) specifically, ء and ا are both in hawāʾiyya per al-Khalīl's
# own reading, so normalization is lossless for same-makhraj detection.
# We use the SAME normalized quran_str for consistency with (a)-(d).

def same_makhraj_rate(text, letter_to_group):
    """Mean indicator S(i) = 1 if letters i and i+1 share a makhraj group."""
    n_pairs = 0
    n_same = 0
    for i in range(len(text) - 1):
        a, b = text[i], text[i+1]
        ga = letter_to_group.get(a)
        gb = letter_to_group.get(b)
        if ga is None or gb is None:
            continue
        n_pairs += 1
        if ga == gb:
            n_same += 1
    return n_same / n_pairs if n_pairs > 0 else 0.0, n_same, n_pairs

s_obs_khalil, n_same_q, n_pairs_q = same_makhraj_rate(quran_str, letter_to_khalil)
print(f"Quran same-makhraj rate (al-Khalīl): {s_obs_khalil:.5f} ({n_same_q}/{n_pairs_q})", file=sys.stderr)

# Multiset-preserving shuffle null (same approach as sub-test (d))
B_NULL = 500
null_s_khalil = []
shuf_buf = list(quran_str)
for b in range(B_NULL):
    random.shuffle(shuf_buf)
    s_null, _, _ = same_makhraj_rate(shuf_buf, letter_to_khalil)
    null_s_khalil.append(s_null)
null_mean_khalil = sum(null_s_khalil) / len(null_s_khalil)
null_sd_khalil = (sum((x - null_mean_khalil) ** 2 for x in null_s_khalil) / (len(null_s_khalil) - 1)) ** 0.5
z_e_khalil = (s_obs_khalil - null_mean_khalil) / null_sd_khalil if null_sd_khalil > 0 else 0
p_e_khalil = 0.5 * (1 + erf(z_e_khalil / sqrt(2)))  # one-sided LOWER
print(f"null mean={null_mean_khalil:.5f}, sd={null_sd_khalil:.5f}", file=sys.stderr)
print(f"z_e (al-Khalīl 8) = {z_e_khalil:.3f}, one-sided p (lower) = {p_e_khalil:.5f}", file=sys.stderr)

# ---- Sub-test (e'): Ibn al-Jazarī 17-makhraj — EXPLORATORY sensitivity cell ----
# From al-Muqaddima al-Jazariyya (Ibn al-Jazarī d. 833/1429). Tajwīd-canonical 17-point scheme.
# Groups by articulation point (not al-Khalīl's articulatory class).
# This is finer-grained than al-Khalīl's 8-group scheme (more cells → fewer same-group pairs expected).
print("\n=== Sub-test (e'): Ibn al-Jazarī 17-makhraj (EXPLORATORY, not in Bonferroni k) ===", file=sys.stderr)

JAZARI_17 = {
    'jawf':         set('واي'),           # 1. jawf (air-cavity): madd letters
    'aqsa_lisan_q': set('ق'),              # 2. aqṣā al-lisān (far tongue) + qāf alone
    'aqsa_lisan_k': set('ك'),              # 3. aqṣā al-lisān + kāf alone
    'wasat_lisan':  set('جشي'),            # 4. wasaṭ al-lisān (middle) — yāʾ-non-madd here; we map ي jointly since our text conflates
    'hafat_lisan_d': set('ض'),             # 5. ḥāfat al-lisān (tongue-edge) — ḍād
    'hafat_lisan_l': set('ل'),             # 6. ḥāfat al-lisān — lām
    'taraf_lisan_n': set('ن'),             # 7. ṭaraf al-lisān (tongue-tip) — nūn
    'taraf_lisan_r': set('ر'),             # 8. ṭaraf al-lisān — rāʾ
    'nit_jazari':   set('طدت'),            # 9. niṭʿ — ṭ/d/t
    'lithah':       set('ظذث'),            # 10. lithah — ẓ/dh/th
    'asalah':       set('صسز'),            # 11. asalat al-lisān — ṣ/s/z
    'shafatan_f':   set('ف'),              # 12. shafatān (lip+teeth) — fāʾ
    'shafatan_bmw': set('بمو'),            # 13. shafatān — bāʾ/mīm/wāw (three-way lip cluster)
    'halq_deep':    set('ءه'),             # 14. aqṣā al-ḥalq — hamza/hāʾ
    'halq_mid':     set('عح'),             # 15. wasaṭ al-ḥalq — ʿayn/ḥāʾ
    'halq_up':      set('غخ'),             # 16. adnā al-ḥalq — ghayn/khāʾ
    'khaishum':     set(),                 # 17. khaishūm (nasal cavity) — positional, not a letter-identity group; skip
}
# Verify 28-letter coverage (khaishum contributes no letter-identity)
_all_j = set()
for g, letters in JAZARI_17.items():
    _all_j |= letters
# wāw/yāʾ appear in multiple groups (madd and non-madd); since we can't distinguish
# madd vs non-madd without tashkeel, we use the union and assign each letter to its
# first-listed group for the partition purpose:
# ا→jawf, و→jawf, ي→wasat_lisan (since non-madd yāʾ is more common in roots),
# then override with explicit first-group rule below.
letter_to_jazari = {}
# Process groups in order; first group wins
order = ['jawf', 'aqsa_lisan_q', 'aqsa_lisan_k', 'wasat_lisan', 'hafat_lisan_d', 'hafat_lisan_l',
        'taraf_lisan_n', 'taraf_lisan_r', 'nit_jazari', 'lithah', 'asalah',
        'shafatan_f', 'shafatan_bmw', 'halq_deep', 'halq_mid', 'halq_up']
for g in order:
    for ch in JAZARI_17[g]:
        if ch not in letter_to_jazari:
            letter_to_jazari[ch] = g

# Verify 28-letter coverage
covered = set(letter_to_jazari.keys())
missing = _all - covered  # letters in al-Khalīl partition not covered by Jazarī mapping
if missing:
    print(f"WARNING: Jazarī partition missing letters: {sorted(missing)}", file=sys.stderr)
# Expected: should have all 28 since we assigned all from the 16 non-khaishūm groups
print(f"Jazarī partition: {len(set(letter_to_jazari.values()))} groups active, {len(covered)} letters covered", file=sys.stderr)

s_obs_jazari, n_same_j, n_pairs_j = same_makhraj_rate(quran_str, letter_to_jazari)
print(f"Quran same-makhraj rate (Jazarī 17): {s_obs_jazari:.5f} ({n_same_j}/{n_pairs_j})", file=sys.stderr)

null_s_jazari = []
for b in range(B_NULL):
    random.shuffle(shuf_buf)
    s_null, _, _ = same_makhraj_rate(shuf_buf, letter_to_jazari)
    null_s_jazari.append(s_null)
null_mean_jazari = sum(null_s_jazari) / len(null_s_jazari)
null_sd_jazari = (sum((x - null_mean_jazari) ** 2 for x in null_s_jazari) / (len(null_s_jazari) - 1)) ** 0.5
z_e_jazari = (s_obs_jazari - null_mean_jazari) / null_sd_jazari if null_sd_jazari > 0 else 0
p_e_jazari = 0.5 * (1 + erf(z_e_jazari / sqrt(2)))
print(f"null mean={null_mean_jazari:.5f}, sd={null_sd_jazari:.5f}", file=sys.stderr)
print(f"z_e' (Jazarī 17) = {z_e_jazari:.3f}, one-sided p (lower) = {p_e_jazari:.5f}", file=sys.stderr)

# ---- Verdicts ----
# Bonferroni k=5 (updated from k=4 to include sub-test (e) al-Khalīl primary)
ALPHA_BON = 0.01
THRESH = -2.326  # one-sided α=0.01
a_pass = z_a < THRESH
b_pass = z_b < THRESH
c_pass = z_c < THRESH and all(quran_deltas[i] >= quran_deltas[i+1] for i in range(len(quran_deltas)-1))
e_pass = z_e_khalil < THRESH  # al-Khalīl 8-makhraj PRIMARY
e_prime_pass = z_e_jazari < THRESH  # Jazarī 17-makhraj exploratory sensitivity
joint = a_pass and b_pass and c_pass and d_passes and e_pass

# Partition-sensitivity interpretation (pre-locked 2026-04-14)
if e_pass and e_prime_pass:
    partition_sensitivity = 'ROBUST — signal present in both al-Khalīl 8 and Jazarī 17'
elif e_pass and not e_prime_pass:
    partition_sensitivity = 'PARTITION-SENSITIVE — al-Khalīl only, Jazarī fails (flag)'
elif not e_pass and e_prime_pass:
    partition_sensitivity = 'INVERTED — Jazarī only, al-Khalīl fails (consult classical-scholar)'
else:
    partition_sensitivity = 'NO-SIGNAL — neither partition detects depression'

print("\n=== Verdicts ===", file=sys.stderr)
print(f"(a) H_3 primary:       z={z_a:.3f} vs thresh {THRESH}: {'PASS' if a_pass else 'FAIL'}", file=sys.stderr)
print(f"(b) H_2 sanity:        z={z_b:.3f}: {'PASS' if b_pass else 'FAIL'}", file=sys.stderr)
print(f"(c) H_4 + trend:       z={z_c:.3f}, trend={'monotone' if all(quran_deltas[i] >= quran_deltas[i+1] for i in range(len(quran_deltas)-1)) else 'non-monotone'}: {'PASS' if c_pass else 'FAIL'}", file=sys.stderr)
print(f"(d) shuffle recover:   {'PASS' if d_passes else 'FAIL'}", file=sys.stderr)
print(f"(e) al-Khalīl 8:       z={z_e_khalil:.3f}: {'PASS' if e_pass else 'FAIL'} [PRIMARY, in Bonferroni k=5]", file=sys.stderr)
print(f"(e') Jazarī 17:        z={z_e_jazari:.3f}: {'PASS' if e_prime_pass else 'FAIL'} [EXPLORATORY, not in k]", file=sys.stderr)
print(f"Partition sensitivity: {partition_sensitivity}", file=sys.stderr)
print(f"JOINT (a∧b∧c∧d∧e): {'PASS' if joint else 'FAIL'}", file=sys.stderr)

# ---- Output ----
out = {
    'seed': 20260413,
    'hypothesis': 'H-NEW-25 consonant-trigram entropy — al-Khalīl talāʾum al-ḥurūf',
    'rules_tuple': 'no-tashkeel, rasm-consonant, hamza→alif, 28-letter',
    'alphabet_size': len(alphabet_set),
    'N_quran': N_quran,
    'baseline_sources': list(baseline_strs.keys()),
    'results_by_corpus': results,
    'sub_a_H3_primary': {
        'quran_H3': results['quran']['H_3'],
        'baseline_mean_H3': base_mean_H3,
        'baseline_sd_H3': base_sd_H3,
        'z': z_a,
        'p_one_sided': p_a,
        'pooled_bootstrap_z': z_a_pool,
        'pooled_bootstrap_p': p_a_pool,
        'threshold': THRESH_A,
        'pass': a_pass,
    },
    'sub_b_H2_sanity': {
        'quran_H2': results['quran']['H_2'],
        'baseline_mean_H2': base_mean_H2,
        'baseline_sd_H2': base_sd_H2,
        'z': z_b,
        'p': p_b,
        'pass': b_pass,
    },
    'sub_c_H4_and_trend': {
        'quran_H4': results['quran']['H_4'],
        'baseline_mean_H4': base_mean_H4,
        'baseline_sd_H4': base_sd_H4,
        'z': z_c,
        'p': p_c,
        'quran_deltas_H2_H3_H4': quran_deltas,
        'pass': c_pass,
    },
    'sub_d_shuffle': {
        'shuffled_H3': H_3_shuf,
        'z': z_d,
        'pass': d_passes,
    },
    'sub_e_al_khalil_8_makhraj': {
        'partition_source': 'Kitāb al-ʿAyn, ed. Makhzūmī/Sāmarrāʾī Baghdad 1980-1985 vol.1 pp. 57-60 (VERIFIED by classical-scholar 2026-04-14)',
        'partition': {g: ''.join(sorted(letters)) for g, letters in AL_KHALIL_8.items()},
        'partition_size': 8,
        'quran_same_makhraj_rate': s_obs_khalil,
        'null_mean': null_mean_khalil,
        'null_sd': null_sd_khalil,
        'n_null_draws': B_NULL,
        'z': z_e_khalil,
        'p_one_sided': p_e_khalil,
        'threshold': THRESH,
        'pass': e_pass,
        'role': 'PRIMARY — counts toward Bonferroni k=5',
    },
    'sub_e_prime_jazari_17_makhraj': {
        'partition_source': 'al-Muqaddima al-Jazariyya (Ibn al-Jazarī d. 833/1429), tajwīd-canonical 17-makhraj',
        'partition_size': len(set(letter_to_jazari.values())),
        'quran_same_makhraj_rate': s_obs_jazari,
        'null_mean': null_mean_jazari,
        'null_sd': null_sd_jazari,
        'n_null_draws': B_NULL,
        'z': z_e_jazari,
        'p_one_sided': p_e_jazari,
        'threshold': THRESH,
        'pass': e_prime_pass,
        'role': 'EXPLORATORY — sensitivity cell, NOT in Bonferroni k',
    },
    'partition_sensitivity': partition_sensitivity,
    'joint_pass': joint,
    'bonferroni_k': 5,
    'alpha_bon': ALPHA_BON,
    'threshold': THRESH,
}
out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-25.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
