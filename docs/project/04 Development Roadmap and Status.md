# Daily Intelligence System — Development Roadmap and Status

> **Purpose**
>
> This document controls the implementation of the Daily Intelligence System.
>
> It records the current phase, completed decisions, active milestone, blockers, deferred work and next highest-priority action.
>
> It is not a long-term product vision document and should not duplicate the Project Brief, Product Requirements, System Architecture or Information Taxonomy.
>
> ---
>
> **Primary Question**
>
> > *What should be built now, what has already been completed, and what is the next highest-value step?*
>
> ---
>
> **Update Frequency**
>
> Update whenever the active milestone, project status, blocker or implementation priority changes.

---

# Roadmap Principles

Development should follow these rules:

- Build one complete vertical slice before expanding scope.
- Prefer working output over additional planning.
- Do not create features without a validated need.
- Do not add recurring cost.
- Do not introduce production AI calls.
- Keep daily manual work negligible.
- Validate locally before enabling automation.
- Use Git and tests to verify each material change.
- Keep the repository public-safe.
- Stop at stable checkpoints.

The project should not move to the next phase until the current phase has a clear completion condition.

---

# Current Project Status

| Field | Current Status |
|---|---|
| Project Phase | Phase 0 — Definition and Repository Setup |
| Current Milestone | Complete and validate the initial project-control documents |
| Repository Status | Public repository created and opened locally in VS Code |
| Implementation Status | No production code yet |
| Automation Status | Not started |
| Source Registry | Not started |
| Testing Status | Not started |
| Current Blockers | None |
| Current Priority | Finalise project definition, then begin the smallest local vertical slice |

---

# Completed Work

## Project Decisions

- Selected a hybrid information model:
  - ChatGPT provides independent interpretation and synthesis.
  - GitHub provides deterministic collection, organisation, ranking and archiving.
- Confirmed zero recurring monetary cost as a hard constraint.
- Confirmed negligible daily manual work as a hard constraint.
- Confirmed that production must not consume GitHub AI or Copilot credits.
- Confirmed that the MVP will use public structured sources.
- Confirmed that RSS and Atom are the first supported source types.
- Confirmed that production will run through Python and GitHub Actions.
- Confirmed that the system will not use LLM calls, agents, RAG, embeddings or vector databases during the MVP.
- Confirmed that the repository will remain public.
- Confirmed that private Career OS materials will remain outside the repository.
- Confirmed JSON Lines for processed article records.
- Confirmed JSON for run summaries.
- Confirmed Markdown for daily reports.
- Confirmed UTC for internal timestamps.
- Confirmed that the system will generate one primary report placement per item.
- Confirmed automated repository persistence as the initial delivery model.
- Deferred GitHub Issues, GitHub Pages and newsletter ingestion.

## Repository Setup

- Created the public GitHub repository.
- Added:
  - `README.md`
  - `.gitignore`
  - `LICENSE`
- Opened the repository locally in VS Code.
- Created:
  - `docs/project/`
  - `src/`
- Created the initial project-control files.

## Project Documentation

Drafted:

- `00 Project Brief.md`
- `01 Product Requirements.md`
- `02 System Architecture.md`
- `03 Information Taxonomy and Source Policy.md`
- `04 Development Roadmap and Status.md`

---

# Development Phases

---

# Phase 0 — Definition and Repository Setup

## Objective

Create the minimum project definition required to begin implementation without major ambiguity.

## Scope

- define project purpose;
- define product behaviour;
- define information taxonomy and source policy;
- define system architecture;
- define implementation roadmap;
- review consistency across documents;
- establish the initial repository structure.

## Completion Criteria

Phase 0 is complete when:

- documents `00` through `04` are internally consistent;
- no major contradiction remains between requirements and architecture;
- unresolved decisions are explicitly listed;
- the MVP boundary is clear;
- the next implementation milestone is defined;
- the initial documentation changes are committed and pushed.

## Current Status

**In progress**

## Remaining Actions

- review documents `00` through `04` as one system;
- remove duplication or contradictions;
- verify all hard constraints are consistently represented;
- decide whether any open decisions block implementation;
- commit and push the initial documentation set;
- upload the approved project documents to the dedicated GPT project.

---

# Phase 1 — Local Vertical Slice

## Objective

Build the smallest complete local pipeline that proves the core workflow.

## Initial Scope

Use a very small controlled source set and implement:

1. configuration loading;
2. RSS or Atom parsing;
3. basic record normalisation;
4. required-field validation;
5. exact duplicate reduction;
6. simple domain classification;
7. provisional relevance scoring;
8. JSON Lines persistence;
9. Markdown report generation;
10. structured run summary.

## Deliberately Excluded

- near-duplicate clustering;
- broad source coverage;
- advanced ranking;
- GitHub Actions;
- daily schedule;
- automated commits;
- GitHub Issues;
- GitHub Pages;
- newsletter ingestion;
- AI-generated summaries.

## Initial Source Scope

Use approximately three to five sources selected to test different cases:

- one primary institutional source;
- one high-quality reporting source;
- one AI or technology source;
- one European or Italian source;
- optionally one startup or opportunity source.

The purpose is testing system behaviour, not achieving broad coverage.

## Expected Files

Likely files introduced during this phase:

```text
config/
├── sources.yaml
├── domains.yaml
└── settings.yaml

src/daily_intelligence/
├── __init__.py
├── cli.py
├── config.py
├── collect.py
├── normalize.py
├── validate.py
├── deduplicate.py
├── classify.py
├── rank.py
├── storage.py
├── report.py
├── models.py
└── logging_config.py

tests/
└── fixtures/

pyproject.toml