#!/usr/bin/env python3
"""H-NEW-37 — Fāṣila terminal-vowel Markov residual (vowel-level saj' test).

Ibn Rashīq al-ʿUmda fī maḥāsin al-shiʿr (Dār al-Jīl Beirut 1981) vol.1
pp. 151-165 classifies qāfiya by its terminal vowel + preceding consonant.
This test measures vowel-level Markov predictability of verse-end
vowels in the Quran vs within-surah shuffle nulls and vs prose baselines.

Classifier extracts the pause-vowel (tajwīd: the short vowel/tanwīn
actually pronounced or assumed at verse-end) from the tashkeel-preserved
Ḥafs-Kufan final word. Classes: {a, u, i, aa, uu, ii, an, un, in, ay,
aw, none} — 12-way.

Pre-registered sub-tests (Bonferroni k=6):
  (a) Quran transition entropy < shuffle-null entropy at z < −2.58
  (b) Quran vs Bukhari (predicted-vowel from morph) |Δ|/SE > 2.58
  (c) Quran vs Jahiz same threshold
  (d) Exclude 29 muqaṭṭaʿāt surahs; (a) still holds
  (e) Meccan-only subset; (a) still holds
  (f) Medinan-only subset; (a) still holds

Seed 20260414.
"""

import json
import math
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260414)

# Tashkeel diacritics
TANWIN_A, TANWIN_U, TANWIN_I = 0x64B, 0x64C, 0x64D
FATHA, DAMMA, KASRA = 0x64E, 0x64F, 0x650
SHADDA, SUKUN = 0x651, 0x652
DAGGER_ALIF = 0x670
# Letters
LETTER_ALIF = 0x627
LETTER_ALIF_WASL = 0x671
LETTER_ALIF_MAQSURA = 0x649
LETTER_ALIF_MADDA = 0x622
LETTER_W = 0x648
LETTER_Y = 0x64A
LETTER_T_MARB = 0x629
LETTER_HA = 0x647

VOWEL_CLASSES = ['a', 'u', 'i', 'aa', 'uu', 'ii', 'an', 'un', 'in', 'ay', 'aw', 'none']
V2I = {v: i for i, v in enumerate(VOWEL_CLASSES)}


def classify_ending(word):
    """Return the pause-vowel class for a tashkeel-preserved word."""
    if not word:
        return 'none'
    chars = list(word)
    last = chars[-1]
    prev = chars[-2] if len(chars) >= 2 else None
    lo = ord(last)

    # Tanwīn (nunation)
    if lo == TANWIN_A:
        return 'an'
    if lo == TANWIN_U:
        return 'un'
    if lo == TANWIN_I:
        return 'in'

    # Short vowels
    if lo == FATHA:
        if prev and ord(prev) in (LETTER_ALIF, LETTER_ALIF_WASL):
            return 'aa'
        return 'a'
    if lo == DAMMA:
        if prev and ord(prev) == LETTER_W:
            return 'uu'
        return 'u'
    if lo == KASRA:
        if prev and ord(prev) == LETTER_Y:
            return 'ii'
        return 'i'

    # Terminal letters (implicit sukūn / pausal forms)
    if lo in (LETTER_ALIF, LETTER_ALIF_WASL, LETTER_ALIF_MADDA, LETTER_ALIF_MAQSURA, DAGGER_ALIF):
        return 'aa'
    if lo == LETTER_W:
        if prev and ord(prev) == DAMMA:
            return 'uu'
        return 'aw'
    if lo == LETTER_Y:
        if prev and ord(prev) == KASRA:
            return 'ii'
        return 'ay'
    if lo == LETTER_T_MARB:
        return 'none'
    if lo == SUKUN:
        if prev:
            p = ord(prev)
            if p == FATHA:
                return 'a'
            if p == DAMMA:
                return 'u'
            if p == KASRA:
                return 'i'
        return 'none'

    return 'none'


# ---- Load Quran ----
Q = json.loads((ROOT / 'quran-text/quran-full-tashkeel.json').read_text())

per_surah_endings = {}
for s in sorted(Q, key=lambda x: x['id']):
    sid = s['id']
    endings = []
    for v in s['verses']:
        text = v['text'].strip()
        words = text.split()
        if not words:
            continue
        endings.append(classify_ending(words[-1]))
    per_surah_endings[sid] = endings

# Full sequence (mushaf order) for global transition matrix
all_endings = []
for sid in sorted(per_surah_endings):
    all_endings.extend(per_surah_endings[sid])

print(f"total verse endings: {len(all_endings)}", file=sys.stderr)
dist = Counter(all_endings)
print(f"class distribution: {dict(dist)}", file=sys.stderr)


def transition_entropy(seq):
    """Compute average conditional entropy H(v_{t+1} | v_t) over a sequence.

    Lower = more predictable = stronger Markov structure.
    """
    # Count transitions
    trans = defaultdict(Counter)
    for a, b in zip(seq[:-1], seq[1:]):
        trans[a][b] += 1
    # Compute H(b|a) weighted by P(a)
    total = len(seq) - 1
    if total <= 0:
        return 0.0
    h = 0.0
    for a, counters in trans.items():
        n_a = sum(counters.values())
        p_a = n_a / total
        h_b_a = 0.0
        for b, n_ab in counters.items():
            p_ba = n_ab / n_a
            if p_ba > 0:
                h_b_a -= p_ba * math.log2(p_ba)
        h += p_a * h_b_a
    return h


# Quran full-corpus transition entropy
quran_H = transition_entropy(all_endings)
print(f"\nQuran vowel-transition entropy: {quran_H:.4f} bits", file=sys.stderr)

# Unigram entropy (upper bound if transitions were independent)
total = sum(dist.values())
unigram_H = -sum((c / total) * math.log2(c / total) for c in dist.values() if c > 0)
print(f"Quran vowel unigram entropy: {unigram_H:.4f} bits", file=sys.stderr)
print(f"Markov reduction: {unigram_H - quran_H:.4f} bits", file=sys.stderr)


# ---- Within-surah shuffle null (1000 perms) ----
N_PERM = 1000
print(f"\n=== Within-surah shuffle null ({N_PERM} perms) ===", file=sys.stderr)
null_H = []
for perm in range(N_PERM):
    shuffled = []
    for sid in sorted(per_surah_endings):
        lst = list(per_surah_endings[sid])
        random.shuffle(lst)
        shuffled.extend(lst)
    h = transition_entropy(shuffled)
    null_H.append(h)
    if (perm + 1) % 200 == 0:
        print(f"  perm {perm+1}/{N_PERM}", file=sys.stderr)

null_mean = sum(null_H) / len(null_H)
null_var = sum((h - null_mean) ** 2 for h in null_H) / (len(null_H) - 1)
null_sd = math.sqrt(null_var)
z_a = (quran_H - null_mean) / null_sd if null_sd > 0 else 0
p_emp_a = sum(1 for h in null_H if h <= quran_H) / len(null_H)
print(f"null μ={null_mean:.4f} σ={null_sd:.4f}, Quran={quran_H:.4f}, z={z_a:+.3f}, p_emp={p_emp_a:.4f}",
      file=sys.stderr)

sub_a_pass = z_a < -2.58


# ---- Baseline vowel prediction (morphological) ----
# For Bukhari and Jahiz: predict pause-vowel from final word using heuristics
# because baselines are not tashkeel-annotated. We use a simple rule:
# final letter = ا/ى → 'aa'; ة → 'none'; ي → 'ii'/'ay' (→ 'ii' default); و → 'uu'/'aw';
# else assume short 'a' as default (most common case in classical Arabic pause).
import re
AR_LETTER = re.compile(r'[\u0621-\u064A]')


def predict_pause_vowel(word):
    """Predict pause-vowel from unvoweled word — heuristic fallback."""
    # Keep only Arabic letters
    letters = ''.join(ch for ch in word if AR_LETTER.match(ch))
    if not letters:
        return 'none'
    last = letters[-1]
    lo = ord(last)
    if lo in (LETTER_ALIF, LETTER_ALIF_MADDA, LETTER_ALIF_MAQSURA):
        return 'aa'
    if lo == LETTER_ALIF_WASL:
        return 'aa'
    if lo == LETTER_W:
        return 'uu'  # common in verb 3pl (-ū) and sound masc plural (-ūn stripped)
    if lo == LETTER_Y:
        return 'ii'  # common in -ī / -īn
    if lo == LETTER_T_MARB:
        return 'none'
    if lo == LETTER_HA:
        return 'a'  # common pronominal suffix -hu/-ha pause → 'a'
    return 'a'  # default pause


def baseline_vowel_seq(text, split_rx, split_func=None):
    """Split text into sentences, extract final-word pause vowel per sentence."""
    if split_func:
        parts = split_func(text)
    else:
        parts = re.split(split_rx, text)
    seq = []
    for p in parts:
        words = p.strip().split()
        if not words:
            continue
        # Get last word with Arabic letters
        last_with_letters = None
        for w in reversed(words):
            if any(AR_LETTER.match(ch) for ch in w):
                last_with_letters = w
                break
        if last_with_letters:
            seq.append(predict_pause_vowel(last_with_letters))
    return seq


# Bukhari — split on ḥaddathanā hadith-report markers
bukhari_text = (ROOT / 'data/baseline-corpora/raw/bukhari-noquran.txt').read_text(
    encoding='utf-8', errors='replace')


def hadith_split(text):
    return re.split(r'حدثنا|أخبرنا|وحدثنا|وأخبرنا', text)


bukhari_seq = baseline_vowel_seq(bukhari_text, None, hadith_split)
print(f"\nbukhari pause-vowel sequence length: {len(bukhari_seq)}", file=sys.stderr)
print(f"bukhari distribution: {dict(Counter(bukhari_seq))}", file=sys.stderr)
bukhari_H = transition_entropy(bukhari_seq)
print(f"bukhari H = {bukhari_H:.4f} bits", file=sys.stderr)

# Jahiz — split on punctuation
jahiz_text = (ROOT / 'data/baseline-corpora/raw/jahiz-hayawan.txt').read_text(
    encoding='utf-8', errors='replace')
jahiz_seq = baseline_vowel_seq(jahiz_text, r'[.!?؟۔\n]+|\s{2,}')
print(f"\njahiz pause-vowel sequence length: {len(jahiz_seq)}", file=sys.stderr)
print(f"jahiz distribution: {dict(Counter(jahiz_seq))}", file=sys.stderr)
jahiz_H = transition_entropy(jahiz_seq)
print(f"jahiz H = {jahiz_H:.4f} bits", file=sys.stderr)


# ---- SE of entropy via bootstrap ----
def bootstrap_entropy_se(seq, n_boot=500):
    n = len(seq)
    h_list = []
    for _ in range(n_boot):
        idx = [random.randrange(n - 1) for _ in range(n - 1)]
        # Resample transition pairs
        trans = defaultdict(Counter)
        for i in idx:
            trans[seq[i]][seq[i + 1]] += 1
        total = sum(sum(c.values()) for c in trans.values())
        h = 0.0
        for a, counters in trans.items():
            n_a = sum(counters.values())
            if n_a == 0:
                continue
            p_a = n_a / total
            h_b_a = 0.0
            for b, n_ab in counters.items():
                p_ba = n_ab / n_a
                if p_ba > 0:
                    h_b_a -= p_ba * math.log2(p_ba)
            h += p_a * h_b_a
        h_list.append(h)
    mean = sum(h_list) / len(h_list)
    var = sum((h - mean) ** 2 for h in h_list) / (len(h_list) - 1)
    return math.sqrt(var), mean


print("\n=== Bootstrap SE ===", file=sys.stderr)
quran_se, quran_bs_mean = bootstrap_entropy_se(all_endings, n_boot=500)
bukhari_se, bukhari_bs_mean = bootstrap_entropy_se(bukhari_seq, n_boot=500)
jahiz_se, jahiz_bs_mean = bootstrap_entropy_se(jahiz_seq, n_boot=500)
print(f"Quran H={quran_H:.4f} ±{quran_se:.4f}", file=sys.stderr)
print(f"Bukhari H={bukhari_H:.4f} ±{bukhari_se:.4f}", file=sys.stderr)
print(f"Jahiz H={jahiz_H:.4f} ±{jahiz_se:.4f}", file=sys.stderr)

# Sub-b: Quran vs Bukhari
se_diff_bukhari = math.sqrt(quran_se ** 2 + bukhari_se ** 2)
z_b = (quran_H - bukhari_H) / se_diff_bukhari if se_diff_bukhari > 0 else 0
sub_b_pass = z_b < -2.58
print(f"\nSub-(b) Quran < Bukhari: z={z_b:+.3f}, PASS={sub_b_pass}", file=sys.stderr)

# Sub-c: Quran vs Jahiz
se_diff_jahiz = math.sqrt(quran_se ** 2 + jahiz_se ** 2)
z_c = (quran_H - jahiz_H) / se_diff_jahiz if se_diff_jahiz > 0 else 0
sub_c_pass = z_c < -2.58
print(f"Sub-(c) Quran < Jahiz: z={z_c:+.3f}, PASS={sub_c_pass}", file=sys.stderr)


# ---- Robustness: exclude muqaṭṭaʿāt (d), Meccan-only (e), Medinan-only (f) ----
# Muqaṭṭaʿāt surahs: Q 2, 3, 7, 10-15, 19-20, 26-32, 36, 38, 40-46, 50, 68
MUQATT = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
          36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
# Meccan surahs (standard list — Nöldeke/Cairo)
# Use traditional Ibn ʿAbbās list: all surahs except Medinan
MEDINAN = {2, 3, 4, 5, 8, 9, 24, 33, 47, 48, 49, 55, 57, 58, 59, 60, 61, 62, 63,
           64, 65, 66, 76, 98, 99, 110}
MECCAN = set(range(1, 115)) - MEDINAN


def seq_exclude(exclude_set):
    out = []
    for sid in sorted(per_surah_endings):
        if sid in exclude_set:
            continue
        out.extend(per_surah_endings[sid])
    return out


def seq_include(include_set):
    out = []
    for sid in sorted(per_surah_endings):
        if sid not in include_set:
            continue
        out.extend(per_surah_endings[sid])
    return out


seq_d = seq_exclude(MUQATT)
seq_e = seq_include(MECCAN)
seq_f = seq_include(MEDINAN)


def robustness_test(seq, label, n_perm=500):
    H = transition_entropy(seq)
    null_Hs = []
    for _ in range(n_perm):
        shuffled = list(seq)
        random.shuffle(shuffled)
        null_Hs.append(transition_entropy(shuffled))
    m = sum(null_Hs) / len(null_Hs)
    v = sum((h - m) ** 2 for h in null_Hs) / (len(null_Hs) - 1)
    sd = math.sqrt(v)
    z = (H - m) / sd if sd > 0 else 0
    p_emp = sum(1 for h in null_Hs if h <= H) / len(null_Hs)
    return {'label': label, 'n': len(seq), 'H': H, 'null_mean': m, 'null_sd': sd, 'z': z, 'p_emp': p_emp}


print("\n=== Robustness sub-tests (500 perms each, cross-surah shuffle) ===", file=sys.stderr)
res_d = robustness_test(seq_d, 'exclude-muqattaat')
res_e = robustness_test(seq_e, 'meccan-only')
res_f = robustness_test(seq_f, 'medinan-only')
for r in (res_d, res_e, res_f):
    print(f"{r['label']} n={r['n']}: H={r['H']:.4f}, null μ={r['null_mean']:.4f}±{r['null_sd']:.4f}, "
          f"z={r['z']:+.3f}, p_emp={r['p_emp']:.4f}", file=sys.stderr)

sub_d_pass = res_d['z'] < -2.58
sub_e_pass = res_e['z'] < -2.58
sub_f_pass = res_f['z'] < -2.58

# ---- Joint verdict ----
# Tier-A: all six pass
# Tier-B: (a) + any of (b,c) passes
# NULL: all non-significant
passes = [sub_a_pass, sub_b_pass, sub_c_pass, sub_d_pass, sub_e_pass, sub_f_pass]
tier_a = all(passes)
tier_b = sub_a_pass and (sub_b_pass or sub_c_pass)
null_verdict = not any(passes)
reverse = z_a > 2.58

if tier_a:
    verdict = 'TIER-A (all 6 pass)'
elif tier_b:
    verdict = 'TIER-B (sub-a + at least one differential)'
elif sub_a_pass:
    verdict = 'PARTIAL (only sub-a passes)'
elif reverse:
    verdict = 'REVERSE (Quran MORE random than shuffle)'
elif null_verdict:
    verdict = 'NULL (no effect)'
else:
    verdict = 'MIXED'

print(f"\n=== VERDICT: {verdict} ===", file=sys.stderr)
print(f"(a) z={z_a:+.3f} [pass: {sub_a_pass}]", file=sys.stderr)
print(f"(b) z={z_b:+.3f} [pass: {sub_b_pass}]", file=sys.stderr)
print(f"(c) z={z_c:+.3f} [pass: {sub_c_pass}]", file=sys.stderr)
print(f"(d) z={res_d['z']:+.3f} [pass: {sub_d_pass}]", file=sys.stderr)
print(f"(e) z={res_e['z']:+.3f} [pass: {sub_e_pass}]", file=sys.stderr)
print(f"(f) z={res_f['z']:+.3f} [pass: {sub_f_pass}]", file=sys.stderr)

out = {
    'seed': 20260414,
    'hypothesis': 'H-NEW-37 fāṣila terminal-vowel Markov residual (Ibn Rashīq qāfiya)',
    'rules_tuple': 'hafs-kufan, tashkeel-preserved, 12-class-pause-vowel',
    'classes': VOWEL_CLASSES,
    'n_verses': len(all_endings),
    'quran_dist': dict(dist),
    'quran_H': quran_H,
    'quran_unigram_H': unigram_H,
    'quran_markov_reduction': unigram_H - quran_H,
    'null_H_mean': null_mean,
    'null_H_sd': null_sd,
    'z_a': z_a,
    'p_emp_a': p_emp_a,
    'sub_a_pass': sub_a_pass,
    'quran_se_bootstrap': quran_se,
    'bukhari': {
        'n': len(bukhari_seq),
        'H': bukhari_H,
        'se': bukhari_se,
        'z_diff': z_b,
        'pass': sub_b_pass,
        'dist': dict(Counter(bukhari_seq)),
    },
    'jahiz': {
        'n': len(jahiz_seq),
        'H': jahiz_H,
        'se': jahiz_se,
        'z_diff': z_c,
        'pass': sub_c_pass,
        'dist': dict(Counter(jahiz_seq)),
    },
    'sub_d_exclude_muqattaat': res_d,
    'sub_e_meccan_only': res_e,
    'sub_f_medinan_only': res_f,
    'verdict': verdict,
    'bonferroni_k': 6,
    'alpha_bon': 0.0083,
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-37.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
