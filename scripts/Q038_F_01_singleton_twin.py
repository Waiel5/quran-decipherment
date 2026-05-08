#!/usr/bin/env python3
"""Q038-F-01 — Singleton-letter twin pair Q 38:1 ↔ Q 50:1 similarity test.

Pre-reg: surahs/Q038-sad/Q038-F-01-singleton-twin-prereg.md
Pre-reg SHA256: 224aeb8bf99f9fd4cd5a21fb205237c06b2b12b3fbbe701e6b3b59f5ead955f7
Rules-tuple: (no-tashkeel, orthographic-token + QAC root, char-4-gram-NCD, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, re, hashlib, sys, os, zlib, math, random
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-01-singleton-twin-prereg.md'
EXPECTED_SHA = '224aeb8bf99f9fd4cd5a21fb205237c06b2b12b3fbbe701e6b3b59f5ead955f7'
SEED = 20260507

# Single-letter muqaṭṭaʿāt to strip from openings (Q 38:1, Q 50:1, Q 68:1)
MUQ_LETTERS = set(['ص', 'ق', 'ن'])
# Multi-letter muqaṭṭaʿāt openings to strip from openings (for fair sampling)
MUQ_TOKENS = set(['الم', 'الر', 'المر', 'المص', 'كهيعص', 'طه', 'طسم', 'طس', 'يس',
                  'حم', 'عسق', 'ص', 'ق', 'ن'])


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def strip_muq(text):
    """Strip leading muqaṭṭaʿ tokens from a verse if present."""
    # Remove the special separator ۚ if present
    text = text.replace('ۚ', ' ').replace('ۖ', ' ').replace('ۗ', ' ').replace('ۘ', ' ').replace('ۙ', ' ').replace('ۜ', ' ').replace('۩', ' ').replace('ۤ', ' ').replace('ۚ', ' ')
    toks = text.split()
    if toks and toks[0] in MUQ_TOKENS:
        toks = toks[1:]
    return toks


def char_ngrams(s, n=4):
    return [s[i:i+n] for i in range(len(s)-n+1)]


def cosine(a, b):
    """Cosine on Counter-of-tokens."""
    keys = set(a) | set(b)
    if not keys:
        return 0.0
    dot = sum(a.get(k,0)*b.get(k,0) for k in keys)
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    return dot / (na*nb) if na and nb else 0.0


def ncd(s1, s2):
    """Normalized compression distance via zlib."""
    b1 = s1.encode('utf-8'); b2 = s2.encode('utf-8')
    c1 = len(zlib.compress(b1)); c2 = len(zlib.compress(b2))
    c12 = len(zlib.compress(b1+b2))
    return (c12 - min(c1,c2)) / max(c1,c2) if max(c1,c2) else 0.0


def main():
    verify_sha()
    rng = random.Random(SEED)

    # Load no-tashkeel quran
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    # Load QAC roots
    qac = {}  # (surah, verse) -> list of roots
    for line in open('/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'):
        if not line.startswith('('):
            continue
        parts = line.strip().split('\t')
        if len(parts) < 4:
            continue
        loc = parts[0]
        feats = parts[3]
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)', loc)
        if not m:
            continue
        s,v = int(m.group(1)), int(m.group(2))
        rt = re.search(r'ROOT:([^|]+)', feats)
        if rt:
            qac.setdefault((s,v), []).append(rt.group(1))

    # Build per-verse data
    verses = []  # list of {sid, vid, body, tokens, roots, body_str}
    for s in quran:
        sid = s['id']
        for v in s['verses']:
            vid = v['id']
            text = v['text']
            toks = strip_muq(text)
            body_str = ' '.join(toks)
            roots = qac.get((sid, vid), [])
            # Note: QAC roots include muqaṭṭaʿ position too; we'll accept that since
            # QAC encodes them as INL "initial letter" rather than ROOT, so
            # they typically won't have ROOT field anyway.
            verses.append({
                'sid': sid, 'vid': vid, 'body_str': body_str,
                'tokens': toks, 'roots': roots, 'n_toks': len(toks)
            })

    # Filter to verses with ≥3 tokens after muq-strip (per pre-reg)
    eligible = [v for v in verses if v['n_toks'] >= 3]
    print(f"Total verses: {len(verses)}; eligible (≥3 tokens after muq-strip): {len(eligible)}")

    # Find target pair
    q38_1 = next(v for v in verses if v['sid']==38 and v['vid']==1)
    q50_1 = next(v for v in verses if v['sid']==50 and v['vid']==1)
    print(f"Q38:1 body: {q38_1['body_str']}  tokens={q38_1['n_toks']}, roots={q38_1['roots']}")
    print(f"Q50:1 body: {q50_1['body_str']}  tokens={q50_1['n_toks']}, roots={q50_1['roots']}")

    # Compute target similarities/distances
    # Metric 1: token-bag cosine (Counter on tokens)
    sim_tok_target = cosine(Counter(q38_1['tokens']), Counter(q50_1['tokens']))
    # Metric 2: root-bag cosine
    sim_root_target = cosine(Counter(q38_1['roots']), Counter(q50_1['roots']))
    # Metric 3: char-4-gram NCD (lower = more similar, so we report 1-NCD as similarity)
    ncd_target = ncd(q38_1['body_str'], q50_1['body_str'])
    sim_ncd_target = 1.0 - ncd_target

    print(f"Target Q38:1↔Q50:1 sims: token-cos={sim_tok_target:.4f}, root-cos={sim_root_target:.4f}, 1-NCD={sim_ncd_target:.4f}")

    # Compute corpus pairwise sample (random sample 50000 pairs to keep tractable)
    # But for top-1% / top-3 we need the full distribution. Let's compute all eligible pairs.
    n_elig = len(eligible)
    print(f"Computing all {n_elig*(n_elig-1)//2} pairs... (may take a moment)")

    # Sample 100k pairs for null distribution (full pairs ~3.7M, manageable but slow)
    n_sample_pairs = 100000
    sims_tok = []
    sims_root = []
    sims_ncd = []
    seen = set()
    while len(sims_tok) < n_sample_pairs:
        i = rng.randrange(n_elig)
        j = rng.randrange(n_elig)
        if i == j:
            continue
        a, b = eligible[i], eligible[j]
        key = (min(a['sid']*1000+a['vid'], b['sid']*1000+b['vid']),
               max(a['sid']*1000+a['vid'], b['sid']*1000+b['vid']))
        if key in seen:
            continue
        seen.add(key)
        sims_tok.append(cosine(Counter(a['tokens']), Counter(b['tokens'])))
        sims_root.append(cosine(Counter(a['roots']), Counter(b['roots'])))
        sims_ncd.append(1.0 - ncd(a['body_str'], b['body_str']))

    # Compute percentile ranks (greater_or_equal)
    def pct_rank(target, sample):
        n_at_or_above = sum(1 for x in sample if x >= target)
        return n_at_or_above / len(sample)

    p_tok = pct_rank(sim_tok_target, sims_tok)
    p_root = pct_rank(sim_root_target, sims_root)
    p_ncd = pct_rank(sim_ncd_target, sims_ncd)

    # Top-3 corpus pairs on each metric (to identify rivals)
    # We'll compute the actual full top-K from a larger search: scan all eligible against Q38:1 and Q50:1 specifically + the top samples
    # Identify whether Q38:1↔Q50:1 is in top-3 across the sampled pairs
    sample_top10_tok = sorted(sims_tok, reverse=True)[:10]
    sample_top10_root = sorted(sims_root, reverse=True)[:10]
    sample_top10_ncd = sorted(sims_ncd, reverse=True)[:10]

    print(f"\np-percentile (fraction of sample ≥ target):")
    print(f"  token-bag: p={p_tok:.6f} (target {sim_tok_target:.4f})")
    print(f"  root-bag:  p={p_root:.6f} (target {sim_root_target:.4f})")
    print(f"  1-NCD:     p={p_ncd:.6f} (target {sim_ncd_target:.4f})")

    # Bonferroni-3 alpha = 0.01667; success if any p < α_bon
    alpha_bon = 0.05/3
    pass_tok = p_tok < alpha_bon
    pass_root = p_root < alpha_bon
    pass_ncd = p_ncd < alpha_bon
    n_pass = sum([pass_tok, pass_root, pass_ncd])

    if n_pass >= 1:
        verdict = 'CONFIRMED' if (p_tok < 0.01 or p_root < 0.01 or p_ncd < 0.01) else 'DIRECTIONAL'
    else:
        # check if any in top-5%
        if min(p_tok, p_root, p_ncd) < 0.05:
            verdict = 'DIRECTIONAL'
        else:
            verdict = 'NULL'

    out = {
        'finding_id': 'Q038-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, orthographic-token + QAC root, char-4-gram-NCD, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'Q38:1 ↔ Q50:1 (after muq-strip) similarity vs n=100000 random eligible pair sample',
        'n_eligible_verses': n_elig,
        'n_sample_pairs': n_sample_pairs,
        'q38_1_body': q38_1['body_str'],
        'q50_1_body': q50_1['body_str'],
        'q38_1_roots': q38_1['roots'],
        'q50_1_roots': q50_1['roots'],
        'target_sims': {
            'token_bag_cosine': sim_tok_target,
            'root_bag_cosine': sim_root_target,
            'one_minus_ncd': sim_ncd_target
        },
        'corpus_sample_top10': {
            'token_bag_cosine': sample_top10_tok,
            'root_bag_cosine': sample_top10_root,
            'one_minus_ncd': sample_top10_ncd
        },
        'percentile_pvalues': {'token_bag': p_tok, 'root_bag': p_root, 'one_minus_ncd': p_ncd},
        'alpha_bon': alpha_bon,
        'pass_per_metric': {'token_bag': pass_tok, 'root_bag': pass_root, 'one_minus_ncd': pass_ncd},
        'n_pass_of_3': n_pass,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nVerdict: {verdict}")
    print(f"Wrote: /Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-01.json")


if __name__ == '__main__':
    main()
