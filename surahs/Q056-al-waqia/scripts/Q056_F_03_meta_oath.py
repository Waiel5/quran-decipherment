#!/usr/bin/env python3
"""
Q056-F-03 — META-OATH device rate corpus-wide.
SHA-locked pre-reg: 93625801acf90a9667638b8163e6f1d6203538734cd25fa5ca70931259dfbb80
"""
import json, hashlib, re, os
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/preregs/Q056-F-03-meta-oath-rate-prereg.md'
EXPECTED_SHA = '93625801acf90a9667638b8163e6f1d6203538734cd25fa5ca70931259dfbb80'
with open(PREREG,'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f'SHA mismatch: {actual}'

with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
    Q = json.load(f)

# GARDEN-OF-FORKING-PATHS DISCLOSURE 2026-05-07:
# The text contains ornamental rukūʿ markers (۞) and ayah-pause markers (ۚ ۖ ۗ ۘ etc.)
# which are presentation-detail editorial annotations, NOT content graphemes.
# The pre-reg specified "no-tashkeel orthographic-token" as rules-tuple. Tashkeel
# excludes diacritics; the ۞ is not tashkeel but an ornament. Per rules-tuple
# spirit (orthographic content tokens), strip these before regex anchoring.
# This change is mechanical (regex anchor only) and does NOT alter the test direction
# or the operational definition. Pre-disclosed before re-running.
ORNAMENT_RX = re.compile(r'[۞ۚۖۗۘۙۛ]')
def clean(text):
    return ORNAMENT_RX.sub('', text).strip()

# Triggers for oath-formula in v.N (orthographic, no-tashkeel)
oath_trigger_patterns = [
    r'^فلا أقسم',     # fa-lā uqsimu
    r'^لا أقسم',      # lā uqsimu
    r'^أقسم',         # uqsimu
    r'^و(?:ال|ل)',    # wa-al... or wa-l... (oath particle wāw + the)
]

# Restricted: classical "oath verse" detection — find verses starting with sequences of "wa-X" oaths
# We use a simpler operational definition:
#   "qasam-trigger verse" = verse starting with "فلا أقسم" or "لا أقسم" or "أقسم"
#                           OR a verse that opens with "و" + by-noun-pattern (و + definite-article)
#                           AND part of a standard oath-cluster (3 or more such verses in sequence at surah head OR after مكة-like opener)
# But the META-OATH check only requires the trigger + the immediately following verse to contain qasam-self-reference.

META_OATH_KEYS = [
    'قسم', 'لقسم', 'بقسم',  # qasam roots
]

# For each surah, find triggers
hits = []
for s in Q:
    sid = s['id']
    verses = s['verses']
    for i, v in enumerate(verses):
        text = clean(v['text'])
        # Trigger: must start with qasam-formula OR a "wāw-bi-noun" oath (ambiguous; use conservative trigger)
        is_trigger = False
        first2 = ' '.join(text.split()[:2])
        if any(re.match(p, text) for p in [r'^فلا أقسم', r'^لا أقسم', r'^أقسم', r'^فأقسم']):
            is_trigger = True
            trigger_kind = 'uqsimu-explicit'
        # also: "و" oath — check if first word starts with "و" and is followed by a noun, AND surah opens with multi-oath
        # We restrict to explicit-uqsimu form for the META-OATH test (most defensible operationalization)
        if is_trigger and i+1 < len(verses):
            next_text = clean(verses[i+1]['text'])
            for k in META_OATH_KEYS:
                # Token-level check: a stand-alone token containing the qasam-root
                if re.search(r'(^|\s)(ل?قسم|بقسم|أقسم|قسم[^a-zA-Z]?)(\s|$)', next_text):
                    hits.append({'surah': sid, 'trigger_v': v['id'], 'trigger_text': text,
                                 'next_v': verses[i+1]['id'], 'next_text': next_text,
                                 'trigger_kind': trigger_kind})
                    break

print(f'Total META-OATH instances (uqsimu-explicit + next-verse contains qasam-noun):')
for h in hits:
    print(f"  Q{h['surah']}:{h['trigger_v']}-{h['next_v']}")
    print(f"    trig: {h['trigger_text']}")
    print(f"    next: {h['next_text']}")
    print()

surahs_with_meta = sorted(set(h['surah'] for h in hits))
print(f'Surahs with META-OATH: {surahs_with_meta}')
print(f'Count: {len(surahs_with_meta)}')

# Also: broader operationalization including wa-N oaths followed by qasam-self-reference
# Check standard "oath cluster + meta-statement" pattern by scanning ALL surahs with multi-oath openings.
# Wider scan: any verse containing "قسم" as a content noun + immediately preceded by oath-particle-laden verse(s)
print('\n=== BROADER SCAN: verses containing standalone qasam-noun ===')
qasam_noun_verses = []
for s in Q:
    for v in s['verses']:
        text = clean(v['text'])
        # tokens
        for tok in text.split():
            # standalone qasam-noun: قسم / لقسم / بقسم (not in compound that would change meaning)
            if tok in ('قسم','لقسم','بقسم','أقسم'):
                qasam_noun_verses.append((s['id'], v['id'], text, tok))
                break
print(f'Verses containing standalone qasam-noun token: {len(qasam_noun_verses)}')
for sid, vid, text, tok in qasam_noun_verses[:30]:
    print(f'  Q{sid}:{vid} [{tok}]: {text[:120]}')

# For each, check the previous verse — is it an oath?
print('\n=== Previous-verse-is-oath check for each qasam-noun verse ===')
meta_pairs = []
for sid, vid, text, tok in qasam_noun_verses:
    if vid == 1: continue  # no previous
    prev_v = next((v for v in Q[sid-1]['verses'] if v['id'] == vid-1), None)
    if not prev_v: continue
    prev_text = clean(prev_v['text'])
    # Is prev verse an oath? Triggers: starts with و + (article or by-noun), OR لا أقسم / أقسم
    is_oath = False
    if re.match(r'^(فلا أقسم|لا أقسم|أقسم|فأقسم)', prev_text):
        is_oath = True
    # OR starts with و + (article-prefixed noun) — e.g., والشمس, والنجم, والتين
    elif re.match(r'^و[ال][^\s]+', prev_text):  # wa-l-...
        is_oath = True
    elif re.match(r'^و[^\sالله]', prev_text) and len(prev_text.split()) <= 4:
        # short verse starting with wāw (but not والله / wa-allāh content)
        # only count if 1-3 words (typical oath form)
        is_oath = True
    if is_oath:
        meta_pairs.append({'surah': sid, 'oath_v': vid-1, 'oath_text': prev_text,
                           'meta_v': vid, 'meta_text': text})

print(f'\nMETA-OATH pairs (oath + qasam-self-reference):')
for h in meta_pairs:
    print(f"  Q{h['surah']}:{h['oath_v']}-{h['meta_v']}")
    print(f"    oath: {h['oath_text'][:100]}")
    print(f"    meta: {h['meta_text'][:100]}")

surahs_meta = sorted(set(h['surah'] for h in meta_pairs))
print(f'\nSurahs with META-OATH (broader scan): {surahs_meta}')
n = len(surahs_meta)
print(f'Count: {n}')

verdict = 'VINDICATED' if 1 <= n <= 3 else ('NULL-MORE-COMMON' if n > 3 else 'PIPELINE-BUG')
print(f'\nVERDICT: {verdict} (pre-reg: 1 ≤ count ≤ 3)')

result = {
    'test_id': 'Q056-F-03',
    'prereg_sha': EXPECTED_SHA,
    'narrow_uqsimu_explicit_meta_oaths': hits,
    'broader_meta_pairs': meta_pairs,
    'narrow_surahs': surahs_with_meta,
    'broader_surahs': surahs_meta,
    'narrow_count': len(surahs_with_meta),
    'broader_count': n,
    'verdict': verdict,
}

OUT = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/csv/Q056-F-03.json'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT,'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f'\nWrote {OUT}')
