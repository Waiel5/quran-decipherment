#!/usr/bin/env python3
"""
Q032-F-01 — Sajda-verse cosmic-language clustering: Q 32:15 vs Q 13:15 + Q 16:49.
Replication of Q022-F-01 protocol.
Pre-reg SHA verified at runtime; fail-fast on mismatch.
Seed: 20260508. n_perm = 10000. Bonferroni-3.
"""
import json, re, math, random, hashlib, os, sys

EXPECTED_SHA = '93541c6eef6193f57ddfce776a465c5445ffb91a8637fd4a868ff4032d806e84'
PREREG_PATH = '/Users/grey/Downloads/quran/surahs/Q032-al-sajda/Q032-F-01-sajda-cosmic-twin-prereg.md'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q032-al-sajda/csv/Q032-F-01.json'

ANNO_PUNCT_RE = re.compile(r'[ۣۖۗۘۚۛۜ۠ۡۢۤۥۦۧۨ۩ۭ]')

def clean(s):
    return ANNO_PUNCT_RE.sub('', s).strip()

def verify_sha():
    with open(PREREG_PATH, 'rb') as f:
        got = hashlib.sha256(f.read()).hexdigest()
    if got != EXPECTED_SHA:
        print(f'SHA MISMATCH: expected {EXPECTED_SHA}, got {got}')
        sys.exit(1)
    print(f'Pre-reg SHA verified: {got}')

def main():
    verify_sha()
    q = json.load(open(QURAN_PATH))

    SAJDAS = [(7,206), (13,15), (16,49), (17,109), (19,58),
              (22,18), (22,77),
              (25,60), (27,25), (32,15), (38,24), (41,37), (53,62),
              (84,21), (96,19)]
    cosmic = [(13,15), (16,49)]
    target = (32,15)
    q22_18 = (22,18)

    # Tokenize each sajda verse
    tok = {}
    for s, v in SAJDAS:
        verse = next(vv['text'] for vv in q[s-1]['verses'] if vv['id'] == v)
        toks = clean(verse).split()
        tok[(s,v)] = toks

    # Build vocab
    vocab = sorted({w for toks in tok.values() for w in toks})
    vidx = {w:i for i,w in enumerate(vocab)}

    def vec(toks):
        v = [0.0]*len(vocab)
        for w in toks:
            v[vidx[w]] += 1
        n = math.sqrt(sum(x*x for x in v)) or 1.0
        return [x/n for x in v]

    def cos(a, b):
        return sum(x*y for x,y in zip(a,b))

    vecs = {k: vec(tok[k]) for k in tok}
    target_v = vecs[target]

    sim = {k: cos(target_v, vecs[k]) for k in vecs if k != target}
    sim_cosmic_mean = sum(sim[k] for k in cosmic) / len(cosmic)
    sim_q22_18 = sim[q22_18]
    others_11 = [k for k in sim if k not in cosmic and k != q22_18]
    sim_others_11_sorted = sorted([sim[k] for k in others_11])
    median_others = sim_others_11_sorted[len(sim_others_11_sorted)//2]
    mean_others = sum(sim_others_11_sorted) / len(sim_others_11_sorted)

    # T1: cosmic-pair > median-others
    t1 = sim_cosmic_mean > median_others
    # T2: cos(target, Q22:18) > median-others
    t2 = sim_q22_18 > median_others
    # T3: permutation null — random 2-set from non-target sajdas
    rng = random.Random(20260508)
    keys = list(sim.keys())
    n_perm = 10000
    obs = sim_cosmic_mean
    perm_count = 0
    for _ in range(n_perm):
        chosen = rng.sample(keys, 2)
        m = (sim[chosen[0]] + sim[chosen[1]]) / 2
        if m >= obs:
            perm_count += 1
    p_perm = (perm_count + 1) / (n_perm + 1)
    t3 = p_perm < 0.01667

    n_pass = sum([t1, t2, t3])
    verdict = ('VINDICATED' if n_pass == 3
               else 'DIRECTIONAL' if n_pass >= 1
               else 'NULL')

    out = {
        'test_id': 'Q032-F-01',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': 20260508,
        'n_perm': n_perm,
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'sim_target_to_cosmic_mean': sim_cosmic_mean,
        'sim_target_to_Q22_18': sim_q22_18,
        'sim_target_to_others_11_median': median_others,
        'sim_target_to_others_11_mean': mean_others,
        'sim_target_to_others_11_sorted': sim_others_11_sorted,
        'detail_pairwise': {f'Q{s}:{v}': round(sim[(s,v)],4) for (s,v) in sim},
        'T1_cosmic_gt_median_others': t1,
        'T2_q22_18_gt_median_others': t2,
        'T3_permutation_p_low': p_perm,
        'T3_pass_alpha_bon_0_01667': t3,
        'tests_passed': n_pass,
        'tests_total': 3,
        'bonferroni_k': 3,
        'alpha_bon': 0.01667,
        'verdict': verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'Q032-F-01 verdict: {verdict} ({n_pass}/3 tests passed)')
    print(f'  cos(Q32:15, cosmic-mean) = {sim_cosmic_mean:.4f}')
    print(f'  cos(Q32:15, Q22:18)      = {sim_q22_18:.4f}')
    print(f'  median(11 others)        = {median_others:.4f}')
    print(f'  T3 permutation p_low     = {p_perm:.4f}')

if __name__ == '__main__':
    main()
