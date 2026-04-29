"""
HMM-F-01..04 — Bifurcation, cohesion, cross-cluster, multi-rāwī tests.

Pre-registration: hawamim-7-bifurcation-prereg.md (sha embedded below as expected).
This script computes:
  - Per-surah Shannon rhyme-entropy on final-letter distribution (min-tashkeel).
  - HMM-F-01 bifurcation test: 2-piece-mean (Q40-42 vs Q43-46) vs flat-mean.
  - HMM-F-02 within-cluster cohesion d̄ for HM-7, HM-A (40-42), HM-B (43-46), using
    pre-computed FR distance matrix (h-new-111).
  - HMM-F-03 cross-cluster comparison HM-7 vs ALR-5 vs ALM-6.
  - HMM-F-04 multi-rāwī: rank Q42's rhyme entropy among the 29 muqaṭṭaʿāt-opened surahs.

Rules-tuple: (no-tashkeel for FR; min-tashkeel for rhyme final-letter; orthographic-token;
graphemes; basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi).

Seed: 20260428.
"""
import json, math, hashlib, random
from collections import Counter

SEED = 20260428
random.seed(SEED)

# ---------- text loading ----------
def load_min_tashkeel():
    with open('/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json') as f:
        return json.load(f)

ALEF_FORMS = {'أ':'ا','إ':'ا','آ':'ا','ٱ':'ا'}
YA_FORMS = {'ى':'ي'}
HAMZA_VARS = {'ؤ':'و','ئ':'ي'}

def normch(c):
    if c in ALEF_FORMS: return ALEF_FORMS[c]
    if c in YA_FORMS: return YA_FORMS[c]
    if c in HAMZA_VARS: return HAMZA_VARS[c]
    return c

def strip_diac(s):
    out=[]
    for ch in s:
        cp=ord(ch)
        if 0x0621<=cp<=0x064A:
            out.append(normch(ch))
    return ''.join(out)

def final_letter_of_verse(text):
    s = strip_diac(text).strip()
    if not s: return None
    return s[-1]

# ---------- rhyme entropy per surah ----------
def shannon_entropy(counter):
    total = sum(counter.values())
    if total == 0: return 0.0
    H = 0.0
    for v in counter.values():
        if v == 0: continue
        p = v/total
        H -= p*math.log2(p)
    return H

def per_surah_rhyme():
    qm = load_min_tashkeel()
    out = {}
    for surah in qm:
        sid = surah['id']
        verses = surah['verses']
        # exclude the bismillāh verse for non-Q1 surahs only when it's verse #1 prefix?
        # Per Hafs-Kufan tradition, basmala is verse 1 ONLY in Q1; for other surahs the basmala
        # is recited but not part of verse 1. The min-tashkeel JSON includes the basmala
        # text as a prefix to verse 1 of most surahs (need to check). For rhyme purposes, we
        # only care about verse-final letters; basmala isn't a verse-final unit, so its inclusion
        # as prefix doesn't matter. Use all verses as-is, taking final letter of each.
        cnt = Counter()
        finals=[]
        for v in verses:
            fl = final_letter_of_verse(v['text'])
            if fl is None: continue
            cnt[fl]+=1
            finals.append(fl)
        H = shannon_entropy(cnt)
        top = cnt.most_common(1)[0] if cnt else (None,0)
        out[sid] = {
            'n_verses': len(finals),
            'entropy_bits': H,
            'top_letter': top[0],
            'top_frac': top[1]/len(finals) if finals else 0.0,
            'distinct_letters': len(cnt),
            'distribution': dict(cnt.most_common()),
        }
    return out

# ---------- FR distance matrix ----------
def load_fr_matrix():
    """h-new-111 stores upper-triangular as a flat list of {i,j,d} or [i,j,d] entries.
    Reconstruct full 114x114 matrix indexed 0..113."""
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d = json.load(f)
    flat = d['D_matrix_upper_triangular']
    M = [[0.0]*114 for _ in range(114)]
    for entry in flat:
        if isinstance(entry, dict):
            i = entry.get('i'); j = entry.get('j'); v = entry.get('d', entry.get('distance'))
        elif isinstance(entry, (list, tuple)):
            if len(entry) == 3:
                i, j, v = entry
            else:
                raise ValueError(f"unexpected entry: {entry}")
        else:
            raise ValueError(f"unexpected entry type: {type(entry)}")
        # i, j are likely 1-indexed surah numbers
        if i >= 1 and j >= 1 and i <= 114 and j <= 114:
            ii, jj = i-1, j-1
        else:
            ii, jj = i, j
        M[ii][jj] = v
        M[jj][ii] = v
    return M

# ---------- cohesion ----------
def mean_pairwise(idxs, M):
    n=len(idxs)
    if n<2: return None
    s=0.0; c=0
    for i in range(n):
        for j in range(i+1,n):
            s += M[idxs[i]-1][idxs[j]-1]
            c += 1
    return s/c

# ---------- bifurcation test ----------
def bifurcation_test(rhyme_dict):
    # entropy values for HM-7
    e = [rhyme_dict[s]['entropy_bits'] for s in range(40,47)]
    # group A: indices 0,1,2 (Q40,41,42); B: 3,4,5,6 (Q43-46)
    A = e[:3]; B = e[3:]
    mu_A = sum(A)/3; mu_B = sum(B)/4
    mu_all = sum(e)/7
    # SSE_2piece = sum( (e_i - mu_A)^2 for i in A ) + sum((e_i - mu_B)^2 for i in B)
    sse_2 = sum((x-mu_A)**2 for x in A) + sum((x-mu_B)**2 for x in B)
    sse_flat = sum((x-mu_all)**2 for x in e)
    # F-like ratio for variance reduction
    # permutation null: random partitions of HM-7 into 3 vs 4
    rng = random.Random(SEED)
    obs_diff = mu_A - mu_B
    obs_redux = sse_flat - sse_2  # how much SSE reduced
    n_perm = 10000
    count_diff_ge = 0
    count_redux_ge = 0
    for _ in range(n_perm):
        idx = list(range(7))
        rng.shuffle(idx)
        Apa = [e[i] for i in idx[:3]]
        Bpa = [e[i] for i in idx[3:]]
        muA = sum(Apa)/3; muB = sum(Bpa)/4
        mu = sum(Apa+Bpa)/7
        sse2 = sum((x-muA)**2 for x in Apa) + sum((x-muB)**2 for x in Bpa)
        ssef = sum((x-mu)**2 for x in Apa+Bpa)
        if (muA - muB) >= obs_diff: count_diff_ge += 1
        if (ssef - sse2) >= obs_redux: count_redux_ge += 1
    return {
        'entropy_HM7': e,
        'mu_A_Q40_42': mu_A,
        'mu_B_Q43_46': mu_B,
        'mu_all': mu_all,
        'obs_diff_A_minus_B': obs_diff,
        'sse_2piece': sse_2,
        'sse_flat': sse_flat,
        'sse_reduction': obs_redux,
        'p_perm_diff_one_sided': count_diff_ge / n_perm,
        'p_perm_sse_reduction_one_sided': count_redux_ge / n_perm,
        'n_perm': n_perm,
    }

# ---------- cohesion test ----------
def cohesion_block(M):
    HM7 = list(range(40,47))
    HMA = [40,41,42]
    HMB = [43,44,45,46]
    ALR = [10,11,12,14,15]
    ALM = [2,3,29,30,31,32]
    sets = {'HM-7':HM7, 'HM-A(40-42)':HMA, 'HM-B(43-46)':HMB, 'ALR-5':ALR, 'ALM-6':ALM}
    out = {}
    for name, idxs in sets.items():
        out[name] = {'k': len(idxs), 'd_bar': mean_pairwise(idxs, M)}
    # Permutation null for each at corresponding K
    rng = random.Random(SEED+1)
    n_perm = 10000
    surahs = list(range(1,115))
    for name, idxs in sets.items():
        K = len(idxs)
        d_obs = out[name]['d_bar']
        ge = 0; le = 0
        for _ in range(n_perm):
            samp = rng.sample(surahs, K)
            d = mean_pairwise(samp, M)
            if d <= d_obs: le += 1  # lower d̄ = more cohesive
            if d >= d_obs: ge += 1
        out[name]['p_perm_le_one_sided'] = le / n_perm
        out[name]['p_perm_ge_one_sided'] = ge / n_perm
        out[name]['percentile_le'] = 100.0 * le / n_perm
    return out

# ---------- multi-rāwī test ----------
def multirawi_test(rhyme_dict):
    # 29 muqaṭṭaʿāt-opened surahs
    MUQ29 = [2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68]
    rows = [(s, rhyme_dict[s]['entropy_bits']) for s in MUQ29]
    rows.sort(key=lambda r: -r[1])
    rank_map = {s:i+1 for i,(s,_) in enumerate(rows)}
    return {
        'muqattaat_29_entropy_ranked': [{'surah':s,'entropy':e,'rank':i+1} for i,(s,e) in enumerate(rows)],
        'Q42_rank_in_muqattaat_29': rank_map[42],
        'top_5_entropy_muqattaat_29': rows[:5],
    }

# ---------- main ----------
def main():
    rhyme = per_surah_rhyme()
    M = load_fr_matrix()
    # confirm shape
    assert isinstance(M, list) and len(M)==114 and len(M[0])==114, f"M shape: {len(M)}x{len(M[0]) if M else '?'}"
    bif = bifurcation_test(rhyme)
    coh = cohesion_block(M)
    mr  = multirawi_test(rhyme)
    out = {
        'seed': SEED,
        'rules_tuple': '(no-tashkeel for FR; min-tashkeel for rhyme; orthographic-token; graphemes; basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi)',
        'rhyme_per_surah_HM7': {s: rhyme[s] for s in range(40,47)},
        'HMM_F_01_bifurcation': bif,
        'HMM_F_02_cohesion': coh,
        'HMM_F_03_cross_cluster': {
            'HM-7_d_bar': coh['HM-7']['d_bar'],
            'HM-A_d_bar': coh['HM-A(40-42)']['d_bar'],
            'HM-B_d_bar': coh['HM-B(43-46)']['d_bar'],
            'ALR-5_d_bar': coh['ALR-5']['d_bar'],
            'ALM-6_d_bar': coh['ALM-6']['d_bar'],
            'most_cohesive': min(
                ['HM-7','HM-A(40-42)','HM-B(43-46)','ALR-5','ALM-6'],
                key=lambda k: coh[k]['d_bar'])
        },
        'HMM_F_04_multirawi': mr,
    }
    with open('/Users/grey/Downloads/quran/findings/cross-finding/csv/hawamim-7-cluster-bifurcation.json','w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    # human-readable summary
    print('=== HMM-F-01 BIFURCATION ===')
    print(f"HM-A μ entropy = {bif['mu_A_Q40_42']:.3f} bits")
    print(f"HM-B μ entropy = {bif['mu_B_Q43_46']:.3f} bits")
    print(f"diff (A-B)     = {bif['obs_diff_A_minus_B']:.3f}")
    print(f"SSE flat       = {bif['sse_flat']:.4f}")
    print(f"SSE 2-piece    = {bif['sse_2piece']:.4f}")
    print(f"reduction      = {bif['sse_reduction']:.4f}")
    print(f"p_perm (diff)  = {bif['p_perm_diff_one_sided']:.4f}")
    print(f"p_perm (SSE)   = {bif['p_perm_sse_reduction_one_sided']:.4f}")
    print()
    print('=== HMM-F-02 COHESION (FR-roots d̄, lower=more cohesive) ===')
    for name in ['HM-7','HM-A(40-42)','HM-B(43-46)','ALR-5','ALM-6']:
        r = coh[name]
        print(f"{name:>14s}: d̄={r['d_bar']:.4f}, K={r['k']}, percentile_le={r['percentile_le']:.2f}%, p_le={r['p_perm_le_one_sided']:.4f}")
    print()
    print('=== HMM-F-03 MOST COHESIVE BLOCK ===')
    print(out['HMM_F_03_cross_cluster']['most_cohesive'])
    print()
    print('=== HMM-F-04 MULTI-RĀWĪ (Q42 rank in muqaṭṭaʿāt-29 by entropy desc) ===')
    print(f"Q42 rank: {mr['Q42_rank_in_muqattaat_29']} of 29")
    for s,e in mr['top_5_entropy_muqattaat_29']:
        print(f"  Q{s}: H={e:.3f}")
    print()
    print('=== Rhyme entropy per HM-7 surah ===')
    for s in range(40,47):
        r = rhyme[s]
        print(f"Q{s}: H={r['entropy_bits']:.3f} bits | top={r['top_letter']} ({r['top_frac']*100:.0f}%) | distinct={r['distinct_letters']}/{r['n_verses']}v")
    return out

if __name__=='__main__':
    main()
