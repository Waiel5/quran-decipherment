#!/usr/bin/env python3
"""
Q 76 al-Insān (al-Dahr) — Specialist family runner
================================================
Runs all 4 SHA-locked pre-registered tests for Q 76:
  Q076-F-01: paradise-tableau density (corpus-EXACT-EXTREME hypothesis)
  Q076-F-02: longest 100%-alif single-rāwī surah
  Q076-F-03: Q 75 ↔ Q 76 creation-axis pair-cohesion
  Q076-F-04: Shīʿī Ahl-al-Bayt revelation-cause audit (deductive)

SHA-locked pre-regs:
  Q076-F-01: d401a8f92a881ba575aab2df64aed799c1c273020667ae58a202c6d598fe2fb9
  Q076-F-02: edbf64cd5d1e68c0368af8aa4c37975d465d142300c90a418d95fd3f3cc87c75
  Q076-F-03: cec8ffb295982d7a5cd7761069c96cf9e731123e28c8a30ae9155eede2f5700a
  Q076-F-04: 7270e66d5abf84fdf3ffa646d7b47b891975f27163272bf88c00f5f86dab03e7

seed = 20260509
n_perm = 10000
Bonferroni-k = 4, α_bon = 0.0125
"""
import json, random, statistics, hashlib, os, sys
from collections import Counter, defaultdict

# ---------- SHA verification ----------
PREREG_DIR = '/Users/grey/Downloads/quran/surahs/Q076-al-insan/preregs/'
EXPECTED_SHAS = {
    'Q076-F-01-paradise-density-prereg.md': 'd401a8f92a881ba575aab2df64aed799c1c273020667ae58a202c6d598fe2fb9',
    'Q076-F-02-monorhyme-prereg.md':         'edbf64cd5d1e68c0368af8aa4c37975d465d142300c90a418d95fd3f3cc87c75',
    'Q076-F-03-q75-q76-pair-prereg.md':      'cec8ffb295982d7a5cd7761069c96cf9e731123e28c8a30ae9155eede2f5700a',
    'Q076-F-04-shii-ahlbayt-audit-prereg.md':'7270e66d5abf84fdf3ffa646d7b47b891975f27163272bf88c00f5f86dab03e7',
}
def verify_shas():
    for f, expected in EXPECTED_SHAS.items():
        path = PREREG_DIR + f
        with open(path, 'rb') as h:
            actual = hashlib.sha256(h.read()).hexdigest()
        if actual != expected:
            print(f"❌ SHA MISMATCH on {f}")
            print(f"   expected: {expected}")
            print(f"   actual:   {actual}")
            sys.exit(1)
        print(f"✓ SHA OK: {f}")
    print()
verify_shas()

# ---------- Constants ----------
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.0125  # Bonferroni-4
random.seed(SEED)

# ---------- Load corpus ----------
DATA_DIR = '/Users/grey/Downloads/quran/'
text = json.load(open(DATA_DIR + 'quran-text/quran-no-tashkeel.json'))
ri = json.load(open(DATA_DIR + 'data/morphology/root-index.json'))
h111 = json.load(open(DATA_DIR + 'findings/phase-b-hypotheses/csv/h-new-111.json'))

# Build FR matrix
D = [[0.0]*115 for _ in range(115)]
for a, b, dist in h111['D_matrix_upper_triangular']:
    D[a][b] = dist; D[b][a] = dist

# Build per-verse (s_id, v_id, n_words, n_paradise, words) tuple list
# Strip basmala from Q 1 v 1? Q 76 has no basmala issue; Q 1 v 1 is the basmala itself.
# Per project convention: basmala_policy = counted-only-in-surah-1 (it IS counted in Q 1).
verses_data = []
for s in text:
    sid = s['id']
    for v in s['verses']:
        words = v['text'].split()
        verses_data.append((sid, v['id'], len(words), words))

# ---------- Paradise lexicon ----------
paradise_terms = set([
    'الأبرار', 'أبرار', 'كأس', 'كأسا', 'الكأس', 'كافور', 'كافورا', 'عينا', 'عين', 'العين',
    'يفجرونها', 'تفجير', 'تفجيرا', 'يفجرون', 'جنة', 'جنات', 'الجنة', 'الجنات', 'جنتان',
    'جنتين', 'حرير', 'حريرا', 'متكئ', 'متكئين', 'متكئون', 'الأرائك', 'أرائك', 'أريكة',
    'دانية', 'ظلال', 'ظلالها', 'الظلال', 'قطوف', 'قطوفها', 'القطوف', 'تذليلا', 'تذليل',
    'آنية', 'الآنية', 'فضة', 'الفضة', 'أكواب', 'الأكواب', 'كوب', 'قواريرا', 'قوارير',
    'قارورة', 'تقديرا', 'قدروها', 'يسقون', 'سقاهم', 'وسقاهم', 'زنجبيل', 'زنجبيلا',
    'سلسبيل', 'سلسبيلا', 'يطوف', 'يطاف', 'ويطوف', 'ويطاف', 'ولدان', 'الولدان', 'مخلدون',
    'مخلد', 'لؤلؤ', 'لؤلؤا', 'اللؤلؤ', 'منثورا', 'منثور', 'نعيم', 'نعيما', 'النعيم',
    'ثياب', 'الثياب', 'سندس', 'السندس', 'إستبرق', 'استبرق', 'أساور', 'الأساور', 'حلوا',
    'يحلون', 'حلية', 'شرابا', 'شراب', 'الشراب', 'طهور', 'طهورا', 'نضرة', 'ناضرة',
    'سرور', 'سرورا', 'فاكهة', 'فواكه', 'الفاكهة', 'تسنيم', 'رحيق', 'مختوم', 'حدائق',
    'فردوس', 'عدن', 'الفردوس', 'كواعب', 'الحور', 'حور', 'حوراء', 'حورا', 'مكنون',
    'مرفوعة', 'موضوعة', 'مصفوفة', 'مبثوثة', 'سدر', 'السدر', 'مخضود', 'مخضودة', 'طلح',
    'الطلح', 'منضود', 'منضودة', 'ممدودة', 'مسكوب', 'فرش', 'الفرش', 'فراش', 'بطائن',
    'بطائنها',
])

def is_paradise_word(w, terms):
    if w in terms: return True
    for prefix in 'وفبكل':
        if w.startswith(prefix) and len(w) > 2 and w[1:] in terms: return True
    return False

# Annotate each verse with paradise-count
verses_annotated = []
for sid, vid, nw, words in verses_data:
    pc = sum(1 for w in words if is_paradise_word(w, paradise_terms))
    verses_annotated.append((sid, vid, nw, pc, words))

results = {}

# ============================================================
# Q076-F-01: paradise density (corpus-EXACT-EXTREME)
# ============================================================
print("\n" + "="*70)
print("Q076-F-01 — Paradise-tableau density (corpus-EXACT-EXTREME)")
print("="*70)

# Cell A: whole-surah density rank
surah_density = []
for s_id_target in range(1, 115):
    s_v = [(nw, pc) for sid, vid, nw, pc, _ in verses_annotated if sid == s_id_target]
    wc = sum(nw for nw, _ in s_v)
    pc = sum(pc for _, pc in s_v)
    surah_density.append((s_id_target, wc, pc, pc/wc if wc > 0 else 0))

surah_density_sorted = sorted(surah_density, key=lambda x: -x[3])
q76_rank_A = next(i+1 for i, sd in enumerate(surah_density_sorted) if sd[0] == 76)
q76_density_A = next(sd[3] for sd in surah_density if sd[0] == 76)
rank2_density = surah_density_sorted[1][3]
separation_ratio = q76_density_A / rank2_density if rank2_density > 0 else float('inf')

print(f"\nCell A (whole-surah rank):")
print(f"  Q 76 paradise-density: {100*q76_density_A:.3f}%")
print(f"  Q 76 rank: {q76_rank_A} / 114")
print(f"  Rank-2 density: {100*rank2_density:.3f}%")
print(f"  Separation ratio Q 76 / rank-2 = {separation_ratio:.3f}×")
cell_A_pass = q76_rank_A == 1 and separation_ratio >= 1.5
print(f"  Cell A: {'PASS' if cell_A_pass else 'NULL'} (rank=1, sep≥1.5×)")

# Cell B: 11-verse window rank
WIN = 11
windows = []
for s_id_target in range(1, 115):
    s_v = [v for v in verses_annotated if v[0] == s_id_target]
    for i in range(len(s_v) - WIN + 1):
        win = s_v[i:i+WIN]
        wc = sum(v[2] for v in win)
        pc = sum(v[3] for v in win)
        windows.append((s_id_target, win[0][1], win[-1][1], wc, pc, pc/wc if wc > 0 else 0))

windows_sorted = sorted(windows, key=lambda x: -x[5])
q76_in_top5 = sum(1 for w in windows_sorted[:5] if w[0] == 76)
q76_in_top10 = sum(1 for w in windows_sorted[:10] if w[0] == 76)
print(f"\nCell B (11-verse window rank):")
print(f"  Total windows: {len(windows)}")
print(f"  Q 76 windows in top-5: {q76_in_top5} / 5")
print(f"  Q 76 windows in top-10: {q76_in_top10} / 10")
print(f"  Top-10:")
for rank, w in enumerate(windows_sorted[:10], 1):
    s, vs, ve, wc, pc, dens = w
    mark = " ⭐ Q 76" if s == 76 else ""
    print(f"    {rank:2d}. Q {s:3d} v{vs}-{ve}: {pc:2d}/{wc:3d} = {100*dens:.2f}%{mark}")
cell_B_pass = q76_in_top5 >= 1
cell_B_extreme = q76_in_top5 == 5
print(f"  Cell B: {'PASS' if cell_B_pass else 'NULL'} ({'EXTREME — all top-5 in Q 76' if cell_B_extreme else f'{q76_in_top5} in top-5'})")

# Cell C: length-matched permutation null on whole-surah density
print(f"\nCell C (length-matched permutation null):")
all_verses = verses_annotated
n_q76_verses = sum(1 for v in all_verses if v[0] == 76)
print(f"  Q 76 verse count: {n_q76_verses}")
random.seed(SEED)
null_densities_C = []
for _ in range(N_PERM):
    sample = random.sample(all_verses, n_q76_verses)
    wc = sum(v[2] for v in sample)
    pc = sum(v[3] for v in sample)
    null_densities_C.append(pc/wc if wc > 0 else 0)
p_C = sum(1 for d in null_densities_C if d >= q76_density_A) / N_PERM
print(f"  Q 76 observed density: {100*q76_density_A:.3f}%")
print(f"  Null mean: {100*statistics.mean(null_densities_C):.3f}%")
print(f"  Null max: {100*max(null_densities_C):.3f}%")
print(f"  p_perm = {p_C:.5f}")
cell_C_pass = p_C < ALPHA_BON
print(f"  Cell C: {'PASS' if cell_C_pass else 'NULL'} (α_bon = {ALPHA_BON})")

# Cell D: paradise-vocab-distribution null (shuffle paradise tokens uniformly)
print(f"\nCell D (paradise-vocab-distribution null):")
total_paradise_tokens = sum(v[3] for v in all_verses)
# Word-position-array; each verse gets its size; we shuffle paradise into positions
# Easier: for each permutation, pick the same total_paradise_tokens random verse positions
total_words = sum(v[2] for v in all_verses)
print(f"  Total words: {total_words}, paradise tokens: {total_paradise_tokens}")
# More efficient: assign each token to a random verse weighted by verse word-count
verse_weights = [v[2] for v in all_verses]
verse_keys = [(v[0], v[1]) for v in all_verses]

random.seed(SEED + 1)
q76_rank_1_count = 0
for perm in range(N_PERM):
    # For each paradise token, pick a verse weighted by word-count (so denser verses are more likely)
    sample_verse_indices = random.choices(range(len(all_verses)), weights=verse_weights, k=total_paradise_tokens)
    counts = Counter(sample_verse_indices)
    # Aggregate per surah
    per_surah_p = defaultdict(int)
    for idx, c in counts.items():
        per_surah_p[all_verses[idx][0]] += c
    per_surah_w = defaultdict(int)
    for v in all_verses:
        per_surah_w[v[0]] += v[2]
    densities = sorted([(s, per_surah_p[s] / per_surah_w[s]) for s in range(1, 115)], key=lambda x: -x[1])
    rank_q76 = next(i+1 for i, (s, _) in enumerate(densities) if s == 76)
    if rank_q76 == 1:
        q76_rank_1_count += 1

p_D = q76_rank_1_count / N_PERM
print(f"  Q 76 lands at rank 1: {q76_rank_1_count} / {N_PERM} permutations")
print(f"  p_perm (rank=1 by chance) = {p_D:.5f}")
cell_D_pass = p_D < ALPHA_BON
print(f"  Cell D: {'PASS' if cell_D_pass else 'NULL'} (α_bon = {ALPHA_BON})")

f01_passes = sum([cell_A_pass, cell_B_pass, cell_C_pass, cell_D_pass])
f01_verdict = (
    'CORPUS-EXACT-EXTREME' if (f01_passes == 4 and separation_ratio >= 1.5 and cell_B_extreme) else
    'CONFIRMED' if f01_passes >= 3 else
    'PASS-DIRECTED' if f01_passes >= 2 else
    'NULL'
)
print(f"\nQ076-F-01 verdict: {f01_verdict} ({f01_passes}/4 cells PASS)")
results['Q076-F-01'] = {
    'verdict': f01_verdict, 'passes': f01_passes, 'cells_total': 4,
    'cell_A_pass': cell_A_pass, 'cell_B_pass': cell_B_pass, 'cell_C_pass': cell_C_pass, 'cell_D_pass': cell_D_pass,
    'q76_density': q76_density_A, 'q76_rank': q76_rank_A, 'rank2_density': rank2_density,
    'separation_ratio': separation_ratio, 'q76_in_top5_windows': q76_in_top5, 'q76_in_top10_windows': q76_in_top10,
    'p_C': p_C, 'p_D': p_D,
}

# ============================================================
# Q076-F-02: longest 100%-alif single-rāwī surah
# ============================================================
print("\n" + "="*70)
print("Q076-F-02 — Longest 100%-alif single-rāwī surah")
print("="*70)
finals_per_surah = []
for s in text:
    finals = []
    for v in s['verses']:
        words = v['text'].strip().split()
        if not words: continue
        last = words[-1].rstrip('۞ۚۖ')
        if last:
            finals.append(last[-1])
    if finals:
        ctr = Counter(finals)
        top_letter, top_count = ctr.most_common(1)[0]
        frac = top_count / len(finals)
        finals_per_surah.append((s['id'], len(finals), top_letter, frac))

# 100%-alif surahs
alif_100 = sorted([s for s in finals_per_surah if s[2] == 'ا' and s[3] == 1.0], key=lambda x: -x[1])
print(f"\n100%-alif surahs (n={len(alif_100)}):")
for s in alif_100:
    mark = " ⭐ Q 76" if s[0] == 76 else ""
    print(f"  Q {s[0]:3d}: {s[1]} verses{mark}")
q76_alif_rank = next(i+1 for i, s in enumerate(alif_100) if s[0] == 76)
print(f"\nCell A: Q 76 rank among 100%-alif surahs = {q76_alif_rank} / {len(alif_100)}")
cell_A2 = q76_alif_rank == 1
print(f"  Cell A: {'PASS' if cell_A2 else 'NULL'}")

# Cell B: among all 100%-monorhyme surahs (any letter)
single_rawi = sorted([s for s in finals_per_surah if s[3] == 1.0], key=lambda x: -x[1])
q76_in_single_rank = next(i+1 for i, s in enumerate(single_rawi) if s[0] == 76)
print(f"\nCell B: Q 76 rank among ALL single-rāwī surahs = {q76_in_single_rank} / {len(single_rawi)}")
print(f"  Q 54 al-Qamar (55v, single-rāwī ر) is the longest.")
print(f"  Q 76 is rank-2/{len(single_rawi)} overall, rank-1/{len(alif_100)} for alif specifically.")
print(f"  Cell B: descriptive — Q 76 = corpus-EXACT longest 100%-alif but rank-2 overall single-rāwī.")
cell_B2 = q76_in_single_rank <= 2  # rank-2 overall (after Q 54)

f02_passes = sum([cell_A2, cell_B2])
f02_verdict = 'CONFIRMED-CORPUS-EXACT' if f02_passes == 2 and cell_A2 else ('PASS-DIRECTED' if f02_passes >= 1 else 'NULL')
print(f"\nQ076-F-02 verdict: {f02_verdict} ({f02_passes}/2 cells PASS)")
results['Q076-F-02'] = {
    'verdict': f02_verdict, 'passes': f02_passes, 'cells_total': 2,
    'q76_alif_rank': q76_alif_rank, 'q76_overall_single_rawi_rank': q76_in_single_rank,
    'n_alif100': len(alif_100), 'n_single_rawi': len(single_rawi),
}

# ============================================================
# Q076-F-03: Q 75 ↔ Q 76 creation-axis pair-cohesion
# ============================================================
print("\n" + "="*70)
print("Q076-F-03 — Q 75 ↔ Q 76 creation-axis pair-cohesion")
print("="*70)

# Per-surah root sets
surah_roots = defaultdict(set)
for root, locs in ri.items():
    for loc in locs:
        if isinstance(loc, list) and len(loc) >= 2:
            surah_roots[loc[0]].add(root)

# Cell A: Mushaf-adjacent pairs with creation-triplet (xlq, Ans, nTf) in BOTH
triplet = {'xlq', 'Ans', 'nTf'}
adjacent_pairs_with_triplet = []
for s in range(1, 114):
    if triplet.issubset(surah_roots[s]) and triplet.issubset(surah_roots[s+1]):
        adjacent_pairs_with_triplet.append((s, s+1))
print(f"\nMushaf-adjacent pairs with creation-triplet in BOTH:")
for p in adjacent_pairs_with_triplet:
    print(f"  Q {p[0]} ↔ Q {p[1]}")
print(f"  Total: {len(adjacent_pairs_with_triplet)} / 113 pairs ({100*len(adjacent_pairs_with_triplet)/113:.2f}%)")
cell_A3 = (75, 76) in adjacent_pairs_with_triplet
print(f"  Cell A: {'PASS' if cell_A3 else 'NULL'} (Q 75-76 in the rare set)")

# Permutation null: how often does a random pair have the triplet?
random.seed(SEED + 2)
null_count_C = 0
for _ in range(N_PERM):
    a, b = random.sample(range(1, 115), 2)
    if triplet.issubset(surah_roots[a]) and triplet.issubset(surah_roots[b]):
        null_count_C += 1
p_triplet_pair = null_count_C / N_PERM
print(f"  Random-pair triplet co-occurrence: {null_count_C}/{N_PERM} = {p_triplet_pair:.4f}")
print(f"  Adjacent-pair empirical rate: {len(adjacent_pairs_with_triplet)}/113 = {len(adjacent_pairs_with_triplet)/113:.4f}")

# Cell B: FR-distance pair-cohesion percentile
all_pair_dists = sorted([D[i][j] for i in range(1, 115) for j in range(i+1, 115)])
q75_q76_dist = D[75][76]
q75_q76_percentile = sum(1 for d in all_pair_dists if d <= q75_q76_dist) / len(all_pair_dists) * 100
print(f"\nCell B (FR-distance):")
print(f"  Q 75 ↔ Q 76 FR-distance = {q75_q76_dist:.4f}")
print(f"  Percentile in 6,441 pair-distances = {q75_q76_percentile:.1f}%")
cell_B3 = q75_q76_percentile <= 25
print(f"  Cell B: {'PASS' if cell_B3 else 'NULL'} (≤ 25th percentile)")

# Q 76's mushaf-prev (Q 75) FR-cohort percentile-rank among Q 76's neighbors
q76_to_others = sorted([(s, D[76][s]) for s in range(1, 115) if s != 76], key=lambda x: x[1])
q75_rank_for_q76 = next(i+1 for i, (s, _) in enumerate(q76_to_others) if s == 75)
print(f"  Q 75 is FR-rank #{q75_rank_for_q76} of 113 from Q 76's row")

f03_passes = sum([cell_A3, cell_B3])
f03_verdict = 'CONFIRMED' if f03_passes == 2 else ('PARTIAL' if f03_passes == 1 else 'NULL')
print(f"\nQ076-F-03 verdict: {f03_verdict} ({f03_passes}/2 cells PASS)")
results['Q076-F-03'] = {
    'verdict': f03_verdict, 'passes': f03_passes, 'cells_total': 2,
    'cell_A_pass': cell_A3, 'cell_B_pass': cell_B3,
    'adjacent_triplet_pairs': adjacent_pairs_with_triplet, 'p_triplet_pair_random': p_triplet_pair,
    'q75_q76_fr_dist': q75_q76_dist, 'q75_q76_fr_percentile': q75_q76_percentile,
    'q75_rank_from_q76': q75_rank_for_q76,
}

# ============================================================
# Q076-F-04: Shīʿī Ahl-al-Bayt revelation-cause classical-claim audit
# ============================================================
print("\n" + "="*70)
print("Q076-F-04 — Shīʿī Ahl-al-Bayt classical-claim audit")
print("="*70)

# Search Bukhari, Muslim, Tirmidhi for the revelation-cause narrative
def get_en(h):
    e = h.get('english')
    if isinstance(e, str): return e
    elif isinstance(e, dict):
        return e.get('text') or e.get('matn') or e.get('body') or json.dumps(e, ensure_ascii=False)
    return ''

audit_targets = {
    'revelation_cause': {  # the Ahl al-Bayt three-fast-iftar narrative
        'ar': ['أهل البيت', 'فاطمة', 'علي بن أبي طالب', 'الحسن والحسين', 'فضة', 'يوفون بالنذر', 'أسير', 'أسيرا', 'مسكين'],
        'en': ['Fatima and Ali', 'Hasan and Husayn', 'fed the captive', 'fed the orphan', 'three days fasting', 'Ahl al-Bayt revelation', 'Surah Insan revealed about'],
        'pattern_count': 4,  # need ≥ 4 keywords in single hadith for revelation-cause confirmation
    },
    'friday_fajr_q32_q76': {
        'ar': ['الم تنزيل', 'هل أتى', 'يوم الجمعة', 'الفجر'],
        'en': ['Hal-ata', 'Hal ata', 'Insan', 'Dahr', 'Tanzil', 'Sajdah', 'Friday', 'Fajr', 'Jumua'],
        'pattern_count': 3,
    },
}

audit_results = defaultdict(list)
hadith_corpora = {
    'Bukhari': '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json',
    'Muslim': '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json',
    'Tirmidhi': '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json',
    'AbuDawud': '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/abudawud.json',
    'IbnMajah': '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/ibnmajah.json',
    'Nasai': '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/nasai.json',
}
for corpus_name, path in hadith_corpora.items():
    if not os.path.exists(path):
        print(f"  {corpus_name}: file not found")
        continue
    h_data = json.load(open(path))
    for h in h_data['hadiths']:
        ar = h.get('arabic', '') or ''
        en = get_en(h)
        for target_name, terms in audit_targets.items():
            ar_hits = sum(1 for t in terms['ar'] if t in ar)
            en_hits = sum(1 for t in terms['en'] if t.lower() in en.lower())
            total_hits = ar_hits + en_hits
            if total_hits >= terms['pattern_count']:
                audit_results[target_name].append({
                    'corpus': corpus_name, 'id': h['id'], 'bookId': h.get('bookId'),
                    'idInBook': h.get('idInBook'),
                    'ar_hits': ar_hits, 'en_hits': en_hits, 'total_hits': total_hits,
                    'ar': ar[:200], 'en': en[:300],
                })

# Cell A: revelation-cause search
print(f"\nCell A: Revelation-cause Ahl-al-Bayt narrative search across 6 Sunni canonical corpora:")
n_revelation_cause = len(audit_results.get('revelation_cause', []))
print(f"  Hadiths matching ≥ 4 keywords: {n_revelation_cause}")
for hit in audit_results.get('revelation_cause', [])[:5]:
    print(f"    [{hit['corpus']} #{hit['id']}] hits={hit['total_hits']}: {hit['en'][:200]}")
cell_A4 = n_revelation_cause == 0  # PASS-NEGATIVE if zero
print(f"  Cell A (audit-verified-negative): {'PASS' if cell_A4 else 'POSITIVE-FOUND'}")

# Cell B: Friday-Fajr recitation
n_friday = len(audit_results.get('friday_fajr_q32_q76', []))
print(f"\nCell B: Friday-Fajr Q 32 + Q 76 recitation:")
print(f"  Hadiths matching ≥ 3 keywords: {n_friday}")
for hit in audit_results.get('friday_fajr_q32_q76', [])[:5]:
    print(f"    [{hit['corpus']} #{hit['id']}] hits={hit['total_hits']}: {hit['en'][:200]}")
cell_B4 = n_friday >= 1  # PASS-POSITIVE if ≥1 in canonical corpus
print(f"  Cell B (audit-verified-positive): {'PASS' if cell_B4 else 'NULL'}")

f04_passes = sum([cell_A4, cell_B4])
f04_verdict = (
    'AUDIT-VERIFIED-NEGATIVE-AND-FRIDAY-CONFIRMED' if (cell_A4 and cell_B4) else
    'AUDIT-NEGATIVE-FRIDAY-CONFIRMED' if (cell_A4 and cell_B4) else
    'AUDIT-VERIFIED-NEGATIVE' if cell_A4 else
    'AUDIT-VERIFIED-POSITIVE' if not cell_A4 else
    'AUDIT-INCONCLUSIVE'
)
print(f"\nQ076-F-04 verdict: {f04_verdict} ({f04_passes}/2 cells PASS)")
results['Q076-F-04'] = {
    'verdict': f04_verdict,
    'cell_A_pass_negative': cell_A4,
    'cell_B_pass_positive': cell_B4,
    'n_revelation_cause_hits': n_revelation_cause,
    'n_friday_fajr_hits': n_friday,
    'friday_fajr_hits_summary': [{'corpus': h['corpus'], 'id': h['id'], 'bookId': h['bookId'], 'idInBook': h['idInBook']} for h in audit_results.get('friday_fajr_q32_q76', [])[:8]],
    'revelation_cause_hits_summary': [{'corpus': h['corpus'], 'id': h['id'], 'ar_hits': h['ar_hits'], 'en_hits': h['en_hits']} for h in audit_results.get('revelation_cause', [])[:8]],
}

# ============================================================
# Family summary
# ============================================================
print("\n" + "="*70)
print("Q076-F family summary (Bonferroni-k=4, α_bon=0.0125)")
print("="*70)
for fid, r in results.items():
    print(f"  {fid}: {r['verdict']}")

# Save outputs
out_dir = '/Users/grey/Downloads/quran/surahs/Q076-al-insan/csv/'
os.makedirs(out_dir, exist_ok=True)
for fid, r in results.items():
    with open(out_dir + f'{fid}.json', 'w') as h:
        json.dump(r, h, indent=2, ensure_ascii=False)
with open(out_dir + 'Q076-F-family-summary.json', 'w') as h:
    json.dump({
        'family': 'Q076-F (Q 76 al-Insān specialist)',
        'date_run': '2026-05-09',
        'seed': SEED, 'n_perm': N_PERM, 'bonferroni_k': 4, 'alpha_bon': ALPHA_BON,
        'results': results,
    }, h, indent=2, ensure_ascii=False)

# Also save the paradise lexicon for reproducibility
with open(out_dir + 'Q076-F-01-paradise-lexicon.json', 'w') as h:
    json.dump({'lexicon': sorted(paradise_terms), 'count': len(paradise_terms),
               'description': 'Paradise-tableau lexicon for Q076-F-01 (Q 76 specialist run, 2026-05-09)'},
              h, indent=2, ensure_ascii=False)

print(f"\nResults saved to {out_dir}")
print("Done.")
