#!/usr/bin/env python3
"""H-NEW-2280 — al-Biqāʿī munāsabah SEAM-cohesion test (pericope-scoped).

Tests Burhān al-Dīn al-Biqāʿī's doctrine (*Naẓm al-durar fī tanāsub al-āyāt
wa-l-suwar*) that each sūra coheres with its successor — at the granularity
al-Biqāʿī actually uses: the BOUNDARY pericope, not the whole sūra. For all 113
canonical mushaf adjacencies (Q N → Q N+1), compute the root-Jaccard between the
LAST pericope (last min(k,len) verses) of sūra N and the FIRST pericope (first
min(k,len) verses) of sūra N+1, and compare the corpus mean to a permutation
null that scrambles the adjacency relation while reusing the SAME real
pericopes (non-adjacent last/first pairing).

Direction LOCKED before computation: canonical-seam cohesion > random-pair
baseline (z > 0, one-tailed greater). A reversed result (z < 0) is a
pre-commit-violation published as NULL with prominence — it would mean
munāsabah is NOT a seam-lexical (shared-root) effect, refining al-Biqāʿī.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2280-munasabah-seam.md
Pre-reg SHA256: f48df847e1e6559d9a610ef8cfc6159a48eed81fe64909bd9297fa3076d4014d

Seed 20260509, n_perm=10000. k in {3, 5} (primary k=3; replication k=5).
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(
    PROJECT_ROOT,
    'findings/phase-b-hypotheses/prereg-h-new-2280-munasabah-seam.md',
)
EXPECTED_SHA = 'f48df847e1e6559d9a610ef8cfc6159a48eed81fe64909bd9297fa3076d4014d'
SEED = 20260509
SEED_REPLICATE = 20260510
N_PERM = 10000
K_VALUES = [3, 5]               # primary k=3, replication k=5
BONFERRONI_K = len(K_VALUES)    # family size = 2
ALPHA_CORR = 0.05 / BONFERRONI_K

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_NO_TASHKEEL = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-2280.json')

N_SURAHS = 114
# Bismillāh-less famous classical munāsabah seam (al-Biqāʿī; al-Tirmidhī #3170)
NAMED_SEAM = (8, 9)


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(
            f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}",
            file=sys.stderr,
        )
        sys.exit(1)


def load_surah_lengths():
    text = json.load(open(QURAN_NO_TASHKEEL))
    lengths = {}
    names = {}
    for s in text:
        sid = int(s['id'])
        lengths[sid] = len(s['verses'])
        names[sid] = s.get('transliteration', s.get('name', str(sid)))
    assert len(lengths) == N_SURAHS, f'expected {N_SURAHS} surahs, got {len(lengths)}'
    return lengths, names


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4.

    Identical convention to h-new-1380.py / h-new-1510.py / h-new-1520.py /
    h-new-1760.py: takes the first ROOT-tagged feature per morphological
    segment.
    """
    verse_roots = defaultdict(set)
    with open(MORPH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            loc_clean = loc.strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc_clean.split(':'))
            except ValueError:
                continue
            for tok in features.split('|'):
                if tok.startswith('ROOT:'):
                    root = tok[len('ROOT:'):]
                    verse_roots[(s, v)].add(root)
                    break
    return dict(verse_roots)


def first_pericope_roots(verse_roots, sid, length, k):
    """Union of ROOTs over the first min(k, length) verses of surah sid."""
    kk = min(k, length)
    out = set()
    for v in range(1, kk + 1):
        out |= verse_roots.get((sid, v), set())
    return out


def last_pericope_roots(verse_roots, sid, length, k):
    """Union of ROOTs over the last min(k, length) verses of surah sid."""
    kk = min(k, length)
    out = set()
    for v in range(length - kk + 1, length + 1):
        out |= verse_roots.get((sid, v), set())
    return out


def jaccard(a, b):
    u = a | b
    if not u:
        return 0.0
    return len(a & b) / len(u)


def run_for_k(k, verse_roots, lengths, names, seed):
    # Precompute every surah's last-pericope and first-pericope root-set once.
    last_roots = {sid: last_pericope_roots(verse_roots, sid, lengths[sid], k)
                  for sid in range(1, N_SURAHS + 1)}
    first_roots = {sid: first_pericope_roots(verse_roots, sid, lengths[sid], k)
                   for sid in range(1, N_SURAHS + 1)}

    # Observed: 113 canonical adjacencies N -> N+1
    per_seam = []
    obs_Js = []
    for N in range(1, N_SURAHS):  # 1..113
        a = last_roots[N]
        b = first_roots[N + 1]
        J = jaccard(a, b)
        obs_Js.append(J)
        per_seam.append({
            'seam': f'Q{N}->Q{N+1}',
            'N': N,
            'N1': N + 1,
            'name_N': names[N],
            'name_N1': names[N + 1],
            'last_k': min(k, lengths[N]),
            'first_k': min(k, lengths[N + 1]),
            'n_last_roots': len(a),
            'n_first_roots': len(b),
            'inter': len(a & b),
            'union': len(a | b),
            'shared_roots': sorted(a & b),
            'jaccard': J,
        })
    obs_mean = sum(obs_Js) / len(obs_Js)

    # Permutation null: 113 random (last_a, first_b) pairs with b != a and
    # b != a+1 (non-canonical-successor, non-self). Reuses the SAME real
    # pericopes; scrambles ONLY the adjacency relation.
    rng = random.Random(seed)
    all_ids = list(range(1, N_SURAHS + 1))
    null_means = []
    for _ in range(N_PERM):
        vals = []
        # mirror the 113 canonical draws: for each canonical N, pick a random
        # last-pericope surah a and a random first-pericope surah b that is not
        # the canonical successor of a and not a itself.
        for _draw in range(N_SURAHS - 1):  # 113 draws
            a = rng.choice(all_ids)
            while True:
                b = rng.choice(all_ids)
                if b != a and b != a + 1:
                    break
            vals.append(jaccard(last_roots[a], first_roots[b]))
        null_means.append(sum(vals) / len(vals))

    null_mean = sum(null_means) / len(null_means)
    null_std = (sum((x - null_mean) ** 2 for x in null_means) / len(null_means)) ** 0.5
    z = (obs_mean - null_mean) / null_std if null_std > 0 else float('nan')
    n_ge = sum(1 for x in null_means if x >= obs_mean)
    p_greater = n_ge / N_PERM
    p_report = (1.0 / N_PERM) if n_ge == 0 else p_greater

    direction_match = obs_mean > null_mean
    pre_commit_violation = obs_mean < null_mean

    if pre_commit_violation:
        verdict = 'PRE-COMMIT-VIOLATION (NULL with prominence)'
    elif direction_match and p_greater < ALPHA_CORR:
        verdict = 'PASS-DIRECTED (Bonferroni)'
    elif direction_match and p_greater < 0.05:
        verdict = 'PASS-DIRECTED (raw only; misses Bonferroni)'
    elif direction_match:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # Rankings
    ranked = sorted(per_seam, key=lambda d: d['jaccard'], reverse=True)
    top10 = ranked[:10]
    bottom10 = ranked[-10:]
    named = next(d for d in per_seam
                 if d['N'] == NAMED_SEAM[0] and d['N1'] == NAMED_SEAM[1])
    named_rank = 1 + [d['seam'] for d in ranked].index(named['seam'])

    return {
        'k': k,
        'seed': seed,
        'n_adjacencies': len(obs_Js),
        'observed_mean_seam_jaccard': obs_mean,
        'null_mean': null_mean,
        'null_std': null_std,
        'z_score': z,
        'p_greater_perm': p_greater,
        'p_reportable_upper_bound': p_report,
        'n_perm_ge_obs': n_ge,
        'alpha_bonferroni': ALPHA_CORR,
        'direction_locked': 'canonical-seam > random-pair (z > 0)',
        'direction_match': direction_match,
        'pre_commit_violation': pre_commit_violation,
        'verdict': verdict,
        'named_seam_Q8_Q9': {
            'seam': named['seam'],
            'jaccard': named['jaccard'],
            'inter': named['inter'],
            'union': named['union'],
            'shared_roots': named['shared_roots'],
            'rank_of_113': named_rank,
        },
        'top10_strongest_seams': [
            {'seam': d['seam'], 'name_N': d['name_N'], 'name_N1': d['name_N1'],
             'jaccard': d['jaccard'], 'inter': d['inter'], 'union': d['union'],
             'shared_roots': d['shared_roots']}
            for d in top10
        ],
        'bottom10_weakest_seams': [
            {'seam': d['seam'], 'name_N': d['name_N'], 'name_N1': d['name_N1'],
             'jaccard': d['jaccard'], 'inter': d['inter'], 'union': d['union']}
            for d in bottom10
        ],
        'per_seam': per_seam,
    }


def main():
    verify_sha()
    lengths, names = load_surah_lengths()
    verse_roots = load_qac_roots_by_verse()

    results = {}
    for k in K_VALUES:
        results[f'k{k}'] = run_for_k(k, verse_roots, lengths, names, SEED)

    # MW-5 second-seed replicate at primary k=3
    replicate_k3 = run_for_k(3, verse_roots, lengths, names, SEED_REPLICATE)

    primary = results['k3']
    overall_pass = (
        primary['verdict'].startswith('PASS-DIRECTED')
        and results['k5']['verdict'].startswith(('PASS-DIRECTED', 'DIRECTIONAL'))
    )

    out = {
        'finding_id': 'H-NEW-2280',
        'title': 'al-Biqāʿī munāsabah seam-cohesion test (pericope-scoped at the surah-pair seam)',
        'prereg_sha': EXPECTED_SHA,
        'seed_primary': SEED,
        'seed_replicate': SEED_REPLICATE,
        'n_perm': N_PERM,
        'k_values': K_VALUES,
        'primary_k': 3,
        'bonferroni_k': BONFERRONI_K,
        'alpha_bonferroni': ALPHA_CORR,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'null_model': 'random non-adjacent last/first pericope pairing (b != a, b != a+1); same real pericopes, scrambled adjacency',
        'aggregation_scale': 'seam pericope (last min(k,len) verses of N vs first min(k,len) verses of N+1)',
        'classical_claim': 'al-Biqāʿī, Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar — each sūra coheres with its successor; seam is the locus of munāsabah. Famous case: Q8 al-Anfāl -> Q9 al-Tawba (basmala-less seam; al-Tirmidhī idInBook #3170).',
        'direction_locked': 'canonical-seam cohesion > random-pair baseline (z > 0, one-tailed greater)',
        'results_by_k': results,
        'replicate_k3_seed20260510': {
            'k': replicate_k3['k'], 'seed': replicate_k3['seed'],
            'observed_mean_seam_jaccard': replicate_k3['observed_mean_seam_jaccard'],
            'null_mean': replicate_k3['null_mean'], 'null_std': replicate_k3['null_std'],
            'z_score': replicate_k3['z_score'], 'p_greater_perm': replicate_k3['p_greater_perm'],
            'verdict': replicate_k3['verdict'],
        },
        'overall_pass_both_k': overall_pass,
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    for k in K_VALUES:
        r = results[f'k{k}']
        print(f"=== k={k} ===")
        print(f"  obs mean seam J = {r['observed_mean_seam_jaccard']:.6f}")
        print(f"  null mean       = {r['null_mean']:.6f}  null std = {r['null_std']:.6f}")
        print(f"  z               = {r['z_score']:.3f}")
        print(f"  p_perm (>=obs)  = {r['p_greater_perm']:.4f}  (count {r['n_perm_ge_obs']}/{N_PERM})  α_bonf={ALPHA_CORR}")
        print(f"  direction match = {r['direction_match']}")
        print(f"  verdict         = {r['verdict']}")
        ns = r['named_seam_Q8_Q9']
        print(f"  Q8->Q9 J = {ns['jaccard']:.4f}  rank {ns['rank_of_113']}/113  shared={ns['shared_roots']}")
        print(f"  top3 seams: " + ", ".join(
            f"{d['seam']}({d['jaccard']:.3f})" for d in r['top10_strongest_seams'][:3]))
        print()
    rr = replicate_k3
    print(f"=== replicate k=3 seed {SEED_REPLICATE} ===")
    print(f"  obs={rr['observed_mean_seam_jaccard']:.6f} null={rr['null_mean']:.6f} "
          f"z={rr['z_score']:.3f} p={rr['p_greater_perm']:.4f} verdict={rr['verdict']}")


if __name__ == '__main__':
    main()
