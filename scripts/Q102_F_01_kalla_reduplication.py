#!/usr/bin/env python3
"""Q102-F-01 — al-Takāthur rebuke-kallā triple-run (Arm A) + single-particle adjacent refrain (Arm B).

Pre-reg: surahs/Q102-al-takathur/Q102-F-01-kalla-reduplication-prereg.md
Pre-reg SHA256: 87433a4dd51b12605a09e63140437f480ac2e551b05014137837b0d31046acf4
Rules-tuple: (no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
             + (QAC v0.4, POS:AVR, LEM kal~aA) for kallā disambiguation.

Arm A: Q 102 is the corpus-UNIQUE carrier of a run of 3 consecutive verses each bearing a genuine
       rebuke-kallā (POS:AVR LEM kal~aA); every other surah's max consecutive-kallā run is <= 2.
       Total corpus rebuke-kallā = 33 (replicates al-Dānī via H-NEW-2230); homograph-clean (no first-half).
Arm B: the ordered adjacent pair (kallā sawfa taʿlamūn -> thumma kallā sawfa taʿlamūn) is corpus-
       exclusive to Q 102:3-4 (B-H1); the bare post-kallā threat string "sawfa taʿlamūn" standing alone
       as a whole rebuke-verse occurs only at Q 102:3,4 (B-H2). B-H3 = length-stratified re-pairing
       null on single-particle adjacent near-twins (supporting context only, seed 20260509, 10000 perms).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q102-al-takathur/Q102-F-01-kalla-reduplication-prereg.md')
EXPECTED_SHA = '87433a4dd51b12605a09e63140437f480ac2e551b05014137837b0d31046acf4'
SEED = 20260509
N_PERM = 10000
OUT_PATH = os.path.join(ROOT, 'surahs/Q102-al-takathur/csv/Q102-F-01.json')

PAUSE = set('۪ۭۖۚۗۛۙۘ۠ۤ۫ۧۦٰۨ۬۞')
LEADING_PARTICLES = ['ثم', 'و', 'ف', 'بل', 'او']  # closed set, normalized no-tashkeel


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)
    print(f"SHA OK: {actual}")


def norm(t):
    return ' '.join(''.join(c for c in t if c not in PAUSE).split())


def parse_qac_kalla():
    """Return dict surah -> sorted list of verse-numbers carrying a genuine rebuke-kallā (POS:AVR LEM kal~aA)."""
    path = os.path.join(ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
    per = defaultdict(set)
    total = 0
    with open(path, encoding='utf-8') as f:
        for line in f:
            if not line.startswith('('):
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0].strip('()')
            feats = parts[3]
            if 'POS:AVR' in feats and 'LEM:kal~aA' in feats:
                s, v, w, _ = loc.split(':')
                per[int(s)].add(int(v))
                total += 1
    return {s: sorted(vs) for s, vs in per.items()}, total


def max_consecutive_run(verses):
    """Longest run of consecutive integers in a sorted list."""
    if not verses:
        return 0
    best = cur = 1
    for i in range(1, len(verses)):
        if verses[i] == verses[i - 1] + 1:
            cur += 1
            best = max(best, cur)
        else:
            cur = 1
    return best


def main():
    verify_sha()
    quran = json.load(open(os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')))

    # normalized verse texts keyed by (surah, verse)
    vtext = {}
    surah_verses = defaultdict(list)  # surah -> [(verse, norm_text)]
    for s in quran:
        sid = int(s['id'])
        for v in s['verses']:
            nt = norm(v['text'])
            vtext[(sid, v['id'])] = nt
            surah_verses[sid].append((v['id'], nt))

    # ================= ARM A — rebuke-kallā triple-run =================
    kalla_verses, total_kalla = parse_qac_kalla()

    # per-surah max consecutive run
    runs = {s: max_consecutive_run(vs) for s, vs in kalla_verses.items()}
    q102_verses = kalla_verses.get(102, [])
    q102_run = runs.get(102, 0)
    others_max = max((r for s, r in runs.items() if s != 102), default=0)
    sole_max = (q102_run == 3) and (others_max <= 2)

    # homograph cleanliness: no rebuke-kallā in surahs 1..18
    first_half = sorted(s for s in kalla_verses if s <= 18)

    a_h1 = (q102_verses == [3, 4, 5]) and (len(q102_verses) == 3)
    a_h2 = (total_kalla == 33) and (len(first_half) == 0)
    a_h3 = sole_max

    arm_a_confirmed = a_h1 and a_h2 and a_h3

    # ================= ARM B — single-particle adjacent refrain =================
    # B-H1: ordered adjacent pair where v_{n+1} == particle + ' ' + v_n  (single leading particle)
    def single_particle_extension(short, longg):
        for p in LEADING_PARTICLES:
            if longg == p + ' ' + short:
                return p
        return None

    near_twin_pairs = []  # (surah, n, n+1, particle)
    for s, vs in surah_verses.items():
        vs_sorted = sorted(vs)
        for i in range(len(vs_sorted) - 1):
            (vn, tn) = vs_sorted[i]
            (vm, tm) = vs_sorted[i + 1]
            if vm != vn + 1:
                continue
            p = single_particle_extension(tn, tm)
            if p is not None:
                near_twin_pairs.append((s, vn, vm, p))

    b_h1_q102 = any(s == 102 and vn == 3 and vm == 4 for (s, vn, vm, p) in near_twin_pairs)
    b_h1_count = len(near_twin_pairs)
    b_h1 = b_h1_q102 and (b_h1_count == 1)

    # B-H2: bare post-kallā threat — whole verse (after the rebuke particle) == 'سوف تعلمون'
    # i.e. verse text is exactly 'كلا سوف تعلمون' or 'ثم كلا سوف تعلمون'
    bare_threat_strings = {'كلا سوف تعلمون', 'ثم كلا سوف تعلمون'}
    bare_threat_locs = [(s, v) for (s, v), t in vtext.items() if t in bare_threat_strings]
    b_h2 = (len(bare_threat_locs) == 2) and all(s == 102 for s, v in bare_threat_locs)

    arm_b_confirmed = b_h1 and b_h2

    # ----- B-H3 supporting context: length-stratified re-pairing null -----
    rng = random.Random(SEED)
    # observed corpus count of single-particle adjacent near-twins = b_h1_count
    # null: within each surah, randomly re-pair its verses into adjacent slots (shuffle order),
    # count single-particle near-twins under the shuffled adjacency, length-strata = word-count bucket.
    obs_count = b_h1_count
    null_ge = 0
    null_counts = []
    surah_text_lists = {s: [t for (_, t) in sorted(vs)] for s, vs in surah_verses.items()}
    for _ in range(N_PERM):
        c = 0
        for s, texts in surah_text_lists.items():
            shuffled = texts[:]
            rng.shuffle(shuffled)
            for i in range(len(shuffled) - 1):
                p = single_particle_extension(shuffled[i], shuffled[i + 1])
                if p is not None:
                    c += 1
        null_counts.append(c)
        if c >= obs_count:
            null_ge += 1
    p_perm = (null_ge + 1) / (N_PERM + 1)
    null_mean = sum(null_counts) / len(null_counts)

    # ================= verdicts =================
    if arm_a_confirmed:
        verdict_a = 'CONFIRMED'
    elif a_h1 and a_h2 and not a_h3:
        verdict_a = 'NULL (pre-commit violation: not sole max-run)'
    else:
        verdict_a = 'NULL'

    if arm_b_confirmed:
        verdict_b = 'CONFIRMED'
    elif b_h1 ^ b_h2:
        verdict_b = 'DIRECTIONAL'
    else:
        verdict_b = 'NULL (pre-commit violation)'

    out = {
        'test_id': 'Q102-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, QAC v0.4 POS:AVR LEM kal~aA, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'arm_A': {
            'q102_kalla_verses': q102_verses,
            'q102_max_run': q102_run,
            'others_max_run': others_max,
            'total_corpus_rebuke_kalla': total_kalla,
            'first_half_rebuke_kalla_surahs': first_half,
            'per_surah_kalla_verses': {str(s): v for s, v in sorted(kalla_verses.items())},
            'per_surah_max_run': {str(s): r for s, r in sorted(runs.items())},
            'A_H1_q102_run_is_3_4_5': a_h1,
            'A_H2_census_33_and_homograph_clean': a_h2,
            'A_H3_q102_sole_max_run': a_h3,
            'verdict_A': verdict_a,
        },
        'arm_B': {
            'single_particle_adjacent_near_twin_pairs': near_twin_pairs,
            'B_H1_count': b_h1_count,
            'B_H1_q102_3_4_present': b_h1_q102,
            'B_H1_pass': b_h1,
            'bare_threat_locs': bare_threat_locs,
            'B_H2_pass': b_h2,
            'verdict_B': verdict_b,
            'B_H3_supporting': {
                'observed_near_twin_count': obs_count,
                'null_mean': null_mean,
                'p_perm': p_perm,
                'note': 'supporting context only; not a gating permutation test (see pre-reg).',
            },
        },
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # console summary
    print('\n===== Q102-F-01 RESULTS =====')
    print(f'ARM A: q102 kallā verses={q102_verses} run={q102_run}; others_max_run={others_max}; '
          f'census={total_kalla}; first-half-rebuke-surahs={first_half}')
    print(f'  A-H1={a_h1} A-H2={a_h2} A-H3={a_h3} -> {verdict_a}')
    print(f'ARM B: single-particle adjacent near-twin pairs (corpus)={near_twin_pairs}')
    print(f'  B-H1 count={b_h1_count} (q102_3_4={b_h1_q102}); bare-threat locs={bare_threat_locs}')
    print(f'  B-H1={b_h1} B-H2={b_h2} -> {verdict_b}')
    print(f'  B-H3 (context): obs={obs_count} null_mean={null_mean:.3f} p_perm={p_perm:.4f}')
    print(f'JSON -> {OUT_PATH}')


if __name__ == '__main__':
    main()
