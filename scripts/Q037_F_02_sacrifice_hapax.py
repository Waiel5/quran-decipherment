#!/usr/bin/env python3
"""Q037-F-02 — Sacrifice-of-Ishmael block hapax + lexical-isolation test.

Pre-reg: surahs/Q037-al-saffat/Q037-F-02-sacrifice-hapax-prereg.md
Pre-reg SHA256: 31df0ef290064534ff92bb7b135fef19147b56f2540cb89882ea869e87c9e381
Rules-tuple: (no-tashkeel, QAC-root-index + orthographic-token, IDF, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os, random, math
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q037-al-saffat/Q037-F-02-sacrifice-hapax-prereg.md'
EXPECTED_SHA = '31df0ef290064534ff92bb7b135fef19147b56f2540cb89882ea869e87c9e381'
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
    roots = json.load(open('/Users/grey/Downloads/quran/data/morphology/root-index.json'))

    # H1: hapax — roots whose all attestations lie in Q 37:99-113
    block_loc = lambda s,v: (s==37 and 99 <= v <= 113)
    hapax_in_block = []
    block_root_count = Counter()  # for diagnostics
    for root, atts in roots.items():
        all_in = True
        any_in = False
        for att in atts:
            if isinstance(att, list):
                s, v = att[0], att[1]
            else:
                parts = att.split(':') if isinstance(att, str) else None
                if not parts: continue
                s, v = int(parts[0]), int(parts[1])
            if block_loc(s,v):
                any_in = True
                block_root_count[root] += 1
            else:
                all_in = False
        if any_in and all_in:
            hapax_in_block.append((root, block_root_count[root]))

    n_hapax = len(hapax_in_block)
    h1_pass = n_hapax >= 3

    # Build per-verse token sets for Q 37 (no-tashkeel orthographic tokens)
    q37 = next(s for s in quran if s['id']==37)
    verses_by_id = {v['id']: v['text'].split() for v in q37['verses']}

    block_tokens = []
    for vid in range(99, 114):
        block_tokens.extend(verses_by_id[vid])
    rest_tokens = []
    for vid, toks in verses_by_id.items():
        if not (99 <= vid <= 113):
            rest_tokens.extend(toks)

    # IDF over Q 37 verses
    df = Counter()
    for vid, toks in verses_by_id.items():
        for t in set(toks):
            df[t] += 1
    N_doc = len(verses_by_id)
    def tfidf(tokens):
        tf = Counter(tokens)
        return {t: tf[t] * math.log((N_doc + 1) / (df[t] + 1)) for t in tf}

    block_vec = tfidf(block_tokens)
    rest_vec = tfidf(rest_tokens)
    D_obs = 1.0 - cosine(block_vec, rest_vec)

    # H2: permutation null — random 15-verse contiguous spans from comparable surahs
    pool_surahs = [7, 11, 19, 21, 26, 27, 28, 38]  # Q 37 excluded from pool
    null_distances = []
    for _ in range(N_PERM):
        sid = pool_surahs[rng.randint(0, len(pool_surahs)-1)]
        s = next(x for x in quran if x['id']==sid)
        verses = s['verses']
        if len(verses) < 15:
            continue
        start = rng.randint(0, len(verses)-15)
        span_tokens = []
        rest_tokens_s = []
        for i, v in enumerate(verses):
            t = v['text'].split()
            if start <= i < start+15:
                span_tokens.extend(t)
            else:
                rest_tokens_s.extend(t)
        # Build IDF for that surah
        df_s = Counter()
        for v in verses:
            for tok in set(v['text'].split()):
                df_s[tok] += 1
        N_s = len(verses)
        def tfidf_s(tokens):
            tf = Counter(tokens)
            return {t: tf[t] * math.log((N_s + 1) / (df_s[t] + 1)) for t in tf}
        v1 = tfidf_s(span_tokens)
        v2 = tfidf_s(rest_tokens_s)
        d = 1.0 - cosine(v1, v2)
        null_distances.append(d)

    p_iso = sum(1 for d in null_distances if d >= D_obs) / len(null_distances)
    h2_pass = p_iso <= 0.01667

    # H3: comparison anchors
    def block_isolation(sid, vrange):
        s = next(x for x in quran if x['id']==sid)
        verses_b = {v['id']: v['text'].split() for v in s['verses']}
        block_t = []
        rest_t = []
        for vid, toks in verses_b.items():
            if vid in vrange:
                block_t.extend(toks)
            else:
                rest_t.extend(toks)
        df_b = Counter()
        for vid, toks in verses_b.items():
            for t in set(toks):
                df_b[t] += 1
        N_b = len(verses_b)
        def ti(tokens):
            tf = Counter(tokens)
            return {t: tf[t] * math.log((N_b + 1) / (df_b[t] + 1)) for t in tf}
        return 1.0 - cosine(ti(block_t), ti(rest_t))

    D_q21 = block_isolation(21, set(range(69, 72)))
    D_q11 = block_isolation(11, set(range(69, 84)))

    h3_pass = (D_obs > D_q21) and (D_obs > D_q11)

    # Verdict
    if h1_pass and h2_pass and h3_pass:
        verdict = 'CONFIRMED'
    elif sum([h1_pass, h2_pass, h3_pass]) == 2:
        verdict = 'DIRECTIONAL'
    elif n_hapax == 0:
        verdict = 'PRE-COMMIT-VIOLATION'
    elif sum([h1_pass, h2_pass, h3_pass]) == 1:
        verdict = 'DIRECTIONAL-WEAK'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q037-F-02',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC-root-index + orthographic-token, IDF, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'block': 'Q 37:99-113 (Abraham + son sacrifice narrative, 15 verses)',
        'h1_hapax_count': n_hapax,
        'h1_hapax_roots': hapax_in_block,
        'h1_threshold': 3,
        'h1_pass': h1_pass,
        'h2_block_isolation_obs': D_obs,
        'h2_perm_null_mean': sum(null_distances)/len(null_distances),
        'h2_perm_null_max': max(null_distances),
        'h2_perm_null_p_one_tailed': p_iso,
        'h2_alpha_bon': 0.01667,
        'h2_pass': h2_pass,
        'h3_comparisons': {
            'Q21:69-71_isolation': D_q21,
            'Q11:69-83_isolation': D_q11,
        },
        'h3_pass': h3_pass,
        'verdict': verdict,
        'honest_limits': 'TF-IDF on a 15-verse block has high variance; QAC-hapax depends on root-index v0.4 segmentation; comparison anchors differ in length (Q21:69-71 = 3 verses).',
    }

    print('=== Q037-F-02 SACRIFICE-BLOCK HAPAX + ISOLATION ===')
    print(f'H1 hapax in Q 37:99-113: {n_hapax}')
    for r, c in hapax_in_block:
        print(f'  root={r}, in_block_count={c}')
    print(f'  H1 pass (≥3): {h1_pass}')
    print(f'\nH2 block isolation (1 - cosine to surah-rest): {D_obs:.4f}')
    print(f'  perm null: mean={sum(null_distances)/len(null_distances):.4f}, max={max(null_distances):.4f}')
    print(f'  perm-p (one-tailed): {p_iso:.4f}; α_bon=0.01667; pass: {h2_pass}')
    print(f'\nH3 comparisons:')
    print(f'  Q 37:99-113: {D_obs:.4f}')
    print(f'  Q 21:69-71  (Abraham fire): {D_q21:.4f}')
    print(f'  Q 11:69-83  (angel-visit) : {D_q11:.4f}')
    print(f'  H3 pass (Q 37 > both): {h3_pass}')
    print(f'\nVerdict: {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv/Q037-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
