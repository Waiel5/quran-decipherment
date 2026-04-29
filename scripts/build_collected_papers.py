#!/usr/bin/env python3
"""Build COLLECTED-PAPERS.md by concatenating findings files with TOC + title page."""
import os
import re
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
FINDINGS = ROOT / "findings"
OUT = ROOT / "COLLECTED-PAPERS.md"
DATE = "2026-04-12"

# Files to exclude (in-flight with other agents, or csv, or special)
EXCLUDE_NAMES = {
    "verse-commentaries-top500.md",  # being written by parallel agent
    "per-verse-annotations.md",      # 983 KB, verse-by-verse data table — keep out of collected
}

# Canonical ordering: top-level synthesis, then phase-a, phase-b, phase-c
def gather_files():
    sections = []

    # Top-level synthesis files
    top_level_order = [
        "scholar-commentary.md",
        "convergence-analysis.md",
        "classical-cross-references.md",
        "intra-quranic-cross-references.md",
        "balagha-mapping.md",
        "deep-hypotheses-queue.md",
        "khawatim-al-hashr-analysis.md",
        "verse-signature-atlas-highlights.md",
        "the-perfect-flow-essay.md",
    ]
    top = []
    for name in top_level_order:
        p = FINDINGS / name
        if p.exists() and name not in EXCLUDE_NAMES:
            top.append(p)
    sections.append(("Part I — Synthesis and Cross-Cutting Studies", top))

    # Phase A
    a_dir = FINDINGS / "phase-a-replications"
    a_files = sorted([p for p in a_dir.glob("*.md") if p.name not in EXCLUDE_NAMES])
    sections.append(("Part II — Phase A: Replication Audits", a_files))

    # Phase B
    b_dir = FINDINGS / "phase-b-hypotheses"
    b_files = sorted([p for p in b_dir.glob("*.md") if p.name not in EXCLUDE_NAMES])
    sections.append(("Part III — Phase B: Novel Hypotheses", b_files))

    # Phase C
    c_dir = FINDINGS / "phase-c-structures"
    c_files = sorted([p for p in c_dir.glob("*.md") if p.name not in EXCLUDE_NAMES])
    sections.append(("Part IV — Phase C: Structural Deep Dives", c_files))

    return sections

def slugify(name):
    """Make a markdown anchor slug."""
    s = name.lower().replace(".md", "")
    s = re.sub(r"[^a-z0-9\-]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def word_count(text):
    return len(re.findall(r"\S+", text))

def main():
    sections = gather_files()
    all_files = [p for _, files in sections for p in files]
    file_count = len(all_files)

    # First pass: compute total word count by reading each file
    total_words = 0
    file_wcs = {}
    for p in all_files:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            text = ""
        wc = word_count(text)
        file_wcs[p] = wc
        total_words += wc

    # Build title page + intro
    header = []
    header.append("# THE QURAN DECIPHERMENT PROJECT")
    header.append("## Collected Papers")
    header.append("")
    header.append(f"**Date:** {DATE}  ")
    header.append(f"**File count:** {file_count} findings documents  ")
    header.append(f"**Total word count (body):** ~{total_words:,} words  ")
    header.append(f"**Repository:** `/Users/grey/Downloads/quran/`  ")
    header.append(f"**Canonical order:** per `docs/master-index.md`")
    header.append("")
    header.append("---")
    header.append("")
    header.append("## Introduction")
    header.append("")
    header.append(
        "This volume collects the complete set of findings documents produced by the Quran "
        "Decipherment Project as of 2026-04-12. The project is a computational-philological "
        "audit of the Arabic Quran that asks two questions under rigorous methodology: which "
        "century-old numerological, stylometric, and rhetorical-structure claims about the "
        "text survive honest statistical scrutiny, and does the text exhibit any novel, "
        "reproducible structural signatures that prior scholarship has not documented. "
        "Every phase-A replication is a blind re-derivation from the primary text; every "
        "phase-B hypothesis is pre-registered; every phase-C structural claim is cross-"
        "checked against classical tafsīr, ʿilm al-munāsabāt, and ʿilm al-balāgha."
    )
    header.append("")
    header.append(
        "The methodology is uniform across all papers. Every numerical claim carries a "
        "five-field rules tuple (corpus variant, tokenization, letter-counting rule, basmala "
        "policy, root-normalization scheme). Twenty-two anchor values are test-covered and "
        "fingerprint-matched on every commit. A four-stratum null-model hierarchy is applied: "
        "L0 digit-preserving shuffles, L1 degree-preserving graph randomization, L2 3-gram "
        "character Markov shufflers, L3 length-matched slices of a 13.4-million-token "
        "matched Arabic-prose baseline (Mu'allaqāt, Imruʾ al-Qays, Mutanabbī, al-Jāḥiẓ, "
        "Sīra ibn Hishām, Bukhārī with Quran-quotations stripped). A claim must beat L0–L2 "
        "internally and survive L3 to reach Bonferroni-surviving status."
    )
    header.append("")
    header.append(
        "The volume is divided into four parts. Part I contains cross-cutting synthesis "
        "documents — the scholar's commentary, the convergence analysis, the classical-tafsīr "
        "cross-reference map, the intra-Quranic cross-reference map, the balāgha mapping, "
        "the pre-registered deep-hypotheses queue, the Khawātim al-Ḥashr analysis, the "
        "verse-signature atlas highlights, and the perfect-flow essay. Part II contains the "
        "Phase A replication audits of published claims (Khalifa Code-19, al-Baqara middle-"
        "ayah, Kaheel/Nawfal word-pairs, Cuypers Al-Māʾida macro-ring, Farrin whole-muṣḥaf "
        "ring, etc.). Part III contains the Phase B novel-hypothesis investigations, "
        "organized alphabetically. Part IV contains the Phase C structural deep dives — one "
        "per surah or theological theme that merited extended treatment."
    )
    header.append("")
    header.append(
        "The reader should be aware of three deliberate conventions. First, failures are "
        "reported with equal prominence to successes — the project aims at an honest ledger, "
        "not an apologia or a polemic. Second, the Quran is treated as one text: 114 surahs, "
        "6,236 verses, no \"editions\" framing; scribal and diacritical variants are handled "
        "inside the rules tuple, not by multiplying texts. Third, classical scholarship is "
        "integrated throughout: every finding that has a prior-art ancestor is cited back to "
        "al-Zarkashī (d. 1392), al-Biqāʿī (d. 1480), al-Suyūṭī (d. 1505), al-Kirmānī (d. 1106), "
        "or Ibn al-Muʿtazz (d. 908), with modern parallels to McKay (1999), Witztum-Rips-"
        "Rosenberg (1994), Cuypers (2015), Farrin (2014), and Sinai (2017)."
    )
    header.append("")
    header.append(
        "These papers are source documents, not a narrative. For a thirty-minute overview "
        "see `EXECUTIVE-SUMMARY.md` in the repository root. For a three-hour narrative "
        "synthesis see `findings/scholar-commentary.md` (reproduced here as the first "
        "document of Part I). For the full technical monograph see "
        "`THE-QURAN-DECIPHERMENT-MONOGRAPH.md`. For the literary-critical treatment see "
        "`findings/the-perfect-flow-essay.md` (reproduced here as the last document of "
        "Part I). For the historical-anthropological treatment see `THE-MAN-AT-THE-CENTER.md`."
    )
    header.append("")
    header.append("---")
    header.append("")

    # TOC
    header.append("## Table of Contents")
    header.append("")
    for part_title, files in sections:
        header.append(f"### {part_title}")
        header.append("")
        for p in files:
            anchor = slugify(p.name)
            wc = file_wcs.get(p, 0)
            header.append(f"- [{p.name}](#{anchor}) — {wc:,} words")
        header.append("")
    header.append("---")
    header.append("")

    # Cross-reference map (abbreviated: which files cite which)
    header.append("## Cross-Reference Map")
    header.append("")
    header.append(
        "Each phase-B and phase-C paper cites the phase-A replications relevant to its claim "
        "family, and every claim in every paper is indexed to `docs/master-index.md` "
        "section 4 (novel findings) or section 5 (replication audits). Key cross-reference "
        "hubs in this volume:"
    )
    header.append("")
    header.append(
        "- **convergence-analysis.md** maps every Bonferroni-surviving finding to its "
        "convergent evidence across methods.\n"
        "- **classical-cross-references.md** maps every finding back to its classical "
        "ancestor (al-Zarkashī, al-Biqāʿī, al-Suyūṭī, al-Kirmānī, Ibn al-Muʿtazz).\n"
        "- **intra-quranic-cross-references.md** maps every finding to the Quranic parallels "
        "that anchor or extend it.\n"
        "- **balagha-mapping.md** maps every novel rhetorical observation to the "
        "classical-balāgha taxonomy (*jinās, tarṣīʿ, radd al-ʿajuz, iltifāt, tikrār, sajʿ*).\n"
        "- **deep-hypotheses-queue.md** contains the 22 pre-registered hypotheses and their "
        "disposition.\n"
        "- **code19-khalifa-full-audit.md** (Part II) is the master falsification record for "
        "the Code-19 literature.\n"
        "- **cross-textual-baseline.md** (Part III) is the master matched-baseline record; "
        "every numerical claim in the volume is anchored to its results.\n"
        "- **ring-center-semantics.md** (Part IV) is the master record for every Bonferroni-"
        "surviving ring in the corpus."
    )
    header.append("")
    header.append("---")
    header.append("")

    # Write the output
    with open(OUT, "w", encoding="utf-8") as out:
        out.write("\n".join(header))
        out.write("\n")

        for part_title, files in sections:
            out.write("\n\n")
            out.write(f"# {part_title}\n")
            out.write("\n")
            for p in files:
                anchor = slugify(p.name)
                out.write("\n\n---\n\n")
                out.write(f"<a id=\"{anchor}\"></a>\n\n")
                out.write(f"# {p.name}\n\n")
                out.write(f"*Source: `{p.relative_to(ROOT)}`*\n\n")
                out.write("---\n\n")
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                except Exception as e:
                    text = f"[Error reading file: {e}]"
                out.write(text)
                if not text.endswith("\n"):
                    out.write("\n")

    # Compute final size
    final_size = OUT.stat().st_size
    final_text = OUT.read_text(encoding="utf-8", errors="replace")
    final_wc = word_count(final_text)
    print(f"Wrote {OUT}")
    print(f"File count (findings): {file_count}")
    print(f"Total word count: {final_wc:,}")
    print(f"Size on disk: {final_size:,} bytes ({final_size/1024/1024:.2f} MB)")

if __name__ == "__main__":
    main()
