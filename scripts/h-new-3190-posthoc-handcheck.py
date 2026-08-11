#!/usr/bin/env python3
"""H-NEW-3190 POST-HOC hand-check. NON-CONFIRMATORY, no verdict rests on it.

Prereg §7.4 requires a hand-read sample of pairs where the ten translations AGREE, not only
where they disagree: disagreements advertise themselves, shared errors do not. Writes to a
SIBLING directory; the locked run directory is not touched.
"""
import json, os, re, sys, unicodedata
import numpy as np

ROOT = '/Users/grey/Downloads/quran'
RUN = sys.argv[1] if len(sys.argv) > 1 else \
    f'{ROOT}/findings/phase-b-hypotheses/runs/h-new-3190/20260809T121246Z'
OUT = RUN + '-posthoc'
LANGS = ['bn', 'en', 'es', 'fr', 'id', 'ru', 'sv', 'tr', 'ur', 'zh']

rows = json.load(open(f'{RUN}/pool.json'))
WAQF_RE = re.compile('[' + re.escape(''.join(chr(c) for c in range(0x06D6, 0x06DF)) + chr(0x06E9)) + ']')
qt = json.load(open(f'{ROOT}/quran-text/quran-no-tashkeel.json'))
verses = {(s['id'], v['id']): [w for w in WAQF_RE.sub(' ', v['text']).split() if w]
          for s in qt for v in s['verses']}
T = {}
for L in LANGS:
    dd = json.load(open(f'{ROOT}/data/alt-text/risan-quran-json/dist/quran_{L}.json'))
    T[L] = {(s['id'], v['id']): v['translation'] for s in dd for v in s['verses']}


def norm_tokens(s, lang):
    s = unicodedata.normalize('NFKC', s).lower()
    s = re.sub(r'\[[^\]]*\]', ' ', s); s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'[^\w\s]', ' ', s, flags=re.UNICODE)
    if lang == 'zh':
        s = ''.join(s.split()); return [s[i:i+2] for i in range(len(s)-1)] or list(s)
    return s.split()


def lev(a, b):
    if len(a) < len(b): a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def key(x):
    return tuple(x) if isinstance(x, (list, tuple)) else tuple(json.loads(x.replace('(', '[').replace(')', ']')))


def pct(v):
    v = np.asarray(v, float); o = np.argsort(v, kind='mergesort'); out = np.empty(len(v)); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
        out[o[i:j + 1]] = (i + j) / 2.0 / max(len(v) - 1, 1); i = j + 1
    return out


A = [key(r['a']) for r in rows]
B = [key(r['b']) for r in rows]
d_l2 = {}
for L in LANGS:
    vals = []
    for a, b in zip(A, B):
        x, y = norm_tokens(T[L][a], L), norm_tokens(T[L][b], L)
        vals.append(lev(x, y) / max(len(x), len(y), 1))
    d_l2[L] = pct(vals)
M = np.vstack([d_l2[L] for L in LANGS])
pooled = np.median(M, axis=0)
spread = M.max(axis=0) - M.min(axis=0)      # small spread = the ten translations AGREE


def diff_tokens(a, b):
    ta, tb = verses[a], verses[b]
    return [(x, y) for x, y in zip(ta, tb) if x != y] if len(ta) == len(tb) else \
        [('<unequal length>', f'{len(ta)}v{len(tb)}')]


report = {'A_agree_LOW_but_lexical': [], 'B_agree_HIGH_but_morphological': [],
          'C_maximal_disagreement': []}

# A. ten translations AGREE the pair is CLOSE, yet the Arabic difference is purely LEXICAL.
#    If the lexical distinction is real, a shared collapse is a shared translator error.
idx = [i for i in range(len(rows))
       if rows[i]['n_lex'] >= 1 and rows[i]['n_morph'] == 0 and spread[i] < 0.25]
for i in sorted(idx, key=lambda i: pooled[i])[:10]:
    report['A_agree_LOW_but_lexical'].append(dict(
        pair=f'{A[i]}<->{B[i]}', d=rows[i]['d'], n_lex=rows[i]['n_lex'],
        pooled_rank=round(float(pooled[i]), 4), spread=round(float(spread[i]), 4),
        differing_tokens=diff_tokens(A[i], B[i]),
        en=[T['en'][A[i]], T['en'][B[i]]], fr=[T['fr'][A[i]], T['fr'][B[i]]]))

# B. ten translations AGREE the pair is FAR APART, yet the Arabic difference is purely
#    MORPHOLOGICAL (same root). A shared amplification of a same-root alternation.
idx = [i for i in range(len(rows))
       if rows[i]['n_morph'] >= 1 and rows[i]['n_lex'] == 0 and spread[i] < 0.35]
for i in sorted(idx, key=lambda i: -pooled[i])[:10]:
    report['B_agree_HIGH_but_morphological'].append(dict(
        pair=f'{A[i]}<->{B[i]}', d=rows[i]['d'], n_morph=rows[i]['n_morph'],
        n_indel=rows[i]['n_indel'],
        pooled_rank=round(float(pooled[i]), 4), spread=round(float(spread[i]), 4),
        differing_tokens=diff_tokens(A[i], B[i]),
        en=[T['en'][A[i]], T['en'][B[i]]], fr=[T['fr'][A[i]], T['fr'][B[i]]]))

# C. where the ten translations DISAGREE most (the easy direction, included for contrast)
for i in sorted(range(len(rows)), key=lambda i: -spread[i])[:10]:
    report['C_maximal_disagreement'].append(dict(
        pair=f'{A[i]}<->{B[i]}', d=rows[i]['d'], n_lex=rows[i]['n_lex'],
        n_morph=rows[i]['n_morph'], spread=round(float(spread[i]), 4),
        per_language={L: round(float(d_l2[L][i]), 3) for L in LANGS},
        differing_tokens=diff_tokens(A[i], B[i])))

os.makedirs(OUT, exist_ok=True)
with open(f'{OUT}/handcheck.json', 'w') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

for k, v in report.items():
    print('=' * 96); print(k, f'(n shown {len(v)})')
    for e in v[:6]:
        print(' ', e['pair'], 'd=', e['d'], 'diff=', e.get('differing_tokens'),
              'rank=', e.get('pooled_rank'), 'spread=', e.get('spread'))
        if 'en' in e:
            print('     en1:', e['en'][0][:105]); print('     en2:', e['en'][1][:105])
print('\nwrote', f'{OUT}/handcheck.json')
