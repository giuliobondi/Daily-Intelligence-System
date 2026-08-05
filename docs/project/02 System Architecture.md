# Daily Intelligence System — System Architecture

> **Purpose**
>
> This document defines how the Daily Intelligence System will satisfy the approved product requirements.
>
> It describes the system components, data flow, configuration, storage, automation, failure handling and public-repository boundaries.
>
> It defines the intended architecture without locking the project into unnecessary implementation complexity.
>
> ---
>
> **Primary Question**
>
> > *How should the system collect, process, store and publish information reliably at zero recurring cost and with negligible daily manual work?*
>
> ---
>
> **Update Frequency**
>
> Update when a material architectural decision changes the system’s components, data flow, storage, automation, security boundaries or operational model.

---

# Architectural Objective

The architecture should support one complete daily workflow:

    Configured public sources
            ↓
    Collection
            ↓
    Record normalisation
            ↓
    Validation
            ↓
    Duplicate reduction
            ↓
    Domain classification
            ↓
    Relevance scoring
            ↓
    Processed storage
            ↓
    Daily Markdown report
            ↓
    Automated persistence
            ↓
    Visible run status

The system should remain:

- zero-cost in normal operation;
- deterministic;
- repository-native;
- transparent;
- modular enough to maintain;
- simple enough to understand;
- resilient to individual source failures;
- independent from paid AI services.

The architecture should solve the current workflow before supporting future features.

---

# Architectural Principles

## Repository-Native

The system should run primarily through:

- Python;
- GitHub Actions;
- version-controlled configuration;
- repository-based reports and processed data.

External infrastructure should not be required for the MVP.

## Deterministic Before Intelligent

Classification, ranking and duplicate reduction should begin with deterministic logic.

The architecture should not depend on:

- LLM calls;
- embeddings;
- vector databases;
- autonomous agents;
- machine-learning services;
- paid inference APIs.

## Configuration Before Hard-Coding

Sources, domains, keywords, entities and ranking weights should be maintained outside core Python logic where practical.

## Partial Failure Tolerance

A single invalid feed or malformed record should not stop all successful sources from being processed.

Critical pipeline failures should stop publication of a falsely successful report.

## Explainability

The system should preserve enough metadata to explain:

- where an item came from;
- how it was classified;
- why it received its score;
- whether it belongs to a duplicate cluster;
- whether a run was complete.

## Minimal Dependencies

The architecture should use a small number of stable libraries.

New dependencies should be introduced only when they provide clear value.

## Public-Safe by Default

All committed outputs must remain suitable for a public repository.

---

# System Boundary

The GitHub repository owns:

- source configuration;
- collection;
- normalisation;
- validation;
- deduplication;
- classification;
- ranking;
- storage;
- report generation;
- automated execution;
- execution visibility.

The repository does not own:

- ChatGPT scheduled research;
- AI-generated interpretation;
- private newsletter ingestion;
- private email access;
- Career OS updates;
- paid source access;
- full article extraction;
- investment or political recommendations.

---

# High-Level Components

The MVP should contain the following logical components.

    Configuration
        ↓
    Collector
        ↓
    Normalizer
        ↓
    Validator
        ↓
    Deduplicator
        ↓
    Classifier
        ↓
    Ranker
        ↓
    Storage
        ↓
    Report Generator
        ↓
    Automation and Persistence
        ↓
    Logs and Run Summary

Each component should have one clear responsibility.

---

# 1. Configuration Layer

## Responsibility

Define the behaviour of the system without requiring changes to core processing logic.

## Initial Configuration Areas

The architecture should support configuration for:

- sources;
- domains;
- keywords;
- tracked entities;
- geographic priorities;
- ranking weights;
- report limits;
- collection window;
- timezone;
- language handling;
- source activation status.

## Recommended Format

Use YAML for manually maintained configuration.

Reasons:

- readable in GitHub and VS Code;
- suitable for nested structures;
- easier to edit than JSON;
- widely supported in Python;
- appropriate for small configuration files.

## Initial Configuration Files

The likely initial structure is:

    config/
    ├── sources.yaml
    ├── domains.yaml
    ├── entities.yaml
    └── settings.yaml

### `sources.yaml`

Defines:

- source ID;
- name;
- feed URL;
- homepage URL;
- source tier;
- source type;
- default domains;
- language;
- geographic scope;
- active status.

### `domains.yaml`

Defines:

- domain IDs;
- display names;
- report order;
- keywords;
- exclusions;
- default weights;
- active status.

### `entities.yaml`

Defines tracked entities and aliases.

This file may remain small during the MVP.

### `settings.yaml`

Defines operational settings such as:

- collection-window length;
- timezone;
- report item limits;
- similarity thresholds;
- ranking weights;
- output paths;
- whether optional sections are displayed.

## Validation

Configuration should be validated at startup.

Invalid required fields should produce a clear error before collection begins.

---

# 2. Collection Layer

## Responsibility

Retrieve items from configured public structured sources.

## Initial Supported Source Types

The MVP should initially support:

- RSS;
- Atom.

Official public APIs may be added later when they fill a demonstrated coverage gap.

Supporting RSS and Atom first is sufficient to test the complete architecture.

## Collector Behaviour

For each active source:

1. read the source configuration;
2. request or parse the feed;
3. record collection start time;
4. capture available entries;
5. preserve source identity;
6. record success, empty result or failure;
7. continue to the next source.

## Source-Level Isolation

Each source should be processed independently.

A failure should create a source result such as:

    source_id
    status
    items_received
    error_type
    error_message
    retrieved_at

The collector should distinguish:

- successful source with items;
- successful source with no new items;
- source parse failure;
- source network failure;
- invalid source configuration.

## Network Handling

Where direct HTTP requests are used:

- use an explicit timeout;
- use a descriptive user agent;
- avoid repeated unnecessary requests;
- respect the source’s public endpoint and usage conditions;
- avoid aggressive retry behaviour.

## Output

The collection layer should return raw source records in a common preliminary structure.

It should not perform final classification or ranking.

---

# 3. Normalisation Layer

## Responsibility

Convert raw feed entries into a consistent internal record format.

## Normalisation Tasks

The normaliser should handle:

- field-name consistency;
- whitespace cleanup;
- title cleanup;
- timestamp parsing;
- timezone normalisation;
- URL cleanup;
- author formatting;
- description cleanup;
- language and source metadata attachment.

## Timestamp Convention

Use UTC internally.

Reasons:

- consistent comparison across global sources;
- compatible with ISO 8601;
- easier scheduled processing;
- avoids ambiguity during daylight-saving changes.

Reports may display timestamps in Europe/Rome where useful, but stored timestamps should remain UTC.

## URL Policy

For each item, preserve:

- original URL;
- normalised URL.

Normalisation may remove:

- common tracking parameters;
- URL fragments;
- unnecessary trailing slashes.

The system should not attempt aggressive canonicalisation that could break a valid link.

## Title Policy

Preserve:

- original title;
- normalised title.

The normalised title may:

- convert to lowercase;
- remove repeated whitespace;
- standardise punctuation;
- remove leading or trailing whitespace.

The original title must remain available for report display.

## Output

The normalisation layer should produce candidate internal records.

---

# 4. Validation Layer

## Responsibility

Determine whether each candidate record is usable.

## Required Fields

A record should normally require:

- source ID;
- title;
- usable article URL;
- retrieval timestamp.

Publication timestamp is strongly preferred but may be absent.

## Publication Timestamp Policy

If `published_at` is missing or invalid:

1. retain the record only if the source and retrieval metadata are otherwise valid;
2. mark the publication time as unavailable;
3. avoid treating retrieval time as confirmed publication time;
4. apply a ranking or report penalty if configured;
5. keep the limitation visible.

The system should not invent publication timestamps.

## Invalid Records

Records should be excluded when:

- title is missing or empty;
- URL is unusable;
- source identity is missing;
- required fields cannot be normalised safely.

Excluded records should be counted and logged with a reason.

## Output

The validator should produce:

- valid candidate records;
- invalid-record summaries.

---

# 5. Collection-Window Filtering

## Responsibility

Select records relevant to the current reporting period.

## Initial Policy

The daily run should primarily select items published within the previous 24 hours.

A configurable tolerance should be allowed because:

- GitHub Actions may start later than scheduled;
- some feeds publish delayed timestamps;
- international time zones differ;
- occasional workflow failures may require recovery.

## Recommended Initial Window

Use a configurable 30-hour lookback during the MVP.

This provides modest tolerance without turning the report into a multi-day archive.

The exact value should remain configurable and should be evaluated during testing.

## Missing Timestamp Items

Items without a reliable publication timestamp may be included only when:

- they were not previously processed;
- they were retrieved during the current run;
- configuration allows them.

They should be visibly marked and may receive a ranking penalty.

---

# 6. Record Identity and Idempotency

## Responsibility

Prevent repeated runs from creating uncontrolled duplicate records.

## Record ID

Each record should receive a deterministic identifier derived from stable values.

Recommended approach:

    record_id = hash(source_id + normalized_url)

Fallback when URL normalisation is insufficient:

    record_id = hash(source_id + normalized_title + published_at)

The exact implementation should preserve consistency across repeated runs.

## Idempotent Behaviour

Running the pipeline twice with the same inputs should not create additional copies of the same record.

The system should:

- recognise existing record IDs;
- update only when a meaningful field changes;
- avoid duplicate daily report entries;
- avoid unnecessary commits when outputs are unchanged.

---

# 7. Duplicate Reduction Layer

## Responsibility

Reduce repeated presentation while preserving useful source diversity.

## Stage 1 — Exact Duplicate Detection

The MVP must detect:

- identical normalised URLs;
- identical normalised titles;
- repeated source records.

Exact duplicates may be merged or suppressed automatically.

## Stage 2 — Near-Duplicate Detection

The MVP should support conservative title similarity.

Recommended initial method:

- token-based title similarity;
- deterministic similarity threshold;
- comparison only within the relevant time window;
- optional support from shared entities or keywords.

The exact algorithm should be simple and inspectable.

A lightweight library may be used if it materially improves reliability.

## Cluster Structure

Each cluster should preserve:

- cluster ID;
- primary record ID;
- member record IDs;
- unique source count;
- earliest publication time;
- latest publication time.

## Primary Record Selection

Select the primary record using a deterministic order such as:

1. highest source tier;
2. highest relevance score;
3. most complete metadata;
4. earliest direct publication;
5. stable record-ID tie-break.

The final order may be refined after sample evaluation.

## Conservative Policy

When similarity is uncertain, preserve separate records.

False merging is more harmful than displaying a limited amount of duplication during the MVP.

---

# 8. Domain Classification Layer

## Responsibility

Assign topic domains and geographic tags using transparent rules.

## Classification Inputs

The classifier may use:

- source default domains;
- title keywords;
- description keywords;
- tracked entities;
- aliases;
- exclusion terms;
- geographic references.

## Initial Rule Model

Each domain configuration may contain:

    id
    name
    keywords
    strong_keywords
    keyword_groups
    exclusions
    default_weight
    report_order

## Suggested Classification Logic

1. Start with configured source defaults.
2. Detect strong title matches.
3. Detect entity matches.
4. Detect keyword groups.
5. Review description matches.
6. Apply exclusion rules.
7. Assign one or more domains.
8. Mark unmatched records as unclassified.

## Classification Evidence

Each record should preserve:

- assigned domains;
- matched keywords;
- matched entities;
- source-default contribution;
- exclusions applied.

## Primary Domain

For report placement, one primary domain may be selected from the assigned domains using:

1. strongest classification evidence;
2. domain priority;
3. configured report order.

Secondary domains remain stored.

This avoids excessive repetition in the daily report.

## Unclassified Records

Unclassified records should:

- remain in processed storage;
- be counted in the run summary;
- remain available for evaluation;
- be omitted from the main report by default.

A high unclassified rate should trigger taxonomy review.

---

# 9. Geographic Classification

## Responsibility

Assign geographic tags independently from topic domains.

## Inputs

Geographic classification may use:

- source geographic defaults;
- country names;
- city names;
- institutions;
- tracked entities;
- configured aliases.

## Output

Each record may receive:

- zero or more geographic tags;
- one primary geography for ranking or display.

Geography should not be inferred from publication location alone.

---

# 10. Content-Type Classification

## Responsibility

Assign one content type where practical.

## Initial Types

- Official Announcement;
- Data Release;
- Research;
- News Reporting;
- Analysis;
- Opinion;
- Company Update;
- Funding or Transaction;
- Event or Opportunity;
- Technical Release;
- Other.

## Classification Method

Content type may be inferred from:

- source type;
- feed category;
- title patterns;
- configured keywords;
- source defaults.

The classification should remain conservative.

---

# 11. Relevance-Scoring Layer

## Responsibility

Assign a deterministic and explainable score used for report ordering.

## Scoring Philosophy

The score should represent practical relevance to the user, not absolute global importance.

The score should remain:

- deterministic;
- configurable;
- inspectable;
- reproducible.

## Initial Score Components

A first scoring model may include:

    base score
    + source-tier weight
    + domain-priority weight
    + geography-priority weight
    + tracked-entity weight
    + content-type weight
    + multi-source coverage bonus
    + recency bonus
    - duplicate penalty
    - missing-metadata penalty
    - promotional-content penalty

## Example Conceptual Formula

    relevance_score =
        source_quality
      + domain_relevance
      + geography_relevance
      + entity_relevance
      + content_type_relevance
      + coverage_bonus
      + recency_bonus
      - quality_penalties

The exact weights should be defined through configuration after sample testing.

## Score Components

Each record should preserve the contribution of each component.

Example:

    score_components:
      source_tier: 3
      domain_priority: 4
      geography_priority: 2
      entity_priority: 1
      coverage_bonus: 2
      metadata_penalty: -1

## Tie-Breaking

Recommended stable order:

1. relevance score descending;
2. publication time descending;
3. source tier ascending;
4. normalised title;
5. record ID.

---

# 12. Storage Architecture

## Responsibility

Persist processed records, reports and run summaries in a form compatible with a public Git repository.

## Storage Decision

Use JSON Lines for processed article records during the MVP.

### Why JSON Lines

- simple and human-inspectable;
- each record remains independently readable;
- append and filter operations are straightforward;
- nested fields such as domains and score components are supported;
- easy to use with Python;
- compatible with Git diffs at small MVP scale;
- avoids introducing a database before required.

### Why Not SQLite Initially

SQLite is useful for querying and scale, but during the MVP it would:

- produce binary database diffs;
- reduce GitHub readability;
- complicate review;
- add migration concerns;
- provide more capability than initially needed.

SQLite may be reconsidered if the archive becomes too large or query requirements materially increase.

### Why Not CSV

CSV is weak for:

- lists of domains;
- score components;
- duplicate clusters;
- nested metadata;
- optional fields.

## Proposed Data Structure

    data/
    ├── processed/
    │   ├── 2026/
    │   │   ├── 08/
    │   │   │   ├── 2026-08-04.jsonl
    │   │   │   └── ...
    │   └── ...
    └── runs/
        ├── 2026/
        │   ├── 08/
        │   │   ├── 2026-08-04.json
        │   │   └── ...

## Raw Data

The MVP should not persist complete raw feed responses by default.

Reasons:

- unnecessary repository growth;
- possible copyrighted content;
- low operational value;
- duplication of public source data.

Small test fixtures may be stored under `tests/fixtures/`.

## Processed Records

Processed records may contain:

- permitted source metadata;
- classifications;
- duplicate information;
- ranking data;
- processing status.

## Run Summary

Each run should create a structured summary containing:

    run_id
    started_at
    completed_at
    status
    collection_window
    active_sources
    successful_sources
    empty_sources
    failed_sources
    raw_items
    valid_items
    invalid_items
    duplicate_items
    displayed_items
    warnings

---

# 13. Report-Generation Layer

## Responsibility

Generate a concise, readable Markdown report from processed records.

## Separation from Collection

Report generation should operate on processed records, not directly on live feed responses.

This improves:

- reproducibility;
- testing;
- debugging;
- future formatting changes.

## Proposed Report Path

    reports/
    └── daily/
        └── 2026/
            └── 08/
                └── 2026-08-04.md

## Report Construction

The generator should:

1. load the current run summary;
2. load eligible processed records;
3. select primary cluster records;
4. assign each item to one display section;
5. apply report limits;
6. render the header;
7. render domain sections;
8. render warnings;
9. write the Markdown file.

## Report Limits

Initial configurable defaults should be:

- maximum 5 items per domain;
- maximum 30 items in the full report.

These are starting values and should be evaluated during real use.

## Domain Placement

Each record should appear once in the main report under its primary domain.

Secondary domains may be shown as tags.

This avoids excessive repetition.

## Story Entry

A story entry should contain:

- title;
- source;
- publication time;
- short feed-provided description when available;
- direct link;
- secondary-domain tags where useful;
- related-source count when greater than one.

Displaying raw relevance scores should remain optional.

Scores are useful for debugging but may reduce report readability.

## Description Length

Descriptions should be truncated to a configurable maximum.

Recommended initial value:

- approximately 300 characters.

The report must not fabricate summaries.

---

# 14. Automation Layer

## Responsibility

Run the complete pipeline automatically through GitHub Actions.

## Workflow Triggers

The production workflow should support:

- scheduled daily execution;
- manual execution through `workflow_dispatch`.

## Schedule

The exact time remains a product decision.

The workflow schedule should be defined in UTC because GitHub Actions cron uses UTC.

A morning report for Europe/Rome should account for daylight-saving changes.

Because GitHub cron cannot automatically follow local daylight-saving time, the initial schedule should prioritise practical consistency rather than exact local-time precision.

## Workflow Stages

The GitHub Actions workflow should:

1. check out the repository;
2. set up the supported Python version;
3. install dependencies;
4. run configuration validation;
5. run the pipeline;
6. run critical validation;
7. inspect whether output changed;
8. commit generated outputs when valid;
9. push the commit;
10. expose workflow status and logs.

## Explicit Timeout

The workflow should define a timeout.

Recommended initial maximum:

- 10 minutes.

The pipeline should normally run substantially faster.

## Concurrency

The workflow should prevent overlapping daily runs.

Use a GitHub Actions concurrency group so that a second run does not create conflicting output.

## Permissions

Use the minimum required workflow permissions.

The workflow will likely require repository content write permission if it commits generated outputs.

It should not receive unrelated permissions.

---

# 15. Automated Commit Strategy

## Responsibility

Preserve generated outputs without daily user intervention.

## Commit Contents

An automated run may update:

- the daily processed-record file;
- the daily report;
- the run-summary file.

## Commit Message

Recommended pattern:

    chore(data): generate intelligence report for YYYY-MM-DD

## No-Change Runs

If no repository output changes, the workflow should not create an empty commit.

## Commit Identity

The automated workflow should use a clearly identifiable bot-style Git identity.

## Risk

Scheduled commits can create repository noise.

This is acceptable for a daily archive but should remain limited to one coherent automated commit per run.

---

# 16. Logging and Observability

## Responsibility

Make system behaviour understandable without requiring advanced monitoring infrastructure.

## Logging Levels

Use standard levels:

- `DEBUG` for local troubleshooting;
- `INFO` for normal pipeline progress;
- `WARNING` for degraded but recoverable conditions;
- `ERROR` for source or record failures;
- `CRITICAL` for failures that prevent valid output.

## Required Log Events

Log:

- configuration loaded;
- number of active sources;
- source collection results;
- number of raw items;
- number of invalid items;
- duplicate reduction results;
- classification counts;
- unclassified count;
- report item count;
- output paths;
- workflow completion status.

## Structured Run Summary

The run-summary JSON file is the main persistent observability artifact.

GitHub Actions logs provide technical detail.

The report provides user-visible warnings.

## Failure Visibility

A degraded run should produce:

- a valid report when core processing succeeds;
- a visible warning;
- failed-source details in the run summary.

A critical failure should:

- fail the workflow;
- avoid committing a falsely successful report;
- preserve logs for investigation.

---

# 17. Error-Handling Model

## Recoverable Errors

Examples:

- one source unavailable;
- one malformed entry;
- missing optional metadata;
- no new items from a valid source;
- a record failing classification.

The pipeline should continue and record the issue.

## Critical Errors

Examples:

- invalid global configuration;
- processed storage cannot be written;
- report cannot be generated;
- output validation fails;
- repository persistence logic is unsafe;
- all sources fail and no valid report can be produced.

The workflow should fail.

## Degraded Success

The architecture should support a run status such as:

- `success`;
- `degraded`;
- `failed`.

### Success

Core pipeline completed and no material failures occurred.

### Degraded

Core pipeline completed, but one or more sources or records failed.

### Failed

A critical stage failed or no trustworthy report could be produced.

---

# 18. Output Validation

Before outputs are committed, the system should verify:

- report file exists;
- report date matches the run;
- required report header fields exist;
- at least one valid item exists, unless the run legitimately found none;
- all displayed items contain usable links;
- no duplicate primary records appear;
- processed JSON Lines parse correctly;
- run-summary JSON is valid;
- no restricted raw article bodies are present.

A legitimate no-news report should still be distinguishable from a failed run.

---

# 19. Testing Architecture

The initial repository should eventually include:

    tests/
    ├── fixtures/
    ├── test_config.py
    ├── test_normalize.py
    ├── test_validate.py
    ├── test_deduplicate.py
    ├── test_classify.py
    ├── test_rank.py
    ├── test_storage.py
    └── test_report.py

## Unit Tests

Test deterministic logic independently.

## Integration Test

Use a controlled set of local feed fixtures to test the complete pipeline without relying on live external sources.

## Live Source Smoke Test

A limited optional test may verify that a small number of active feeds remain reachable.

Live tests should not make unit tests dependent on internet availability.

## Workflow Validation

The GitHub Actions workflow should initially be tested through manual execution before enabling the daily schedule.

---

# 20. Proposed Repository Structure After MVP Setup

The expected structure is:

    daily-intelligence-system/
    ├── .github/
    │   └── workflows/
    │       └── daily-intelligence.yml
    │
    ├── config/
    │   ├── sources.yaml
    │   ├── domains.yaml
    │   ├── entities.yaml
    │   └── settings.yaml
    │
    ├── data/
    │   ├── processed/
    │   └── runs/
    │
    ├── docs/
    │   └── project/
    │       ├── 00 Project Brief.md
    │       ├── 01 Product Requirements.md
    │       ├── 02 System Architecture.md
    │       ├── 03 Information Taxonomy and Source Policy.md
    │       └── 04 Development Roadmap and Status.md
    │
    ├── reports/
    │   └── daily/
    │
    ├── src/
    │   └── daily_intelligence/
    │       ├── __init__.py
    │       ├── cli.py
    │       ├── config.py
    │       ├── collect.py
    │       ├── normalize.py
    │       ├── validate.py
    │       ├── deduplicate.py
    │       ├── classify.py
    │       ├── rank.py
    │       ├── storage.py
    │       ├── report.py
    │       ├── models.py
    │       └── logging_config.py
    │
    ├── tests/
    │   └── fixtures/
    │
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── pyproject.toml
    └── requirements.txt

This is the expected direction, not a requirement to create every file immediately.

Files should be introduced only when their corresponding functionality is implemented.

## Packaging Decision

Use a `src/` package layout.

Reasons:

- avoids accidental imports from the repository root;
- keeps code responsibilities clear;
- supports testing cleanly;
- remains appropriate if the project grows;
- adds little practical complexity.

---

# 21. Python and Dependency Strategy

## Python Version

Use a currently supported stable Python version available in GitHub Actions.

The exact version should be verified against current GitHub-hosted runner support before implementation.

## Initial Dependencies

The likely MVP dependencies are:

- `feedparser` for RSS and Atom parsing;
- `PyYAML` for configuration;
- `python-dateutil` for timestamp parsing;
- `pytest` for testing.

A lightweight title-similarity dependency may be considered later if standard-library logic is insufficient.

## Standard Library

Prefer standard-library tools for:

- URL parsing;
- hashing;
- JSON;
- logging;
- dataclasses;
- datetime handling where adequate;
- file operations.

## Dependency Management

Use `pyproject.toml` as the main project and dependency definition.

A separate `requirements.txt` may be generated or retained only if it materially simplifies GitHub Actions or user setup.

Avoid maintaining duplicated dependency declarations manually.

---

# 22. Data Model

The internal article record should be represented as a typed Python model.

A dataclass is sufficient for the MVP.

The model should support:

- serialisation to JSON;
- optional fields;
- lists of domains and geographies;
- score-component storage;
- processing status.

A complex validation framework is not required initially unless configuration and record complexity justify it.

---

# 23. Command-Line Interface

The MVP should expose one main command for the complete pipeline.

Conceptual usage:

    python -m daily_intelligence.cli run

Possible later commands:

    validate-config
    collect
    generate-report
    check-sources

The first implementation should avoid building an elaborate CLI.

A single end-to-end command plus configuration validation is sufficient.

---

# 24. Security and Privacy Architecture

## Secrets

The MVP should avoid secrets entirely where possible.

If a future public API requires a key:

- store it in GitHub Secrets;
- never print it;
- never commit it;
- make that source optional.

## Public Outputs

Only permitted public metadata should be committed.

## Private Context

The following remain outside the repository:

- Career OS source files;
- personal emails;
- private newsletters;
- private account details;
- proprietary information;
- authentication cookies.

## Dependency Security

Dependencies should remain minimal and should be periodically reviewed.

Automated dependency tooling may be considered later, but it is not required before the MVP works.

---

# 25. Copyright Architecture

The system should not fetch or store full article bodies during the MVP.

The architecture should operate on:

- feed titles;
- links;
- authors;
- timestamps;
- short descriptions;
- categories;
- system-generated metadata.

Descriptions should be truncated for presentation.

When source permissions are uncertain, the system should store less content.

---

# 26. ChatGPT Boundary

The GitHub pipeline and ChatGPT scheduled briefing remain independent.

The architecture does not include:

- automated GitHub-to-ChatGPT transfer;
- ChatGPT API calls;
- automatic report upload;
- plugin or connector access;
- AI-generated repository summaries.

This avoids:

- paid API usage;
- connector dependency;
- daily manual copying;
- fragile authentication;
- privacy uncertainty.

---

# 27. Architectural Decisions

The following decisions are established for the MVP.

| Area | Decision |
|---|---|
| Runtime | Python |
| Automation | GitHub Actions |
| Initial sources | RSS and Atom |
| Configuration | YAML |
| Internal timezone | UTC |
| Processed storage | JSON Lines |
| Run summaries | JSON |
| Reports | Markdown |
| Production AI calls | None |
| Full article storage | Not allowed |
| Database | Not required initially |
| Report placement | One primary domain per item |
| Secondary domains | Stored and optionally shown as tags |
| Daily persistence | Automated repository commit |
| Delivery interface | GitHub repository report |
| GitHub issues | Deferred |
| GitHub Pages | Deferred |
| Newsletter ingestion | Deferred |
| Private sources | Excluded from MVP |

These decisions may be revised only when evidence shows a meaningful limitation.

---

# 28. Open Architectural Decisions

The following remain unresolved:

- exact Python version;
- exact GitHub Actions execution time;
- exact title-similarity method;
- exact near-duplicate threshold;
- exact source and domain configuration schemas;
- exact score weights;
- whether relevance scores appear in the public report;
- how missing-timestamp records are displayed;
- whether JSON Lines files are daily or monthly after scale increases;
- whether source-health history requires a separate file;
- whether a dependency-lock file is needed;
- whether `requirements.txt` is necessary alongside `pyproject.toml`;
- exact format of automated report commits;
- exact no-news report behaviour.

These should be resolved during implementation or sample evaluation rather than guessed prematurely.

---

# 29. Architecture Validation Plan

Before enabling scheduled production, validate the architecture through four stages.

## Stage 1 — Configuration Validation

Confirm that:

- valid configuration loads;
- missing required fields fail clearly;
- inactive sources are skipped;
- domains and settings are internally consistent.

## Stage 2 — Local Vertical Slice

Using local fixtures:

- parse feed entries;
- normalise records;
- validate required fields;
- remove exact duplicates;
- classify domains;
- assign provisional scores;
- write JSON Lines;
- generate Markdown.

## Stage 3 — Live Manual Run

Using a small source universe:

- run the pipeline locally;
- inspect source failures;
- inspect processed records;
- inspect classifications;
- inspect duplicates;
- inspect report length and readability.

## Stage 4 — GitHub Actions Manual Run

Before scheduling:

- trigger the workflow manually;
- confirm dependencies install;
- confirm outputs generate;
- confirm permissions;
- confirm automated commit;
- confirm failure behaviour.

Only after these stages should the daily schedule be enabled.

---

# 30. Current Status

**Status:** Initial architecture defined

**Architecture decisions completed:**

- repository-native Python workflow;
- RSS and Atom as initial source types;
- YAML configuration;
- UTC internal timestamps;
- deterministic processing;
- JSON Lines storage;
- Markdown reports;
- automated GitHub Actions execution;
- automated repository persistence;
- public-safe metadata only;
- no production AI calls.

**Still required before implementation:**

- initial source universe;
- final configuration schemas;
- provisional ranking formula;
- initial test fixtures;
- exact report template;
- implementation roadmap.

**Next document:**

- 