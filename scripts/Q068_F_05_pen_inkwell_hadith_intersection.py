#!/usr/bin/env python3
"""
Q068-F-05 — pen-inkwell hadith intersection: does Q 68:1 dominate
Q 68's hadith citation profile across the 9 books?
"""
import hashlib, json, math, os, re, sys
from collections import defaultdict

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q068-al-qalam/preregs/Q068-F-05-pen-inkwell-hadith-intersection-prereg.md'
EXPECTED_SHA = '7b5e8990c846e374a337415ec73971c53a044d22e225c530d0007dea4a27baf7'

with open(PREREG, 'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}')

# Normalize Arabic text: alif/yaa/taa-marbuta/tashkeel
# Also strip Quranic editorial pause-glyphs (U+06D6..U+06DC, U+06DD..U+06DF) which appear
# only in mushaf text and never in hadith corpus — leaving them in would create false negatives.
def normalize(s):
    if not s: return s
    s = s.replace('أ','ا').replace('إ','ا').replace('آ','ا')
    s = s.replace('ى','ي').replace('ة','ه')
    s = re.sub(r'[ًٌٍَُِّْٰٓـ~]','', s)
    s = re.sub(r'[ۖ-ۭ]', '', s)  # Quranic pause/sajda marks
    return s

# Pick a deterministic distinctive substring per Q 68 verse:
# longest contiguous content-word substring with at least 4 words,
# excluding stop-words.
STOPWORDS = {
    'و','ف','ل','ب','ك','ع','من','الى','عن','في','على','هو','هي',
    'انا','نحن','هم','ما','لا','ان','ال','ا','يا','قال','قالوا','قل',
    'كان','كانوا','هذا','هذه','الذي','التي','الذين'
}

# Load Q 68 verses
with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    q = json.load(f)
q68 = q[67]['verses']

def pick_distinctive(verse_text):
    """Pick deterministic 4+-word phrase from a verse most likely to be quote-able."""
    words = [normalize(w) for w in verse_text.split() if normalize(w)]
    # remove tatweel/punctuation already done by normalize
    # exclude stopwords by leading position only — keep contiguous
    # Strategy: pick the longest 4-word contiguous span where at least 3 of the 4 are non-stop
    best = None; best_score = -1
    for i in range(len(words) - 3):
        span = words[i:i+4]
        non_stop = sum(1 for w in span if w not in STOPWORDS and len(w) >= 3)
        # break ties by total length
        score = non_stop * 100 + sum(len(w) for w in span)
        if score > best_score:
            best_score = score
            best = span
    if not best:
        return ' '.join(words[:4]) if len(words) >= 4 else ' '.join(words)
    return ' '.join(best)

verse_phrases = {}
for v_idx, v in enumerate(q68):
    txt = v if isinstance(v, str) else v.get('text', '')
    verse_phrases[v_idx + 1] = pick_distinctive(txt)

# Load all 9 books and walk for hadith records w/ Arabic text
BOOKS = ['bukhari','muslim','tirmidhi','abudawud','nasai','ibnmajah','malik','ahmed','darimi']
base = f'{PROJECT}/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/'

book_records = {}
for b in BOOKS:
    p = os.path.join(base, b + '.json')
    with open(p, encoding='utf-8') as f:
        data = json.load(f)
    records = []
    def walk(o):
        if isinstance(o, dict):
            arabic_text = o.get('arabic', '')
            if arabic_text and isinstance(arabic_text, str):
                records.append({
                    'idInBook': o.get('idInBook'),
                    'arabic_normalized': normalize(arabic_text),
                })
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(data)
    book_records[b] = records

# Count citations per verse per book
citation_counts = {v: {b: 0 for b in BOOKS} for v in range(1, 53)}
citation_records = defaultdict(list)  # verse -> list of (book, idInBook)

for v in range(1, 53):
    phrase = verse_phrases[v]
    if not phrase or len(phrase) < 6:  # skip very short phrases
        continue
    for b in BOOKS:
        for rec in book_records[b]:
            if phrase in rec['arabic_normalized']:
                citation_counts[v][b] += 1
                citation_records[v].append((b, rec['idInBook']))

# Total citations per verse
verse_totals = {v: sum(citation_counts[v].values()) for v in range(1, 53)}
T = sum(verse_totals.values())

# Sort verses by citation count
sorted_verses = sorted(verse_totals.items(), key=lambda x: -x[1])
v_max, max_count = sorted_verses[0]
v1_count = verse_totals[1]
v1_rank = next(i+1 for i, (v, _) in enumerate(sorted_verses) if v == 1)

# Binomial test for Q 68:1 under uniform null
def binomial_p_ge(n, k, p):
    if k <= 0: return 1.0
    if p <= 0 or p >= 1: return 1.0 if p<=0 else 0.0
    log_p = math.log(p); log_q = math.log1p(-p)
    total = 0.0
    for i in range(k, n+1):
        lc = math.lgamma(n+1) - math.lgamma(i+1) - math.lgamma(n-i+1)
        total += math.exp(lc + i*log_p + (n-i)*log_q)
    return total

p_uniform = 1.0 / 52
p_binom_v1 = binomial_p_ge(T, v1_count, p_uniform) if T > 0 else 1.0
expected_uniform = T / 52

direction_reversed = (v1_count < expected_uniform)
if direction_reversed:
    verdict = 'NULL_DIRECTION_REVERSED'
    interp = (f"Q 68:1 cited {v1_count} times vs expected {expected_uniform:.2f} under uniform null. "
              f"Direction reversed; pre-commit violation, published as NULL.")
elif v1_rank == 1 and p_binom_v1 < 0.05:
    verdict = 'VINDICATED'
    interp = (f"Q 68:1 is the modal verse of Q 68 ({v1_count}/{T} citations); "
              f"binomial p={p_binom_v1:.4f} < 0.05 vs uniform null. "
              f"Pen-inkwell hadith complex empirically anchored at Q 68:1.")
elif v1_rank <= 3:
    verdict = 'DIRECTIONAL'
    interp = (f"Q 68:1 ranks {v1_rank}/52 in citation count ({v1_count}/{T}); "
              f"binomial p={p_binom_v1:.4f}.")
else:
    verdict = 'NULL'
    interp = (f"Q 68:1 ranks {v1_rank}/52 in citation count ({v1_count}/{T}); "
              f"NOT the modal verse. Pen-inkwell hadith complex is interpreted "
              f"by classical narrators as commenting on Q 68:1 but is not directly "
              f"verbatim-citing it.")

output = {
    'finding_id': 'Q068-F-05',
    'prereg_sha256': actual,
    'date_run': '2026-05-07',
    'rules_tuple': 'normalized Arabic substring match (alif/yaa/taa-marbuta unified, tashkeel stripped); 9 canonical hadith books; pre-registered distinctive 4+-word substrings per verse',
    'verse_distinctive_phrases': verse_phrases,
    'citation_counts_per_verse_per_book': citation_counts,
    'verse_totals': verse_totals,
    'total_citations_T': T,
    'modal_verse': v_max,
    'modal_verse_count': max_count,
    'q68_v1_count': v1_count,
    'q68_v1_rank': v1_rank,
    'expected_under_uniform': expected_uniform,
    'binomial_p_value_q68_v1': p_binom_v1,
    'top10_verses_by_citation': sorted_verses[:10],
    'q68_v1_citing_records': citation_records.get(1, []),
    'verdict': verdict,
    'interpretation': interp,
}

out_path = f'{PROJECT}/surahs/Q068-al-qalam/csv/Q068-F-05.json'
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q068-F-05: VERDICT={verdict}')
print(f'  Total Q 68 hadith citations T={T}')
print(f'  Modal verse: v{v_max} with {max_count} citations')
print(f'  Q 68:1 rank: {v1_rank}/52, count={v1_count}, expected uniform={expected_uniform:.2f}')
print(f'  Binomial p(v=1): {p_binom_v1:.4e}')
print(f'  Top 10 verses by citation:')
for v, c in sorted_verses[:10]:
    print(f'    v{v}: {c} citations | phrase: {verse_phrases.get(v, "")[:60]}')
print(f'  Output: {out_path}')
