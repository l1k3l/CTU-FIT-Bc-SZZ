---
name: add-question
description: Use when the user wants to add or draft study materials for a specific SZZ exam question (e.g. "add question 4 from AG1", "draft the long+short for 7DBS"). Drives the full workflow — reads relevant course PDFs, drafts long+short, links to Pojmy/ canonical concepts, surfaces definition conflicts before writing.
---

# Add SZZ exam question

Drive the end-to-end workflow for creating `[N][COURSE]-long.md` and `[N][COURSE]-short.md` in the FIT ČVUT SZZ vault.

## Inputs

- **Question number** (e.g. `4`)
- **Course** (e.g. `AG1`, `AAG`, `DBS`, `DML`, …)
- **Question text** (the exam question itself). If the user didn't paste it, **stop and ask** — without the exact wording you can't match section headings to the question parts.

If the user didn't specify whether the course is BI-SPOL or BI-UI, ask. Don't guess.

## Workflow

1. **Read source PDFs** in `materials/<COURSE>/` (e.g. `materials/AG1/`, `materials/AAG/`). These are the source of truth — do not rely on prior knowledge if the lecture content differs. Note: `materials/` is gitignored.

2. **Skim `Pojmy/`** for existing concept notes that map to terms in the question. Note which terms have canonical definitions and which don't.

3. **Detect definition conflicts.** For each term that already has a `Pojmy/` note: if this course defines it differently, **STOP and surface the conflict to the user.** Show the existing definition and the course-specific one. Ask: merge into one note with course-specific section, or split into two notes with a parent? Do not silently overwrite or fork.

4. **Draft `[N][COURSE]-long.md`** in `BI-SPOL/` or `BI-UI/`:
   - Frontmatter: `tags: [otázka, kurz/<COURSE>, otázka/<N>, todo]`.
   - First line: `> **Otázka SZZ:** <exact question text>`.
   - Section headings match the parts of the question.
   - First defined-term mention: `**[[Term]]**` (link + bold). Subsequent: plain or `[[Term|term]]`.
   - For canonical definitions that already exist in `Pojmy/`: embed the definition section, e.g. `![[Graf#Definice]]`.
   - Include proofs/proof sketches, pseudocode, complexities, motivation, examples.
   - End with a "Co je potřeba na zkoušku znát" summary section.

5. **Add or stub missing `Pojmy/` notes.** When a term is referenced via `[[…]]` but no note exists, create at least a stub with the canonical definition pulled from the lecture PDF, plus `aliases:` for Czech inflections. If a full note requires research across multiple courses, delegate to the `add-concept` skill instead of inlining.

6. **Draft `[N][COURSE]-short.md`** as the handwriting-ready cheat sheet (see CLAUDE.md for short-version rules: definitions only, no proofs except when essential, no pseudocode, no embeds, compact LaTeX/tables, ~1–2 A4 pages handwritten).

7. **Verify** before declaring done:
   - All parts of the exam question have a corresponding section.
   - All shared terms link to `Pojmy/` (first occurrence).
   - No definitions in long.md contradict `Pojmy/` notes.
   - Short.md fits the 20-minute handwriting budget.

8. **Commit:** one commit for `long+short+any new Pojmy stubs`. Message: `Add <N><COURSE>: <short topic>`.

## Anti-patterns

- Transcribing PDF pages verbatim. The processing (re-wording, atomizing, structuring) is the value.
- Inventing definitions from prior knowledge when the PDF disagrees. PDF wins.
- Silently choosing one of two conflicting definitions. Always surface the conflict.
- Pre-emptively creating MOCs because "this question is graph-related". MOCs are demand-driven (≥5 related notes).
- Over-linking — every occurrence of "graph" turned into `[[Graf]]`. Link only the first meaningful mention per note.
- Writing the short version as a mechanical compression of the long version. It should reflect what would actually be written on paper in 20 minutes.

## Reference

- Full design: `docs/superpowers/specs/2026-05-26-zettelkasten-vault-design.md`
- Templates: `Šablony/long.md`, `Šablony/short.md`
- Existing example: `BI-SPOL/3AG1-long.md`, `BI-SPOL/3AG1-short.md`
