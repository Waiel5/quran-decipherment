#!/usr/bin/env python3
"""H-NEW-2510 — Divine-self-reference density corpus map + tawḥīd-declaration class.

Generalizes Q020-F-05 (MASTER-FINDINGS-LEDGER §10.120: Q20:14 is the rank-1
divine-self-reference verse within Ṭā-Hā) to all 6236 verses, re-grounded in the
QAC v0.4 morphology (person/number features) instead of a noisy regex proxy.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2510-divine-self-reference.md
Pre-reg SHA256 embedded below; verified at runtime (fail-fast on mismatch).

Rules-tuple: (no-tashkeel, QAC-morphology-segment, words-as-denominator,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed 20260509, 10000 permutations, per-verse word-shuffle null.
"""
import re
import json
import math
import random
import hashlib
import sys
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'findings/phase-b-hypotheses/prereg-h-new-2510-divine-self-reference.md'
EXPECTED_SHA = '68845be397a198ed5b95abe701c6b126159715ed07aa28c82b09ad16bfbdb53a'
QAC = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-2510.json'

SEED = 20260509
NPERM = 10000

# Pre-named tawḥīd-declaration anchor set (locked in pre-reg §3 H2)
ANCHORS = [(20, 14), (27, 9), (28, 30), (2, 255), (112, 1), (112, 2)]


def verify_sha():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f'FAIL: pre-reg SHA mismatch\n expected {EXPECTED_SHA}\n actual   {actual}',
              file=sys.stderr)
        sys.exit(1)


def load_qac():
    """Return verse_segs[(s,v)] = list of (word_idx, feats); word_count[(s,v)] = int."""
    verse_segs = defaultdict(list)
    words = defaultdict(set)
    loc_re = re.compile(r'\((\d+):(\d+):(\d+):(\d+)\)')
    with open(QAC, encoding='utf-8') as f:
        for line in f:
            if not line.startswith('('):
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) != 4:
                continue
            loc, form, tag, feats = parts
            m = loc_re.match(loc)
            if not m:
                continue
            s, v, w, _seg = map(int, m.groups())
            verse_segs[(s, v)].append((w, feats))
            words[(s, v)].add(w)
    word_count = {k: len(ws) for k, ws in words.items()}
    return verse_segs, word_count


# ---- token classifiers (QAC feature column) ----
def is_allah(ft):           # divine name proper noun  (token 1)
    return 'POS:PN' in ft and 'LEM:{ll~ah' in ft

def is_ilah(ft):            # noun ilah (tawhid-noun)  (token 2)
    return 'LEM:<ila`h' in ft

def is_pron_1s(ft):         # standalone ana  (token 3a)
    return 'POS:PRON' in ft and re.search(r'\|1S\b', ft)

def is_pron_1p(ft):         # standalone nahnu  (token 3b)
    return 'POS:PRON' in ft and re.search(r'\|1P\b', ft)

def is_clitic_1(ft):        # suffix -ni/-i/-na  (token 4)
    return 'PRON:1S' in ft or 'PRON:1P' in ft

def is_illa(ft):            # restrictive illa  (token 5, gated by adjacency to ilah)
    return 'LEM:<il~aA' in ft


def verse_counts(segs):
    """Return (numA, numB, gated_bool, breakdown) for one verse's segment list.

    Metric-A (primary, lexical/speaker-agnostic): tokens 1-5 (illa only when it
        immediately follows an ilah segment = the tawhid formula).
    Metric-B (robustness, divine-gated): bare 1S/1P (tokens 3,4) count only if the
        verse passes the divine-speech gate (has Allah-name OR tawhid-formula);
        unambiguous tokens 1,2,5 always count.
    """
    feats = [ft for _w, ft in segs]
    n_allah = sum(1 for ft in feats if is_allah(ft))
    n_ilah = sum(1 for ft in feats if is_ilah(ft))
    # tawhid-illa: an illa segment whose immediately-preceding segment is ilah
    n_tawhid_illa = 0
    for i in range(1, len(feats)):
        if is_illa(feats[i]) and is_ilah(feats[i - 1]):
            n_tawhid_illa += 1
    has_tawhid = n_tawhid_illa > 0
    n_pron1 = sum(1 for ft in feats if is_pron_1s(ft) or is_pron_1p(ft))
    n_clitic = sum(1 for ft in feats if is_clitic_1(ft))

    unambiguous = n_allah + n_ilah + n_tawhid_illa          # tokens 1,2,5
    ambiguous_1st = n_pron1 + n_clitic                       # tokens 3,4
    numA = unambiguous + ambiguous_1st
    gate = (n_allah > 0) or has_tawhid
    numB = unambiguous + (ambiguous_1st if gate else 0)
    breakdown = {'allah': n_allah, 'ilah': n_ilah, 'tawhid_illa': n_tawhid_illa,
                 'pron_1st': n_pron1, 'clitic_1st': n_clitic, 'gated': gate}
    return numA, numB, breakdown


def main():
    verify_sha()
    verse_segs, word_count = load_qac()
    verse_keys = sorted(verse_segs.keys())
    assert len(verse_keys) == 6236, f'expected 6236 verses, got {len(verse_keys)}'

    # ---- observed densities ----
    rows = []
    for k in verse_keys:
        s, v = k
        wc = word_count[k]
        numA, numB, bd = verse_counts(verse_segs[k])
        rows.append({'surah': s, 'verse': v, 'wc': wc,
                     'numA': numA, 'densityA': numA / wc,
                     'numB': numB, 'densityB': numB / wc,
                     'bd': bd})

    densA = [r['densityA'] for r in rows]
    densB = [r['densityB'] for r in rows]
    obs_max = max(densA)
    rankA = sorted(range(len(rows)), key=lambda i: -densA[i])
    top20_idx = rankA[:20]
    obs_top20_mean = statistics.mean(densA[i] for i in top20_idx)

    def rank_of(s, v, dens):
        order = sorted(range(len(rows)), key=lambda i: -dens[i])
        for r, i in enumerate(order, 1):
            if rows[i]['surah'] == s and rows[i]['verse'] == v:
                return r
        return None

    q2014_rank = rank_of(20, 14, densA)
    q2014_density = next(r['densityA'] for r in rows if (r['surah'], r['verse']) == (20, 14))

    # ---- permutation null (per-verse word-shuffle) ----
    # We shuffle the *segment-bearing words*: pool all words (each word = its list of
    # segments), shuffle, re-assign preserving each verse's word-count, recount.
    word_blocks = []  # each = list of feats for one orthographic word
    counts = []
    for k in verse_keys:
        # group this verse's segments by word index
        byw = defaultdict(list)
        for w, ft in verse_segs[k]:
            byw[w].append(ft)
        ws = [byw[w] for w in sorted(byw)]
        word_blocks.extend(ws)
        counts.append(len(ws))

    def counts_from_words(word_list):
        feats = [ft for blk in word_list for ft in blk]
        segs = [(0, ft) for ft in feats]  # word idx irrelevant for A; adjacency preserved within block order
        # rebuild adjacency for tawhid-illa: flatten in word order
        return verse_counts(segs)

    rng = random.Random(SEED)
    null_max = []
    null_top20 = []
    for _ in range(NPERM):
        sh = word_blocks[:]
        rng.shuffle(sh)
        idx = 0
        nd = []
        for c, k in zip(counts, verse_keys):
            wl = sh[idx:idx + c]
            idx += c
            numA, _numB, _bd = counts_from_words(wl)
            nd.append(numA / word_count[k])
        null_max.append(max(nd))
        nd_sorted = sorted(nd, reverse=True)
        null_top20.append(statistics.mean(nd_sorted[:20]))

    p_max = (sum(1 for x in null_max if x >= obs_max) + 1) / (NPERM + 1)
    p_top20 = (sum(1 for x in null_top20 if x >= obs_top20_mean) + 1) / (NPERM + 1)

    # ---- H2: anchor enrichment ----
    anchor_ranks = {f'{s}:{v}': rank_of(s, v, densA) for s, v in ANCHORS}
    anchors_in_top20 = sum(1 for r in anchor_ranks.values() if r is not None and r <= 20)
    anchor_mean_rank = statistics.mean([r for r in anchor_ranks.values() if r is not None])

    # ---- verdicts ----
    h1_pass = (p_max <= 0.05) and (p_top20 <= 0.05)
    h2_pass = (anchors_in_top20 >= 3) or (anchor_mean_rank <= 624)
    if h1_pass and h2_pass:
        verdict = 'CONFIRMED'
    elif h1_pass or h2_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # ---- top-20 tables ----
    def fmt_top(idx_list, dens, num_key):
        out = []
        for rk, i in enumerate(idx_list, 1):
            r = rows[i]
            out.append({'rank': rk, 'surah': r['surah'], 'verse': r['verse'],
                        'density': round(dens[i], 4), 'num': r[num_key], 'wc': r['wc'],
                        'breakdown': r['bd']})
        return out

    top20_A = fmt_top(top20_idx, densA, 'numA')
    rankB = sorted(range(len(rows)), key=lambda i: -densB[i])
    top20_B = fmt_top(rankB[:20], densB, 'numB')

    # Spearman A vs B (rank correlation, ties broken by index — adequate for robustness)
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        rk = [0] * len(vals)
        for r, i in enumerate(order):
            rk[i] = r
        return rk
    ra, rb = ranks(densA), ranks(densB)
    n = len(densA)
    mean_r = (n - 1) / 2
    cov = sum((ra[i] - mean_r) * (rb[i] - mean_r) for i in range(n))
    va = sum((ra[i] - mean_r) ** 2 for i in range(n))
    vb = sum((rb[i] - mean_r) ** 2 for i in range(n))
    spearman = cov / math.sqrt(va * vb) if va and vb else float('nan')

    # how concentrated: share of self-ref mass in top decile
    total_num = sum(r['numA'] for r in rows)
    top_decile_n = int(round(0.10 * n))
    top_decile_mass = sum(rows[i]['numA'] for i in rankA[:top_decile_n])

    out = {
        'finding_id': 'H-NEW-2510',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED, 'n_perm': NPERM,
        'rules_tuple': '(no-tashkeel, QAC-morphology-segment, words-as-denominator, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'n_verses': n,
        'metricA_definition': 'Allah-name + ilah + tawhid-illa + bare-1S/1P + clitic-1S/1P, / QAC-word-count (PRIMARY, speaker-agnostic)',
        'metricB_definition': 'as A but bare/clitic 1st-person gated to divine-speech verses (has Allah-name OR tawhid-formula) (ROBUSTNESS)',
        'observed': {
            'max_densityA': round(obs_max, 4),
            'top20_mean_densityA': round(obs_top20_mean, 4),
            'corpus_mean_densityA': round(statistics.mean(densA), 5),
            'corpus_mean_densityB': round(statistics.mean(densB), 5),
            'top_decile_self_ref_mass_share': round(top_decile_mass / total_num, 4),
        },
        'null': {
            'method': 'per-verse word-shuffle preserving each verse word-count; recount under identical token rules',
            'p_max': round(p_max, 5),
            'null_max_mean': round(statistics.mean(null_max), 4),
            'p_top20_mean': round(p_top20, 5),
            'null_top20_mean': round(statistics.mean(null_top20), 4),
        },
        'H1_concentration_pass': h1_pass,
        'H2_anchor_enrichment_pass': h2_pass,
        'anchor_ranks': anchor_ranks,
        'anchors_in_top20': anchors_in_top20,
        'anchor_mean_rank': round(anchor_mean_rank, 1),
        'Q20_14_corpus_rank': q2014_rank,
        'Q20_14_density': round(q2014_density, 4),
        'spearman_A_B': round(spearman, 4),
        'top20_metricA': top20_A,
        'top20_metricB': top20_B,
        'verdict': verdict,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f'verses scored: {n}')
    print(f'max densityA={obs_max:.4f}  p_max={p_max:.5f}')
    print(f'top20-mean densityA={obs_top20_mean:.4f}  p_top20={p_top20:.5f}')
    print(f'Q20:14 corpus rank: {q2014_rank}/{n}  (density {q2014_density:.4f})')
    print(f'anchors in top-20: {anchors_in_top20}/6 ; anchor mean rank {anchor_mean_rank:.1f}')
    print(f'Spearman A vs B: {spearman:.4f}')
    print(f'H1={h1_pass} H2={h2_pass} -> VERDICT {verdict}')
    print('--- top-10 Metric-A ---')
    for t in top20_A[:10]:
        print(f"  #{t['rank']:2d} Q{t['surah']}:{t['verse']:<3d} d={t['density']:.4f} "
              f"num={t['num']} wc={t['wc']} {t['breakdown']}")


if __name__ == '__main__':
    main()
