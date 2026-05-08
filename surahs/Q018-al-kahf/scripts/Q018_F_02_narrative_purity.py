#!/usr/bin/env python3
"""Q018-F-02: Narrative-purity rank — Q 18 vs Q 12 (LOCKED pre-reg).

Replicates the Q012-F-01 narrative-purity index across all 114 surahs,
finds Q 18's rank, and tests Direction A (Q 18 in top 25%) and Direction B
(Q 18 ranks lower than Q 12).
"""
import json, re, hashlib, os

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q018-al-kahf/preregs/Q018-F-02-narrative-purity-vs-Q12-prereg.md"
QURAN = f"{PROJECT}/quran-text/quran-no-tashkeel.json"
OUT = f"{PROJECT}/surahs/Q018-al-kahf/csv/Q018-F-02.json"

# 1. Lock the marker set (IDENTICAL to Q012-F-01)
SPEECH_MARKERS = ['قال', 'قالت', 'قالوا', 'قلنا', 'قل']
SEQ_MARKERS = ['فلما', 'ولما', 'إذ', 'إذا', 'ثم', 'بينما']
STATE_MARKERS = ['كان', 'وكان']
EVENT_MARKERS = ['جاء', 'جاءت', 'جاءوا', 'ذهب', 'ذهبوا', 'أتى', 'أتوا']
VISUAL_MARKERS = ['رأى', 'رأيت', 'رأوا']
SEND_MARKERS = ['أرسل', 'بعث']
ALL_MARKERS = SPEECH_MARKERS + SEQ_MARKERS + STATE_MARKERS + EVENT_MARKERS + VISUAL_MARKERS + SEND_MARKERS

MUSHAF_RE = re.compile(r'[۞۩ۚۖۗۛۧۜ]')

# 2. SHA-check pre-reg
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256: {sha}")

# 3. Load Quran
q = json.load(open(QURAN))

# 4. Compute per-surah narrative metrics
results = []
for s in q:
    sid = s['id']
    verses_w_marker = 0
    total_marker_tokens = 0
    total_words = 0
    total_verses = len(s['verses'])
    for v in s['verses']:
        text = MUSHAF_RE.sub('', v['text'])
        words = text.split()
        total_words += len(words)
        # Word-boundary regex
        marker_count_in_verse = 0
        for marker in ALL_MARKERS:
            # Word-boundary match
            for w in words:
                if w == marker:
                    marker_count_in_verse += 1
                    total_marker_tokens += 1
        if marker_count_in_verse > 0:
            verses_w_marker += 1
    frac = verses_w_marker / total_verses if total_verses else 0
    density = total_marker_tokens / total_words if total_words else 0
    score = 0.5 * frac + 0.5 * (density / 0.30)
    results.append({
        'surah': sid,
        'frac_narrative_verses': frac,
        'marker_density_per_word': density,
        'narrative_purity_score': score,
        'verses_w_marker': verses_w_marker,
        'total_verses': total_verses,
        'total_marker_tokens': total_marker_tokens,
        'total_words': total_words,
    })

# 5. Rank by frac_narrative_verses
ranked_frac = sorted(results, key=lambda r: -r['frac_narrative_verses'])
ranked_score = sorted(results, key=lambda r: -r['narrative_purity_score'])
ranked_density = sorted(results, key=lambda r: -r['marker_density_per_word'])

q18_rank_frac = next(i+1 for i, r in enumerate(ranked_frac) if r['surah'] == 18)
q12_rank_frac = next(i+1 for i, r in enumerate(ranked_frac) if r['surah'] == 12)
q18_rank_score = next(i+1 for i, r in enumerate(ranked_score) if r['surah'] == 18)
q12_rank_score = next(i+1 for i, r in enumerate(ranked_score) if r['surah'] == 12)
q18_rank_density = next(i+1 for i, r in enumerate(ranked_density) if r['surah'] == 18)
q12_rank_density = next(i+1 for i, r in enumerate(ranked_density) if r['surah'] == 12)

q18_data = next(r for r in results if r['surah'] == 18)
q12_data = next(r for r in results if r['surah'] == 12)

# 6. Verdicts
direction_A = (q18_rank_frac <= 28)
direction_B = (q18_rank_frac > q12_rank_frac)

if direction_A and direction_B:
    verdict = 'CONFIRMED'
elif direction_A:
    verdict = 'PARTIAL_A_only'
elif direction_B:
    verdict = 'PARTIAL_B_only'
else:
    verdict = 'NULL'

print(f'Q 18 rank by frac_narrative_verses: {q18_rank_frac}/114 (frac={q18_data["frac_narrative_verses"]:.4f})')
print(f'Q 12 rank by frac_narrative_verses: {q12_rank_frac}/114 (frac={q12_data["frac_narrative_verses"]:.4f})')
print(f'Q 18 rank by narrative_purity_score: {q18_rank_score}/114 (score={q18_data["narrative_purity_score"]:.4f})')
print(f'Q 12 rank by narrative_purity_score: {q12_rank_score}/114 (score={q12_data["narrative_purity_score"]:.4f})')
print(f'Direction A (Q 18 ≤ 28): {direction_A}')
print(f'Direction B (Q 18 > Q 12): {direction_B}')
print(f'Verdict: {verdict}')

result = {
    'finding_id': 'Q018-F-02',
    'pre_reg_sha256': sha,
    'verdict': verdict,
    'direction_A_top25_pass': direction_A,
    'direction_B_below_Q12': direction_B,
    'q18_rank_frac': q18_rank_frac,
    'q12_rank_frac': q12_rank_frac,
    'q18_rank_score': q18_rank_score,
    'q12_rank_score': q12_rank_score,
    'q18_rank_density': q18_rank_density,
    'q12_rank_density': q12_rank_density,
    'q18_data': q18_data,
    'q12_data': q12_data,
    'top_15_by_frac': [r['surah'] for r in ranked_frac[:15]],
    'top_15_by_score': [r['surah'] for r in ranked_score[:15]],
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, default=str)
print(f'\nWritten to {OUT}')
