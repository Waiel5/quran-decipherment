#!/usr/bin/env python3
"""Q024-F-04: Q 24:30-31 vs Q 33:53-59 lexical comparison."""
import re, json, hashlib, os
from collections import Counter

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-04-hijab-passages-comparison-prereg.md"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-04.json"

sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()

# Parse QAC roots per (s,v)
verses_roots = {}
verses_lemmas = {}
verses_tokens = {}
with open(f'{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('('): continue
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)\s+(\S+)\s+(\S+)\s+(.*)', line)
        if not m: continue
        s, v = int(m.group(1)), int(m.group(2))
        feat = m.group(7)
        rm = re.search(r'ROOT:([^|\s]+)', feat)
        lm = re.search(r'LEM:([^|\s]+)', feat)
        verses_roots.setdefault((s, v), Counter())
        verses_tokens[(s, v)] = verses_tokens.get((s, v), 0) + 1
        if rm:
            verses_roots[(s, v)][rm.group(1)] += 1
        if lm:
            verses_lemmas.setdefault((s, v), Counter())[lm.group(1)] += 1


def aggregate(scope):
    roots = Counter()
    lemmas = Counter()
    tokens = 0
    for k in scope:
        for r, c in verses_roots.get(k, {}).items():
            roots[r] += c
        for l, c in verses_lemmas.get(k, {}).items():
            lemmas[l] += c
        tokens += verses_tokens.get(k, 0)
    return roots, lemmas, tokens


q24_scope = [(24, 30), (24, 31)]
q33_scope = [(33, v) for v in range(53, 60)]

q24_roots, q24_lemmas, q24_tokens = aggregate(q24_scope)
q33_roots, q33_lemmas, q33_tokens = aggregate(q33_scope)

# Jaccard on root-set
shared = set(q24_roots) & set(q33_roots)
union = set(q24_roots) | set(q33_roots)
jac_roots = len(shared) / len(union) if union else 0.0

# Modesty-specific root presence
HJB = 'Hjb'  # ḥijāb
XMR = 'xmr'  # khimār
Q24_has_xmr = q24_roots.get(XMR, 0) > 0
Q33_has_xmr = q33_roots.get(XMR, 0) > 0
Q24_has_Hjb = q24_roots.get(HJB, 0) > 0
Q33_has_Hjb = q33_roots.get(HJB, 0) > 0

# Direction verdicts
if jac_roots < 0.30:
    verdict_A = 'CONFIRMED'
elif jac_roots < 0.50:
    verdict_A = 'DIRECTIONAL'
else:
    verdict_A = 'NULL'

verdict_B = 'CONFIRMED' if (Q24_has_xmr and not Q33_has_xmr) else ('NULL' if (not Q24_has_xmr or Q33_has_xmr) else 'DIRECTIONAL')
verdict_C = 'CONFIRMED' if (Q33_has_Hjb and not Q24_has_Hjb) else ('NULL' if (not Q33_has_Hjb or Q24_has_Hjb) else 'DIRECTIONAL')

# Modesty-related root inventory
MODESTY_ROOTS = ['gDD', 'xmr', 'jyb', 'Hjb', 'zyn', 'frj', 'HfZ', 'ndY',
                 'jlb', 'nks', 'sbl', 'byt', 'btr', 'b<l', 'Eyr', 'Eyn']
modesty_table = {}
for r in MODESTY_ROOTS:
    modesty_table[r] = {
        'q24_30_31': q24_roots.get(r, 0),
        'q33_53_59': q33_roots.get(r, 0),
    }

result = {
    'finding_id': 'Q024-F-04',
    'pre_reg_sha256': sha,
    'q24_30_31_distinct_roots': len(q24_roots),
    'q24_30_31_total_root_tokens': sum(q24_roots.values()),
    'q33_53_59_distinct_roots': len(q33_roots),
    'q33_53_59_total_root_tokens': sum(q33_roots.values()),
    'jaccard_root_overlap': jac_roots,
    'shared_roots': sorted(shared),
    'q24_only_roots': sorted(set(q24_roots) - set(q33_roots)),
    'q33_only_roots': sorted(set(q33_roots) - set(q24_roots)),
    'verdict_A_lexical_distinct': verdict_A,
    'verdict_B_xmr_only_q24': verdict_B,
    'verdict_C_Hjb_only_q33': verdict_C,
    'modesty_root_inventory': modesty_table,
    'overall_verdict': verdict_A if (verdict_A == verdict_B == verdict_C)
        else f'A:{verdict_A}/B:{verdict_B}/C:{verdict_C}',
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, default=str, ensure_ascii=False)

print(json.dumps({k: v for k, v in result.items() if k != 'modesty_root_inventory' and 'roots' not in k},
                 indent=2, default=str))
print(f"\nXmr-only-Q24: {Q24_has_xmr} (and Q33 has xmr: {Q33_has_xmr})")
print(f"Hjb-only-Q33: {Q33_has_Hjb} (and Q24 has Hjb: {Q24_has_Hjb})")
print(f"\nFull output written to {OUT}")
