#!/usr/bin/env python3
"""
Classify each pair from pairs_raw.json into:
  - word_order
  - lexeme_substitution
  - inflection_change
  - particle_addition_or_removal
  - preposition_change
  - suffix_pronoun_change
  - addition (one verse strictly contains the other)
  - identical_lemma_set (ratio==1.0; could still be word-order/inflection)

Each pair gets multiple labels — they are not mutually exclusive.

Output:
  - pairs_classified.json
  - mutashabih-pairs.csv  with full table
"""
import json, re, csv
from collections import Counter, defaultdict

PAIRS = '/Users/grey/Downloads/quran/scripts/mutashabih/pairs_raw.json'
MORPH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
SAHIH = '/Users/grey/Downloads/quran/data/translations/en.sahih.txt'
OUT_JSON = '/Users/grey/Downloads/quran/scripts/mutashabih/pairs_classified.json'
OUT_CSV  = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/mutashabih-pairs.csv'

PARTICLES_FORMS = {'wa','fa','sa','la','bi','li','ka','qad','vum~a','>a','>am','ya','yA','>aw','la~','lA','maA','>i*aA','min','EalaY`','EalaY','>ilaY`','>ilaY','fiY'}
PRONOMINAL_SUFF = {'humo','huma','hum','haA','hi','hu','ka','kumo','kum','kumA','naA','niY','y','tumo','tum','tumA','tu','ta','ti','wA@','tunolA','tin'}
PREPS_LEM = {'min','EalaY`','>ilaY`','fiY','Ean','ka','bi','li','ladaY','xilaAl','>amaAm'}

# parse morphology
verses_morph = defaultdict(list)
with open(MORPH) as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.strip().split('\t')
        if len(parts) < 4:
            continue
        loc, form, tag, feats = parts
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)', loc)
        if not m:
            continue
        s, v, w, p = map(int, m.groups())
        d = {'w': w, 'p': p, 'form': form, 'tag': tag, 'lem': None, 'root': None, 'pos': None,
             'num': None, 'gen': None, 'tense': None, 'feats': feats}
        for fld in feats.split('|'):
            if fld.startswith('LEM:'):
                d['lem'] = fld[4:]
            elif fld.startswith('ROOT:'):
                d['root'] = fld[5:]
            elif fld.startswith('POS:'):
                d['pos'] = fld[4:]
            elif fld in ('PERF','IMPF','IMPV'):
                d['tense'] = fld
            elif fld in ('SG','DUAL','PL','MS','MP','FS','FP','M','F'):
                if fld in ('MS','MP','FS','FP','M','F'):
                    d['gen'] = fld
        verses_morph[(s,v)].append(d)

# load pairs and texts
with open(PAIRS) as f:
    pairs = json.load(f)

with open(QURAN) as f:
    qdata = json.load(f)
texts = {}
for surah in qdata:
    for v in surah['verses']:
        texts[(surah['id'], v['id'])] = v['text']

# english translation: line N (1-indexed) -> verse N in canonical order
sahih_lines = open(SAHIH).read().splitlines()
# build (s,v) -> sahih index
en = {}
i = 0
for surah in qdata:
    for v in surah['verses']:
        if i < len(sahih_lines):
            en[(surah['id'], v['id'])] = sahih_lines[i]
        i += 1

# ---------- classifier ----------
def lemma_seq(vk):
    """ordered list of lemma-or-form keys, one per token (one per morph row)"""
    return [(d['lem'] or d['form']) for d in verses_morph[vk]]

def stem_seq(vk):
    """ordered list of STEM-only entries (filter out PREFIX/SUFFIX)"""
    return [d for d in verses_morph[vk] if 'STEM' in d['feats']]

def classify(pair):
    a = (pair['s1'], pair['v1'])
    b = (pair['s2'], pair['v2'])
    only_a = pair['only1']
    only_b = pair['only2']
    common = pair['common_tokens']
    labels = []

    # check the COMPLETE lemma sequences (not just bag) for word-order changes
    seq_a = lemma_seq(a)
    seq_b = lemma_seq(b)
    bag_a = Counter(seq_a)
    bag_b = Counter(seq_b)
    same_bag = (bag_a == bag_b)
    same_seq = (seq_a == seq_b)
    if same_bag and not same_seq:
        labels.append('word_order')
    if same_bag and same_seq:
        labels.append('truly_identical')
    if same_bag and pair['len1'] == pair['len2']:
        # same bag, possibly different sequence handled above
        pass

    # detect particle add/remove and pronoun add/remove from only_a/only_b
    # tokens in only_a/only_b have prefix L:, F:
    def parse_tok(t):
        if t.startswith('L:'): return ('L', t[2:])
        if t.startswith('F:'): return ('F', t[2:])
        return ('?', t)

    toks_a = [parse_tok(t) for t in only_a]
    toks_b = [parse_tok(t) for t in only_b]

    flat_a = set(only_a)
    flat_b = set(only_b)

    # particles via form-tokens
    part_a = [v for k,v in toks_a if k=='F' and v in PARTICLES_FORMS]
    part_b = [v for k,v in toks_b if k=='F' and v in PARTICLES_FORMS]
    if part_a or part_b:
        labels.append('particle_change')

    # pronoun suffixes
    pron_a = [v for k,v in toks_a if k=='F' and v in PRONOMINAL_SUFF]
    pron_b = [v for k,v in toks_b if k=='F' and v in PRONOMINAL_SUFF]
    if pron_a or pron_b:
        labels.append('suffix_pronoun_change')

    # prepositions (often appear as lemmas in QAC, e.g., L:min, L:fiY)
    prep_a = [v for k,v in toks_a if k=='L' and v in PREPS_LEM]
    prep_b = [v for k,v in toks_b if k=='L' and v in PREPS_LEM]
    if prep_a or prep_b:
        labels.append('preposition_change')

    # lexeme substitutions: pairs of differing LEMMAS that share the same ROOT (inflection)
    # vs differing LEMMAS with different ROOTS (substitution)
    # We need to compare the unique-set of stem lemmas in each.
    stems_a = [d for d in verses_morph[a] if 'STEM' in d['feats'] and d['lem']]
    stems_b = [d for d in verses_morph[b] if 'STEM' in d['feats'] and d['lem']]
    lem_a = Counter(d['lem'] for d in stems_a)
    lem_b = Counter(d['lem'] for d in stems_b)
    only_lem_a = (lem_a - lem_b)
    only_lem_b = (lem_b - lem_a)
    # same-root pairs across the two only-sets => inflection change
    root_a = {}
    for d in stems_a:
        if d['lem'] in only_lem_a:
            root_a.setdefault(d['root'], []).append(d['lem'])
    root_b = {}
    for d in stems_b:
        if d['lem'] in only_lem_b:
            root_b.setdefault(d['root'], []).append(d['lem'])
    inflection_pairs = []
    substitution_pairs = []
    for r in set(root_a) & set(root_b):
        if r is None: continue
        for la in root_a[r]:
            for lb in root_b[r]:
                inflection_pairs.append((r, la, lb))
    matched_a = set(la for r in (set(root_a)&set(root_b)) if r for la in root_a[r])
    matched_b = set(lb for r in (set(root_a)&set(root_b)) if r for lb in root_b[r])
    unmatched_a = [(r, la) for r, ls in root_a.items() if r for la in ls if la not in matched_a]
    unmatched_b = [(r, lb) for r, ls in root_b.items() if r for lb in ls if lb not in matched_b]

    # substitutions: differing-root lexemes
    if unmatched_a and unmatched_b:
        for ra, la in unmatched_a:
            for rb, lb in unmatched_b:
                substitution_pairs.append(((ra, la), (rb, lb)))
    if inflection_pairs:
        labels.append('inflection_change')
    if substitution_pairs:
        labels.append('lexeme_substitution')

    # addition: one verse strictly contains the other (in bag terms)
    if all(bag_a[k] <= bag_b[k] for k in bag_a) and bag_a != bag_b:
        labels.append('addition_in_b')
    if all(bag_b[k] <= bag_a[k] for k in bag_b) and bag_a != bag_b:
        labels.append('addition_in_a')

    # If no labels at all (everything matched perfectly): mark identical_lemma_set
    if not labels:
        labels.append('identical_lemma_set')

    return {
        'labels': labels,
        'inflection_pairs': inflection_pairs,
        'substitution_pairs': substitution_pairs,
        'particle_a_only': part_a,
        'particle_b_only': part_b,
        'pron_a_only': pron_a,
        'pron_b_only': pron_b,
        'unmatched_a': unmatched_a,
        'unmatched_b': unmatched_b,
    }

# ---------- run ----------
out = []
for p in pairs:
    cls = classify(p)
    enriched = dict(p)
    enriched['classification'] = cls
    enriched['arabic1'] = texts.get((p['s1'], p['v1']), '')
    enriched['arabic2'] = texts.get((p['s2'], p['v2']), '')
    enriched['english1'] = en.get((p['s1'], p['v1']), '')
    enriched['english2'] = en.get((p['s2'], p['v2']), '')
    out.append(enriched)

with open(OUT_JSON, 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f'wrote {OUT_JSON}: {len(out)} pairs')

# label histogram
hist = Counter()
for o in out:
    for l in o['classification']['labels']:
        hist[l] += 1
print('\nlabel histogram:')
for l, c in hist.most_common():
    print(f'  {l}: {c}')

# write CSV
import csv
with open(OUT_CSV, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow([
        'rank','s1','v1','s2','v2','overlap_ratio','len1','len2','common',
        'labels','inflection_pairs','substitution_pairs','particle_diff','pron_diff',
        'arabic1','arabic2','english1','english2'
    ])
    for i, o in enumerate(out, 1):
        cls = o['classification']
        w.writerow([
            i, o['s1'], o['v1'], o['s2'], o['v2'],
            o['overlap_ratio'], o['len1'], o['len2'], o['common_count'],
            ';'.join(cls['labels']),
            ';'.join(f"{r}:{a}/{b}" for r,a,b in cls['inflection_pairs']),
            ';'.join(f"{a[1]}/{b[1]}" for a,b in cls['substitution_pairs']),
            f"a:{','.join(cls['particle_a_only'])} b:{','.join(cls['particle_b_only'])}",
            f"a:{','.join(cls['pron_a_only'])} b:{','.join(cls['pron_b_only'])}",
            o['arabic1'], o['arabic2'],
            o['english1'][:200], o['english2'][:200],
        ])
print(f'wrote {OUT_CSV}')
