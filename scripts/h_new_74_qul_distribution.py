#!/usr/bin/env python3
"""H-NEW-74 — Comprehensive distribution analysis of the Quranic *qul*
imperative (قل = "Say!"; canonical filter POS:V|IMPV|LEM:qaAla|2MS).

Pre-registration:
    /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-74-qul-distribution-prereg.md

Cells (Bonferroni k=6, α_bon=0.00833):
  1. Total count == 332 (MW-control).
  2. Per-surah distribution (descriptive: top-10/bottom-N + density).
  3. Surah-initial qul (v1, w1) and fast-opening (v ≤ 3).
  4. Formulaic-frame catalog (qul + X1, qul + X1 + X2).
  5. qul-density × Meccan/Medinan Mann-Whitney U.
  6. qul-density × Nöldeke 4-phase Kruskal-Wallis.

Seed: 20260417.
"""
from __future__ import annotations
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-74.json'
SEED = 20260417

# ============================================================
# 0. Load Tanzil JSON for surah text + metadata
# ============================================================
with open(ROOT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    quran = json.load(f)

surah_meta = {}
for s in quran:
    surah_meta[s['id']] = {
        'name': s['name'],
        'transliteration': s['transliteration'],
        'type': s['type'],
        'total_verses': s['total_verses'],
    }

# Build (surah, verse) -> token list (no-tashkeel surface)
TASHKEEL_RE = re.compile(r'[\u064B-\u065F\u0670\u0640\u06D6-\u06ED]')
PUNCT_RE = re.compile(r'[\u06D4\u06DD\u06DE\u06DF\u060C\u061B\u061F\u0640\u200C\u200D\u200E\u200F\u00B7]+')

def normalize_token(w: str) -> str:
    w = TASHKEEL_RE.sub('', w)
    w = PUNCT_RE.sub('', w)
    for src, dst in [('أ','ا'),('إ','ا'),('آ','ا'),('ٱ','ا'),('ء','ا'),
                     ('ؤ','و'),('ئ','ي'),('ى','ي'),('ة','ه')]:
        w = w.replace(src, dst)
    return w.strip()

verse_tokens = {}    # (sid, vid) -> list of normalised tokens
verse_text   = {}    # (sid, vid) -> raw text
for s in quran:
    sid = s['id']
    for v in s['verses']:
        vid = v['id']
        text = v['text']
        verse_text[(sid, vid)] = text
        toks = [normalize_token(t) for t in text.split()]
        toks = [t for t in toks if t]
        verse_tokens[(sid, vid)] = toks

# ============================================================
# 1. Load chronology (Nöldeke + Egyptian-standard period)
# ============================================================
chronology = {}
with open(ROOT / 'data/revelation-order.csv', encoding='utf-8') as f:
    header = f.readline()
    for line in f:
        parts = line.rstrip('\n').split(',')
        if len(parts) < 7:
            continue
        rev_ord, mush, name_ar, name_tl, period, nold_ord, nold_phase = parts[:7]
        try:
            sid = int(mush)
        except ValueError:
            continue
        chronology[sid] = {
            'period': period.strip(),     # 'Meccan' / 'Medinan'
            'phase': nold_phase.strip(),  # 'Early Meccan' / 'Middle Meccan' / 'Late Meccan' / 'Medinan'
            'noldeke_order': int(nold_ord),
            'rev_order': int(rev_ord),
        }

print(f"Loaded {len(quran)} surahs, {len(verse_tokens)} verses; "
      f"chronology for {len(chronology)} surahs.", file=sys.stderr)

# ============================================================
# 2. Load QAC morphology — extract qul-tokens
#    Filter: POS:V & IMPV & LEM:qaAla & 2MS
# ============================================================
qul_locations: list[dict] = []
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')

with open(ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt',
          encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        loc, surface, tag, feats = parts[0], parts[1], parts[2], parts[3]
        # Canonical four-feature filter
        if 'POS:V' not in feats:
            continue
        if 'IMPV' not in feats:
            continue
        if 'LEM:qaAla' not in feats:
            continue
        if '|2MS' not in feats:
            continue
        m = LOC_RE.match(loc)
        if not m:
            continue
        sid, vid, wid, pid = (int(x) for x in m.groups())
        qul_locations.append({
            'sid': sid, 'vid': vid, 'wid': wid, 'pid': pid,
            'surface': surface,
            'feats': feats,
        })

total_qul = len(qul_locations)
print(f"qul (canonical filter) total = {total_qul}", file=sys.stderr)

# ============================================================
# Cell 1 — total-count MW control
# ============================================================
cell1 = {
    'total_qul': total_qul,
    'expected': 332,
    'pass': total_qul == 332,
}
print(f"Cell 1 (total-count MW): {cell1['pass']} ({total_qul} vs expected 332)",
      file=sys.stderr)

# ============================================================
# Cell 2 — per-surah distribution
# ============================================================
qul_per_surah = Counter()
qul_per_surah_first_v = defaultdict(list)  # sid -> sorted list of vids of qul tokens
for q in qul_locations:
    qul_per_surah[q['sid']] += 1
    qul_per_surah_first_v[q['sid']].append(q['vid'])

per_surah_table = []
for sid in range(1, 115):
    n = qul_per_surah.get(sid, 0)
    vc = surah_meta[sid]['total_verses']
    density = (n * 100.0 / vc) if vc else 0.0
    per_surah_table.append({
        'sid': sid,
        'name': surah_meta[sid]['name'],
        'transliteration': surah_meta[sid]['transliteration'],
        'period': chronology.get(sid, {}).get('period', ''),
        'phase': chronology.get(sid, {}).get('phase', ''),
        'verse_count': vc,
        'qul_count': n,
        'qul_density_per_100': round(density, 3),
    })

# top-10 by COUNT
top10_count = sorted(per_surah_table, key=lambda r: -r['qul_count'])[:10]
# top-10 by DENSITY (only surahs with at least 1 qul)
top10_density = sorted(
    [r for r in per_surah_table if r['qul_count'] > 0],
    key=lambda r: -r['qul_density_per_100'])[:10]
zero_qul = [r for r in per_surah_table if r['qul_count'] == 0]

cell2 = {
    'top10_by_count': top10_count,
    'top10_by_density': top10_density,
    'zero_qul_count': len(zero_qul),
    'zero_qul_surahs': [r['sid'] for r in zero_qul],
    'surahs_with_qul': sum(1 for r in per_surah_table if r['qul_count'] > 0),
}
print(f"Cell 2: top-10 (by count) ranges {top10_count[0]['qul_count']}-"
      f"{top10_count[-1]['qul_count']}; {len(zero_qul)} surahs have NO qul.",
      file=sys.stderr)

# ============================================================
# Cell 3 — surah-initial / fast-opening qul
# ============================================================
v1_w1 = []   # qul at (v=1, w=1)
fast = []    # first qul of surah occurs at v <= 3
for sid in sorted(qul_per_surah_first_v):
    vids = sorted(qul_per_surah_first_v[sid])
    first_v = vids[0]
    # find the wid of the very first qul in this surah:
    first_qul = sorted([q for q in qul_locations if q['sid'] == sid],
                       key=lambda q: (q['vid'], q['wid']))[0]
    if first_qul['vid'] == 1 and first_qul['wid'] == 1:
        v1_w1.append(sid)
    if first_qul['vid'] <= 3:
        fast.append({'sid': sid, 'first_vid': first_qul['vid'],
                     'first_wid': first_qul['wid']})

predicted_v1_w1 = {72, 109, 112, 113, 114}
cell3 = {
    'v1_w1_qul_openers': sorted(v1_w1),
    'predicted_v1_w1': sorted(predicted_v1_w1),
    'pass': set(v1_w1) == predicted_v1_w1,
    'fast_openers_v_le_3': sorted(fast, key=lambda r: r['sid']),
}
print(f"Cell 3 v1-w1 qul-openers: {sorted(v1_w1)} "
      f"(predicted {sorted(predicted_v1_w1)}; pass={cell3['pass']})",
      file=sys.stderr)

# ============================================================
# Cell 4 — formulaic-frame catalog (qul + X1, qul + X1 + X2)
# ============================================================
# For each qul, take the next 1 / 2 / 3 normalised tokens within the same verse.
frames_1 = Counter()
frames_2 = Counter()
frames_3 = Counter()
qul_with_frames = []
for q in qul_locations:
    sid, vid, wid = q['sid'], q['vid'], q['wid']
    toks = verse_tokens[(sid, vid)]
    # locate qul: surface token at wid (1-indexed)
    if wid - 1 >= len(toks):
        # mismatch (shouldn't happen but guard)
        continue
    after = toks[wid:]   # tokens after qul
    # Pad to 3
    nx1 = after[0] if len(after) > 0 else ''
    nx2 = after[1] if len(after) > 1 else ''
    nx3 = after[2] if len(after) > 2 else ''
    if nx1:
        frames_1[(nx1,)] += 1
    if nx1 and nx2:
        frames_2[(nx1, nx2)] += 1
    if nx1 and nx2 and nx3:
        frames_3[(nx1, nx2, nx3)] += 1
    qul_with_frames.append({
        'sid': sid, 'vid': vid, 'wid': wid,
        'nx1': nx1, 'nx2': nx2, 'nx3': nx3,
    })

# Pre-registered formulaic frame match: check each predicate.
def matches_frame(frame_predicate, qul_token_record):
    """frame_predicate is a list of (slot, candidates) tuples."""
    for slot, cands in frame_predicate:
        if slot == 1:
            if qul_token_record['nx1'] not in cands:
                return False
        elif slot == 2:
            if qul_token_record['nx2'] not in cands:
                return False
        elif slot == 3:
            if qul_token_record['nx3'] not in cands:
                return False
    return True

# Each formulaic frame is a name → list of (slot, set-of-candidate-tokens)
# All tokens are NORMALISED (tashkeel-stripped, hamza-collapsed)
PRE_REG_FRAMES = {
    'qul_aʿūdhu':       [(1, {'اعوذ'})],
    'qul_huwa':         [(1, {'هو'})],
    'qul_yā_ayyuhā':    [(1, {'يا'}), (2, {'ايها'})],
    'qul_innī_innamā':  [(1, {'انى', 'انما', 'ان', 'انا'})],  # certainty frame
    'qul_law':          [(1, {'لو'})],
    'qul_hal':          [(1, {'هل'})],
    'qul_man':          [(1, {'من'})],
    'qul_li-':          [(1, {'لمن', 'للناس', 'للذين'})],   # surface-merged li-
    'qul_aʾa-':         [(1, {'انعبد', 'اتتخذون', 'اتعبدون', 'افغير', 'افلم',
                              'اولم', 'افلا', 'افتصبرون', 'افنضرب'})],
    # Additional discovered frames (still pre-registered as candidates):
    'qul_yā_ahla':      [(1, {'يا'}), (2, {'اهل'})],
    'qul_li-lladhīna':  [(1, {'للذين'})],
    'qul_kafā':         [(1, {'كفى'})],
    'qul_arā':          [(1, {'ارايتم', 'ارايت'})],
    'qul_amara':        [(1, {'امر'})],
    'qul_aʾaghayra':    [(1, {'افغير', 'اغير'})],
}

frame_matches = {name: 0 for name in PRE_REG_FRAMES}
frame_match_locations = {name: [] for name in PRE_REG_FRAMES}
for r in qul_with_frames:
    for name, pred in PRE_REG_FRAMES.items():
        if matches_frame(pred, r):
            frame_matches[name] += 1
            frame_match_locations[name].append((r['sid'], r['vid'], r['wid']))

frames_passing_threshold = [name for name, c in frame_matches.items() if c >= 5]
cell4 = {
    'frame_match_counts': dict(sorted(frame_matches.items(),
                                       key=lambda kv: -kv[1])),
    'frames_passing_threshold_5': frames_passing_threshold,
    'pass': len(frames_passing_threshold) >= 3,
    'top20_frames_1word': [
        {'frame': ' '.join(k), 'count': v}
        for k, v in frames_1.most_common(20)
    ],
    'top20_frames_2word': [
        {'frame': ' '.join(k), 'count': v}
        for k, v in frames_2.most_common(20)
    ],
    'top20_frames_3word': [
        {'frame': ' '.join(k), 'count': v}
        for k, v in frames_3.most_common(20)
    ],
}
print(f"Cell 4: {len(frames_passing_threshold)} frames pass ≥5x "
      f"({frames_passing_threshold})", file=sys.stderr)

# ============================================================
# Cell 5 — qul-density × Meccan/Medinan Mann-Whitney U
# ============================================================
def mann_whitney_u(x, y):
    """Two-sample Mann-Whitney U with normal approximation (two-sided).
    Returns (U, z, p)."""
    n1, n2 = len(x), len(y)
    if n1 == 0 or n2 == 0:
        return (None, None, 1.0)
    combined = sorted([(v, 'x') for v in x] + [(v, 'y') for v in y],
                      key=lambda r: r[0])
    # Compute ranks (average rank for ties)
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1  # 1-indexed
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    rank_sum_x = sum(r for r, (_, lbl) in zip(ranks, combined) if lbl == 'x')
    U1 = rank_sum_x - n1 * (n1 + 1) / 2.0
    U2 = n1 * n2 - U1
    U = min(U1, U2)
    mu_U = n1 * n2 / 2.0
    sigma_U = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)
    if sigma_U == 0:
        return (U, 0.0, 1.0)
    z = (U - mu_U) / sigma_U
    # two-sided p via normal CDF
    p = math.erfc(abs(z) / math.sqrt(2.0))
    return (U, z, p)

mecc_dens = [r['qul_density_per_100'] for r in per_surah_table
             if r['period'] == 'Meccan']
med_dens = [r['qul_density_per_100'] for r in per_surah_table
            if r['period'] == 'Medinan']
U, z, p_mw = mann_whitney_u(mecc_dens, med_dens)
cell5 = {
    'mecc_n': len(mecc_dens),
    'med_n': len(med_dens),
    'mecc_mean_density': round(sum(mecc_dens) / len(mecc_dens), 3),
    'med_mean_density': round(sum(med_dens) / len(med_dens), 3),
    'mecc_median_density': round(sorted(mecc_dens)[len(mecc_dens) // 2], 3),
    'med_median_density': round(sorted(med_dens)[len(med_dens) // 2], 3),
    'U': U, 'z': z, 'p': p_mw,
    'alpha_bon': 0.05 / 6,
    'pass': p_mw is not None and p_mw < 0.05 / 6,
}
print(f"Cell 5 MW U={U:.1f} z={z:.3f} p={p_mw:.3e} (Meccan {len(mecc_dens)} "
      f"med {cell5['mecc_median_density']:.2f} vs Medinan {len(med_dens)} "
      f"med {cell5['med_median_density']:.2f})", file=sys.stderr)

# ============================================================
# Cell 6 — qul-density × Nöldeke 4-phase Kruskal-Wallis
# ============================================================
def kruskal_wallis(*groups):
    """Kruskal-Wallis H test across k groups (chi-square approx)."""
    all_vals = []
    for i, g in enumerate(groups):
        for v in g:
            all_vals.append((v, i))
    all_vals.sort(key=lambda r: r[0])
    N = len(all_vals)
    # ranks with tie-correction
    ranks = [0.0] * N
    i = 0
    while i < N:
        j = i
        while j + 1 < N and all_vals[j + 1][0] == all_vals[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    rank_sums = defaultdict(float)
    rank_ns = defaultdict(int)
    for r, (_, gi) in zip(ranks, all_vals):
        rank_sums[gi] += r
        rank_ns[gi] += 1
    H = 12.0 / (N * (N + 1)) * sum(
        (rank_sums[gi] ** 2) / rank_ns[gi] for gi in rank_sums
    ) - 3 * (N + 1)
    df = len(groups) - 1
    # p-value from chi-square upper tail
    # Use Wilson-Hilferty approximation for chi-square cdf
    p = chi2_sf(H, df)
    return (H, df, p)

def chi2_sf(x, k):
    """Survival function of chi-square (1 - cdf). Uses series for k <= 60."""
    if x <= 0:
        return 1.0
    # Use math.lgamma + incomplete gamma via series
    # Q(k/2, x/2) = upper incomplete gamma normalised.
    # For small k and moderate x use the recurrence:
    # Q(s, x) for integer s: e^{-x} * sum_{j=0}^{s-1} x^j / j!
    if k % 2 == 0:
        s = k // 2
        # Q(s, x/2) = e^{-x/2} * sum_{j=0}^{s-1} (x/2)^j / j!
        z = x / 2.0
        term = 1.0
        total = 1.0
        for j in range(1, s):
            term *= z / j
            total += term
        return math.exp(-z) * total
    else:
        # half-integer s: use series + erfc
        # Q(1/2, z) = erfc(sqrt(z))
        # recurrence: Q(s+1, z) = Q(s, z) + z^s e^{-z}/Γ(s+1)
        z = x / 2.0
        s = 0.5
        Q = math.erfc(math.sqrt(z))
        # bring s up to k/2
        target = k / 2.0
        while s + 1 <= target + 1e-9:
            # Q(s+1, z) = Q(s, z) + z^s e^{-z} / Γ(s+1)
            log_term = s * math.log(z) - z - math.lgamma(s + 1)
            Q += math.exp(log_term)
            s += 1.0
        return max(0.0, min(1.0, Q))

PHASES = ['Early Meccan', 'Middle Meccan', 'Late Meccan', 'Medinan']
phase_groups = {ph: [] for ph in PHASES}
for r in per_surah_table:
    if r['phase'] in phase_groups:
        phase_groups[r['phase']].append(r['qul_density_per_100'])

H, df, p_kw = kruskal_wallis(*[phase_groups[ph] for ph in PHASES])
phase_summary = []
for ph in PHASES:
    g = phase_groups[ph]
    if g:
        phase_summary.append({
            'phase': ph,
            'n': len(g),
            'mean_density': round(sum(g) / len(g), 3),
            'median_density': round(sorted(g)[len(g) // 2], 3),
        })
cell6 = {
    'H': H, 'df': df, 'p': p_kw,
    'alpha_bon': 0.05 / 6,
    'pass': p_kw is not None and p_kw < 0.05 / 6,
    'phase_summary': phase_summary,
}
print(f"Cell 6 KW H={H:.3f} df={df} p={p_kw:.3e}", file=sys.stderr)
for r in phase_summary:
    print(f"   {r['phase']}: n={r['n']} mean={r['mean_density']:.2f} "
          f"med={r['median_density']:.2f}", file=sys.stderr)

# ============================================================
# Bonus: addressee classification descriptive
# ============================================================
# Surahs containing qul split by Meccan/Medinan
mecc_with_qul = [r for r in per_surah_table
                 if r['period'] == 'Meccan' and r['qul_count'] > 0]
med_with_qul = [r for r in per_surah_table
                if r['period'] == 'Medinan' and r['qul_count'] > 0]
addressee_summary = {
    'meccan_surahs_with_qul': len(mecc_with_qul),
    'meccan_total': len([r for r in per_surah_table if r['period'] == 'Meccan']),
    'medinan_surahs_with_qul': len(med_with_qul),
    'medinan_total': len([r for r in per_surah_table if r['period'] == 'Medinan']),
    'mecc_total_qul': sum(r['qul_count'] for r in mecc_with_qul),
    'med_total_qul': sum(r['qul_count'] for r in med_with_qul),
}

# ============================================================
# Write JSON output
# ============================================================
OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
output = {
    'finding_id': 'h-new-74',
    'title': 'qul (قل) imperative — comprehensive distribution',
    'seed': SEED,
    'rules_tuple': '(no-tashkeel, hafs-kufan, canonical-114, Tanzil-JSON, '
                   'Leeds-QAC-v0.4 LEM:qaAla|IMPV|2MS)',
    'cell1_total_count': cell1,
    'cell2_per_surah_distribution': cell2,
    'cell3_surah_initial_qul': cell3,
    'cell4_formulaic_frames': cell4,
    'cell5_period_density_MWU': cell5,
    'cell6_phase_density_KW': cell6,
    'addressee_summary': addressee_summary,
    'per_surah_table': per_surah_table,
    'qul_with_frames': qul_with_frames,
}
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nWrote {OUT_JSON}", file=sys.stderr)
print(f"\n=== JOINT VERDICT ===", file=sys.stderr)
print(f"  Cell 1 (total = 332): {'PASS' if cell1['pass'] else 'FAIL'}", file=sys.stderr)
print(f"  Cell 2 (per-surah distribution): PUBLISHED", file=sys.stderr)
print(f"  Cell 3 (v1-w1 openers): {'PASS' if cell3['pass'] else 'FAIL'}", file=sys.stderr)
print(f"  Cell 4 (≥3 frames ≥5x): {'PASS' if cell4['pass'] else 'FAIL'}", file=sys.stderr)
print(f"  Cell 5 (period MW U): {'PASS' if cell5['pass'] else 'FAIL'} (p={cell5['p']:.3e})",
      file=sys.stderr)
print(f"  Cell 6 (phase KW H): {'PASS' if cell6['pass'] else 'FAIL'} (p={cell6['p']:.3e})",
      file=sys.stderr)
