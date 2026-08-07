#!/usr/bin/env python3
"""H-NEW-2800 — POST-HOC DIAGNOSTICS. Not a registered inference.

Everything in this file was written AFTER the primary run
(findings/phase-b-hypotheses/runs/h-new-2800/20260807T060054Z/) and carries no
pre-registered direction, no Bonferroni slot and no verdict authority. Per
INVESTIGATION-PROTOCOL 1.7 (MW-7) any claim resting on it carries a single-test
alpha = 0.05 ceiling and is labelled post-hoc wherever it appears.

Purpose:
  D1  quantify the U+06DE (rub al-hizb) tokenisation artefact in the onset bigrams
  D2  characterise WHAT drives al-Bukhari's real-boundary onset concentration
  D3  locate the single non-legal occurrence of the G1 generative template
  D4  per-1000-word rates of the generative rules by register (unit-drift-clean view)
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

PROJECT = '/Users/grey/Downloads/quran'
QJSON = os.path.join(PROJECT, 'quran-text/quran-no-tashkeel.json')
J2500 = os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-2500.json')
BUKHARI = os.path.join(PROJECT, 'data/baseline-corpora/raw/bukhari-noquran.txt')
PRIMARY_RUN = os.path.join(
    PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2800/20260807T060054Z/h-new-2800.json')

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2800-diagnostics', RUNSTAMP)

# Written as explicit escapes, NOT as literal Arabic: typing these ranges as literals
# lets bidirectional reordering permute the range endpoints. These are byte-identical to
# h-new-2800.py's and to H-NEW-2680's.
AR_DIAC = re.compile('[\\u0610-\\u061a\\u064b-\\u065f\\u0670\\u06d6-\\u06ed\\u0640]')
NON_AR = re.compile('[^\\u0621-\\u064a\\s]')
HIZB = '۞'
TOP_K = 8


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def conj_strip(w):
    return w[1:] if len(w) >= 3 and w[0] in ('و', 'ف') else w


def onset_bigram(u):
    return (conj_strip(u[0]), u[1]) if len(u) >= 2 else None


def topk(units, k=TOP_K):
    bg = [b for b in (onset_bigram(u) for u in units) if b]
    if not bg:
        return 0.0, 0, []
    c = Counter(bg)
    return sum(n for _, n in c.most_common(k)) / len(bg), len(bg), c.most_common(k)


def main():
    os.makedirs(RUNDIR, exist_ok=True)
    qjson = json.load(open(QJSON, encoding='utf-8'))
    gp = json.load(open(J2500, encoding='utf-8'))['genre_proxy']
    sg = {int(k): v for k, v in gp['surah_genre'].items()}
    LEGAL = [s for s in range(1, 115) if sg[s] == 'legal_medinan']

    verses = {}
    for su in qjson:
        for vv in su['verses']:
            verses[(su['id'], vv['id'])] = vv['text']

    legal_units_raw = [verses[(s, v)].split()
                       for s in LEGAL for v in range(1, len(qjson[s - 1]['verses']) + 1)]

    # ---- D1: the U+06DE artefact -------------------------------------------
    n_hizb_verses = sum(1 for u in legal_units_raw if u and u[0] == HIZB)
    n_hizb_corpus = sum(1 for t in verses.values() if t.split() and t.split()[0] == HIZB)
    legal_units_clean = [[w for w in u if w != HIZB] for u in legal_units_raw]
    raw_c, raw_n, raw_top = topk(legal_units_raw)
    cln_c, cln_n, cln_top = topk(legal_units_clean)
    d1 = {
        'what': 'U+06DE RUB EL HIZB is tokenised as a standalone word in '
                'quran-text/quran-no-tashkeel.json and occupies verse-initial position, '
                'splitting the real onset bigram.',
        'legal_verses_starting_with_U06DE': n_hizb_verses,
        'corpus_verses_starting_with_U06DE': n_hizb_corpus,
        'topk_conc_as_run': raw_c,
        'topk_conc_marker_removed': cln_c,
        'delta': cln_c - raw_c,
        'top_bigrams_marker_removed': [[' '.join(b), n] for b, n in cln_top],
        'effect_on_H5_H6': 'H6 gap is 0.29815 - 0.16111 = 0.13704; the artefact is worth '
                           f'{cln_c - raw_c:.5f}. Removing it cannot change either verdict.',
    }
    log(f'D1 U+06DE: {n_hizb_verses} legal verses affected; conc {raw_c:.5f} -> {cln_c:.5f}')

    # ---- D2: what drives al-Bukhari's concentration -------------------------
    buk = NON_AR.sub(' ', AR_DIAC.sub('', open(BUKHARI, encoding='utf-8').read())).split()
    openers = {'حدثنا', 'حدثني', 'أخبرنا', 'أخبرني'}
    idx = [i for i, w in enumerate(buk) if w in openers]
    units = [buk[a + 1:b] for a, b in zip(idx, idx[1:] + [len(buk)]) if b - a - 1 >= 3]
    _c, _n, top = topk(units, 32)
    # An onset bigram is ONOMASTIC if it contains a name-chain particle or a theophoric.
    NAME_MARKERS = {'بن', 'ابن', 'أبي', 'أبو', 'عن', 'عبد'}
    onom = [(b, n) for b, n in top if set(b) & NAME_MARKERS]
    d2 = {
        'what': 'al-Bukhari real-boundary onset concentration is driven by the ISNAD NAME '
                'inventory, not by legal formulae. The two corpora have closed onset sets of '
                'different KINDS.',
        'n_units': len(units),
        'top32': [[' '.join(b), n] for b, n in top],
        'top32_onomastic': [[' '.join(b), n] for b, n in onom],
        'share_of_top32_mass_that_is_onomastic':
            sum(n for _, n in onom) / sum(n for _, n in top),
        'n_onomastic_of_top32': len(onom),
    }
    log(f"D2 onomastic share of Bukhari top-32 mass: "
        f"{d2['share_of_top32_mass_that_is_onomastic']:.4f}")

    # ---- D3: the single non-legal G1 occurrence -----------------------------
    prim = json.load(open(PRIMARY_RUN, encoding='utf-8'))
    g1 = prim['census']['G1']['locations']
    g1_nonlegal = [l for l in g1 if sg[int(l.split(':')[0])] != 'legal_medinan']
    d3 = {
        'g1_total': len(g1),
        'g1_locations': g1,
        'g1_non_legal_locations': g1_nonlegal,
        'g1_non_legal_text': {l: verses[(int(l.split(':')[0]), int(l.split(':')[1]))]
                              for l in g1_nonlegal},
    }
    log(f'D3 G1 non-legal occurrences: {g1_nonlegal}')

    # ---- D4: unit-drift-clean per-1000-word rates ---------------------------
    ud = prim['unit_drift_declaration']
    d4 = {}
    for fid in ['G1', 'G2', 'G3']:
        byreg = prim['census'][fid]['by_register']
        d4[fid] = {r: {'n': byreg.get(r, 0),
                       'per_1000_words': 1000.0 * byreg.get(r, 0) / ud['words_by_register'][r],
                       'per_100_verses': 100.0 * byreg.get(r, 0) / ud['verses_by_register'][r]}
                   for r in ud['words_by_register']}
    log('D4 G3 per-1000-words: ' + ', '.join(
        f"{r}={d4['G3'][r]['per_1000_words']:.2f}" for r in d4['G3']))

    out = {
        'id': 'H-NEW-2800-DIAGNOSTICS',
        'status': 'POST-HOC — no pre-registered direction, no Bonferroni slot, no verdict '
                  'authority. MW-7 single-test alpha = 0.05 ceiling applies to anything '
                  'resting on it.',
        'primary_run': os.path.relpath(PRIMARY_RUN, PROJECT),
        'D1_hizb_marker_artefact': d1,
        'D2_bukhari_concentration_is_onomastic': d2,
        'D3_G1_non_legal_occurrence': d3,
        'D4_generative_rules_per_1000_words': d4,
    }
    outp = os.path.join(RUNDIR, 'h-new-2800-diagnostics.json')
    with open(outp, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    manifest = {
        'finding_id': 'H-NEW-2800-DIAGNOSTICS',
        'status': 'POST-HOC',
        'utc': datetime.now(timezone.utc).isoformat(),
        'script': os.path.relpath(os.path.abspath(__file__), PROJECT),
        'script_sha256': sha256_file(os.path.abspath(__file__)),
        'frozen_inputs': {os.path.relpath(p, PROJECT): sha256_file(p)
                          for p in [QJSON, J2500, BUKHARI, PRIMARY_RUN]},
        'output': os.path.relpath(outp, PROJECT),
    }
    with open(os.path.join(RUNDIR, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    log(f'wrote {outp}')


if __name__ == '__main__':
    main()
