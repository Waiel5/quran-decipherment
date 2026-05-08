#!/usr/bin/env python3
"""Q006-F-03 — Tawḥīd-anti-idolatry lexical density across 114 surahs.

Pre-reg: surahs/Q006-al-anam/Q006-F-03-tawhid-density-prereg.md
Pre-reg SHA-256 (locked): e5a3c300577299a1f29fa1b6c8c1408dee4b165cb86a68946bf9d781ea3ff4dc
Direction: TOP-3 / HIGH-DENSITY (LOCKED)
Bonferroni k=2, alpha_bon=0.025
Rules-tuple: (no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q006-al-anam/Q006-F-03-tawhid-density-prereg.md'
EXPECTED_SHA = 'e5a3c300577299a1f29fa1b6c8c1408dee4b165cb86a68946bf9d781ea3ff4dc'
TXT = ROOT / 'quran-text/quran-no-tashkeel.json'
OUT = ROOT / 'surahs/Q006-al-anam/csv/Q006-F-03.json'

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: {sha} != {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

# Locked tawḥīd cluster patterns
PATTERNS = {
    'la_ilaha_illa':  re.compile(r'لا\s+إله\s+إلا'),
    'la_sharika':     re.compile(r'لا\s+شريك'),
    'sharik_family':  re.compile(r'(?<![ا-ي])(?:ال|ب|ل|و|ف)?(?:شريك|شركاء|شركاؤ|شركائ|شركاءه|شركاءك)\w*(?![ا-ي])'),
    'wahdah':         re.compile(r'(?<![ا-ي])وحده(?![ا-ي])'),
    'ittakhadh_walad': re.compile(r'اتخذ\w*\s+\S*\s*ولد'),
    'shirk_verbs':    re.compile(r'(?<![ا-ي])(?:يشركون|أشركوا|أشركتم|تشركوا|تشركون|أشرك|يشرك|أشركوا|يشركن|تشركون)(?![ا-ي])'),
    'al_shirk':       re.compile(r'(?<![ا-ي])الشرك(?![ا-ي])'),
    'al_wahid':       re.compile(r'(?<![ا-ي])الواحد(?![ا-ي])'),
}

txt = json.load(open(TXT))

per_surah = {}
for s in txt:
    sid = s['id']
    n_verses = len(s['verses'])
    n_words = 0
    counts = {k: 0 for k in PATTERNS}
    sample = []
    for v in s['verses']:
        text = v['text']
        n_words += len(text.split())
        for k, pat in PATTERNS.items():
            ms = pat.findall(text)
            if ms:
                counts[k] += len(ms)
                if len(sample) < 6:
                    sample.append({'verse': v['id'], 'cluster': k, 'tokens': ms[:3]})
    total = sum(counts.values())
    per_surah[sid] = {
        'surah': sid,
        'n_verses': n_verses,
        'n_words': n_words,
        'cell_A_total_count': total,
        'per_cluster_counts': counts,
        'cell_B_density_per_100w': (total / n_words * 100) if n_words else 0.0,
        'sample': sample,
    }

ranked_A = sorted(per_surah.values(), key=lambda x: (-x['cell_A_total_count'], x['surah']))
# Cell B eligibility: ≥2 tokens (more permissive given short tawḥīd surahs are pre-registered as legitimate)
eligible_B = [v for v in per_surah.values() if v['cell_A_total_count'] >= 2]
ranked_B = sorted(eligible_B, key=lambda x: (-x['cell_B_density_per_100w'], x['surah']))

q6_a_rank = next(i + 1 for i, it in enumerate(ranked_A) if it['surah'] == 6)
q6_b_rank = next(i + 1 for i, it in enumerate(ranked_B) if it['surah'] == 6)
q1_b_rank = next((i + 1 for i, it in enumerate(ranked_B) if it['surah'] == 1), None)
q112_b_rank = next((i + 1 for i, it in enumerate(ranked_B) if it['surah'] == 112), None)

# Verdict
if q6_b_rank <= 3:
    verdict = 'CONFIRMED'
elif q6_b_rank <= 5:
    verdict = 'DIRECTIONAL'
elif q6_b_rank >= 10:
    verdict = 'PRE_COMMIT_VIOLATION'
else:
    verdict = 'NULL'

result = {
    'test_id': 'Q006-F-03',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': 20260507,
    'direction_locked': 'TOP-3-HIGH-DENSITY',
    'bonferroni_k': 2,
    'alpha_bon': 0.025,
    'rules_tuple': '(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'cluster_terms': list(PATTERNS.keys()),
    'q6_cell_A_total_count': per_surah[6]['cell_A_total_count'],
    'q6_per_cluster_counts': per_surah[6]['per_cluster_counts'],
    'q6_cell_A_rank': q6_a_rank,
    'q6_cell_B_density_per_100w': per_surah[6]['cell_B_density_per_100w'],
    'q6_cell_B_rank': q6_b_rank,
    'q6_n_words': per_surah[6]['n_words'],
    'q1_cell_B_rank': q1_b_rank,
    'q112_cell_B_rank': q112_b_rank,
    'q1_density_per_100w': per_surah[1]['cell_B_density_per_100w'],
    'q112_density_per_100w': per_surah[112]['cell_B_density_per_100w'],
    'verdict': verdict,
    'top15_cell_B': [
        {'rank': i + 1, 'surah': it['surah'], 'density_per_100w': it['cell_B_density_per_100w'],
         'total_count': it['cell_A_total_count'], 'n_words': it['n_words'],
         'cluster_breakdown': it['per_cluster_counts']}
        for i, it in enumerate(ranked_B[:15])
    ],
    'top10_cell_A': [
        {'rank': i + 1, 'surah': it['surah'], 'total_count': it['cell_A_total_count'],
         'cluster_breakdown': it['per_cluster_counts']}
        for i, it in enumerate(ranked_A[:10])
    ],
    'q6_sample_matches': per_surah[6]['sample'],
    'honest_limits': [
        '8-cluster regex set (locked) covering la_ilaha_illa, la_sharika, sharik_family, wahdah, ittakhadh_walad, shirk_verbs, al_shirk, al_wahid.',
        'Cell B eligibility: ≥2 tokens (allows formulaic short surahs like Q 112 to participate).',
        'Pure tawḥīd-DECLARATIVE (Q 112) and tawḥīd-POLEMIC (Q 6) both contribute; metric is theological-vocabulary density, not narrowly anti-idolatry.',
        'Q 109 al-Kāfirūn is a co-competitor at the top.',
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q006-F-03: Cell A (total count) = {per_surah[6]["cell_A_total_count"]}, rank A = {q6_a_rank}/114', file=sys.stderr)
print(f'Q006-F-03: Cell B (density per 100w) = {per_surah[6]["cell_B_density_per_100w"]:.3f}, rank B = {q6_b_rank}/{len(eligible_B)}', file=sys.stderr)
print(f'Q1 rank B = {q1_b_rank}; Q112 rank B = {q112_b_rank}', file=sys.stderr)
print(f'Verdict: {verdict}', file=sys.stderr)
print(f'Output: {OUT}', file=sys.stderr)
