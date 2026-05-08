#!/usr/bin/env python3
"""Q016-F-02 — Q 16:68-69 bee-passage corpus-hapax lemma count.

Pre-reg: surahs/Q016-al-nahl/Q016-F-02-bee-verse-hapax-prereg.md
SHA256: 31d55e2dc1bb77fde5fb27f96247b55e58663555ec4e41fa51386db8b9967b14
Rules-tuple: (no-tashkeel, QAC-lemma, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, hashlib, sys, os, random, re
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q016-al-nahl/Q016-F-02-bee-verse-hapax-prereg.md'
EXPECTED_SHA = '31d55e2dc1bb77fde5fb27f96247b55e58663555ec4e41fa51386db8b9967b14'
SEED = 20260507
N_PERM = 10000

QAC_PATH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'

CONTENT_POS = {'N', 'V', 'ADJ', 'PCPL'}


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def parse_qac():
    """Returns:
       - by_verse: dict (s,v) -> list of {lemma, pos, root, ...}
       - lemma_to_verses: dict lemma -> set of (s,v) where lemma is content-attested
       - content_token_count: dict (s,v) -> int (# content tokens in that verse)"""
    by_verse = defaultdict(list)
    lemma_to_verses = defaultdict(set)
    pat = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)\t(\S+)\t(\S+)\t(.+)$')
    with open(QAC_PATH) as f:
        for line in f:
            line = line.rstrip('\n')
            m = pat.match(line)
            if not m: continue
            s, v, w, p, form, postag, feats = m.groups()
            s, v = int(s), int(v)
            lem_m = re.search(r'LEM:([^\|]+)', feats)
            pos_m = re.search(r'POS:([^\|]+)', feats)
            root_m = re.search(r'ROOT:([^\|]+)', feats)
            if not (lem_m and pos_m): continue
            lemma = lem_m.group(1)
            pos = pos_m.group(1)
            root = root_m.group(1) if root_m else None
            entry = {'lemma': lemma, 'pos': pos, 'root': root}
            by_verse[(s, v)].append(entry)
            if pos in CONTENT_POS:
                lemma_to_verses[lemma].add((s, v))
    content_token_count = {sv: sum(1 for e in es if e['pos'] in CONTENT_POS) for sv, es in by_verse.items()}
    return by_verse, lemma_to_verses, content_token_count


def content_lemmas_in_window(by_verse, window):
    s_lemmas = set()
    for sv in window:
        for e in by_verse.get(sv, []):
            if e['pos'] in CONTENT_POS:
                s_lemmas.add(e['lemma'])
    return s_lemmas


def hapax_count_fast(window, by_verse, lemma_to_verses):
    """A lemma in `window` is hapax iff its attested verse-set is a subset of `window`."""
    win_set = set(window)
    lemmas = content_lemmas_in_window(by_verse, window)
    hapaxes = []
    for L in lemmas:
        attest = lemma_to_verses.get(L, set())
        if attest.issubset(win_set):
            hapaxes.append(L)
    return hapaxes


def main():
    verify_sha()
    by_verse, lemma_to_verses, content_count = parse_qac()
    print(f'Parsed QAC: {len(by_verse)} verses, {len(lemma_to_verses)} content-lemmas')

    # Bee passage
    bee_window = [(16, 68), (16, 69)]
    bee_lemmas = content_lemmas_in_window(by_verse, bee_window)
    bee_hapaxes = hapax_count_fast(bee_window, by_verse, lemma_to_verses)
    bee_n_content = sum(content_count.get(sv, 0) for sv in bee_window)
    print(f"Bee passage Q 16:68-69: {len(bee_lemmas)} content-lemmas, {len(bee_hapaxes)} hapaxes, {bee_n_content} content-tokens")
    print(f"  hapax lemmas: {sorted(bee_hapaxes)}")

    # Length-controlled null
    all_verses = sorted(by_verse.keys())
    candidates = []
    for sv in all_verses:
        s, v = sv
        if (s, v+1) in by_verse:
            candidates.append([(s, v), (s, v+1)])
    lo, hi = bee_n_content * 0.7, bee_n_content * 1.3
    matched = [w for w in candidates if lo <= sum(content_count.get(sv,0) for sv in w) <= hi and w != bee_window]
    print(f"  candidate length-matched 2-verse windows: {len(matched)}")

    random.seed(SEED)
    null_counts = []
    for _ in range(N_PERM):
        w = random.choice(matched)
        h = hapax_count_fast(w, by_verse, lemma_to_verses)
        null_counts.append(len(h))
    n_ge = sum(1 for c in null_counts if c >= len(bee_hapaxes))
    p_perm = (n_ge + 1) / (N_PERM + 1)
    null_mean = sum(null_counts) / len(null_counts)
    null_max = max(null_counts)

    # MW-5: Q 12:4-5
    pc_window = [(12, 4), (12, 5)]
    pc_hapax = hapax_count_fast(pc_window, by_verse, lemma_to_verses)
    print(f"  MW-5 control Q 12:4-5: {len(pc_hapax)} hapaxes (expected ≥ 1)")

    verdict = 'PASS' if (len(bee_hapaxes) >= 4 and p_perm <= 0.05) else (
              'DIRECTIONAL' if (len(bee_hapaxes) in (2,3) and p_perm <= 0.10) else
              'PRE_COMMIT_VIOLATION' if len(bee_hapaxes) == 0 else 'NULL')

    out = {
        'finding_id': 'Q016-F-02',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC-lemma, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'bee_window': bee_window,
        'bee_n_content_lemmas': len(bee_lemmas),
        'bee_hapax_count': len(bee_hapaxes),
        'bee_hapax_lemmas': sorted(bee_hapaxes),
        'bee_all_lemmas': sorted(bee_lemmas),
        'bee_n_content_tokens': bee_n_content,
        'null_window_pool_size': len(matched),
        'null_mean_hapax': null_mean,
        'null_max_hapax': null_max,
        'p_perm': p_perm,
        'mw5_q12_4_5_hapax_count': len(pc_hapax),
        'mw5_q12_4_5_hapaxes': sorted(pc_hapax),
        'mw5_pass': len(pc_hapax) >= 1,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv/Q016-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"  null mean hapax = {null_mean:.3f}, max = {null_max}, p_perm = {p_perm:.4f}")
    print(f"  VERDICT: {verdict}")


if __name__ == '__main__':
    main()
