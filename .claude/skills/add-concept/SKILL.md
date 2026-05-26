---
name: add-concept
description: Use when the user wants to add a canonical concept note to Pojmy/ (e.g. "add a Pojmy entry for funkce", "create Pojmy/Graf"). Researches the term across all course PDFs in the vault, drafts a canonical Czech definition with cross-course sections, populates Czech-inflected aliases.
---

# Add Pojmy/ concept note

Add a new canonical atomic concept note to `Pojmy/` for the FIT ČVUT SZZ vault.

## Input

- **Term** (Czech, singular nominative). Example: `Funkce`, `Graf`, `Konečný automat`.

If the term is ambiguous (means multiple things across courses), ask the user whether they want one note with sections, or separate notes + a parent disambiguation. Default behavior is **stop and ask** when ambiguity is detected.

## Workflow

1. **Cross-PDF research.** Grep / read across course PDFs in `materials/` for the term. Collect:
   - The most rigorous definition (usually DML if a math term, lecture 1–2 of the owning course otherwise).
   - Any course-specific simplifications or extensions.
   - Related terms (those that will become wikilinks).

2. **Detect conflicts.** If the term is defined non-equivalently across courses, surface the conflict before writing. Do not silently pick one.

3. **Draft `Pojmy/<Term>.md`:**
   - Filename: capitalized singular nominative, dashes for multi-word (`Konečný-automat.md`, `Slabě-souvislý-graf.md`).
   - Frontmatter `aliases:`: include the term in nominative + key inflected Czech forms (gen., dat., akk., lok., instr., plural). Use lowercase aliases for autocomplete.
   - Frontmatter `tags:`: `[definice, kurz/<COURSE1>, kurz/<COURSE2>, …]` for every course that uses the term.
   - Body sections:
     - `## Definice` — the canonical, atomic definition. 1–3 lines. LaTeX where it helps.
     - `## Použití v <KURZ>` — only when a specific course extends or specializes the definition. Optional.
     - `## Související` — bullet list of `[[other-concept]]` links.
   - **Do not** include theorems or proofs in `Pojmy/` notes — those belong in question summaries. `Pojmy/` is for definitions and pointers.

4. **Backlink check.** Search `BI-SPOL/` and `BI-UI/` for occurrences of the term that are not yet linked. Show the user the list and ask whether to wire them up. Don't mass-edit silently.

5. **Commit:** message `Pojmy: <term>` (or `Pojmy: <term1>, <term2>, …` for batched additions).

## Naming rules

- Singular nominative, capitalized: `Graf`, not `grafy` or `graf`.
- Multi-word: dashes, e.g. `Konečný-automat.md`, not `Konečný automat.md` (links read cleaner).
- No timestamp IDs.
- Disambiguation when truly needed: parenthetical suffix, e.g. `Funkce (matematika).md` vs `Funkce (programování).md`. Prefer one-note-multiple-sections to disambiguation pages.

## Aliases — Czech inflection

Czech declines heavily; aliases let `[[Graf|grafu]]` autocomplete from any case. Always include at least:

```yaml
aliases: [<lowercase nominative>, <genitive>, <dative>, <accusative>, <locative>, <instrumental>, <plural>]
```

For `Graf`: `[graf, grafu, grafem, grafy, grafů, grafům]`. For irregular declension (`Číslo` → `čísla, číslu, …`) include all stems.

## Anti-patterns

- Including proofs or theorems in `Pojmy/` notes. Those go in question summaries.
- Importing a definition verbatim from a PDF without re-wording. Atomic notes should be in your own words to test understanding.
- Creating a note for a term that appears only once in one course — that's not a shared concept yet. Wait for the second reference.
- Skipping aliases. Without them, every grammatical case requires manual `[[Term|term]]` aliasing in every link.
- Pre-emptively grouping concepts via folders inside `Pojmy/`. `Pojmy/` is intentionally flat — use links and (later) MOCs.

## Reference

- Full design: `docs/superpowers/specs/2026-05-26-zettelkasten-vault-design.md`
- Template: `Šablony/pojem.md`
