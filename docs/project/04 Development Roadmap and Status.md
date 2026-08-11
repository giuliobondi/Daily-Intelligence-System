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
- Start from the user need and workflow, not from a preferred technology.
- Prefer working output over additional infrastructure.
- Do not create features without a validated need.
- Prefer the simplest solution that satisfies the requirement.
- Do not add recurring monetary cost.
- Do not introduce production AI calls.
- Keep daily manual work negligible.
- Prefer RSS, official APIs and other structured public sources before scraping.
- Prefer deterministic rules before machine learning or LLM-based logic.
- Validate locally before enabling automation.
- Use Git and tests as the verification layer for every material change.
- Keep the repository public-safe.
- Stop at stable checkpoints.
- Treat technically successful execution as insufficient if the report is noisy, repetitive, misleading or too long.

The project should not move to the next phase until the current phase has a clear completion condition.

---

# Current Project Status

| Field | Current Status |
|---|---|
| Project Phase | Phase 1 complete — transition to Phase 2 production-readiness validation |
| Current Milestone | Milestone 2 — Validate a minimal real-source run before automation |
| Repository Status | Public Python repository with a working local deterministic pipeline |
| Implementation Status | Local collection-to-report vertical slice complete and validated |
| Automation Status | GitHub Actions not yet implemented |
| Source Registry | One controlled fixture/sample source; production source set not yet selected |
| Taxonomy Status | Two implemented domains: Technology and Software; Artificial Intelligence |
| Testing Status | 104 tests passing at Phase 1 closeout |
| Current Blockers | No Phase 1 implementation blocker; production network/source behaviour still unvalidated |
| Current Priority | Refresh canonical project documents, then validate the smallest real-source run before GitHub Actions |

---

# Completed Work

## Project Decisions

The following decisions are established unless explicitly changed later:

- Use a hybrid information model:
  - ChatGPT provides independent interpretation and synthesis outside the production pipeline.
  - GitHub and Python provide deterministic collection, organisation, ranking, reporting and archiving.
- Zero recurring monetary cost is a hard constraint.
- Daily manual work should be negligible.
- Production must not consume GitHub AI, Copilot or other recurring AI credits.
- Public structured sources are the default input class.
- RSS and Atom are the first supported source types.
- Production automation will use ordinary Python and GitHub Actions.
- The core system will not depend on LLM calls, agents, RAG, embeddings, vector databases or paid APIs.
- The repository remains public.
- Private Career OS materials remain outside the repository.
- Processed records use JSON Lines.
- Run summaries use JSON.
- Daily reports use Markdown.
- Internal timestamps use timezone-aware UTC datetimes.
- Reports use one primary placement per item, with secondary domains shown as metadata.
- Relevance scoring is deterministic and explainable.
- Automated repository persistence remains the intended initial delivery model once GitHub Actions is implemented.
- GitHub Issues, GitHub Pages and newsletter ingestion remain deferred.

## Repository and Package Setup

Completed repository foundations include:

- public GitHub repository;
- `README.md`;
- `.gitignore`;
- `LICENSE`;
- `pyproject.toml`;
- `config/`;
- `src/daily_intelligence/`;
- `tests/` and controlled fixtures;
- `docs/project/` for canonical project documentation.

The Python package uses a `src/` layout and requires Python 3.12 or later.

## Implemented Phase 1 Modules

The local processing core now includes:

```text
src/daily_intelligence/
├── __init__.py
├── cli.py
├── classify.py
├── collect.py
├── config.py
├── deduplicate.py
├── filter_window.py
├── models.py
├── normalize.py
├── pipeline.py
├── rank.py
├── report.py
├── run_summary.py
├── storage.py
└── validate.py
```

The exact repository tree remains the source of truth if file names later change.

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
- establish repository structure;
- make hard constraints explicit;
- separate current requirements from deferred ideas.

## Completion Criteria

Phase 0 is complete when:

- documents `00` through `04` are internally consistent enough to guide implementation;
- no major contradiction blocks the local vertical slice;
- unresolved decisions are explicitly visible;
- the MVP boundary is clear;
- the next implementation milestone is defined;
- repository foundations exist.

## Status

**Complete**

## Completion Notes

Phase 0 established the initial product, architecture, information policy and implementation sequence. The original documents later became stale as implementation progressed, so they are being refreshed after Phase 1 rather than treated as immutable historical snapshots.

---

# Phase 1 — Local Vertical Slice

## Objective

Build the smallest complete local pipeline that proves the core workflow from collection to readable output.

## Implemented Scope

Phase 1 implemented and validated:

1. configuration loading;
2. RSS/Atom collection from controlled inputs;
3. structured source-level collection results;
4. record normalisation;
5. required-field validation;
6. deterministic collection-window filtering;
7. exact duplicate reduction;
8. simple deterministic domain classification;
9. provisional deterministic relevance scoring;
10. JSON Lines persistence;
11. deterministic Markdown report selection and rendering;
12. structured JSON run summaries;
13. end-to-end local orchestration;
14. one-command CLI execution;
15. source-level failure isolation and degraded-run behaviour;
16. user-facing operational report metadata and warnings;
17. minimal standard-library run-level logging;
18. automated tests for critical deterministic logic and integration paths.

## Local Execution

The pipeline can be run locally with:

```text
python -m daily_intelligence.cli run
```

The CLI currently constructs repository-default output paths and a previous-24-hours collection window.

## Current Controlled Configuration

Phase 1 intentionally uses a narrow controlled setup:

- one fixture/sample source;
- Technology and Software domain;
- Artificial Intelligence domain;
- deterministic ranking weights;
- configurable report limits.

This configuration validates pipeline behaviour. It is not intended to represent the final production source universe or taxonomy coverage.

## Key Implemented Behaviour

### Collection

Each source returns a structured result with status:

- `success`;
- `empty`;
- `failed`.

Expected source-level failures are isolated so one bad source does not discard successful source results.

### Normalisation and Identity

Records preserve useful source metadata while normalising titles, URLs and timestamps. Record identity is deterministic from source identity and normalised URL.

### Validation

Invalid records are separated visibly from valid records before later processing.

### Collection Window

The reporting window is now enforced rather than recorded only as metadata.

Current Phase 1 behaviour:

- requires timezone-aware window boundaries;
- uses inclusive boundaries;
- excludes records published before or after the window;
- excludes records without a confirmed publication timestamp;
- rejects reversed windows.

### Deduplication

Current exact duplicate handling uses:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

### Classification

Classification uses source defaults plus deterministic keyword matching with word-boundary protection. Multiple domains are allowed. Unclassified records remain valid processed records but are omitted from the main report.

### Ranking

The current provisional score is deterministic and based on:

- configured source tier;
- number of domain matches;
- number of keyword matches.

Score components are stored for transparency.

### Storage and Reporting

Processed records are written as JSON Lines using deterministic overwrite semantics for a target file.

The Markdown report:

- applies deterministic selection;
- respects total and per-domain limits;
- places each item once under a primary domain;
- shows secondary domains as metadata;
- shows relevance score;
- uses only feed-provided descriptions;
- truncates descriptions to configuration limits;
- omits unclassified records from the main report;
- exposes run status, monitored window, source health, collected count and displayed count;
- exposes warnings on degraded runs.

### Run Summary and Logging

Each run produces a structured JSON summary containing operational counts, status, warnings and monitored window.

The pipeline also emits lightweight standard-library logs for:

- pipeline start;
- source outcomes;
- validation counts;
- collection-window retention;
- duplicate counts;
- classification/ranking counts;
- output paths;
- final run status.

## Validation Completed

Phase 1 has been validated through:

- unit tests for deterministic modules;
- controlled feed fixture tests;
- end-to-end pipeline integration tests;
- degraded source integration testing;
- collection-window boundary and exclusion tests;
- report-selection and operational-header tests;
- CLI invocation tests;
- logging tests;
- manual one-command CLI runs;
- generated JSONL inspection;
- generated Markdown inspection;
- run-summary inspection;
- repeated full-suite execution.

At Phase 1 closeout:

> **104 tests pass.**

A manual CLI run also exposed a real gap: the original pipeline recorded a collection window without enforcing it. The missing filter was then implemented, regression-tested and revalidated through the CLI. This is the model for future development: real output should drive the next justified change.

## Completion Criteria

Phase 1 is complete because:

- the pipeline runs locally from one command;
- controlled feeds are collected successfully;
- valid records are normalised;
- invalid records are handled visibly;
- the reporting window is enforced;
- exact duplicates are reduced;
- deterministic classification and scoring work;
- processed JSON Lines are written;
- a readable bounded Markdown report is generated;
- a structured run summary is written;
- degraded runs remain usable and visibly incomplete;
- repeated writes to the same target are deterministic;
- critical deterministic behaviour has automated tests;
- run-level logs are inspectable;
- no paid service or production AI call is used.

## Status

**Complete**

---

# Phase 2 — Minimal Real-Source Production Readiness

## Objective

Validate the local pipeline against a very small real public source set before adding scheduled automation or speculative quality features.

The purpose is to discover real source, metadata, network and report-quality problems with the smallest possible production-like input set.

## Why This Phase Comes Next

The earlier roadmap placed a large quality-logic phase before GitHub Actions. That sequence is no longer justified.

Phase 1 proved the deterministic pipeline technically. The next unknowns are now external and operational:

- live HTTP behaviour;
- source reliability;
- publication timestamp quality;
- feed metadata quality;
- output usefulness with real information;
- maintenance burden.

Near-duplicate clustering, entity tracking, geography logic and similar features should not be built until real output demonstrates a meaningful need.

## Scope

Use a deliberately small real-source set and implement only the production-readiness work required to run it reliably.

Likely scope:

- select a small number of high-quality public RSS/Atom sources;
- preserve the existing source-policy hierarchy;
- validate live HTTP collection behaviour;
- add explicit network timeouts if required by the current collector;
- add conservative retry behaviour only if justified;
- use a clear user agent where appropriate;
- inspect malformed or unusual feed behaviour;
- inspect publication timestamps and timezone handling;
- inspect source descriptions and URLs;
- inspect report relevance and repetition;
- adjust only deterministic rules that fail on observed cases;
- preserve source-level failure isolation;
- keep the source set small enough for manual quality review.

## Deliberately Excluded

Unless real-source validation proves they are needed, do not add:

- near-duplicate clustering;
- semantic similarity;
- entity extraction;
- geographic classification;
- content-type classification;
- machine learning;
- LLM calls;
- embeddings;
- RAG;
- a large source registry;
- dashboards;
- frontends;
- GitHub Issues delivery;
- GitHub Pages.

## Entry Condition

Phase 1 local vertical slice is complete.

## Completion Criteria

Phase 2 is complete when:

- a small real-source set can be collected manually and repeatably;
- live-source requests use acceptable timeout/error behaviour;
- source failures remain isolated and visible;
- publication timestamps behave predictably enough for the reporting window;
- generated reports contain real items and are manually inspectable;
- no critical metadata issue blocks the pipeline;
- obvious low-quality source choices are removed rather than compensated for with complexity;
- the report is useful enough to justify automated daily execution;
- no recurring monetary cost or production AI dependency has been introduced.

## Validation

- run the pipeline manually against the real-source set;
- inspect source-level logs;
- inspect failed/empty source behaviour;
- inspect publication timestamps;
- inspect JSONL records;
- inspect report relevance and repetition;
- inspect run summary;
- deliberately test one unavailable or invalid source;
- rerun with unchanged or similar inputs;
- run the full automated test suite after any code change.

## Status

**Next active development phase**

---

# Phase 3 — GitHub Automation

## Objective

Run the validated production-ready pipeline automatically in the public repository with zero recurring monetary cost.

## Scope

- create a GitHub Actions workflow;
- add `workflow_dispatch` for manual execution;
- use minimal repository permissions;
- set an explicit workflow timeout;
- prevent unnecessary overlap where appropriate;
- install the package and dependencies deterministically;
- run configuration validation;
- execute the pipeline;
- validate generated outputs;
- expose logs and failures clearly;
- create one coherent automated output commit when files actually change;
- avoid empty commits;
- enable scheduled execution only after manual Actions validation.

## Entry Condition

Phase 2 must show that the real-source pipeline is reliable enough to automate.

## Completion Criteria

Phase 3 is complete when:

- `workflow_dispatch` completes successfully;
- valid outputs are generated in the repository;
- one coherent automated commit is created when appropriate;
- no-change runs avoid empty commits;
- failed-source behaviour remains visible;
- critical failures stop invalid publication;
- workflow permissions are minimal;
- logs are sufficient to diagnose failures;
- execution stays within the configured timeout;
- no AI credits or paid services are consumed;
- scheduled execution is enabled only after manual workflow validation.

## Validation

- inspect workflow permissions;
- run through `workflow_dispatch`;
- inspect logs;
- inspect generated JSONL, report and run-summary files;
- inspect the automated commit;
- test a degraded source run;
- test a critical configuration failure;
- test a no-change run;
- confirm the workflow remains zero-cost under normal repository usage.

---

# Phase 4 — Initial Production Evaluation

## Objective

Evaluate whether the automated system is genuinely useful in daily use before expanding quality logic or delivery features.

## Evaluation Period

Approximately two weeks after stable scheduled automation begins.

## Questions

### Usage

- Is the report opened consistently?
- Can it be scanned in approximately 10–15 minutes?
- Are source links used selectively?

### Coverage

- Are major relevant stories missed?
- Are any important domains consistently empty?
- Are some domains overrepresented?

### Noise

- Are low-value items frequently displayed?
- Is promotional content overrepresented?
- Are obvious duplicate stories still common?

### Classification

- Are items assigned to useful domains?
- Is the unclassified rate acceptable?
- Are multi-domain items handled clearly?

### Ranking

- Do high-value items appear near the top?
- Do source-tier weights distort relevance?
- Are keyword matches creating noisy score inflation?

### Operations

- Do scheduled runs complete reliably?
- Are failures understandable?
- Is source maintenance acceptably low?
- Does the project remain at zero recurring cost?

## Completion Criteria

Phase 4 is complete when:

- approximately two weeks of reports have been reviewed;
- major weaknesses are documented with examples;
- low-value or unreliable sources are identified;
- useful sources are confirmed;
- ranking and classification problems are prioritised by observed impact;
- further development decisions are based on evidence rather than the original speculative roadmap.

---

# Phase 5 — Evidence-Driven Quality Expansion

## Objective

Add only quality features justified by production evidence.

## Possible Enhancements

Depending on observed limitations, this phase may include:

- broader source universe;
- conservative near-duplicate detection;
- multi-source story clustering;
- stronger domain classification;
- richer secondary-domain logic;
- geographic classification;
- content-type classification;
- tracked entities;
- source-quality penalties;
- source-health history;
- refined ranking weights;
- report-length adjustments;
- unclassified-item review tooling;
- concentration metrics;
- trend or archive analysis.

## Entry Rules

A feature should enter this phase only when:

- the problem is observed in real reports;
- the limitation materially reduces usefulness, reliability or maintainability;
- the proposed feature creates measurable value;
- a simpler deterministic solution is insufficient;
- recurring monetary cost remains zero;
- recurring AI-credit use remains zero;
- maintenance remains proportionate.

## Validation

Use evaluation appropriate to the observed problem, such as:

- curated fixtures;
- false-positive and false-negative duplicate review;
- manual classification samples;
- ranking comparison with human judgment;
- unclassified-item rates;
- publisher/domain concentration;
- source-health history;
- report-length and repetition review.

---

# Phase 6 — Optional Delivery and Interface Improvements

## Objective

Improve access only if repository-native Markdown reports become a demonstrated usability limitation.

## Possible Enhancements

- GitHub Issues delivery;
- GitHub Pages;
- weekly archive summaries;
- opportunity-specific views;
- other zero-cost delivery improvements.

## Entry Condition

Reports must already be used in practice and the delivery limitation must be observed rather than assumed.

## Excluded by Default

- paid APIs;
- automated ChatGPT integration;
- private email ingestion;
- full-article extraction;
- autonomous agents;
- RAG;
- vector databases;
- complex cloud infrastructure;
- sophisticated frontend development;
- mobile application development.

---

# Current Milestone

## Milestone 2 — Validate a Minimal Real-Source Run Before Automation

### Objective

Move from controlled fixtures to a deliberately small production-like source set without expanding the system unnecessarily.

### Required Outputs

- a small approved real-source subset in `config/sources.yaml`;
- reliable live collection behaviour;
- explicit request timeout/error handling where needed;
- real JSONL output;
- real Markdown report;
- real JSON run summary;
- manual quality inspection notes;
- tests for any newly discovered deterministic edge cases.

### Validation Checklist

- [ ] Real feeds can be collected manually.
- [ ] Network requests cannot hang indefinitely.
- [ ] Source-level failures remain isolated.
- [ ] Publication timestamps are usable for collection-window filtering.
- [ ] Real records preserve useful source metadata.
- [ ] The report contains relevant real items.
- [ ] Obvious noise or duplication is documented.
- [ ] No speculative quality feature has been added without evidence.
- [ ] No recurring monetary cost has been introduced.
- [ ] Full automated tests still pass.

### Completion Action

When the real-source slice is stable, stop and review whether the system is ready for `workflow_dispatch` and GitHub Actions rather than automatically expanding the source set or taxonomy.

---

# Deferred Features

| Feature | Status | Reason |
|---|---|---|
| Near-duplicate clustering | Deferred pending evidence | Exact deduplication is sufficient until real reports show material repetition |
| Multi-source story clustering | Deferred pending evidence | Adds logic and false-merge risk without a validated current need |
| Geographic classification | Deferred pending evidence | Current controlled taxonomy does not require it yet |
| Entity tracking | Deferred pending evidence | No demonstrated report-quality requirement yet |
| Content-type classification | Deferred pending evidence | Keep Phase 2 focused on real-source reliability |
| Broad source expansion | Deferred | Start with a small production-quality set and expand only when coverage gaps are demonstrated |
| GitHub Issues delivery | Deferred | Core repository report should be validated first |
| GitHub Pages | Deferred | Avoid frontend work before repository browsing is proven insufficient |
| Newsletter-email ingestion | Rejected for core MVP | Adds privacy, authentication and workflow complexity |
| Public newsletter feeds | Possible later | May be added as ordinary structured sources if valuable and compliant |
| LLM summaries | Rejected for core MVP | Recurring cost and unnecessary dependency |
| Automated ChatGPT integration | Rejected for core MVP | Violates the deterministic zero-cost architecture |
| Machine-learning classification | Rejected for core MVP | Deterministic logic should remain default until insufficient |
| Embeddings and semantic search | Rejected for core MVP | No validated need |
| RAG | Rejected for core MVP | No validated workflow problem |
| Autonomous agents | Rejected for core MVP | Adds complexity without current value |
| Cloud database | Rejected for core MVP | Repository-native JSONL is sufficient initially |
| Private source ingestion | Rejected for core MVP | Conflicts with public-repository and privacy boundaries |
| Multi-user support | Rejected for core MVP | Initial product is single-user |

---

# Project Risks

## Planning Without Use

The project may accumulate architecture or quality features before producing value from real information.

**Control:** the next milestone is a minimal real-source run, not another planning or infrastructure phase.

## Scope Expansion

Features may be added because they are technically interesting rather than because the report needs them.

**Control:** every material feature must solve a documented observed limitation.

## Premature Source Expansion

A large source registry may create noise and maintenance before source quality is understood.

**Control:** Phase 2 uses a deliberately small real-source set.

## Weak Information Quality

The pipeline may run correctly while producing a noisy, repetitive or unhelpful report.

**Control:** manual report inspection remains a required validation step; technical success alone is not sufficient.

## Network and Feed Instability

Real RSS/Atom sources may fail, hang, change format or publish inconsistent timestamps.

**Control:** source-level isolation, explicit timeout/error behaviour, conservative source selection and visible run summaries.

## GitHub Actions Complexity

Automation may be added before real-source behaviour is understood.

**Control:** GitHub Actions starts only after minimal real-source validation.

## Repository Growth

Daily JSON and Markdown files may accumulate indefinitely.

**Control:** keep the initial repository-native storage model and review retention only after real production usage provides evidence.

## Maintenance Burden

Source instability may create recurring manual work.

**Control:** prefer stable structured sources, remove low-value sources, and avoid compensating for poor sources with complex code.

## Misleading Success States

A technically completed run may conceal failed sources or incomplete output.

**Control:** structured run status, user-facing report metadata, warnings and logs must remain aligned.

---

# Decision Gates

The following gates prevent premature expansion.

## Gate 1 — Begin Implementation

**Status: passed**

Required:

- core project documents existed;
- repository foundations existed;
- no major unresolved blocker prevented the local slice.

## Gate 2 — Complete the Local Vertical Slice

**Status: passed**

Required:

- local end-to-end pipeline works;
- collection-window filtering works;
- exact duplicate handling works;
- deterministic classification and ranking work;
- output is inspectable;
- failures are visible;
- initial tests pass;
- one-command local execution works.

## Gate 3 — Add GitHub Actions

**Status: not yet passed**

Required:

- local pipeline remains stable;
- a small real-source set has been validated manually;
- network timeout/error behaviour is acceptable;
- report generation is repeatable with real data;
- failure modes are understood;
- output is useful enough to justify automation.

## Gate 4 — Expand Sources or Quality Logic

**Status: not yet passed**

Required:

- a concrete coverage, repetition, classification or ranking gap is demonstrated;
- proposed changes solve that observed gap;
- added maintenance is proportionate;
- the simpler current system is insufficient.

## Gate 5 — Add Delivery Features

**Status: not yet passed**

Required:

- reports are being used;
- repository browsing is a demonstrated usability limitation;
- the proposed delivery feature remains zero-cost and low-maintenance.

---

# Status Tracking

## Current Phase

Phase 1 complete; transitioning into Phase 2 — Minimal Real-Source Production Readiness.

## Current Milestone

Milestone 2 — Validate a Minimal Real-Source Run Before Automation.

## Completed Since Last Documentation Baseline

- implemented the full local deterministic pipeline;
- added structured source-level collection results;
- implemented normalisation and deterministic record identity;
- implemented record validation;
- implemented exact deduplication;
- implemented deterministic classification and ranking;
- implemented JSONL storage;
- implemented deterministic Markdown reporting;
- implemented structured run summaries;
- implemented end-to-end orchestration;
- added a one-command local CLI;
- added collection-window filtering after manual validation exposed the missing enforcement;
- validated degraded partial-source behaviour;
- added operational status, source health, monitored window and warnings to the Markdown report;
- added minimal run-level logging;
- validated the full local workflow manually;
- reached 104 passing automated tests at Phase 1 closeout.

## Active Work

- refresh project documents `00` through `04` so canonical documentation matches the implemented system;
- prepare the minimal real-source validation milestone.

## Blockers

No current Phase 1 blocker.

Before automation, live network/source behaviour remains intentionally unvalidated.

## Decisions Needed

Before or during Phase 2:

- exact small real-source set for first production-like run;
- request timeout policy based on current collector implementation and live-source behaviour;
- whether a minimal retry policy is necessary;
- whether the current 24-hour collection window remains appropriate for real sources;
- whether any real feed requires a revised missing-publication-time policy.

These decisions should be resolved from evidence rather than assumed in advance.

## Validation Completed

- 104 passing tests at Phase 1 closeout;
- targeted unit and integration suites;
- degraded-run test;
- collection-window regression test;
- CLI invocation test;
- logging test;
- manual CLI execution;
- manual inspection of generated JSONL, Markdown and JSON run summary.

## Next Highest-Priority Action

After the documentation refresh is complete:

> Select the smallest credible real RSS/Atom source set and validate one manual production-like run before building GitHub Actions.

## Deferred Until Later

- broad taxonomy expansion;
- near-duplicate logic;
- entities;
- geography;
- content types;
- source-health history;
- advanced ranking;
- scheduled automation;
- delivery interfaces;
- AI-generated content.

---

# Changelog

## 2026-08-11 — Phase 1 Local Vertical Slice Completed

- Replaced the stale Phase 0 implementation status with the validated repository state.
- Marked Phase 0 and Phase 1 complete.
- Recorded the implemented local pipeline, CLI, collection-window filtering, operational reporting and logging.
- Recorded 104 passing tests at Phase 1 closeout.
- Reordered the roadmap so minimal real-source production-readiness validation precedes GitHub Actions.
- Moved speculative quality features behind evidence from real reports.
- Preserved zero recurring cost, deterministic processing, negligible daily manual work and public-repository safety as fixed constraints.
- Defined Milestone 2 as the next active development milestone.

## 2026-08-05 — Initial Roadmap Baseline

- Restored the original project roadmap and project-control structure.
- Defined the local vertical slice as the first implementation phase.
- Deferred automation, delivery features and production AI until the deterministic core was validated.