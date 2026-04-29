#!/usr/bin/env python3
"""H-NEW-84 — Sūrat al-Ikhlāṣ "1/3 of the Quran" — quantitative test.

Pre-reg: findings/phase-b-hypotheses/h-new-84-ikhlas-third-prereg.md
Locked: 2026-04-15.

7 operationalizations of "1/3 equivalence" (Bonferroni k=7, α_bon=0.00714):
  1. LENGTH (graphemic letters)
  2. TOKEN COUNT
  3. INFORMATION CONTENT (Shannon bits under corpus marginal)
  4. UNIQUE ROOT COVERAGE
  5. THEOLOGICAL CATEGORY COVERAGE (al-Ghazālī 3-category schema)
  6. THEOLOGICAL CONCENTRATION (Q 112 density vs corpus density, expecting ~3×)
  7. DIVINE-NAME COVERAGE (out of 99 names)

Per-axis PASS: ratio in [0.30, 0.37].
Overall:
  ≥ 5 PASS → PASS-STRONG
  ≥ 3 PASS → PASS-WEAK
  1-2 PASS → REFUTED-WEAK
  0 PASS  → REFUTED-STRONG

Rules tuple: (no-tashkeel; word-segment substring rule; hafs-kufan; 6236 verses;
basmala-counted-only-in-surah-1; mashriqi; Leeds Quranic Arabic Corpus 0.4).
Seed: 20260417.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
BON_K = 7
ALPHA_BON = 0.05 / BON_K
PASS_LOW = 0.30
PASS_HIGH = 0.37  # ±10% around 1/3 ≈ 0.333

# ============================================================
# Load corpus
# ============================================================
with open(ROOT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    corpus = json.load(f)
assert len(corpus) == 114

ARABIC_LETTERS = re.compile(r'[ء-ي]')

verses = []  # global verse list
for s in corpus:
    sid = s['id']
    for v in s['verses']:
        verses.append({
            'sid': sid, 'vid': v['id'], 'text': v['text'],
            'words': v['text'].split(),
            'letters': ARABIC_LETTERS.findall(v['text']),
        })
assert len(verses) == 6236

# Q 112 = al-Ikhlāṣ
ikhlas = [v for v in verses if v['sid'] == 112]
assert len(ikhlas) == 4

# ============================================================
# Pre-compute corpus aggregates
# ============================================================
all_letters_corpus = [c for v in verses for c in v['letters']]
N_LETTERS = len(all_letters_corpus)

all_tokens_corpus = [w for v in verses for w in v['words']]
N_TOKENS = len(all_tokens_corpus)

ikhlas_letters = [c for v in ikhlas for c in v['letters']]
N_LETTERS_IKH = len(ikhlas_letters)

ikhlas_tokens = [w for v in ikhlas for w in v['words']]
N_TOKENS_IKH = len(ikhlas_tokens)

# ============================================================
# Load Leeds morphology for roots/lemmas
# ============================================================
morph_path = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|\s]+)')
LEM_RE = re.compile(r'LEM:([^|\s]+)')

morph_rows = []  # list of (sid, vid, wid, sid_seg, root, lem, tag, features)
with open(morph_path, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        loc_m = LOC_RE.match(parts[0])
        if not loc_m:
            continue
        sid, vid, wid, seg = (int(x) for x in loc_m.groups())
        form = parts[1]
        tag = parts[2]
        features = parts[3]
        root_m = ROOT_RE.search(features)
        lem_m = LEM_RE.search(features)
        morph_rows.append({
            'sid': sid, 'vid': vid, 'wid': wid, 'seg': seg,
            'form': form, 'tag': tag,
            'root': root_m.group(1) if root_m else None,
            'lem': lem_m.group(1) if lem_m else None,
            'features': features,
        })

# All Quran roots (distinct, non-None)
all_roots_corpus = set(r['root'] for r in morph_rows if r['root'])
N_ROOTS_CORPUS = len(all_roots_corpus)

# Q 112 roots
ikhlas_roots = set(r['root'] for r in morph_rows if r['sid'] == 112 and r['root'])
N_ROOTS_IKH = len(ikhlas_roots)

# Q 112 lemmas
ikhlas_lemmas = set(r['lem'] for r in morph_rows if r['sid'] == 112 and r['lem'])
all_lemmas_corpus = set(r['lem'] for r in morph_rows if r['lem'])
N_LEMMAS_CORPUS = len(all_lemmas_corpus)
N_LEMMAS_IKH = len(ikhlas_lemmas)

# ============================================================
# AXIS 1 — LENGTH (graphemic letters)
# ============================================================
ratio_axis1 = N_LETTERS_IKH / N_LETTERS

# ============================================================
# AXIS 2 — TOKEN COUNT
# ============================================================
ratio_axis2 = N_TOKENS_IKH / N_TOKENS

# ============================================================
# AXIS 3 — INFORMATION CONTENT (Shannon bits under corpus marginal)
# ============================================================
char_counts = Counter(all_letters_corpus)
TOTAL_CHARS = sum(char_counts.values())
char_p = {c: cnt / TOTAL_CHARS for c, cnt in char_counts.items()}

def shannon_bits(letters):
    """Sum of -log2 p(c) for each letter under corpus marginal."""
    bits = 0.0
    for c in letters:
        if c in char_p and char_p[c] > 0:
            bits += -math.log2(char_p[c])
    return bits

bits_ikhlas = shannon_bits(ikhlas_letters)
bits_corpus = shannon_bits(all_letters_corpus)
ratio_axis3 = bits_ikhlas / bits_corpus

# ============================================================
# AXIS 4 — UNIQUE ROOT COVERAGE
# ============================================================
ratio_axis4 = N_ROOTS_IKH / N_ROOTS_CORPUS

# ============================================================
# AXIS 5 — THEOLOGICAL CATEGORY COVERAGE (al-Ghazālī schema)
# ============================================================
THEME_KEYWORDS = {
    'theology': [
        'الله', 'ربك', 'ربكم', 'ربنا', 'ربي', 'إله', 'إلهك', 'إلهكم', 'إلهنا',
        'الرحمن', 'الرحيم', 'الملك', 'القدوس', 'السلام', 'المؤمن', 'المهيمن',
        'العزيز', 'الجبار', 'المتكبر', 'الخالق', 'البارئ', 'المصور', 'الغفار',
        'القهار', 'الوهاب', 'أحد', 'الصمد', 'واحد', 'العالمين', 'سبحان',
        'تبارك', 'الحي', 'القيوم', 'الرحمان',
    ],
    'narratives': [
        'موسى', 'عيسى', 'إبراهيم', 'نوح', 'آدم', 'يوسف', 'يعقوب', 'سليمان',
        'داود', 'يونس', 'زكريا', 'يحيى', 'لوط', 'شعيب', 'هود', 'صالح', 'إدريس',
        'ذي القرنين', 'القرى', 'مدين', 'ثمود', 'عاد', 'فرعون', 'هامان', 'قارون',
        'السبت', 'إسحق', 'إسحاق', 'إسماعيل', 'الكهف', 'الكوثر', 'البيت', 'مكة',
        'طوى', 'بدر', 'حنين', 'الأحزاب', 'إذ قال', 'إذ قالت',
    ],
    'commandments': [
        'حرم', 'حلال', 'أوفوا', 'الصلاة', 'الزكاة', 'الصيام', 'الصوم', 'الحج',
        'اتقوا', 'نكاح', 'طلاق', 'الميراث', 'الربا', 'الجهاد', 'الفطرة', 'اليمين',
        'الكفارة', 'الهدي', 'القسط', 'العدل', 'الحدود', 'كتب عليكم', 'يا أيها الذين',
        'الديات', 'القصاص', 'لا تقربوا', 'لا تأكلوا', 'فاجلدوا', 'فاقطعوا',
        'يحل', 'لا يحل', 'البيع', 'الفقراء', 'المساكين', 'العفو',
    ],
}

def category_counts(text):
    """Return dict of category -> total keyword hit count via substring search."""
    out = {}
    for cat, kws in THEME_KEYWORDS.items():
        c = 0
        for kw in kws:
            c += text.count(kw)
        out[cat] = c
    return out

# For each verse, count category hits and assign dominant category (ties allowed → all-tied get 1/k)
theology_dominant_count = 0
narrative_dominant_count = 0
commandment_dominant_count = 0
none_count = 0
for v in verses:
    cats = category_counts(v['text'])
    total = sum(cats.values())
    if total == 0:
        none_count += 1
        continue
    max_v = max(cats.values())
    winners = [k for k, val in cats.items() if val == max_v]
    if 'theology' in winners:
        theology_dominant_count += 1.0 / len(winners)
    if 'narratives' in winners:
        narrative_dominant_count += 1.0 / len(winners)
    if 'commandments' in winners:
        commandment_dominant_count += 1.0 / len(winners)

n_categorized = len(verses) - none_count
theology_fraction = theology_dominant_count / len(verses)
ratio_axis5 = theology_fraction  # direct fraction of corpus verses dominated by theology

# Also compute conditional fraction (excluding uncategorized)
theology_fraction_cond = theology_dominant_count / n_categorized if n_categorized else 0.0

# ============================================================
# AXIS 6 — THEOLOGICAL CONCENTRATION (Q 112 density vs corpus density)
# ============================================================
ikhlas_text = ' '.join(v['text'] for v in ikhlas)
ikhlas_theo_hits = sum(ikhlas_text.count(kw) for kw in THEME_KEYWORDS['theology'])
ikhlas_density = ikhlas_theo_hits / N_TOKENS_IKH

corpus_text = ' '.join(v['text'] for v in verses)
corpus_theo_hits = sum(corpus_text.count(kw) for kw in THEME_KEYWORDS['theology'])
corpus_density = corpus_theo_hits / N_TOKENS

R_concentration = ikhlas_density / corpus_density if corpus_density > 0 else 0.0
# PASS: concentration factor in [3.0/1.1, 3.0*1.1] = [2.727, 3.30]
# But to keep ratio in [0.30, 0.37] format like other axes, we report ratio = 1/R (so a 3× concentration → 1/3)
ratio_axis6 = 1.0 / R_concentration if R_concentration > 0 else 0.0

# ============================================================
# AXIS 7 — DIVINE-NAME COVERAGE (99 names)
# ============================================================
# Standard 99-names list (Tirmidhī #3507 enumeration; al-Bayhaqī variant tail merged).
NAMES_99 = [
    'الله', 'الرحمن', 'الرحيم', 'الملك', 'القدوس', 'السلام', 'المؤمن', 'المهيمن',
    'العزيز', 'الجبار', 'المتكبر', 'الخالق', 'البارئ', 'المصور', 'الغفار', 'القهار',
    'الوهاب', 'الرزاق', 'الفتاح', 'العليم', 'القابض', 'الباسط', 'الخافض', 'الرافع',
    'المعز', 'المذل', 'السميع', 'البصير', 'الحكم', 'العدل', 'اللطيف', 'الخبير',
    'الحليم', 'العظيم', 'الغفور', 'الشكور', 'العلي', 'الكبير', 'الحفيظ', 'المقيت',
    'الحسيب', 'الجليل', 'الكريم', 'الرقيب', 'المجيب', 'الواسع', 'الحكيم', 'الودود',
    'المجيد', 'الباعث', 'الشهيد', 'الحق', 'الوكيل', 'القوي', 'المتين', 'الولي',
    'الحميد', 'المحصي', 'المبدئ', 'المعيد', 'المحيي', 'المميت', 'الحي', 'القيوم',
    'الواجد', 'الماجد', 'الواحد', 'الأحد', 'الصمد', 'القادر', 'المقتدر', 'المقدم',
    'المؤخر', 'الأول', 'الآخر', 'الظاهر', 'الباطن', 'الوالي', 'المتعالي', 'البر',
    'التواب', 'المنتقم', 'العفو', 'الرءوف', 'مالك الملك', 'ذو الجلال والإكرام',
    'المقسط', 'الجامع', 'الغني', 'المغني', 'المانع', 'الضار', 'النافع', 'النور',
    'الهادي', 'البديع', 'الباقي', 'الوارث', 'الرشيد', 'الصبور',
]
# Note: 100 entries because we include الله (the proper name) plus the 99 attributes
# (Tirmidhī's enumeration counts الله as #1 but classical scholars debate;
#  we include it AND treat the 99 attributes as the test set proper).
# The denominator below is 99 (the attribute names) — we'll subtract الله from the count.
NAMES_99_ATTR = [n for n in NAMES_99 if n != 'الله']
assert len(NAMES_99_ATTR) == 99

# Count distinct names appearing in Q 112 (substring; for "الأحد" check both الأحد and أحد form)
def names_in_text(text, names):
    return [n for n in names if n in text]

names_in_ikhlas = names_in_text(ikhlas_text, NAMES_99_ATTR)
# Also accept أحد as a stem-form proxy for الأحد (since Q 112 has أحد without ال-)
extra_proxies = []
if 'أحد' in ikhlas_text and 'الأحد' not in names_in_ikhlas:
    extra_proxies.append('أحد→الأحد(stem)')
n_names_in_ikhlas = len(names_in_ikhlas) + len(extra_proxies)

ratio_axis7 = n_names_in_ikhlas / 99

# Sanity: count names in entire corpus
names_in_corpus = names_in_text(corpus_text, NAMES_99_ATTR)
n_names_in_corpus = len(names_in_corpus)

# ============================================================
# MW-5 known-distinctive controls
# ============================================================
# Q 1 (al-Fātiḥa) — should be theology-dominant
fatiha_verses = [v for v in verses if v['sid'] == 1]
fatiha_text = ' '.join(v['text'] for v in fatiha_verses)
fatiha_cats = category_counts(fatiha_text)
fatiha_theology_dominant = fatiha_cats['theology'] >= max(fatiha_cats['narratives'], fatiha_cats['commandments'])

# Q 2:255 (āyat al-kursī)
kursi = [v for v in verses if v['sid'] == 2 and v['vid'] == 255][0]
kursi_cats = category_counts(kursi['text'])
kursi_theology_dominant = kursi_cats['theology'] >= max(kursi_cats['narratives'], kursi_cats['commandments'])

# Q 59:22-24 (khawātim al-ḥashr)
khawatim_text = ' '.join(v['text'] for v in verses if v['sid'] == 59 and 22 <= v['vid'] <= 24)
khawatim_cats = category_counts(khawatim_text)
khawatim_names_count = len(names_in_text(khawatim_text, NAMES_99_ATTR))

# ============================================================
# Verdict
# ============================================================
def classify(ratio, label):
    in_band = PASS_LOW <= ratio <= PASS_HIGH
    return {
        'axis': label,
        'ratio_q112_to_corpus': ratio,
        'target_low': PASS_LOW,
        'target_high': PASS_HIGH,
        'pass': bool(in_band),
        'distance_from_one_third': ratio - 1/3,
    }

axes_results = [
    {**classify(ratio_axis1, '1_LENGTH_letters'),
     'numerator': N_LETTERS_IKH, 'denominator': N_LETTERS,
     'note': '47 / 330,709 letter-graphemes; literal-length test'},
    {**classify(ratio_axis2, '2_TOKEN_COUNT'),
     'numerator': N_TOKENS_IKH, 'denominator': N_TOKENS,
     'note': 'whitespace tokens'},
    {**classify(ratio_axis3, '3_INFORMATION_CONTENT_shannon_bits'),
     'numerator': bits_ikhlas, 'denominator': bits_corpus,
     'note': 'sum of -log2 p(c) per letter under corpus marginal'},
    {**classify(ratio_axis4, '4_UNIQUE_ROOT_COVERAGE'),
     'numerator': N_ROOTS_IKH, 'denominator': N_ROOTS_CORPUS,
     'note': f'Q 112 roots: {sorted(ikhlas_roots)}'},
    {**classify(ratio_axis5, '5_THEOLOGY_CATEGORY_COVERAGE_alGhazali'),
     'numerator': theology_dominant_count, 'denominator': len(verses),
     'note': f'fraction of 6236 verses dominated by theology category; conditional on categorized = {theology_fraction_cond:.4f}; uncategorized = {none_count}'},
    {**classify(ratio_axis6, '6_THEOLOGY_CONCENTRATION_inverse'),
     'numerator': ikhlas_density, 'denominator': corpus_density,
     'note': f'concentration factor = {R_concentration:.4f}× ; expected 3× → ratio 1/R = {ratio_axis6:.4f}'},
    {**classify(ratio_axis7, '7_DIVINE_NAMES_99'),
     'numerator': n_names_in_ikhlas, 'denominator': 99,
     'note': f'names in Q 112: {names_in_ikhlas} + proxies {extra_proxies}'},
]

n_pass = sum(1 for a in axes_results if a['pass'])
if n_pass >= 5:
    verdict = 'PASS-STRONG'
elif n_pass >= 3:
    verdict = 'PASS-WEAK'
elif n_pass >= 1:
    verdict = 'REFUTED-WEAK'
else:
    verdict = 'REFUTED-STRONG'

# Find best-matching interpretation: axis closest to 1/3
best_axis = min(axes_results, key=lambda a: abs(a['ratio_q112_to_corpus'] - 1/3))

results = {
    'hypothesis_id': 'H-NEW-84',
    'title': 'Sūrat al-Ikhlāṣ "1/3 of the Quran" quantitative test',
    'rules_tuple': '(no-tashkeel; word-segment substring rule; hafs-kufan; 6236 verses; '
                   'basmala-counted-only-in-surah-1; mashriqi; Leeds Quranic Arabic Corpus 0.4)',
    'seed': SEED,
    'bonferroni_k': BON_K,
    'alpha_bon': ALPHA_BON,
    'tolerance_band_for_ratio': [PASS_LOW, PASS_HIGH],
    'q112_summary': {
        'verses': 4,
        'tokens': N_TOKENS_IKH,
        'letters': N_LETTERS_IKH,
        'distinct_roots': sorted(ikhlas_roots),
        'distinct_lemmas': sorted(ikhlas_lemmas),
    },
    'corpus_summary': {
        'verses': len(verses),
        'tokens': N_TOKENS,
        'letters': N_LETTERS,
        'distinct_roots': N_ROOTS_CORPUS,
        'distinct_lemmas': N_LEMMAS_CORPUS,
    },
    'axes': axes_results,
    'n_axes_pass': n_pass,
    'overall_verdict': verdict,
    'best_matching_axis': best_axis['axis'],
    'best_matching_ratio': best_axis['ratio_q112_to_corpus'],
    'corpus_category_breakdown': {
        'theology_dominant_verses': theology_dominant_count,
        'narrative_dominant_verses': narrative_dominant_count,
        'commandment_dominant_verses': commandment_dominant_count,
        'uncategorized_verses': none_count,
        'total_verses': len(verses),
        'theology_fraction_of_total': theology_fraction,
        'theology_fraction_of_categorized': theology_fraction_cond,
    },
    'mw5_controls': {
        'fatiha_theology_dominant': fatiha_theology_dominant,
        'fatiha_cats': fatiha_cats,
        'kursi_theology_dominant': kursi_theology_dominant,
        'kursi_cats': kursi_cats,
        'khawatim_cats': khawatim_cats,
        'khawatim_names_count_of_99': khawatim_names_count,
    },
    'ikhlas_token_corpus_freq': {w: all_tokens_corpus.count(w) for w in set(ikhlas_tokens)},
    'names_in_corpus_count_of_99': n_names_in_corpus,
    'names_in_corpus_list': names_in_corpus,
}

# Write output
out_json = ROOT / 'findings/phase-b-hypotheses/csv/h-new-84.json'
out_json.parent.mkdir(parents=True, exist_ok=True)
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Print summary
print("=" * 75)
print("H-NEW-84 — Sūrat al-Ikhlāṣ '1/3 of the Quran' (Bonferroni k=7)")
print("=" * 75)
print(f"Q 112: 4 verses, {N_TOKENS_IKH} tokens, {N_LETTERS_IKH} letters")
print(f"Corpus: 6236 verses, {N_TOKENS} tokens, {N_LETTERS} letters")
print(f"Tolerance band for 1/3 ratio: [{PASS_LOW}, {PASS_HIGH}]")
print()
for a in axes_results:
    star = ' ***PASS***' if a['pass'] else ''
    r = a['ratio_q112_to_corpus']
    target = (PASS_LOW + PASS_HIGH) / 2
    fold_off = (target / r) if r > 0 else float('inf')
    print(f"Axis {a['axis']}")
    print(f"  Ratio Q112/corpus = {r:.6f}  (target ≈ 0.333; band [0.30, 0.37]){star}")
    if not a['pass'] and r > 0:
        print(f"  Off by factor: actual is {1/(3*r):.2f}× too small (or 1/3 is {target/r:.1f}× larger)")
    print(f"  Numerator: {a['numerator']}  Denominator: {a['denominator']}")
    print(f"  Note: {a['note']}")
    print()
print(f"MW-5 sanity:")
print(f"  Q 1 al-Fātiḥa theology-dominant: {fatiha_theology_dominant} (cats={fatiha_cats})")
print(f"  Q 2:255 āyat al-kursī theology-dominant: {kursi_theology_dominant} (cats={kursi_cats})")
print(f"  Q 59:22-24 khawātim names hits / 99: {khawatim_names_count}")
print()
print(f"Corpus category breakdown:")
print(f"  Theology-dominant verses:   {theology_dominant_count:.1f} / 6236 = {theology_fraction:.4f}")
print(f"  Narrative-dominant verses:  {narrative_dominant_count:.1f}")
print(f"  Commandment-dominant verses: {commandment_dominant_count:.1f}")
print(f"  Uncategorized verses:       {none_count}")
print()
print(f"Axes PASSING (in [0.30, 0.37]): {n_pass} / 7")
print(f"Best-matching axis: {best_axis['axis']}  ratio={best_axis['ratio_q112_to_corpus']:.4f}")
print(f"OVERALL VERDICT: {verdict}")
print()
print(f"Wrote {out_json}")
