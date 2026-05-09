"""Q092F01: Q 92 al-Layl is the corpus-UNIQUE yāʾ-monorhyme surah.

Anchor: Q 92 has rhyme_entropy=0.0 (perfect monorhyme) AND top_final_letter='ي'.
Among the 15 perfect-monorhyme surahs, this is the ONLY ya-final one.
Verify against h-new-750.json + h-new-700.json.
"""
import json

h750 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json'))

results = {
    'finding_id': 'Q092F01',
    'title': 'Q 92 al-Layl is the corpus-UNIQUE yāʾ-monorhyme surah',
    'date': '2026-05-09',
    'instrument': 'h-new-750.json (locked rhyme/iʿjāz instrument)',
    'rules_tuple': {
        'orthography': 'no-tashkeel', 'verse_numbering': 'hafs-kufan',
        'feature': 'verse-final letter, rhyme-entropy = Shannon nats over per-surah final letter distribution',
    },
}

# Find all perfect-monorhyme surahs
perfect = [s for s in h750['per_surah'] if s['rhyme_entropy_nats'] == 0.0]
perfect.sort(key=lambda x: -x['n_verses'])
results['n_perfect_monorhyme'] = len(perfect)
results['perfect_monorhyme_surahs'] = [
    {'surah': s['surah'], 'n_verses': s['n_verses'], 'top_final_letter': s['top_final_letter'], 'mean_FR': s['mean_content_distance']}
    for s in perfect
]

# Group by terminal letter
from collections import Counter
terminal_counts = Counter(s['top_final_letter'] for s in perfect)
results['terminal_letter_distribution'] = dict(terminal_counts)

# Q 92 specifically
q92 = next(s for s in h750['per_surah'] if s['surah'] == 92)
results['Q92'] = q92

# Verdict
yaa_perfect = [s for s in perfect if s['top_final_letter'] == 'ي']
results['n_yaa_perfect_monorhyme'] = len(yaa_perfect)
results['Q92_unique_yaa_perfect'] = (len(yaa_perfect) == 1 and yaa_perfect[0]['surah'] == 92)
results['verdict'] = 'CORPUS-EXACT-1-OF-1' if results['Q92_unique_yaa_perfect'] else 'NOT-UNIQUE'

# Among Q 92's nearest 8 FR neighbors (from H-NEW-111), how many are perfect-monorhyme?
h111 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
D = [[0.0] * 115 for _ in range(115)]
for a, b, dist in h111['D_matrix_upper_triangular']:
    D[a][b] = dist
    D[b][a] = dist

q92_neighbors = sorted([(t, D[92][t]) for t in range(1, 115) if t != 92], key=lambda x: x[1])[:10]
perfect_set = {s['surah'] for s in perfect}
neighbor_perfect = [(t, d, t in perfect_set) for t, d in q92_neighbors]
results['Q92_top10_neighbors_with_monorhyme_flag'] = neighbor_perfect

print("=== Q092F01: Q 92 al-Layl yāʾ-monorhyme uniqueness ===")
print()
print(f"All 15 perfect-monorhyme surahs (rhyme entropy = 0):")
for s in perfect:
    print(f"  Q{s['surah']:>3}  n_verses={s['n_verses']:>3}  terminal={s['top_final_letter']}  mean_FR={s['mean_content_distance']:.4f}")
print()
print(f"Terminal-letter distribution: {dict(terminal_counts)}")
print()
print(f"Yāʾ-perfect-monorhyme surahs: {len(yaa_perfect)}")
for s in yaa_perfect:
    print(f"  Q{s['surah']}")
print()
print(f"VERDICT: {results['verdict']}")
print()
print(f"Q 92's top-10 FR neighbors (perfect-monorhyme flag):")
for t, d, is_pm in neighbor_perfect:
    print(f"  Q{t:>3} {d:.4f} {'PERFECT-MONORHYME' if is_pm else ''}")

with open('/Users/grey/Downloads/quran/surahs/Q092-al-layl/csv/Q092F01-yaa-monorhyme.json', 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print("\nWritten to surahs/Q092-al-layl/csv/Q092F01-yaa-monorhyme.json")
