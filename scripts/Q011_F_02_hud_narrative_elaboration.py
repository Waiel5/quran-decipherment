#!/usr/bin/env python3
"""Q011-F-02 — Hūd-narrative elaboration: Q 11:50-60 vs Q 7:65-72.

Pre-reg: surahs/Q011-hud/preregs/Q011-F-02-hud-narrative-elaboration-prereg.md
Pre-reg SHA256: b9073e1febe40f8da2db5b3b636658cb6ecd275d2691caa2415740d9e2add610
Rules-tuple: (no-tashkeel, orthographic-token, regex-word-boundary, QAC-v0.4-root,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, hashlib, sys, os, re

PREREG = '/Users/grey/Downloads/quran/surahs/Q011-hud/preregs/Q011-F-02-hud-narrative-elaboration-prereg.md'
EXPECTED_SHA = 'b9073e1febe40f8da2db5b3b636658cb6ecd275d2691caa2415740d9e2add610'

PUNCT_PATTERN = re.compile(r'[\s۞ۚۗۖۘۙ]+')
SPEECH_RE = re.compile(r'(?:^|\s)(قال|قالوا|قالت|قلنا|قل)(?=\s|$)')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def tokenize(text):
    return [t for t in PUNCT_PATTERN.split(text) if t]


def block_tokens(verses, lo, hi):
    """Return concatenated token list for verses[lo..hi] inclusive (1-indexed)."""
    selected = [v for v in verses if lo <= v['id'] <= hi]
    tokens = []
    for v in selected:
        tokens.extend(tokenize(v['text']))
    return selected, tokens


def block_speech_count(verses, lo, hi):
    selected = [v for v in verses if lo <= v['id'] <= hi]
    total = 0
    for v in selected:
        total += len(SPEECH_RE.findall(v['text']))
    return total, len(selected)


def parse_qac_roots(qac_path, surah, verses_filter):
    """Return set of distinct roots for tokens in (surah, verse in verses_filter)."""
    roots = set()
    with open(qac_path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]  # e.g., (1:1:1:1)
            features = parts[3]
            m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)', loc)
            if not m:
                continue
            sid = int(m.group(1)); vid = int(m.group(2))
            if sid != surah:
                continue
            if vid not in verses_filter:
                continue
            # Extract ROOT:xxx
            for f in features.split('|'):
                if f.startswith('ROOT:'):
                    roots.add(f[5:])
    return roots


def main():
    verify_sha()
    with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
        quran = json.load(f)
    q11 = next(s for s in quran if s['id'] == 11)
    q7 = next(s for s in quran if s['id'] == 7)

    # Block bounds (locked in pre-reg)
    Q11_LO, Q11_HI = 50, 60
    Q7_LO, Q7_HI = 65, 72

    # A. Verse counts (deterministic)
    q11_vv = sum(1 for v in q11['verses'] if Q11_LO <= v['id'] <= Q11_HI)
    q7_vv = sum(1 for v in q7['verses'] if Q7_LO <= v['id'] <= Q7_HI)

    # B. Token counts
    _, q11_toks = block_tokens(q11['verses'], Q11_LO, Q11_HI)
    _, q7_toks = block_tokens(q7['verses'], Q7_LO, Q7_HI)
    q11_tok_n = len(q11_toks)
    q7_tok_n = len(q7_toks)

    # C. Distinct-root counts
    qac_path = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
    q11_roots = parse_qac_roots(qac_path, 11, set(range(Q11_LO, Q11_HI+1)))
    q7_roots = parse_qac_roots(qac_path, 7, set(range(Q7_LO, Q7_HI+1)))
    q11_roots_n = len(q11_roots)
    q7_roots_n = len(q7_roots)

    # D. Direct-speech density (per verse)
    q11_speech, _ = block_speech_count(q11['verses'], Q11_LO, Q11_HI)
    q7_speech, _ = block_speech_count(q7['verses'], Q7_LO, Q7_HI)
    q11_speech_density = q11_speech / q11_vv if q11_vv else 0
    q7_speech_density = q7_speech / q7_vv if q7_vv else 0

    indicators = {
        'A_verses': q11_vv > q7_vv,
        'B_tokens': q11_tok_n > q7_tok_n,
        'C_roots': q11_roots_n > q7_roots_n,
        'D_speech_density': q11_speech_density > q7_speech_density,
    }
    n_passed = sum(indicators.values())
    if n_passed == 4:
        verdict = 'CONFIRMED'
    elif n_passed == 3:
        verdict = 'DIRECTIONAL'
    elif n_passed == 0:
        verdict = 'NULL — pre-commit-violation candidate (Q 11 less elaborated)'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q011-F-02',
        'prereg_sha': EXPECTED_SHA,
        'seed': 20260507,
        'rules_tuple': '(no-tashkeel, orthographic-token, regex-word-boundary, QAC-v0.4-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'q11_block': {'lo': Q11_LO, 'hi': Q11_HI},
        'q7_block': {'lo': Q7_LO, 'hi': Q7_HI},
        'axes': {
            'A_verses': {'q11': q11_vv, 'q7': q7_vv, 'q11_higher': indicators['A_verses']},
            'B_tokens': {'q11': q11_tok_n, 'q7': q7_tok_n, 'q11_higher': indicators['B_tokens']},
            'C_distinct_roots': {'q11': q11_roots_n, 'q7': q7_roots_n, 'q11_higher': indicators['C_roots']},
            'D_speech_density': {
                'q11_count': q11_speech, 'q11_per_verse': q11_speech_density,
                'q7_count': q7_speech, 'q7_per_verse': q7_speech_density,
                'q11_higher': indicators['D_speech_density'],
            },
        },
        'n_axes_q11_higher': n_passed,
        'verdict': verdict,
    }
    out_dir = '/Users/grey/Downloads/quran/surahs/Q011-hud/csv'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'Q011-F-02.json'), 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q011-F-02 verdict: {verdict} ({n_passed}/4)")
    for k, v in out['axes'].items():
        print(f"  {k}: {v}")


if __name__ == '__main__':
    main()
