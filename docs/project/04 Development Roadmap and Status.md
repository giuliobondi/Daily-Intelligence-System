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
| Project Phase | Phase 0 — Definition and Repository Setup - Completed| 
| Current Milestone | Complete and validate the initial project-control documents |
| Repository Status | Public repository created and opened locally in VS Code |
| Implementation Status | No production code yet |
| Automation Status | Not started |
| Source Registry | Not started |
| Testing Status | Not started |
| Current Blockers | Documentation restoration and final consistency review |
| Current Priority | Restore complete project documents, validate them, and then begin the smallest local vertical slice |

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

Drafted and restored:

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

- verify that documents `00` through `04` are complete and have intact endings;
- review documents `00` through `04` as one system;
- remove any duplication or contradiction that materially affects implementation;
- verify all hard constraints are consistently represented;
- confirm that open decisions do not block the first local vertical slice;
- inspect the documentation-only diff;
- commit and push the restored documentation set;
- replace the truncated copies in the dedicated GPT project with the canonical versions.

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
```

Files should be created only when the relevant functionality is implemented.

## Completion Criteria

Phase 1 is complete when:

- the pipeline runs locally from one command;
- sample feeds are collected successfully;
- valid records are normalised;
- invalid records are handled visibly;
- exact duplicates are reduced;
- records receive at least one simple classification outcome;
- relevance scores are deterministic;
- processed JSON Lines are written;
- a readable Markdown report is generated;
- a structured run summary is written;
- repeated execution with unchanged input does not create uncontrolled duplicates;
- critical functions have initial tests;
- no paid service or AI call is used.

## Validation

- run the pipeline locally;
- inspect output files;
- inspect log messages;
- inspect duplicate handling;
- inspect classification;
- inspect ranking order;
- inspect report readability;
- rerun with unchanged input;
- run automated tests.

---

# Phase 2 — Quality Logic

## Objective

Improve information quality after the local pipeline works end to end.

## Scope

- conservative near-duplicate detection;
- multi-source story clustering;
- stronger domain classification;
- secondary-domain tags;
- geographic classification;
- content-type classification;
- tracked entities;
- configurable ranking weights;
- report-length controls;
- unclassified-item review;
- source-quality penalties;
- improved score explainability.

## Entry Condition

Phase 1 must already produce a reliable complete report.

## Completion Criteria

Phase 2 is complete when:

- near duplicates are reduced without excessive false merging;
- classification is usable across a reviewed sample;
- ranking places clearly important items above routine items;
- score components are inspectable;
- multi-domain records do not create excessive repetition;
- report length remains within configured limits;
- a manually reviewed validation sample passes agreed quality thresholds.

## Validation

- use curated fixtures;
- review false-positive clusters;
- review false-negative clusters;
- review misclassifications;
- compare ranking with manual judgment;
- inspect unclassified-item rate;
- inspect publisher and domain concentration.

---

# Phase 3 — GitHub Automation

## Objective

Run the validated pipeline automatically in the public repository.

## Scope

- create GitHub Actions workflow;
- configure scheduled execution;
- add manual workflow trigger;
- set explicit timeout;
- prevent overlapping runs;
- use minimal permissions;
- run configuration validation;
- execute the pipeline;
- validate generated output;
- commit valid outputs automatically;
- push changes;
- expose failure logs.

## Entry Condition

The local pipeline must be stable and repeatable.

## Completion Criteria

Phase 3 is complete when:

- the workflow runs successfully through manual GitHub Actions execution;
- outputs are generated correctly in the repository;
- one coherent automated commit is created;
- failed-source behaviour is visible;
- critical failures stop publication;
- no-change runs avoid empty commits;
- no AI credits or paid services are used;
- the scheduled trigger is enabled only after manual validation.

## Validation

- run through `workflow_dispatch`;
- inspect workflow permissions;
- inspect logs;
- inspect generated files;
- inspect automated commit;
- test a degraded source failure;
- test a critical configuration failure;
- confirm the workflow stays within the configured timeout.

---

# Phase 4 — Initial Production Evaluation

## Objective

Evaluate whether the system is useful in real daily use.

## Evaluation Period

Approximately two weeks after stable automation begins.

## Questions

### Usage

- Is the report opened consistently?
- Can it be scanned in approximately 10–15 minutes?
- Are source links used selectively?

### Coverage

- Are major relevant stories missed?
- Are any domains consistently empty?
- Are some domains overrepresented?

### Noise

- Are low-value items frequently displayed?
- Is promotional content overrepresented?
- Are obvious duplicates still common?

### Classification

- Are items assigned to useful domains?
- Is the unclassified rate acceptable?
- Are multi-domain items handled clearly?

### Ranking

- Do high-value items appear near the top?
- Do source-tier weights distort relevance?
- Does multi-source coverage create inappropriate ranking inflation?

### Operations

- Do scheduled runs complete reliably?
- Are failures understandable?
- Is maintenance acceptably low?
- Does the project remain at zero recurring cost?

## Completion Criteria

Phase 4 is complete when:

- at least two weeks of reports have been reviewed;
- major weaknesses are documented;
- low-value sources are identified;
- useful sources are confirmed;
- ranking and classification issues are prioritised;
- further development decisions are based on evidence.

---

# Phase 5 — Controlled Expansion

## Objective

Add only features justified by the production evaluation.

## Possible Enhancements

- broader source universe;
- more robust source-health history;
- improved clustering;
- richer entity tracking;
- weekly archive analytics;
- GitHub Issue delivery;
- GitHub Pages;
- opportunity-specific report section;
- selected public newsletter feeds;
- more detailed concentration metrics;
- improved trend detection.

## Rules

A feature should enter this phase only when:

- the problem is observed in real use;
- the feature creates measurable value;
- recurring monetary cost remains zero;
- recurring AI-credit use remains zero;
- maintenance remains proportionate;
- a simpler solution is insufficient.

## Excluded by Default

- paid APIs;
- automated ChatGPT integration;
- private email ingestion;
- full-article extraction;
- autonomous agents;
- RAG;
- vector databases;
- complex cloud infrastructure;
- mobile application development.

---

# Current Milestone

## Milestone 0 — Approve the Initial Project Definition

### Objective

Complete Phase 0 and create the first stable repository checkpoint.

### Required Outputs

- approved `00 Project Brief.md`;
- approved `01 Product Requirements.md`;
- approved `02 System Architecture.md`;
- approved `03 Information Taxonomy and Source Policy.md`;
- approved `04 Development Roadmap and Status.md`.

### Validation Checklist

- [ ] Project purpose is clear.
- [ ] MVP scope is clear.
- [ ] Non-goals are explicit.
- [ ] Hard constraints are consistent.
- [ ] Product requirements are testable.
- [ ] Architecture satisfies the requirements.
- [ ] Taxonomy matches intended domains.
- [ ] Public-repository boundaries are clear.
- [ ] Open decisions are visible.
- [ ] No code has been prematurely added.
- [ ] No private Career OS content is present.
- [ ] Documentation ownership is clear.

### Completion Action

Commit and push the full documentation set as one coherent project-definition commit.

### Suggested Commit Message

```text
docs: restore complete project definition
```

---

# Next Milestone

## Milestone 1 — Build the Local Collection-to-Report Slice

The first implementation milestone should produce a working local report from a very small source set.

### First Technical Deliverables

- `pyproject.toml`;
- initial package structure;
- typed article model;
- configuration loader;
- small `sources.yaml`;
- small `domains.yaml`;
- feed collection;
- basic normalisation;
- JSON Lines output;
- basic Markdown report;
- initial tests.

### Important Constraint

Do not implement the full architecture at once.

The first technical checkpoint should be:

> Load valid configuration and successfully parse one controlled RSS or Atom fixture into a typed normalised record.

Only after that works should the next pipeline stage be added.

---

# Deferred Features

| Feature | Status | Reason |
|---|---|---|
| GitHub Issues delivery | Deferred | Core report should be validated first |
| GitHub Pages | Deferred | Avoid frontend work before usefulness is proven |
| Newsletter-email ingestion | Deferred | Adds privacy and authentication complexity |
| Public newsletter feeds | Monitoring | May be added as normal sources if structured and valuable |
| LLM summaries | Rejected for MVP | Recurring cost and unnecessary dependency |
| Automated ChatGPT integration | Rejected for MVP | Connectors and API assumptions violate constraints |
| Machine-learning classification | Rejected for MVP | Deterministic logic should be tested first |
| Embeddings and semantic search | Rejected for MVP | No validated need |
| RAG | Rejected for MVP | No validated workflow problem |
| Autonomous agents | Rejected for MVP | Adds complexity without current value |
| Cloud database | Rejected for MVP | JSON Lines is sufficient initially |
| Private source ingestion | Rejected for MVP | Public repository and privacy constraints |
| Multi-user support | Rejected for MVP | Initial product is single-user |

---

# Project Risks

## Documentation Without Execution

The project may remain in planning mode.

**Control:** Phase 0 ends with one documentation commit, after which the next action must be technical implementation.

## Scope Expansion

New features may be added before the MVP works.

**Control:** every new feature must solve a documented limitation.

## Premature Source Expansion

A large source list may create noise before the pipeline is stable.

**Control:** Phase 1 uses only three to five test sources.

## Weak Quality Evaluation

The system may run technically but produce poor information.

**Control:** quality review is a dedicated phase with manual comparison.

## GitHub Actions Complexity

Automation may be added before local behaviour is reliable.

**Control:** GitHub Actions begins only after the local vertical slice works.

## Repository Growth

Daily JSON and Markdown files may accumulate.

**Control:** review storage strategy after the initial production period.

## Maintenance Burden

Source instability may create recurring manual work.

**Control:** source-level isolation, health tracking and conservative source selection.

---

# Decision Gates

The following gates prevent premature expansion.

## Gate 1 — Begin Implementation

Required:

- documents `00` through `04` approved;
- initial commit pushed;
- no major unresolved blocker.

## Gate 2 — Add Quality Logic

Required:

- local end-to-end pipeline works;
- output is inspectable;
- exact duplicate handling works;
- initial tests pass.

## Gate 3 — Add GitHub Actions

Required:

- local pipeline is stable;
- configuration is validated;
- report generation is repeatable;
- failure modes are understood.

## Gate 4 — Expand Sources

Required:

- source gaps are demonstrated;
- new sources pass the source policy;
- additional coverage justifies added maintenance.

## Gate 5 — Add Delivery Features

Required:

- reports are being used;
- repository browsing is a real usability limitation;
- delivery feature remains zero-cost and low-maintenance.

---

# Status Tracking Template

Use this section during active development.

## Current Phase

Phase:

## Current Milestone

Milestone:

## Completed Since Last Update

-

## Active Work

-

## Blockers

-

## Decisions Needed

-

## Validation Completed

-

## Next Highest-Priority Action

-

## Deferred Until Later

-

---

# Changelog

## 2026-08-05 — Complete Roadmap Restored

- Restored the full document after earlier truncation.
- Updated the current blocker to documentation restoration and consistency review.
- Updated the remaining Phase 0 actions to reflect the actual repository state.
- Preserved the local vertical slice as the first implementation target.
- Deferred automation until local validation.
- Deferred secondary delivery and AI features.