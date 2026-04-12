#!/usr/bin/env python3
"""
Phase C — Chiastic / ring-composition audit across all 114 surahs.

Pipeline:
  1. Build R(v) = set of triliteral roots in each verse from QAC morphology.
  2. score(surah) = sum_{i=1..N//2} jaccard(R(v_i), R(v_{N+1-i})), normalised by floor(N/2).
  3. Null model: shuffle verse order in each surah, seeded with surah_id*1000 + trial.
     We use 200 shuffles per surah for stability.
  4. Rank surahs by z-score (observed vs shuffle distribution).
  5. Top-5 ring diagrams.
  6. Cross-check Cuypers (5) and Farrin (2).
  7. Sub-surah sliding windows (sizes 5..15) for surahs with N >= 10.
  8. Cross-surah ring at the whole-Quran scale: pair surah k with 115-k,
     similarity = jaccard of their verse-aggregated root sets, normalised, vs
     null shuffles of the surah index 1..114.
  9. Center-verse semantics for top rings.

Outputs:
  - findings/phase-c-structures/chiastic-audit.md (writeup)
  - analysis/notebooks/chiastic_audit_results.json (machine-readable)
"""
from __future__ import annotations
import json, re, math, random, statistics, os, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/grey/Downloads/quran')
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
MORPH = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
SAHIH = ROOT / 'data/translations/en.sahih.txt'
OUT_MD = ROOT / 'findings/phase-c-structures/chiastic-audit.md'
OUT_JSON = ROOT / 'analysis/notebooks/chiastic_audit_results.json'

# ---- 1. load morphology -> roots per verse ------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

def load_roots_per_verse():
    """Returns dict[(surah, verse)] -> set(root_str)."""
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
            if not m:
                continue
            s, v, w, seg = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
            rm = ROOT_RE.search(feats)
            if rm:
                rv[(s, v)].add(rm.group(1))
    return rv

# ---- 2. similarity --------------------------------------------------------
def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    u = a | b
    if not u:
        return 0.0
    return len(a & b) / len(u)

# ---- 3. ring score --------------------------------------------------------
def ring_score(verse_roots: list[set]) -> tuple[float, int, list[float]]:
    """verse_roots in surah order. Returns (mean_pair_jaccard, n_pairs, pair_scores)."""
    n = len(verse_roots)
    half = n // 2
    if half == 0:
        return 0.0, 0, []
    pair_scores = []
    for i in range(half):
        a = verse_roots[i]
        b = verse_roots[n - 1 - i]
        pair_scores.append(jaccard(a, b))
    return sum(pair_scores) / half, half, pair_scores

# ---- main -----------------------------------------------------------------
def main():
    print('Loading morphology …', file=sys.stderr)
    roots_per_verse = load_roots_per_verse()

    with open(QURAN_JSON, encoding='utf-8') as f:
        quran = json.load(f)

    # build per-surah verse-root lists in canonical order
    surah_data = []  # list of dicts
    for s in quran:
        sid = s['id']
        verses = s['verses']
        v_roots = [roots_per_verse.get((sid, v['id']), set()) for v in verses]
        surah_data.append({
            'id': sid,
            'name': s['name'],
            'transliteration': s['transliteration'],
            'type': s['type'],
            'n_verses': len(verses),
            'v_roots': v_roots,
        })

    # ---- observed ring scores + null distribution -----------------------
    N_SHUFFLES = 200
    results = []
    for s in surah_data:
        sid = s['id']
        n = s['n_verses']
        if n < 2:
            results.append({**{k: s[k] for k in ['id','name','transliteration','type','n_verses']},
                            'observed': None, 'mean_null': None, 'std_null': None,
                            'z': None, 'p_empirical': None, 'pair_scores': []})
            continue
        obs, half, pair_scores = ring_score(s['v_roots'])
        null_scores = []
        for trial in range(N_SHUFFLES):
            rng = random.Random(sid * 1000 + trial)
            perm = list(s['v_roots'])
            rng.shuffle(perm)
            ns, _, _ = ring_score(perm)
            null_scores.append(ns)
        mean_null = statistics.fmean(null_scores)
        std_null = statistics.pstdev(null_scores) or 1e-12
        z = (obs - mean_null) / std_null
        p_emp = (sum(1 for x in null_scores if x >= obs) + 1) / (N_SHUFFLES + 1)
        results.append({
            'id': sid, 'name': s['name'], 'transliteration': s['transliteration'],
            'type': s['type'], 'n_verses': n,
            'observed': obs, 'mean_null': mean_null, 'std_null': std_null,
            'z': z, 'p_empirical': p_emp, 'pair_scores': pair_scores,
        })

    # ---- rank ----------------------------------------------------------
    ranked = [r for r in results if r['z'] is not None]
    ranked.sort(key=lambda r: r['z'], reverse=True)

    # ---- top 5 detailed pairs ------------------------------------------
    sahih_lines = SAHIH.read_text(encoding='utf-8').splitlines()
    # build verse-index lookup: list of (surah, verse) in canonical order
    verse_index = []
    for s in surah_data:
        for v_idx in range(1, s['n_verses'] + 1):
            verse_index.append((s['id'], v_idx))
    assert len(verse_index) == 6236
    def sahih_for(s, v):
        idx = verse_index.index((s, v))
        return sahih_lines[idx]
    # faster lookup
    vmap = {sv: i for i, sv in enumerate(verse_index)}
    def sahih(s, v):
        return sahih_lines[vmap[(s, v)]]

    top5 = ranked[:5]
    top5_diagrams = []
    for r in top5:
        sid = r['id']
        s = next(x for x in surah_data if x['id'] == sid)
        n = s['n_verses']
        half = n // 2
        pairs = []
        for i in range(half):
            a_idx = i + 1
            b_idx = n - i
            a = s['v_roots'][i]
            b = s['v_roots'][n - 1 - i]
            shared = sorted(a & b)
            pairs.append({'a': a_idx, 'b': b_idx, 'jaccard': jaccard(a, b),
                          'shared_roots': shared,
                          'a_n_roots': len(a), 'b_n_roots': len(b)})
        center = (n + 1) // 2 if n % 2 == 1 else None
        top5_diagrams.append({
            'id': sid, 'name': s['name'], 'transliteration': s['transliteration'],
            'n_verses': n, 'half_pairs': pairs,
            'center_verse_index': center,
            'center_verse_text': sahih(sid, center) if center else None,
            'observed': r['observed'], 'z': r['z'], 'p': r['p_empirical'],
        })

    # ---- sub-surah sliding windows -----------------------------
    SUBSURAH_RESULTS = []
    for s in surah_data:
        if s['n_verses'] < 10:
            continue
        for w in range(5, 16):
            if w > s['n_verses']:
                break
            for start in range(0, s['n_verses'] - w + 1):
                window = s['v_roots'][start:start + w]
                obs, half, pairs = ring_score(window)
                # quick null on the same window
                null_scores = []
                for trial in range(50):
                    rng = random.Random(s['id'] * 100000 + start * 100 + w * 10 + trial)
                    perm = list(window)
                    rng.shuffle(perm)
                    ns, _, _ = ring_score(perm)
                    null_scores.append(ns)
                mean_null = statistics.fmean(null_scores)
                std_null = statistics.pstdev(null_scores) or 1e-12
                z = (obs - mean_null) / std_null
                if obs < 0.20:
                    continue  # skip noise
                SUBSURAH_RESULTS.append({
                    'surah': s['id'], 'name': s['transliteration'],
                    'start_verse': start + 1, 'end_verse': start + w,
                    'window': w, 'obs': obs, 'z': z,
                    'mean_null': mean_null, 'std_null': std_null,
                })
    SUBSURAH_RESULTS.sort(key=lambda r: (r['z'], r['obs']), reverse=True)
    top_sub = SUBSURAH_RESULTS[:25]

    # ---- cross-surah ring at whole-Quran scale -----------------
    # Build per-surah aggregated root set
    surah_root_set = {s['id']: set().union(*s['v_roots']) for s in surah_data}
    def cross_score(order):
        """order: list of 114 surah ids in some order. Pair k with 115-k."""
        total = 0.0
        cnt = 0
        for i in range(57):
            a_id = order[i]
            b_id = order[113 - i]
            total += jaccard(surah_root_set[a_id], surah_root_set[b_id])
            cnt += 1
        return total / cnt
    canonical_order = [s['id'] for s in surah_data]
    cross_obs = cross_score(canonical_order)
    cross_null = []
    for trial in range(2000):
        rng = random.Random(7777 + trial)
        perm = list(canonical_order)
        rng.shuffle(perm)
        cross_null.append(cross_score(perm))
    cross_mean = statistics.fmean(cross_null)
    cross_std = statistics.pstdev(cross_null)
    cross_z = (cross_obs - cross_mean) / (cross_std or 1e-12)
    cross_p = (sum(1 for x in cross_null if x >= cross_obs) + 1) / (len(cross_null) + 1)

    # ---- output JSON ---------------------------------
    out = {
        'config': {
            'similarity': 'jaccard of verse root sets',
            'normalisation': 'sum of pair-jaccard / floor(N/2)',
            'n_shuffles_intra': N_SHUFFLES,
            'n_shuffles_cross': 2000,
            'morph_source': 'Quranic Arabic Corpus 0.4 (Dukes)',
            'text_source': 'quran-no-tashkeel.json',
        },
        'all_surah_scores': sorted(results, key=lambda r: -(r['z'] or -9)),
        'top5_diagrams': top5_diagrams,
        'top_subsurah': top_sub,
        'cross_surah_ring': {
            'observed': cross_obs, 'mean_null': cross_mean,
            'std_null': cross_std, 'z': cross_z, 'p_empirical': cross_p,
        },
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, default=str)
    print(f'wrote {OUT_JSON}', file=sys.stderr)
    print(f'top 20 by z:', file=sys.stderr)
    for r in ranked[:20]:
        print(f"  {r['id']:3d} {r['transliteration']:20s} N={r['n_verses']:4d} obs={r['observed']:.4f} z={r['z']:6.2f} p={r['p_empirical']:.3f}", file=sys.stderr)
    print(f"surah 2 (Al-Baqarah): rank={[i for i,r in enumerate(ranked) if r['id']==2][0]+1}/{len(ranked)} z={[r['z'] for r in ranked if r['id']==2][0]:.2f}", file=sys.stderr)
    print(f"surah 5 (Al-Ma'ida):  rank={[i for i,r in enumerate(ranked) if r['id']==5][0]+1}/{len(ranked)} z={[r['z'] for r in ranked if r['id']==5][0]:.2f}", file=sys.stderr)
    print(f"cross-surah ring: obs={cross_obs:.4f} null={cross_mean:.4f} z={cross_z:.2f} p={cross_p:.3f}", file=sys.stderr)

if __name__ == '__main__':
    main()
