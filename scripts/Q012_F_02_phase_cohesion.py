#!/usr/bin/env python3
"""Q012-F-02 — per-narrative-phase internal cohesion of Q 12.

Pre-reg: surahs/Q012-yusuf/Q012-F-02-phase-cohesion-prereg.md
Pre-reg SHA256: 1e9a06cd2676df1e36c0f3319aabd360a4369d32bf2f1e78147b6b55868d5038
"""
import json, re, hashlib, math, random, sys, os
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q012-yusuf/Q012-F-02-phase-cohesion-prereg.md'
EXPECTED_SHA = '1e9a06cd2676df1e36c0f3319aabd360a4369d32bf2f1e78147b6b55868d5038'
SEED = 20260428


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def tokenize(t):
    t = re.sub(r'[ۚۖۗۛۙۘ۠٠-٩]', ' ', t)
    return [w for w in t.split() if w]


def main():
    verify_sha()
    d = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    q12 = d[11]
    texts = [v['text'] for v in q12['verses']]
    docs = [tokenize(t) for t in texts]
    N = len(docs)
    df = Counter()
    for doc in docs:
        df.update(set(doc))

    def tfidf(doc):
        tf = Counter(doc)
        vec = {w: c * math.log(N / df[w]) for w, c in tf.items() if df[w]}
        nrm = math.sqrt(sum(v * v for v in vec.values()))
        return {k: v / nrm for k, v in vec.items()} if nrm > 0 else {}

    vecs = [tfidf(doc) for doc in docs]

    def cosine(a, b):
        keys = set(a) & set(b)
        return sum(a[k] * b[k] for k in keys)

    phases = [
        ('Opening', 1, 3), ('Dream', 4, 6), ('Well/Brothers', 7, 18),
        ('Caravan/Egypt sale', 19, 22), ('Aziz wife/seduction/prison', 23, 34),
        ('Prison-dreams + Pharaoh', 35, 49), ('Elevation', 50, 57),
        ("Brothers' visits", 58, 82), ('Reunion', 83, 101),
        ('Epilogue', 102, 111),
    ]

    per_phase = []
    for label, lo, hi in phases:
        idxs = list(range(lo - 1, hi))
        sims = [cosine(vecs[idxs[i]], vecs[idxs[j]])
                for i in range(len(idxs)) for j in range(i + 1, len(idxs))]
        mean = sum(sims) / len(sims) if sims else 0.0
        per_phase.append({'phase': label, 'lo': lo, 'hi': hi, 'n_verses': hi - lo + 1,
                          'mean_pairwise_cosine_sim': mean})

    all_sims = [cosine(vecs[i], vecs[j]) for i in range(N) for j in range(i + 1, N)]
    whole = sum(all_sims) / len(all_sims)

    rng = random.Random(SEED)
    n_perm = 1000
    null = []
    for r in per_phase:
        actual = r['mean_pairwise_cosine_sim']
        n_v = r['n_verses']
        means = []
        for _ in range(n_perm):
            perm = rng.sample(range(N), n_v)
            sims = [cosine(vecs[perm[i]], vecs[perm[j]])
                    for i in range(n_v) for j in range(i + 1, n_v)]
            means.append(sum(sims) / len(sims) if sims else 0)
        p_g = sum(1 for x in means if x >= actual) / n_perm
        null.append({'phase': r['phase'], 'actual': actual,
                     'null_mean': sum(means) / n_perm, 'p_greater': p_g})

    out = {
        'finding_id': 'Q012-F-02',
        'prereg_sha': EXPECTED_SHA, 'seed': SEED, 'n_perm': n_perm,
        'rules_tuple': '(no-tashkeel, whitespace-token, TF-IDF-internal, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'TF-IDF on Q12 verses; per-phase mean pairwise cosine similarity; null = random size-matched samples from Q12',
        'phase_split': phases, 'whole_surah_mean': whole,
        'per_phase': per_phase, 'permutation_null': null,
        'bonferroni_k': 10, 'alpha_corrected': 0.005,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv/Q012-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    n_pass = sum(1 for n in null if n['p_greater'] < 0.005)
    print(f"Q012-F-02: {n_pass}/10 phases pass Bonferroni α=0.005")


if __name__ == '__main__':
    main()
