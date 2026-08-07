#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2740 — Is the rasm/imla' divergence set non-randomly distributed?

Runner for the pre-registration at
    findings/phase-b-hypotheses/prereg-h-new-2740-rasm-divergence.md

Every decision rule implemented below is a transcription of that file's sections 4-6.
The pre-registration SHA and every frozen-input SHA are verified at runtime and the
script exits non-zero on any mismatch.

Author: Waiel Al-Shujaa    Date: 2026-08-07
Protocol 7.1 note: stdlib only. No numpy, no third-party dependency.
"""
import collections
import datetime
import hashlib
import json
import os
import random
import re
import sys
import time

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))

PREREG = 'findings/phase-b-hypotheses/prereg-h-new-2740-rasm-divergence.md'
PREREG_SHA = '6eee19757e437067679e7286c4d3823ef17589dacdf0ff84c22bd5c27cbb2db7'

FROZEN = {
    'data/alt-text/quran-uthmani-txt.txt':
        'e5e7e54988877d6164832d55435135a563b9cfc249e0c8efd73e9e7f23231db8',
    'data/alt-text/quran-simple-txt.txt':
        '777c190d8e4ab081a80b4f10f5e309f1ab2a87e4d3ea97e5a7eabc59f4fe0b72',
    'data/hafs-verse-counts.tsv':
        'e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba',
    'findings/phase-b-hypotheses/csv/h-new-2500.json':
        'a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25',
    'findings/phase-b-hypotheses/csv/h-new-2530.json':
        '5ca17050c20b15734ad9a734e7bad7b938b616c924ec53dfcd24814a1473b68c',
    'data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt':
        'a067ebb34ccabe92376f3008b9cdfb32eea9d6167062172318635e53f500fb05',
}

SEED_PRIMARY = 20260509
SEED_REPLICATION = 20260519
N_PERM = 10000
BONFERRONI_K = 5
ALPHA = 0.05 / BONFERRONI_K          # 0.01, prereg section 6


# ----------------------------------------------------------------- SHA gate
def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def gate():
    got = sha256(os.path.join(REPO, PREREG))
    if got != PREREG_SHA:
        raise SystemExit(f'PRE-REG SHA MISMATCH\n  expected {PREREG_SHA}\n  got      {got}')
    for rel, want in FROZEN.items():
        got = sha256(os.path.join(REPO, rel))
        if got != want:
            raise SystemExit(f'FROZEN INPUT SHA MISMATCH: {rel}\n  expected {want}\n  got      {got}')
    print(f'SHA gate passed: pre-registration + {len(FROZEN)} frozen inputs.')


# ----------------------------------------------------------- instrument 4.2
PAUSE_MARKS = ''.join(chr(c) for c in range(0x06D6, 0x06EE))
HARAKAT = ''.join(chr(c) for c in range(0x064B, 0x0653))
OTHER_MARKS = ''.join(chr(c) for c in list(range(0x0653, 0x0660)) + [0x0670, 0x0640])
ALL_MARKS_RE = re.compile('[' + re.escape(PAUSE_MARKS + HARAKAT + OTHER_MARKS) + ']')
PAUSE_RE = re.compile('[' + re.escape(PAUSE_MARKS) + ']')
IRAB_RE = re.compile('[ٌٍَُِ]$')   # tanwin-damm/kasr, fatha, damma, kasra

N4_MAP = str.maketrans({'أ': 'ا', 'إ': 'ا',        # a -> alif
                        'ؤ': 'و', 'ئ': 'ي',        # w-hamza -> waw, y-hamza -> yaa
                        'ء': ''})                                  # bare hamza dropped


def base_letters(word):
    """4.2 - strip every diacritic and annotation sign; keep base letters."""
    return ALL_MARKS_RE.sub('', word).replace(' ', '')


def skel(word, n1=True, n2=True, n3=True, n4=True):
    """4.2 + 4.3 - base letters then the requested convention normalisations."""
    w = base_letters(word)
    if n1:
        w = w.replace('ٱ', 'ا')          # alef wasla -> alef
    if n2:
        w = w.replace('ى', 'ي')          # alef maksura -> yaa (dotting convention)
    if n3:
        w = w.replace('آ', 'ا')          # alef+madda -> alef
    if n4:
        w = w.translate(N4_MAP)
    return w


def pausal_key(word):
    """6-I2 - fully-vowelled simple token, pause signs removed, final i'rab vowel
    or tanwin-damm/kasr removed. Tanwin-fath is deliberately NOT removed."""
    return IRAB_RE.sub('', PAUSE_RE.sub('', word).replace(' ', ''))


def levenshtein(a, b):
    m, n = len(a), len(b)
    row = list(range(n + 1))
    for i in range(1, m + 1):
        prev, row[0] = row[0], i
        for j in range(1, n + 1):
            cur = row[j]
            row[j] = min(row[j] + 1, row[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return row[n]


def align_verse(u_line, s_line):
    """4.1 - deterministic greedy merge of surplus simple tokens."""
    a, b = u_line.split(), s_line.split()
    if len(a) == len(b):
        return [(x, y, False) for x, y in zip(a, b)]
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        deficit = (len(b) - j) - (len(a) - i)
        best_cost, best_m = levenshtein(skel(a[i]), skel(b[j])), 1
        for m in range(2, min(deficit, 4) + 2):
            if j + m > len(b):
                break
            cost = levenshtein(skel(a[i]), skel(''.join(b[j:j + m])))
            if cost < best_cost:
                best_cost, best_m = cost, m
        out.append((a[i], ' '.join(b[j:j + best_m]), best_m > 1))
        i += 1
        j += best_m
    if i != len(a) or j != len(b):
        return None
    return out


def read_text(rel):
    return [l.rstrip('\n') for l in open(os.path.join(REPO, rel), encoding='utf-8')
            if l.strip() and not l.lstrip().startswith('#')]


# ------------------------------------------------------------- typology 5
def classify(u_sk, s_sk):
    """5 - edit-operation class, mapped onto al-Suyuti's scheme."""
    import difflib
    ops = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, u_sk, s_sk).get_opcodes():
        if tag == 'equal':
            continue
        ops.append((tag, u_sk[i1:i2], s_sk[j1:j2]))
    classes = set()
    for tag, us, ss in ops:
        if tag == 'insert':                       # simple has letters the rasm lacks
            for ch in set(ss):
                classes.add({'ا': 'HADHF-ALIF', 'ي': 'HADHF-YA',
                             'و': 'HADHF-WAW', 'ل': 'HADHF-LAM'}.get(ch, 'HADHF-OTHER'))
        elif tag == 'delete':                     # rasm has letters the simple text lacks
            for ch in set(us):
                classes.add({'ا': 'ZIYADA-ALIF', 'و': 'ZIYADA-WAW',
                             'ي': 'ZIYADA-YA'}.get(ch, 'ZIYADA-OTHER'))
        else:
            pair = (us, ss)
            if pair in (('و', 'ا'), ('ا', 'و')):
                classes.add('BADAL-WAW-ALIF')
            elif pair in (('ي', 'ا'), ('ا', 'ي')):
                classes.add('BADAL-YA-ALIF')
            else:
                classes.add('BADAL-OTHER')
    if not classes:
        return 'NONE'
    if len(classes) == 1:
        return classes.pop()
    return 'MIXED'


# ------------------------------------------------------------- permutation
def perm_p(observed, nulls, greater=True):
    if greater:
        hits = sum(1 for v in nulls if v >= observed)
    else:
        hits = sum(1 for v in nulls if v <= observed)
    return (1 + hits) / (1 + len(nulls))


def main(seed, outdir):
    t0 = time.time()
    gate()
    rng = random.Random(seed)
    res = {'id': 'H-NEW-2740', 'seed': seed, 'n_perm': N_PERM,
           'bonferroni_k': BONFERRONI_K, 'alpha_bonferroni': ALPHA,
           'prereg_sha256': PREREG_SHA}

    U = read_text('data/alt-text/quran-uthmani-txt.txt')
    S = read_text('data/alt-text/quran-simple-txt.txt')
    if len(U) != 6236 or len(S) != 6236:
        raise SystemExit(f'verse-count assertion failed: {len(U)} / {len(S)}')

    counts = [(int(l.split()[0]), int(l.split()[1]))
              for l in open(os.path.join(REPO, 'data/hafs-verse-counts.tsv')) if l.split()]
    if sum(n for _, n in counts) != 6236 or len(counts) != 114:
        raise SystemExit('hafs verse-count assertion failed')
    n_ayat = dict(counts)
    index = [(s, a) for s, n in counts for a in range(1, n + 1)]

    # register labels -------------------------------------------------- 3
    gp = json.load(open(os.path.join(REPO, 'findings/phase-b-hypotheses/csv/h-new-2500.json'),
                        encoding='utf-8'))['genre_proxy']['surah_genre']
    want = json.load(open(os.path.join(REPO, 'findings/phase-b-hypotheses/csv/h-new-2530.json'),
                          encoding='utf-8'))['n_per_genre']
    got = dict(collections.Counter(gp.values()))
    if got != want:
        raise SystemExit(f'register marginal assertion failed: {got} != {want}')
    print(f'Register labels verified against h-new-2530 n_per_genre: {want}')
    res['register_marginals'] = want

    # alignment -------------------------------------------------------- 4.1
    toks, fails = [], []
    for k, (u, s) in enumerate(zip(U, S)):
        al = align_verse(u, s)
        if al is None:
            fails.append(index[k])
            continue
        n = len(al)
        for wi, (uw, sw, merged) in enumerate(al):
            toks.append({'surah': index[k][0], 'ayah': index[k][1], 'wi': wi, 'nw': n,
                         'fasl': merged, 'u_raw': uw, 's_raw': sw})
    res['alignment'] = {'verses_aligned': 6236 - len(fails), 'verses_failed': len(fails),
                        'failed_list': fails, 'tokens': len(toks),
                        'fasl_merges': sum(t['fasl'] for t in toks)}
    if fails:
        raise SystemExit(f'ALIGNMENT COVERAGE FAILED (prereg 4.1 locked 6236/6236): {fails}')
    print(f"Aligned 6236/6236 verses -> {len(toks)} token pairs "
          f"({res['alignment']['fasl_merges']} FASL merges).")

    # exceptionlessness of the convention layers ----------------------- 4.3
    u_base = [base_letters(t['u_raw']) for t in toks]
    s_base = [base_letters(t['s_raw']) for t in toks]
    exc = {
        'N1_wasla_in_simple': sum(w.count('ٱ') for w in s_base),
        'N2_word_final_dotted_yaa_in_uthmani': sum(
            1 for w in u_base for part in w.split() if part.endswith('ي')),
        'N3_madda_in_uthmani': sum(w.count('آ') for w in u_base),
    }
    exc['N1_SYSTEMATIC'] = exc['N1_wasla_in_simple'] == 0
    exc['N2_SYSTEMATIC'] = exc['N2_word_final_dotted_yaa_in_uthmani'] == 0
    exc['N3_SYSTEMATIC'] = exc['N3_madda_in_uthmani'] == 0
    res['exceptionlessness'] = exc
    print('Exceptionlessness:', {k: v for k, v in exc.items() if k.endswith('SYSTEMATIC')})

    # layer accounting -------------------------------------------------- 4.4
    layers, prev = [], None
    for name, kw in [('marks-only', dict(n1=0, n2=0, n3=0, n4=0)),
                     ('+N1 wasla', dict(n1=1, n2=0, n3=0, n4=0)),
                     ('+N2 yaa-dotting', dict(n1=1, n2=1, n3=0, n4=0)),
                     ('+N3 madda', dict(n1=1, n2=1, n3=1, n4=0)),
                     ('+N4 hamza', dict(n1=1, n2=1, n3=1, n4=1))]:
        d = sum(1 for t in toks if skel(t['u_raw'], **kw) != skel(t['s_raw'], **kw))
        layers.append({'layer': name, 'divergent_tokens': d,
                       'removed_by_this_layer': (prev - d) if prev is not None else None})
        prev = d
    res['layer_accounting'] = layers
    for L in layers:
        print(f"  {L['layer']:20s} divergent={L['divergent_tokens']:>6}"
              f"{'  removed ' + str(L['removed_by_this_layer']) if L['removed_by_this_layer'] else ''}")

    for t in toks:
        t['uk'] = skel(t['u_raw'])
        t['sk'] = skel(t['s_raw'])
        t['div'] = t['uk'] != t['sk']
        t['k2'] = pausal_key(t['s_raw'])

    div_toks = [t for t in toks if t['div']]
    res['divergence_set'] = {
        'total_tokens': len(toks),
        'residual_divergent_tokens': len(div_toks),
        'rate': len(div_toks) / len(toks),
        'systematic_tokens_removed': layers[0]['divergent_tokens'] - len(div_toks),
        'naive_diff_tokens': layers[0]['divergent_tokens'],
    }

    # typology counts ---------------------------------------------------- 5
    tycount, tytypes = collections.Counter(), collections.defaultdict(set)
    for t in div_toks:
        c = 'FASL' if t['fasl'] else classify(t['uk'], t['sk'])
        t['cls'] = c
        tycount[c] += 1
        tytypes[c].add((t['uk'], t['sk']))
    res['typology'] = {c: {'tokens': n, 'distinct_type_pairs': len(tytypes[c])}
                       for c, n in tycount.most_common()}
    res['typology_examples'] = {
        c: [f'{a} | {b}' for a, b in sorted(tytypes[c], key=lambda p: -sum(
            1 for t in div_toks if t['uk'] == p[0] and t['sk'] == p[1]))[:8]]
        for c in tycount}
    print('Typology:', {c: n for c, n in tycount.most_common()})

    # hamza (N4) quarantine size
    res['typology']['HAMZ_quarantined_by_N4'] = {
        'tokens': layers[3]['divergent_tokens'] - layers[4]['divergent_tokens'],
        'distinct_type_pairs': None}

    # ---------------------------------------------- lexical determinism (5/6)
    by_type = collections.defaultdict(list)
    for t in toks:
        by_type[t['sk']].append(t)
    all_div, none_div, mixed = [], [], []
    for k, v in by_type.items():
        flags = set(x['div'] for x in v)
        (all_div if flags == {True} else none_div if flags == {False} else mixed).append((k, v))
    div_in_mixed = sum(1 for k, v in mixed for x in v if x['div'])
    res['lexical_determinism'] = {
        'skeleton_types_total': len(by_type),
        'types_all_divergent': len(all_div),
        'types_none_divergent': len(none_div),
        'types_mixed': len(mixed),
        'divergent_tokens_in_invariant_types': len(div_toks) - div_in_mixed,
        'divergent_tokens_in_mixed_types': div_in_mixed,
        'fraction_divergence_lexically_determined':
            (len(div_toks) - div_in_mixed) / len(div_toks),
    }
    # prereg 6 verdict label: LEXICALLY-DETERMINED iff >= 0.90
    res['lexical_determinism']['verdict'] = (
        'LEXICALLY-DETERMINED'
        if res['lexical_determinism']['fraction_divergence_lexically_determined'] >= 0.90
        else 'NOT-LEXICALLY-DETERMINED')
    print('Lexical determinism: '
          f"{res['lexical_determinism']['fraction_divergence_lexically_determined']:.4f}"
          f" -> {res['lexical_determinism']['verdict']}")

    # ============================================================ I1
    import math
    strata = collections.defaultdict(lambda: ([], []))   # length -> (labels, log10 freqs)
    for lab, group in ((1, all_div), (0, none_div)):
        for k, v in group:
            if k:
                L, F = strata[min(len(k), 12)]
                L.append(lab)
                F.append(math.log10(len(v)))

    def pooled_delta(assign):
        """Weighted mean over length strata of
        mean(log10 f | divergent) - mean(log10 f | non-divergent)."""
        num = den = 0.0
        for labs, freqs in assign.values():
            sd = nd_ = 0.0
            cd = cn = 0
            for lab, f in zip(labs, freqs):
                if lab:
                    sd += f
                    cd += 1
                else:
                    nd_ += f
                    cn += 1
            if not cd or not cn:
                continue
            w = cd + cn
            num += w * (sd / cd - nd_ / cn)
            den += w
        return num / den if den else float('nan')

    obs_I1 = pooled_delta(strata)
    nulls = []
    for _ in range(N_PERM):
        shuf = {}
        for s, (labs, freqs) in strata.items():
            perm = list(labs)
            rng.shuffle(perm)
            shuf[s] = (perm, freqs)
        nulls.append(pooled_delta(shuf))
    p_I1 = perm_p(obs_I1, nulls, greater=True)
    res['I1_frequency_concentration'] = {
        'statistic': 'pooled length-stratified delta mean log10 frequency (divergent - non-divergent)',
        'locked_direction': 'POSITIVE',
        'observed': obs_I1, 'p_perm_one_sided': p_I1,
        'null_mean': sum(nulls) / len(nulls),
        'n_strata': len(strata),
        'n_types': sum(len(labs) for labs, _ in strata.values()),
        'direction_held': obs_I1 > 0,
        'verdict': ('CONCENTRATED' if (p_I1 < ALPHA and obs_I1 > 0)
                    else 'PRE-COMMIT VIOLATION (published as NULL)' if obs_I1 < 0
                    else 'NULL'),
    }
    print(f'I1 delta={obs_I1:+.4f} p={p_I1:.5f} -> {res["I1_frequency_concentration"]["verdict"]}')

    # ============================================================ I2/I3/I4 set
    by_k2 = collections.defaultdict(list)
    for t in toks:
        by_k2[t['k2']].append(t)
    primary = {}
    for k, v in by_k2.items():
        variants = collections.Counter(x['uk'] for x in v)
        if len(variants) != 2:
            continue
        a, b = list(variants)
        if len(a) == len(b):
            continue
        short = a if len(a) < len(b) else b
        primary[k] = (v, short)
    for k, (v, short) in primary.items():
        for x in v:
            x['SHORT'] = (x['uk'] == short)
    flat = [(k, x) for k, (v, _) in primary.items() for x in v]
    res['stratified_set'] = {
        'n_strata': len(primary), 'n_tokens': len(flat),
        'informative_minority_mass': sum(
            min(collections.Counter(x['SHORT'] for x in v).values()) for v, _ in primary.values()),
        'verse_final_tokens': sum(1 for _, x in flat if x['wi'] == x['nw'] - 1),
        'register_marginals': dict(collections.Counter(gp[str(x['surah'])] for _, x in flat)),
    }
    print('Stratified set:', res['stratified_set'])

    labels = [x['SHORT'] for _, x in flat]
    strat_id = [k for k, _ in flat]
    vfinal = [x['wi'] == x['nw'] - 1 for _, x in flat]
    reg = [gp[str(x['surah'])] for _, x in flat]
    relpos = [x['ayah'] / n_ayat[x['surah']] for _, x in flat]
    groups = collections.defaultdict(list)
    for i, s in enumerate(strat_id):
        groups[s].append(i)

    def stat_I2(lab):
        return sum(1 for i in range(len(lab)) if (not lab[i]) and vfinal[i])   # LONG & verse-final

    def centred(lab):
        out = [0.0] * len(lab)
        for _, idxs in groups.items():
            m = sum(1 for i in idxs if lab[i]) / len(idxs)
            for i in idxs:
                out[i] = (1.0 if lab[i] else 0.0) - m
        return out

    REGS = sorted(set(reg))

    def stat_I3a(lab):
        c = centred(lab)
        tot = 0.0
        for r in REGS:
            idxs = [i for i in range(len(lab)) if reg[i] == r]
            if idxs:
                tot += (sum(c[i] for i in idxs) ** 2) / len(idxs)
        return tot

    def stat_I3b(lab):
        c = centred(lab)
        e = [c[i] for i in range(len(lab)) if reg[i] == 'eschatological_mufassal']
        m = [c[i] for i in range(len(lab)) if reg[i] == 'legal_medinan']
        if not e or not m:
            return 0.0
        return sum(e) / len(e) - sum(m) / len(m)

    def stat_I4(lab):
        num = den = 0.0
        for _, idxs in groups.items():
            sh = [relpos[i] for i in idxs if lab[i]]
            lo = [relpos[i] for i in idxs if not lab[i]]
            if not sh or not lo:
                continue
            num += len(idxs) * (sum(sh) / len(sh) - sum(lo) / len(lo))
            den += len(idxs)
        return num / den if den else 0.0

    obs = {k: f(labels) for k, f in
           [('I2', stat_I2), ('I3a', stat_I3a), ('I3b', stat_I3b), ('I4', stat_I4)]}
    nullsd = {k: [] for k in obs}
    for _ in range(N_PERM):
        lab = list(labels)
        for _, idxs in groups.items():
            sub = [lab[i] for i in idxs]
            rng.shuffle(sub)
            for i, val in zip(idxs, sub):
                lab[i] = val
        nullsd['I2'].append(stat_I2(lab))
        nullsd['I3a'].append(stat_I3a(lab))
        nullsd['I3b'].append(stat_I3b(lab))
        nullsd['I4'].append(stat_I4(lab))

    p_I2 = perm_p(obs['I2'], nullsd['I2'], greater=True)
    p_I3a = perm_p(obs['I3a'], nullsd['I3a'], greater=True)
    p_I3b = perm_p(obs['I3b'], nullsd['I3b'], greater=True)
    p_I4 = (1 + sum(1 for v in nullsd['I4'] if abs(v) >= abs(obs['I4']))) / (1 + N_PERM)

    res['I2_verse_final'] = {
        'statistic': 'count of LONG-variant tokens at verse-final position, within-stratum permutation',
        'locked_direction': 'LONG enriched verse-finally', 'observed': obs['I2'],
        'null_mean': sum(nullsd['I2']) / N_PERM, 'p_perm_one_sided': p_I2,
        'direction_held': obs['I2'] > sum(nullsd['I2']) / N_PERM,
        'verdict': 'CONDITIONED' if p_I2 < ALPHA else 'NULL',
        'power_note': 'declared underpowered in prereg 6-I2'}
    res['I3a_register_omnibus'] = {
        'statistic': 'within-stratum-centred dispersion of SHORT rate across 4 registers',
        'locked_direction': 'none (omnibus)', 'observed': obs['I3a'],
        'null_mean': sum(nullsd['I3a']) / N_PERM, 'p_perm': p_I3a,
        'verdict': 'CONDITIONED' if p_I3a < ALPHA else 'NULL'}
    res['I3b_register_contrast'] = {
        'statistic': 'centred SHORT rate, eschatological_mufassal minus legal_medinan',
        'locked_direction': 'POSITIVE', 'observed': obs['I3b'],
        'null_mean': sum(nullsd['I3b']) / N_PERM, 'p_perm_one_sided': p_I3b,
        'direction_held': obs['I3b'] > 0,
        'verdict': ('CONDITIONED' if p_I3b < ALPHA and obs['I3b'] > 0
                    else 'PRE-COMMIT VIOLATION (published as NULL)' if obs['I3b'] < 0 else 'NULL')}
    res['I4_surah_position'] = {
        'statistic': 'pooled within-stratum mean relative-position difference (SHORT - LONG)',
        'locked_direction': 'two-sided', 'observed': obs['I4'],
        'null_mean': sum(nullsd['I4']) / N_PERM, 'p_perm_two_sided': p_I4,
        'verdict': 'CONDITIONED' if p_I4 < ALPHA else 'NULL'}
    for k in ('I2_verse_final', 'I3a_register_omnibus', 'I3b_register_contrast', 'I4_surah_position'):
        print(f'  {k}: obs={res[k]["observed"]} verdict={res[k]["verdict"]}')

    # ---------------------------------------------- unconditioned contrast (MW-7)
    naive_reg = collections.Counter()
    naive_tot = collections.Counter()
    for t in toks:
        r = gp[str(t['surah'])]
        naive_tot[r] += 1
        if t['div']:
            naive_reg[r] += 1
    res['descriptive_unconditioned_register_rates'] = {
        r: naive_reg[r] / naive_tot[r] for r in naive_tot}
    res['descriptive_unconditioned_verse_final_rate'] = {
        'verse_final': (sum(1 for t in toks if t['div'] and t['wi'] == t['nw'] - 1) /
                        max(1, sum(1 for t in toks if t['wi'] == t['nw'] - 1))),
        'non_final': (sum(1 for t in toks if t['div'] and t['wi'] != t['nw'] - 1) /
                      max(1, sum(1 for t in toks if t['wi'] != t['nw'] - 1)))}

    # ---------------------------------------------- classical audit (7)
    def where(pred):
        return [f"{t['surah']}:{t['ayah']}" for t in toks if pred(t)]

    badal_waw = collections.Counter()
    for t in div_toks:
        if t.get('cls') == 'BADAL-WAW-ALIF':
            badal_waw[(t['uk'], t['sk'])] += 1
    ibrahim = collections.Counter(t['surah'] for t in toks if t['uk'] == 'ابرهم')
    kitab_plene = where(lambda t: t['sk'] in ('كتاب',) and t['uk'] == 'كتاب')
    kitab_defect = where(lambda t: t['sk'] in ('كتاب',) and t['uk'] == 'كتب')
    samawat_plene = where(lambda t: t['sk'] == 'سماوات' and t['uk'] == 'سموات')
    ziyada_q33 = [{'ref': f"{t['surah']}:{t['ayah']}", 'uthmani': t['uk'], 'simple': t['sk'],
                   'verse_final': t['wi'] == t['nw'] - 1, 'class': t.get('cls')}
                  for t in div_toks if t['surah'] == 33 and t.get('cls') == 'ZIYADA-ALIF']
    res['classical_audit'] = {
        'anchor': ("al-Suyuti, al-Itqan fi 'ulum al-Qur'an, al-naw' al-sadis wa-l-sab'un "
                   "(fi marsum al-khatt wa-adab kitabatihi); "
                   "data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt line 23216"),
        'C1_badal_waw_items': {f'{a} | {b}': n for (a, b), n in badal_waw.most_common()},
        'C2_ibrahim_defective_by_surah': dict(ibrahim),
        'C3_kitab_plene_locations': kitab_plene,
        'C3_kitab_defective_count': len(kitab_defect),
        'C4_samawat_plene_locations': samawat_plene,
        'C5_ziyada_alif_in_Q33': ziyada_q33,
    }

    # ---------------------------------------------- alternating inventory
    res['alternating_inventory'] = sorted(
        [{'simple_pausal_form': k,
          'variants': dict(collections.Counter(x['uk'] for x in v)),
          'n_tokens': len(v)}
         for k, (v, _) in primary.items()],
        key=lambda d: -d['n_tokens'])

    # ---------------------------------------------- consolidated verdicts (prereg 6)
    res['verdicts'] = {
        'descriptive_lexical_determinism': res['lexical_determinism']['verdict'],
        'I1_frequency_concentration': res['I1_frequency_concentration']['verdict'],
        'I2_verse_final': res['I2_verse_final']['verdict'],
        'I3a_register_omnibus': res['I3a_register_omnibus']['verdict'],
        'I3b_register_contrast': res['I3b_register_contrast']['verdict'],
        'I4_surah_position': res['I4_surah_position']['verdict'],
    }
    res['verdicts']['n_registered_cells_passing'] = sum(
        1 for k, v in res['verdicts'].items()
        if k.startswith('I') and v in ('CONCENTRATED', 'CONDITIONED'))
    res['wall_seconds'] = round(time.time() - t0, 1)

    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'h-new-2740.json'), 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    manifest = {'finding_id': 'H-NEW-2740', 'seed': seed, 'n_perm': N_PERM,
                'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'prereg': PREREG, 'prereg_sha256': PREREG_SHA,
                'script': 'findings/phase-b-hypotheses/scripts/h-new-2740.py',
                'script_sha256': sha256(os.path.abspath(__file__)),
                'frozen_inputs': FROZEN,
                'output': os.path.relpath(os.path.join(outdir, 'h-new-2740.json'), REPO)}
    with open(os.path.join(outdir, 'manifest.json'), 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    print(f'Wrote {outdir}  ({res["wall_seconds"]}s)')
    return res


if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else SEED_PRIMARY
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    tag = 'primary' if seed == SEED_PRIMARY else 'replication' if seed == SEED_REPLICATION else 'other'
    main(seed, os.path.join(REPO, 'findings/phase-b-hypotheses/runs/h-new-2740',
                            f'{stamp}-{tag}-seed{seed}'))
