#!/usr/bin/env python3
"""H-NEW-61 — Comprehensive surah opening-word distribution.

For each of 114 surahs:
  - Extract the FIRST word after any muqaṭṭaʿāt opener and after basmala.
  - Extract the first 3 words (incipit triple).
  - Map opener to a 9-class taxonomy (PRAISE, VOCATIVE, CONDITIONAL_TEMPORAL,
    OATH_PARTICLE, IMPERATIVE, REPORT_ASSERTIVE, DEMONSTRATIVE_PRONOMINAL,
    INTERROGATIVE_NEGATIVE, OTHER_CONTENT).

Pre-registration: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-61-opening-words-prereg.md

Cells (Bonferroni k=6, α_bon=0.00833):
  1. Descriptive distribution (top-10 openers, 9-class).
  2. MW-5 al-ḥamd control (Q1, 6, 18, 34, 35).
  3. χ² uniform vs observed 9-class.
  4. Opener-class × Meccan/Medinan Fisher exact.
  5. Opener-class × muqaṭṭaʿāt-opener Fisher exact.
  6. Twin-incipit (w1,w2,w3) match permutation test.

Seed: 20260416.
"""
import json, math, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260416
random.seed(SEED)

# ============================================================
# Locked muqaṭṭaʿāt set (29 surahs)
# ============================================================
MUQATTAAT_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
                    31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}

# Locked muqaṭṭaʿāt token forms (normalized: tashkeel-stripped, no shadda).
# These are the actual normalized token-strings that appear at the head of
# verses 1 (and v2 of Q42). Each entry is a list of consecutive tokens to skip
# at the head of the verse stream.
MUQATTAAT_NORMALIZED_TOKENS = {
    'الم',     # Q2,3,29,30,31,32  (also part of Q7 as الم then ص separately? — no, Q7 = المص as one token)
    'المص',    # Q7
    'الر',     # Q10,11,12,14,15
    'المر',    # Q13
    'كهيعص',   # Q19
    'طه',      # Q20
    'طسم',     # Q26,28
    'طس',      # Q27
    'يس',      # Q36
    'ص',       # Q38
    'حم',      # Q40,41,43,44,45,46 (also Q42 v1)
    'عسق',     # Q42 v2 (after حم in v1)
    'ق',       # Q50
    'ن',       # Q68
}

# ============================================================
# Tashkeel / orthographic normalization (consonant skeleton)
# ============================================================
TASHKEEL_RE = re.compile(r'[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]')
PUNCT_RE = re.compile(r'[\u06D4\u06DD\u06DE\u06DF\u060C\u061B\u061F\u0640\u200C\u200D\u200E\u200F\u061B\u061F\u00B7]+')
# Tanzil includes 'ۛ' U+06DB pause marks within verses; treat as whitespace.

def normalize(w):
    """Strip tashkeel + collapse hamza/alif/yāʾ/tāʾ-marbūṭa variants."""
    w = TASHKEEL_RE.sub('', w)
    w = PUNCT_RE.sub('', w)
    for src, dst in [('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ء','ا'),
                     ('ؤ','و'),('ئ','ي'),('ى','ي'),('ة','ه')]:
        w = w.replace(src, dst)
    return w.strip()

BASMALA_RE = re.compile(r'^بسم\s+الله\s+الرحمن\s+الرحيم\s*$')

# ============================================================
# Load chronology
# ============================================================
noldeke = {}
with open(ROOT / 'data/revelation-order.csv', encoding='utf-8') as f:
    header = f.readline().strip().split(',')
    for line in f:
        parts = line.strip().split(',')
        if len(parts) < 7:
            continue
        rev_ord, mush, name_ar, name_tl, period, nold_ord, nold_phase = parts[:7]
        try:
            sid = int(mush)
            noldeke[sid] = {
                'period': period.strip(),
                'phase': nold_phase.strip(),
                'noldeke_order': int(nold_ord),
                'rev_order': int(rev_ord),
                'name_ar': name_ar.strip(),
                'name_tl': name_tl.strip(),
            }
        except ValueError:
            continue
print(f"loaded chronology: {len(noldeke)} surahs", file=sys.stderr)

# ============================================================
# Load Quran
# ============================================================
Qdata = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text(encoding='utf-8'))
surahs = {s['id']: s for s in Qdata}
print(f"loaded Quran: {len(surahs)} surahs", file=sys.stderr)

# ============================================================
# Locked extractor: first word after muqaṭṭaʿāt + basmala
# ============================================================
def extract_word_stream(surah_id):
    """Concatenated normalized word tokens for surah, with verse-positions."""
    s = surahs[surah_id]
    stream = []  # list of (verse_id, word_idx, raw_token, normalized_token)
    for v in s['verses']:
        text = v['text'].strip()
        if not text:
            continue
        # Skip basmala if v1 is exact basmala (S != 1)
        if surah_id != 1 and v['id'] == 1 and BASMALA_RE.match(text):
            continue
        # For S1, treat v1 (which IS basmala) as skipped per pre-reg.
        if surah_id == 1 and v['id'] == 1:
            continue
        words = text.split()
        for wi, w in enumerate(words):
            nw = normalize(w)
            if not nw:
                continue
            stream.append((v['id'], wi, w, nw))
    return stream

def extract_opening_tokens(surah_id, k=3):
    """Return list of dicts for the first k non-muqaṭṭaʿāt tokens."""
    stream = extract_word_stream(surah_id)
    # Skip muqaṭṭaʿāt prefix
    i = 0
    if surah_id in MUQATTAAT_SURAHS:
        # Skip leading run of normalized tokens that match a muqaṭṭaʿāt opener.
        while i < len(stream) and stream[i][3] in MUQATTAAT_NORMALIZED_TOKENS:
            i += 1
    out = []
    for j in range(i, min(i + k, len(stream))):
        v_id, w_idx, raw, norm = stream[j]
        out.append({
            'verse_id': v_id,
            'word_idx': w_idx,
            'raw': raw,
            'normalized': norm,
            'global_position': j,
        })
    return out

# Apply extractor to all surahs
opening_data = {}
for sid in sorted(surahs.keys()):
    incipit = extract_opening_tokens(sid, k=3)
    opening_data[sid] = {
        'incipit': incipit,
        'w1_raw': incipit[0]['raw'] if incipit else '',
        'w1_norm': incipit[0]['normalized'] if incipit else '',
        'w2_norm': incipit[1]['normalized'] if len(incipit) > 1 else '',
        'w3_norm': incipit[2]['normalized'] if len(incipit) > 2 else '',
        'incipit_triple': tuple(t['normalized'] for t in incipit),
        'period': noldeke.get(sid, {}).get('period', 'Unknown'),
        'phase': noldeke.get(sid, {}).get('phase', 'Unknown'),
        'name_ar': noldeke.get(sid, {}).get('name_ar', ''),
        'name_tl': noldeke.get(sid, {}).get('name_tl', ''),
        'is_muqattaat': sid in MUQATTAAT_SURAHS,
        'n_verses': len(surahs[sid]['verses']),
    }

# ============================================================
# Cell 2 — MW-5 al-ḥamd control (run FIRST per pre-reg)
# ============================================================
print("\n=== Cell 2: MW-5 al-ḥamd control ===", file=sys.stderr)
hamd_surahs = {1, 6, 18, 34, 35}
hamd_w1_set = {'الحمد', 'الحمدلله'}  # al-ḥamd or merged form
mw5_correct = 0
mw5_details = {}
for sid in sorted(hamd_surahs):
    w1 = opening_data[sid]['w1_norm']
    is_hamd = w1 in hamd_w1_set
    mw5_details[sid] = {'w1': w1, 'is_hamd': is_hamd}
    print(f"  S{sid}: w1='{w1}' → {'HAMD' if is_hamd else 'MISS'}", file=sys.stderr)
    if is_hamd:
        mw5_correct += 1
mw5_pass = (mw5_correct == 5)
print(f"  MW-5 verdict: {mw5_correct}/5 → {'PASS' if mw5_pass else 'FAIL — EXTRACTOR BROKEN'}", file=sys.stderr)

# Sanity: stop if MW-5 fails
if not mw5_pass:
    print("  WARNING: MW-5 failed; downstream cells invalidated. Continuing for diagnostics.", file=sys.stderr)

# ============================================================
# 9-class taxonomy assignment (locked per pre-reg)
# ============================================================
# Token-classification rules (priority order):
#   PRAISE > VOCATIVE > CONDITIONAL_TEMPORAL > OATH_PARTICLE > IMPERATIVE >
#   REPORT_ASSERTIVE > DEMONSTRATIVE_PRONOMINAL > INTERROGATIVE_NEGATIVE > OTHER_CONTENT

PRAISE_LEMMAS = {'الحمد', 'الحمدلله', 'حمد', 'سبحان', 'سبح', 'يسبح', 'سبحت',
                 'تبارك', 'تباركت'}
VOCATIVE_PREFIXES = ('يا', 'ياي', 'يأ', 'يأي')
CONDITIONAL_LEMMAS = {'اذا', 'اذ', 'يوم', 'حين', 'لو', 'يومئذ', 'حينئذ',
                      'فاذا', 'متى'}
# OATH: leading wa- on a content noun (oath particle); also ta-, la-
# Detected on raw token via prefix; we strip wa-/fa-/ta- and inspect.
IMPER_LEMMAS = {'قل', 'اقرا', 'انظر', 'اتل', 'اعبد', 'اعبدوا', 'استغفر',
                'ادع', 'بلغ', 'انذر', 'اذكر', 'تبع', 'اتبع', 'كن', 'فاسجد',
                'فبشرهم', 'سل', 'فقل'}
REPORT_LEMMAS = {'قد', 'انا', 'ان', 'انه', 'انها', 'تنزيل', 'تنزل', 'كتاب',
                 'سوره', 'حم', 'ليس', 'هكذا'}
DEMONSTRATIVE_LEMMAS = {'ذلك', 'تلك', 'هذا', 'هذه', 'هؤلاء', 'هو', 'هي', 'هم',
                        'الله'}
INTERROG_NEG_LEMMAS = {'هل', 'ا', 'ما', 'الم', 'الا', 'ليس', 'ايا', 'ايها'}
INTERROG_PREFIXES = ('الم', 'الا', 'افلا', 'أ')

def classify_opener(w1_norm, w1_raw):
    """Return (class, reason)."""
    w = w1_norm
    if not w:
        return 'OTHER_CONTENT', 'empty'
    # PRAISE
    if w in PRAISE_LEMMAS:
        return 'PRAISE', 'lemma'
    # also catch ḥamd as substring start
    for stem in ['الحمد', 'سبحن', 'سبح', 'تبارك', 'يسبح']:
        if w.startswith(stem) and len(w) <= len(stem) + 4:
            return 'PRAISE', f'startswith {stem}'
    # VOCATIVE — token starts with يا (yā), often as part of يأيها or fused.
    if w.startswith('يا') or w.startswith('يايها') or w.startswith('يأ'):
        return 'VOCATIVE', 'starts-with-yā'
    if w in {'يا'}:
        return 'VOCATIVE', 'bare-yā'
    # CONDITIONAL_TEMPORAL
    if w in CONDITIONAL_LEMMAS:
        return 'CONDITIONAL_TEMPORAL', 'lemma'
    # OATH — leading wa- on a content noun used as swearing particle.
    # Heuristic: w starts with و and the subsequent word is short (<= 8 chars)
    # AND the surah is short (Mufaṣṣal). Rather than length, we use a strict
    # rule: opener startswith 'و' AND the surah is one of the classical oath-
    # opening surahs OR is in the short Mufaṣṣal (n_verses <= 50 and Meccan).
    # To remain mechanical & pre-registered: opener-token = 'و' + content-noun.
    if w.startswith('و') and len(w) > 1:
        # verify it's the oath-particle form by checking the raw token
        # contains a definite-article after wa- (ال) or is a bare oath noun
        # like wa-tīn, wa-shams, etc.
        rest = w[1:]
        if rest.startswith('ال') or rest in {'الفجر', 'الشمس', 'الليل', 'النجم',
                                              'العصر', 'التين', 'القرءان',
                                              'القران', 'العاديات', 'المرسلات',
                                              'الذاريات', 'الطور', 'الصافات',
                                              'الذريات', 'النازعات', 'الصبح',
                                              'الضحى', 'السماء', 'البلد', 'القلم',
                                              'النحل'}:
            return 'OATH_PARTICLE', 'wa-l-X'
        # bare oath noun (rare but check)
        if rest in {'فجر', 'شمس', 'ليل', 'نجم', 'عصر', 'تين', 'قرءان', 'قران'}:
            return 'OATH_PARTICLE', 'wa-X'
    # IMPERATIVE
    if w in IMPER_LEMMAS:
        return 'IMPERATIVE', 'lemma'
    # REPORT_ASSERTIVE
    if w in REPORT_LEMMAS:
        return 'REPORT_ASSERTIVE', 'lemma'
    # DEMONSTRATIVE / PRONOMINAL
    if w in DEMONSTRATIVE_LEMMAS:
        return 'DEMONSTRATIVE_PRONOMINAL', 'lemma'
    # INTERROGATIVE / NEGATIVE
    if w in INTERROG_NEG_LEMMAS:
        return 'INTERROGATIVE_NEGATIVE', 'lemma'
    # Default
    return 'OTHER_CONTENT', 'default'

# Apply
for sid, info in opening_data.items():
    cls, reason = classify_opener(info['w1_norm'], info['w1_raw'])
    info['class'] = cls
    info['class_reason'] = reason

# ============================================================
# Cell 1 — Descriptive distribution
# ============================================================
print("\n=== Cell 1: Descriptive distribution ===", file=sys.stderr)
w1_counter = Counter(info['w1_norm'] for info in opening_data.values())
print("\nTop-15 most frequent opener tokens (normalized):", file=sys.stderr)
for w, n in w1_counter.most_common(15):
    sids = [sid for sid, info in opening_data.items() if info['w1_norm'] == w]
    print(f"  {w!r}: n={n}  surahs={sids[:8]}{'...' if len(sids) > 8 else ''}", file=sys.stderr)

class_counter = Counter(info['class'] for info in opening_data.values())
print("\nOpener 9-class distribution:", file=sys.stderr)
for cls in ['PRAISE', 'VOCATIVE', 'CONDITIONAL_TEMPORAL', 'OATH_PARTICLE',
            'IMPERATIVE', 'REPORT_ASSERTIVE', 'DEMONSTRATIVE_PRONOMINAL',
            'INTERROGATIVE_NEGATIVE', 'OTHER_CONTENT']:
    n = class_counter.get(cls, 0)
    print(f"  {cls:>30s}: {n}", file=sys.stderr)

# ============================================================
# Cell 3 — χ² uniform vs observed 9-class
# ============================================================
print("\n=== Cell 3: χ² uniformity test (9 classes) ===", file=sys.stderr)
classes = ['PRAISE', 'VOCATIVE', 'CONDITIONAL_TEMPORAL', 'OATH_PARTICLE',
           'IMPERATIVE', 'REPORT_ASSERTIVE', 'DEMONSTRATIVE_PRONOMINAL',
           'INTERROGATIVE_NEGATIVE', 'OTHER_CONTENT']
observed = [class_counter.get(c, 0) for c in classes]
N = sum(observed)
expected = N / len(classes)
chi2 = sum((o - expected) ** 2 / expected for o in observed)
df = len(classes) - 1

# χ² survival approximation via incomplete gamma
def chi2_sf(x, df):
    """Survival function (1 - CDF) for χ² with df degrees of freedom.
    Uses series for small x and asymptotic for large.  Approximation suffices."""
    if x <= 0:
        return 1.0
    # use math.lgamma for upper incomplete gamma via continued fraction
    a = df / 2.0
    z = x / 2.0
    # use Lanczos-style recurrence
    if z < a + 1:
        # series
        term = 1.0 / a
        s = term
        for k in range(1, 500):
            term *= z / (a + k)
            s += term
            if abs(term) < 1e-15 * abs(s):
                break
        regularized_lower = s * math.exp(-z + a * math.log(z) - math.lgamma(a))
        return max(0.0, 1.0 - regularized_lower)
    else:
        # continued fraction for upper
        b = z + 1 - a
        c_ = 1e30
        d_ = 1.0 / b
        h = d_
        for i in range(1, 500):
            an = -i * (i - a)
            b += 2.0
            d_ = an * d_ + b
            if abs(d_) < 1e-30:
                d_ = 1e-30
            c_ = b + an / c_
            if abs(c_) < 1e-30:
                c_ = 1e-30
            d_ = 1.0 / d_
            delta = d_ * c_
            h *= delta
            if abs(delta - 1.0) < 1e-12:
                break
        regularized_upper = h * math.exp(-z + a * math.log(z) - math.lgamma(a))
        return max(0.0, regularized_upper)

p_chi2 = chi2_sf(chi2, df)
print(f"  N={N}, expected per class={expected:.2f}", file=sys.stderr)
print(f"  observed: {dict(zip(classes, observed))}", file=sys.stderr)
print(f"  χ²={chi2:.3f}, df={df}, p={p_chi2:.6e}", file=sys.stderr)
ALPHA_BON = 0.05 / 6
cell3_pass = p_chi2 < ALPHA_BON
print(f"  Cell 3 verdict: {'PASS' if cell3_pass else 'FAIL'} (α_bon={ALPHA_BON:.5f})", file=sys.stderr)

# ============================================================
# Cell 4 — Class × Meccan/Medinan Fisher exact (per class)
# ============================================================
def fisher_exact_two_sided(a, b, c, d):
    """Fisher's exact test, two-sided.  Returns p."""
    def log_fact(n):
        return math.lgamma(n + 1)
    def hyper_pmf(k, n, K, N):
        return math.exp(log_fact(K) + log_fact(N - K) + log_fact(n) + log_fact(N - n)
                       - log_fact(k) - log_fact(K - k) - log_fact(n - k) - log_fact(N - K - n + k) - log_fact(N))
    # 2x2 table:
    #              col1  col2  rowsum
    # row1          a     b    a+b = n
    # row2          c     d    c+d
    # colsum     a+c=K  b+d  N=a+b+c+d
    n = a + b
    K = a + c
    N = a + b + c + d
    if N == 0:
        return 1.0
    p_obs = hyper_pmf(a, n, K, N)
    p_total = 0.0
    k_min = max(0, n + K - N)
    k_max = min(n, K)
    for k in range(k_min, k_max + 1):
        p_k = hyper_pmf(k, n, K, N)
        if p_k <= p_obs * (1 + 1e-12):
            p_total += p_k
    return min(1.0, p_total)

print("\n=== Cell 4: Class × Meccan/Medinan Fisher exact ===", file=sys.stderr)
period_class_table = defaultdict(Counter)
for sid, info in opening_data.items():
    period_class_table[info['period']][info['class']] += 1

print(f"  {'class':<30s} {'M-Mec':>6s} {'M-Med':>6s} {'NotMec':>7s} {'NotMed':>7s} {'p':>10s}", file=sys.stderr)

cell4_results = {}
testable_classes = [c for c in classes if class_counter.get(c, 0) >= 3]
k_inner_4 = len(testable_classes)
alpha_inner_4 = ALPHA_BON / max(1, k_inner_4)

for cls in testable_classes:
    a = period_class_table['Meccan'][cls]
    c = period_class_table['Medinan'][cls]
    b = sum(period_class_table['Meccan'].values()) - a
    d = sum(period_class_table['Medinan'].values()) - c
    p = fisher_exact_two_sided(a, b, c, d)
    cell4_results[cls] = {
        'meccan_in_class': a, 'meccan_other': b,
        'medinan_in_class': c, 'medinan_other': d,
        'p': p, 'pass': p < alpha_inner_4,
    }
    flag = ' *' if p < alpha_inner_4 else ''
    print(f"  {cls:<30s} {a:>6d} {c:>6d} {b:>7d} {d:>7d} {p:>10.5f}{flag}", file=sys.stderr)

print(f"  inner Bonferroni k={k_inner_4}, α_inner={alpha_inner_4:.5f}", file=sys.stderr)
cell4_any_pass = any(v['pass'] for v in cell4_results.values())

# ============================================================
# Cell 5 — Class × muqaṭṭaʿāt-opener Fisher exact
# ============================================================
print("\n=== Cell 5: Class × Muqaṭṭaʿāt-opener Fisher exact ===", file=sys.stderr)
muq_class_table = defaultdict(Counter)
for sid, info in opening_data.items():
    key = 'MUQ' if info['is_muqattaat'] else 'NON_MUQ'
    muq_class_table[key][info['class']] += 1

print(f"  {'class':<30s} {'MUQ':>5s} {'NMUQ':>5s} {'NotM':>5s} {'NotN':>5s} {'p':>10s}", file=sys.stderr)

cell5_results = {}
k_inner_5 = len(testable_classes)
alpha_inner_5 = ALPHA_BON / max(1, k_inner_5)

for cls in testable_classes:
    a = muq_class_table['MUQ'][cls]
    c = muq_class_table['NON_MUQ'][cls]
    b = sum(muq_class_table['MUQ'].values()) - a
    d = sum(muq_class_table['NON_MUQ'].values()) - c
    p = fisher_exact_two_sided(a, b, c, d)
    cell5_results[cls] = {
        'muq_in_class': a, 'muq_other': b,
        'nonmuq_in_class': c, 'nonmuq_other': d,
        'p': p, 'pass': p < alpha_inner_5,
    }
    flag = ' *' if p < alpha_inner_5 else ''
    print(f"  {cls:<30s} {a:>5d} {c:>5d} {b:>5d} {d:>5d} {p:>10.5f}{flag}", file=sys.stderr)

print(f"  inner Bonferroni k={k_inner_5}, α_inner={alpha_inner_5:.5f}", file=sys.stderr)
cell5_any_pass = any(v['pass'] for v in cell5_results.values())

# ============================================================
# Cell 6 — Twin-incipit (w1, w2, w3) match permutation test
# ============================================================
print("\n=== Cell 6: Twin-incipit permutation test ===", file=sys.stderr)
incipit_triples = [info['incipit_triple'] for info in opening_data.values()]
w1_only = [info['w1_norm'] for info in opening_data.values()]

def count_twins(items):
    """Number of items that share their key with at least one other item."""
    c = Counter(items)
    return sum(1 for k, v in c.items() if v >= 2), sum(v for k, v in c.items() if v >= 2)

twin_groups_w1, twin_members_w1 = count_twins(w1_only)
twin_groups_w13, twin_members_w13 = count_twins(incipit_triples)
print(f"  w1 only: {twin_groups_w1} distinct repeated openers, {twin_members_w1} surahs in twin-groups", file=sys.stderr)
print(f"  (w1,w2,w3): {twin_groups_w13} distinct repeated incipits, {twin_members_w13} surahs in twin-groups", file=sys.stderr)

# Show twin groups
print("\n  Twin w1-only groups:", file=sys.stderr)
w1_groups = defaultdict(list)
for sid, info in opening_data.items():
    w1_groups[info['w1_norm']].append(sid)
for w, sids in sorted(w1_groups.items(), key=lambda x: -len(x[1])):
    if len(sids) >= 2:
        print(f"    {w!r}: {sids}", file=sys.stderr)

print("\n  Twin (w1,w2,w3) groups:", file=sys.stderr)
trip_groups = defaultdict(list)
for sid, info in opening_data.items():
    trip_groups[info['incipit_triple']].append(sid)
for trip, sids in sorted(trip_groups.items(), key=lambda x: -len(x[1])):
    if len(sids) >= 2:
        print(f"    {' '.join(trip)!r}: {sids}", file=sys.stderr)

# Permutation test: how often does the count of twin-incipit groups arise under a random
# null where each surah is given a random opener-tuple drawn from the empirical pool?
# Strict test: permute the (w1, w2, w3) tuples among the 114 surahs and count twins.
# Since permutation does NOT change the multiset of tuples (just their assignments),
# the count of twin-groups is INVARIANT under permutation. So this test is degenerate.
#
# Instead: bootstrap from the empirical w1, w2, w3 marginal distributions
# independently — i.e., assume w1, w2, w3 are independent draws from their marginals.
# This is a KNOCK-OUT null that breaks any incipit syntax, then check if observed
# twin-incipit count is more than expected under independence.

print("\n  Permutation null: independent marginal draws (10⁴ samples)", file=sys.stderr)
w1_pool = [info['w1_norm'] for info in opening_data.values()]
w2_pool = [info['w2_norm'] for info in opening_data.values()]
w3_pool = [info['w3_norm'] for info in opening_data.values()]

n_perm = 10000
null_twin_groups = []
null_twin_members = []
for _ in range(n_perm):
    sample = []
    for _ in range(114):
        sample.append((random.choice(w1_pool), random.choice(w2_pool), random.choice(w3_pool)))
    g, m = count_twins(sample)
    null_twin_groups.append(g)
    null_twin_members.append(m)

null_twin_groups.sort()
null_twin_members.sort()
emp_p_groups = sum(1 for x in null_twin_groups if x >= twin_groups_w13) / n_perm
emp_p_members = sum(1 for x in null_twin_members if x >= twin_members_w13) / n_perm
print(f"  observed twin-groups={twin_groups_w13}, null median={null_twin_groups[n_perm//2]}, p={emp_p_groups:.4f}", file=sys.stderr)
print(f"  observed twin-members={twin_members_w13}, null median={null_twin_members[n_perm//2]}, p={emp_p_members:.4f}", file=sys.stderr)

# Pre-reg PASS: empirical_p < α_bon. Direction: twin-incipit count EXCEEDS null
cell6_pass = emp_p_groups < ALPHA_BON
print(f"  Cell 6 verdict: {'PASS' if cell6_pass else 'FAIL'} (need p<{ALPHA_BON:.5f})", file=sys.stderr)

# Also test: w1-only twin (less stringent)
null_w1_groups = []
for _ in range(n_perm):
    sample = [random.choice(w1_pool) for _ in range(114)]
    g, m = count_twins(sample)
    null_w1_groups.append(g)
null_w1_groups.sort()
emp_p_w1 = sum(1 for x in null_w1_groups if x >= twin_groups_w1) / n_perm
print(f"  w1-only twin-groups: observed={twin_groups_w1}, null median={null_w1_groups[n_perm//2]}, p={emp_p_w1:.4f}", file=sys.stderr)

# ============================================================
# Bonus: opener-class × log(verse_count) correlation (descriptive)
# ============================================================
print("\n=== Bonus: opener-class × log(verse_count) ===", file=sys.stderr)
import statistics
class_lens = defaultdict(list)
for sid, info in opening_data.items():
    class_lens[info['class']].append(math.log(info['n_verses']))
for cls in classes:
    arr = class_lens.get(cls, [])
    if arr:
        med = statistics.median(arr)
        mean = statistics.mean(arr)
        print(f"  {cls:>30s}: n={len(arr):3d}, mean log(verses)={mean:.2f}, median={med:.2f}, mean verses={math.exp(mean):.1f}", file=sys.stderr)

# ============================================================
# QAC POS lookup (descriptive)
# ============================================================
print("\n=== QAC POS lookup for opener w1 ===", file=sys.stderr)
qac_path = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
qac_pos = {}
LOC_RE = re.compile(r'\((\d+):(\d+):(\d+):(\d+)\)')
if qac_path.exists():
    # Parse: get POS for token (sid, vid, wid) -- we want word_id = 1 only (first segment)
    # Index by (sid, vid, wid_word) -> first segment's POS
    pos_idx = defaultdict(dict)
    with open(qac_path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 3:
                continue
            loc = parts[0]
            form = parts[1]
            tag = parts[2]
            features = parts[3] if len(parts) > 3 else ''
            m = LOC_RE.match(loc)
            if not m:
                continue
            sid, vid, wid, segid = map(int, m.groups())
            # Take POS from FIRST segment of each word
            if segid == 1:
                pos_idx[(sid, vid)][wid] = tag
                # If first seg is a clitic (e.g., wa-/bi-/li-), prefer the next stem segment.
                # We'll keep first-seg as a default and override if next is STEM.
            elif segid == 2 and wid not in pos_idx[(sid, vid)] or (segid == 2 and pos_idx[(sid, vid)].get(wid) in {'CONJ', 'P', 'DET'}):
                # Override clitic-only with stem POS where applicable
                if 'STEM' in features or tag in {'N', 'V', 'PN', 'ADJ', 'PRON', 'DEM', 'REL', 'IMPV'}:
                    pos_idx[(sid, vid)][wid] = tag

    # Now for each surah, find the opener's POS by (sid, opener.verse_id, opener.word_idx + 1)
    # word_idx in our extractor is 0-based; QAC is 1-based.
    pos_counter = Counter()
    for sid, info in opening_data.items():
        if not info['incipit']:
            continue
        op = info['incipit'][0]
        vid = op['verse_id']
        # Convert 0-based to 1-based; also note that QAC doesn't include basmala
        # for surahs other than Q1.  For Q1 it does include basmala in v1.
        wid_1 = op['word_idx'] + 1
        pos = pos_idx.get((sid, vid), {}).get(wid_1, '?')
        qac_pos[sid] = pos
        pos_counter[pos] += 1
    print("  POS distribution for openers (QAC tags):", file=sys.stderr)
    for p, n in pos_counter.most_common():
        print(f"    {p}: {n}", file=sys.stderr)
else:
    print(f"  QAC file not found at {qac_path}; skipping POS enrichment.", file=sys.stderr)

# ============================================================
# Final verdict
# ============================================================
print("\n=== FINAL VERDICTS (Bonferroni k=6, α_bon=0.00833) ===", file=sys.stderr)
print(f"  Cell 1 (descriptive):                      PUBLISHED", file=sys.stderr)
print(f"  Cell 2 (MW-5 al-ḥamd control):             {'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)
print(f"  Cell 3 (χ² uniformity):                    {'PASS' if cell3_pass else 'FAIL'}  (p={p_chi2:.3e})", file=sys.stderr)
print(f"  Cell 4 (period × class, any inner pass):   {'PASS' if cell4_any_pass else 'FAIL'}", file=sys.stderr)
print(f"  Cell 5 (muqaṭṭaʿāt × class, any inner):    {'PASS' if cell5_any_pass else 'FAIL'}", file=sys.stderr)
print(f"  Cell 6 (twin-incipit perm vs null):        {'PASS' if cell6_pass else 'FAIL'}  (p={emp_p_groups:.4f})", file=sys.stderr)

# ============================================================
# Save JSON
# ============================================================
out = {
    'seed': SEED,
    'hypothesis_id': 'H-NEW-61',
    'title': 'Surah opening-word distribution — comprehensive',
    'rules_tuple': '(no-tashkeel, hafs-kufan, canonical-114, 29-muqaṭṭaʿāt-set)',
    'n_surahs': 114,
    'bonferroni_k': 6,
    'alpha_bon': ALPHA_BON,
    'extractor': {
        'description': 'first word after muqaṭṭaʿāt-token-run + after basmala',
        'muqattaat_surahs': sorted(MUQATTAAT_SURAHS),
        'muqattaat_normalized_tokens': sorted(MUQATTAAT_NORMALIZED_TOKENS),
    },
    'cell_2_mw5': {
        'hamd_surahs': sorted(hamd_surahs),
        'correct': mw5_correct,
        'pass': mw5_pass,
        'details': mw5_details,
    },
    'cell_1_descriptive': {
        'top_15_openers': [(w, n, sorted([sid for sid, info in opening_data.items() if info['w1_norm'] == w]))
                           for w, n in w1_counter.most_common(15)],
        'class_distribution': {c: class_counter.get(c, 0) for c in classes},
    },
    'cell_3_chi2': {
        'observed': dict(zip(classes, observed)),
        'expected': expected,
        'chi2': chi2,
        'df': df,
        'p': p_chi2,
        'pass': cell3_pass,
    },
    'cell_4_period_class': {
        'period_class_table': {p: dict(c) for p, c in period_class_table.items()},
        'inner_bonferroni_k': k_inner_4,
        'alpha_inner': alpha_inner_4,
        'per_class': cell4_results,
        'any_pass': cell4_any_pass,
    },
    'cell_5_muqattaat_class': {
        'muq_class_table': {p: dict(c) for p, c in muq_class_table.items()},
        'inner_bonferroni_k': k_inner_5,
        'alpha_inner': alpha_inner_5,
        'per_class': cell5_results,
        'any_pass': cell5_any_pass,
    },
    'cell_6_twin_incipit': {
        'observed_twin_groups_w1w2w3': twin_groups_w13,
        'observed_twin_members_w1w2w3': twin_members_w13,
        'observed_twin_groups_w1': twin_groups_w1,
        'observed_twin_members_w1': twin_members_w1,
        'null_n_perm': n_perm,
        'null_median_groups_w1w2w3': null_twin_groups[n_perm // 2],
        'null_median_members_w1w2w3': null_twin_members[n_perm // 2],
        'null_median_groups_w1': null_w1_groups[n_perm // 2],
        'emp_p_twin_groups_w1w2w3': emp_p_groups,
        'emp_p_twin_members_w1w2w3': emp_p_members,
        'emp_p_twin_groups_w1': emp_p_w1,
        'pass': cell6_pass,
        'twin_groups_w1_detail': {w: sids for w, sids in w1_groups.items() if len(sids) >= 2},
        'twin_groups_w1w2w3_detail': {' '.join(t): sids for t, sids in trip_groups.items() if len(sids) >= 2},
    },
    'qac_pos': {str(sid): qac_pos.get(sid, '?') for sid in opening_data.keys()},
    'qac_pos_distribution': dict(Counter(qac_pos.values())) if qac_pos else {},
    'opening_data': {
        str(sid): {
            'w1_raw': info['w1_raw'],
            'w1_norm': info['w1_norm'],
            'w2_norm': info['w2_norm'],
            'w3_norm': info['w3_norm'],
            'incipit_triple': list(info['incipit_triple']),
            'class': info['class'],
            'class_reason': info['class_reason'],
            'period': info['period'],
            'phase': info['phase'],
            'is_muqattaat': info['is_muqattaat'],
            'n_verses': info['n_verses'],
            'name_ar': info['name_ar'],
            'name_tl': info['name_tl'],
            'qac_pos': qac_pos.get(sid, '?'),
        } for sid, info in opening_data.items()
    },
    'verdicts': {
        'cell_1': 'PUBLISHED',
        'cell_2_mw5': 'PASS' if mw5_pass else 'FAIL_EXTRACTOR_BROKEN',
        'cell_3_chi2': 'PASS' if cell3_pass else 'FAIL',
        'cell_4_period': 'PASS' if cell4_any_pass else 'FAIL',
        'cell_5_muqattaat': 'PASS' if cell5_any_pass else 'FAIL',
        'cell_6_twin': 'PASS' if cell6_pass else 'FAIL',
    },
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-61.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f"\nsaved: {out_path}", file=sys.stderr)
