# GRAMMAR-AT-RHYME audit. Each rhyme word: its grammatical role, its HEAD, agreement.
# All -ūn rhyme words are masc.sing.; check the head is masc.sing. (or rhyme is majrūr genitive m.s.)
rows = [
 (1, "al-maknūn", "khabar of ẓalla; ism=rasm-u-l-waḥy (m.s. nom->khabar accus al-maknūn-a)", "rasm (m.s.)", "OK — khabar ẓalla, masc sg"),
 (2, "al-maghbūn", "fāʿil of khāba (m.s.)", "(implied) al-maghbūn itself is fāʿil", "OK masc sg"),
 (3, "al-madfūn", "khabar of ẓalla; ism=al-durr (m.s.)", "al-durr (m.s.)", "OK"),
 (4, "al-maftūn", "naʿt/khabar; al-ʿaqlu...al-maftūn (m.s. def)", "al-ʿaql (m.s.)", "OK"),
 (5, "al-makhzūn", "mafʿūl bih of hijtu (m.s.)", "(obj) ", "OK — 'I stirred the stored[-hoard]'"),
 (6, "al-maʾmūn", "khabar/naʿt of al-dalīl (m.s.)", "al-dalīl (m.s.)", "OK"),
 (7, "al-maqrūn", "naʿt of al-sabīl (m.s., gen)", "al-sabīl (m.s.)", "OK (meter breaks though)"),
 (8, "al-mashḥūn", "fāʿil of ḍalla (m.s.)", "al-mashḥūn itself", "OK"),
 (9, "al-marhūn", "fāʿil of ʿazza (m.s.)", "al-marhūn itself", "OK"),
 (10,"mawḍūn", "naʿt of naẓm-un (m.s. indef)", "naẓm (m.s.)", "OK"),
 (11,"al-maḍmūn", "naʿt of al-bayān (m.s., gen) — 'ḥusni l-bayāni l-maḍmūn'", "al-bayān (m.s.)", "OK"),
 (12,"al-maṭʿūn", "khabar of al-bayān (m.s.)", "al-bayān (m.s.)", "OK (but ʿajuz meter breaks)"),
 (13,"mawhūn", "naʿt of laḥn-un (m.s. indef)", "laḥn (m.s.)", "OK"),
 (14,"al-marṣūn", "majrūr by ghayr (ghayru l-marṣūn) (m.s.)", "al-waṣl ... ghayru l-marṣūn", "OK"),
 (15,"al-maymūn", "naʿt of al-layl (m.s.)", "al-layl (m.s.)", "OK"),
 (16,"al-mawzūn", "fāʿil of iṭmaʾanna (m.s.)", "al-mawzūn itself", "OK"),
 (17,"al-maḍnūn", "khabar/naʿt of ḥimā-hu (m.s.) — 'ḥimāhu l-maḍnūn'", "ḥimā (m.s.)", "OK"),
 (18,"al-maḥṣūn", "naʿt of dhū l-bayān (m.s.) — 'wa-dhū l-bayāni l-maḥṣūn'", "dhū (m.s.)", "OK — see diction note"),
 (19,"maẓnūn", "khabar — 'fa-maqāluhum maẓnūn' (maqāl m.s.)", "maqāl (m.s.)", "OK — recast singularized head (was al-muddaʿūn PL). METER breaks though"),
 (20,"al-masjūn", "naʿt of al-lisān (m.s.) — 'ʿuqadu l-lisāni l-masjūn'? prompt: 'al-lisānu l-masjūn'", "al-lisān (m.s.)", "OK — number fixed (was al-ʿārifīn PL)"),
 (21,"al-madyūn", "khabar of yaẓalla; ism=al-lafẓ (m.s.)", "al-lafẓ (m.s.)", "OK grammar — DICTION flag"),
 (22,"al-maʾfūn", "naʿt of al-ḥisāb (m.s.) — 'wahmi l-ḥisābi l-maʾfūn'", "al-ḥisāb (m.s.)", "OK — number fixed (was al-qawm humu PL)"),
 (23,"(tāj)-an-nūn", "an-nūn=muḍāf ilayh; tāj (m.s.) fāʿil of inzawā", "tāj (m.s.)", "OK"),
 (24,"bi-mamnūn", "khabar laysa (majrūr bi-bāʾ zāʾida); ism laysa = al-lafẓ? 'fa-laysa bi-mamnūn'", "al-lafẓ/al-musammā (m.s.)", "OK grammar (DARB meter breaks)"),
 (25,"maskūn", "khabar of amsat? no—prompt recast: 'fa-ghadat kharāban maskūn'; maskūn naʿt of kharāb (m.s.)", "kharāb (m.s.)", "OK — gender fixed (was dār FEM)"),
 (26,"al-maṭḥūn", "naʿt of al-jabīn (m.s.)", "al-jabīn (m.s.)", "OK"),
 (27,"al-mawṭūn", "khabar of huwa (-> al-qarīḍ m.s.)", "al-qarīḍ (m.s.)", "OK grammar — DICTION note"),
 (28,"al-ʿurjūn", "naʿt of al-qadīm (m.s., gen)", "al-qadīm (m.s.)", "OK"),
 (29,"al-maḥzūn", "naʿt of al-gharīq (m.s.)", "al-gharīq (m.s.)", "OK"),
 (30,"maḥḍūn", "naʿt of badʾ-un (m.s.)", "badʾ (m.s.)", "OK"),
]
print(f"{'#':>3} {'rhyme':<14} {'head':<22} verdict")
for n,r,role,head,v in rows:
    print(f"{n:>3} {r:<14} {head:<22} {v}")
