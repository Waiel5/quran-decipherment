#!/usr/bin/env python3
"""
Phase C — Prophet micro-ring scanner.

Applies the chiastic-audit ring score (pair-Jaccard of triliteral root sets)
to a curated list of prophet pericopes (Noah, Moses, Abraham, Joseph,
David/Solomon, Jonah, Jesus, Adam), with two complementary null models:

  (A) Intra-pericope null: shuffle the verse order *within* the pericope
      only (N! / 2 possible orderings). 2000 trials per pericope, seed =
      (surah * 100000) + start. This is the conservative null — it tells
      you whether the *order* of verses inside the pericope is ringed,
      controlling for the pericope's own bag of verses.

  (B) Surah-wide null: shuffle the verse order of the *entire surah* and
      resample a window of the same width at the same offset. 2000 trials.
      This asks whether the *combination* of these verses + their order
      produces a ring-score beyond what a random N-verse window of the
      same surah would.

Reports: observed ring-score, mean/std of each null, z-A, z-B, empirical
p. Bonferroni across the 41 pericopes tested here => z > ~3.5 for alpha=0.05.

Outputs: analysis/notebooks/prophet_rings_results.json
"""
from __future__ import annotations
import json, re, random, statistics, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/grey/Downloads/quran')
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
MORPH = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
SAHIH = ROOT / 'data/translations/en.sahih.txt'
OUT_JSON = ROOT / 'analysis/notebooks/prophet_rings_results.json'

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

def load_roots_per_verse():
    rv = defaultdict(set)
    with open(MORPH, encoding='utf-8') as f:
        header_seen = False
        for line in f:
            line = line.rstrip('\n')
            if not line or line.startswith('#'):
                continue
            if line.startswith('LOCATION'):
                header_seen = True
                continue
            if not header_seen:
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            m = LOC_RE.match(loc)
            if not m: continue
            s, v = int(m.group(1)), int(m.group(2))
            rm = ROOT_RE.search(feats)
            if rm:
                rv[(s, v)].add(rm.group(1))
    return rv

def jaccard(a: set, b: set) -> float:
    u = a | b
    if not u: return 0.0
    return len(a & b) / len(u)

def ring_score(verse_roots):
    n = len(verse_roots)
    half = n // 2
    if half == 0: return 0.0, 0, []
    pair_scores = []
    for i in range(half):
        pair_scores.append(jaccard(verse_roots[i], verse_roots[n-1-i]))
    return sum(pair_scores)/half, half, pair_scores

# Prophet pericopes to test
PERICOPES = [
    # --- Noah ---
    ('Noah', '71:1-28 Surah Nuh (whole)', 71, 1, 28),
    ('Noah', '11:25-49 Hud Noah pericope', 11, 25, 49),
    ('Noah', '7:59-64 A`raf Noah', 7, 59, 64),
    ('Noah', '26:105-122 Shu`ara Noah', 26, 105, 122),

    # --- Moses (beyond Moses-deep) ---
    ('Moses', '28:7-42 Qasas birth narrative', 28, 7, 42),
    ('Moses', '20:9-98 Ta-Ha long Moses', 20, 9, 98),
    ('Moses', '7:103-162 A`raf Moses', 7, 103, 162),
    ('Moses', '26:10-68 Shu`ara Moses', 26, 10, 68),

    # --- Abraham ---
    ('Abraham', '2:124-141 Baqara (beyond 131-144)', 2, 124, 141),
    ('Abraham', '6:74-83 Aflachain An`am', 6, 74, 83),
    ('Abraham', '11:69-76 Hud angelic visitation', 11, 69, 76),
    ('Abraham', '14:35-41 Ibrahim prayer', 14, 35, 41),
    ('Abraham', '19:41-50 Maryam', 19, 41, 50),
    ('Abraham', '21:51-73 Anbiya idol-destruction', 21, 51, 73),
    ('Abraham', '26:69-104 Shu`ara', 26, 69, 104),
    ('Abraham', '37:83-113 Saffat sacrifice', 37, 83, 113),

    # --- Joseph ---
    ('Joseph', '12:1-111 whole Yusuf', 12, 1, 111),
    ('Joseph', '12:4-6 dream', 12, 4, 6),
    ('Joseph', '12:7-18 brothers', 12, 7, 18),
    ('Joseph', '12:36-42 prison', 12, 36, 42),
    ('Joseph', '12:58-93 recognition', 12, 58, 93),
    ('Joseph', '12:94-101 reunion', 12, 94, 101),

    # --- David / Solomon ---
    ('David/Solomon', '27:15-44 Naml hoopoe/Sheba', 27, 15, 44),
    ('David/Solomon', '38:17-40 Sad David/Solomon', 38, 17, 40),
    ('David/Solomon', '34:10-14 Saba Solomon jinn', 34, 10, 14),

    # --- Jonah ---
    ('Jonah', '37:139-148 Yunus whale', 37, 139, 148),
    ('Jonah', '10:1-109 whole Yunus', 10, 1, 109),

    # --- Jesus ---
    ('Jesus', '3:35-63 AL Imran birth/life', 3, 35, 63),
    ('Jesus', '5:109-120 Ma\'ida table', 5, 109, 120),
    ('Jesus', '19:16-40 Maryam', 19, 16, 40),

    # --- Adam ---
    ('Adam', '2:30-39 Baqara primordial', 2, 30, 39),
    ('Adam', '7:11-25 A`raf temptation', 7, 11, 25),
    ('Adam', '15:26-42 Hijr', 15, 26, 42),
    ('Adam', '20:115-127 Ta-Ha', 20, 115, 127),
]

def main():
    print('Loading morphology ...', file=sys.stderr)
    roots_per_verse = load_roots_per_verse()
    with open(QURAN_JSON, encoding='utf-8') as f:
        quran = json.load(f)
    surah_map = {s['id']: s for s in quran}
    # per-surah full verse-root lists
    surah_roots = {}
    for s in quran:
        sid = s['id']
        n = s['total_verses']
        surah_roots[sid] = [roots_per_verse.get((sid, v+1), set()) for v in range(n)]

    sahih_lines = SAHIH.read_text(encoding='utf-8').splitlines()
    verse_index = []
    for s in quran:
        for v in range(1, s['total_verses']+1):
            verse_index.append((s['id'], v))
    vmap = {sv: i for i, sv in enumerate(verse_index)}
    def sahih(s, v):
        return sahih_lines[vmap[(s, v)]]

    N_SHUFFLE = 2000
    results = []
    for prophet, label, sid, start, end in PERICOPES:
        window = surah_roots[sid][start-1:end]
        N = len(window)
        obs, half, pair_scores = ring_score(window)
        # Null A — intra-pericope shuffle
        nullA = []
        for t in range(N_SHUFFLE):
            rng = random.Random(sid * 100000 + start * 100 + t)
            perm = list(window)
            rng.shuffle(perm)
            nullA.append(ring_score(perm)[0])
        muA = statistics.fmean(nullA); sdA = statistics.pstdev(nullA) or 1e-12
        zA = (obs - muA) / sdA
        pA = (sum(1 for x in nullA if x >= obs) + 1) / (N_SHUFFLE + 1)

        # Null B — surah-wide shuffle, resample same-width window at same offset
        full = surah_roots[sid]
        nullB = []
        for t in range(N_SHUFFLE):
            rng = random.Random(sid * 100000 + start * 100 + t + 77777)
            perm = list(full)
            rng.shuffle(perm)
            sub = perm[start-1:end]
            nullB.append(ring_score(sub)[0])
        muB = statistics.fmean(nullB); sdB = statistics.pstdev(nullB) or 1e-12
        zB = (obs - muB) / sdB
        pB = (sum(1 for x in nullB if x >= obs) + 1) / (N_SHUFFLE + 1)

        # Top pair details
        pair_details = []
        for i in range(half):
            a_v = start + i
            b_v = end - i
            a = surah_roots[sid][a_v-1]
            b = surah_roots[sid][b_v-1]
            pair_details.append({
                'a_verse': a_v, 'b_verse': b_v,
                'jaccard': jaccard(a, b),
                'shared': sorted(a & b),
            })
        pair_details.sort(key=lambda x: -x['jaccard'])

        center_verse = None; center_text = None
        if N % 2 == 1:
            center_verse = start + N//2
            center_text = sahih(sid, center_verse)
        else:
            # two middle verses
            c1 = start + N//2 - 1; c2 = start + N//2
            center_verse = f"{c1}/{c2}"
            center_text = f"[{c1}] {sahih(sid, c1)} // [{c2}] {sahih(sid, c2)}"

        res = {
            'prophet': prophet,
            'label': label,
            'surah': sid, 'start': start, 'end': end, 'N': N,
            'observed': obs,
            'null_A_intra': {'mean': muA, 'std': sdA, 'z': zA, 'p_emp': pA},
            'null_B_surah': {'mean': muB, 'std': sdB, 'z': zB, 'p_emp': pB},
            'top_pairs': pair_details[:5],
            'center_verse': center_verse,
            'center_text': center_text,
        }
        results.append(res)
        print(f"{prophet:14s} {label[:40]:40s} N={N:3d} obs={obs:.3f} zA={zA:+.2f} zB={zB:+.2f} p_A={pA:.4f}", file=sys.stderr)

    # Bonferroni thresholds (41 tests, two nulls -> 82 tests; use the stricter)
    import math
    from statistics import NormalDist
    # one-sided alpha 0.05 / 41 = 0.001219 => z_crit
    nd = NormalDist()
    z_crit_41 = nd.inv_cdf(1 - 0.05/41)
    z_crit_82 = nd.inv_cdf(1 - 0.05/82)

    out = {
        'config': {
            'similarity': 'jaccard of verse root sets (QAC v0.4)',
            'nulls': {
                'A_intra': 'shuffle verse order within pericope (2000 trials)',
                'B_surah': 'shuffle full surah, resample window at same offset (2000 trials)',
            },
            'n_pericopes_tested': len(PERICOPES),
            'bonferroni_z_41': z_crit_41,
            'bonferroni_z_82': z_crit_82,
        },
        'results': results,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f'wrote {OUT_JSON}', file=sys.stderr)
    print(f'Bonferroni z thresholds: 41-test={z_crit_41:.2f}, 82-test={z_crit_82:.2f}', file=sys.stderr)

if __name__ == '__main__':
    main()
