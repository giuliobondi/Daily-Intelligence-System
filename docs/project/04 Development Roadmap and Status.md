````markdown
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
| Project Phase | Phase 2 complete — ready to begin Phase 3 GitHub Automation |
| Current Milestone | Milestone 3 — Validate the pipeline through manual GitHub Actions execution |
| Repository Status | Public Python repository with a validated deterministic real-source pipeline |
| Implementation Status | Local collection-to-report pipeline validated against seven real public RSS sources |
| Automation Status | GitHub Actions not yet implemented; `workflow_dispatch` is the next implementation step |
| Source Registry | Seven active validated public RSS sources |
| Taxonomy Status | Seven implemented domains; three target domains remain deferred |
| Testing Status | 110 automated tests passing |
| Current Blockers | No blocker to beginning manual GitHub Actions implementation |
| Current Priority | Implement the smallest GitHub Actions workflow and validate it manually before scheduling |

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
- Broad heterogeneous feeds may use no default domain rather than forcing every item into a misleading classification.
- Source defaults should represent a genuine source-wide topical guarantee rather than a broad publisher category.
- Unclassified records are preferable to misleading classifications.
- Retry logic should not be added without evidence that current bounded single-attempt collection is insufficient.

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

## Implemented Processing Modules

The processing core includes:

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

Phase 0 established the initial product, architecture, information policy and implementation sequence.

The canonical documents are updated as implementation changes rather than being treated as immutable historical snapshots.

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

The CLI constructs repository-default output paths and a previous-24-hours collection window.

## Phase 1 Controlled Configuration

Phase 1 intentionally used:

- one fixture/sample source;
- Technology and Software domain;
- Artificial Intelligence domain;
- deterministic ranking weights;
- configurable report limits.

That setup existed to validate pipeline behaviour before introducing real network and information-quality uncertainty.

## Key Implemented Behaviour

### Collection

Each source returns a structured result with status:

- `success`;
- `empty`;
- `failed`.

Expected source-level failures are isolated so one bad source does not discard successful source results.

### Normalisation and Identity

Records preserve useful source metadata while normalising titles, URLs and timestamps.

Record identity is deterministic from source identity and normalised URL.

### Validation

Invalid records are separated visibly from valid records before later processing.

### Collection Window

The reporting window is enforced rather than recorded only as metadata.

Current behaviour:

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

Classification uses source defaults plus deterministic keyword matching with word-boundary protection.

Multiple domains are allowed.

Unclassified records remain valid processed records but are omitted from the main report.

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

The pipeline emits lightweight standard-library logs for:

- pipeline start;
- source outcomes;
- validation counts;
- collection-window retention;
- duplicate counts;
- classification/ranking counts;
- output paths;
- final run status.

## Phase 1 Validation Completed

Phase 1 was validated through:

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

> **104 tests passed.**

A manual CLI run also exposed a real gap: the original pipeline recorded a collection window without enforcing it.

The missing filter was implemented, regression-tested and revalidated through the CLI.

This established the development pattern used in Phase 2:

> real output should drive the next justified change.

## Status

**Complete**

---

# Phase 2 — Minimal Real-Source Production Readiness

## Objective

Validate the local pipeline against a deliberately small real public source set before adding scheduled automation or speculative quality features.

The purpose was to discover real source, metadata, network and report-quality problems using the smallest useful production-like input set.

## Implemented Real-Source Set

The validated active registry contains seven public RSS sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Sifted.

The source set is intentionally small enough to remain inspectable.

Broad source expansion remains deferred until real use demonstrates a coverage gap.

## Implemented Taxonomy

The implemented taxonomy now contains seven active domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Companies and Corporate Strategy;
4. Artificial Intelligence;
5. Technology and Software;
6. Startups and Venture Capital;
7. Europe and the European Union.

The target taxonomy remains broader than the implemented subset.

The following target domains remain deferred:

- Financial Markets;
- Italy;
- Milan and Bocconi ecosystem.

## Network Production-Readiness Changes

Real-source testing exposed two concrete collector requirements:

- remote requests needed a bounded timeout;
- some feeds required an explicit User-Agent.

The collector was therefore hardened using ordinary Python standard-library networking.

Current remote collection behaviour:

```text
remote feed URL
→ urllib Request
→ explicit User-Agent and Accept headers
→ 10-second timeout
→ response bytes
→ feedparser
```

Expected HTTP, URL and timeout failures are converted into `CollectionError`.

Source-level failures remain isolated by `collect_source`.

Normal SSL certificate verification remains enabled.

No SSL bypass was introduced.

No new third-party HTTP dependency was added.

No retry policy was added because real-source testing did not demonstrate a current need for one.

## Real-Source Compatibility Validation

All seven selected feeds were collected successfully through the actual project collector.

Observed feed sizes during Phase 2 included:

- BBC World — approximately two dozen entries;
- BBC Business — approximately five dozen entries;
- ECB — 15 entries;
- European Commission — 30 entries;
- Istat — 10 entries;
- OpenAI — more than one thousand entries;
- Sifted — approximately two dozen entries.

The large OpenAI feed did not create a blocker because collection-window filtering reduces the eligible record set after validation.

All entries returned by the seven feeds during the compatibility test normalised successfully.

No missing publication timestamps were observed in the tested entries.

Missing descriptions occurred for some feeds and entries but were already valid under the current optional-description model.

No change to timestamp fallback logic or normalisation architecture was justified.

## Source-Default Classification Correction

The first full real-source report exposed misleading classification caused by overly broad source defaults.

Examples included:

- unrelated BBC Business items being forced into Economics and Macroeconomics;
- an ECB concert announcement being classified as Economics and Europe/EU;
- relevance scores being inflated by domains assigned solely from broad publisher defaults.

The smallest correction was to make `default_domains` explicitly optional.

Broad sources may now use:

```yaml
default_domains: []
```

Current default-domain policy:

- BBC News World → no default domain;
- BBC News Business → no default domain;
- European Central Bank → no default domain;
- European Commission Highlighted News → no default domain;
- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

This policy reflects the rule:

> A source default should represent a genuine source-wide topical guarantee, not merely the general category of the publisher.

`geographic_scope` remains required and non-empty.

Domain keyword lists remain required and non-empty.

## Evidence-Based Keyword Adjustment

Removing broad source defaults improved precision but exposed a recall gap in Global Politics and Geopolitics.

Real in-window BBC World items were manually reviewed.

Candidate keywords were simulated against the actual processed sample before configuration was changed.

The following keywords were added because they recovered clearly relevant political or geopolitical stories without observed false positives in the sample:

- `war`;
- `conflict`;
- `parliament`.

Several broader candidates were tested but deliberately not added, including terms such as:

- `government`;
- `defence`;
- `president`;
- `prime minister`.

Those terms produced ambiguous or low-value matches in the observed sample.

This preserves the policy of preferring under-classification over noisy classification.

## Real Report Validation

The first production-like run succeeded technically but exposed classification noise.

The initial report displayed 15 items.

After removing inappropriate broad source defaults, the report became smaller and more credible, displaying 8 items.

After the evidence-based Global Politics keyword additions, the report displayed 11 items across useful sections including:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Artificial Intelligence;
- Startups and Venture Capital.

This iterative inspection demonstrated that technical success alone is insufficient and that real report quality should drive deterministic corrections.

The resulting report was judged useful enough to justify moving to automation without further tuning from a single day of data.

Broader ranking, source-concentration and classification-quality evaluation remains deferred until actual scheduled use provides longitudinal evidence.

## Degraded Real-Source Validation

A temporary controlled run was executed using:

- one valid real Istat source;
- one deliberately invalid remote source.

Observed behaviour:

- Istat collection succeeded;
- the invalid source failed with `CollectionError`;
- the overall run status became `degraded`;
- the failure appeared in structured warnings;
- the valid Istat record still reached the final report;
- successful-source output was preserved.

This confirms real-network partial-source failure isolation rather than relying only on fixture tests.

## Phase 2 Validation Completed

Phase 2 validation included:

- direct live feed compatibility probing;
- hardened collector tests;
- real collection through the actual project collector;
- normalization of all returned entries from the seven selected feeds;
- repeated full-suite automated testing;
- real CLI execution;
- real JSONL inspection;
- real Markdown report inspection;
- real run-summary inspection;
- classification coverage review;
- simulated keyword evaluation against the actual processed sample;
- deliberate degraded real-network execution;
- repeated report-quality comparison after deterministic corrections.

At Phase 2 closeout:

> **110 automated tests pass.**

The manual Phase 2 runtime artifacts were used for validation and then removed rather than automatically treated as permanent repository history.

Production persistence policy will be implemented and validated during GitHub Actions work.

## Completion Criteria

Phase 2 is complete because:

- a small real-source set can be collected manually and repeatedly;
- remote requests use an explicit bounded timeout;
- feeds that require a User-Agent collect successfully;
- normal SSL verification remains intact;
- source failures remain isolated and visible;
- publication timestamps behave adequately for the current 24-hour reporting window;
- real metadata survives normalization;
- all tested real entries normalised successfully;
- real JSONL, Markdown and run-summary outputs were generated and inspected;
- report-quality problems were identified from real output;
- only small deterministic corrections justified by evidence were added;
- misleading broad source defaults were removed;
- conservative classification recall was improved with tested keywords;
- the report is useful enough to justify automated execution;
- a deliberate real-network failure produced a usable degraded run;
- the full automated suite passes;
- zero recurring monetary cost remains intact;
- no production AI dependency was introduced.

## Status

**Complete**

---

# Phase 3 — GitHub Automation

## Objective

Run the validated real-source pipeline automatically in the public repository with zero recurring monetary cost.

## Scope

Phase 3 should remain narrowly focused on execution and persistence.

Implement:

- a GitHub Actions workflow;
- `workflow_dispatch` for manual execution;
- minimal repository permissions;
- an explicit workflow timeout;
- overlap protection where justified;
- deterministic package installation;
- configuration validation;
- pipeline execution;
- generated-output validation;
- visible logs and failures;
- one coherent automated output commit when files actually change;
- no empty commits.

Scheduled execution should be enabled only after manual Actions validation succeeds.

## Entry Condition

Phase 2 real-source production-readiness validation is complete.

This condition is now satisfied.

## First Implementation Rule

Do not begin with scheduled daily execution.

First prove the exact production workflow manually through:

```text
workflow_dispatch
→ environment setup
→ package installation
→ pipeline execution
→ output inspection
→ commit behaviour inspection
→ failure inspection
```

Only after that workflow is stable should a schedule be enabled.

## Completion Criteria

Phase 3 is complete when:

- `workflow_dispatch` completes successfully;
- valid outputs are generated in the repository;
- one coherent automated commit is created when appropriate;
- no-change runs avoid empty commits;
- failed-source behaviour remains visible;
- critical configuration failures stop invalid publication;
- workflow permissions are minimal;
- logs are sufficient to diagnose failures;
- execution remains within the configured timeout;
- no AI credits or paid services are consumed;
- scheduled execution is enabled only after manual workflow validation.

## Validation

Phase 3 validation should include:

- inspect workflow permissions;
- manually trigger `workflow_dispatch`;
- inspect Actions logs;
- inspect generated JSONL, Markdown and run-summary files;
- inspect the automated commit;
- test a degraded-source run where practical;
- test a critical configuration failure;
- test a no-change run;
- verify no empty commit is created;
- verify generated paths are correct;
- confirm the workflow remains zero-cost under normal repository usage.

## Status

**Current active development phase**

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

## Milestone 3 — Validate Manual GitHub Actions Execution

### Objective

Move the validated real-source pipeline from local execution into the smallest reliable GitHub Actions workflow before scheduled automation is enabled.

### Required Outputs

- one minimal GitHub Actions workflow;
- manual `workflow_dispatch`;
- explicit workflow timeout;
- minimal repository permissions;
- deterministic package installation;
- pipeline execution using repository configuration;
- generated JSONL output;
- generated Markdown report;
- generated JSON run summary;
- visible failure logs;
- coherent commit behaviour when outputs change;
- no empty commit when outputs do not change.

### Validation Checklist

- [ ] Workflow can be triggered manually.
- [ ] Dependencies install successfully.
- [ ] Configuration loads successfully in Actions.
- [ ] Real feeds collect successfully in Actions.
- [ ] Generated paths are correct.
- [ ] JSONL output is inspectable.
- [ ] Markdown output is inspectable.
- [ ] Run-summary JSON is inspectable.
- [ ] Source-level failures remain visible.
- [ ] Critical failures stop invalid publication.
- [ ] Workflow permissions are minimal.
- [ ] Workflow has an explicit timeout.
- [ ] Changed outputs create one coherent commit.
- [ ] Unchanged outputs do not create an empty commit.
- [ ] No paid service or AI credit is consumed.
- [ ] Full automated tests still pass.

### Completion Action

When manual GitHub Actions execution is stable:

> Review the workflow, output persistence and failure behaviour before enabling scheduled daily execution.

Do not use successful local Phase 2 runs as justification to skip this manual Actions checkpoint.

---

# Deferred Features

| Feature | Status | Reason |
|---|---|---|
| Near-duplicate clustering | Deferred pending production evidence | Exact deduplication remains sufficient until repeated reports show material duplication |
| Multi-source story clustering | Deferred pending production evidence | Adds logic and false-merge risk without a validated current requirement |
| Geographic classification | Deferred pending production evidence | Geographic scope metadata exists; topic-level geography logic is not yet required |
| Entity tracking | Deferred pending production evidence | No demonstrated report-quality requirement |
| Content-type classification | Deferred pending production evidence | Current real reports do not justify the added logic |
| Broad source expansion | Deferred | Seven real sources are enough for the automation and initial-use phases |
| Financial Markets domain | Deferred | Target taxonomy domain not yet required by current real-source validation |
| Italy domain | Deferred | Geographic source metadata and current Economics coverage are sufficient for now |
| Milan and Bocconi domain | Deferred | No validated stable structured source has yet justified implementation |
| Source-health history | Deferred pending repeated automated runs | Current run summaries expose per-run health sufficiently |
| Advanced ranking | Deferred pending production evidence | Current deterministic score is adequate for initial automation |
| GitHub Issues delivery | Deferred | Repository-native reports should be used first |
| GitHub Pages | Deferred | Avoid frontend work before repository browsing is demonstrated to be insufficient |
| Newsletter-email ingestion | Rejected for core MVP | Adds privacy, authentication and workflow complexity |
| Public newsletter feeds | Possible later | May be added as ordinary structured sources if valuable and compliant |
| LLM summaries | Rejected for core MVP | Recurring cost and unnecessary dependency |
| Automated ChatGPT integration | Rejected for core MVP | Violates the deterministic zero-cost architecture |
| Machine-learning classification | Rejected for core MVP | Deterministic logic should remain default until proven insufficient |
| Embeddings and semantic search | Rejected for core MVP | No validated need |
| RAG | Rejected for core MVP | No validated workflow problem |
| Autonomous agents | Rejected for core MVP | Adds complexity without current value |
| Cloud database | Rejected for core MVP | Repository-native JSONL remains sufficient initially |
| Private source ingestion | Rejected for core MVP | Conflicts with public-repository and privacy boundaries |
| Multi-user support | Rejected for core MVP | Initial product is single-user |

---

# Project Risks

## Planning Without Use

The project may accumulate architecture or quality features before producing value from real information.

**Control:** Phase 3 focuses only on putting the validated pipeline into reliable GitHub-native execution.

## Scope Expansion

Features may be added because they are technically interesting rather than because the report needs them.

**Control:** every material feature outside automation must solve a documented observed limitation.

## Premature Source Expansion

A larger source registry may create noise and maintenance before the seven-source set has been evaluated in repeated production use.

**Control:** keep the current seven-source registry through initial automation unless a concrete coverage gap appears.

## Weak Information Quality

The pipeline may run correctly while producing a noisy, repetitive or unhelpful report.

**Control:** Phase 2 established manual report inspection and conservative classification; Phase 4 will evaluate quality longitudinally.

## Network and Feed Instability

Real RSS/Atom sources may fail, hang, change format or publish inconsistent metadata.

**Control:** source-level isolation, explicit 10-second timeout behaviour, clear User-Agent handling, conservative source selection, run summaries and visible warnings.

## GitHub Actions Complexity

Automation may introduce unnecessary workflow logic or repository-write risk.

**Control:** begin with `workflow_dispatch`, minimal permissions and one coherent workflow; schedule only after manual validation.

## Repository Growth

Daily JSON and Markdown files may accumulate indefinitely.

**Control:** keep the initial repository-native storage model and review retention only after real production usage provides evidence.

## Maintenance Burden

Source instability may create recurring manual work.

**Control:** prefer stable structured sources, remove low-value sources and avoid compensating for poor sources with complex code.

## Misleading Success States

A technically completed run may conceal failed sources or incomplete output.

**Control:** structured run status, user-facing report metadata, warnings, logs and automated publication rules must remain aligned.

## Installed-Package Freshness During Local Development

A locally installed package may lag behind the source tree even when source-based tests pass.

**Control:** remember that pytest can exercise the repository source tree while `python -m daily_intelligence.cli` may execute an installed package copy. Refresh the installation when CLI behaviour does not reflect validated source changes.

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

**Status: passed**

Required:

- local pipeline remains stable;
- a small real-source set has been validated manually;
- network timeout/error behaviour is acceptable;
- report generation is repeatable with real data;
- failure modes are understood;
- output is useful enough to justify automation.

Evidence:

- seven real public feeds validated;
- remote requests bounded by a 10-second timeout;
- User-Agent requirement observed and implemented;
- real reports generated repeatedly;
- classification noise identified and corrected conservatively;
- real degraded-source behaviour validated;
- 110 automated tests passing;
- zero recurring monetary cost preserved.

Gate 3 passing means GitHub Actions implementation may begin.

It does not mean scheduled execution should be enabled immediately.

## Gate 4 — Expand Sources or Quality Logic

**Status: not yet passed for broad expansion**

Required:

- a concrete coverage, repetition, classification or ranking gap is demonstrated;
- proposed changes solve that observed gap;
- added maintenance is proportionate;
- the simpler current system is insufficient.

Phase 2 demonstrated small classification gaps and justified narrow corrections.

It did not justify broad source expansion, near-duplicate clustering or major ranking redesign.

## Gate 5 — Add Delivery Features

**Status: not yet passed**

Required:

- reports are being used;
- repository browsing is a demonstrated usability limitation;
- the proposed delivery feature remains zero-cost and low-maintenance.

---

# Status Tracking

## Current Phase

Phase 3 — GitHub Automation.

## Current Milestone

Milestone 3 — Validate Manual GitHub Actions Execution.

## Completed Since Last Documentation Baseline

- selected and validated seven real public RSS sources;
- expanded the implemented taxonomy from two to seven domains;
- retained three target domains as deferred;
- hardened remote collection with explicit request headers and a 10-second timeout;
- preserved normal SSL verification;
- validated redirects and live feed parsing;
- validated all returned entries from the selected feeds through normalization;
- confirmed tested real feeds provided usable publication timestamps;
- kept missing descriptions optional;
- made `default_domains` explicitly empty-capable for broad sources;
- removed misleading broad source defaults after real report inspection;
- retained narrow source defaults only for Istat, OpenAI and Sifted;
- added `war`, `conflict` and `parliament` to Global Politics after simulation against real processed records;
- deliberately rejected broader ambiguous candidate keywords;
- generated and inspected real JSONL, Markdown and JSON run summaries;
- improved report quality through evidence-based deterministic changes;
- validated real-network degraded-source behaviour;
- preserved successful output when one source failed;
- removed manual validation artifacts rather than treating them as production history;
- kept retry logic, near-duplicate detection, advanced ranking and broader taxonomy expansion deferred;
- reached 110 passing automated tests.

## Active Work

- reconcile canonical project documents with the completed Phase 2 implementation;
- prepare the smallest GitHub Actions `workflow_dispatch` implementation.

## Blockers

No current blocker to beginning Phase 3.

Scheduling remains intentionally blocked until manual GitHub Actions execution and repository persistence are validated.

## Decisions Needed During Phase 3

Resolve only the automation decisions necessary for the first manual workflow:

- exact workflow file structure;
- minimal required GitHub permissions;
- explicit Actions timeout;
- package-install strategy in the runner;
- output validation before commit;
- commit conditions;
- no-change behaviour;
- concurrency behaviour if needed;
- handling of degraded versus critical failures;
- exact transition condition from manual `workflow_dispatch` to scheduled execution.

Do not introduce unrelated quality features while resolving these decisions.

## Validation Completed

- 110 passing automated tests;
- targeted collection/configuration/classification regression suites;
- live collection through the actual project collector;
- seven-source compatibility validation;
- normalization of all observed returned real-feed entries;
- real 24-hour pipeline runs;
- real JSONL inspection;
- real Markdown report inspection;
- real run-summary inspection;
- classification coverage analysis by source;
- keyword simulations against real records;
- report comparison before and after source-default corrections;
- deliberate unavailable-source real-network run;
- degraded status and warning validation;
- confirmation that successful-source output survives another source's failure.

## Next Highest-Priority Action

After the canonical documentation refresh is complete:

> Implement the smallest GitHub Actions workflow with `workflow_dispatch`, minimal permissions and an explicit timeout, then validate one manual Actions run before adding any schedule.

## Deferred Until Later

- scheduled automation until manual Actions validation passes;
- broad source expansion;
- Financial Markets domain;
- Italy domain;
- Milan and Bocconi domain;
- near-duplicate logic;
- entities;
- geography classification;
- content types;
- source-health history;
- advanced ranking;
- delivery interfaces;
- AI-generated content.

---

# Changelog

## 2026-08-11 — Phase 2 Real-Source Production Readiness Completed

- Selected and validated seven public real-source RSS feeds.
- Hardened remote collection with explicit request headers and a 10-second timeout.
- Confirmed normal SSL verification and real-source redirect behaviour.
- Kept retry logic absent because current evidence did not justify it.
- Validated real feed metadata and publication timestamps through the existing normalizer.
- Expanded the implemented taxonomy from two to seven domains without expanding the full target taxonomy.
- Added support for empty `default_domains` for broad heterogeneous sources.
- Replaced misleading broad source defaults with conservative source-wide defaults.
- Used real report inspection to identify classification false positives.
- Added `war`, `conflict` and `parliament` only after testing candidate keywords against real processed records.
- Generated and manually inspected real JSONL, Markdown and run-summary outputs.
- Improved the real report from a noisy initial version to a smaller, more credible output.
- Validated deliberate real-network partial-source failure and degraded-run behaviour.
- Reached 110 passing automated tests.
- Removed manual Phase 2 runtime artifacts pending the automated persistence design.
- Marked Phase 2 complete.
- Passed Gate 3 and made Phase 3 GitHub Automation the active phase.
- Defined Milestone 3 as manual `workflow_dispatch` validation before scheduled execution.

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
````
