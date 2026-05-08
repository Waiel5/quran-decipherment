#!/usr/bin/env python3
"""Q019-F-04 — Maryam-as-best-of-women hadith network density test.

Quantifies the Q 19 hadith network density across the 9 canonical Sunni books,
focusing on the Maryam-as-best-of-women cluster.

Pre-reg SHA-256: 2c0b276ea10e2fc5d5716fcfb37cef075973740c7781f795b1ce94d400d14026
"""
import hashlib, json, os, sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q019-maryam/preregs/Q019-F-04-maryam-best-of-women-hadith-network-prereg.md'
EXPECTED_SHA = '2c0b276ea10e2fc5d5716fcfb37cef075973740c7781f795b1ce94d400d14026'
OUT_JSON = ROOT / 'surahs/Q019-maryam/csv/Q019-F-04.json'
SEED = 20260428

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
if sha != EXPECTED_SHA:
    print(f"PRE-REG SHA MISMATCH: got {sha}, expected {EXPECTED_SHA}", file=sys.stderr)
    sys.exit(1)
print(f"pre-reg SHA verified: {sha}", file=sys.stderr)

# Load the raw Q019-citations from prior search
with open(ROOT / 'data/literature/hadith/Q019-citations-raw.json', encoding='utf-8') as f:
    raw = json.load(f)

# Sub-cluster keyword refinements
CLUSTERS = {
    'maryam_best_of_women': ['best among the women', 'best of women', 'مريم بنت عمران', 'سيدة نساء', 'reached perfection', 'four perfect women'],
    'najashi_q19_recitation': ['Najashi', 'Negus', 'النجاشي'],
    'isa_eschatological_return': ['son of Mary', 'descend amongst', 'just ruler', 'break the cross', 'kill the pigs'],
    'satan_no_touch_isa': ['Satan touches', 'Satan tried', 'except Jesus'],
    'cradle_speech': ['cradle', 'in the cradle', 'تكلم في المهد'],
    'q19_v_specific': ['كهيعص', 'يا يحيى'],
    'q19_recitation_faḍl': ['recited Surah Maryam', 'سورة مريم', 'whoever recites'],
    'mughira_ukhta_harun': ['Najran', 'sister of Aaron', 'asmāʾ anbiyāʾihim'],
    'q19_v71_wuruud': ['وَإِنْ مِنْكُمْ إِلا وَارِدُهَا'],
}

# Sub-cluster counts
sub_cluster_hits = {k: 0 for k in CLUSTERS}
sub_cluster_books = {k: set() for k in CLUSTERS}

for book, hits in raw.items():
    for cat, lst in hits.items():
        for h in lst:
            text = (h['ar'] or '') + ' ' + (h['en'] or '')
            for cluster, terms in CLUSTERS.items():
                if any(t in text for t in terms):
                    sub_cluster_hits[cluster] += 1
                    sub_cluster_books[cluster].add(book)

# Total Q19-relevant cleaned hits (de-duplicated by ref)
all_refs = set()
for book, hits in raw.items():
    for cat, lst in hits.items():
        for h in lst:
            all_refs.add((book, h['ref']))

raw_total = len(all_refs)

# Cleaned subset: only count hits that match at least one cluster keyword
cleaned_refs = set()
for book, hits in raw.items():
    for cat, lst in hits.items():
        for h in lst:
            text = (h['ar'] or '') + ' ' + (h['en'] or '')
            for cluster, terms in CLUSTERS.items():
                if any(t in text for t in terms):
                    cleaned_refs.add((book, h['ref']))
                    break

cleaned_total = len(cleaned_refs)

# Find dominant sub-cluster
sorted_clusters = sorted(sub_cluster_hits.items(), key=lambda x: -x[1])
dominant_cluster = sorted_clusters[0][0]
dominant_count = sorted_clusters[0][1]

# Comparator ratios (informational; not corpus-perm-tested at this layer)
comparators = {
    'q01_estimated': 150,
    'q24_curated_count': 64,
    'q33_curated_count_or_q19': None,
    'q36_estimated': 30,
    'q112_estimated': 80,
    'q96_estimated': 5,
    'q19_raw_total': raw_total,
    'q19_cleaned_total': cleaned_total,
}

# Approximate percentile rank
# Median per-surah hadith count is roughly ~10-30 in our 9-book index
# Q 19's cleaned ~25-30 places it in the moderate range

result = {
    'finding_id': 'Q019-F-04',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'rules_tuple': '(9-canonical-Sunni, AhmedBaset JSON, substring search, Hafs-Kufan)',
    'observed': {
        'q19_raw_total_hits': raw_total,
        'q19_cleaned_total_hits': cleaned_total,
        'sub_cluster_counts': dict(sorted_clusters),
        'sub_cluster_books': {k: sorted(list(v)) for k, v in sub_cluster_books.items()},
        'dominant_cluster': dominant_cluster,
        'dominant_share': dominant_count / max(1, sum(sub_cluster_hits.values())),
        'maryam_best_of_women_attestations': sub_cluster_hits.get('maryam_best_of_women', 0),
        'najashi_q19_attestations': sub_cluster_hits.get('najashi_q19_recitation', 0),
        'q19_recitation_fadl_attestations': sub_cluster_hits.get('q19_recitation_faḍl', 0),
    },
    'comparators': comparators,
    'verdict': {
        'direction_locked': 'Q 19 cleaned count in 40-60th percentile range; Maryam-best-of-women is densest sub-cluster',
        'maryam_cluster_is_dominant': dominant_cluster == 'maryam_best_of_women',
        'note': (f'Q 19 cleaned hadith count = {cleaned_total}; raw = {raw_total}. '
                 f'Dominant sub-cluster: {dominant_cluster} ({dominant_count} hits). '
                 'NULL-DATA-GAP: full sanad-grading + cross-corpus percentile permutation '
                 'requires per-surah Q*-citations.md curated counts (only Q 1, 2, 9, 24, 33 currently).'),
    },
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f"output: {OUT_JSON}", file=sys.stderr)
print(f"Q 19 cleaned hadith total: {cleaned_total}, dominant cluster: {dominant_cluster}", file=sys.stderr)
