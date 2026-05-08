#!/usr/bin/env python3
"""
Q050-F-01 — muqaṭṭaʿ + oath-wāw uniqueness audit.

For each of the 29 muqaṭṭaʿāt-opener surahs, check verse 1 to see whether
its muqaṭṭaʿ-letter sequence is immediately followed by an oath-particle
wāw (و) construction (i.e., 'وال' as start of next non-letter token).
"""
import hashlib, json, sys, re

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q050-qaf/preregs/Q050-F-01-muqattaa-oath-wow-prereg.md'
EXPECTED_SHA = '8ad78d219bf7ea2175724c65a1c215221329072c54830f895487d976b7a70fd8'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json') as f:
    qd = json.load(f)

mushaf_marks = ['۞', 'ۚ', 'ۖ', 'ۗ', 'ۛ', 'ۜ', '۠', '۩', 'ۭ']

# Canonical 29 muqaṭṭaʿāt openers (al-Suyūṭī catalogue)
muqattaat_surahs = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28,
                    29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46,
                    50, 68]

# Define the canonical muqaṭṭaʿ-letter strings as orthographic prefixes
# of verse 1 (no-tashkeel form) — derived empirically below by inspection.

def strip_marks(t):
    for m in mushaf_marks:
        t = t.replace(m, '')
    return ' '.join(t.split())

results_per_surah = []
match_count = 0
for s in muqattaat_surahs:
    q = qd[s - 1]
    v1 = strip_marks(q['verses'][0]['text'])
    tokens = v1.split()
    # Identify the muqaṭṭaʿ prefix: tokens that consist only of disconnected single
    # Arabic letters or short letter clusters at the start.
    # Canonical muqaṭṭaʿ tokens in no-tashkeel orthography:
    # - "الم" (3 letters, a single connected token)
    # - "المص"
    # - "المر"
    # - "الر"
    # - "كهيعص"
    # - "طه"
    # - "طسم"
    # - "طس"
    # - "يس"
    # - "ص"
    # - "حم"
    # - "حم عسق" (Q42 = HM + ʿSQ on two tokens or 'حم' + 'عسق')
    # - "ق"
    # - "ن"
    canonical_muqattaa_token_set = {
        'الم', 'المص', 'المر', 'الر',
        'كهيعص', 'طه', 'طسم', 'طس', 'يس',
        'ص', 'حم', 'عسق', 'ق', 'ن'
    }
    # Strip muqaṭṭaʿ-tokens from start
    i = 0
    muq_prefix_tokens = []
    while i < len(tokens) and tokens[i] in canonical_muqattaa_token_set:
        muq_prefix_tokens.append(tokens[i])
        i += 1
    rest = tokens[i:]
    first_after = rest[0] if rest else ''
    # Test: does first_after start with 'وال' (oath-wāw + definite article)?
    wow_oath_match = first_after.startswith('وال') if first_after else False
    # Also report if first_after starts with 'و' alone (oath-wāw only without al-)
    wow_only = first_after.startswith('و') if first_after else False

    results_per_surah.append({
        'surah': s,
        'verse_1_text': v1,
        'muqattaa_prefix_tokens': muq_prefix_tokens,
        'first_token_after_muqattaa': first_after,
        'matches_muqattaa_plus_oath_wow_al': wow_oath_match,
        'starts_with_wow': wow_only,
    })
    if wow_oath_match:
        match_count += 1

# Identify which surahs match
matching_surahs = [r['surah'] for r in results_per_surah if r['matches_muqattaa_plus_oath_wow_al']]

q50_match = (50 in matching_surahs)
q38_match = (38 in matching_surahs)

if q50_match and matching_surahs == [38, 50]:
    verdict = 'CONFIRMED-PAIR'
    interpretation = ('Q 50 and Q 38 are the ONLY two muqaṭṭaʿāt verse-1s with the muqaṭṭaʿ-letter '
                      '+ oath-wāw + definite-article construction. This is the singleton-letter cohort '
                      '(Q 50 ق, Q 38 ص) of muqaṭṭaʿāt openers; Q 68 ن is the third singleton but does '
                      'NOT use this construction at verse 1.')
elif q50_match and len(matching_surahs) == 1:
    verdict = 'CONFIRMED-UNIQUE'
    interpretation = 'Q 50:1 is the corpus-unique muqaṭṭaʿ + oath-wāw + al- construction.'
elif q50_match and len(matching_surahs) >= 3:
    verdict = 'NULL'
    interpretation = f'Pattern not unique: {len(matching_surahs)} muqaṭṭaʿāt verses match.'
elif not q50_match:
    verdict = 'NULL-Q50-MISS'
    interpretation = ('PRE-COMMIT VIOLATION: Q 50 itself does not match the construction as parsed. '
                      'Re-check token tokenization.')
else:
    verdict = 'OTHER'
    interpretation = f'Matching surahs: {matching_surahs}'

output = {
    'finding_id': 'Q050-F-01',
    'prereg_sha256': actual_sha,
    'date_run': '2026-05-07',
    'rules_tuple': '(no-tashkeel, orthographic-token, exact substring match after Quranic-mark stripping, basmala-not-counted-in-Q50, Hafs-Kufan, mushaf-order)',
    'muqattaat_surahs_tested': muqattaat_surahs,
    'matching_surahs_count': match_count,
    'matching_surahs_list': matching_surahs,
    'per_surah_diagnostic': results_per_surah,
    'verdict': verdict,
    'interpretation': interpretation,
}

out_path = f'{PROJECT}/surahs/Q050-qaf/csv/Q050-F-01.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q050-F-01: VERDICT={verdict}')
print(f'  matching_surahs_count: {match_count}')
print(f'  matching_surahs: {matching_surahs}')
print(f'  Output: {out_path}')
