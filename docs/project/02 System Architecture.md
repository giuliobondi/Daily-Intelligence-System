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
- replacement of weak sources before disproportionate source-specific complexity;
- configuration-first source and domain changes where the existing pipeline already supports them;
- conservative classification over forced coverage.

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

The core system is implemented as a repository-native deterministic production pipeline.

The current architecture supports:

- repository-native configuration loading;
- seven active real public RSS sources;
- eight active topic domains;
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

Phase 3 automation architecture is complete.

Phase 4 has now demonstrated that the existing architecture can support meaningful source and taxonomy changes through configuration alone.

The first validated Phase 4 architectural checkpoint replaced:

```text
Sifted
→ Tech.eu
```

and expanded the taxonomy:

```text
7 active domains
→ 8 active domains
```

by adding Financial Markets.

No application module required modification for those changes.

The current architectural priority remains:

> **continue improving the information layer through controlled source/domain changes, then design richer report context without weakening the zero-cost, deterministic and public-safe architecture.**

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

Production wraps this application flow with:

```text
GitHub trigger
→ checkout
→ Python setup
→ dependency installation
→ automated tests
→ production CLI
→ output validation
→ Git staging
→ no-change guard
→ bot commit
→ push
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

Configuration remains separate from business logic so changing:

- sources;
- source defaults;
- domain keywords;
- active domains;
- score weights;
- report limits;

does not require modifying core processing code.

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

This is intentional architecture.

A broad source should not receive a default merely because the publisher is associated with a topic.

The Tech.eu replacement validated this architecture directly.

### Domain Validation Behaviour

Domain configuration currently requires:

- unique domain identifier;
- non-empty name;
- keyword list;
- boolean activation state.

The addition of Financial Markets required only configuration and corresponding test updates.

No processing-module change was necessary.

This validates the intended architecture:

> taxonomy expansion should normally be configuration-first.

---

## 5.3 `collect.py`

Owns source retrieval and feed parsing.

Remote flow:

```text
feed URL
→ urllib Request
→ explicit User-Agent
→ explicit Accept header
→ 10-second timeout
→ standard TLS verification
→ redirects
→ feedparser
→ structured collection result
```

Each source produces a structured result such as:

```text
success
empty
failed
```

Expected source-level network failures are isolated.

Current implementation does not include:

- retry logic;
- rate-limit scheduling;
- browser automation;
- authenticated retrieval;
- source-specific premium-content handling.

Add those only if real evidence justifies them.

### Source-Replacement Validation

Tech.eu was tested through the actual collector before configuration change.

Observed:

```text
status: success
20 items received
```

Sifted was also technically collectible.

Therefore its replacement was not an HTTP compatibility decision.

It was an information-quality decision.

---

## 5.4 `normalize.py`

Owns transformation from feedparser entries into canonical article records.

Normalisation preserves:

- source identity;
- title;
- article URL;
- publication time;
- description where available;
- retrieval time.

URLs and titles are normalised for later identity/deduplication.

Publication timestamps are timezone-aware.

### Metadata Evidence from Phase 4

The Tech.eu vs Sifted comparison showed:

```text
Tech.eu:
20/20 tested records had descriptions

Sifted:
0/24 tested records had descriptions
```

Both normalised successfully.

This demonstrates that:

> normalisation validity and product metadata quality are separate architectural concerns.

The model can accept a missing description, while source policy may still reject the source because that omission materially harms the report.

---

## 5.5 `validate.py`

Owns structural record validation.

Validation checks that downstream processing receives records with required fields.

Invalid records remain distinguishable from valid records.

Current architecture does not treat missing optional description as structural invalidity.

That remains correct.

Source-quality policy decides whether repeated missing descriptions make a source unsuitable.

---

## 5.6 `filter_window.py`

Owns publication-time eligibility.

Current collection window:

```text
actual run timestamp - 24 hours
through
actual run timestamp
```

Eligibility is based on:

```text
published_at
```

not retrieval time.

Records without publication timestamps are excluded from window eligibility.

Both boundaries remain inclusive.

The window uses timezone-aware datetimes.

---

## 5.7 `deduplicate.py`

Owns exact duplicate reduction.

Current deterministic evidence:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

Near-duplicate or same-story clustering remains deferred.

Do not add fuzzy matching unless repeated production evidence demonstrates material report duplication.

---

## 5.8 `classify.py`

Owns deterministic topic classification.

Current classification evidence:

```text
source defaults
+
configured keyword matches against title and description
```

An article may belong to multiple domains.

An article may remain unclassified.

That is an intentional state.

### Source Defaults

Source defaults are applied only when the selected source/feed provides genuine source-wide topical evidence.

Current production defaults:

```text
BBC News World                → none
BBC News Business             → none
European Central Bank         → none
European Commission           → none
Istat Press Releases          → Economics and Macroeconomics
OpenAI News                   → Artificial Intelligence
Tech.eu                       → none
```

Tech.eu was explicitly tested with a Startups/VC default.

That produced misleading assignments to:

- corporate M&A;
- AI stories;
- European industrial-policy stories;
- broader fintech/business stories.

The final architecture therefore uses:

```yaml
default_domains: []
```

for Tech.eu.

### Classification Precision Rule

Prefer:

```text
unclassified
```

over:

```text
weak or misleading domain assignment
```

A high unclassified count is not automatically an architecture defect.

A 17 August 2026 run produced:

```text
30 unique records
26 unclassified
4 displayed
```

Manual inspection showed that most of the 26 excluded records were correctly outside the intended report scope.

Therefore the correct validation question is:

> Which high-value stories are being missed?

not:

> What percentage of all records are classified?

### Keyword Architecture

Keyword matching remains deliberately simple and inspectable.

Current Phase 4 evidence-backed changes include:

```text
Global Politics and Geopolitics
+ tariffs

Companies and Corporate Strategy
+ acquired

Startups and Venture Capital
+ early-stage fund
+ funding market
- startup
```

The removal of generic `startup` is architecturally important.

It demonstrated that a broad lexical signal can create:

```text
weak semantic evidence
→ domain assignment
→ additional domain score
→ additional keyword score
→ low-value report promotion
```

The architecture therefore requires candidate keyword testing against real records before configuration changes.

### Keyword Variant Limitation

Testing acquisition variants also showed that closely related terms can independently match one record.

Because the current score adds one point per matched keyword, naive synonym expansion can inflate relevance.

Do not introduce stemming, NLP or a more complex matcher yet.

The current response should be:

```text
select candidate terms conservatively
→ simulate
→ inspect
```

---

## 5.9 `rank.py`

Owns deterministic relevance scoring.

Current formula:

```text
relevance score
=
source-tier score
+ domain-match score
+ keyword-match score
```

Current source-tier values:

```text
Tier 1 → 4
Tier 2 → 3
Tier 3 → 2
Tier 4 → 1
```

Current additional weights:

```text
2 points per assigned domain
1 point per matched keyword
```

Score components remain stored for transparency.

The formula remains provisional.

### Architectural Rule

If weak evidence inflates score:

> **fix source defaults or classification evidence before redesigning ranking.**

Phase 4 reinforced this rule through:

- Tech.eu source-default testing;
- removal of generic `startup`;
- conservative Financial Markets terms.

No change to ranking weights was needed.

---

## 5.10 `storage.py`

Owns processed-record persistence.

Processed records are written as JSON Lines.

Current path pattern:

```text
data/processed/YYYY/MM/YYYY-MM-DD.jsonl
```

The write model replaces the dated target deterministically during a run rather than continually appending.

This supports:

- predictable reruns;
- simple history;
- bounded duplicate behaviour;
- regression testing against stored production records.

Stored records were directly useful during Phase 4.

Three historical JSONL files provided a:

```text
114-record regression corpus
```

for taxonomy validation.

This confirms the value of repository-native processed-record history as a testing asset.

No database is currently justified.

---

## 5.11 `report.py`

Owns deterministic report selection and Markdown rendering.

Current report behaviour includes:

- one primary section per story;
- secondary domains shown as metadata;
- source attribution;
- publication timestamp;
- relevance score;
- direct article link;
- feed-provided description where available;
- bounded item counts.

Current limits:

```text
maximum 5 items per domain
maximum 30 items overall
maximum description length 300 characters
```

These limits are configuration, not architecture constants.

### Current Limitation

The report still acts partly as an intelligence index.

It may provide too little context to understand some developments without opening the source.

Production use has validated the requirement:

> provide enough lawful context for initial understanding while preserving the source for deeper reading.

The architectural method is not yet selected.

Do not implement richer summarisation before the dedicated design phase establishes:

- required context depth;
- lawful source material;
- metadata availability;
- fallback behaviour;
- report-length constraints;
- treatment of premium-exception sources;
- validation method.

### Architecture Preference for Richer Context

Evaluate mechanisms in this order:

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
→ smallest justified boundary change
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

GitHub Actions invokes the same CLI.

### Local Installation Note

Because the package uses a `src/` layout, source-based pytest execution can reflect newer repository code while:

```text
python -m daily_intelligence.cli
```

may execute a stale installed package.

When CLI behaviour appears inconsistent with source changes:

```text
verify installation state first
```

before diagnosing an application bug.

This remains a development-environment concern, not a production dependency.

---

# 6. Configuration Architecture

Configuration is repository-native and human-readable.

The goal is to separate changing information policy from stable processing code.

Phase 4A validated this design strongly:

```text
source replacement
+
keyword correction
+
new domain
```

required changes only to:

```text
config/sources.yaml
config/domains.yaml
```

plus configuration tests.

No core processing module required modification.

---

## 6.1 `sources.yaml`

Current fields include:

- `id`;
- `name`;
- `feed_url`;
- `source_type`;
- `source_tier`;
- `default_domains`;
- `language`;
- `geographic_scope`;
- `active`.

Current active registry:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News;
- Istat Press Releases;
- OpenAI News;
- Tech.eu.

The file remains the runtime source of truth for active production feeds.

### Sifted Architectural Decision

Sifted was removed from current production.

The replacement decision was based on:

```text
same basic collection compatibility
+
substantially better Tech.eu metadata richness
+
better follow-up usability
```

Do not retain a technically compatible weak source merely because existing architecture can parse it.

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

These remain policy/audit dimensions for now.

They should become runtime fields only if application behaviour genuinely requires them.

---

## 6.2 `domains.yaml`

Current fields include:

- `id`;
- `name`;
- `keywords`;
- `active`.

Current active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union;
- Financial Markets.

Financial Markets is now implemented.

Target domains still not implemented:

- Italy;
- Milan and Bocconi Ecosystem.

### Italy

Strategically approved.

Implementation should remain configuration-first if suitable source evidence and keywords can support it.

### Milan/Bocconi

This is now a validated product requirement rather than merely a candidate.

However, its likely inputs may include:

- events;
- programmes;
- deadlines;
- opportunities;
- ecosystem news.

The current `ArticleRecord` and pipeline should be reused if possible.

Do not create a separate opportunity architecture until real source metadata demonstrates that the existing model is insufficient.

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

These remain configurable defaults.

No setting was changed during Phase 4A.

That is intentional.

The source and taxonomy problems were solved upstream instead of changing ranking/report settings.

---

# 7. Data Model and Record Lifecycle

A feed entry passes through:

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

- structurally valid record outside the reporting window;
- unique record with no domain;
- classified record not selected because of limits;
- source with technically valid records but insufficient metadata quality.

This separation improves:

- testability;
- counter interpretation;
- failure isolation;
- source evaluation;
- future extension.

---

# 8. Collection-Window Architecture

Current CLI behaviour:

```text
actual run timestamp - 24 hours
through
actual run timestamp
```

Both boundaries are inclusive.

Eligibility uses `published_at`.

## Observed Production Limitation

GitHub Actions scheduled runs may start materially later than the configured cron trigger.

Because the reporting cutoff uses actual execution time:

```text
configured trigger
→ delayed run start
→ shifted cutoff
→ shifted eligible story set
```

## Current Decision

Do not change the reporting window yet.

Potential future architecture:

```text
fixed reporting cutoff
→ deterministic information window
→ GitHub delay affects delivery time only
```

Implement only if repeated evidence demonstrates material product harm.

---

# 9. Deduplication Architecture

Current exact reduction:

```text
normalised URL
→ fallback normalised title
```

No near-duplicate clustering exists.

No story-level clustering exists.

No vector similarity exists.

These remain deferred until repeated report evidence demonstrates a meaningful problem.

---

# 10. Classification Architecture

Classification remains:

```text
source defaults
+
title keyword matches
+
description keyword matches
```

Properties:

- deterministic;
- explainable;
- multi-domain;
- allows unclassified records;
- configurable;
- no ML dependency.

## Current Architectural Principle

Classification should optimize for:

```text
useful precision
```

rather than:

```text
maximum coverage
```

The 17 August report review validated that many unclassified records were intentionally low-value.

Do not add generic vocabulary merely to improve classification counts.

---

# 11. Ranking Architecture

Current formula:

```text
source-tier points
+
2 × assigned domains
+
1 × matched keywords
```

The ranking architecture remains unchanged after Phase 4A.

This is important evidence.

Observed report-quality defects were corrected through:

```text
source replacement
source defaults
keyword precision
domain coverage
```

not ranking sophistication.

Continue to prefer upstream corrections.

---

# 12. Report Architecture

The report remains deterministic Markdown.

Current flow:

```text
classified/scored records
→ deterministic ordering
→ domain limits
→ overall limit
→ one primary placement
→ secondary-domain metadata
→ Markdown rendering
```

Unclassified records remain stored but are not displayed.

### Sparse Reports

A sparse report is not automatically defective.

The relevant question is whether:

- major useful stories were missed;
- selected items are weak;
- source coverage is insufficient.

Do not introduce filler behaviour.

---

# 13. Storage Architecture

Current persistent artifacts:

```text
data/processed/YYYY/MM/YYYY-MM-DD.jsonl
data/runs/YYYY/MM/YYYY-MM-DD.json
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

Repository-native history remains sufficient.

Phase 4 demonstrated an additional architectural benefit:

> historical processed records can act as deterministic regression corpora for taxonomy changes.

No external database is justified.

---

# 14. Failure Architecture

Failure handling remains layered.

## Source-Level Recoverable Failure

One source may fail while others succeed.

Expected outcome:

```text
partial data
→ degraded run
→ report persists
→ failure visible
```

## Critical Failure

Examples:

- invalid configuration;
- core pipeline failure;
- invalid required output.

Expected outcome:

```text
pipeline/workflow fails
→ misleading output not published
```

Both behaviours have been validated.

---

# 15. Logging and Observability

Run-level logging remains standard-library based.

Current logs expose:

- run start;
- active source count;
- per-source collected item count;
- validation totals;
- window totals;
- deduplication totals;
- classification/unclassified totals;
- output paths;
- final run status.

The 17 August Phase 4A validation used these logs to confirm:

```text
7 active
7 successful
1281 valid
32 window-eligible
30 unique
26 unclassified
success
```

Operational metrics should support diagnosis, not become optimization targets automatically.

---

# 16. Test Architecture

The automated suite currently contains:

> **110 tests**

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

Automated tests remain independent of live internet access.

Fixtures and temporary configuration remain the default deterministic test layer.

Real-source validation is separate.

## Phase 4A Validation Pattern

Phase 4A added a useful development pattern:

```text
live source probe
→ classification simulation
→ candidate keyword simulation
→ stored-corpus regression
→ configuration edit
→ targeted tests
→ full suite
→ real pipeline run
→ manual report inspection
```

This pattern should be reused for material source/taxonomy changes.

---

# 17. Production Automation Architecture

GitHub Actions remains the production execution environment.

High-level workflow:

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

## Scheduled Trigger

Current configured schedule:

```text
06:05 Europe/Rome
```

This remains a desired trigger time, not guaranteed execution time.

## Runtime

```text
ubuntu-latest
Python 3.12
```

## Permissions

Required:

```text
contents: write
```

No broader production permission is currently needed.

## Secrets

No source credentials or repository secrets are required.

## Production AI

No:

- OpenAI API;
- Copilot;
- GitHub AI;
- third-party paid AI.

---

# 18. Concurrency Architecture

Production uses one concurrency group.

Policy:

```text
one Daily Intelligence production run at a time
```

with:

```text
cancel-in-progress: false
```

This prevents simultaneous jobs from racing on:

- date-based output paths;
- Git commits;
- Git pushes.

---

# 19. Scheduler Architecture

GitHub scheduler latency is an external platform limitation.

Observed delays can be substantial.

Current mitigation:

```text
schedule earlier than desired reading time
```

No additional infrastructure is justified.

The unresolved architectural issue is only whether content selection should use a fixed cutoff independent of execution time.

---

# 20. Network Architecture

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

Current characteristics:

- seven active public RSS sources;
- one request per source per run remains lightweight;
- no source authentication;
- no source-specific rate-limit architecture;
- no retry architecture.

Tech.eu required no custom collector logic.

That supports the current architectural preference:

> choose sources compatible with the simple collector where possible.

---

# 21. Source Access Architecture

Production separates:

```text
automation access
```

from:

```text
reader access
```

This distinction remains fundamental.

---

## Automated Public Source Layer

Production may ingest through:

- public RSS;
- public Atom;
- official free APIs;
- public structured metadata;
- other explicitly permitted automation endpoints.

No authenticated publisher access belongs here.

---

## Bocconi Premium Reading Layer

The user may have legitimate access to publications including:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore;
- Foreign Affairs;
- Harvard Business Review.

This can improve manual follow-up.

It does not automatically expand ingestion rights.

---

## Research / Database Layer

Examples:

- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- S&P Capital IQ Pro;
- Aida.

These remain manual research systems unless an explicitly permitted structured automation interface exists.

---

# 22. Premium Bocconi Exception Architecture

A narrow product exception has now been defined.

Some premium publications may deserve production discovery even when their public metadata cannot support the same context depth as fully public sources.

This is allowed only if:

```text
exceptional information value
+
legitimate Bocconi reader access
+
public/automation-compatible discovery endpoint
+
no automated premium-body retrieval
```

This changes the acceptable report experience, not the authentication architecture.

Production still must not:

- automate OpenAthens;
- log into publishers;
- store personal publisher credentials;
- fetch premium article bodies;
- bypass paywalls.

Potential premium-exception source:

```text
public feed metadata
→ deterministic classification/ranking
→ thinner report entry
→ user opens article manually through Bocconi
```

Current highest-priority technical candidate:

```text
Financial Times
```

followed by:

```text
Il Sole 24 Ore
```

No premium source is currently active under this exception.

---

# 23. Security and Privacy Architecture

The repository is public.

Never commit:

- credentials;
- Bocconi credentials;
- Career OS private content;
- private emails;
- newsletter contents;
- authentication cookies;
- access tokens;
- licensed database text;
- restricted copyrighted content.

Current production requires no source credential.

That remains preferable.

Even if GitHub Secrets could technically store institutional credentials, architecture policy prohibits using that mechanism to automate premium publisher access merely because the user has legitimate reading rights.

---

# 24. Copyright and Content Boundaries

The repository may store, where permitted:

- titles;
- source names;
- links;
- timestamps;
- short feed descriptions;
- public structured summaries;
- derived domains;
- matched keywords;
- relevance scores;
- operational metadata.

The system must not store:

- complete copyrighted articles;
- paywall-bypassed content;
- authenticated premium article bodies;
- substantial unauthorised excerpts;
- licensed database full text.

## Richer-Report Boundary

The richer-context requirement does not override copyright rules.

Objective:

> enough lawful context for initial understanding.

Not:

> reproduction of the source article.

---

# 25. Architecture for ChatGPT Use

ChatGPT remains outside the production dependency chain.

Production must remain useful without any ChatGPT API call.

ChatGPT may be used manually for:

- development reasoning;
- code review;
- project-document drafting;
- source/domain strategy;
- source-audit interpretation;
- product-quality review;
- deciding whether observed limitations justify implementation changes.

The separation remains:

```text
Daily Intelligence System
= deterministic production infrastructure

ChatGPT
= external development and reasoning layer
```

The richer-report requirement does not automatically change this boundary.

---

# 26. Implemented vs Active vs Deferred Architecture

## Implemented and Validated

- Python package;
- repository-native configuration;
- seven-source public RSS registry;
- eight-domain active taxonomy;
- RSS/Atom collection;
- local fixture collection;
- remote HTTP/HTTPS retrieval;
- explicit request headers;
- 10-second timeout;
- normal TLS verification;
- redirect handling;
- structured source outcomes;
- source-level failure isolation;
- normalisation;
- deterministic URL cleaning;
- UTC-aware timestamps;
- deterministic SHA-256 record IDs;
- structural validation;
- previous-24-hours publication filtering;
- exact deduplication;
- deterministic classification;
- empty source defaults;
- deterministic ranking;
- JSONL persistence;
- Markdown reporting;
- JSON run summaries;
- pipeline orchestration;
- CLI;
- logging;
- automated tests;
- real-source validation;
- GitHub Actions;
- manual workflow dispatch;
- scheduled execution;
- automated output validation;
- automated bot persistence;
- no-change guard;
- degraded automated publication;
- critical-failure protection;
- concurrency protection;
- repository-native production history;
- Tech.eu replacing Sifted;
- Financial Markets domain;
- conservative keyword regression workflow.

## Active Architectural Evaluation

- further source correction/expansion;
- Financial Times automation/interface suitability;
- Il Sole 24 Ore automation/interface suitability;
- Bank of Italy source role;
- Reuters feasibility;
- Italy domain implementation;
- Milan/Bocconi source architecture;
- source metadata richness;
- Premium Bocconi Exception application;
- richer-report architecture;
- reporting-window cutoff independence.

## Deferred Until Evidence

- retry logic;
- near-duplicate clustering;
- story clustering;
- entity extraction;
- article-level geography;
- content-type classification;
- separate opportunity record model;
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
- stronger finance/business reporting remains under evaluation;
- Italy is not yet an explicit domain;
- Milan/Bocconi is not yet implemented;
- independent AI reporting remains limited;
- all current active automated feeds are English-language;
- full bilingual classification is unvalidated;
- exact deduplication does not detect differently worded coverage of the same story;
- records without publication timestamps are excluded;
- ranking remains provisional;
- classification remains conservative;
- strategically useful records can still remain unclassified;
- no entity enrichment exists;
- no article-level geography exists;
- no content-type classification exists;
- no long-term source-health history exists;
- current description depth may still be insufficient for richer-report requirements;
- Premium Bocconi Exception rendering is not implemented;
- report composition can be sparse;
- scheduler timing is not precise;
- collection window remains tied to actual execution time;
- there is no dedicated latest-report alias;
- GitHub Markdown remains the primary delivery interface.

These limitations are not an automatic feature backlog.

Each requires evidence.

---

# 28. Architecture Decision Rules

Before adding any architectural component, ask:

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

Preferred pattern:

```text
observe
→ reproduce
→ isolate
→ smallest justified change
→ test
→ inspect output
→ stop
```

For source/taxonomy work, extend this to:

```text
strategic need
→ source probe
→ metadata/access review
→ classifier simulation
→ regression corpus
→ smallest config change
→ tests
→ real pipeline
→ report inspection
```

---

# 29. Current Open Architecture Decisions

## Source Universe

The current seven-source registry is intentionally not considered final.

Next technical audit:

```text
Financial Times
```

Then, if still justified:

```text
Il Sole 24 Ore
Bank of Italy
Reuters
```

Do not add all strategically attractive sources simultaneously.

---

## BBC Business

Current architecture can support removing it through configuration if stronger coverage validates.

Do not remove it before replacement evidence exists.

---

## Italy

Strategically approved.

Architectural question:

> Can Italy be added through current `domains.yaml` plus a small validated source set?

Preferred source candidates:

```text
Il Sole 24 Ore
Istat
Bank of Italy
```

Do not create Italy-specific processing logic unless necessary.

---

## Milan/Bocconi

Now a fixed product requirement.

Architectural question:

> Can public Bocconi/B4i/career sources fit the existing article pipeline cleanly?

Investigate first:

```text
B4i
Bocconi Career Services
Bocconi News & Events
```

Prefer reusing:

```text
ArticleRecord
collector
classifier
reporter
```

before introducing:

- new record models;
- event databases;
- deadline engines.

---

## Richer Report Context

Open question:

> What is the smallest deterministic and compliant mechanism that provides enough context for initial understanding?

Candidate input order:

1. richer feed fields;
2. public structured metadata;
3. official free APIs;
4. narrowly justified permitted public extraction;
5. more complex mechanisms only if simpler ones fail.

Premium-exception sources may deliberately have thinner automated context.

No production AI summarisation architecture has been selected.

---

## Reporting Window

Current:

```text
actual run time - 24 hours
→ actual run time
```

Candidate:

```text
fixed cutoff
→ deterministic 24-hour report window
```

More production evidence is required.

---

## Output Validation for No-News Runs

A legitimate no-news case may eventually expose whether output non-empty validation is too strict.

Do not change theory-first.

Reproduce first.

---

## Sponsored Content

Tech.eu testing exposed explicit sponsored content.

No architecture change is justified from one observation.

If sponsored material begins to enter reports materially:

```text
observe repeatedly
→ define deterministic handling
→ test
```

---

## Near-Duplicate Handling

Deferred.

---

## Long-Term Source Health

Per-run summaries remain sufficient.

---

## Delivery Interface

GitHub Markdown remains sufficient until reading friction becomes a demonstrated product constraint.

---

# 30. Architecture Validation Gates

## Gate A — Local Architecture

**Status: passed**

Evidence:

- local orchestration;
- deterministic processing;
- automated tests;
- inspectable output;
- visible failures;
- operational CLI.

---

## Gate B — Real-Source Architecture

**Status: passed**

Evidence:

- real public feeds;
- bounded HTTP;
- explicit headers;
- redirects;
- usable timestamps;
- successful parsing;
- real report generation;
- real degraded-source validation;
- 110 tests.

---

## Gate C — Automation Architecture

**Status: passed**

Evidence:

- manual workflow dispatch;
- full tests in Actions;
- production CLI in Actions;
- output validation;
- bot persistence;
- no-change guard;
- critical failure handling;
- degraded publication.

---

## Gate D — Scheduled Production Architecture

**Status: passed**

Evidence:

- scheduled execution observed;
- production outputs persisted;
- concurrency protection;
- 06:05 Europe/Rome trigger configuration.

Known limitation:

- trigger punctuality not guaranteed.

---

## Gate E — Source/Domain Expansion Architecture

**Status: partially passed; active**

The first controlled Phase 4 checkpoint passed.

Evidence:

- Sifted problem reproduced;
- Tech.eu alternative researched;
- real collector probe completed;
- normalisation validated;
- metadata compared;
- source default tested;
- classification simulation completed;
- stored-corpus regression completed;
- source replacement completed;
- new Financial Markets domain added;
- config tests updated;
- 110 tests passed;
- real 17 August run completed;
- report manually inspected.

This proves:

> the existing architecture can support substantial source/domain correction through configuration without new processing components.

Gate E remains open because:

- final source universe is not selected;
- Italy remains unimplemented;
- Milan/Bocconi remains unimplemented;
- premium-source architecture has not yet been exercised in production.

---

## Gate F — Richer Report Architecture

**Status: not passed**

Required before implementation:

- exact context requirement;
- source metadata audit;
- copyright/access boundary;
- Premium Bocconi fallback behaviour;
- output-length target;
- provenance design;
- candidate approach comparison;
- acceptance tests.

The user need is validated.

Implementation architecture is not.

---

## Gate G — Advanced Quality Architecture

**Status: not passed**

Possible future examples:

- near-duplicate clustering;
- entities;
- content type;
- article-level geography;
- advanced ranking.

Entry requires:

- repeated real problem;
- simpler corrections insufficient;
- explicit evaluation method.

---

# 31. Current Architecture Summary

The Daily Intelligence System is a production-operational, repository-native deterministic Python pipeline.

Core application flow:

```text
collect
→ normalize
→ validate
→ filter
→ deduplicate
→ classify
→ rank
→ store
→ report
→ run summary
```

Production flow:

```text
GitHub trigger
→ setup
→ test
→ run
→ validate
→ persist
```

Current information architecture:

```text
7 active public RSS sources
8 active domains
deterministic source defaults
deterministic keyword classification
deterministic ranking
repository-native historical data
```

Current active source set:

```text
BBC News World
BBC News Business
European Central Bank
European Commission Highlighted News
Istat Press Releases
OpenAI News
Tech.eu
```

Current active domains:

```text
Global Politics and Geopolitics
Economics and Macroeconomics
Companies and Corporate Strategy
Artificial Intelligence
Technology and Software
Startups and Venture Capital
Europe and the European Union
Financial Markets
```

Current architectural direction:

```text
finish source/domain correction
→ validate Italy
→ validate Milan/Bocconi
→ stop expansion when information universe is strong enough
→ design richer context
```

The architecture should remain simple unless actual report usage proves otherwise.

---

# Changelog

## 2026-08-17 — Phase 4A Source and Domain Architecture Validation

- Reconciled architecture with the first validated Phase 4 source/domain correction.
- Replaced Sifted with Tech.eu in the active seven-source registry.
- Recorded the controlled Tech.eu/Sifted comparison.
- Recorded 20/20 Tech.eu descriptions versus 0/24 Sifted descriptions in the tested samples.
- Recorded that source replacement was driven by product metadata/access quality rather than parser compatibility.
- Recorded Tech.eu as a broad Tier 2 source with no default domain.
- Added Financial Markets as the eighth implemented domain.
- Recorded that Financial Markets required configuration only and no processing-module changes.
- Added the evidence-backed classification changes `tariffs`, `acquired`, `early-stage fund` and `funding market`.
- Recorded removal of generic `startup`.
- Added the architectural warning that near-synonymous keywords may independently increase score.
- Added the 114-record regression pattern as a reusable source/taxonomy validation mechanism.
- Recorded the real 17 August 2026 pipeline validation.
- Recorded that 26/30 unclassified records did not represent a system failure after manual inspection.
- Established that classification percentage is not an architectural KPI.
- Added the narrow Premium Bocconi Exception while preserving the existing authentication prohibition.
- Upgraded Milan/Bocconi from candidate to validated product requirement.
- Recorded the preference to reuse the existing `ArticleRecord` pipeline for future Milan/Bocconi inputs before creating new event/opportunity architecture.
- Preserved ranking weights, report settings and core processing modules unchanged.
- Confirmed 110 automated tests remain passing.

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
- Recorded automated bot persistence.
- Recorded no-change commit protection.
- Recorded deliberate critical configuration failure validation.
- Recorded deliberate degraded source publication validation.
- Recorded concurrency protection.
- Recorded substantial GitHub scheduler latency.
- Recorded the scheduler-latency/report-window coupling as an open architecture decision.
- Added richer-report architecture as a validated later design problem.
- Added automated public / Bocconi premium reading / research-database separation.
- Explicitly prohibited authenticated premium-content ingestion.
- Added source/domain expansion as the next active architectural work.

## 2026-08-11 — Phase 2 Real-Source Architecture Validated

- Moved the minimal real-source registry into implemented architecture.
- Recorded seven validated public RSS sources.
- Expanded the implemented taxonomy from two to seven active domains.
- Added bounded HTTP retrieval with 10-second timeout.
- Added explicit User-Agent and Accept headers.
- Preserved standard SSL verification.
- Validated redirects and real-feed parsing.
- Added structured remote failure handling.
- Kept retry logic absent.
- Added support for empty source defaults.
- Recorded narrow-vs-broad source-default policy.
- Added evidence-based politics keyword refinement.
- Validated real publication timestamps.
- Validated partial-source degradation.
- Reached 110 passing tests.

## 2026-08-11 — Phase 1 Architecture Baseline

- Replaced the pre-implementation architecture with the validated local architecture.
- Added orchestration and CLI components.
- Added publication-window filtering.
- Recorded deterministic record identity.
- Recorded exact deduplication.
- Recorded classification and ranking.
- Recorded report selection.
- Recorded run-summary and logging.
- Distinguished implemented and deferred architecture.
- Defined real-source validation as the next gate.

## Initial System Architecture Baseline

- Defined the deterministic pipeline.
- Established Python and repository-native configuration.
- Defined source collection, normalisation, validation, deduplication, classification, ranking, storage and reporting responsibilities.
- Established zero recurring cost, public-source preference and no-production-AI constraints.