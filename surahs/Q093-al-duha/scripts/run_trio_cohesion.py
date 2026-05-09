"""Q093F02: Q 92+Q 93+Q 94 trio FR cohesion (4 null pools).

Pre-reg: surahs/Q093-al-duha/preregs/Q093F02-trio-cohesion.md (SHA-locked).
"""
import json
import statistics
import random

SEED = 20260509
N_PERM = 10000

h111 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
D = [[0.0] * 115 for _ in range(115)]
for a, b, dist in h111['D_matrix_upper_triangular']:
    D[a][b] = dist
    D[b][a] = dist


def mean_intra(c):
    pairs = [D[a][b] for i, a in enumerate(c) for b in c[i + 1:]]
    return statistics.mean(pairs)


def perm_test(cluster, pool, label):
    random.seed(SEED)
    obs = mean_intra(cluster)
    nulls = []
    for _ in range(N_PERM):
        rand = random.sample(pool, len(cluster))
        nulls.append(mean_intra(rand))
    null_mean = statistics.mean(nulls)
    null_sd = statistics.stdev(nulls)
    p_lower = sum(1 for n in nulls if n <= obs) / N_PERM
    z = (obs - null_mean) / null_sd
    return {
        'label': label, 'cluster': cluster, 'pool_size': len(pool),
        'obs': obs, 'null_mean': null_mean, 'null_sd': null_sd,
        'z': z, 'p_lower': p_lower, 'n_perm': N_PERM, 'seed': SEED,
    }


results = {
    'finding_id': 'Q093F02',
    'title': 'Q 92 + Q 93 + Q 94 trio FR cohesion',
    'date': '2026-05-09',
    'rules_tuple': {
        'orthography': 'no-tashkeel',
        'verse_numbering': 'hafs-kufan',
        'feature': 'root-distribution Fisher-Rao distance (h-new-111)',
        'null_model': 'random-triple-from-pool',
        'n_perm': N_PERM,
        'seed': SEED,
    },
    'tests': {
        'F02a_corpus': perm_test([92, 93, 94], list(range(1, 115)), 'trio vs corpus triple'),
        'F02b_mufaṣṣal': perm_test([92, 93, 94], list(range(49, 115)), 'trio vs mufaṣṣal Q49-114 triple'),
        'F02c_short_mufaṣṣal': perm_test([92, 93, 94], list(range(78, 115)), 'trio vs short-mufaṣṣal Q78-114 triple'),
        'F02d_qiṣār': perm_test([92, 93, 94], list(range(89, 115)), 'trio vs qiṣār Q89-114 triple'),
    },
}

results['bonferroni'] = {
    'k': 4, 'family': 'Q093F02-trio-cohesion-4-pools',
    'alpha': 0.05, 'alpha_bon': 0.05 / 4,
    'pre_committed_pools': ['F02a_corpus', 'F02b_mufaṣṣal', 'F02c_short_mufaṣṣal', 'F02d_qiṣār'],
}

verdicts = []
for k in results['bonferroni']['pre_committed_pools']:
    p = results['tests'][k]['p_lower']
    if p < results['bonferroni']['alpha_bon']:
        verdicts.append((k, 'PASS'))
    elif p < 0.05:
        verdicts.append((k, 'PASS-DIRECTED'))
    else:
        verdicts.append((k, 'NULL'))
results['verdicts'] = verdicts

print("=== Q093F02 Q 92+Q 93+Q 94 TRIO FR cohesion ===")
for k in results['bonferroni']['pre_committed_pools']:
    t = results['tests'][k]
    print(f"  {t['label']}: obs={t['obs']:.4f}  null_mean={t['null_mean']:.4f}  z={t['z']:+.3f}  p_lower={t['p_lower']:.5f}")
print()
print(f"Bonferroni k=4 → α_bon = {results['bonferroni']['alpha_bon']:.4f}")
for k, v in verdicts:
    print(f"  {k}: {v}")

with open('/Users/grey/Downloads/quran/surahs/Q093-al-duha/csv/Q093F02-trio-cohesion.json', 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print("\nWritten to surahs/Q093-al-duha/csv/Q093F02-trio-cohesion.json")
