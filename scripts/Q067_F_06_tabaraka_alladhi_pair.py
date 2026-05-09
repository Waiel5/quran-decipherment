#!/usr/bin/env python3
"""Q067-F-06 — tabāraka alladhī opener verse-pair tightness test.

Tests whether the 3 surah-opener verses {Q 25:1, Q 64:1, Q 67:1} that share
the tabāraka alladhī formula are tighter on verse-level Fisher-Rao than a
length-matched null draw from corpus verses.

Pre-reg: surahs/Q067-al-mulk/preregs/Q067-F-06-tabaraka-alladhi-pair-prereg.md
Pre-reg SHA256: d39272d336133ffa8bb30690859b5661fa264f31e5e0ac8f0eefe4084fd7e7aa
Seed: 20260509
"""
import json
import hashlib
import sys
import re
import math
import random
import statistics
from collections import Counter, defaultdict

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q067-al-mulk/preregs/Q067-F-06-tabaraka-alladhi-pair-prereg.md'
EXPECTED_SHA = 'd39272d336133ffa8bb30690859b5661fa264f31e5e0ac8f0eefe4084fd7e7aa'
SEED = 20260509
N_PERM = 10000
K_TOP = 500
DIRICHLET_ALPHA = 0.5
QAC_PATH = f'{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_JSON = f'{PROJECT}/quran-text/quran-no-tashkeel.json'
OUT_PATH = f'{PROJECT}/surahs/Q067-al-mulk/csv/Q067-F-06.json'

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f'PRE-REG SHA MISMATCH:\n  expected {EXPECTED_SHA}\n  actual   {actual}', file=sys.stderr)
        sys.exit(1)


def parse_qac():
    """Return: verse_roots[(s,v)] = list of stem-roots, global root counts."""
    verse_roots = defaultdict(list)
    global_root_counts = Counter()
    with open(QAC_PATH, encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            vid = int(m.group(2))
            feat = parts[3]
            if 'STEM' not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            root = rm.group(1)
            verse_roots[(sid, vid)].append(root)
            global_root_counts[root] += 1
    return verse_roots, global_root_counts


def load_verse_wordcounts():
    """Word-counts per verse from no-tashkeel json (strip basmala only at Q1)."""
    with open(QURAN_JSON, encoding='utf-8') as f:
        data = json.load(f)
    wc = {}
    # data structure: list of surahs each with 'verses' list having {id, text}
    if isinstance(data, list):
        for entry in data:
            sid = entry.get('id') or entry.get('chapter') or entry.get('num')
            verses = entry.get('verses') or entry.get('ayat') or []
            for v in verses:
                vid = v.get('id') or v.get('verse')
                txt = (v.get('text') or v.get('arabic') or '').strip()
                if sid is None or vid is None:
                    continue
                wc[(int(sid), int(vid))] = len(txt.split())
    elif isinstance(data, dict):
        # Try alternative shape
        for sid_str, surah_obj in data.items():
            try:
                sid = int(sid_str)
            except ValueError:
                continue
            verses = surah_obj.get('verses', surah_obj) if isinstance(surah_obj, dict) else surah_obj
            if isinstance(verses, list):
                for i, v in enumerate(verses, 1):
                    txt = v.get('text', '') if isinstance(v, dict) else v
                    if txt:
                        wc[(sid, i)] = len(str(txt).split())
            elif isinstance(verses, dict):
                for vid_str, txt in verses.items():
                    try:
                        vid = int(vid_str)
                    except ValueError:
                        continue
                    wc[(sid, vid)] = len(str(txt).split())
    return wc


def main():
    verify_sha()

    rng = random.Random(SEED)

    verse_roots, global_root_counts = parse_qac()
    word_counts = load_verse_wordcounts()

    # Locked top-K root index
    top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
    top_root_index = {r: i for i, r in enumerate(top_roots)}

    def verse_prob_vector(s, v):
        """Dirichlet-smoothed L1-normalized count vector over top-K roots."""
        vec = [0.0] * K_TOP
        for r in verse_roots.get((s, v), []):
            idx = top_root_index.get(r)
            if idx is not None:
                vec[idx] += 1.0
        smoothed = [c + DIRICHLET_ALPHA for c in vec]
        total = sum(smoothed)
        return [x / total for x in smoothed]

    def fr_distance(p, q):
        bc = 0.0
        for a, b in zip(p, q):
            bc += math.sqrt(a * b)
        bc = max(-1.0, min(1.0, bc))
        return 2.0 * math.acos(bc)

    # Target triplet
    target_verses = [(25, 1), (64, 1), (67, 1)]
    target_wc = [word_counts.get(v, 0) for v in target_verses]
    target_vecs = [verse_prob_vector(*v) for v in target_verses]

    # Pairwise FR distances among target triplet
    pairs = []
    for i in range(3):
        for j in range(i + 1, 3):
            d = fr_distance(target_vecs[i], target_vecs[j])
            pairs.append({
                'pair': [list(target_verses[i]), list(target_verses[j])],
                'fr_distance': d,
            })
    target_mean_fr = statistics.mean(p['fr_distance'] for p in pairs)

    # Length-matched verses: build pools per word-count target (±1 word)
    # Tolerance: target_wc[i] ± 1
    # Build verse-set indexed by word-count
    by_wc = defaultdict(list)
    for v, w in word_counts.items():
        by_wc[w].append(v)
    pools = []
    for w_target in target_wc:
        pool = []
        for w in range(max(1, w_target - 1), w_target + 2):
            pool.extend(by_wc.get(w, []))
        pools.append(pool)

    # Secondary descriptive: also include all 4 tabāraka alladhī occurrences (Q25:1, 25:10, 25:61, 67:1)
    # Note: Q 64:1 has tabāraka alladhī bi-yadihi al-mulk? No — Q 64:1 has yusabbiḥu li-llāhi mā…
    # Per pre-reg, the comparison set is {Q25:1, Q64:1, Q67:1}; we lock to that for the primary test.
    # Secondary check: re-test with 4 of the 5 tabāraka alladhī verses (Q25:1, 25:10, 25:61, 43:85, 67:1)
    secondary_verses = [(25, 1), (25, 10), (25, 61), (43, 85), (67, 1)]
    sec_vecs = [verse_prob_vector(*v) for v in secondary_verses]
    sec_pairs = []
    for i in range(len(secondary_verses)):
        for j in range(i + 1, len(secondary_verses)):
            d = fr_distance(sec_vecs[i], sec_vecs[j])
            sec_pairs.append({
                'pair': [list(secondary_verses[i]), list(secondary_verses[j])],
                'fr_distance': d,
            })
    secondary_mean_fr = statistics.mean(p['fr_distance'] for p in sec_pairs)
    secondary_wc = [word_counts.get(v, 0) for v in secondary_verses]

    # Permutation null: draw 3 verses with length matched to target_wc (±1)
    null_means = []
    n_eligible = [len(p) for p in pools]
    # If any pool is empty, fail-fast
    for i, p in enumerate(pools):
        if not p:
            print(f'PRE-REG VIOLATION: empty pool for target wc={target_wc[i]}', file=sys.stderr)
            sys.exit(1)

    for _ in range(N_PERM):
        triplet = [rng.choice(pools[0]), rng.choice(pools[1]), rng.choice(pools[2])]
        # Compute mean pairwise FR
        vecs = [verse_prob_vector(*v) for v in triplet]
        ds = []
        for i in range(3):
            for j in range(i + 1, 3):
                ds.append(fr_distance(vecs[i], vecs[j]))
        null_means.append(statistics.mean(ds))

    null_sorted = sorted(null_means)
    n_le = sum(1 for x in null_means if x <= target_mean_fr)
    p_perm = (n_le + 1) / (N_PERM + 1)

    def q(arr, frac):
        idx = max(0, min(len(arr) - 1, int(frac * len(arr))))
        return arr[idx]

    null_quants = {
        'min': null_sorted[0],
        'q01': q(null_sorted, 0.01),
        'q05': q(null_sorted, 0.05),
        'q10': q(null_sorted, 0.10),
        'q25': q(null_sorted, 0.25),
        'q50': q(null_sorted, 0.50),
        'q75': q(null_sorted, 0.75),
        'q95': q(null_sorted, 0.95),
        'max': null_sorted[-1],
        'mean': statistics.mean(null_means),
        'stdev': statistics.stdev(null_means),
    }

    passes_tighter = target_mean_fr < null_quants['q05']
    pre_commit_violation = target_mean_fr > null_quants['q50']  # reversed direction

    if passes_tighter:
        verdict = 'TIGHTER'
        interpretation = (
            f'tabāraka alladhī opener triplet {{Q25:1, Q64:1, Q67:1}} mean FR={target_mean_fr:.4f} '
            f'< null q05={null_quants["q05"]:.4f}, p_perm={p_perm:.4f}. '
            f'The shared opener formula generates verse-level lexical cohesion beyond length-matched chance.'
        )
    elif pre_commit_violation:
        verdict = 'NULL_PRECOMMIT_VIOLATION'
        interpretation = (
            f'tabāraka alladhī opener triplet mean FR={target_mean_fr:.4f} '
            f'> null median={null_quants["q50"]:.4f} (reversed direction). '
            f'p_perm={p_perm:.4f}. Pre-registered TIGHTER direction violated. The verses are NOT closer than chance; '
            f'the shared opener formula does NOT predict root-distribution similarity.'
        )
    else:
        verdict = 'NULL'
        interpretation = (
            f'tabāraka alladhī opener triplet mean FR={target_mean_fr:.4f}, '
            f'null q05={null_quants["q05"]:.4f}, p_perm={p_perm:.4f}. '
            f'Tightness pre-registration NOT met at p<0.05. The shared opener formula does NOT generate '
            f'verse-level FR cohesion at this rules-tuple beyond what length alone explains.'
        )

    out = {
        'finding_id': 'Q067-F-06',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC-stem-roots, K=500, Dirichlet α=0.5, FR-distance verse-level, Hafs-Kufan)',
        'target_verses': target_verses,
        'target_word_counts': target_wc,
        'target_pairwise_fr': pairs,
        'target_mean_fr': target_mean_fr,
        'null_distribution': null_quants,
        'p_perm_target_le_null': p_perm,
        'pool_sizes_per_target_wc': n_eligible,
        'passes_tighter_q05': passes_tighter,
        'pre_commit_violation': pre_commit_violation,
        'verdict': verdict,
        'interpretation': interpretation,
        'secondary': {
            'verses': secondary_verses,
            'word_counts': secondary_wc,
            'pairwise_fr': sec_pairs,
            'mean_fr': secondary_mean_fr,
            'note': 'Descriptive: includes all 5 of corpus verse-level *tabāraka alladhī* occurrences (Q25:1, Q25:10, Q25:61, Q43:85, Q67:1). Q 64:1 starts *yusabbiḥu* not *tabāraka*, but is included in the primary 3-verse comparison set because the brief locked it; the secondary recomputes over the actual *tabāraka alladhī* occurrences.',
        },
    }

    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Q067-F-06: VERDICT={verdict}')
    print(f'  Target word counts: {target_wc}')
    print(f'  Target mean FR: {target_mean_fr:.4f}')
    print(f'  Null q05: {null_quants["q05"]:.4f}, median: {null_quants["q50"]:.4f}')
    print(f'  p_perm: {p_perm:.4f}')
    print(f'  Secondary (5 actual tabāraka alladhī verses) mean FR: {secondary_mean_fr:.4f}')
    print(f'  Output: {OUT_PATH}')


if __name__ == '__main__':
    main()
