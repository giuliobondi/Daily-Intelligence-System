# Daily Intelligence System — System Architecture

> **Purpose**
>
> This document defines the technical architecture of the Daily Intelligence System.
>
> It describes the implemented processing model, component boundaries, data flow, storage model, configuration model, failure behaviour, observability and the architectural constraints that govern future development.
>
> It is not the implementation-status tracker. Current phase, milestone and development sequencing belong in `04 Development Roadmap and Status.md`.
>
> ---
>
> **Primary Question**
>
> > *How is the Daily Intelligence System structured, how does information move through it, and which architectural decisions are fixed, implemented, planned or deferred?*
>
> ---
>
> **Architecture Principle**
>
> The system should remain a small deterministic information pipeline unless real usage demonstrates that additional complexity creates material value.

---

# 1. Architecture Goals

The architecture should satisfy the following priorities, in order:

1. zero recurring monetary cost;
2. reliability;
3. negligible recurring manual work;
4. information and source quality;
5. maintainability;
6. transparency and auditability;
7. security and privacy;
8. learning and signaling value;
9. technical sophistication.

The architecture should therefore prefer:

- ordinary Python;
- GitHub-native automation;
- structured public sources;
- deterministic processing;
- explicit configuration;
- inspectable intermediate data;
- local files rather than unnecessary databases;
- standard-library capabilities where practical;
- small modules with clear responsibilities;
- visible failure states;
- tests for important deterministic behaviour.

The architecture should avoid:

- paid APIs;
- paid news services;
- automation platforms with recurring fees;
- production LLM calls;
- GitHub AI or Copilot credit consumption;
- agents;
- RAG;
- embeddings;
- vector databases;
- cloud infrastructure;
- private newsletter ingestion;
- complex frontend applications;
- machine-learning components without a validated need.

---

# 2. Architectural Status

The deterministic local processing core is implemented and validated.

The current architecture supports:

- configuration loading;
- RSS/Atom collection;
- structured source-level outcomes;
- normalisation;
- validation;
- collection-window filtering;
- exact deduplication;
- deterministic classification;
- deterministic ranking;
- JSONL persistence;
- deterministic Markdown report generation;
- structured JSON run summaries;
- pipeline orchestration;
- one-command local execution;
- degraded partial-source behaviour;
- operational report metadata;
- lightweight run-level logging;
- automated unit and integration testing.

At the Phase 1 closeout, the repository has 104 passing tests.

The following production components are not yet implemented:

- production multi-source registry;
- hardened remote-network behaviour;
- GitHub Actions workflow;
- scheduled execution;
- automated repository commits;
- production source-health history;
- evidence-driven advanced quality logic.

---

# 3. High-Level Architecture

The implemented local data flow is:

```text
Configuration
→ Collection
→ Normalisation
→ Validation
→ Collection-window filtering
→ Exact deduplication
→ Classification
→ Ranking
→ Processed-record storage
→ Report selection and rendering
→ Run-summary generation
→ Output persistence
```

The orchestration layer coordinates these stages and exposes them through a thin command-line interface.

Conceptually:

```text
User / Scheduler
        |
        v
      CLI
        |
        v
   Pipeline Orchestrator
        |
        +--> Configuration
        |
        +--> Source Collection
        |
        +--> Normalisation
        |
        +--> Validation
        |
        +--> Window Filtering
        |
        +--> Deduplication
        |
        +--> Classification
        |
        +--> Ranking
        |
        +--> JSONL Storage
        |
        +--> Report Selection
        |
        +--> Run Summary
        |
        +--> Markdown Report
        |
        +--> Logging
```

The production automation layer will eventually invoke the same deterministic pipeline rather than introducing a separate processing path.

---

# 4. Repository Architecture

The current processing package is organised under:

```text
src/daily_intelligence/
```

Implemented modules are:

```text
__init__.py
cli.py
classify.py
collect.py
config.py
deduplicate.py
filter_window.py
models.py
normalize.py
pipeline.py
rank.py
report.py
run_summary.py
storage.py
validate.py
```

Configuration lives under:

```text
config/
```

Current configuration files include:

```text
sources.yaml
domains.yaml
settings.yaml
```

Tests live under:

```text
tests/
```

Controlled feed fixtures live under:

```text
tests/fixtures/
```

Generated production-style outputs are intended to use repository paths under:

```text
data/
reports/
```

The exact repository tree is always the source of truth if file names or directories later change.

---

# 5. Component Responsibilities

## 5.1 `models.py`

Owns the canonical structured article record used across pipeline stages.

The article model preserves both original and derived metadata so deterministic processing remains auditable.

Current important fields include:

- source identifier;
- original title;
- normalised title;
- original article URL;
- normalised URL;
- publication timestamp;
- retrieval timestamp;
- description;
- assigned domains;
- matched keywords;
- relevance score;
- score components;
- deterministic record identifier.

The article record is enriched as it moves through the pipeline rather than replaced by unrelated stage-specific formats.

---

## 5.2 `config.py`

Owns configuration loading and validation.

It reads the repository configuration and exposes typed configuration objects used by processing modules.

Current configuration types include:

- source configuration;
- domain configuration;
- ranking configuration;
- report configuration.

Configuration should remain separate from business logic so changing sources, keywords, score weights or report limits does not require modifying core processing code.

---

## 5.3 `collect.py`

Owns source collection.

The collector currently supports RSS/Atom-style structured feeds and returns source-level structured outcomes rather than allowing ordinary source failures to terminate the complete run.

Each collection result records:

- source identifier;
- status;
- entries;
- received-item count;
- error type;
- error message;
- retrieval timestamp.

Current statuses are:

- `success`;
- `empty`;
- `failed`.

Expected source-level failures are isolated.

A failed source should not discard valid results from successful sources.

Unexpected programming failures should not be silently converted into normal source failures.

---

## 5.4 `normalize.py`

Owns deterministic article normalisation.

Current responsibilities include:

- trimming and normalising titles;
- normalising URLs;
- removing selected tracking parameters;
- removing fragments;
- parsing publication timestamps;
- converting recognised timestamps to timezone-aware UTC values;
- creating deterministic record identifiers.

The original article URL is preserved separately from the normalised URL so the report can continue linking to the publisher-provided location.

### Record Identity

The implemented identifier is based deterministically on:

```text
source_id + normalized_url
```

using SHA-256.

There is currently no fallback identifier when a valid URL is unavailable.

That behaviour should not be broadened until real-source validation demonstrates a need.

---

## 5.5 `validate.py`

Owns structural record validation before later processing.

Validation currently checks important conditions such as:

- source identifier exists;
- title exists;
- article URL is valid HTTP or HTTPS;
- retrieval timestamp is timezone-aware.

Validation returns valid and invalid records separately.

Invalid input should be visible rather than silently disappearing.

Validation is intentionally distinct from collection-window eligibility.

A record may be structurally valid but later excluded because its publication timestamp falls outside the monitored window.

---

## 5.6 `filter_window.py`

Owns deterministic publication-window filtering.

This component was added after manual end-to-end validation showed that recording a collection window without enforcing it produced misleading daily output.

Current behaviour:

- accepts timezone-aware start and end datetimes;
- rejects naive boundaries;
- rejects a window whose end precedes its start;
- uses inclusive boundaries;
- retains records whose `published_at` falls within the window;
- excludes records published before the window;
- excludes records published after the window;
- excludes records whose `published_at` is missing.

Current CLI behaviour constructs a previous-24-hours window.

The missing-publication-time policy is conservative and provisional.

Alternative fallback behaviour should be considered only if real production feeds demonstrate a meaningful need.

---

## 5.7 `deduplicate.py`

Owns deterministic exact duplicate reduction.

Current duplicate checks are applied in this order:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

The component returns both:

- unique records;
- duplicate records.

Near-duplicate or semantic clustering is not part of the implemented core.

That functionality remains deferred until real reports demonstrate material repetition that exact deduplication cannot address.

---

## 5.8 `classify.py`

Owns deterministic domain classification.

Current logic combines:

- source-level default domains;
- configured domain keywords;
- title and description text.

Keyword matching is:

- case-insensitive;
- protected by word-boundary behaviour;
- deterministic.

A record may belong to multiple domains.

Classification does not require every record to receive a domain.

Unclassified records remain valid processed records but are omitted from the main Markdown report by default.

The current implemented taxonomy contains two active domains:

- Technology and Software;
- Artificial Intelligence.

This is a controlled Phase 1 taxonomy used to validate system behaviour, not the intended final coverage model.

---

## 5.9 `rank.py`

Owns deterministic relevance scoring.

The current Phase 1 score is provisional and intentionally simple.

Conceptually:

```text
relevance score
=
source-tier score
+ domain-match score
+ keyword-match score
```

Current configured source-tier values are:

- Tier 1 → 4 points;
- Tier 2 → 3 points;
- Tier 3 → 2 points;
- Tier 4 → 1 point.

Current additional weights are:

- 2 points per domain match;
- 1 point per matched keyword.

Score components are retained with each processed record for transparency.

The current formula is not treated as a final relevance model.

Ranking should change only when real-report review demonstrates systematic ordering problems.

---

## 5.10 `storage.py`

Owns processed-record persistence.

Processed records are written as JSON Lines.

The current write model overwrites the target file deterministically rather than continually appending to the same file.

This supports idempotent reruns for a given target path and prevents uncontrolled duplication.

Repository-native files remain the preferred storage mechanism unless production usage demonstrates a real database requirement.

---

## 5.11 `report.py`

Owns deterministic report selection and Markdown rendering.

It contains two distinct responsibilities:

### Selection

The public report selector determines which processed records appear.

Current selection behaviour:

- excludes unclassified records;
- requires an active primary domain;
- orders records deterministically;
- respects maximum items per domain;
- respects maximum items overall.

### Rendering

The Markdown renderer presents selected records in a readable daily report.

Current report behaviour includes:

- date heading;
- generation timestamp;
- run status;
- monitored time window;
- active source count;
- successful source count;
- empty source count;
- failed source count;
- collected-item count;
- displayed-item count;
- degraded-run warnings;
- domain sections;
- article title and publisher link;
- source name;
- publication timestamp;
- relevance score;
- secondary-domain metadata;
- short feed-provided description;
- configured description truncation.

Each story appears once under its primary domain.

Secondary domains are shown as metadata rather than duplicating the story across sections.

No generated summary text is produced.

---

## 5.12 `run_summary.py`

Owns structured operational metadata for one pipeline execution.

The run summary is the persistent operational record of what happened.

Current summary information includes:

- run identifier;
- start timestamp;
- completion timestamp;
- run status;
- collection window;
- active sources;
- successful sources;
- empty sources;
- failed sources;
- raw item count;
- valid item count;
- invalid item count;
- duplicate item count;
- displayed item count;
- warnings.

Run status distinguishes:

- successful execution;
- degraded execution;
- failed execution where applicable.

The same summary object is used to support both:

- persistent JSON operational output;
- user-facing Markdown operational metadata.

This prevents report status from being recomputed independently.

---

## 5.13 `pipeline.py`

Owns end-to-end local orchestration.

It coordinates the processing stages without absorbing their internal logic.

The current orchestration sequence is:

1. load active sources;
2. load domains;
3. load ranking settings;
4. load report settings;
5. collect all active sources;
6. normalise successful source entries;
7. validate records;
8. filter records by collection window;
9. deduplicate eligible records;
10. classify and score unique records;
11. determine report-selected records;
12. write processed JSONL;
13. build the run summary;
14. render the Markdown report using the run summary;
15. write the Markdown report;
16. write the JSON run summary;
17. emit completion logging;
18. return a structured pipeline result.

The orchestrator deliberately remains thin.

Business rules should continue to live in focused modules rather than accumulating inside `pipeline.py`.

---

## 5.14 `cli.py`

Owns the local command-line entry point.

The implemented command is:

```text
python -m daily_intelligence.cli run
```

The CLI is intentionally thin.

It currently:

- creates the run timestamp;
- creates the run identifier;
- constructs a previous-24-hours collection window;
- derives repository-default output paths;
- invokes the pipeline.

The CLI should not duplicate pipeline logic.

Future GitHub Actions automation should call the same underlying pipeline behaviour rather than creating a parallel implementation.

---

# 6. Configuration Architecture

Configuration is repository-native and human-readable.

The goal is to separate changing information policy from stable processing code.

## 6.1 `sources.yaml`

Current implemented source fields include:

- `id`;
- `name`;
- `feed_url`;
- `source_type`;
- `source_tier`;
- `default_domains`;
- `language`;
- `geographic_scope`;
- `active`.

The current Phase 1 source registry contains one controlled sample source.

Production source selection belongs to the next development phase.

Potential future source metadata should not be added until required.

---

## 6.2 `domains.yaml`

Current implemented domain fields include:

- `id`;
- `name`;
- `keywords`;
- `active`.

Current active Phase 1 domains are:

- Technology and Software;
- Artificial Intelligence.

The broader target taxonomy is defined in `03 Information Taxonomy and Source Policy.md`.

---

## 6.3 `settings.yaml`

Current settings include deterministic ranking and report configuration.

Ranking configuration currently defines:

- source-tier scores;
- domain-match score;
- keyword-match score.

Report configuration currently defines:

- maximum items per domain;
- maximum total items;
- maximum description length.

Current report limits are:

- maximum 5 items per domain;
- maximum 30 items overall;
- maximum description length 300 characters.

These are configurable defaults rather than permanent product truths.

---

# 7. Data Model and Record Lifecycle

A collected feed entry passes through several states.

Conceptually:

```text
Raw feed entry
→ normalised article record
→ validated article record
→ window-eligible article record
→ unique article record
→ classified article record
→ scored article record
→ stored processed record
→ optional displayed report item
```

These states are deliberately separate.

For example:

- a structurally valid article may be outside the collection window;
- an in-window article may be a duplicate;
- a unique article may remain unclassified;
- a processed article may not appear because of report limits.

This separation prevents misleading counters and allows each processing rule to remain testable.

---

# 8. Collection-Window Architecture

The collection window represents the publication-time interval eligible for the current report.

The implemented Phase 1 CLI uses:

```text
run timestamp - 24 hours
through
run timestamp
```

Both boundaries are inclusive.

The window must be timezone-aware.

Current eligibility is determined using `published_at`, not retrieval time.

A record can therefore be:

- collected now;
- structurally valid;
- excluded from today's report because it was published earlier.

This distinction is important.

The run summary currently records validation counts separately from report eligibility.

For example:

```text
raw items: 1
valid items: 1
displayed items: 0
```

is legitimate when the valid article falls outside the monitored publication window.

An explicit post-window eligibility count is not currently part of the run-summary schema.

That should be added only if operational use demonstrates that it materially improves observability.

---

# 9. Deduplication Architecture

Deduplication is intentionally conservative.

Current exact duplicate rules:

### Rule 1 — Normalised URL

Records with the same deterministic normalised URL are considered duplicates.

### Rule 2 — Normalised Title

Records that survive URL matching but share the same normalised title are considered duplicates.

This approach is:

- deterministic;
- inexpensive;
- explainable;
- easy to test.

It does not attempt to infer that differently worded articles describe the same event.

Potential future approaches such as title similarity, semantic clustering or story grouping remain deferred because they introduce false-merge risk and additional maintenance.

---

# 10. Classification Architecture

Classification is currently rules-based.

The design intentionally separates:

- source defaults;
- domain configuration;
- keyword matching.

Source defaults provide prior domain knowledge for a publisher.

Keyword matching allows individual articles to receive additional domains.

A record can therefore receive multiple domains.

Current primary-domain behaviour is deterministic:

- the first assigned eligible domain becomes the report section;
- later domains become secondary tags.

Potential future classification dimensions include:

- geography;
- content type;
- entities.

They are not implemented dependencies of the core pipeline.

---

# 11. Ranking Architecture

Ranking is a deterministic prioritisation layer, not an attempt to model objective news importance.

The score is currently used to order already-processed items before report limits are applied.

Current signals are intentionally simple:

- source tier;
- domain count;
- keyword count.

Future ranking changes may incorporate observed signals such as:

- source-quality penalties;
- domain-specific weights;
- geography;
- recency;
- entity importance;
- duplicate-cluster significance.

None should be added without evidence from real report evaluation.

The ranking system should remain explainable even if additional deterministic signals are introduced.

---

# 12. Report Architecture

The Markdown report is the primary user-facing artifact of the deterministic system.

The report is designed for rapid scanning rather than exhaustive archival reading.

Current objectives:

- concise;
- deterministic;
- source-transparent;
- bounded in length;
- visibly incomplete when degraded;
- easy to inspect in GitHub or locally.

The report does not rewrite or summarise full articles.

It exposes publisher-provided metadata and short descriptions.

The user can then choose which original sources deserve deeper reading or separate interpretation through ChatGPT.

---

# 13. Run Status and Failure Architecture

Failure handling distinguishes ordinary source degradation from critical system failures.

## Source-Level Failures

Expected source-level failures should be isolated.

Examples may include:

- unavailable feed;
- missing local fixture;
- malformed source response that the collector explicitly handles.

A source failure should produce:

- `failed` source status;
- error metadata;
- degraded run status where appropriate;
- visible warning in the Markdown report;
- visible warning in logs.

Successful sources should still contribute output.

## Empty Sources

A valid source with no entries should be represented as `empty`, not as a failure.

## Critical Failures

Failures that prevent trustworthy execution should not be silently downgraded.

Examples include:

- invalid core configuration;
- unexpected programming errors;
- invalid critical assumptions;
- failures that prevent valid output persistence.

Critical failure policy will need to be incorporated explicitly into GitHub Actions publication behaviour.

---

# 14. Observability Architecture

Observability uses three complementary surfaces.

## 14.1 Run Summary JSON

Purpose:

- persistent machine-readable operational record.

Contains:

- run status;
- source outcomes;
- counts;
- collection window;
- warnings;
- timestamps.

## 14.2 Markdown Operational Header

Purpose:

- user-facing indication of report completeness.

Shows:

- run status;
- monitored window;
- source health;
- item counts;
- warnings.

This prevents a degraded report from appearing indistinguishable from a complete one.

## 14.3 Standard-Library Logging

Purpose:

- technical execution diagnosis;
- local development visibility;
- future GitHub Actions log visibility.

Current pipeline logs include:

- pipeline start;
- source collection outcomes;
- validation counts;
- collection-window filtering counts;
- deduplication counts;
- classification/ranking counts;
- output paths;
- final status.

No custom logging framework is required.

---

# 15. Storage Architecture

The repository itself is the initial storage and delivery layer.

## Processed Records

Intended path pattern:

```text
data/processed/YYYY/MM/YYYY-MM-DD.jsonl
```

## Run Summaries

Intended path pattern:

```text
data/runs/YYYY/MM/YYYY-MM-DD.json
```

## Daily Reports

Intended path pattern:

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

The CLI currently derives paths using this structure.

Runtime output generated during controlled local testing should not automatically be treated as permanent repository data.

Automated production persistence will be defined when GitHub Actions is implemented.

---

# 16. Idempotency and Determinism

The system should produce predictable results from equivalent inputs and configuration.

Current deterministic properties include:

- deterministic URL normalisation;
- deterministic record identifier;
- deterministic validation;
- deterministic collection-window boundaries supplied by the run;
- deterministic exact deduplication;
- deterministic keyword classification;
- deterministic relevance score;
- deterministic report ordering;
- deterministic report limits;
- overwrite semantics for a target JSONL file.

A rerun targeting the same output path should not create uncontrolled duplicate content.

Network-fed production runs will naturally differ when the external source data changes.

---

# 17. Testing Architecture

Testing is part of the architecture rather than an optional development convenience.

At Phase 1 closeout, 104 tests pass.

Current coverage includes:

- configuration loading;
- source collection;
- controlled feed fixtures;
- normalisation;
- validation;
- collection-window filtering;
- exact deduplication;
- classification;
- ranking;
- storage;
- report selection;
- report rendering;
- run-summary generation;
- end-to-end pipeline orchestration;
- source-level degraded behaviour;
- CLI invocation;
- run-level logging.

Important integration scenarios include:

### Happy Path

One controlled source produces one valid in-window record that is processed and displayed.

### Degraded Source

One source succeeds and one source fails.

Expected behaviour:

- successful records survive;
- run status becomes degraded;
- report contains successful information;
- report displays a warning;
- run summary exposes failure counts.

### Out-of-Window Record

A structurally valid article is collected but published outside the monitored interval.

Expected behaviour:

- raw count reflects collection;
- validation count reflects structural validity;
- record is excluded before deduplication/classification/reporting;
- displayed count is zero if no other eligible items exist.

### Logging

Important run-stage messages are exposed through the pipeline logger.

---

# 18. Production Automation Architecture

GitHub Actions is the intended production execution environment, but it is not yet implemented.

The future workflow should remain a wrapper around the same Python pipeline.

Planned responsibilities include:

- checkout repository;
- configure Python;
- install project;
- validate configuration;
- run tests or required pre-run validation;
- execute pipeline;
- inspect output validity;
- commit changed production artifacts;
- avoid empty commits;
- expose failures through workflow logs;
- run manually through `workflow_dispatch`;
- later run on a schedule.

The workflow should use:

- minimum required permissions;
- explicit timeout;
- no AI service;
- no paid external service;
- no secret unless a real source eventually requires one.

Scheduled execution should not be enabled until a manual production-like run and a manual GitHub Actions run are successful.

---

# 19. Network Architecture

Real remote-source hardening is intentionally incomplete.

Phase 1 focused on deterministic local behaviour.

Before automated production collection, the collector should be validated against a small real-source set.

Production-readiness review should determine the minimum required behaviour for:

- request timeout;
- user agent;
- retry count;
- retryable errors;
- malformed responses;
- redirect handling;
- feed parser behaviour;
- rate limits.

The default design principle is conservative:

- requests must not hang indefinitely;
- retries should be bounded;
- source failures should remain isolated;
- a poor source should be removed rather than supported through disproportionate complexity.

No production network feature should be added without a real-source reason.

---

# 20. Security and Privacy Architecture

The repository is public.

Therefore the architecture must never require committing:

- credentials;
- private Career OS data;
- private email content;
- private newsletter content;
- access tokens;
- personally sensitive datasets;
- restricted copyrighted content.

If credentials become necessary for an optional future source, they must use environment variables or GitHub Secrets and must not become a core-system dependency.

The preferred source universe remains public structured information that does not require authentication.

---

# 21. Copyright and Content Boundaries

The system should preserve metadata required for intelligence triage without reproducing restricted source content.

The repository may store:

- titles;
- publisher names;
- article links;
- timestamps;
- short feed-provided descriptions where appropriate;
- derived deterministic metadata;
- scores;
- classifications.

The system should not store:

- complete copyrighted articles;
- bypassed paywall content;
- unauthorised scraped full text.

The report is intended to direct the user toward original sources rather than replace them.

---

# 22. Architecture for ChatGPT Use

ChatGPT is outside the automated production dependency chain.

The deterministic system should be useful without any ChatGPT API call.

ChatGPT may be used manually for:

- interpreting selected stories;
- connecting information to career or project context;
- analysing trends;
- deciding whether a system limitation is worth addressing;
- development reasoning;
- code generation and review.

The architectural separation is:

```text
Daily Intelligence System
= deterministic collection and filtering infrastructure

ChatGPT
= optional external reasoning and interpretation layer
```

This separation preserves:

- zero recurring system cost;
- auditability;
- portability;
- reliability;
- freedom from API-credit dependence.

---

# 23. Implemented vs Planned vs Deferred Architecture

## Implemented and Validated

- Python package;
- repository configuration;
- RSS/Atom collection;
- structured source results;
- normalisation;
- deterministic URL cleaning;
- UTC timestamp parsing;
- deterministic SHA-256 record IDs;
- validation;
- collection-window filtering;
- exact deduplication;
- deterministic domain classification;
- deterministic ranking;
- JSONL persistence;
- deterministic report selection;
- Markdown rendering;
- operational report metadata;
- structured run-summary JSON;
- end-to-end pipeline orchestration;
- local CLI;
- source-level degraded behaviour;
- lightweight logging;
- automated tests.

## Planned for Production MVP

- small real-source registry;
- validated HTTP timeout behaviour;
- bounded retry policy if needed;
- production user-agent behaviour if needed;
- GitHub Actions workflow;
- `workflow_dispatch`;
- automated output persistence;
- automated commits;
- scheduled execution;
- real-use evaluation.

## Deferred Until Evidence

- near-duplicate clustering;
- story clustering;
- entity extraction;
- geographic classification;
- content-type classification;
- source-health history;
- advanced source penalties;
- sophisticated ranking;
- broad taxonomy expansion logic;
- dashboards;
- GitHub Pages;
- GitHub Issues delivery;
- machine learning;
- LLM processing;
- embeddings;
- RAG;
- agents;
- databases;
- cloud infrastructure.

---

# 24. Current Architectural Limitations

The current system should not be described as production-complete.

Known limitations include:

- only one controlled sample source is configured;
- only two domains are implemented;
- remote-source behaviour has not yet been validated broadly;
- explicit network timeout/retry policy is not yet production-hardened;
- exact deduplication cannot detect differently worded versions of the same story;
- records with missing publication timestamps are excluded from report-window eligibility;
- ranking is provisional;
- no entity or geographic enrichment exists;
- no production source-health history exists;
- GitHub Actions is not implemented;
- automated commits are not implemented;
- scheduled execution is not implemented;
- real daily report quality has not yet been evaluated over time.

These are visible limitations, not automatic development requirements.

Each should be addressed only when required by the next validated workflow step.

---

# 25. Architectural Decision Rules

Any proposed architectural change should answer:

1. What observed problem does this solve?
2. Is that problem currently validated?
3. Can configuration or a deterministic rule solve it instead?
4. What recurring cost does it add?
5. What maintenance does it add?
6. What new failure modes does it create?
7. How will success be tested?
8. Does it preserve public-repository safety?
9. Does it preserve negligible daily manual work?
10. Does it delay actual use of the system?

The default answer to unnecessary infrastructure should be no.

---

# 26. Open Architectural Decisions

The following decisions remain intentionally open.

## Real-Source Set

Determine the smallest credible source set for production-like validation.

Owner: Phase 2.

## Network Timeout

Determine a bounded timeout appropriate for live RSS/Atom requests.

Owner: Phase 2.

## Retry Policy

Determine whether any retry behaviour is necessary after observing live source failures.

Owner: Phase 2.

## Missing Publication Timestamp Policy

Current behaviour excludes missing publication timestamps.

Reconsider only if valuable real sources frequently omit the field.

Owner: evidence from Phase 2 or Phase 4.

## Collection Window

Current CLI default is the previous 24 hours.

Reconsider tolerance only if source publication behaviour causes systematic misses.

Owner: evidence from live feeds.

## Near-Duplicate Detection

No implementation until exact deduplication proves insufficient.

Owner: Phase 5 if justified.

## Production Source Health History

Current run summaries capture per-run operational state but not long-term source health.

Add only if recurring source reliability becomes difficult to manage manually.

## Automated Commit Strategy

Final GitHub Actions commit behaviour must ensure:

- outputs are validated first;
- no empty commits;
- one coherent commit per successful publication event;
- critical failures do not publish misleading output.

Owner: Phase 3.

## Output Retention

Repository-native daily history is currently intended.

Retention or archival policy should be revisited only after real production growth is measurable.

---

# 27. Architecture Validation Gates

## Gate A — Local Architecture

Status: passed.

Required:

- local orchestration works;
- deterministic processing works;
- test coverage exists;
- output is inspectable;
- failures are visible.

## Gate B — Real-Source Architecture

Status: not yet passed.

Required:

- small live source set works reliably enough;
- requests cannot hang indefinitely;
- source metadata is usable;
- report output is useful;
- no critical external-source behaviour is unresolved.

## Gate C — Automation Architecture

Status: not yet passed.

Required:

- real-source architecture has passed;
- manual GitHub Actions run works;
- outputs are validated before persistence;
- permissions are minimal;
- failure states are visible;
- no paid or AI dependency is introduced.

## Gate D — Advanced Quality Architecture

Status: not yet passed.

Required:

- real reports demonstrate a material limitation;
- simpler deterministic adjustments are insufficient;
- the new component has an explicit evaluation method.

---

# 28. Current Architecture Summary

The Daily Intelligence System is currently a repository-native deterministic Python pipeline.

Its implemented core is:

```text
collect
→ normalize
→ validate
→ filter by publication window
→ deduplicate
→ classify
→ rank
→ store
→ generate readable report
→ generate run summary
→ expose operational status
```

It runs locally through:

```text
python -m daily_intelligence.cli run
```

It has no recurring monetary cost and no production AI dependency.

At Phase 1 closeout:

- the complete local vertical slice is implemented;
- 104 tests pass;
- manual CLI execution is validated;
- collection-window enforcement is validated;
- degraded source handling is validated;
- report operational visibility is validated;
- run-level logging is validated.

The next architectural objective is not additional sophistication.

It is to validate this same architecture with a deliberately small set of real public feeds before introducing GitHub Actions automation.

---

# Changelog

## 2026-08-11 — Phase 1 Architecture Baseline

- Replaced the pre-implementation architecture with the validated local system architecture.
- Added explicit orchestration and CLI components.
- Added collection-window filtering as a first-class processing stage.
- Recorded deterministic SHA-256 record identity.
- Recorded exact URL/title deduplication.
- Recorded current deterministic classification and ranking behaviour.
- Recorded report selection and operational metadata behaviour.
- Recorded run-summary and logging responsibilities.
- Distinguished implemented, production-planned and deferred components.
- Removed speculative modules that are not part of the current repository.
- Reframed near-duplicate, entity, geography and content-type logic as evidence-driven future enhancements.
- Defined real-source validation as the next architecture gate before GitHub Actions.