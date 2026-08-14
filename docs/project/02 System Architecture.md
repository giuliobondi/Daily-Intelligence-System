# Daily Intelligence System — System Architecture

> **Purpose**
>
> This document defines the technical architecture of the Daily Intelligence System.
>
> It describes the implemented processing model, component boundaries, data flow, storage model, configuration model, failure behaviour, observability, automation architecture and the architectural constraints that govern future development.
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
- repository-native storage;
- standard-library capabilities where practical;
- small modules with clear responsibilities;
- visible failure states;
- tests for important deterministic behaviour;
- replacement of weak sources before disproportionate source-specific complexity.

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
- authenticated premium-news scraping;
- private newsletter ingestion;
- complex frontend applications;
- machine-learning components without a validated need.

---

# 2. Architectural Status

The core system is now implemented as a repository-native deterministic production pipeline.

The current architecture supports:

- repository-native configuration loading;
- seven active real public RSS sources;
- RSS/Atom collection;
- bounded remote HTTP retrieval;
- explicit User-Agent and Accept headers;
- normal SSL verification;
- redirect-compatible remote retrieval;
- structured source-level outcomes;
- source-level failure isolation;
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
- automated unit and integration testing;
- GitHub Actions manual execution;
- GitHub Actions scheduled execution;
- automated output validation;
- automated repository persistence;
- automated bot commits;
- no-change commit protection;
- critical-failure publication protection;
- concurrency protection.

The current automated test suite contains:

> **110 passing tests.**

Phase 3 automation architecture has been validated.

The current architectural priority is no longer basic automation.

It is:

> **improve the information layer through source/domain correction and expansion, then design richer report context without weakening the zero-cost, deterministic and public-safe architecture.**

---

# 3. High-Level Architecture

The implemented data flow is:

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

Production automation wraps the same pipeline.

Conceptually:

```text
Manual trigger / Scheduled trigger
             |
             v
      GitHub Actions
             |
             v
      Install + Test
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
             |
             v
      Output Validation
             |
             v
    Repository Persistence
```

There is no separate production processing implementation.

Local execution and GitHub Actions invoke the same application pipeline.

---

# 4. Repository Architecture

The processing package is organised under:

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

Production automation lives under:

```text
.github/workflows/
```

Current production workflow:

```text
.github/workflows/daily-intelligence.yml
```

Tests live under:

```text
tests/
```

Controlled feed fixtures live under:

```text
tests/fixtures/
```

Generated production outputs live under:

```text
data/
reports/
```

Canonical project documents live under:

```text
docs/project/
```

The exact repository tree remains the source of truth if file names or directories later change.

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

Future richer-report fields should extend this model only when an explicit processing need exists.

Do not add fields merely to mirror every property exposed by every feed.

---

## 5.2 `config.py`

Owns configuration loading and validation.

It reads repository configuration and exposes typed configuration objects used by processing modules.

Current configuration types include:

- source configuration;
- domain configuration;
- ranking configuration;
- report configuration.

Configuration remains separate from business logic so changing sources, keywords, score weights or report limits does not require modifying core processing code.

### Source Validation Behaviour

Source configuration currently requires:

- non-empty source identifier;
- non-empty source name;
- non-empty feed location;
- supported source type;
- valid source tier;
- `default_domains` list;
- non-empty language;
- non-empty geographic scope;
- boolean activation state.

`default_domains` may be an explicitly empty list:

```yaml
default_domains: []
```

This supports broad heterogeneous sources whose articles should rely on content-based classification rather than forced publisher-wide topics.

`geographic_scope` remains required and non-empty.

### Configuration Boundary

Information-policy properties should not automatically become runtime configuration.

For example, source-review concepts such as:

- reader accessibility;
- Bocconi access mode;
- metadata richness;
- review status;

may remain documentation-level properties unless processing logic actually needs them.

This prevents descriptive source research from unnecessarily increasing runtime configuration complexity.

---

## 5.3 `collect.py`

Owns source collection.

The collector supports:

- controlled local feed files;
- remote HTTP/HTTPS RSS feeds;
- remote HTTP/HTTPS Atom feeds.

It returns source-level structured outcomes rather than allowing expected source failures to terminate the complete run.

Each collection result records:

- source identifier;
- status;
- entries;
- received-item count;
- error type;
- error message;
- retrieval timestamp.

Current statuses are:

```text
success
empty
failed
```

Expected source-level failures are isolated.

A failed source does not discard valid results from successful sources.

Unexpected programming failures should not be silently converted into normal source failures.

### Local Collection

Local feed paths are validated before being passed to `feedparser`.

A missing local file raises `CollectionError`.

### Remote Collection

Current remote collection flow is:

```text
configured HTTP/HTTPS feed
→ urllib Request
→ explicit User-Agent
→ explicit Accept header
→ 10-second timeout
→ normal TLS verification
→ normal redirect handling
→ response bytes
→ feedparser
```

The collector uses standard-library networking rather than a third-party HTTP client.

Expected remote failures converted into `CollectionError` include:

- HTTP errors;
- URL/network errors;
- request timeout.

Normal SSL certificate verification remains enabled.

No SSL-verification bypass exists.

### Parser Behaviour

After content is loaded, `feedparser` parses the feed.

A parser result marked malformed through `bozo` is currently rejected with `CollectionError`.

Production evidence has not justified weakening this policy.

### Retry Policy

No retry logic is currently implemented.

This remains intentional.

The preferred response to an unreliable low-value source is:

```text
review source
→ replace or remove when appropriate
```

before:

```text
add increasingly complex retry/resilience behaviour
```

Retries should be added only if repeated production evidence demonstrates that bounded retry materially improves a valuable source.

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

That behaviour should not be broadened without evidence.

### Publication Timestamps

The normaliser uses feed-provided publication timestamps.

The current source set has supplied usable publication timestamps during production validation.

No publication-time inference layer exists.

### Optional Descriptions

Descriptions remain optional for structural validity.

The system does not generate a synthetic description during normalisation.

Production use has now shown that missing or thin descriptions can create a product-quality limitation.

That issue belongs to the upcoming richer-report design rather than being silently solved inside normalisation.

---

## 5.5 `validate.py`

Owns structural record validation before later processing.

Validation checks important conditions such as:

- source identifier exists;
- title exists;
- article URL is valid HTTP or HTTPS;
- retrieval timestamp is timezone-aware.

Validation returns valid and invalid records separately.

Invalid input remains visible rather than disappearing silently.

Validation is intentionally distinct from collection-window eligibility.

A record may be:

```text
structurally valid
but
not eligible for the current reporting window
```

---

## 5.6 `filter_window.py`

Owns deterministic publication-window filtering.

Current behaviour:

- accepts timezone-aware start and end datetimes;
- rejects naive boundaries;
- rejects a window whose end precedes its start;
- uses inclusive boundaries;
- retains records whose `published_at` falls within the window;
- excludes records published before the window;
- excludes records published after the window;
- excludes records whose `published_at` is missing.

The current CLI constructs a previous-24-hours window relative to actual execution time.

This architecture is now under evidence-based review because GitHub scheduler latency can shift the effective report window.

No change has yet been implemented.

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

Near-duplicate or semantic clustering remains deferred.

Potential approaches such as:

- title similarity;
- event clustering;
- semantic embeddings;
- LLM comparison;

are not part of the current architecture.

False merging remains a greater concern than modest repeated coverage.

---

## 5.8 `classify.py`

Owns deterministic domain classification.

Current logic combines:

- source-level default domains;
- configured domain keywords;
- title and description text.

Keyword matching is:

- case-insensitive;
- word-boundary protected;
- deterministic.

A record may belong to multiple domains.

A record may also remain unclassified.

Unclassified records remain valid processed records but are omitted from the main Markdown report.

### Current Implemented Taxonomy

The current implemented taxonomy contains seven active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

The broader target taxonomy is defined in:

```text
03 Information Taxonomy and Source Policy.md
```

### Source Defaults

Source defaults are interpreted as prior topical evidence.

They should be used only where the selected feed is narrow enough that essentially every item legitimately belongs to that topic.

Current source-default policy:

```text
BBC News World                → none
BBC News Business             → none
European Central Bank         → none
European Commission           → none
Istat Press Releases          → Economics and Macroeconomics
OpenAI News                   → Artificial Intelligence
Sifted                        → Startups and Venture Capital
```

### Conservative Classification Principle

The architecture follows:

> prefer no source default over a weak publisher-level assumption.

And:

> prefer an unclassified record over a misleading classification.

### Evidence-Based Keyword Refinement

Current evidence-based Global Politics additions include:

- `war`;
- `conflict`;
- `parliament`.

Broader candidates such as:

- `government`;
- `defence`;
- `president`;
- `prime minister`;

were tested but rejected because of ambiguous or low-value matches.

---

## 5.9 `rank.py`

Owns deterministic relevance scoring.

The current score is intentionally simple.

Conceptually:

```text
relevance score
=
source-tier score
+ domain-match score
+ keyword-match score
```

Current configured source-tier values are:

```text
Tier 1 → 4
Tier 2 → 3
Tier 3 → 2
Tier 4 → 1
```

Current additional weights are:

```text
2 points per assigned domain
1 point per matched keyword
```

Score components are retained for transparency.

The formula remains provisional.

### Architectural Rule

If weak upstream evidence inflates scores:

> correct the source/default/classification evidence before redesigning ranking.

Production experience has already demonstrated this principle.

---

## 5.10 `storage.py`

Owns processed-record persistence.

Processed records are written as JSON Lines.

The current write model overwrites the target file deterministically rather than continually appending.

This supports:

- predictable same-path reruns;
- bounded duplicate behaviour;
- simple repository inspection.

Repository-native files remain the storage architecture.

No database is justified.

---

## 5.11 `report.py`

Owns deterministic report selection and Markdown rendering.

It contains two distinct responsibilities.

### Selection

The report selector determines which processed records appear.

Current selection behaviour:

- excludes unclassified records;
- requires an active primary domain;
- orders records deterministically;
- respects maximum items per domain;
- respects maximum items overall.

### Primary-Domain Placement

The first eligible assigned domain becomes the story's primary report section.

Later assigned domains appear as secondary metadata.

### Rendering

The current Markdown renderer includes:

- report date;
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
- article title and source link;
- source name;
- publication timestamp;
- relevance score;
- secondary-domain metadata;
- short feed-provided description.

Each story appears once.

### Current Limitation

The report currently acts partly as an intelligence index.

It may provide too little information to understand a development without opening the source.

Production use has validated a new requirement:

> the report should provide enough lawful context for initial understanding, while preserving the original source for deeper reading.

The architectural method for satisfying that requirement is not yet selected.

Do not implement a summarisation layer before the richer-report design phase determines:

- required context depth;
- permitted source material;
- metadata availability;
- fallback behaviour;
- report-length constraints;
- validation method.

### Architecture Preference for Richer Context

Evaluate candidate mechanisms in this order:

```text
existing richer RSS/Atom fields
→ public structured metadata
→ official free APIs
→ narrowly justified permitted public-page extraction
→ more complex approaches only if necessary
```

Do not assume:

- full article ingestion;
- LLM summarisation;
- authenticated premium-content retrieval;

are required.

---

## 5.12 `run_summary.py`

Owns structured operational metadata for one pipeline execution.

The run summary is the persistent machine-readable record of what happened.

Current information includes:

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

The same summary supports:

- JSON operational history;
- Markdown operational metadata.

Run status distinguishes:

```text
success
degraded
failed
```

where applicable.

---

## 5.13 `pipeline.py`

Owns end-to-end orchestration.

It coordinates processing stages without absorbing their internal logic.

Current orchestration sequence:

1. load active sources;
2. load domains;
3. load ranking settings;
4. load report settings;
5. collect active sources;
6. normalise successful source entries;
7. validate records;
8. filter records by publication window;
9. deduplicate eligible records;
10. classify and score unique records;
11. determine report-selected records;
12. write processed JSONL;
13. build run summary;
14. render Markdown report;
15. write Markdown report;
16. write JSON run summary;
17. emit completion logging;
18. return structured pipeline result.

The orchestrator remains intentionally thin.

### Normalisation-Failure Boundary

The pipeline currently normalises entries from successful sources directly.

Broad per-entry `NormalizationError` isolation has not been introduced because production evidence has not justified it.

If a future feed contains one malformed entry that terminates an otherwise usable source run:

```text
reproduce
→ regression test
→ make smallest justified boundary change
```

---

## 5.14 `cli.py`

Owns the command-line entry point.

Current command:

```text
python -m daily_intelligence.cli run
```

The CLI:

- configures standard-library logging;
- creates the run timestamp;
- creates the run identifier;
- constructs the current previous-24-hours collection window;
- derives repository output paths;
- invokes the pipeline.

The CLI should remain thin.

GitHub Actions invokes the same CLI rather than implementing a parallel processing path.

### Local Installation Note

Because the package uses a `src/` layout, local source-based pytest execution can reflect newer repository code while:

```text
python -m daily_intelligence.cli
```

may execute a stale installed package.

When CLI behaviour does not match validated source changes, refresh the local package installation before diagnosing a new application bug.

This is a development-environment concern, not a production architecture dependency.

---

# 6. Configuration Architecture

Configuration is repository-native and human-readable.

The goal is to separate changing information policy from stable processing code.

---

## 6.1 `sources.yaml`

Current source fields include:

- `id`;
- `name`;
- `feed_url`;
- `source_type`;
- `source_tier`;
- `default_domains`;
- `language`;
- `geographic_scope`;
- `active`.

The current registry contains seven public RSS feeds:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News;
- Istat Press Releases;
- OpenAI News;
- Sifted.

The source universe is now under active review.

The file remains the runtime source of truth for active production feeds.

### Access Metadata

Reader-accessibility properties should not automatically be added to `sources.yaml`.

Examples:

```text
public web
Bocconi direct
SearchLib
database
extra paid subscription
```

These are currently policy/review dimensions.

They should become runtime configuration only if application behaviour genuinely needs them.

---

## 6.2 `domains.yaml`

Current fields include:

- `id`;
- `name`;
- `keywords`;
- `active`.

Current active domains are:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

Candidate expansion domains:

- Financial Markets;
- Italy;
- Milan and Bocconi ecosystem.

Domain expansion should follow source/domain strategy and technical validation.

---

## 6.3 `settings.yaml`

Current settings define:

- ranking weights;
- report limits.

Current ranking configuration includes:

- source-tier scores;
- domain-match score;
- keyword-match score.

Current report configuration includes:

- maximum items per domain;
- maximum total items;
- maximum description length.

Current values:

```text
maximum 5 items per domain
maximum 30 items overall
maximum description length 300 characters
```

These are configurable defaults, not permanent product truths.

The richer-report design may justify changes to report settings.

---

# 7. Data Model and Record Lifecycle

A feed entry passes through distinct processing states:

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

These states remain deliberately separate.

Examples:

- a structurally valid article may be outside the reporting window;
- an in-window article may be a duplicate;
- a unique article may remain unclassified;
- a classified article may not be displayed because of report limits.

This separation improves:

- testability;
- counter interpretation;
- failure isolation;
- future extension.

---

# 8. Collection-Window Architecture

The collection window represents the publication-time interval eligible for a report.

Current CLI behaviour:

```text
actual run timestamp - 24 hours
through
actual run timestamp
```

Both boundaries are inclusive.

The window must be timezone-aware.

Eligibility uses:

```text
published_at
```

not retrieval time.

A record can therefore be:

```text
collected
valid
but outside the report window
```

## Observed Production Limitation

Scheduled GitHub Actions execution has demonstrated substantial trigger latency.

A scheduled workflow may start materially later than the configured cron time.

Because the reporting window is currently based on actual start time:

```text
configured trigger
→ delayed GitHub start
→ later report cutoff
→ shifted 24-hour window
→ potentially different eligible stories
```

This coupling means infrastructure timing can affect information composition.

## Current Decision

Do not change the window yet.

The issue is now an explicit architecture question.

Potential future design:

```text
fixed reporting cutoff
→ deterministic 24-hour information window
→ GitHub delay affects delivery time only
```

This should be implemented only if repeated production evidence confirms that the current coupling materially harms report consistency.

---

# 9. Deduplication Architecture

Deduplication remains conservative.

Current exact duplicate rules:

## Rule 1 — Normalised URL

Same normalised URL means duplicate.

## Rule 2 — Normalised Title

Records surviving URL comparison but sharing the same normalised title are duplicates.

The first deterministic occurrence is retained.

This approach is:

- deterministic;
- inexpensive;
- explainable;
- easy to test.

It does not infer that differently worded articles describe the same event.

Near-duplicate logic remains deferred.

---

# 10. Classification Architecture

Classification is rules-based.

It separates:

- source defaults;
- domain configuration;
- keyword evidence.

A record may:

- receive one domain;
- receive multiple domains;
- remain unclassified.

Primary report placement is deterministic.

Potential future dimensions include:

- article-level geography;
- content type;
- entities.

They are not part of the core pipeline.

The active source/domain expansion phase may justify additional domains.

It does not automatically justify more sophisticated classification machinery.

---

# 11. Ranking Architecture

Ranking is deterministic prioritisation.

It is not an attempt to calculate objective global importance.

Current signals:

- source tier;
- domain count;
- keyword count.

Future signals might include:

- domain priority;
- recency;
- entities;
- geography;
- independent multi-source coverage.

Source accessibility and metadata richness should primarily be handled through source eligibility and report design before being introduced as ranking penalties.

Avoid downstream scoring complexity when upstream source selection can solve the problem more cleanly.

---

# 12. Report Architecture

The Markdown report is the primary user-facing production artifact.

Current objectives:

- concise;
- deterministic;
- source-transparent;
- bounded;
- operationally transparent;
- easy to inspect on GitHub;
- easy to read on desktop or mobile.

## Current User Experience

The current report provides:

```text
headline
source
publication time
relevance score
secondary domains
feed description when available
source link
```

This is sufficient for triage.

It is not consistently sufficient for understanding.

## Target User Experience

The future architecture should support:

```text
report
→ understand core development
→ decide whether deeper reading is useful
→ open selected source
```

rather than:

```text
report
→ identify headline
→ click article
→ only then understand development
```

## Architectural Constraint

The report must not become a public mirror of copyrighted articles.

Any richer context must remain compatible with:

- source permissions;
- public-repository storage;
- copyright boundaries;
- zero recurring cost;
- no authenticated scraping.

## Sparse and Concentrated Reports

Production has also demonstrated that a technically healthy run may produce a short and concentrated report.

This is an information-quality issue, not automatically an architectural failure.

Do not add:

- minimum quotas;
- artificial publisher balancing;
- automatic filler;

without repeated evidence.

Source expansion should be evaluated before adding complex report-balancing logic.

---

# 13. Run Status and Failure Architecture

Failure handling distinguishes:

- source degradation;
- critical system failure.

---

## Source-Level Failure

Expected collection failures are isolated.

Examples:

- unavailable feed;
- HTTP failure;
- DNS failure;
- timeout;
- malformed feed.

A failed source produces:

- `failed` source status;
- error metadata;
- degraded run status where appropriate;
- report warning;
- log warning.

Successful sources continue.

### Validated Automated Behaviour

A deliberate GitHub Actions degraded-source test changed BBC World to an invalid hostname.

Observed behaviour:

```text
7 active sources
6 successful
1 failed
status = degraded
```

The report remained usable.

The workflow persisted degraded output.

This is the production policy.

---

## Empty Sources

A valid source returning no entries is represented as:

```text
empty
```

not as failed.

---

## Critical Failures

Critical failures should stop trustworthy publication.

Examples:

- invalid source configuration;
- invalid core configuration;
- unexpected programming error;
- failure preventing valid output creation.

A deliberate invalid `geographic_scope: []` configuration was tested through GitHub Actions.

Observed behaviour:

- tests/configuration validation failed;
- production publication did not proceed successfully;
- no misleading successful output was published.

This establishes the critical-failure boundary.

---

# 14. Observability Architecture

Observability uses four complementary surfaces.

---

## 14.1 Run Summary JSON

Persistent machine-readable operational record.

Contains:

- status;
- source counts;
- item counts;
- collection window;
- warnings;
- timestamps.

---

## 14.2 Markdown Operational Header

User-facing indication of report completeness.

Shows:

- run status;
- monitored period;
- source health;
- item counts;
- warnings.

---

## 14.3 Standard-Library Logging

Technical execution diagnosis.

Logs include:

- pipeline start;
- each source outcome;
- validation count;
- window-filter count;
- duplicate count;
- classification/ranking count;
- output paths;
- final status.

CLI logging is explicitly configured so these messages appear in GitHub Actions.

---

## 14.4 GitHub Actions Job Status

Repository-level automation visibility.

Exposes:

- workflow success/failure;
- failed step;
- test failures;
- pipeline logs;
- persistence failures.

No external monitoring service is currently justified.

---

# 15. Storage Architecture

The repository itself is the production storage and delivery layer.

---

## Processed Records

```text
data/processed/YYYY/MM/YYYY-MM-DD.jsonl
```

---

## Run Summaries

```text
data/runs/YYYY/MM/YYYY-MM-DD.json
```

---

## Daily Reports

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

---

## Production Persistence

GitHub Actions automatically persists changed outputs.

Current persistence flow:

```text
pipeline
→ generate outputs
→ validate expected outputs
→ git add production output directories
→ inspect staged changes
→ no change: exit without commit
→ changes exist: commit as github-actions[bot]
→ push
```

The bot identity is used only for automated production persistence.

Generated production history remains visible in ordinary Git history.

---

## Output Validation

Before persistence, the workflow validates the expected dated output files.

The current architecture assumes all three core outputs exist:

- processed JSONL;
- run-summary JSON;
- Markdown report.

A future no-news production case should be reviewed if empty JSONL is demonstrated to be valid but current file-size validation rejects it.

Do not redesign this path without reproducing the actual case.

---

## Retention

No retention or archive-cleanup mechanism exists.

Repository-native daily history remains intentionally simple.

Revisit retention only after repository growth becomes a demonstrated problem.

---

# 16. Idempotency and Determinism

The system should produce predictable results from equivalent inputs and configuration.

Deterministic properties include:

- URL normalisation;
- record identity;
- validation;
- filtering for supplied boundaries;
- exact deduplication;
- keyword classification;
- relevance scoring;
- report ordering;
- report limits;
- target-file overwrite semantics.

Network-fed production runs naturally differ because:

- feed contents change;
- retrieval time changes;
- run timestamp changes.

## Automated Commit Determinism

The workflow does not create empty commits.

This branch has been explicitly validated.

A same-day rerun may still create a legitimate changed commit because timestamps or feed content changed.

That is not considered an empty-commit defect.

---

# 17. Testing Architecture

Testing is part of the architecture.

Current suite:

> **110 tests pass.**

Coverage includes:

- configuration loading;
- source validation;
- empty `default_domains`;
- non-empty geographic scope;
- source collection;
- feed fixtures;
- remote request timeout;
- User-Agent behaviour;
- HTTP failure handling;
- network failure handling;
- normalisation;
- validation;
- publication-window filtering;
- exact deduplication;
- classification;
- ranking;
- storage;
- report selection;
- report rendering;
- run-summary generation;
- end-to-end pipeline orchestration;
- degraded behaviour;
- CLI invocation;
- logging configuration.

## Test Isolation

Deterministic automated tests do not depend on live internet access.

Fixtures and temporary configuration remain the default for automated tests.

Real-source behaviour is validated separately through production-like or actual production runs.

## Production-Level Tests Completed

The following have been explicitly tested through GitHub Actions:

```text
normal successful production run
degraded source run
critical configuration failure
changed-output commit
no-change commit guard
scheduled execution
```

---

# 18. Production Automation Architecture

GitHub Actions is the production execution environment.

The workflow remains a thin wrapper around the Python application.

Current high-level workflow:

```text
workflow_dispatch / schedule
→ checkout
→ Python 3.12
→ install project + development dependencies
→ run 110 tests
→ run production CLI
→ validate outputs
→ stage output directories
→ no-change guard
→ bot commit
→ push
```

## Manual Trigger

Supported through:

```text
workflow_dispatch
```

This is used for:

- testing;
- recovery;
- controlled production reruns.

## Scheduled Trigger

The production schedule is:

```text
06:05 Europe/Rome
```

The schedule was moved earlier after observing significant GitHub scheduler delays.

The schedule should be understood as:

> desired trigger time

not:

> guaranteed exact execution time.

## Runtime

Current runner:

```text
ubuntu-latest
```

Current configured Python:

```text
3.12
```

## Package Installation

The workflow installs the project with development dependencies so the same job can:

- run tests;
- run production.

## Timeout

An explicit workflow job timeout is configured.

The current timeout remains comfortably above normal runtime while preventing an indefinitely stuck job.

## Permissions

The workflow requires:

```text
contents: write
```

because it commits generated outputs to the repository.

No broader repository permissions are required for current production behaviour.

## Secrets

No source credentials or repository secrets are required for the current production source universe.

## Production AI

The workflow makes no:

- OpenAI API call;
- Copilot call;
- GitHub AI call;
- third-party paid AI call.

---

# 19. Concurrency Architecture

Concurrency became necessary once both:

- manual dispatch;
- scheduled execution;

could start production runs.

Without protection, overlapping runs could:

- write the same date-based paths;
- create conflicting commits;
- race during push.

The workflow therefore uses a single production concurrency group.

Current policy:

```text
one Daily Intelligence production run at a time
```

with:

```text
cancel-in-progress: false
```

A currently running production job should finish rather than being aborted by a newer trigger.

This is preferable for a small daily pipeline where preserving a valid run is more important than immediately replacing it.

---

# 20. Scheduler Architecture and Timing

GitHub Actions scheduling is an external platform dependency.

Production evidence shows that scheduled runs may start materially later than configured.

Observed delays have exceeded two hours.

This is not currently treated as a system failure because:

- the scheduled event eventually executes;
- the processing pipeline behaves correctly;
- outputs are persisted correctly.

## Current Mitigation

Schedule earlier than the desired reading time:

```text
06:05 Europe/Rome
```

This creates delivery buffer.

## Architectural Limitation

GitHub schedule delay currently affects both:

- delivery time;
- report-window composition.

The latter occurs because the CLI uses actual run time as the reporting cutoff.

Potential future mitigation:

```text
scheduled report date / fixed cutoff
→ deterministic information window
→ execution can happen later
```

No implementation has been selected yet.

---

# 21. Network Architecture

Current remote flow:

```text
feed URL
→ urllib Request
→ User-Agent
→ Accept header
→ 10-second timeout
→ TLS verification
→ normal redirects
→ feedparser
```

Validated production characteristics:

- all seven current sources have collected successfully;
- network failures remain isolated;
- no source requires authentication;
- no source currently requires custom rate-limit handling;
- one request per active source per run remains operationally lightweight.

Retry behaviour remains absent.

Rate-limit architecture remains absent.

Add either only when real evidence requires them.

---

# 22. Source Access Architecture

The production architecture now explicitly separates:

```text
automation access
```

from:

```text
reader access
```

This distinction is important after production exposed a Sifted Pro access problem and after the user mapped substantial Bocconi institutional access.

---

## Automated Source Layer

The production pipeline may ingest only sources available through:

- public RSS;
- public Atom;
- official free APIs;
- public structured metadata;
- other explicitly automation-permitted endpoints.

Production should not depend on authenticated publisher access.

---

## Personal Premium Reading Layer

The user may legitimately have direct or institutional access to publications such as:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore;
- Foreign Affairs;
- Harvard Business Review;
- other Bocconi-supported publications.

This can improve manual follow-up.

It does not automatically expand production ingestion rights.

---

## Research / Database Layer

Institutional research resources may include:

- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- S&P Capital IQ Pro;
- Aida.

These remain manual research tools unless an explicitly permitted automation interface exists.

The production architecture must not scrape them.

---

# 23. Security and Privacy Architecture

The repository is public.

The architecture must never require committing:

- credentials;
- Bocconi credentials;
- private Career OS content;
- private emails;
- newsletter-email content;
- authentication cookies;
- access tokens;
- licensed database text;
- restricted copyrighted content.

## Current Credential Position

The current production system requires no source credential.

This is preferable.

If a future optional feature requires a secret:

- it must use environment variables or GitHub Secrets;
- it must not expose secrets in logs;
- it must not become a dependency of the core system unless the user explicitly changes the architecture constraints.

Institutional premium content should not be introduced merely because credentials could technically be stored as GitHub Secrets.

The licensing and product-architecture question comes first.

---

# 24. Copyright and Content Boundaries

The repository may store, where permitted:

- titles;
- source names;
- direct links;
- timestamps;
- short feed descriptions;
- public structured summaries;
- derived classifications;
- derived scores;
- operational metadata.

The system must not store:

- complete copyrighted articles;
- paywall-bypassed content;
- authenticated premium article bodies;
- substantial unauthorised excerpts;
- licensed database full text.

## Richer-Report Boundary

The new richer-report requirement does not override these rules.

The objective is:

> provide enough lawful context for initial understanding.

It is not:

> reproduce the article.

The richer-report design must preserve provenance and use the smallest source-content footprint sufficient for the product need.

---

# 25. Architecture for ChatGPT Use

ChatGPT remains outside the production dependency chain.

The production system must remain useful without an API call to ChatGPT.

ChatGPT may be used manually for:

- development reasoning;
- code generation and review;
- project-document drafting;
- source/domain strategy evaluation;
- interpretation of selected stories;
- trend analysis;
- deciding whether a limitation justifies implementation complexity.

The architectural separation remains:

```text
Daily Intelligence System
= deterministic collection, filtering, ranking and reporting infrastructure

ChatGPT
= optional external reasoning and development layer
```

The future richer-report requirement does not automatically change this boundary.

Production LLM summarisation remains unselected.

---

# 26. Implemented vs Planned vs Deferred Architecture

## Implemented and Validated

- Python package;
- repository-native configuration;
- seven-source public RSS registry;
- seven-domain implemented taxonomy;
- RSS/Atom collection;
- local feed collection;
- remote HTTP/HTTPS collection;
- explicit User-Agent;
- explicit Accept header;
- 10-second request timeout;
- normal SSL verification;
- redirect handling;
- structured source outcomes;
- source-level failure isolation;
- normalisation;
- deterministic URL cleaning;
- UTC publication timestamps;
- deterministic SHA-256 record IDs;
- structural validation;
- previous-24-hours filtering;
- exact deduplication;
- deterministic classification;
- empty source defaults;
- deterministic ranking;
- JSONL persistence;
- Markdown reporting;
- structured run-summary JSON;
- pipeline orchestration;
- CLI;
- logging;
- automated tests;
- real-source validation;
- GitHub Actions workflow;
- manual workflow dispatch;
- automated tests in Actions;
- production execution in Actions;
- output validation;
- bot persistence;
- no-change guard;
- degraded automated publication;
- critical-failure protection;
- scheduled execution;
- concurrency protection;
- repository-native production history.

## Active Architectural Evaluation

- source correction and expansion;
- domain expansion;
- Sifted keep/replace/remove decision;
- source metadata richness;
- source accessibility;
- richer-report architecture;
- reporting-window cutoff independence.

## Deferred Until Evidence

- retry logic;
- near-duplicate clustering;
- story clustering;
- entity extraction;
- article-level geography;
- content-type classification;
- long-term source-health database;
- advanced ranking;
- automatic publisher-diversity penalties;
- LLM summarisation;
- authenticated premium ingestion;
- dashboards;
- GitHub Pages;
- GitHub Issues delivery;
- machine learning;
- embeddings;
- RAG;
- autonomous agents;
- cloud database;
- complex frontend.

---

# 27. Current Architectural Limitations

Known limitations include:

- current production source universe contains only seven feeds;
- Sifted may link to inaccessible Pro content;
- some feed descriptions are too thin for the intended richer report;
- OpenAI-related AI coverage may be publisher-concentrated;
- three target domains remain unimplemented;
- all current production feeds are English-language;
- full bilingual classification is unvalidated;
- exact deduplication does not detect differently worded coverage of the same story;
- records without publication timestamps are excluded;
- ranking remains provisional;
- classification remains conservative;
- some valid records remain unclassified;
- no entity enrichment exists;
- no article-level geographic classification exists;
- no content-type classification exists;
- no long-term source-health history exists;
- report context may be insufficient without click-through;
- report composition can be sparse or source-concentrated;
- scheduler timing is not precise;
- the collection window is tied to actual execution time;
- there is no dedicated latest-report alias;
- GitHub Markdown remains the primary delivery interface;
- there is no automated use of Bocconi premium content.

These limitations should not be interpreted as a feature backlog to implement automatically.

Each change still requires evidence.

---

# 28. Architecture Decision Rules

Before adding any new architectural component, ask:

1. What validated user problem does it solve?
2. Is the problem frequent enough to matter?
3. Can the source be replaced instead?
4. Can configuration solve it?
5. Can existing structured metadata solve it?
6. Can standard-library logic solve it?
7. Does it introduce recurring monetary cost?
8. Does it increase daily manual work?
9. Does it require credentials?
10. Does it create copyright or licence risk?
11. Does it introduce another service dependency?
12. How will it be tested?
13. How will failure be visible?
14. What maintenance burden does it add?
15. Can we stop with a simpler solution?

The preferred pattern remains:

```text
observe
→ reproduce
→ isolate
→ smallest justified change
→ test
→ inspect output
→ stop
```

---

# 29. Current Open Architecture Decisions

## Source Universe

The current seven-source registry is no longer assumed to be sufficient.

Immediate work:

- review current sources;
- evaluate Sifted;
- assess candidate replacements;
- evaluate new source proposals from the Career Agent;
- keep production collection public and permitted.

---

## Domain Universe

Reconsider:

- Financial Markets;
- Italy;
- Milan/Bocconi.

Do not implement without appropriate source support and classification evidence.

---

## Richer Report Context

Open question:

> What is the smallest deterministic and compliant mechanism that provides enough context for the user to understand selected developments without immediate click-through?

Candidate inputs should be evaluated in this order:

1. richer feed fields;
2. public structured metadata;
3. official free APIs;
4. limited permitted public extraction if justified;
5. more complex mechanisms only if necessary.

No architecture for AI summarisation has been selected.

---

## Reporting Window

Current:

```text
actual run time - 24 hours
→ actual run time
```

Candidate future architecture:

```text
fixed report cutoff
→ previous 24 hours
```

The fixed-cutoff design would decouple content selection from GitHub scheduler delay.

More production evidence is required before implementation.

---

## Output Validation for No-News Runs

The production workflow currently validates output files before persistence.

If a legitimate no-news run produces an empty processed JSONL file, current non-empty-file validation may need review.

Do not change this from theory alone.

Reproduce a valid no-news case first.

---

## Near-Duplicate Handling

Deferred until repeated report evidence demonstrates material repetition.

---

## Long-Term Source Health

Current per-run summaries remain sufficient.

Add historical source-health analysis only when recurring maintenance requires it.

---

## Delivery Interface

GitHub-rendered Markdown remains sufficient until actual mobile or reading friction becomes a demonstrated limitation.

Potential future options include:

- stable latest-report path;
- GitHub Pages;
- GitHub Issues;
- Obsidian-oriented reading workflow.

None are current core requirements.

---

# 30. Architecture Validation Gates

## Gate A — Local Architecture

**Status: passed**

Evidence:

- local orchestration works;
- deterministic processing works;
- tests exist;
- output is inspectable;
- failures are visible;
- CLI is operational.

---

## Gate B — Real-Source Architecture

**Status: passed**

Evidence:

- seven validated public feeds;
- 10-second timeout;
- explicit User-Agent;
- normal SSL verification;
- successful redirects;
- successful real-feed parsing;
- usable publication timestamps;
- real report generation;
- classification corrections;
- real degraded-source validation;
- 110 passing tests.

---

## Gate C — Automation Architecture

**Status: passed**

Required:

- manual Actions run;
- output validation;
- minimal required repository permissions;
- visible failure states;
- correct commit behaviour;
- no empty commits;
- no paid or AI dependency.

Evidence:

- `workflow_dispatch` validated;
- 110 tests pass in Actions;
- production CLI runs in Actions;
- application logging visible;
- outputs validated;
- bot persistence validated;
- no-change guard validated;
- critical configuration failure validated;
- degraded source publication validated.

---

## Gate D — Scheduled Production Architecture

**Status: passed**

Required:

- Gate C passed;
- scheduled trigger configured;
- scheduled run observed;
- concurrency behaviour safe;
- production history persisted.

Evidence:

- scheduled run observed;
- outputs produced;
- repository persistence succeeded;
- concurrency protection added;
- schedule now set to 06:05 Europe/Rome.

Known limitation:

- scheduler punctuality is not guaranteed.

Gate D passing means automation architecture is complete.

---

## Gate E — Source/Domain Expansion Architecture

**Status: open for controlled work**

Evidence justifying entry:

- Sifted accessibility problem;
- thin feed context;
- sparse/concentrated report;
- three missing target domains;
- broader user information needs;
- substantial available premium reading universe.

Requirements:

- strategic source/domain proposal;
- technical source review;
- automation-permission review;
- metadata inspection;
- controlled source testing;
- report-quality inspection;
- full regression tests.

---

## Gate F — Richer Report Architecture

**Status: not yet passed**

Required before implementation:

- precise richer-context requirement;
- metadata audit;
- copyright/access boundary;
- fallback behaviour;
- output-length target;
- source provenance model;
- candidate approach comparison;
- acceptance tests.

The problem is validated.

The architecture is not yet selected.

---

## Gate G — Advanced Quality Architecture

**Status: not yet passed**

Required:

- repeated real evidence;
- simpler deterministic changes insufficient;
- explicit evaluation method.

Potential examples:

- near-duplicate clustering;
- entity tracking;
- advanced ranking;
- content type;
- article-level geography.

---

# 31. Current Architecture Summary

The Daily Intelligence System is now a production-operational, repository-native deterministic Python pipeline.

Its core remains:

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
→ persist automatically
```

Remote collection follows:

```text
public RSS/Atom
→ bounded HTTP request
→ explicit headers
→ feedparser
→ isolated source result
```

Production automation follows:

```text
GitHub trigger
→ setup
→ install
→ test
→ run pipeline
→ validate outputs
→ commit changed artifacts
→ push
```

It currently has:

- zero recurring monetary cost;
- no production AI dependency;
- no paid API dependency;
- no production source credentials;
- seven active public sources;
- seven implemented domains;
- 110 passing tests;
- conservative deterministic classification;
- deterministic ranking;
- visible degraded-run behaviour;
- critical-failure protection;
- automated persistence;
- scheduled execution;
- concurrency protection;
- inspectable historical reports.

The main architectural bottleneck is no longer infrastructure.

It is information quality.

The next architectural work should therefore support:

> **source/domain correction and expansion first, followed by deliberate richer-report design.**

The architecture should not become more sophisticated merely because production automation is complete.

---

# Changelog

## 2026-08-14 — Phase 3 Automation Architecture Completed

- Reconciled the architecture with completed GitHub Actions production automation.
- Added the implemented `.github/workflows/daily-intelligence.yml` production layer.
- Recorded manual `workflow_dispatch`.
- Recorded scheduled execution.
- Recorded current 06:05 Europe/Rome production schedule.
- Recorded Python 3.12 hosted execution.
- Recorded full automated test execution before production processing.
- Recorded explicit workflow timeout.
- Recorded `contents: write` production permission.
- Recorded output validation before persistence.
- Recorded `github-actions[bot]` automated persistence.
- Recorded no-change commit protection.
- Recorded deliberate critical configuration failure validation.
- Recorded deliberate degraded source publication validation.
- Recorded concurrency protection with non-cancelling production semantics.
- Marked Gate C — Automation Architecture as passed.
- Added Gate D — Scheduled Production Architecture and marked it passed.
- Recorded substantial GitHub scheduler latency as an external platform limitation.
- Recorded scheduler-latency/report-window coupling as an open architecture decision.
- Recorded the current report as potentially too thin for initial understanding.
- Reframed report architecture so original sources are for deeper reading rather than necessarily basic comprehension.
- Added the richer-report architecture design boundary without choosing an implementation.
- Added the distinction between automated public sources, Bocconi premium reading and research/database layers.
- Explicitly prohibited authenticated premium-content ingestion as a consequence of Bocconi access.
- Recorded Sifted accessibility and metadata limitations as source-architecture evidence.
- Added source/domain expansion as the next active architectural work.
- Added no-news output validation as a future evidence-based edge case.
- Preserved zero recurring monetary cost and no-production-AI architecture.

## 2026-08-11 — Phase 2 Real-Source Architecture Validated

- Moved the minimal real-source registry into implemented architecture.
- Recorded seven validated public RSS sources.
- Expanded the implemented taxonomy from two to seven active domains.
- Added bounded remote HTTP retrieval with a 10-second timeout.
- Added explicit User-Agent and Accept request headers.
- Preserved normal SSL certificate verification.
- Validated redirects and real-feed parsing through the actual collector.
- Added explicit remote HTTP, URL and timeout failure handling through `CollectionError`.
- Kept retry logic absent because real-source evidence did not justify it.
- Added support for explicitly empty `default_domains`.
- Recorded the distinction between narrow source-wide defaults and broad heterogeneous feeds.
- Recorded evidence-based Global Politics keyword refinement.
- Confirmed real publication timestamps were usable with the current seven-feed source set.
- Confirmed optional missing descriptions did not invalidate records.
- Validated real-source report quality and corrected misleading source-default behaviour.
- Validated deliberate real-network partial-source failure.
- Recorded test isolation between deterministic fixtures and live production configuration.
- Reached 110 passing automated tests.
- Marked Gate B — Real-Source Architecture as passed.
- Made GitHub Actions manual execution the next architecture gate.

## 2026-08-11 — Phase 1 Architecture Baseline

- Replaced the pre-implementation architecture with the validated local system architecture.
- Added explicit orchestration and CLI components.
- Added collection-window filtering as a first-class processing stage.
- Recorded deterministic SHA-256 record identity.
- Recorded exact URL/title deduplication.
- Recorded deterministic classification and ranking behaviour.
- Recorded report selection and operational metadata behaviour.
- Recorded run-summary and logging responsibilities.
- Distinguished implemented, planned and deferred architecture.
- Removed speculative modules that were not part of the repository.
- Reframed near-duplicate, entity, geography and content-type logic as evidence-driven future enhancements.
- Defined real-source validation as the next architecture gate.

## Initial System Architecture Baseline

- Defined the deterministic pipeline architecture.
- Established Python and repository-native configuration as the core technical model.
- Defined source collection, normalisation, validation, deduplication, classification, ranking, storage and reporting responsibilities.
- Established zero recurring cost, public-source preference and no-production-AI constraints.