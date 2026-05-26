# Zettelkasten vault design — FIT ČVUT SZZ

**Date:** 2026-05-26
**Scope:** Conventions, structure, tooling, and Claude Code skills for the SZZ exam-prep Obsidian vault.

## Goal

Turn this repo into an interconnected Zettelkasten of exam-prep materials. Each exam question gets a long + short markdown file. Recurring concepts (set, function, graph, automaton, …) live as single canonical notes that every question links to, making cross-course connections explicit instead of duplicating definitions.

## Folder structure

```
SZZ/
  AAG/                          source PDFs only
  AG1/                          source PDFs only
  DBS/                          source PDFs only
  DML/                          source PDFs only
  …other course folders…        source PDFs only

  BI-SPOL/                      ALL shared-course question summaries (flat)
    1AAG-long.md
    1AAG-short.md
    3AG1-long.md
    3AG1-short.md
    …

  BI-UI/                        ALL specialization question summaries (flat)

  Pojmy/                        cross-course atomic concept notes (flat)
    Graf.md
    Strom.md
    Funkce.md
    Konečný-automat.md
    …

  MOC/                          maps of content — demand-driven, do NOT pre-create
    Grafy.md
    AG1.md

  Šablony/                      Obsidian Templater templates
    long.md
    short.md
    pojem.md

  docs/superpowers/specs/       design specs (this file)
```

Per-question files are flat inside `BI-SPOL/` and `BI-UI/` — ~104 files in BI-SPOL, ~80 in BI-UI is fine in a single folder. No per-course subdivision.

## File naming

- **Question summaries:** `[question-number][course-name]-long.md` / `…-short.md`. Example: `3AG1-long.md`, `3AG1-short.md`.
- **Concept notes:** singular nominative, capitalized, Czech, no IDs. `Graf.md`, `Strom.md`, `Konečný-automat.md`. Spaces in names allowed but dashes preferred for multi-word terms to keep links readable.
- **MOCs:** plain topic name. `Grafy.md`, `AG1.md`. No `MOC` suffix.

No timestamp prefixes. Obsidian auto-updates wikilinks on rename, so the ID rationale doesn't apply here.

## Concept note (`Pojmy/`) format

```markdown
---
aliases: [graf, grafu, grafem, grafy, grafů, grafům]
tags: [definice, kurz/AG1, kurz/DML]
---

# Graf

## Definice
Kanonická, krátká definice (1–3 řádky, LaTeX).

## Použití v AG1
Kontextové rozšíření / poznámky (volitelné, jen pokud kurz definici zužuje/rozšiřuje).

## Použití v DML
(jen pokud se kurz odlišuje)

## Související
- [[Strom]]
- [[Souvislost]]
- [[Orientovaný-graf]]
```

**Aliases:** include Czech inflected forms so `[[Graf|grafu]]` autocompletes from any case typed in the editor.

## Linking discipline

- **Link first meaningful occurrence per note**, not every occurrence. Over-linking hurts readability.
- **Bold for emphasis stays.** First defined-term mention: `**[[Graf]]**` (link + bold). Subsequent mentions: plain text or `[[Graf|graf]]` for grammatical agreement.
- **Embed (`![[…]]`) sparingly** — only when the canonical content literally belongs inline. Prefer section embeds (`![[Graf#Definice]]`) over whole-file embeds.
- **Don't both tag and link the same concept** on one note. Concepts use wikilinks; cross-cutting metadata uses tags.

## Disambiguation: same term, different definitions

When a term appears in multiple courses:

1. **Same concept, different framing** → one note, sections per course (e.g. `Funkce` with sections for DML's set-theoretic definition and AG1's operational usage).
2. **Genuinely different mathematical objects sharing a name** → separate notes + a parent overview that links them. E.g. `Automat.md` is a thin disambiguator/overview that links `Konečný-automat.md`, `Zásobníkový-automat.md`, `Turingův-stroj.md`.
3. **Unsure which applies** → stop and ask the user before writing. This rule exists because lecturers in different courses sometimes simplify definitions; choosing wrong would propagate.

## Tags

| Purpose | Tag |
|---|---|
| Status | `#todo`, `#hotovo`, `#k-revizi` |
| Note type | `#definice`, `#věta`, `#algoritmus`, `#otázka` |
| Course attribution | `#kurz/AG1`, `#kurz/DML`, … |
| Exam question linkage | `#otázka/3` etc. |
| Spaced-repetition flag | `#flashcard` |

Tags are for metadata, not for concepts. If something has (or could have) a note, link it.

## MOCs

- Create a MOC only when ≥5 related notes need gathering (the "squeeze point").
- MOCs are many-to-many; a note can appear in 0 or N MOCs. They are *not* folders.
- Likely first MOCs: `Grafy.md` (cross-course graph concepts), `AG1.md` (all AG1 questions grouped thematically).

## Long vs. short — what differs from the current CLAUDE.md

The existing CLAUDE.md already specifies long/short conventions. This spec adds:

- **Long notes should `![[…]]`-embed or `[[…]]`-link concept notes for every shared term.** First mention bold-linked.
- **Short notes use plain text** (no embeds) — they are a handwriting rehearsal artifact, not a navigable document. They may still link concepts for cross-referencing while studying, but the goal is "what I would write on paper in 20 minutes".

## Workflow for adding a new question

1. Read lecture PDFs in the relevant course folder (source of truth).
2. Draft `[N][course]-long.md` directly in `BI-SPOL/` or `BI-UI/`.
3. For each major term: check `Pojmy/`. If a note exists → link/embed. If not → create one (or stub it).
4. **If a term is already defined in `Pojmy/` but this course defines it differently — stop and ask the user before writing.**
5. After `-long.md`, write `-short.md` as the handwriting-ready compression.
6. Update relevant MOC if the squeeze point is reached.

## Git

Vault is a git repo. Commit after:
- Each completed question (long + short).
- Each batch of concept-note additions.
- Structural changes (template edits, CLAUDE.md updates).

`.gitignore` excludes `.obsidian/workspace*.json`, `.DS_Store`, `.trash/`. Keep `.obsidian/` config tracked so plugin/template configuration follows the repo.

## Obsidian plugin set

**Day-one:**
- Templater — `Šablony/long.md`, `short.md`, `pojem.md`.

**Strongly recommended before final-review phase:**
- Spaced Repetition (st3v3nmw) — flag definitions/theorems with `#flashcard`.

**Add on demand:**
- Dataview — when a query would be written 3+ times (e.g. "all AG1 questions, status").
- Excalidraw — for automata transition diagrams, proof sketches.

Rule: don't install a plugin until you've felt its absence twice.

## Claude Code skills

Two project-level skills under `.claude/skills/`:

- **add-question** — drives the question-creation workflow end-to-end. Reads relevant PDFs, drafts long+short, detects concept references, surfaces conflicts with existing `Pojmy/` notes, asks user when uncertain. Invocation: `/add-question 4 AG1`.
- **add-concept** — adds a new `Pojmy/` note. Searches all course PDFs for the term, drafts a canonical definition with cross-course sections, populates Czech-inflected aliases.

Both are skills (not subagents) so they're `/`-invokable from inside the vault.

## Out of scope

- Fleeting/literature/permanent note separation — overkill for a 6-month project.
- Timestamp-ID naming.
- Pre-created empty MOCs.
- Auto-generating short.md from long.md — short is its own intentional artifact.
