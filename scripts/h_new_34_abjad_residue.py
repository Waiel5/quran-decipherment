#!/usr/bin/env python3
"""H-NEW-34 — Verse-final abjad-sum modular-residue clustering.

Pre-registered NULL test of ḥisāb al-jummal claim (Ibn ʿArabī / al-Bisṭāmī).
For each of 6236 Quran verses, compute the mashriqi abjad sum of the LAST
WORD. For m ∈ {7, 11, 19}, build the residue distribution and compute χ²
vs uniform expectation of N/m per bin.

Compare Quran χ² to null distribution from 1000 random same-length samples
of each baseline corpus (Bukhari-noquran, Jahiz-hayawan). Pre-registered
prediction: NULL (Quran χ² ≤ baseline 95th pct for all three m).

Bonferroni k=3; per-test α=0.0167.

Seed 20260414.
"""

import json
import math
import random
import re
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260414)

# Mashriqi abjad table (letters -> values)
ABJAD = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10,
    'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90,
    'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700,
    'ض': 800, 'ظ': 900, 'غ': 1000,
}
# Hamza carrier policy: hamza on alif/waw/ya → carrier value; bare hamza skipped
HAMZA_CARRIER = {
    'أ': 1, 'إ': 1, 'آ': 1, 'ٱ': 1,  # alif variants
    'ؤ': 6,   # waw-hamza
    'ئ': 10,  # ya-hamza
    # ء (bare hamza) not in dict → skipped below
    'ى': 10,  # alif-maqsura → ya
    'ة': 5,   # ta-marbuta → ha (eastern convention)
}


def word_abjad(word):
    total = 0
    for ch in word:
        if ch in ABJAD:
            total += ABJAD[ch]
        elif ch in HAMZA_CARRIER:
            total += HAMZA_CARRIER[ch]
    return total


def clean_word(word):
    """Strip tashkeel + non-letters, return contiguous letters."""
    return ''.join(ch for ch in word if ch in ABJAD or ch in HAMZA_CARRIER)


# ---- Load Quran verses ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())

verse_final_words = []
for s in sorted(Q, key=lambda x: x['id']):
    for v in s['verses']:
        text = v['text'].strip()
        words = text.split()
        if not words:
            continue
        last = words[-1]
        last_clean = clean_word(last)
        if not last_clean:
            continue
        verse_final_words.append({
            'surah': s['id'],
            'verse': v['id'],
            'word': last,
            'abjad': word_abjad(last_clean),
            'n_letters': len(last_clean),
        })

print(f"verses with extractable final word: {len(verse_final_words)}", file=sys.stderr)
print(f"sample: {verse_final_words[:3]}", file=sys.stderr)

quran_abjads = [w['abjad'] for w in verse_final_words]
print(f"mean abjad: {statistics.mean(quran_abjads):.2f}", file=sys.stderr)
print(f"median: {statistics.median(quran_abjads)}", file=sys.stderr)
print(f"max: {max(quran_abjads)}", file=sys.stderr)


# ---- Chi-square on residue distribution ----
def chi_square_residues(values, m):
    """χ² vs uniform expectation N/m."""
    counts = [0] * m
    for v in values:
        counts[v % m] += 1
    n = len(values)
    expected = n / m
    chi2 = sum((c - expected) ** 2 / expected for c in counts)
    return chi2, counts


MODULI = [7, 11, 19]
print("\n=== Quran residue χ² ===", file=sys.stderr)
quran_chi2 = {}
for m in MODULI:
    chi2, counts = chi_square_residues(quran_abjads, m)
    quran_chi2[m] = {'chi2': chi2, 'counts': counts}
    print(f"m={m}: χ²={chi2:.3f}, counts={counts}", file=sys.stderr)

# Degrees of freedom = m-1 (for reference)


# ---- Baseline corpora ----
AR_LETTER_PAT = re.compile(r'[\u0621-\u064A]')

def clean_arabic_text(text):
    """Keep only Arabic letters (plus whitespace as word separator)."""
    out = []
    for ch in text:
        if AR_LETTER_PAT.match(ch):
            out.append(ch)
        elif ch.isspace():
            out.append(' ')
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def load_baseline(path):
    raw = Path(path).read_text(encoding='utf-8', errors='replace')
    cleaned = clean_arabic_text(raw)
    words = [w for w in cleaned.split() if clean_word(w)]
    return words


bukhari_words = load_baseline(ROOT / 'data/baseline-corpora/raw/bukhari-noquran.txt')
print(f"\nbukhari baseline words: {len(bukhari_words)}", file=sys.stderr)

# Jahiz
jahiz_path = ROOT / 'data/baseline-corpora/raw/jahiz-hayawan.txt'
if not jahiz_path.exists():
    # Try alternative
    for candidate in ['jahiz-hayawan.openiti.raw.txt', 'jahiz.txt']:
        p = ROOT / f'data/baseline-corpora/raw/{candidate}'
        if p.exists():
            jahiz_path = p
            break
jahiz_words = load_baseline(jahiz_path) if jahiz_path.exists() else []
print(f"jahiz baseline words: {len(jahiz_words)} from {jahiz_path.name}", file=sys.stderr)


# ---- Null distribution: 1000 random same-length samples ----
def baseline_null_chi2(words_pool, N, m, n_perm=1000):
    """Sample N words from baseline pool, compute χ² residues, repeat n_perm."""
    if len(words_pool) < N:
        return None
    chi2_list = []
    for _ in range(n_perm):
        sample = random.sample(words_pool, N)
        vals = [word_abjad(clean_word(w)) for w in sample]
        c2, _ = chi_square_residues(vals, m)
        chi2_list.append(c2)
    return chi2_list


N = len(verse_final_words)
print(f"\n=== Baseline nulls (N={N}, 1000 perms per corpus per m) ===", file=sys.stderr)

bukhari_nulls = {}
for m in MODULI:
    nulls = baseline_null_chi2(bukhari_words, N, m, 1000)
    if nulls is None:
        bukhari_nulls[m] = None
        continue
    sorted_n = sorted(nulls)
    pct95 = sorted_n[int(0.95 * len(sorted_n))]
    pct99 = sorted_n[int(0.99 * len(sorted_n))]
    q_chi2 = quran_chi2[m]['chi2']
    p_emp = sum(1 for x in nulls if x >= q_chi2) / len(nulls)
    bukhari_nulls[m] = {
        'mean': statistics.mean(nulls),
        'sd': statistics.stdev(nulls),
        'pct95': pct95,
        'pct99': pct99,
        'quran_chi2': q_chi2,
        'p_empirical': p_emp,
        'exceeds_95': q_chi2 > pct95,
    }
    print(f"bukhari m={m}: Quran χ²={q_chi2:.3f}, null μ={statistics.mean(nulls):.3f}, "
          f"95pct={pct95:.3f}, 99pct={pct99:.3f}, p_emp={p_emp:.4f}", file=sys.stderr)

jahiz_nulls = {}
if jahiz_words:
    for m in MODULI:
        nulls = baseline_null_chi2(jahiz_words, N, m, 1000)
        if nulls is None:
            jahiz_nulls[m] = None
            continue
        sorted_n = sorted(nulls)
        pct95 = sorted_n[int(0.95 * len(sorted_n))]
        pct99 = sorted_n[int(0.99 * len(sorted_n))]
        q_chi2 = quran_chi2[m]['chi2']
        p_emp = sum(1 for x in nulls if x >= q_chi2) / len(nulls)
        jahiz_nulls[m] = {
            'mean': statistics.mean(nulls),
            'sd': statistics.stdev(nulls),
            'pct95': pct95,
            'pct99': pct99,
            'quran_chi2': q_chi2,
            'p_empirical': p_emp,
            'exceeds_95': q_chi2 > pct95,
        }
        print(f"jahiz m={m}: Quran χ²={q_chi2:.3f}, null μ={statistics.mean(nulls):.3f}, "
              f"95pct={pct95:.3f}, 99pct={pct99:.3f}, p_emp={p_emp:.4f}", file=sys.stderr)

# ---- Verdict ----
# Pre-registered: Quran χ² ≤ baseline 95 pct for all three m → NULL confirmed
# Any m > 95 pct → flagged; joint all 3 > 95 pct → signal
verdict_parts = []
for m in MODULI:
    b = bukhari_nulls.get(m)
    j = jahiz_nulls.get(m) if jahiz_nulls else None
    b_exc = b['exceeds_95'] if b else None
    j_exc = j['exceeds_95'] if j else None
    verdict_parts.append({'m': m, 'bukhari_exceeds_95': b_exc, 'jahiz_exceeds_95': j_exc})

any_exceeds = any(v['bukhari_exceeds_95'] or v['jahiz_exceeds_95'] for v in verdict_parts
                  if v['bukhari_exceeds_95'] is not None or v['jahiz_exceeds_95'] is not None)
all_null = all((v['bukhari_exceeds_95'] is False or v['bukhari_exceeds_95'] is None)
               and (v['jahiz_exceeds_95'] is False or v['jahiz_exceeds_95'] is None)
               for v in verdict_parts)

if all_null:
    verdict = "NULL-CONFIRMED"
elif any_exceeds:
    exceeded_ms = [v['m'] for v in verdict_parts if v['bukhari_exceeds_95'] or v['jahiz_exceeds_95']]
    verdict = f"SIGNAL-FLAGGED for m={exceeded_ms}"
else:
    verdict = "MIXED"

print(f"\n=== VERDICT: {verdict} ===", file=sys.stderr)

out = {
    'seed': 20260414,
    'hypothesis': 'H-NEW-34 verse-final abjad modular residue null test',
    'rules_tuple': 'hafs-kufan, mashriqi abjad, hamza-carrier-policy, last-word-of-verse',
    'classical_anchor': 'Ibn ʿArabī Futūḥāt ch. 2; al-Bisṭāmī Shams al-Āfāq; Khalifa 19-theory echo',
    'moduli': MODULI,
    'n_verses_with_final_word': N,
    'mean_abjad': statistics.mean(quran_abjads),
    'median_abjad': statistics.median(quran_abjads),
    'max_abjad': max(quran_abjads),
    'quran_chi2_per_m': quran_chi2,
    'bukhari_nulls_per_m': bukhari_nulls,
    'jahiz_nulls_per_m': jahiz_nulls,
    'bonferroni_k': 3,
    'alpha_bon': 0.0167,
    'verdict': verdict,
    'verdict_parts': verdict_parts,
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-34.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
