"""Q028-al-qasas — pre-registered novel tests F-01..F-05.

Discipline: SHA-locks pre-regs at runtime; 10 000 perms; seed 20260507; equal NULL prominence.
"""

from __future__ import annotations
import hashlib
import json
import math
import os
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
QURAN_NT = ROOT / 'quran-text' / 'quran-no-tashkeel.json'
REVEAL = ROOT / 'data' / 'revelation-order.csv'
SURAH_DIR = ROOT / 'surahs' / 'Q028-al-qasas'
CSV_DIR = SURAH_DIR / 'csv'
CSV_DIR.mkdir(exist_ok=True, parents=True)

SEED = 20260507
N_PERM = 10000
BONF_K = 5
ALPHA_BON = 0.05 / BONF_K  # 0.01

# Pre-reg SHA expected values (computed 2026-05-07 at file-lock)
PREREG_SHAS = {
    'F-01': '0717e38d1749a70369591a0406a50b40c33aa0d0d9385fab609e7be4887ef218',
    'F-02': 'f32d033c43c9ca9676721cb5f0492c8d97a2145cef8c59c7bf829479f58ce886',
    'F-03': '80061fb62c8aed32f47f91ba90deba17601cb91d24e8f7430a6489625cdb1718',
    'F-04': '2e28b7a4129a8afb280eec2f6134509e3c5d9b5af36a5ea7e4737bda5a80efa9',
    'F-05': 'f9d5c2de81343db78c5794c14fbded3ec07793ed4a55345128d4612809dd741d',
}
PREREG_FILES = {
    'F-01': 'Q028-F-01-madyan-episode-lexical-isolation-prereg.md',
    'F-02': 'Q028-F-02-tsm-moses-twin-pair-prereg.md',
    'F-03': 'Q028-F-03-qarun-block-isolation-prereg.md',
    'F-04': 'Q028-F-04-q28-34-impediment-reference-prereg.md',
    'F-05': 'Q028-F-05-tsm-3-surah-joint-test-prereg.md',
}


def verify_sha(test_id: str) -> str:
    p = SURAH_DIR / PREREG_FILES[test_id]
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    expected = PREREG_SHAS[test_id]
    assert h == expected, f'{test_id} SHA MISMATCH: got {h} vs {expected}'
    return h


# --- token helpers ---
PAUSE_RE = re.compile(r'[ۖۗۚۛۜ۞۩ۘ]')
PREFIXES = ('وال', 'فال', 'ال', 'و', 'ف', 'ل', 'ب', 'ك', 's')


def strip_pause(t: str) -> str:
    return PAUSE_RE.sub(' ', t)


def tokens(t: str) -> list[str]:
    return [w for w in strip_pause(t).split() if w]


def stem(tok: str) -> str:
    """Strip a single Arabic prefix (al/wa/fa/li/bi/ka) for surface-form root collapsing."""
    for p in ('وال', 'فال', 'بال', 'كال', 'لل'):
        if tok.startswith(p) and len(tok) > len(p) + 1:
            return tok[len(p):]
    for p in ('ال',):
        if tok.startswith(p) and len(tok) > 3:
            return tok[2:]
    for p in ('و', 'ف', 'ل', 'ب', 'ك', 'س'):
        if tok.startswith(p) and len(tok) > 2:
            return tok[1:]
    return tok


def load_corpus():
    return json.load(open(QURAN_NT))


# ---------- Q028-F-01 — Madyan-episode lexical isolation ----------

def f01_madyan(corpus):
    verify_sha('F-01')
    rng = random.Random(SEED)
    q28 = corpus[27]
    verses = q28['verses']
    n = len(verses)  # 88

    # corpus token frequency
    corpus_counter: Counter[str] = Counter()
    for s in corpus:
        for v in s['verses']:
            for tok in tokens(v['text']):
                corpus_counter[tok] += 1
    # hapax = corpus-wide ≤ 1
    hapax_set = {t for t, c in corpus_counter.items() if c == 1}

    # Q28 per-verse tokens
    verse_tokens = [tokens(v['text']) for v in verses]
    verse_total = [len(t) for t in verse_tokens]

    # All 7-verse contiguous windows (1-indexed: starts 1..82)
    K = 7
    windows = []
    for start in range(1, n - K + 2):
        win_verses = list(range(start, start + K))
        toks = []
        for vidx in win_verses:
            toks.extend(verse_tokens[vidx - 1])
        n_tok = len(toks)
        n_hap = sum(1 for t in toks if t in hapax_set)
        density = n_hap / n_tok if n_tok else 0.0
        windows.append({'start': start, 'end': start + K - 1,
                        'n_tok': n_tok, 'n_hap': n_hap, 'density': density})

    # Target window: 22-28 (start=22)
    target = next(w for w in windows if w['start'] == 22)
    # Rank (descending density, 1 = highest)
    sorted_w = sorted(windows, key=lambda w: -w['density'])
    target_rank = sorted_w.index(target) + 1

    # H2: corpus-wide hapax tokens INSIDE window 22-28 (i.e. tokens with corpus-count == 1
    # AND that count appears in vv 22-28)
    win22_28_toks = []
    for vidx in range(22, 29):
        win22_28_toks.extend(verse_tokens[vidx - 1])
    win_hapax = [t for t in win22_28_toks if t in hapax_set]
    win_hapax_unique = sorted(set(win_hapax))
    h2_count = len(win_hapax_unique)
    h2_pass = h2_count >= 3

    # H3: مدين Madyan token concentration
    madyan_per_surah = []
    for s_idx, s in enumerate(corpus):
        cnt = 0
        for v in s['verses']:
            for tok in tokens(v['text']):
                # match مدين possibly with prefix و / ل / ف / ب
                core = tok
                for p in ('و', 'ف', 'ل', 'ب', 'ك'):
                    if core.startswith(p) and len(core) > 2:
                        core = core[1:]
                        break
                if core == 'مدين' or core == 'مدينا':
                    cnt += 1
        madyan_per_surah.append({'surah': s_idx + 1, 'count': cnt})
    total_madyan = sum(x['count'] for x in madyan_per_surah)
    q28_madyan = madyan_per_surah[27]['count']
    madyan_share = q28_madyan / total_madyan if total_madyan else 0.0
    h3_pass = madyan_share >= 0.50

    # Permutation null for H1: shuffle verses within Q28 N_PERM times,
    # measure window 22-28 hapax density rank in shuffled.
    n_better = 0
    flat = list(range(n))
    densities_in_perm = []
    for _ in range(N_PERM):
        rng.shuffle(flat)
        # Re-form the same 22-28 window with shuffled verses
        sel = flat[21:28]
        toks = []
        for vidx in sel:
            toks.extend(verse_tokens[vidx])
        n_tok = len(toks); n_hap = sum(1 for t in toks if t in hapax_set)
        d = n_hap / n_tok if n_tok else 0.0
        densities_in_perm.append(d)
        if d >= target['density']:
            n_better += 1
    p_perm = (n_better + 1) / (N_PERM + 1)

    h1_pass = (target_rank <= 4) and (p_perm < ALPHA_BON)

    sub_passes = sum([h1_pass, h2_pass, h3_pass])
    if sub_passes >= 2:
        verdict = 'VINDICATED'
    elif sub_passes == 0:
        verdict = 'NULL'
    else:
        verdict = 'DIRECTIONAL'

    out = {
        'finding_id': 'Q028-F-01',
        'prereg_sha': PREREG_SHAS['F-01'],
        'seed': SEED,
        'n_perm': N_PERM,
        'alpha_bon': ALPHA_BON,
        'h1': {
            'target_window': '22-28',
            'target_density': target['density'],
            'target_n_hap': target['n_hap'],
            'target_n_tok': target['n_tok'],
            'rank_of_82': target_rank,
            'p_perm_one_sided_upper': p_perm,
            'pass': h1_pass,
        },
        'h2': {
            'corpus_hapax_in_window_22_28': win_hapax_unique[:30],
            'count_unique_hapax': h2_count,
            'count_hapax_threshold': 3,
            'pass': h2_pass,
        },
        'h3': {
            'q28_madyan_count': q28_madyan,
            'corpus_total_madyan': total_madyan,
            'madyan_share_in_q28': madyan_share,
            'threshold_share': 0.50,
            'per_surah_distribution': [x for x in madyan_per_surah if x['count'] > 0],
            'pass': h3_pass,
        },
        'verdict': verdict,
        'top10_windows_by_density': [
            {'start': w['start'], 'end': w['end'], 'density': w['density'], 'n_hap': w['n_hap'], 'n_tok': w['n_tok']}
            for w in sorted_w[:10]
        ],
    }
    json.dump(out, open(CSV_DIR / 'Q028-F-01.json', 'w'), ensure_ascii=False, indent=2)
    print(f"F-01: verdict={verdict}, target_rank={target_rank}/82, p={p_perm:.4f}, hapax_in_window={h2_count}, madyan_share={madyan_share:.3f}")
    return out


# ---------- Q028-F-02 — TSM Moses-content twin-pair ----------

def get_block_tokens(corpus, surah_id: int, v_start: int, v_end: int) -> list[str]:
    s = corpus[surah_id - 1]
    out = []
    for v in s['verses']:
        if v_start <= v['id'] <= v_end:
            out.extend(stem(t) for t in tokens(v['text']))
    return out


def cosine(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    dot = sum(a.get(k, 0) * b.get(k, 0) for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


def f02_moses_twin(corpus):
    verify_sha('F-02')
    rng = random.Random(SEED + 1)

    # Define blocks
    M26 = get_block_tokens(corpus, 26, 10, 67)   # Q 26:10-67
    M28 = get_block_tokens(corpus, 28, 3, 43)    # Q 28:3-43
    M20 = get_block_tokens(corpus, 20, 9, 98)    # Q 20:9-98

    tf26 = Counter(M26); tf28 = Counter(M28); tf20 = Counter(M20)
    cos_26_28 = cosine(tf26, tf28)
    cos_26_20 = cosine(tf26, tf20)
    cos_28_20 = cosine(tf28, tf20)

    # H1: cos(M26, M28) > max(cos(M26, M20), cos(M28, M20))
    h1_pass_direction = cos_26_28 > max(cos_26_20, cos_28_20)

    # H2: contrast = cos_26_28 - mean(cos_26_20, cos_28_20)
    contrast = cos_26_28 - 0.5 * (cos_26_20 + cos_28_20)

    # Permutation null: pool tokens from all three blocks; randomly redistribute
    # the same block-sizes 10 000 times; record contrast distribution.
    pool = M26 + M28 + M20
    n26, n28, n20 = len(M26), len(M28), len(M20)
    n_total = len(pool)
    null_contrasts = []
    null_geq = 0
    for _ in range(N_PERM):
        rng.shuffle(pool)
        b26 = pool[:n26]; b28 = pool[n26:n26 + n28]; b20 = pool[n26 + n28:n26 + n28 + n20]
        c1 = cosine(Counter(b26), Counter(b28))
        c2 = cosine(Counter(b26), Counter(b20))
        c3 = cosine(Counter(b28), Counter(b20))
        ctr = c1 - 0.5 * (c2 + c3)
        null_contrasts.append(ctr)
        if ctr >= contrast:
            null_geq += 1
    p_perm = (null_geq + 1) / (N_PERM + 1)
    h2_pass = (contrast >= 0) and (p_perm < ALPHA_BON)

    if h1_pass_direction and h2_pass:
        verdict = 'PASS — TSM-Moses-twin-pair vindicated'
    elif h1_pass_direction or h2_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL — consolidates Wave-FALSIFIED §3.7 (muqaṭṭaʿāt ⊥ content axis)'

    out = {
        'finding_id': 'Q028-F-02',
        'prereg_sha': PREREG_SHAS['F-02'],
        'seed': SEED + 1,
        'n_perm': N_PERM,
        'alpha_bon': ALPHA_BON,
        'block_sizes': {'Q26:10-67': n26, 'Q28:3-43': n28, 'Q20:9-98': n20},
        'cosines': {
            'Q26<->Q28': cos_26_28,
            'Q26<->Q20': cos_26_20,
            'Q28<->Q20': cos_28_20,
        },
        'h1_direction_pass': h1_pass_direction,
        'h2_contrast': contrast,
        'h2_p_perm_one_sided_upper': p_perm,
        'h2_pass': h2_pass,
        'verdict': verdict,
    }
    json.dump(out, open(CSV_DIR / 'Q028-F-02.json', 'w'), ensure_ascii=False, indent=2)
    print(f"F-02: verdict={verdict}; cos(26,28)={cos_26_28:.4f}, cos(26,20)={cos_26_20:.4f}, cos(28,20)={cos_28_20:.4f}; contrast={contrast:.4f}, p={p_perm:.4f}")
    return out


# ---------- Q028-F-03 — Qārūn block isolation ----------

def f03_qarun(corpus):
    verify_sha('F-03')
    rng = random.Random(SEED + 2)
    q28 = corpus[27]
    verses = q28['verses']
    n = len(verses)
    K = 7

    # Per-verse stem-token list
    verse_stems = [[stem(t) for t in tokens(v['text'])] for v in verses]
    surah_total_tf = Counter()
    for v_stems in verse_stems:
        surah_total_tf.update(v_stems)

    # All 7-verse windows
    windows = []
    for start in range(1, n - K + 2):
        toks = []
        for vidx in range(start, start + K):
            toks.extend(verse_stems[vidx - 1])
        win_tf = Counter(toks)
        rest_tf = Counter()
        for k, v in surah_total_tf.items():
            rest_tf[k] = v - win_tf.get(k, 0)
        cos = cosine(win_tf, rest_tf)
        distinct = 1.0 - cos
        windows.append({'start': start, 'end': start + K - 1, 'cos_to_rest': cos,
                        'distinctness': distinct, 'n_tok': len(toks)})

    target_qarun = next(w for w in windows if w['start'] == 76)
    target_madyan = next(w for w in windows if w['start'] == 22)
    sorted_distinct = sorted(windows, key=lambda w: -w['distinctness'])
    qarun_rank = sorted_distinct.index(target_qarun) + 1
    madyan_rank = sorted_distinct.index(target_madyan) + 1
    h1_pass = qarun_rank <= 4

    # H2: pairwise window cosines among 82 windows
    pair_cos = []
    win_tfs = [Counter(verse_stems[w['start'] - 1] + sum(
        [verse_stems[w['start'] + i - 1] for i in range(1, K)], [])) for w in windows]
    for i in range(len(windows)):
        for j in range(i + 1, len(windows)):
            c = cosine(win_tfs[i], win_tfs[j])
            pair_cos.append((i, j, c))
    target_madyan_idx = next(i for i, w in enumerate(windows) if w['start'] == 22)
    target_qarun_idx = next(i for i, w in enumerate(windows) if w['start'] == 76)
    cos_madyan_qarun = cosine(win_tfs[target_madyan_idx], win_tfs[target_qarun_idx])
    sorted_pairs = sorted(pair_cos, key=lambda p: p[2])
    pair_rank = next(r for r, p in enumerate(sorted_pairs, start=1) if (p[0] == target_madyan_idx and p[1] == target_qarun_idx) or (p[0] == target_qarun_idx and p[1] == target_madyan_idx))
    bottom5_threshold = max(1, len(pair_cos) // 20)
    h2_pass = pair_rank <= bottom5_threshold

    # H3: قارون share corpus-wide
    qarun_per_surah = []
    for s_idx, s in enumerate(corpus):
        cnt = 0
        for v in s['verses']:
            for tok in tokens(v['text']):
                core = tok
                for p in ('و', 'ف', 'ل', 'ب', 'ك'):
                    if core.startswith(p) and len(core) > 2:
                        core = core[1:]; break
                if core == 'قارون' or core == 'قارونا':
                    cnt += 1
        if cnt > 0:
            qarun_per_surah.append({'surah': s_idx + 1, 'count': cnt})
    total_qarun = sum(x['count'] for x in qarun_per_surah)
    q28_qarun = next((x['count'] for x in qarun_per_surah if x['surah'] == 28), 0)
    qarun_share = q28_qarun / total_qarun if total_qarun else 0.0
    h3_pass = qarun_share >= 0.50

    sub_passes = sum([h1_pass, h2_pass, h3_pass])
    if sub_passes == 3:
        verdict = 'PASS'
    elif sub_passes == 0:
        verdict = 'NULL'
    else:
        verdict = 'DIRECTIONAL'

    out = {
        'finding_id': 'Q028-F-03',
        'prereg_sha': PREREG_SHAS['F-03'],
        'seed': SEED + 2,
        'n_perm': 0,
        'alpha_bon': ALPHA_BON,
        'h1': {
            'target_window': '76-82 (Qārūn)',
            'target_distinctness': target_qarun['distinctness'],
            'target_cos_to_rest': target_qarun['cos_to_rest'],
            'rank_of_82_distinctness_descending': qarun_rank,
            'pass': h1_pass,
        },
        'h2': {
            'cos_madyan_qarun': cos_madyan_qarun,
            'pair_rank_ascending_of_3321': pair_rank,
            'bottom5pct_threshold': bottom5_threshold,
            'pass': h2_pass,
        },
        'h3': {
            'q28_qarun_count': q28_qarun,
            'corpus_total_qarun': total_qarun,
            'qarun_share_in_q28': qarun_share,
            'per_surah_distribution': qarun_per_surah,
            'pass': h3_pass,
        },
        'reference': {
            'madyan_window_22_28_distinctness': target_madyan['distinctness'],
            'madyan_window_22_28_rank': madyan_rank,
        },
        'top10_distinct_windows': [
            {'start': w['start'], 'end': w['end'], 'distinctness': w['distinctness']}
            for w in sorted_distinct[:10]
        ],
        'verdict': verdict,
    }
    json.dump(out, open(CSV_DIR / 'Q028-F-03.json', 'w'), ensure_ascii=False, indent=2)
    print(f"F-03: verdict={verdict}; qarun rank={qarun_rank}/82, madyan rank={madyan_rank}/82, qarun share={qarun_share:.3f}, pair rank={pair_rank}/{len(pair_cos)}")
    return out


# ---------- Q028-F-04 — Q 28:34 impediment-reference ----------

def f04_impediment(corpus):
    verify_sha('F-04')
    rng = random.Random(SEED + 3)

    q28_v34 = next(v for v in corpus[27]['verses'] if v['id'] == 34)
    q28_v35 = next(v for v in corpus[27]['verses'] if v['id'] == 35)
    target_toks = [stem(t) for t in tokens(q28_v34['text']) + tokens(q28_v35['text'])]
    target_tf = Counter(target_toks)

    # Q 20:25-28
    q20_relief = []
    for v in corpus[19]['verses']:
        if 25 <= v['id'] <= 28:
            q20_relief.extend(stem(t) for t in tokens(v['text']))
    q20_relief_tf = Counter(q20_relief)

    # Corpus token frequencies
    corpus_counter: Counter[str] = Counter()
    for s in corpus:
        for v in s['verses']:
            for tok in tokens(v['text']):
                corpus_counter[stem(tok)] += 1

    # H1: shared low-freq tokens
    shared = set(target_tf) & set(q20_relief_tf)
    low_freq_shared = sorted(t for t in shared if corpus_counter.get(t, 0) <= 5)
    h1_pass = len(low_freq_shared) >= 2

    # H2: cosine target vs Q20:25-28 vs random pairs
    cos_obs = cosine(target_tf, q20_relief_tf)
    target_n = len(target_toks); ref_n = len(q20_relief)

    # Sample 10000 random verse-pairs (2-verse target + 4-verse reference) outside Mūsā
    moses_surahs = {7, 10, 11, 19, 20, 26, 27, 28, 40, 79}
    candidate_surahs = [i for i in range(114) if (i + 1) not in moses_surahs]
    null_count_geq = 0
    cosines = []
    for _ in range(N_PERM):
        # pick s_a and 2 consecutive verses
        s_a = candidate_surahs[rng.randint(0, len(candidate_surahs) - 1)]
        sa = corpus[s_a]
        if sa['total_verses'] < 2:
            continue
        v_start_a = rng.randint(1, sa['total_verses'] - 1)
        a_toks = []
        for v in sa['verses']:
            if v_start_a <= v['id'] <= v_start_a + 1:
                a_toks.extend(stem(t) for t in tokens(v['text']))
        # pick s_b and 4 consecutive verses
        s_b = candidate_surahs[rng.randint(0, len(candidate_surahs) - 1)]
        sb = corpus[s_b]
        if sb['total_verses'] < 4:
            continue
        v_start_b = rng.randint(1, sb['total_verses'] - 3)
        b_toks = []
        for v in sb['verses']:
            if v_start_b <= v['id'] <= v_start_b + 3:
                b_toks.extend(stem(t) for t in tokens(v['text']))
        c = cosine(Counter(a_toks), Counter(b_toks))
        cosines.append(c)
        if c >= cos_obs:
            null_count_geq += 1
    p_perm = (null_count_geq + 1) / (len(cosines) + 1)
    h2_pass = p_perm < ALPHA_BON

    if h1_pass and h2_pass:
        verdict = 'PASS'
    elif h1_pass or h2_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q028-F-04',
        'prereg_sha': PREREG_SHAS['F-04'],
        'seed': SEED + 3,
        'n_perm': N_PERM,
        'alpha_bon': ALPHA_BON,
        'note_locator_correction': "Pre-reg corrected the prompt's mis-located Q28:35; re-anchored to Q28:34 (impediment-reference) + Q28:35 (response). Logged before observation.",
        'h1': {
            'shared_tokens': sorted(shared),
            'shared_low_freq_tokens': low_freq_shared,
            'shared_low_freq_count': len(low_freq_shared),
            'threshold': 2,
            'pass': h1_pass,
        },
        'h2': {
            'cos_obs_q28_v34_35_vs_q20_v25_28': cos_obs,
            'p_perm_one_sided_upper': p_perm,
            'pass': h2_pass,
            'n_samples': len(cosines),
        },
        'verdict': verdict,
    }
    json.dump(out, open(CSV_DIR / 'Q028-F-04.json', 'w'), ensure_ascii=False, indent=2)
    print(f"F-04: verdict={verdict}; shared low-freq={len(low_freq_shared)} ({low_freq_shared}); cos={cos_obs:.4f}, p={p_perm:.4f}")
    return out


# ---------- Q028-F-05 — TSM 3-surah joint cohesion ----------

def f05_tsm_joint(corpus):
    verify_sha('F-05')
    rng = random.Random(SEED + 4)

    # Read revelation order CSV - find Meccan surahs
    meccan_ids = []
    if REVEAL.exists():
        with open(REVEAL) as fh:
            head = None
            for line in fh:
                row = line.strip().split(',')
                if head is None:
                    head = row; continue
                if 'meccan' in [c.lower() for c in row]:
                    try:
                        sid = int(row[head.index('surah')])
                        meccan_ids.append(sid)
                    except (ValueError, KeyError):
                        pass
    if not meccan_ids:
        # fallback: all 'meccan' from JSON
        meccan_ids = [s['id'] for s in corpus if s.get('type') == 'meccan']

    PROPHETS = ['موسى', 'إبراهيم', 'ابراهيم', 'نوح', 'هود', 'صالح', 'شعيب', 'لوط', 'إسماعيل', 'اسماعيل',
                'إدريس', 'ادريس', 'زكريا', 'يحيى', 'عيسى', 'يونس', 'داود', 'سليمان', 'أيوب', 'ايوب', 'يوسف']
    NARR = ['قال', 'قالوا', 'قالت', 'قالا', 'فلما', 'ولما', 'وإذ', 'إذ']

    def densities(s_idx: int):
        s = corpus[s_idx - 1]
        toks = []
        for v in s['verses']:
            toks.extend(tokens(v['text']))
        ntot = len(toks) or 1
        m = sum(1 for t in toks if stem(t) == 'موسى' or t == 'موسى')
        p = sum(1 for t in toks if stem(t) in PROPHETS or t in PROPHETS)
        n = sum(1 for t in toks if stem(t) in NARR or t in NARR)
        return (m / ntot, p / ntot, n / ntot, ntot)

    # All Meccan densities for z-scoring
    meccan_d = [(sid, *densities(sid)) for sid in meccan_ids]
    if not meccan_d:
        meccan_d = [(s['id'], *densities(s['id'])) for s in corpus]
    moses_arr = [d[1] for d in meccan_d]
    proph_arr = [d[2] for d in meccan_d]
    narr_arr = [d[3] for d in meccan_d]

    def mean(a): return sum(a) / len(a)
    def stdev(a):
        m = mean(a); var = sum((x - m) ** 2 for x in a) / len(a)
        return math.sqrt(var)
    mu_m = mean(moses_arr); sd_m = stdev(moses_arr) or 1
    mu_p = mean(proph_arr); sd_p = stdev(proph_arr) or 1
    mu_n = mean(narr_arr); sd_n = stdev(narr_arr) or 1
    median_m = sorted(moses_arr)[len(moses_arr) // 2]
    median_p = sorted(proph_arr)[len(proph_arr) // 2]
    median_n = sorted(narr_arr)[len(narr_arr) // 2]

    # Corpus-wide medians (for H2's "above corpus median" check)
    all_d = [(s['id'], *densities(s['id'])) for s in corpus]
    all_m = sorted([d[1] for d in all_d]); all_p = sorted([d[2] for d in all_d]); all_n = sorted([d[3] for d in all_d])
    corp_med_m = all_m[len(all_m)//2]; corp_med_p = all_p[len(all_p)//2]; corp_med_n = all_n[len(all_n)//2]

    def centroid(triple_ids):
        zs = []
        for sid in triple_ids:
            ds = densities(sid)
            zs.append(((ds[0]-mu_m)/sd_m, (ds[1]-mu_p)/sd_p, (ds[2]-mu_n)/sd_n))
        # mean z across the 3 axes, then mean of those
        per_axis_mean = [mean([zs[i][a] for i in range(3)]) for a in range(3)]
        return mean(per_axis_mean), per_axis_mean

    tsm_centroid, tsm_axis_means = centroid([26, 27, 28])

    # Random Meccan tuples
    null_centroids = []
    null_geq = 0
    for _ in range(N_PERM):
        triple = tuple(rng.sample(meccan_ids, 3))
        c, _ = centroid(triple)
        null_centroids.append(c)
        if c >= tsm_centroid:
            null_geq += 1
    p_perm = (null_geq + 1) / (N_PERM + 1)
    h1_pass = p_perm < ALPHA_BON

    # H2: count cells above corpus-median
    matrix = []
    for sid in [26, 27, 28]:
        ds = densities(sid)
        matrix.append({
            'surah': sid,
            'moses_density': ds[0], 'moses_above_med': ds[0] > corp_med_m,
            'prophet_density': ds[1], 'prophet_above_med': ds[1] > corp_med_p,
            'narr_density': ds[2], 'narr_above_med': ds[2] > corp_med_n,
        })
    cells_above = sum(int(c) for r in matrix for c in (r['moses_above_med'], r['prophet_above_med'], r['narr_above_med']))
    h2_pass = cells_above >= 6

    if h1_pass and h2_pass:
        verdict = 'PASS — TSM-cluster narrative-cohesion vindicated (CHALLENGES Wave-FALSIFIED §3.7)'
    elif h1_pass or h2_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL — consolidates Wave-FALSIFIED §3.7'

    out = {
        'finding_id': 'Q028-F-05',
        'prereg_sha': PREREG_SHAS['F-05'],
        'seed': SEED + 4,
        'n_perm': N_PERM,
        'alpha_bon': ALPHA_BON,
        'tsm_centroid': tsm_centroid,
        'tsm_axis_means': tsm_axis_means,
        'p_perm_one_sided_upper': p_perm,
        'h1_pass': h1_pass,
        'matrix_cells_above_corpus_median': cells_above,
        'matrix_threshold': 6,
        'h2_pass': h2_pass,
        'matrix_per_surah': matrix,
        'corpus_medians': {'moses': corp_med_m, 'prophet': corp_med_p, 'narr': corp_med_n},
        'verdict': verdict,
    }
    json.dump(out, open(CSV_DIR / 'Q028-F-05.json', 'w'), ensure_ascii=False, indent=2)
    print(f"F-05: verdict={verdict}; tsm_centroid={tsm_centroid:.3f}, p={p_perm:.4f}, cells_above={cells_above}/9")
    return out


def main():
    corpus = load_corpus()
    print('=' * 60)
    print('Q028-al-qasas — pre-registered novel tests F-01..F-05')
    print('seed=', SEED, 'N_PERM=', N_PERM, 'alpha_bon=', ALPHA_BON)
    print('=' * 60)
    f01_madyan(corpus)
    f02_moses_twin(corpus)
    f03_qarun(corpus)
    f04_impediment(corpus)
    f05_tsm_joint(corpus)
    print('All 5 done. Outputs in', CSV_DIR)


if __name__ == '__main__':
    main()
