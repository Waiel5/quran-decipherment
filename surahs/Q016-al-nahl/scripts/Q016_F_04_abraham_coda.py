#!/usr/bin/env python3
"""Q016-F-04 — Abraham coda Q 16:120-123 block-homogeneity test.

Pre-reg: surahs/Q016-al-nahl/Q016-F-04-abraham-coda-block-test-prereg.md
SHA256: b56cf82be99ad48c40d29ace39d8d84a4ecfe18bb93c7a97dd3c916602b4a3c9
Rules-tuple: (no-tashkeel, QAC-root-set or orthographic-token-set)
Seed: 20260507
"""
import json, hashlib, sys, os, random, re, math
from collections import defaultdict, Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q016-al-nahl/Q016-F-04-abraham-coda-block-test-prereg.md'
EXPECTED_SHA = 'b56cf82be99ad48c40d29ace39d8d84a4ecfe18bb93c7a97dd3c916602b4a3c9'
SEED = 20260507
N_PERM = 10000
ALPHA_BON = 0.025

QAC_PATH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_NO_TASHKEEL = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'

CODA = [120, 121, 122, 123]


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def parse_qac_q16_roots():
    """Returns dict verse_id -> set of QAC roots in that verse."""
    by_v = defaultdict(set)
    pat = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)\t(\S+)\t(\S+)\t(.+)$')
    with open(QAC_PATH) as f:
        for line in f:
            m = pat.match(line)
            if not m: continue
            s, v = int(m.group(1)), int(m.group(2))
            if s != 16: continue
            r = re.search(r'ROOT:([^\|]+)', m.group(7))
            if r:
                by_v[v].add(r.group(1))
    return by_v


def jaccard(a, b):
    return len(a & b) / max(1, len(a | b))


def cosine_tf(va, vb):
    keys = set(va) | set(vb)
    dot = sum(va.get(k, 0) * vb.get(k, 0) for k in keys)
    na = math.sqrt(sum(x*x for x in va.values()))
    nb = math.sqrt(sum(x*x for x in vb.values()))
    return dot / (na*nb) if na and nb else 0


def main():
    verify_sha()

    # Load text
    with open(QURAN_NO_TASHKEEL) as f:
        d = json.load(f)
    q16 = next(s for s in d if s['id']==16)
    verses = q16['verses']
    n_verses = len(verses)
    text_per_v = {v['id']: v['text'] for v in verses}

    # Parse roots per verse for Q16
    roots_per_v = parse_qac_q16_roots()

    # === Cell A: Roots-Jaccard ===
    coda_set_A = set()
    for v in CODA:
        coda_set_A |= roots_per_v.get(v, set())
    rest_set_A = set()
    for v in range(1, n_verses+1):
        if v not in CODA:
            rest_set_A |= roots_per_v.get(v, set())
    coda_jac = jaccard(coda_set_A, rest_set_A)

    # Null: random 4-verse contiguous windows in Q16, excluding coda
    rng = random.Random(SEED)
    null_jacs = []
    for _ in range(N_PERM):
        # Random start in [1, n-3] excluding overlap with CODA (must be 4 contiguous, fully outside CODA)
        max_start = n_verses - 3
        starts_ok = [s for s in range(1, max_start+1) if not any(c in CODA for c in [s, s+1, s+2, s+3])]
        start = rng.choice(starts_ok)
        win = [start + i for i in range(4)]
        win_set = set()
        for v in win:
            win_set |= roots_per_v.get(v, set())
        rest = set()
        for v in range(1, n_verses+1):
            if v not in win:
                rest |= roots_per_v.get(v, set())
        null_jacs.append(jaccard(win_set, rest))
    n_le_A = sum(1 for j in null_jacs if j <= coda_jac)
    p_A = (n_le_A + 1) / (N_PERM + 1)

    # === Cell B: Token TF cosine ===
    coda_tf = Counter()
    rest_tf = Counter()
    for v in verses:
        toks = v['text'].split()
        if v['id'] in CODA:
            coda_tf.update(toks)
        else:
            rest_tf.update(toks)
    coda_cos = cosine_tf(coda_tf, rest_tf)

    null_cos = []
    for _ in range(N_PERM):
        max_start = n_verses - 3
        starts_ok = [s for s in range(1, max_start+1) if not any(c in CODA for c in [s, s+1, s+2, s+3])]
        start = rng.choice(starts_ok)
        win = [start + i for i in range(4)]
        win_tf = Counter()
        rest_tf2 = Counter()
        for v in verses:
            toks = v['text'].split()
            if v['id'] in win:
                win_tf.update(toks)
            else:
                rest_tf2.update(toks)
        null_cos.append(cosine_tf(win_tf, rest_tf2))
    n_le_B = sum(1 for c in null_cos if c <= coda_cos)
    p_B = (n_le_B + 1) / (N_PERM + 1)

    # MW-5: Q 12:4 single-verse positive control on roots
    qac12 = defaultdict(set)
    pat = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)\t(\S+)\t(\S+)\t(.+)$')
    with open(QAC_PATH) as f:
        for line in f:
            m = pat.match(line)
            if not m: continue
            s, v = int(m.group(1)), int(m.group(2))
            if s != 12: continue
            r = re.search(r'ROOT:([^\|]+)', m.group(7))
            if r:
                qac12[v].add(r.group(1))
    pc_set = qac12.get(4, set())
    pc_rest = set()
    with open(QURAN_NO_TASHKEEL) as f:
        d12 = next(s for s in json.load(f) if s['id']==12)
    n12 = len(d12['verses'])
    for v in range(1, n12+1):
        if v != 4:
            pc_rest |= qac12.get(v, set())
    pc_jac = jaccard(pc_set, pc_rest)
    # Null: random single-verse in Q12
    pc_nulls = []
    rng2 = random.Random(SEED+1)
    for _ in range(2000):
        v = rng2.randint(1, n12)
        if v == 4: continue
        s_set = qac12.get(v, set())
        rest = set()
        for vv in range(1, n12+1):
            if vv != v:
                rest |= qac12.get(vv, set())
        pc_nulls.append(jaccard(s_set, rest))
    pc_p = sum(1 for j in pc_nulls if j <= pc_jac) / max(1, len(pc_nulls))
    mw5_pass = pc_p < 0.10

    # Verdict
    a_reject = p_A <= ALPHA_BON
    b_reject = p_B <= ALPHA_BON
    if a_reject and b_reject:
        verdict = 'CONFIRMED'
    elif a_reject or b_reject:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'
    # Pre-commit violation: coda is MORE typical than median of null
    if coda_jac > sum(null_jacs)/len(null_jacs) and coda_cos > sum(null_cos)/len(null_cos):
        # Check both well above median
        med_a = sorted(null_jacs)[len(null_jacs)//2]
        med_b = sorted(null_cos)[len(null_cos)//2]
        if coda_jac > med_a and coda_cos > med_b:
            verdict_note = 'coda is MORE-typical-than-median; H1 (heterogeneity) WRONG-DIRECTION'
        else:
            verdict_note = 'no pre-commit violation'
    else:
        verdict_note = 'no pre-commit violation'

    out = {
        'finding_id': 'Q016-F-04',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC-root-set or orthographic-token-set)',
        'coda_verses': CODA,
        'cell_A_roots_jaccard': {
            'coda_jaccard': coda_jac,
            'null_mean': sum(null_jacs)/len(null_jacs),
            'null_median': sorted(null_jacs)[len(null_jacs)//2],
            'p_perm': p_A,
            'reject_h0': a_reject,
        },
        'cell_B_token_cosine': {
            'coda_cosine': coda_cos,
            'null_mean': sum(null_cos)/len(null_cos),
            'null_median': sorted(null_cos)[len(null_cos)//2],
            'p_perm': p_B,
            'reject_h0': b_reject,
        },
        'mw5_q12v4_jaccard': pc_jac,
        'mw5_q12v4_p': pc_p,
        'mw5_pass': mw5_pass,
        'coda_unique_roots_count': len(coda_set_A),
        'rest_unique_roots_count': len(rest_set_A),
        'shared_roots_count': len(coda_set_A & rest_set_A),
        'verdict': verdict,
        'verdict_note': verdict_note,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv/Q016-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Cell A — Roots Jaccard: coda={coda_jac:.4f}, null_mean={sum(null_jacs)/len(null_jacs):.4f}, p={p_A:.4f}, reject={a_reject}")
    print(f"Cell B — Token cosine:  coda={coda_cos:.4f}, null_mean={sum(null_cos)/len(null_cos):.4f}, p={p_B:.4f}, reject={b_reject}")
    print(f"MW-5 Q12:4 jaccard={pc_jac:.4f}, p={pc_p:.4f}, pass={mw5_pass}")
    print(f"Coda has {len(coda_set_A)} unique roots; surah-rest has {len(rest_set_A)}; shared = {len(coda_set_A & rest_set_A)}")
    print(f"VERDICT: {verdict} ({verdict_note})")


if __name__ == '__main__':
    main()
