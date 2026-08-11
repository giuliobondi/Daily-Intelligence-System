````markdown
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

The deterministic local processing core and minimal real-source architecture are implemented and validated.

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
- automated unit and integration testing.

At the current Phase 2 closeout:

> **110 automated tests pass.**

The following production components are not yet implemented:

- GitHub Actions workflow;
- `workflow_dispatch`;
- automated repository persistence;
- automated commits;
- scheduled execution;
- production source-health history;
- longitudinal real-report quality evaluation;
- evidence-driven advanced quality logic.

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

The production automation layer should invoke the same deterministic pipeline rather than creating a separate processing path.

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

`default_domains` may now be an explicitly empty list:

```yaml
default_domains: []
```

This supports broad heterogeneous sources whose articles should rely on content-based classification rather than a forced publisher-wide topic.

`geographic_scope` remains required and non-empty.

This distinction was introduced after real report inspection showed that broad source defaults could create misleading classification and inflated relevance scores.

---

## 5.3 `collect.py`

Owns source collection.

The collector supports both:

- controlled local feed files;
- remote HTTP/HTTPS RSS or Atom feeds.

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

- `success`;
- `empty`;
- `failed`.

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
→ explicit User-Agent header
→ explicit Accept header
→ 10-second timeout
→ response bytes
→ feedparser
```

The collector currently uses standard-library networking rather than adding a third-party HTTP client.

The explicit User-Agent was added because live-source validation showed that some otherwise valid feeds rejected the previous bare request behaviour.

The explicit timeout was added because production requests must not be able to hang indefinitely.

Expected remote failures currently converted into `CollectionError` include:

- HTTP errors;
- URL/network errors;
- request timeout.

Normal SSL certificate verification remains enabled.

No SSL-verification bypass is part of the architecture.

### Parser Behaviour

After local or remote content is loaded, `feedparser` parses the feed.

A parser result marked as malformed through `bozo` is currently rejected with `CollectionError`.

Real-source validation did not expose a reason to weaken this policy.

### Retry Policy

No retry logic is currently implemented.

This is intentional.

The Phase 2 real-source set collected successfully enough that retry complexity was not justified.

Retry behaviour should be added only if automated production runs demonstrate a meaningful reliability problem that cannot be handled more simply by removing or replacing an unstable source.

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

### Publication Timestamps

The current normaliser uses feed-provided parsed publication timestamps.

During Phase 2 real-source validation, all observed returned entries from the seven selected feeds supplied usable publication timestamps.

No timestamp fallback architecture was therefore added.

The current conservative missing-publication policy remains appropriate until real production evidence shows otherwise.

### Optional Descriptions

Descriptions remain optional.

Some validated real feeds omit descriptions entirely or for some entries.

That does not make a record invalid.

No synthetic or generated description is created.

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

Real-source validation demonstrated that exact duplicate handling is already useful.

The observed real Phase 2 run removed exact duplicates without requiring semantic or near-duplicate logic.

Near-duplicate or semantic clustering remains deferred until repeated real reports demonstrate material repetition that exact deduplication cannot address.

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

### Current Implemented Taxonomy

The current implemented taxonomy contains seven active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

The broader target taxonomy remains defined in `03 Information Taxonomy and Source Policy.md`.

### Source Defaults

Source defaults are interpreted as prior topical evidence.

They should therefore be used only when the feed is narrow enough that essentially every item legitimately belongs to that domain.

Broad heterogeneous feeds may use no defaults.

Current real-source behaviour includes:

- BBC News World → no default domain;
- BBC News Business → no default domain;
- European Central Bank → no default domain;
- European Commission Highlighted News → no default domain;
- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

This policy was introduced after the first real report showed that broad defaults could force unrelated stories into misleading sections.

### Evidence-Based Keyword Refinement

Real report review exposed a conservative recall gap in Global Politics and Geopolitics.

Candidate keywords were tested against the actual processed sample before configuration was changed.

The following terms were added after that review:

- `war`;
- `conflict`;
- `parliament`.

Broader candidates such as `government`, `defence`, `president` and `prime minister` were not added because the sample showed ambiguity or low-value matches.

The architecture therefore treats taxonomy keywords as evidence-driven configuration, not as a completeness exercise.

---

## 5.9 `rank.py`

Owns deterministic relevance scoring.

The current score is provisional and intentionally simple.

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

- 2 points per assigned domain;
- 1 point per matched keyword.

Score components are retained with each processed record for transparency.

The current formula is not treated as a final relevance model.

### Real-Source Ranking Lesson

Phase 2 showed that ranking quality depends on classification quality.

Broad default domains inflated relevance scores even though the ranking implementation itself behaved exactly as configured.

The corrective action was therefore made at the classification/source-default layer rather than by prematurely changing ranking weights.

Ranking should change only when repeated real-report review demonstrates systematic ordering problems that cannot be solved more simply upstream.

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

It contains two distinct responsibilities.

### Selection

The public report selector determines which processed records appear.

Current selection behaviour:

- excludes unclassified records;
- requires an active primary domain;
- orders records deterministically;
- respects maximum items per domain;
- respects maximum items overall.

### Primary-Domain Placement

The first eligible assigned domain is used as the story's primary report section.

Later assigned domains appear as secondary metadata.

Because domain order affects report placement, source-default order and classification evidence must remain intentional.

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

### Real Report Validation

Phase 2 validated the report against real source data.

The first real run exposed misleading broad-source classification.

After source-default correction and conservative keyword refinement, the report became materially smaller and more credible.

This established an architectural rule:

> Report usefulness is a validation criterion for upstream processing decisions.

A technically successful run is not sufficient if report output is misleading or noisy.

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

The same summary object supports both:

- persistent JSON operational output;
- user-facing Markdown operational metadata.

This prevents report status from being recomputed independently.

---

## 5.13 `pipeline.py`

Owns end-to-end orchestration.

It coordinates processing stages without absorbing their internal logic.

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

### Current Normalisation-Failure Boundary

The pipeline currently normalises entries from successful sources directly.

A broad per-entry `NormalizationError` isolation layer has not been added.

Phase 2 real-source testing normalised all observed entries from the seven selected feeds successfully, so no evidence-based change was justified.

If a future real source exposes one malformed entry that can terminate an otherwise valid source run, the failure should be reproduced with a regression test before this orchestration boundary is changed.

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

### Local Installation Note

During development, source-based pytest execution can reflect repository code even when the locally installed package used by the CLI is stale.

If validated source changes are not reflected in:

```text
python -m daily_intelligence.cli run
```

the local package installation should be refreshed before diagnosing a new application bug.

This is a development-environment concern, not a production architecture dependency.

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

The current active source registry contains seven validated public RSS feeds:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News;
- Istat Press Releases;
- OpenAI News;
- Sifted.

All current real feeds use public access and require no repository secret.

`source_type` currently represents feed protocol and accepts:

- `rss`;
- `atom`.

It is not a publisher-category field.

Potential future source metadata should not be added until required by processing or maintenance.

### Empty Default Domains

`default_domains` is required as a configuration field but may be empty.

Example:

```yaml
default_domains: []
```

This allows broad sources to rely on content evidence rather than being force-classified.

---

## 6.2 `domains.yaml`

Current implemented domain fields include:

- `id`;
- `name`;
- `keywords`;
- `active`.

Current active implemented domains are:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

The broader target taxonomy is defined in `03 Information Taxonomy and Source Policy.md`.

The following target domains are not currently implemented:

- Financial Markets;
- Italy;
- Milan and Bocconi ecosystem.

Domain expansion should remain evidence-driven.

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

The implemented CLI uses:

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

The run summary records validation counts separately from report eligibility.

For example:

```text
raw items: 1
valid items: 1
displayed items: 0
```

is legitimate when the valid article falls outside the monitored publication window.

An explicit post-window eligibility count is not currently part of the run-summary schema.

That should be added only if operational use demonstrates that it materially improves observability.

### Real-Source Validation

The previous-24-hours policy worked adequately with the current seven-feed source set during Phase 2 validation.

No tolerance or fallback window was added.

Reconsider only if scheduled real-world use demonstrates systematic misses caused by publication-time behaviour.

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

Classification is rules-based.

The design intentionally separates:

- source defaults;
- domain configuration;
- keyword matching.

Source defaults provide prior domain knowledge only where a feed is genuinely narrow.

Keyword matching allows individual articles to receive domains based on content.

A record can therefore receive multiple domains.

A record may also remain unclassified.

Current primary-domain behaviour is deterministic:

- the first assigned eligible domain becomes the report section;
- later domains become secondary tags.

Potential future classification dimensions include:

- geography;
- content type;
- entities.

They are not implemented dependencies of the core pipeline.

### Conservative Classification Principle

Real-source validation demonstrated that broad source defaults can create misleading report placement.

Therefore:

> prefer no source default over a weak or merely publisher-level default.

Similarly:

> prefer an unclassified record over a misleading classification.

This policy should remain unless repeated real usage demonstrates that recall is too low and a tested deterministic correction is available.

---

# 11. Ranking Architecture

Ranking is a deterministic prioritisation layer, not an attempt to model objective news importance.

The score is used to order already-processed items before report limits are applied.

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

### Product-Quality Requirement

The report is part of system validation.

A technically successful run is insufficient if the output is:

- misleading;
- excessively noisy;
- repetitive;
- badly classified;
- too long to scan.

Phase 2 used direct real-report inspection to validate and correct classification behaviour before automation.

---

# 13. Run Status and Failure Architecture

Failure handling distinguishes ordinary source degradation from critical system failures.

## Source-Level Failures

Expected source-level failures are isolated.

Examples include:

- unavailable remote feed;
- HTTP failure;
- DNS or URL failure;
- request timeout;
- missing local fixture;
- malformed source response handled by the collector.

A source failure produces:

- `failed` source status;
- error metadata;
- degraded run status where appropriate;
- visible warning in the Markdown report;
- visible warning in logs.

Successful sources continue contributing output.

### Real-Network Validation

Phase 2 deliberately tested:

- one valid real Istat feed;
- one invalid remote hostname.

Observed behaviour:

- Istat succeeded;
- the invalid remote source failed with `CollectionError`;
- overall run status became `degraded`;
- the warning appeared in run-summary JSON and Markdown;
- valid Istat output remained available.

This confirms source-failure isolation against actual network behaviour rather than only controlled fixtures.

## Empty Sources

A valid source with no entries is represented as `empty`, not as a failure.

## Critical Failures

Failures that prevent trustworthy execution should not be silently downgraded.

Examples include:

- invalid core configuration;
- unexpected programming errors;
- invalid critical assumptions;
- failures that prevent valid output persistence.

Critical failure and publication policy must be incorporated explicitly into GitHub Actions behaviour.

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

The repository itself is the intended initial storage and delivery layer.

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

The CLI derives paths using this structure.

### Local Validation Artifacts

Runtime output generated during controlled local testing should not automatically be treated as permanent repository data.

During Phase 2, real JSONL, Markdown and run-summary files were generated and inspected locally, then removed after validation.

This preserved the distinction between:

- local production-like validation artifacts;
- actual automated production history.

### Production Persistence

Automated persistence remains intended for Phase 3.

The GitHub Actions design must define:

- when outputs are considered valid;
- which outputs are committed;
- commit behaviour;
- no-change behaviour;
- critical-failure publication rules.

Do not add `data/` or `reports/` to `.gitignore` merely because Phase 2 validation artifacts were removed.

Repository-native production history remains the intended initial model.

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

Network-fed production runs naturally differ when external source data changes.

### Automation Requirement

GitHub Actions persistence must preserve this deterministic intent.

A no-change run should not create an empty repository commit.

---

# 17. Testing Architecture

Testing is part of the architecture rather than an optional development convenience.

At Phase 2 closeout:

> **110 tests pass.**

Current coverage includes:

- configuration loading;
- empty source-default validation;
- non-empty geographic-scope validation;
- source collection;
- controlled feed fixtures;
- bounded remote request behaviour;
- remote User-Agent behaviour;
- HTTP failure handling;
- URL/network failure handling;
- timeout handling;
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

This behaviour has been tested both:

- with controlled fixtures;
- with a deliberate real-network failure.

### Out-of-Window Record

A structurally valid article is collected but published outside the monitored interval.

Expected behaviour:

- raw count reflects collection;
- validation count reflects structural validity;
- record is excluded before deduplication/classification/reporting;
- displayed count is zero if no other eligible items exist.

### Logging

Important run-stage messages are exposed through the pipeline logger.

### Test Isolation

Automated integration tests must not depend on live production source configuration.

Controlled pipeline tests use temporary or fixture source configuration so that:

- test outcomes remain deterministic;
- internet availability does not affect the automated suite;
- changes to `config/sources.yaml` do not invalidate fixture expectations.

Real source behaviour is validated separately through controlled manual production-like runs.

---

# 18. Production Automation Architecture

GitHub Actions is the intended production execution environment, but it is not yet implemented.

The workflow should remain a thin wrapper around the same Python pipeline.

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

### Phase 3 Entry Rule

Scheduled execution should not be enabled immediately.

The required progression is:

```text
workflow_dispatch
→ manual Actions run
→ inspect logs
→ inspect outputs
→ inspect commit behaviour
→ inspect failure behaviour
→ only then consider schedule
```

The local Phase 2 real-source validation is sufficient to begin this manual Actions work.

It is not sufficient to skip it.

---

# 19. Network Architecture

Remote-source behaviour is now implemented and validated for the current source set.

Current remote flow:

```text
feed URL
→ urllib Request
→ User-Agent
→ Accept header
→ 10-second timeout
→ HTTPS verification / normal redirects
→ response bytes
→ feedparser
```

### Validated Behaviour

Phase 2 established that:

- requests do not wait indefinitely;
- an explicit User-Agent is required by some feeds;
- normal HTTPS certificate verification works;
- BBC redirect behaviour works;
- all seven selected feeds can be parsed through the actual project collector;
- source-level network failures remain isolated;
- real feed metadata is usable;
- publication timestamps are adequate for the current window logic.

### Retry Architecture

Retries remain intentionally absent.

The current design principle is:

- bounded single requests first;
- remove or replace a poor source before adding disproportionate resilience logic;
- add retries only when repeated automated evidence demonstrates that a bounded retry materially improves reliability.

### Rate Limits

No current source required special rate-limit handling during Phase 2.

The system makes one feed request per configured source per run.

Additional rate-limit architecture should not be added without evidence.

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

The current seven real sources require no credentials.

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
- seven-source real public RSS registry;
- seven-domain implemented taxonomy;
- RSS/Atom collection;
- local feed collection;
- remote HTTP/HTTPS feed collection;
- explicit User-Agent;
- explicit Accept header;
- 10-second request timeout;
- normal SSL verification;
- redirect handling through standard-library HTTP behaviour;
- structured source results;
- source-level network failure isolation;
- normalisation;
- deterministic URL cleaning;
- UTC publication timestamp parsing;
- deterministic SHA-256 record IDs;
- validation;
- collection-window filtering;
- exact deduplication;
- deterministic domain classification;
- optional empty source default domains;
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
- automated tests;
- real-source manual pipeline validation;
- real-network degraded-run validation;
- evidence-based classification refinement.

## Planned for Production MVP

- GitHub Actions workflow;
- `workflow_dispatch`;
- minimal repository permissions;
- explicit workflow timeout;
- automated output validation;
- automated repository persistence;
- automated commits;
- no-change commit protection;
- scheduled execution after manual workflow validation;
- longitudinal real-use evaluation.

## Deferred Until Evidence

- retry logic;
- near-duplicate clustering;
- story clustering;
- entity extraction;
- geographic classification;
- content-type classification;
- source-health history;
- advanced source penalties;
- sophisticated ranking;
- broad taxonomy expansion;
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

The current system should not yet be described as fully automated production infrastructure.

Known limitations include:

- GitHub Actions is not implemented;
- automated commits are not implemented;
- scheduled execution is not implemented;
- production persistence policy is not yet validated in GitHub Actions;
- exact deduplication cannot detect differently worded versions of the same story;
- records with missing publication timestamps are excluded from report-window eligibility;
- ranking remains provisional;
- classification remains intentionally conservative;
- some valid unique records remain unclassified and therefore absent from the report;
- URL normalisation removes selected tracking parameters but does not currently remove every publisher-specific tracking parameter;
- no entity enrichment exists;
- no article-level geographic classification exists;
- no content-type classification exists;
- no production source-health history exists;
- no broad per-entry normalisation-failure isolation exists;
- real daily report quality has not yet been evaluated over a sustained automated period.

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

## GitHub Actions Workflow Structure

Determine the smallest workflow that can:

- install the project;
- execute the validated pipeline;
- validate outputs;
- expose failures;
- persist changed artifacts safely.

Owner: Phase 3.

## Workflow Permissions

Determine the minimum repository permissions required for automated persistence.

Owner: Phase 3.

## Workflow Timeout

Set an explicit Actions-level timeout that comfortably exceeds expected normal execution while preventing indefinitely stuck jobs.

Owner: Phase 3.

## Automated Commit Strategy

GitHub Actions commit behaviour must ensure:

- outputs are validated first;
- no empty commits;
- one coherent commit per successful publication event;
- critical failures do not publish misleading output.

Owner: Phase 3.

## Degraded-Run Publication Policy

The local pipeline can produce useful degraded output when one source fails.

Phase 3 must determine whether a degraded automated run should:

- still publish valid output;
- publish with visible warning;
- or fail the workflow under specific thresholds.

The simplest behaviour consistent with existing local semantics should be preferred.

Owner: Phase 3.

## Schedule

Do not enable scheduled execution until `workflow_dispatch` has been validated.

Once manual Actions execution is stable, select the smallest appropriate recurring schedule.

Owner: Phase 3.

## Missing Publication Timestamp Policy

Current behaviour excludes missing publication timestamps.

Phase 2 did not reveal a problem with the current seven-source set.

Reconsider only if valuable future sources frequently omit the field.

Owner: evidence from Phase 4 or later.

## Collection Window

Current CLI default is the previous 24 hours.

Phase 2 did not demonstrate a need to change it.

Reconsider tolerance only if scheduled source publication behaviour causes systematic misses.

Owner: evidence from production use.

## Retry Policy

No retry behaviour is currently implemented.

Add only if repeated automated runs demonstrate a meaningful transient-failure problem.

Owner: evidence from Phase 3 or Phase 4.

## Near-Duplicate Detection

No implementation until exact deduplication proves insufficient.

Owner: Phase 5 if justified.

## Production Source Health History

Current run summaries capture per-run operational state but not long-term source health.

Add only if recurring source reliability becomes difficult to manage manually.

## Output Retention

Repository-native daily history is intended.

Retention or archival policy should be revisited only after real production growth is measurable.

---

# 27. Architecture Validation Gates

## Gate A — Local Architecture

**Status: passed**

Required:

- local orchestration works;
- deterministic processing works;
- test coverage exists;
- output is inspectable;
- failures are visible.

Evidence includes:

- complete local vertical slice;
- CLI validation;
- deterministic processing tests;
- degraded fixture tests;
- collection-window validation;
- report and run-summary inspection.

## Gate B — Real-Source Architecture

**Status: passed**

Required:

- small live source set works reliably enough;
- requests cannot hang indefinitely;
- source metadata is usable;
- report output is useful;
- no critical external-source behaviour is unresolved.

Evidence includes:

- seven validated real public feeds;
- explicit 10-second request timeout;
- explicit User-Agent;
- normal SSL verification;
- successful redirect behaviour;
- successful parsing through the actual collector;
- usable publication timestamps;
- successful normalisation of observed real entries;
- real report generation;
- evidence-based classification corrections;
- deliberate real-network degraded-source validation;
- 110 passing automated tests.

Gate B passing permits work on automation.

## Gate C — Automation Architecture

**Status: not yet passed**

Required:

- real-source architecture has passed;
- manual GitHub Actions run works;
- outputs are validated before persistence;
- permissions are minimal;
- failure states are visible;
- commit behaviour is correct;
- no empty commits are created;
- no paid or AI dependency is introduced.

Gate C must be passed before scheduled production execution is considered stable.

## Gate D — Advanced Quality Architecture

**Status: not yet passed**

Required:

- repeated real reports demonstrate a material limitation;
- simpler deterministic adjustments are insufficient;
- the new component has an explicit evaluation method.

Phase 2 justified narrow classification corrections.

It did not justify near-duplicate clustering, semantic processing, major ranking redesign or broader architecture.

---

# 28. Current Architecture Summary

The Daily Intelligence System is currently a repository-native deterministic Python pipeline with a validated minimal real-source layer.

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

Remote collection currently follows:

```text
public RSS/Atom feed
→ bounded HTTP request
→ explicit request headers
→ feedparser
→ isolated source result
```

It runs locally through:

```text
python -m daily_intelligence.cli run
```

It has:

- zero recurring monetary cost;
- no production AI dependency;
- seven validated real public sources;
- seven implemented domains;
- conservative deterministic classification;
- visible degraded-run behaviour;
- 110 passing automated tests.

Phase 2 established that the architecture can produce useful real output and tolerate ordinary source failure.

The next architectural objective is not additional quality sophistication.

It is:

> run this same validated pipeline through the smallest safe GitHub Actions `workflow_dispatch` workflow and validate persistence, permissions, failure behaviour and commit semantics before scheduling.

---

# Changelog

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
- Confirmed optional missing descriptions do not require architectural fallback.
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
- Recorded current deterministic classification and ranking behaviour.
- Recorded report selection and operational metadata behaviour.
- Recorded run-summary and logging responsibilities.
- Distinguished implemented, production-planned and deferred components.
- Removed speculative modules that are not part of the current repository.
- Reframed near-duplicate, entity, geography and content-type logic as evidence-driven future enhancements.
- Defined real-source validation as the next architecture gate before GitHub Actions.
````
