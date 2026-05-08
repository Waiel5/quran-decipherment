#!/usr/bin/env python3
"""Q037-F-03 — Ranked-Ones oath-trio Q 37:1-3 lexical-cohesion vs Q 37 baseline.

Pre-reg: surahs/Q037-al-saffat/Q037-F-03-ranked-ones-trio-prereg.md
Pre-reg SHA256: 0f39d6771b0f8262613d899bc023e17dbd3a34456f0a83b67775c70d7c763719
Rules-tuple: (no-tashkeel, orthographic-token + QAC-root, cosine, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os, random, math
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q037-al-saffat/Q037-F-03-ranked-ones-trio-prereg.md'
EXPECTED_SHA = '0f39d6771b0f8262613d899bc023e17dbd3a34456f0a83b67775c70d7c763719'
SEED = 20260508
N_PERM = 10000


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def cosine(c1, c2):
    keys = set(c1) | set(c2)
    dot = sum(c1.get(k,0) * c2.get(k,0) for k in keys)
    n1 = math.sqrt(sum(v*v for v in c1.values()))
    n2 = math.sqrt(sum(v*v for v in c2.values()))
    if n1==0 or n2==0: return 0.0
    return dot / (n1*n2)


def main():
    verify_sha()
    rng = random.Random(SEED)

    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    q37 = next(s for s in quran if s['id']==37)
    verses_tokens = {v['id']: Counter(v['text'].split()) for v in q37['verses']}
    n_v = len(q37['verses'])

    # Load QAC root-index → roots per (37, vid)
    roots_idx = json.load(open('/Users/grey/Downloads/quran/data/morphology/root-index.json'))
    verse_roots = {v['id']: Counter() for v in q37['verses']}
    for root, atts in roots_idx.items():
        for att in atts:
            if isinstance(att, list):
                s, v = att[0], att[1]
            else:
                continue
            if s == 37 and v in verse_roots:
                verse_roots[v][root] += 1

    def trio_cohesion(vids, mode='token'):
        if mode == 'token':
            cs = [verses_tokens[vid] for vid in vids]
        else:
            cs = [verse_roots[vid] for vid in vids]
        sims = []
        for i in range(len(cs)):
            for j in range(i+1, len(cs)):
                sims.append(cosine(cs[i], cs[j]))
        return sum(sims)/len(sims) if sims else 0.0

    C_trio_token = trio_cohesion([1,2,3], 'token')
    C_trio_root = trio_cohesion([1,2,3], 'root')

    # Permutation null: random ordered 3-spans of Q 37 verses
    null_token = []
    null_root = []
    all_vids = sorted(verses_tokens.keys())
    for _ in range(N_PERM):
        sample = sorted(rng.sample(all_vids, 3))
        null_token.append(trio_cohesion(sample, 'token'))
        null_root.append(trio_cohesion(sample, 'root'))

    p_token = sum(1 for x in null_token if x >= C_trio_token) / N_PERM
    p_root = sum(1 for x in null_root if x >= C_trio_root) / N_PERM

    # Direct comparisons
    C_456_token = trio_cohesion([4,5,6], 'token')
    C_456_root = trio_cohesion([4,5,6], 'root')
    C_180_182_token = trio_cohesion([180,181,182], 'token')
    C_180_182_root = trio_cohesion([180,181,182], 'root')

    h1_token = p_token <= 0.025
    h1_root = p_root <= 0.025
    h1_pass = h1_token or h1_root
    h2_pass = (C_trio_token > C_456_token) and (C_trio_token > C_180_182_token)

    if h1_pass and h2_pass:
        verdict = 'CONFIRMED'
    elif h1_pass or h2_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'
    if (C_trio_token < sum(null_token)/len(null_token)) and (C_trio_root < sum(null_root)/len(null_root)):
        if not (h1_pass or h2_pass):
            verdict = 'PRE-COMMIT-VIOLATION'

    out = {
        'finding_id': 'Q037-F-03',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token + QAC-root, cosine, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'C_trio_Q37_1_3_token_cosine': C_trio_token,
        'C_trio_Q37_1_3_root_cosine': C_trio_root,
        'null_token_mean': sum(null_token)/len(null_token),
        'null_token_p': p_token,
        'null_root_mean': sum(null_root)/len(null_root),
        'null_root_p': p_root,
        'alpha_bon': 0.025,
        'h1_token_pass': h1_token,
        'h1_root_pass': h1_root,
        'h1_pass': h1_pass,
        'C_Q37_4_6_token_cosine': C_456_token,
        'C_Q37_4_6_root_cosine': C_456_root,
        'C_Q37_180_182_token_cosine': C_180_182_token,
        'C_Q37_180_182_root_cosine': C_180_182_root,
        'h2_pass': h2_pass,
        'verdict': verdict,
        'honest_limits': 'Token-cosine inflated by و/ف+ال template prefix; root-cosine across {ṣ-f-f, z-j-r, t-l-w, dh-k-r} pairwise = 0 expected.',
    }

    print('=== Q037-F-03 RANKED-ONES OATH-TRIO ===')
    print(f'C(Q37:1-3) token-cosine: {C_trio_token:.4f}')
    print(f'C(Q37:1-3) root-cosine:  {C_trio_root:.4f}')
    print(f'null-token mean: {sum(null_token)/len(null_token):.4f}, p={p_token:.4f}')
    print(f'null-root mean:  {sum(null_root)/len(null_root):.4f}, p={p_root:.4f}')
    print(f'C(Q37:4-6) token: {C_456_token:.4f}')
    print(f'C(Q37:180-182) token: {C_180_182_token:.4f}')
    print(f'H1 (any metric perm-p ≤ 0.025): {h1_pass}')
    print(f'H2 (trio > both 4-6 and 180-182 token-cosine): {h2_pass}')
    print(f'Verdict: {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv/Q037-F-03.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
