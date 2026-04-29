# Journal — `stats-rigor` agent, run 1

**Date:** 2026-04-12
**Agent:** `stats-rigor` (general-purpose, bg)
**Task:** Produce v1 of the project's Statistical Rigor Protocol — the null-model + multiple-comparisons methodology that every Phase A replication and Phase B novel finding will have to pass.
**Status:** Complete. Protocol checked in at `docs/statistical-rigor-protocol.md`.

## What I read first

- `docs/design.md` — project-wide spec; confirmed the `stats-rigor` agent is named in the roster and mandated by Phase B's acceptance criterion ("at least 5 patterns survive at least 2 null models").
- `docs/methodology.md` — counting-rules and orthography conventions. The `rules` tuple defined there is exactly the pre-registration unit I build on in the protocol.
- `README.md` — confirmed the replication-first framing.

No `quran-text/` data actually inspected; this run is pure methodology, not data analysis. The live `text-shape` investigation of the 82375/75563/64595 word-count discrepancy has not returned, so I deliberately avoided any claim that depends on an exact text length. Where the protocol needs a length (worked example §5.3), I flag it as "to be locked after text-shape returns."

## What I grounded the protocol in

1. **Witztum, Rips & Rosenberg 1994** (Statistical Science 9(3), 429–438) — the original Bible Codes paper.
2. **McKay, Bar-Natan, Bar-Hillel & Kalai 1999** (Statistical Science 14(2), 150–173) — the definitive refutation. Methodological gold standard. The four McKay-identified failure modes (word-form degrees of freedom, surrogate-text control failures, post-hoc metrics, post-hoc name lists) translate cleanly to the Quranic case and I built §§2–4 of the protocol around exactly these modes.
3. **Gelman & Loken 2013** — garden of forking paths; justification for mandatory pre-registration and forking-paths disclosure even for honest researchers.
4. **Benjamini & Hochberg 1995** — FDR correction.
5. **Holm 1979** — step-down FWER correction.
6. General stylometry / null-model literature (Baayen 2001, Kilgarriff 2005) for the word-shuffle, char-shuffle, and n-gram-Markov-surrogate tradition.

## Key design decisions

- **Five null models in increasing order of stringency (§1.1–1.5)** with an explicit decision tree (§1.6) mapping claim type to null. Every finding must pass *two* nulls from *different rows* of the tree. This is the direct analogue of McKay's "try a different surrogate and the miracle disappears" move.
- **Pre-registration is mandatory (§2.1)** and enforced by commit-hash citation. If pre-reg postdates results, the finding is demoted to exploratory and loses its p-value. This is the strongest defense against the forking-paths failure mode that, per Gelman & Loken, nails even honest researchers.
- **Three-tier multiple-comparison correction (§2.2)**: Bonferroni for small families, Holm-Bonferroni default for > 5, Benjamini-Hochberg FDR for ≥ 50. The "family" includes every test in the running test register, not just the ones that worked.
- **Mandatory garden-of-forking-paths disclosure section (§2.3)** in every finding write-up. Four sub-sections, all required, no empty sections accepted without human review.
- **Three-tier p-value thresholds (§3)**: replication / novel / "revolutionary," with robustness-under-alternative-rule-tuple as an explicit gate. This last gate — the claim must also hold under at least one alternative orthography or numbering — is specifically designed to kill Bible-Codes-style brittleness, and I expect it to kill most of the Code-19 family.
- **Red-flag list (§4)** of claims we reject before running the test, each tied to a specific historical failure mode.
- **Worked example (§5) on Day/Night word counts.** I picked the `al-yawm = 365` claim because it's well-known, attributed (Abdul-Razzaq Nawfal 1959 and follow-ups), and has an obvious hidden fork: *which inflection scope of the root ي-و-م do you count?* I sketched the 5×2 cell matrix (5 inflection scopes × {day, night}) the experiment must report, the two nulls (§1.3 word-bigram + §1.4 length-matched early hadith with quoted-Quran stripped), Holm correction over 20 tests (10 cells × 2 nulls), and a robustness requirement across orthography variants. I deliberately stopped short of running any counts — the data shape is not locked — and I also committed in advance to a guess about the outcome (most likely outcome: no cell survives), so the team can falsify my prior.

## Research-gap note

I flagged explicitly (§6) that **Quranic numerology has never been subjected to a McKay-style peer-reviewed refutation.** Most rebuttals are in Arabic-language religious-studies venues and don't use modern null-model methodology. This project's Phase A, if executed under this protocol, can produce a methodological-paper artifact that fills that gap. That should probably be an explicit deliverable the orchestrator tracks, not a side effect.

## What I did NOT do in this run

- Did not touch any raw text.
- Did not compute any surrogate corpus length, because `text-shape` hasn't returned.
- Did not build a test register file yet — that should be initialized at the start of Phase B, not now.
- Did not enumerate specific comparable-corpus sources beyond naming the candidate collections (Bukhari, Muslim, Muwatta, Mu'allaqat, Sira, Tabari). An actual acquisition run for these is a separate job, possibly for the `morph-data` agent or a new `corpus-control` agent.
- Did not write unit tests for the shuffler/surrogate tools yet — that belongs with `analysis/tools/` once the shape is locked.

## Next recommended work

1. **When `text-shape` returns,** lock the primary-corpus length for the 1.4 null and unit-test it.
2. **Start a Phase-B test register** (`findings/phase-b-hypotheses/test-register.md`) before any Phase B work begins, so the first hypothesis already has a k to divide against.
3. **Dispatch a `corpus-control` job** to acquire the comparable-corpus texts (early hadith + classical poetry + Sira) and strip quoted Quran. This is blocking on the stringent null model and has a long lead time.
4. **Write a standing `finding-template.md`** under `findings/` that already has the §7 checklist and the forking-paths disclosure section pre-stamped. Makes the protocol cheap to comply with.
5. **Stretch:** write up the methodological-paper draft (§6) as an outline in `docs/` so the citation is live from day one.
