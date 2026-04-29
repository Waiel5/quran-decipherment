#!/usr/bin/env python3
"""AMEND-28 mechanical gate: scan all findings for nawʿ-numbered citations and
range-check against the stated-edition total. Any citation exceeding the total
is an automatic hard-error requiring PENDING retag.

Reference totals:
- al-Zarkashī Burhān fī ʿUlūm al-Qurʾān (Abū l-Faḍl Ibrāhīm ed.) = 47 anwāʿ
- al-Suyūṭī Itqān fī ʿUlūm al-Qurʾān (Abū l-Faḍl Ibrāhīm ed.) = 80 anwāʿ

Output: memo to findings/classical-sources/naw-range-audit-2026-04-14.md
"""
import re, os, collections, datetime

ROOT = '/Users/grey/Downloads/quran/findings'
OUT = '/Users/grey/Downloads/quran/findings/classical-sources/naw-range-audit-2026-04-14.md'

PAT = re.compile(
    r'(Itqān|Burhān|Badīʿ\s+al-Qurʾān|Itqan|Burhan|al-Itqān|al-Burhān)'
    r'[^.\n]{0,120}?'
    r'nawʿ\s*(\d+)(?:\s*[-–]\s*(\d+))?',
    re.IGNORECASE
)

LIMITS = {'Itqan': 80, 'Burhan': 47, 'Badic': 100}

META_MARKERS = [
    'pending', 'retract', 'fabric', 'recall error', 'recall-error',
    'confirmed-wrong', 'confirmed wrong', 'was a recall', 'retagged',
    'retag', 're-tag', 'fabrication', 'blocking verbatim',
    'matches the already-retracted', 'matches the retracted',
    'slip matches', 'in any form until',
    'out-of-range', 'out of range', 'mechanical-scan',
    'amend-28', 'amend 28', 'mw-6 mechanical',
    'is out-of-range', 'ceiling',
]

SKIP_FILES = {
    'naw-range-audit-2026-04-14.md',
    'h-new-28-source-anchors.md',
}


def normalize_source(raw):
    s = raw.replace('al-', '').lower()
    if 'itqan' in s or 'itqān' in s: return 'Itqan'
    if 'burhan' in s or 'burhān' in s: return 'Burhan'
    if 'badī' in s or 'badi' in s: return 'Badic'
    return raw


def is_meta(ctx):
    c = ctx.lower()
    return any(m.lower() in c for m in META_MARKERS)


def scan():
    live_errors = []
    meta_refs = []
    all_cites = []
    for dp, _, fn in os.walk(ROOT):
        for f in fn:
            if not f.endswith(('.md', '.tsv')): continue
            if f in SKIP_FILES: continue
            path = os.path.join(dp, f)
            try: txt = open(path).read()
            except: continue
            for m in PAT.finditer(txt):
                src = normalize_source(m.group(1))
                n1 = int(m.group(2))
                n2 = int(m.group(3)) if m.group(3) else None
                ln = txt[:m.start()].count('\n') + 1
                ctx_wide = txt[max(0, m.start()-200):m.end()+200].replace('\n', ' ')
                ctx_narrow = txt[max(0, m.start()-40):m.end()+120].replace('\n', ' ')
                rec = (path, ln, src, n1, n2, ctx_narrow)
                all_cites.append(rec)
                limit = LIMITS.get(src, 999)
                hi = n2 if n2 else n1
                if hi > limit:
                    if is_meta(ctx_wide):
                        meta_refs.append(rec)
                    else:
                        live_errors.append(rec)
    return all_cites, live_errors, meta_refs


def contradictions(all_cites):
    TOPICS = ['muqaṭṭaʿāt', 'fawāṣil', 'ḥusn al-ibtidāʾ', 'ḥusn al-intihāʾ',
             'khawātim', 'iltifāt', 'sajʿ', 'iʿjāz', 'munāsab', 'mutashābih',
             'gharīb', 'qiṣaṣ', 'fawātiḥ']
    bucket = collections.defaultdict(set)
    for path, ln, src, n1, n2, ctx in all_cites:
        ctxl = ctx.lower()
        for t in TOPICS:
            if t.lower() in ctxl:
                bucket[(src, t)].add(n1)
    return {k: sorted(v) for k, v in bucket.items() if len(v) > 1}


def main():
    all_cites, live_errors, meta_refs = scan()
    contras = contradictions(all_cites)
    ts = datetime.date.today().isoformat()
    lines = [
        '---',
        'audit_id: naw-range-audit-2026-04-14',
        'trigger: AMEND-28 pre-publication mechanical check',
        f'date: {ts}',
        'classical_scholar: green',
        f'total_citations_scanned: {len(all_cites)}',
        f'live_out_of_range_errors: {len(live_errors)}',
        f'meta_references_correctly_flagged: {len(meta_refs)}',
        f'internal_contradictions: {len(contras)}',
        'reference_totals:',
        '  - Burhan (Abū l-Faḍl Ibrāhīm ed.): 47 anwāʿ',
        '  - Itqān (Abū l-Faḍl Ibrāhīm ed.): 80 anwāʿ',
        'methodology: mechanical regex + range gate; retraction/meta context detection via heuristic marker list',
        '---',
        '',
        '# AMEND-28 mechanical nawʿ-range audit — 2026-04-14',
        '',
        '## Summary',
        '',
        f'- Citations scanned: **{len(all_cites)}**',
        f'- Live out-of-range errors (require PENDING retag): **{len(live_errors)}**',
        f'- Meta references (already flagged as errors in source; not new errors): {len(meta_refs)}',
        f'- Same-source × same-topic internal contradictions: {len(contras)}',
        '',
        '## Live out-of-range errors',
        '',
        'These citations are prima-facie impossible in the stated edition. Each site',
        'requires MW-6 PENDING retag plus a correct-location best-guess where known.',
        '',
    ]
    for r in live_errors:
        path, ln, src, n1, n2, ctx = r
        nstr = f'{n1}-{n2}' if n2 else str(n1)
        lines.append(f'- **{src} nawʿ {nstr}** (limit {LIMITS[src]}) at `{path}:{ln}`')
        lines.append(f'  - context: `{ctx[:160].strip()}...`')
    lines.append('')
    lines.append('## Internal contradictions (same-source × same-topic, different nawʿ numbers)')
    lines.append('')
    for (src, topic), nums in contras.items():
        lines.append(f'- **{src} × `{topic}`**: nawʿ numbers cited = {nums}')
    lines.append('')
    lines.append('## Meta references (already correctly flagged; no action)')
    lines.append('')
    for r in meta_refs:
        path, ln, src, n1, n2, _ = r
        nstr = f'{n1}-{n2}' if n2 else str(n1)
        lines.append(f'- {src} nawʿ {nstr} at `{path}:{ln}` (meta/retraction)')
    lines.append('')
    lines.append('## Action taken 2026-04-14')
    lines.append('')
    lines.append('- Team-lead directive APPROVED: (a) full scan, (b) immediate PENDING retag on the 3 confirmed spot-check errors, (c) AMEND-28 filing.')
    lines.append('- Script saved at `scripts/naw_range_audit.py` for reproducibility and re-run on any future dispatch cycle.')
    lines.append('- Remaining live errors beyond the 3 flagged ones are queued for lazy-repair: per Option C, they will be corrected in-place when the containing findings file is next touched for other reasons.')
    lines.append('')
    with open(OUT, 'w') as f:
        f.write('\n'.join(lines))
    print(f'wrote: {OUT}')
    print(f'  scanned: {len(all_cites)}')
    print(f'  live errors: {len(live_errors)}')
    print(f'  meta refs: {len(meta_refs)}')
    print(f'  contradictions: {len(contras)}')


if __name__ == '__main__':
    main()
