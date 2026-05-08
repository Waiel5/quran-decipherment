#!/usr/bin/env python3
"""Q016-F-03 — True-isolate persistence of Q 16 across 8 similarity instruments.

Pre-reg: surahs/Q016-al-nahl/Q016-F-03-true-isolate-persistence-prereg.md
SHA256: 7214978abe65a97e6417b7392fda9334a150c43a40bb411a0496721f98272135
Design parent: Q025-F-01 (same 8-instrument battery)
Rules-tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, hashlib, sys, os, random, re, math
from collections import defaultdict, Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q016-al-nahl/Q016-F-03-true-isolate-persistence-prereg.md'
EXPECTED_SHA = '7214978abe65a97e6417b7392fda9334a150c43a40bb411a0496721f98272135'
SEED = 20260507
N_PERM = 10000
TARGET = 16
ALPHA_BON = 0.05 / 8

QAC_PATH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_NO_TASHKEEL = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
QURAN_MIN_TASHKEEL = '/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json'
H_NEW_111 = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
ASMA = '/Users/grey/Downloads/quran/data/asma-al-husna.txt'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def parse_qac_per_surah_roots():
    """Returns dict surah -> list of root-tokens (for set or count usage)."""
    by_surah = defaultdict(list)
    pat = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)\t(\S+)\t(\S+)\t(.+)$')
    with open(QAC_PATH) as f:
        for line in f:
            m = pat.match(line)
            if not m: continue
            s = int(m.group(1))
            feats = m.group(7)
            r = re.search(r'ROOT:([^\|]+)', feats)
            if r:
                by_surah[s].append(r.group(1))
    return by_surah


def load_text():
    with open(QURAN_NO_TASHKEEL) as f:
        d = json.load(f)
    return {s['id']: ' '.join(v['text'] for v in s['verses']) for s in d}


def load_text_min():
    with open(QURAN_MIN_TASHKEEL) as f:
        d = json.load(f)
    return {s['id']: s['verses'] for s in d}


# ===== Instruments =====

def instr_root_jaccard(roots_per_surah):
    sets = {s: set(rs) for s, rs in roots_per_surah.items()}
    sims = {(i,j): 0.0 for i in range(1,115) for j in range(1,115)}
    surahs = sorted(sets)
    for i in surahs:
        for j in surahs:
            if i==j: continue
            a, b = sets[i], sets[j]
            sims[(i,j)] = len(a&b) / max(1, len(a|b))
    return sims


def instr_content_cosine(text_per_surah):
    # TF per surah
    docs = {s: text_per_surah[s].split() for s in text_per_surah}
    df = Counter()
    for s, toks in docs.items():
        for t in set(toks):
            df[t] += 1
    N = len(docs)
    idf = {t: math.log((N+1)/(c+1))+1 for t, c in df.items()}
    vecs = {}
    for s, toks in docs.items():
        c = Counter(toks)
        v = {t: c[t] * idf.get(t, 0) for t in c}
        norm = math.sqrt(sum(x*x for x in v.values()))
        vecs[s] = (v, norm)
    sims = {}
    surahs = sorted(docs)
    for i in surahs:
        vi, ni = vecs[i]
        for j in surahs:
            if i==j: continue
            vj, nj = vecs[j]
            if ni == 0 or nj == 0:
                sims[(i,j)] = 0
                continue
            # iterate smaller
            if len(vi) < len(vj):
                small, big = vi, vj
            else:
                small, big = vj, vi
            dot = sum(small[t] * big.get(t, 0) for t in small)
            sims[(i,j)] = dot / (ni*nj)
    return sims


def char_ngrams(text, n):
    text = text.replace(' ', '')  # collapse whitespace
    return set(text[i:i+n] for i in range(len(text)-n+1))


def instr_char_ngram_dice(text_per_surah, n=3):
    grams = {s: char_ngrams(text_per_surah[s], n) for s in text_per_surah}
    sims = {}
    for i in grams:
        gi = grams[i]
        for j in grams:
            if i==j: continue
            gj = grams[j]
            denom = len(gi) + len(gj)
            sims[(i,j)] = (2*len(gi & gj))/denom if denom else 0
    return sims


def instr_fr_distance():
    with open(H_NEW_111) as f:
        fr = json.load(f)
    mat = fr['D_matrix_upper_triangular']
    sims = {}
    for entry in mat:
        i, j, d = entry
        sims[(i,j)] = 1.0 / (1.0 + d)
        sims[(j,i)] = 1.0 / (1.0 + d)
    # Set i==j to 1.0 (self-sim) — but we exclude self in mean_top3
    return sims


def instr_rhyme_final_letter_cosine(min_text_per_surah):
    """Per-surah final-letter probability vector cosine."""
    surahs = sorted(min_text_per_surah)
    diac = re.compile(r'[ً-ْٰۭۖۗۘۙۚۛۜ۞\s]+')
    profiles = {}
    for s in surahs:
        finals = []
        for v in min_text_per_surah[s]:
            t = diac.sub('', v['text'])
            if t:
                finals.append(t[-1])
        c = Counter(finals)
        total = sum(c.values())
        profiles[s] = {k: v/total for k, v in c.items()}
    sims = {}
    for i in surahs:
        pi = profiles[i]
        ni = math.sqrt(sum(v*v for v in pi.values()))
        for j in surahs:
            if i==j: continue
            pj = profiles[j]
            nj = math.sqrt(sum(v*v for v in pj.values()))
            keys = set(pi)|set(pj)
            dot = sum(pi.get(k,0)*pj.get(k,0) for k in keys)
            sims[(i,j)] = dot/(ni*nj) if ni and nj else 0
    return sims


def instr_root_zipf(roots_per_surah):
    """Weight shared roots by 1/log(1+corpus_freq); rare roots count more."""
    corpus_freq = Counter()
    for s, rs in roots_per_surah.items():
        corpus_freq.update(set(rs))
    weights = {r: 1.0 / math.log(1 + f + 1) for r, f in corpus_freq.items()}
    sets = {s: set(rs) for s, rs in roots_per_surah.items()}
    sims = {}
    for i in sets:
        ai = sets[i]
        wi = sum(weights.get(r, 0) for r in ai)
        for j in sets:
            if i==j: continue
            aj = sets[j]
            wj = sum(weights.get(r, 0) for r in aj)
            shared = ai & aj
            ws = sum(weights.get(r, 0) for r in shared)
            denom = wi + wj - ws
            sims[(i,j)] = ws/denom if denom else 0
    return sims


def instr_divine_name(text_per_surah):
    with open(ASMA) as f:
        names = [line.strip() for line in f if line.strip()]
    # Strip articles for matching
    names_norm = list(set(n.replace('ال', '') for n in names if n))
    # Use original names too
    pats = [re.compile(r'\b' + re.escape(n) + r'\b') for n in names if len(n) > 1]
    name_sets = {}
    for s, text in text_per_surah.items():
        present = set()
        for i, p in enumerate(pats):
            if p.search(text):
                present.add(i)
        name_sets[s] = present
    sims = {}
    for i in name_sets:
        for j in name_sets:
            if i==j: continue
            a, b = name_sets[i], name_sets[j]
            denom = len(a|b)
            sims[(i,j)] = len(a&b)/denom if denom else 0
    return sims


def mean_top3_sim(sims, surah):
    """Mean similarity of `surah` to its 3 most-similar non-self surahs."""
    others = [(j, sims.get((surah, j), 0)) for j in range(1, 115) if j != surah]
    others.sort(key=lambda x: -x[1])
    top3 = others[:3]
    return sum(s for _, s in top3) / 3, [j for j, _ in top3]


def rank_lower(values_dict, target):
    """Rank with LOWER values better (more isolated)."""
    sorted_pairs = sorted(values_dict.items(), key=lambda x: x[1])
    for i, (s, _) in enumerate(sorted_pairs, 1):
        if s == target:
            return i
    return None


def perm_test_lower(values_dict, target, n_perm, seed):
    """Permute the surah identity labels n_perm times; for each perm, the target's value is now a random surah's value. Empirical p = fraction with rank ≤ observed rank."""
    obs_rank = rank_lower(values_dict, target)
    surahs_sorted_by_rank = sorted(values_dict.items(), key=lambda x: x[1])
    rng = random.Random(seed)
    n_le = 0
    for _ in range(n_perm):
        # random label assignment: pick a random surah's value, see its rank
        random_surah = rng.choice(list(values_dict.keys()))
        random_rank = next(i for i, (s, _) in enumerate(surahs_sorted_by_rank, 1) if s == random_surah)
        if random_rank <= obs_rank:
            n_le += 1
    return obs_rank, (n_le + 1) / (n_perm + 1)


def main():
    verify_sha()
    print(f'Loading data...')
    roots_per_surah = parse_qac_per_surah_roots()
    text_per_surah = load_text()
    min_text_per_surah = load_text_min()

    instruments = [
        ('I1_root_jaccard', lambda: instr_root_jaccard(roots_per_surah)),
        ('I2_content_cosine', lambda: instr_content_cosine(text_per_surah)),
        ('I3_char_trigram_dice', lambda: instr_char_ngram_dice(text_per_surah, n=3)),
        ('I4_fr_similarity', lambda: instr_fr_distance()),
        ('I5_rhyme_final_letter_cosine', lambda: instr_rhyme_final_letter_cosine(min_text_per_surah)),
        ('I6_root_zipf_overlap', lambda: instr_root_zipf(roots_per_surah)),
        ('I7_divine_name_jaccard', lambda: instr_divine_name(text_per_surah)),
        ('I8_char_5gram_dice', lambda: instr_char_ngram_dice(text_per_surah, n=5)),
    ]

    results = []
    for name, fn in instruments:
        print(f'  computing {name}...')
        sims = fn()
        # mean_top3 per surah
        mt3 = {}
        top3_for_target = None
        for s in range(1, 115):
            mt, neighbors = mean_top3_sim(sims, s)
            mt3[s] = mt
            if s == TARGET:
                top3_for_target = neighbors
        obs_rank, p = perm_test_lower(mt3, TARGET, N_PERM, SEED + hash(name) % 1000)
        bottom_quartile = obs_rank <= 28
        passes_bon = p <= ALPHA_BON

        # MW-5 positive control: hawamim cluster {40,41,42,43,44} mean rank — should NOT be in bottom-quartile for I1, I2
        hawamim_ranks = [rank_lower(mt3, h) for h in [40,41,42,43,44]]
        ham_mean_rank = sum(hawamim_ranks) / len(hawamim_ranks)
        ham_in_bq = sum(1 for r in hawamim_ranks if r <= 28)
        mw5_pass = (ham_in_bq <= 2) if name in ('I1_root_jaccard', 'I2_content_cosine') else None

        results.append({
            'instrument': name,
            'q16_mean_top3_sim': mt3[TARGET],
            'q16_top3_neighbors': top3_for_target,
            'q16_rank': obs_rank,
            'q16_in_bottom_quartile': bottom_quartile,
            'p_perm_one_sided_lower': p,
            'passes_bonferroni': passes_bon,
            'mw5_hawamim_in_bq_count': ham_in_bq,
            'mw5_hawamim_ranks': hawamim_ranks,
            'mw5_pass': mw5_pass,
        })

    n_in_bq = sum(1 for r in results if r['q16_in_bottom_quartile'])
    n_pass_bon = sum(1 for r in results if r['q16_in_bottom_quartile'] and r['passes_bonferroni'])

    if n_in_bq >= 6 and n_pass_bon >= 6:
        verdict = 'CONFIRMED'
    elif n_in_bq >= 4:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'
    # Pre-commit violation check: q16 in TOP-quartile (rank ≥ 87) on majority
    n_in_tq = sum(1 for r in results if r['q16_rank'] >= 87)
    if n_in_tq >= 5:
        verdict = 'PRE_COMMIT_VIOLATION'

    out = {
        'finding_id': 'Q016-F-03',
        'design_parent': 'Q025-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': 8,
        'alpha_bon': ALPHA_BON,
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'target_surah': TARGET,
        'instruments': results,
        'n_in_bottom_quartile': n_in_bq,
        'n_pass_bonferroni': n_pass_bon,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q016-al-nahl/csv/Q016-F-03.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    for r in results:
        print(f"  {r['instrument']}: rank={r['q16_rank']}/114, p={r['p_perm_one_sided_lower']:.4f}, BQ={r['q16_in_bottom_quartile']}, top3={r['q16_top3_neighbors']}")
    print(f"\nQ16 in bottom-quartile on {n_in_bq}/8 instruments")
    print(f"Q16 passes Bonferroni on {n_pass_bon}/8 instruments")
    print(f"VERDICT: {verdict}")


if __name__ == '__main__':
    main()
