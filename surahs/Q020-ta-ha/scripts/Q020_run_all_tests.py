#!/usr/bin/env python3
"""
Q020 Ṭā Hā — unified test-runner for Q020-F-01..F-05.
Pre-reg SHAs locked at top; verified at runtime.
Seed: 20260507. n_perm: 10000. Bonferroni declared per-test.
"""

import json, hashlib, random, re, math, sys, os, statistics
from pathlib import Path

PROJECT = Path('/Users/grey/Downloads/quran')
PREREG_DIR = PROJECT / 'surahs/Q020-ta-ha/preregs'
OUT_DIR = PROJECT / 'surahs/Q020-ta-ha/csv'
OUT_DIR.mkdir(exist_ok=True, parents=True)

EXPECTED_SHAS = {
    'Q020-F-01-moses-cycle-purity': 'c6429a88447b9bdb3773f2002c1d027b6e8e52406b5bb2413bdef3af197f1e05',
    'Q020-F-02-vocative-test': 'f24a83321ac6f44880b1c48eb00f90d2c3947b01d61040850c1e0ca7c37111c0',
    'Q020-F-03-2letter-muqattaat-cluster': 'b8564a47ca3741d1d04d80861462ed92775d4af7ff530456dbb6a20fa80f9b8b',
    'Q020-F-04-samiri-block-isolation': 'afd0ec991949c0f53afb47b695605d3efa87837b46aee414a5d7bce5baa54394',
    'Q020-F-05-umar-conversion-Q20-14': '4f67f4597a5dddbf19590829dedb57f3ff5e2a77947faebf3810bede0a7d806f',
}

def verify_shas():
    for stem, sha in EXPECTED_SHAS.items():
        p = PREREG_DIR / f'{stem}-prereg.md'
        actual = hashlib.sha256(p.read_bytes()).hexdigest()
        if actual != sha:
            sys.exit(f'PRE-REG SHA MISMATCH on {stem}: expected {sha}, got {actual}')
    print('[SHA OK] all 5 pre-regs verified.')

SEED = 20260507
NPERM = 10000

QURAN = json.load(open(PROJECT / 'quran-text/quran-no-tashkeel.json'))
H750 = json.load(open(PROJECT / 'findings/phase-b-hypotheses/csv/h-new-750.json'))
H111 = json.load(open(PROJECT / 'findings/phase-b-hypotheses/csv/h-new-111.json'))
H720 = json.load(open(PROJECT / 'findings/phase-b-hypotheses/csv/h-new-720.json'))

PER750 = {s['surah']: s for s in H750['per_surah']}

# Build FR distance matrix from triples
FR = {}
for a, b, v in H111['D_matrix_upper_triangular']:
    FR[(a, b)] = v
    FR[(b, a)] = v

def D(i, j):
    return 0.0 if i == j else FR[(i, j)]

# Tokenizer (no-tashkeel orthographic)
def tokens_of_verse(text):
    # Strip Quran end-of-verse punct and pause marks (pipe, colon, parens, etc.)
    cleaned = re.sub(r'[ۣۚۖۗۘۙۛۜ۠ۡۢۤۧۦۨ۩۪ۭ۫]', ' ', text)
    cleaned = re.sub(r'[،؛؟٫٬۔۝·]', ' ', cleaned)
    return [w for w in cleaned.split() if w]

def all_verses(surah_idx):
    """1-indexed surah_idx -> list of (verse_id, word_tokens)."""
    s = QURAN[surah_idx - 1]
    out = []
    for v in s['verses']:
        toks = tokens_of_verse(v['text'])
        # Strip basmala from non-Q1 first verses if it appears (basmala count rules-tuple)
        out.append((v['id'], toks))
    return out

# ===== Q020-F-01 — Moses-cycle purity =====
MOSES_PATTERNS = [
    re.compile(r'\bموسى\b'),
    re.compile(r'\bفرعون\b'),
    re.compile(r'\bهارون\b'),
    re.compile(r'\bبني\b.{0,3}\bاسرايل\b'),  # banī isrāʾīl variants
    re.compile(r'\bإسراءيل\b'), re.compile(r'\bاسرايل\b'), re.compile(r'\bإسرائيل\b'),
    re.compile(r'\bالسامري\b'),
    re.compile(r'\bعصاك\b'), re.compile(r'\bعصاه\b'), re.compile(r'\bعصاي\b'),
    re.compile(r'\bالعصا\b'),
    re.compile(r'\bالبيضاء\b'),
]
def verse_is_moses(toks):
    text = ' '.join(toks)
    return any(p.search(text) for p in MOSES_PATTERNS)

def moses_purity(surah_idx):
    verses = all_verses(surah_idx)
    n = len(verses)
    m = sum(1 for _, toks in verses if verse_is_moses(toks))
    return m / n if n else 0.0, m, n

def run_F01():
    print('\n=== Q020-F-01 — Moses-cycle purity ===')
    purities = []
    for s in range(1, 115):
        f, m, n = moses_purity(s)
        purities.append((s, f, m, n))
    purities_sorted = sorted(purities, key=lambda x: -x[1])
    Q20_rank = next(i for i, (s, f, m, n) in enumerate(purities_sorted, 1) if s == 20)
    Q20_frac = next(f for s, f, m, n in purities if s == 20)
    top10 = [{'surah': s, 'frac': round(f, 4), 'count': m, 'n_verses': n} for s, f, m, n in purities_sorted[:15]]

    # Permutation null: rotate Q20's 135-verse window across the corpus
    rng = random.Random(SEED)
    flat_verses = []  # (toks)
    for sidx in range(1, 115):
        for _, toks in all_verses(sidx):
            flat_verses.append(toks)
    Ntot = len(flat_verses)
    n_q20 = 135
    null_fracs = []
    for _ in range(NPERM):
        start = rng.randrange(0, Ntot)
        win = [flat_verses[(start + k) % Ntot] for k in range(n_q20)]
        m = sum(1 for toks in win if verse_is_moses(toks))
        null_fracs.append(m / n_q20)
    p_perm = sum(1 for x in null_fracs if x >= Q20_frac) / NPERM

    # Verdict
    verdict = 'NULL'
    if Q20_rank == 1 and Q20_frac >= 0.55:
        verdict = 'CONFIRMED'
    elif Q20_rank <= 3 and Q20_frac >= 0.55:
        verdict = 'DIRECTIONAL'
    elif Q20_rank == 1:
        verdict = 'DIRECTIONAL'
    elif Q20_rank > 3 and any(s in (7, 26, 28) for s, *_ in purities_sorted[:1]):
        verdict = 'PRE-COMMIT-VIOLATION'

    out = {
        'finding_id': 'Q020-F-01',
        'pre_reg_sha256': EXPECTED_SHAS['Q020-F-01-moses-cycle-purity'],
        'seed': SEED, 'n_perm': NPERM,
        'Q20_frac': round(Q20_frac, 4),
        'Q20_rank': Q20_rank,
        'Q20_count_verses_with_marker': next(m for s, f, m, n in purities if s == 20),
        'Q20_n_verses': 135,
        'top15': top10,
        'comparators': {f'Q{q}': {
            'frac': round(next(f for s, f, m, n in purities if s == q), 4),
            'rank': next(i for i, (s, f, m, n) in enumerate(purities_sorted, 1) if s == q),
            'count': next(m for s, f, m, n in purities if s == q),
            'n_verses': next(n for s, f, m, n in purities if s == q),
        } for q in [7, 26, 28, 19]},
        'permutation_null': {
            'method': 'rotational shift of corpus, 135-verse window',
            'p_perm': p_perm,
            'null_mean': statistics.mean(null_fracs),
            'null_max': max(null_fracs),
        },
        'verdict': verdict,
    }
    json.dump(out, open(OUT_DIR / 'Q020-F-01.json', 'w'), indent=2, ensure_ascii=False)
    print(f'  Q20 frac={Q20_frac:.4f} rank={Q20_rank}/114 p_perm={p_perm:.4f} verdict={verdict}')
    print(f'  Top-5: {[(s, round(f,3)) for s, f, _, _ in purities_sorted[:5]]}')
    print(f'  Comparators Q7={out["comparators"]["Q7"]} Q26={out["comparators"]["Q26"]} Q28={out["comparators"]["Q28"]}')
    return out

# ===== Q020-F-02 — vocative / 2sg-density =====
def kaaf_suffix_count(toks):
    """Count tokens ending in a single 'ك' (length>=4, ك as suffix proxy for 2sg-obj/poss)."""
    n = 0
    for t in toks:
        if len(t) >= 4 and t.endswith('ك') and not t.endswith('كم') and not t.endswith('كن'):
            n += 1
    return n

ANTA_PATTERNS = [re.compile(r'\bأنت\b'), re.compile(r'\bانت\b'),
                 re.compile(r'\bإياك\b'), re.compile(r'\bاياك\b')]

def two_sg_count(toks):
    text = ' '.join(toks)
    n = sum(len(p.findall(text)) for p in ANTA_PATTERNS)
    n += kaaf_suffix_count(toks)
    return n

def surah_2sg_density(surah_idx):
    verses = all_verses(surah_idx)
    total_words = sum(len(toks) for _, toks in verses)
    total_2sg = sum(two_sg_count(toks) for _, toks in verses)
    return total_2sg / total_words if total_words else 0.0, total_2sg, total_words

def run_F02():
    print('\n=== Q020-F-02 — vocative 2sg-density ===')
    densities = []
    for s in range(1, 115):
        d, n2, nw = surah_2sg_density(s)
        densities.append((s, d, n2, nw))
    Q20_density = next(d for s, d, n2, nw in densities if s == 20)
    all_densities = [d for _, d, _, _ in densities]
    mu = statistics.mean(all_densities)
    sd = statistics.stdev(all_densities)
    z = (Q20_density - mu) / sd if sd else 0.0
    rank_high = sum(1 for x in all_densities if x > Q20_density) + 1

    # Permutation null: shuffle ALL word-tokens of corpus, redistribute into surah-sized bags, recompute Q20 density.
    rng = random.Random(SEED)
    all_tokens = []
    surah_word_counts = []
    for s in range(1, 115):
        verses = all_verses(s)
        toks = [t for _, vt in verses for t in vt]
        surah_word_counts.append(len(toks))
        all_tokens.extend(toks)
    null_dens_q20 = []
    q20_n = surah_word_counts[19]
    Ntot = len(all_tokens)
    for _ in range(NPERM):
        # Sample a random contiguous slice of size q20_n (rotational)
        start = rng.randrange(0, Ntot)
        slice_toks = [all_tokens[(start + k) % Ntot] for k in range(q20_n)]
        # 2sg density on slice — verse boundaries lost, but kaaf-suffix is per-token; ANTA whole-word still works.
        text = ' '.join(slice_toks)
        n2 = sum(len(p.findall(text)) for p in ANTA_PATTERNS) + kaaf_suffix_count(slice_toks)
        null_dens_q20.append(n2 / q20_n)
    p_perm = sum(1 for x in null_dens_q20 if x >= Q20_density) / NPERM

    verdict = 'NULL'
    if z >= 1.5 and p_perm <= 0.025:
        verdict = 'CONFIRMED'
    elif z >= 1.0:
        verdict = 'DIRECTIONAL'

    out = {
        'finding_id': 'Q020-F-02',
        'pre_reg_sha256': EXPECTED_SHAS['Q020-F-02-vocative-test'],
        'seed': SEED, 'n_perm': NPERM,
        'Q20_2sg_density': round(Q20_density, 5),
        'Q20_2sg_count': next(n2 for s, d, n2, nw in densities if s == 20),
        'Q20_word_count': q20_n,
        'corpus_mean_density': round(mu, 5),
        'corpus_stdev_density': round(sd, 5),
        'Q20_z_score': round(z, 3),
        'Q20_rank_high': rank_high,
        'top10_by_density': [{'surah': s, 'density': round(d, 5)} for s, d, _, _ in sorted(densities, key=lambda x: -x[1])[:10]],
        'permutation_null': {
            'method': 'random contiguous corpus-token slice of size N(Q20)',
            'p_perm': p_perm,
            'null_mean': statistics.mean(null_dens_q20),
        },
        'verdict': verdict,
    }
    json.dump(out, open(OUT_DIR / 'Q020-F-02.json', 'w'), indent=2, ensure_ascii=False)
    print(f'  Q20 density={Q20_density:.5f} z={z:.2f} rank={rank_high}/114 p_perm={p_perm:.4f} verdict={verdict}')
    return out

# ===== Q020-F-03 — 2-letter trio cluster =====
def run_F03():
    print('\n=== Q020-F-03 — 2-letter muqaṭṭaʿ trio cluster ===')
    trio = [20, 27, 36]
    rng = random.Random(SEED)
    # Axis 1: FR-distance trio mean intra
    intra_pairs = [(20, 27), (20, 36), (27, 36)]
    trio_fr_mean = statistics.mean(D(a, b) for a, b in intra_pairs)
    null_fr = []
    for _ in range(NPERM):
        s3 = rng.sample(range(1, 115), 3)
        null_fr.append(statistics.mean([D(s3[0], s3[1]), D(s3[0], s3[2]), D(s3[1], s3[2])]))
    p_fr = sum(1 for x in null_fr if x <= trio_fr_mean) / NPERM
    fr_p5 = sorted(null_fr)[int(0.05 * NPERM)]
    axis_fr_pass = trio_fr_mean <= fr_p5

    # Axis 2: sig_A spread (range)
    sigAs = [PER750[s]['sig_A'] for s in trio]
    trio_spread = max(sigAs) - min(sigAs)
    null_spread = []
    for _ in range(NPERM):
        s3 = rng.sample(range(1, 115), 3)
        sa = [PER750[s]['sig_A'] for s in s3]
        null_spread.append(max(sa) - min(sa))
    spread_p5 = sorted(null_spread)[int(0.05 * NPERM)]
    p_spread = sum(1 for x in null_spread if x <= trio_spread) / NPERM
    axis_spread_pass = trio_spread <= spread_p5

    # Axis 3: top-rhyme-letter consensus (≥2 of 3)
    top_letters = [PER750[s]['top_final_letter'] for s in trio]
    consensus = max(top_letters.count(l) for l in set(top_letters))
    null_consensus = []
    for _ in range(NPERM):
        s3 = rng.sample(range(1, 115), 3)
        ls = [PER750[s]['top_final_letter'] for s in s3]
        null_consensus.append(max(ls.count(l) for l in set(ls)))
    p_consensus = sum(1 for x in null_consensus if x >= consensus) / NPERM
    axis_consensus_pass = consensus >= 2 and p_consensus <= 0.05

    # Axis 4: mean_d corpus-rank consensus
    rks = sorted([(s, PER750[s]['mean_content_distance']) for s in range(1, 115)], key=lambda x: x[1])
    rank_of = {s: i + 1 for i, (s, _) in enumerate(rks)}
    trio_ranks = [rank_of[s] for s in trio]
    trio_rank_spread = max(trio_ranks) - min(trio_ranks)
    null_rank_spread = []
    for _ in range(NPERM):
        s3 = rng.sample(range(1, 115), 3)
        r3 = [rank_of[s] for s in s3]
        null_rank_spread.append(max(r3) - min(r3))
    rank_p5 = sorted(null_rank_spread)[int(0.05 * NPERM)]
    p_rank = sum(1 for x in null_rank_spread if x <= trio_rank_spread) / NPERM
    axis_rank_pass = trio_rank_spread <= rank_p5

    n_pass = sum([axis_fr_pass, axis_spread_pass, axis_consensus_pass, axis_rank_pass])
    if n_pass >= 2:
        verdict = 'CONFIRMED'
    elif n_pass == 1:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q020-F-03',
        'pre_reg_sha256': EXPECTED_SHAS['Q020-F-03-2letter-muqattaat-cluster'],
        'seed': SEED, 'n_perm': NPERM,
        'trio': trio,
        'axis_1_FR': {'trio_mean_intra': round(trio_fr_mean, 4), 'null_p5': round(fr_p5, 4),
                      'p_perm': p_fr, 'pass': axis_fr_pass,
                      'pair_distances': {f'{a}-{b}': round(D(a, b), 4) for a, b in intra_pairs}},
        'axis_2_sigA_spread': {'trio_spread': round(trio_spread, 3), 'null_p5': round(spread_p5, 3),
                                'p_perm': p_spread, 'pass': axis_spread_pass,
                                'sig_As': {s: round(PER750[s]['sig_A'], 3) for s in trio}},
        'axis_3_rhyme_top_letter_consensus': {'top_letters': {s: PER750[s]['top_final_letter'] for s in trio},
                                              'consensus': consensus,
                                              'p_perm': p_consensus, 'pass': axis_consensus_pass},
        'axis_4_mean_d_rank_spread': {'trio_ranks': {s: rank_of[s] for s in trio},
                                      'rank_spread': trio_rank_spread, 'null_p5': rank_p5,
                                      'p_perm': p_rank, 'pass': axis_rank_pass},
        'n_axes_pass': n_pass, 'verdict': verdict,
    }
    json.dump(out, open(OUT_DIR / 'Q020-F-03.json', 'w'), indent=2, ensure_ascii=False)
    print(f'  Trio FR={trio_fr_mean:.4f} (p5={fr_p5:.4f}) pass={axis_fr_pass}')
    print(f'  Trio sig_A spread={trio_spread:.3f} (p5={spread_p5:.3f}) pass={axis_spread_pass}')
    print(f'  Top letters={top_letters} consensus={consensus} p={p_consensus:.4f} pass={axis_consensus_pass}')
    print(f'  Trio mean_d rank-spread={trio_rank_spread} (p5={rank_p5}) pass={axis_rank_pass}')
    print(f'  n_axes_pass={n_pass}/4 verdict={verdict}')
    return out

# ===== Q020-F-04 — Sāmirī block =====
def run_F04():
    print('\n=== Q020-F-04 — Sāmirī block lexical isolation ===')
    verses = all_verses(20)  # 1..135
    n = len(verses)
    K = 14
    # Build vocab union of Q20 tokens
    vocab = sorted(set(t for _, toks in verses for t in toks))
    vidx = {t: i for i, t in enumerate(vocab)}
    V = len(vocab)

    def window_tf(start_idx0):  # 0-indexed start
        tf = [0.0] * V
        for k in range(K):
            for t in verses[start_idx0 + k][1]:
                tf[vidx[t]] += 1.0
        s = sum(tf)
        if s > 0:
            tf = [x / s for x in tf]
        return tf

    n_windows = n - K + 1
    windows = [window_tf(i) for i in range(n_windows)]
    surah_mean = [0.0] * V
    for w in windows:
        for i, x in enumerate(w):
            surah_mean[i] += x
    sm_norm = sum(surah_mean)
    if sm_norm > 0:
        surah_mean = [x / sm_norm for x in surah_mean]

    def cosdist(a, b):
        dot = sum(x * y for x, y in zip(a, b))
        na = math.sqrt(sum(x * x for x in a))
        nb = math.sqrt(sum(x * x for x in b))
        if na == 0 or nb == 0: return 1.0
        return 1 - dot / (na * nb)

    cosdists = [cosdist(w, surah_mean) for w in windows]
    # Sāmirī start verse 85 (0-indexed = 84) → window v.85-98
    samiri_start_0 = 84
    samiri_dist = cosdists[samiri_start_0]
    sorted_idx = sorted(range(n_windows), key=lambda i: -cosdists[i])
    samiri_rank = sorted_idx.index(samiri_start_0) + 1

    # Permutation null: shuffle verse-token-lists 10000 times, recompute samiri-position cos dist rank
    rng = random.Random(SEED)
    null_ranks = []
    for _ in range(NPERM):
        order = list(range(n))
        rng.shuffle(order)
        sh_verses = [verses[i] for i in order]
        # rebuild windows using shuffled order
        sh_windows = []
        for s in range(n_windows):
            tf = [0.0] * V
            for k in range(K):
                for t in sh_verses[s + k][1]:
                    tf[vidx[t]] += 1.0
            sm2 = sum(tf)
            if sm2 > 0:
                tf = [x / sm2 for x in tf]
            sh_windows.append(tf)
        # surah-mean over shuffled windows
        sm = [0.0] * V
        for w in sh_windows:
            for i, x in enumerate(w):
                sm[i] += x
        smn = sum(sm)
        if smn > 0:
            sm = [x / smn for x in sm]
        sh_dists = [cosdist(w, sm) for w in sh_windows]
        sh_sorted = sorted(range(n_windows), key=lambda i: -sh_dists[i])
        # In null we look at rank-of-position-84 (positional null)
        null_ranks.append(sh_sorted.index(samiri_start_0) + 1)
    p_perm = sum(1 for r in null_ranks if r <= samiri_rank) / NPERM

    if samiri_rank <= 3 and p_perm <= 0.05:
        verdict = 'CONFIRMED'
    elif samiri_rank <= 12:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # Top-5 most distant 14-windows
    top5 = []
    for r, idx in enumerate(sorted_idx[:8], 1):
        start_v = idx + 1
        end_v = idx + K
        top5.append({'rank': r, 'start_verse': start_v, 'end_verse': end_v, 'cos_dist': round(cosdists[idx], 4)})

    out = {
        'finding_id': 'Q020-F-04',
        'pre_reg_sha256': EXPECTED_SHAS['Q020-F-04-samiri-block-isolation'],
        'seed': SEED, 'n_perm': NPERM,
        'samiri_window': {'start': 85, 'end': 98, 'cos_dist_to_surah_mean': round(samiri_dist, 4),
                          'rank': samiri_rank, 'n_windows': n_windows},
        'top_distant_windows': top5,
        'permutation_null': {
            'method': 'verse-shuffle, recompute window-rank at position 84-0idx (Sāmirī verse-position)',
            'p_perm': p_perm,
            'null_mean_rank': statistics.mean(null_ranks),
        },
        'verdict': verdict,
    }
    json.dump(out, open(OUT_DIR / 'Q020-F-04.json', 'w'), indent=2, ensure_ascii=False)
    print(f'  Sāmirī (v85-98) cos_dist={samiri_dist:.4f} rank={samiri_rank}/{n_windows} p_perm={p_perm:.4f} verdict={verdict}')
    print(f'  Top-3 distant windows: {top5[:3]}')
    return out

# ===== Q020-F-05 — Q20:14 divine-name density =====
def divine_density(toks):
    text = ' '.join(toks)
    n = 0
    n += len(re.findall(r'\bالله\b', text))
    n += len(re.findall(r'\bإله\b', text))
    n += len(re.findall(r'\bإلاه\b', text))
    n += len(re.findall(r'\bأنا\b', text))
    n += len(re.findall(r'\bهو\b', text))
    # ـني suffix proxy
    for t in toks:
        if len(t) >= 4 and t.endswith('ني'):
            n += 1
    nw = len(toks) if toks else 1
    return n / nw, n

def run_F05():
    print('\n=== Q020-F-05 — Q20:14 divine-name density ===')
    verses = all_verses(20)
    densities = [(vid, divine_density(toks)[0], divine_density(toks)[1], len(toks)) for vid, toks in verses]
    v14_density = next(d for vid, d, n, nw in densities if vid == 14)
    sorted_by_dens = sorted(densities, key=lambda x: -x[1])
    v14_rank = next(r for r, (vid, d, n, nw) in enumerate(sorted_by_dens, 1) if vid == 14)

    # Permutation null: shuffle word-tokens across Q20 verses (preserving per-verse word-counts)
    rng = random.Random(SEED)
    all_toks = [t for _, toks in verses for t in toks]
    counts = [len(toks) for _, toks in verses]
    n_v = len(verses)
    null_ranks = []
    null_v14_dens = []
    for _ in range(NPERM):
        sh = list(all_toks)
        rng.shuffle(sh)
        # Reconstruct verses with same word-counts
        new_verses = []
        idx = 0
        for c in counts:
            new_verses.append(sh[idx:idx + c]); idx += c
        # densities
        new_dens = [(i + 1, divine_density(new_verses[i])[0]) for i in range(n_v)]
        new_v14 = next(d for vid, d in new_dens if vid == 14)
        new_sorted = sorted(new_dens, key=lambda x: -x[1])
        new_rank = next(r for r, (vid, d) in enumerate(new_sorted, 1) if vid == 14)
        null_ranks.append(new_rank)
        null_v14_dens.append(new_v14)
    p_perm = sum(1 for r in null_ranks if r <= v14_rank) / NPERM

    if v14_rank <= 3 and p_perm <= 0.05:
        verdict = 'CONFIRMED'
    elif v14_rank <= 13:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    top5 = [{'verse': vid, 'density': round(d, 4), 'count': n, 'word_count': nw}
            for vid, d, n, nw in sorted_by_dens[:5]]

    out = {
        'finding_id': 'Q020-F-05',
        'pre_reg_sha256': EXPECTED_SHAS['Q020-F-05-umar-conversion-Q20-14'],
        'seed': SEED, 'n_perm': NPERM,
        'Q20_14_density': round(v14_density, 4),
        'Q20_14_count': next(n for vid, d, n, nw in densities if vid == 14),
        'Q20_14_word_count': next(nw for vid, d, n, nw in densities if vid == 14),
        'Q20_14_rank': v14_rank,
        'n_verses': n_v,
        'top5_dense_verses': top5,
        'surah_mean_density': round(statistics.mean(d for _, d, _, _ in densities), 4),
        'permutation_null': {
            'method': 'shuffle Q20 word-tokens preserving per-verse word-counts',
            'p_perm': p_perm,
            'null_mean_rank': statistics.mean(null_ranks),
        },
        'verdict': verdict,
    }
    json.dump(out, open(OUT_DIR / 'Q020-F-05.json', 'w'), indent=2, ensure_ascii=False)
    print(f'  Q20:14 density={v14_density:.4f} rank={v14_rank}/{n_v} p_perm={p_perm:.4f} verdict={verdict}')
    print(f'  Top-3: {top5[:3]}')
    return out

if __name__ == '__main__':
    verify_shas()
    f01 = run_F01()
    f02 = run_F02()
    f03 = run_F03()
    f04 = run_F04()
    f05 = run_F05()

    summary = {
        'Q020-F-01': f01['verdict'],
        'Q020-F-02': f02['verdict'],
        'Q020-F-03': f03['verdict'],
        'Q020-F-04': f04['verdict'],
        'Q020-F-05': f05['verdict'],
    }
    print('\n=== SUMMARY ===')
    for k, v in summary.items():
        print(f'  {k}: {v}')
    json.dump(summary, open(OUT_DIR / 'Q020-summary.json', 'w'), indent=2)
