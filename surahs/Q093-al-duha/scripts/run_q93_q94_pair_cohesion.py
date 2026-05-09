"""Q093F01: Q 93 ↔ Q 94 PAIR FR cohesion (3 null pools).

Pre-reg: surahs/Q093-al-duha/preregs/Q093F01-pair-cohesion.md (SHA-locked).

Outputs JSON to surahs/Q093-al-duha/csv/Q093F01-pair-cohesion.json
"""
import json
import statistics
import random

SEED = 20260509
N_PERM = 10000

# Load FR matrix (locked instrument under MW-6)
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
        'label': label,
        'cluster': cluster,
        'pool_size': len(pool),
        'obs': obs,
        'null_mean': null_mean,
        'null_sd': null_sd,
        'z': z,
        'p_lower': p_lower,
        'n_perm': N_PERM,
        'seed': SEED,
    }


# Three null pools, pre-registered
results = {
    'finding_id': 'Q093F01',
    'title': 'Q 93 al-Ḍuḥā ↔ Q 94 al-Sharḥ PAIR FR cohesion',
    'date': '2026-05-09',
    'rules_tuple': {
        'orthography': 'no-tashkeel',
        'verse_numbering': 'hafs-kufan',
        'feature': 'root-distribution Fisher-Rao distance (h-new-111)',
        'instrument': 'h-new-111.json (locked, ex-ante)',
        'null_model': 'random-pair-from-pool',
        'n_perm': N_PERM,
        'seed': SEED,
    },
    'tests': {
        'F01a_corpus_pool': perm_test([93, 94], list(range(1, 115)), 'pair vs all-corpus pair'),
        'F01b_mufaṣṣal_Q49_114': perm_test([93, 94], list(range(49, 115)), 'pair vs mufaṣṣal Q49-114 pair'),
        'F01c_short_mufaṣṣal_Q78_114': perm_test([93, 94], list(range(78, 115)), 'pair vs short-mufaṣṣal Q78-114 pair'),
        'F01d_qiṣār_Q89_114': perm_test([93, 94], list(range(89, 115)), 'pair vs qiṣār Q89-114 pair'),
    },
    'corpus_rank': None,  # filled below
}

# Compute corpus-wide rank
all_pairs = [(a, b, D[a][b]) for a in range(1, 115) for b in range(a + 1, 115)]
all_pairs.sort(key=lambda x: x[2])
for i, (a, b, d) in enumerate(all_pairs, 1):
    if (a, b) == (93, 94):
        results['corpus_rank'] = {'rank': i, 'total': len(all_pairs), 'percentile': i / len(all_pairs) * 100, 'distance': d}
        break

# Bonferroni — pre-registered family of 3 nulls (a + b + c) with d as exploratory-replication
results['bonferroni'] = {
    'k': 3,
    'family': 'Q093F01-pair-cohesion-3-pools',
    'alpha': 0.05,
    'alpha_bon': 0.05 / 3,
    'pre_committed_pools': ['F01a_corpus_pool', 'F01b_mufaṣṣal_Q49_114', 'F01c_short_mufaṣṣal_Q78_114'],
    'exploratory_replication': ['F01d_qiṣār_Q89_114'],
}

# Verdict logic
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

print("=== Q093F01 Q 93 ↔ Q 94 PAIR FR cohesion ===")
for k in ['F01a_corpus_pool', 'F01b_mufaṣṣal_Q49_114', 'F01c_short_mufaṣṣal_Q78_114', 'F01d_qiṣār_Q89_114']:
    t = results['tests'][k]
    print(f"  {t['label']}: obs={t['obs']:.4f}  null_mean={t['null_mean']:.4f}  z={t['z']:+.3f}  p_lower={t['p_lower']:.5f}")
print()
print(f"Bonferroni k={results['bonferroni']['k']} → α_bon = {results['bonferroni']['alpha_bon']:.4f}")
for k, v in verdicts:
    print(f"  {k}: {v}")
print()
print(f"Q 93↔Q 94 corpus rank: {results['corpus_rank']['rank']}/{results['corpus_rank']['total']} ({results['corpus_rank']['percentile']:.2f}%)")

with open('/Users/grey/Downloads/quran/surahs/Q093-al-duha/csv/Q093F01-pair-cohesion.json', 'w') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print("\nWritten to surahs/Q093-al-duha/csv/Q093F01-pair-cohesion.json")
