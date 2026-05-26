# SZZ — Learning materials

This folder is an Obsidian vault containing study materials for the state final exam (SZZ) at FIT ČVUT. The goal is a Zettelkasten where each exam question links to canonical concept notes shared across courses.

Full design rationale: [`docs/superpowers/specs/2026-05-26-zettelkasten-vault-design.md`](docs/superpowers/specs/2026-05-26-zettelkasten-vault-design.md).

## Folder layout

```
AAG/, AG1/, DBS/, DML/, …    source PDFs only (course handouts)
BI-SPOL/                     ALL shared-course question summaries (flat — no per-course subfolders)
BI-UI/                       ALL specialization question summaries (flat)
Pojmy/                       cross-course canonical concept notes (flat)
MOC/                         maps of content — demand-driven, do NOT pre-create
Šablony/                     Obsidian Templater templates
docs/superpowers/specs/      design specs
```

Per-question summary files live **directly** in `BI-SPOL/` or `BI-UI/` — not in per-course subfolders. Ask the user which one a new question belongs to if unclear.

## Per-question conventions

For each exam question, two Markdown files:

- `[question-number][course-name]-long.md` — full version (definitions, theorems, proofs, algorithms, pseudocode, time complexities, motivation, examples).
- `[question-number][course-name]-short.md` — handwriting-ready cheat sheet.

Example: question 3 of AG1 → `BI-SPOL/3AG1-long.md` and `BI-SPOL/3AG1-short.md`.

### Long version — goals
- Cover the exam question completely.
- Definitions, theorems with **proofs** (or proof sketches), pseudocode for algorithms.
- Lecture PDFs are the source of truth.
- Section headings match parts of the exam question.
- **Link or embed concept notes from `Pojmy/`** for every shared term (see linking rules below).

### Short version — goals
The student has **20 minutes per question** in the oral exam and reproduces content on paper. The short version reflects what one would realistically write down:

- **Definitions only** — precise but minimal.
- **No proofs** unless explicitly required. A one-sentence proof-idea is OK for essential proofs.
- **No pseudocode.** Replace with a one-paragraph or bullet description of the algorithm idea + time complexity.
- **No motivation, no examples, no historical notes.**
- Compact notation (LaTeX, small comparison tables).
- ~1–2 sides of A4 when handwritten.
- **Plain text** — no embeds; wikilinks OK for cross-referencing while studying.

## Concept notes (`Pojmy/`)

Canonical, atomic notes for terms used across courses (`Graf.md`, `Funkce.md`, `Konečný-automat.md`). Naming: singular nominative, capitalized, dashes for multi-word. No timestamp IDs.

Template (also lives in `Šablony/pojem.md`):

```markdown
---
aliases: [graf, grafu, grafem, grafy, grafů, grafům]
tags: [definice, kurz/AG1, kurz/DML]
---

# Graf

## Definice
Kanonická, krátká definice.

## Použití v <KURZ>
(jen pokud kurz definici zužuje/rozšiřuje)

## Související
- [[Strom]]
- [[Souvislost]]
```

**Aliases** carry Czech inflected forms so `[[Graf|grafu]]` autocompletes from any case typed.

## Linking discipline

- **Link first meaningful occurrence per note**, not every occurrence.
- **First defined-term mention:** `**[[Graf]]**` (link + bold). Subsequent: plain or `[[Graf|graf]]`.
- **Embeds (`![[…]]`)** sparingly — only when content literally belongs inline. Prefer section embeds (`![[Graf#Definice]]`) over whole-file.
- **Don't both tag and link** the same concept on one note.

## Disambiguation: same term, different definitions

When a term appears in multiple courses:

1. **Same concept, different framing** → one note with sections per course.
2. **Different mathematical objects sharing a name** → separate notes + a thin parent overview (e.g. `Automat.md` → `Konečný-automat.md`, `Zásobníkový-automat.md`, `Turingův-stroj.md`).
3. **Unsure which applies** → **STOP and ask the user before writing.** Some lecturers simplify; choosing wrong propagates.

## Tags

- Status: `#todo`, `#hotovo`, `#k-revizi`
- Type: `#definice`, `#věta`, `#algoritmus`, `#otázka`
- Course: `#kurz/AG1`, `#kurz/DML`, …
- Exam-question linkage: `#otázka/3`
- Spaced-repetition flag: `#flashcard`

## MOCs

Create only when ≥5 related notes need gathering. Never pre-create empty MOCs.

## Workflow when adding a new question

1. Read the relevant course PDFs.
2. Draft `[N][course]-long.md` in `BI-SPOL/` or `BI-UI/`.
3. For each major term: check `Pojmy/`. If a note exists → link/embed. If not → create one (or stub).
4. **If `Pojmy/` already defines a term but the current course defines it differently — stop and ask the user.**
5. Write `-short.md` as a handwriting-ready compression (not mechanical excerpt).
6. Commit (see Git below).

## Git

This vault is a git repository. Commit:
- After each completed question (long + short).
- After each batch of `Pojmy/` additions.
- After structural changes (templates, this file, design specs).

Commit messages: short Czech or English imperative ("Add 3AG1 long+short", "Pojmy: Graf, Strom, Funkce"). One logical change per commit.

`.gitignore` excludes `.obsidian/workspace*.json`, `.DS_Store`, `.trash/` — Obsidian config itself is tracked.

## Language

Materials are in **Czech** (exam and source PDFs are in Czech). Filenames, frontmatter keys, and commit messages may be English; user-facing content is Czech.
