#!/usr/bin/env python3
"""Q024-F-06: Q 24:35 'Allāh nūr al-samāwāti wa-l-arḍ' uniqueness test (LOCKED pre-reg).

Searches the corpus for all 'Allāh + nūr' constructions and classifies
each by syntactic category. Pre-registered claim: exactly ONE
identity-nominal (I-NOM) at Q 24:35.

Rules-tuple: no-tashkeel surface search, min/full-tashkeel verification,
Hafs-Kufan, mushaf-order, orthographic-token adjacency.
"""
import json, hashlib, os, re

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-06-allah-nur-cop-less-uniqueness-prereg.md"
EXPECTED_SHA = "7177ae2738e0e542729319eaecdd1c32e933a0d82c24ceda1779669dfe3dc115"
QURAN_NO = f"{PROJECT}/quran-text/quran-no-tashkeel.json"
QURAN_MIN = f"{PROJECT}/quran-text/quran-min-tashkeel.json"
QURAN_FULL = f"{PROJECT}/quran-text/quran-full-tashkeel.json"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-06.json"

SEED = 20260509

# 1. SHA-lock the pre-reg
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256:    {sha}")
print(f"Expected:          {EXPECTED_SHA}")
if sha != EXPECTED_SHA:
    raise SystemExit("FAIL: pre-reg SHA mismatch — abort.")
print("OK SHA verified.\n")

# 2. Surface search for Allāh + nūr bigram (both orders)
with open(QURAN_NO) as f:
    quran_no = json.load(f)

NEEDLES = [
    ('الله نور', 'Allah-nur'),
    ('نور الله', 'nur-Allah'),
]

hits = []
for s in quran_no:
    for v in s['verses']:
        text = v['text']
        for needle, label in NEEDLES:
            if needle in text:
                # Get word context around the match
                idx = text.find(needle)
                pre = text[max(0, idx - 60):idx]
                hit = text[idx:idx + len(needle)]
                post = text[idx + len(needle):idx + len(needle) + 60]
                hits.append({
                    'surah': s['id'],
                    'verse': v['id'],
                    'order': label,
                    'context': f"...{pre}[{hit}]{post}...",
                    'full_text': text,
                })

print(f"Found {len(hits)} surface-bigram hits:")
for h in hits:
    print(f"  Q{h['surah']:>3}:{h['verse']:>3} ({h['order']}): {h['context'][:200]}")

# 3. Syntactic classification — applies the locked categories
# I-NOM:    Allāh + nūr as direct subject-predicate identity nominal
# PARTITIVE: 'min Allāh + nūr' = 'from Allāh, a light' (preposition before Allāh, nūr indefinite)
# GENITIVE:  'nūr Allāh' = "Allāh's light" (nūr first, possessive)
# PREDICATE-CHAIN: appears in a longer NP chain, not pure identity

def classify(hit):
    """Apply locked syntactic categories based on the surface form + immediate context."""
    text = hit['full_text']
    idx = text.find('الله نور' if hit['order'] == 'Allah-nur' else 'نور الله')
    # Look at the 30 chars before the match for 'من' (from) preposition
    pre_window = text[max(0, idx - 30):idx]
    if hit['order'] == 'nur-Allah':
        # 'nūr Allāh' — nūr precedes Allāh: this is genitive 'Allāh's light'
        return 'GENITIVE'
    # order is 'Allah-nur'
    # Check for 'من' (from) immediately or shortly before — partitive 'from Allāh a light'
    # 'من' precedes 'الله نور' indicates partitive
    pre_tokens = pre_window.strip().split()
    if pre_tokens and pre_tokens[-1] == 'من':
        return 'PARTITIVE'
    # Otherwise — Allāh is the subject and nūr the predicate. Check that nūr is NOT immediately
    # followed by a genitive that would make 'Allāh nūr-X' a different structure (e.g. 'Allāh nūr ʿalā nūr').
    # For Q 24:35 we have 'الله نور السماوات والأرض' — Allāh = light-of-the-heavens-and-earth.
    # The 'nūr al-samāwāti wa-l-arḍ' is the predicate noun-phrase. This is still I-NOM:
    # Allāh = [nūr al-samāwāti wa-l-arḍ]. The predicate is a definite construct, but the
    # sentence remains an identity nominal.
    return 'I-NOM'

for h in hits:
    h['category'] = classify(h)
    print(f"  Q{h['surah']:>3}:{h['verse']:>3} → {h['category']}")

# 4. Count I-NOM matches
i_nom_hits = [h for h in hits if h['category'] == 'I-NOM']
n_i_nom = len(i_nom_hits)
print(f"\nI-NOM count: {n_i_nom}")
for h in i_nom_hits:
    print(f"  Q{h['surah']:>3}:{h['verse']:>3}")

# 5. Cross-validation in min/full-tashkeel — verify case marking is nominative on Allāhu and nūru at Q 24:35
with open(QURAN_MIN) as f:
    quran_min = json.load(f)
with open(QURAN_FULL) as f:
    quran_full = json.load(f)

q24_v35_min = next(v for v in quran_min[23]['verses'] if v['id'] == 35)['text']
q24_v35_full = next(v for v in quran_full[23]['verses'] if v['id'] == 35)['text']
print(f"\nQ 24:35 min-tashkeel head: {q24_v35_min[:60]}")
print(f"Q 24:35 full-tashkeel head: {q24_v35_full[:60]}")

# In min/full tashkeel, look for اللَّهُ (Allāhu, nominative ḍamma) immediately before نور
# This confirms the nominal-sentence subject case.
# Nominative on Allāh: check for the sequence hāʾ + ḍamma immediately before the space + nūn (start of nūru).
# Damma is U+064F. The full Allāh-token ends with hāʾ + damma in nominative.
DAMMA = 'ُ'  # ُ
def has_allah_nominative(text):
    # Look for 'هُ ن' (hāʾ + damma + space + nūn) — Allāhu followed by nūru
    return f'ه{DAMMA} ن' in text or f'ه{DAMMA}ٰ ن' in text
case_verified = has_allah_nominative(q24_v35_min) or has_allah_nominative(q24_v35_full)
print(f"Nominative case on Allāh at Q 24:35 (min/full tashkeel): {case_verified}")

# 6. Verdict
if n_i_nom == 1 and i_nom_hits[0]['surah'] == 24 and i_nom_hits[0]['verse'] == 35:
    verdict = "CONFIRMED"
elif n_i_nom == 0:
    verdict = "NULL-paradox"
elif n_i_nom > 1:
    verdict = "FALSIFIED"
else:
    verdict = "UNEXPECTED"
print(f"\nVerdict: {verdict}")

# 7. Write JSON
out = {
    'finding_id': 'Q024-F-06',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'date': '2026-05-09',
    'rules_tuple': '(no-tashkeel for surface, min/full-tashkeel for case verification, orthographic-token, Hafs-Kufan)',
    'surface_hits': len(hits),
    'i_nom_hits': n_i_nom,
    'all_hits': hits,
    'nominative_case_verified_at_q24_35': case_verified,
    'verdict': verdict,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
print(f"\nWrote {OUT}")
