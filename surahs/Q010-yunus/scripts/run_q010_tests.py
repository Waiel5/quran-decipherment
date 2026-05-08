#!/usr/bin/env python3
"""Run all 4 Q 010 pre-registered novel tests.

Pre-reg SHA verification per pre-reg file.
Outputs JSON results to surahs/Q010-yunus/csv/.
"""
import hashlib, json, os, random, re, sys

ROOT = '/Users/grey/Downloads/quran'
QTEXT = os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')
FR = os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-111.json')
PREREG_DIR = os.path.join(ROOT, 'surahs/Q010-yunus')
OUT_DIR = os.path.join(ROOT, 'surahs/Q010-yunus/csv')

def sha256(path):
    with open(path, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()


def verify_prereg(name):
    p = os.path.join(PREREG_DIR, name)
    s = sha256(p)
    print(f'  pre-reg {name}: SHA256={s}')
    return s


def load_quran():
    with open(QTEXT) as f: return json.load(f)


def F01_yunus_concentration():
    print('\n--- Q010-F-01: yūnus token concentration ---')
    sha = verify_prereg('Q010-F-01-yunus-token-concentration-prereg.md')
    qd = load_quran()
    total_tokens = q10_tokens = 0
    locations = []
    total_words = q10_words = 0
    for s in qd:
        sid = s['id']
        for v in s['verses']:
            words = v['text'].split()
            total_words += len(words)
            if sid == 10: q10_words += len(words)
            for w in words:
                clean = re.sub(r'[^ء-ي]', '', w)
                if clean == 'يونس':
                    total_tokens += 1
                    if sid == 10: q10_tokens += 1
                    locations.append({'surah': sid, 'verse': v['id']})
    concentration = q10_tokens / total_tokens if total_tokens > 0 else 0.0
    baseline = q10_words / total_words if total_words > 0 else 0.0
    ratio = concentration / baseline if baseline > 0 else 0.0
    confirmed = concentration > 1.5 * baseline and total_tokens >= 2
    out = {
        'finding_id': 'Q010-F-01',
        'prereg_sha256': sha,
        'total_tokens': total_tokens,
        'q10_tokens': q10_tokens,
        'q10_concentration': concentration,
        'q10_words': q10_words,
        'total_words': total_words,
        'baseline_uniform': baseline,
        'concentration_ratio': ratio,
        'locations': locations,
        'verdict': 'CONFIRMED' if confirmed else 'NULL',
        'comparison_to_q012_f03': 'yūsuf 92.6% in Q12 vs yūnus {:.1%} in Q10'.format(concentration),
        'note': 'Q 10 is named after a prophet whose token appears only at v. 98 in Q 10. The other occurrence is at Q 37:139 (al-Ṣāffāt).' if total_tokens == 2 else None,
    }
    with open(os.path.join(OUT_DIR, 'Q010-F-01.json'), 'w') as f: json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k != 'locations'}, ensure_ascii=False, indent=2))
    print(f'Locations: {locations}')
    return out


def F02_alr_cluster():
    print('\n--- Q010-F-02: ALR-cluster Fisher-Rao cohesion ---')
    sha = verify_prereg('Q010-F-02-alr-cluster-cohesion-prereg.md')
    with open(FR) as f: fr = json.load(f)
    D = {}
    for a, b, d in fr['D_matrix_upper_triangular']:
        D[(a, b)] = d; D[(b, a)] = d
    def dist(a, b):
        if a == b: return 0
        return D.get((a, b), float('nan'))
    alr = [10, 11, 12, 14, 15]
    # intra-cluster mean
    pairs = [(a, b) for i, a in enumerate(alr) for b in alr[i+1:]]
    intra_mean = sum(dist(a, b) for a, b in pairs) / len(pairs)
    # corpus mean
    all_d = [d for (a, b), d in D.items() if a < b]
    corpus_mean = sum(all_d) / len(all_d)
    # permutation: sample 5 from 1..114 excluding alr
    rng = random.Random(1042899)
    other_surahs = [s for s in range(1, 115) if s not in alr]
    n_perm = 10000
    smaller = 0
    perm_means = []
    for _ in range(n_perm):
        sample = rng.sample(other_surahs, 5)
        sp = [(a, b) for i, a in enumerate(sample) for b in sample[i+1:]]
        m = sum(dist(a, b) for a, b in sp) / len(sp)
        perm_means.append(m)
        if m <= intra_mean: smaller += 1
    pval = smaller / n_perm
    # Q10 sub-test: Q10 mean to ALR siblings vs to others
    q10_to_alr = [dist(10, s) for s in alr if s != 10]
    q10_to_others = [dist(10, s) for s in range(1, 115) if s != 10 and s not in alr]
    q10_alr_mean = sum(q10_to_alr) / len(q10_to_alr)
    q10_other_mean = sum(q10_to_others) / len(q10_to_others)
    confirmed_main = (pval <= 0.025) and (intra_mean < corpus_mean)
    out = {
        'finding_id': 'Q010-F-02',
        'prereg_sha256': sha,
        'alr_cluster': alr,
        'intra_mean_FR': intra_mean,
        'corpus_mean_FR': corpus_mean,
        'perm_p': pval,
        'n_perm': n_perm,
        'alpha_bonferroni_2': 0.025,
        'q10_to_alr_mean': q10_alr_mean,
        'q10_to_others_mean': q10_other_mean,
        'q10_alr_advantage': q10_other_mean - q10_alr_mean,
        'pairwise_alr': {f'Q{a}-Q{b}': dist(a, b) for a, b in pairs},
        'verdict_intra_lt_random': 'CONFIRMED' if confirmed_main else 'NULL',
        'verdict_q10_alr_pull': 'PULLED-IN' if q10_alr_mean < q10_other_mean else 'NULL',
    }
    with open(os.path.join(OUT_DIR, 'Q010-F-02.json'), 'w') as f: json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps(out, indent=2))
    return out


def F03_narrative_purity():
    print('\n--- Q010-F-03: narrative-purity index ---')
    sha = verify_prereg('Q010-F-03-narrative-purity-prereg.md')
    qd = load_quran()
    proper_nouns = {
        'يونس', 'موسى', 'نوح', 'هود', 'صالح', 'شعيب', 'لوط',
        'ابراهيم', 'إبراهيم', 'اسحاق', 'إسحاق', 'يعقوب', 'اسماعيل', 'إسماعيل',
        'يوسف', 'فرعون', 'عيسى', 'داود', 'سليمان', 'ادريس', 'إدريس',
        'ايوب', 'أيوب', 'زكريا', 'يحيى', 'الياس', 'إلياس', 'اليسع', 'ذو',
    }
    rows = []
    for s in qd:
        sid = s['id']
        words = []
        for v in s['verses']: words.extend(v['text'].split())
        total = len(words)
        narr = 0
        for w in words:
            cw = re.sub(r'[^ء-ي]', '', w)
            if cw in proper_nouns: narr += 1
        density = narr / total if total > 0 else 0.0
        rows.append({'surah': sid, 'words': total, 'narr_count': narr, 'density': density})
    # rank by density desc
    rows.sort(key=lambda r: -r['density'])
    for i, r in enumerate(rows): r['rank'] = i + 1
    q10 = next(r for r in rows if r['surah'] == 10)
    q12 = next(r for r in rows if r['surah'] == 12)
    confirmed = q10['rank'] > 30
    out = {
        'finding_id': 'Q010-F-03',
        'prereg_sha256': sha,
        'q10_density': q10['density'],
        'q10_rank': q10['rank'],
        'q10_narr_count': q10['narr_count'],
        'q10_words': q10['words'],
        'q12_density': q12['density'],
        'q12_rank': q12['rank'],
        'top_10_narrative': [{'surah': r['surah'], 'rank': r['rank'], 'density': r['density']} for r in rows[:10]],
        'bottom_10': [{'surah': r['surah'], 'rank': r['rank'], 'density': r['density']} for r in rows[-10:]],
        'verdict': 'CONFIRMED' if confirmed else 'NULL',
    }
    with open(os.path.join(OUT_DIR, 'Q010-F-03.json'), 'w') as f: json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k not in ('top_10_narrative', 'bottom_10')}, indent=2))
    print('TOP-10:', out['top_10_narrative'])
    return out


def F04_awliya_signature():
    print('\n--- Q010-F-04: awliyāʾ lexical signature ---')
    sha = verify_prereg('Q010-F-04-awliya-lexical-prereg.md')
    qd = load_quran()
    # exact phrase
    strict_pat = re.compile(r'لا خوف عليهم ولا هم يحزنون')
    # loose: tolerate alternate pronouns / minor variants
    loose_pat = re.compile(r'لا خوف علي(?:ه[م]|كم|نا) ولا هم يحزنون|لا خوف علي(?:ه[م]|كم) و?لا (?:هم|أنتم|أنفسهم) (?:تحزنون|يحزنون)')
    strict_hits = []
    loose_hits = []
    for s in qd:
        sid = s['id']
        for v in s['verses']:
            t = v['text']
            if strict_pat.search(t):
                strict_hits.append({'surah': sid, 'verse': v['id'], 'text': t})
            if loose_pat.search(t):
                loose_hits.append({'surah': sid, 'verse': v['id'], 'text': t})
    n_strict = len(strict_hits); n_loose = len(loose_hits)
    confirmed = n_strict >= 6
    null_strict = n_strict < 4
    out = {
        'finding_id': 'Q010-F-04',
        'prereg_sha256': sha,
        'phrase_strict_count': n_strict,
        'phrase_loose_count': n_loose,
        'strict_locations': strict_hits,
        'loose_only': [h for h in loose_hits if not any(s['surah']==h['surah'] and s['verse']==h['verse'] for s in strict_hits)],
        'verdict': 'CONFIRMED' if confirmed else ('NULL' if null_strict else 'DIRECTIONAL'),
    }
    with open(os.path.join(OUT_DIR, 'Q010-F-04.json'), 'w') as f: json.dump(out, f, ensure_ascii=False, indent=2)
    print(json.dumps({k: v for k, v in out.items() if k not in ('strict_locations', 'loose_only')}, indent=2))
    print(f'Strict hits ({n_strict}):')
    for h in strict_hits: print(f'  Q{h["surah"]}:{h["verse"]} — {h["text"]}')
    return out


if __name__ == '__main__':
    os.makedirs(OUT_DIR, exist_ok=True)
    F01_yunus_concentration()
    F02_alr_cluster()
    F03_narrative_purity()
    F04_awliya_signature()
