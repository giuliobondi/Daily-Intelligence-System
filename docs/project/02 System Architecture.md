# Daily Intelligence System — System Architecture

> **Purpose**
>
> This document defines the technical architecture of the Daily Intelligence System.
>
> It describes the implemented processing model, component boundaries, data flow, storage model, configuration model, failure behaviour, observability, automation architecture and the architectural constraints that govern future development.
>
> It is not the implementation-status tracker. Current phase, milestone and development sequencing belong in `04 Development Roadmap and Status.md`.
>
> Source suitability, licensing decisions and source-audit conclusions belong in `03 Information Taxonomy and Source Policy.md`.

---

> **Primary Question**
>
> *How is the Daily Intelligence System structured, how does information move through it, and which architectural decisions are fixed, implemented, planned or deferred?*

---

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
- conservative classification over forced coverage;
- reuse of the existing `ArticleRecord` pipeline before introducing new record models;
- source-specific complexity only when information value justifies it.

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
- authenticated Bocconi scraping;
- private newsletter ingestion;
- complex frontend applications;
- machine-learning components without a validated need;
- source-specific parsing logic when a standard structured endpoint already works;
- new processing paradigms introduced only to increase source count.

---

# 2. Architectural Status

The core system is implemented as a repository-native deterministic production pipeline.

The current architecture supports:

- repository-native configuration loading;
- twelve active real public RSS sources;
- ten active topic domains;
- RSS/Atom collection;
- bounded remote HTTP retrieval;
- explicit User-Agent and Accept headers;
- normal SSL verification;
- redirect-compatible remote retrieval;
- structured source-level outcomes;
- source-level failure isolation;
- normalisation;
- generic HTML-to-text description normalisation;
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
- concurrency protection;
- domains whose classification evidence comes entirely from validated source defaults;
- empty domain keyword lists where explicitly permitted;
- deterministic case-sensitive acronym handling;
- multilingual deterministic keyword classification;
- historical regression using persisted processed records.

Phase 3 automation architecture is complete.

Phase 4 has now demonstrated three important architectural properties.

First:

> substantial source/domain expansion can usually be performed through configuration and existing pipeline components.

Examples:

```text
Sifted
→ Tech.eu

Financial Markets
→ added through configuration

Federal Reserve
→ added through configuration

Lavoce.info
→ added through configuration

Google DeepMind
→ added through configuration
```

Second:

> strategic macroareas can be implemented through the existing article pipeline even when lexical keywords are not the correct primary classification evidence.

Examples:

```text
Tech Europe Foundation
→ source default
→ Milan and Bocconi Ecosystem

MIMIT News
→ source default
→ Italy

Lavoce.info Imprese
→ source default
→ Italy
```

Third:

> source-specific input defects should trigger general fixes only when the fix improves the architecture beyond one source.

Example:

```text
MIMIT HTML descriptions
→ exposed a general normalization issue
→ generic HTML-to-text normalization implemented
→ no MIMIT-specific branch added
```

The current architectural priority remains:

> **continue controlled source research using the existing pipeline, while refusing new processing architectures unless repeated evidence shows they are necessary.**

---

# 3. High-Level Architecture

The implemented application flow is:

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

This remains an important architectural constraint:

> local validation should exercise the same code path used by scheduled production.

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

Defines core immutable or structured data models used across the pipeline.

Important conceptual models include:

- source configuration;
- domain configuration;
- raw collected item;
- normalised article record;
- source collection outcome;
- validation result;
- run summary structures.

The article remains the core production record type.

Do not introduce a separate event, opportunity or statistical record model without a validated requirement.

---

## 5.2 `config.py`

Loads and validates repository configuration.

Responsibilities include:

- source registry loading;
- domain registry loading;
- settings loading;
- required-field validation;
- type validation;
- source/default-domain references;
- configuration error reporting.

Current architecture supports:

```text
SourceConfig.default_domains
```

including:

```text
empty tuple/list
```

for sources with no automatic domain evidence.

Current architecture also supports:

```text
DomainConfig.keywords
```

being empty.

This is deliberately used where source identity provides better evidence than generic lexical rules.

Current examples:

```text
Italy
keywords: []

Milan and Bocconi Ecosystem
keywords: []
```

This does not mean all domains should omit keywords.

It means:

> empty keyword sets are a supported configuration state when validated source defaults provide stronger evidence.

Source configuration and domain configuration remain separate from processing logic.

---

## 5.3 `collect.py`

Collects configured RSS/Atom sources.

Responsibilities include:

- public HTTP/HTTPS retrieval;
- explicit request headers;
- bounded timeout;
- redirect handling;
- feed parsing;
- raw item extraction;
- source-level result reporting;
- source-level failure isolation.

Current remote retrieval policy includes:

```text
timeout = 10 seconds
standard TLS verification
explicit User-Agent
explicit Accept header
```

Retry logic is not implemented.

Do not add retries until repeated production evidence shows that transient failures are materially harming report quality.

A source failure should normally degrade the run rather than crash the entire pipeline.

Malformed or technically incompatible feeds should not automatically trigger parser exceptions or source-specific repairs.

A general collector change requires evidence that it improves more than one strategically justified source class.

---

## 5.4 `normalize.py`

Converts collected feed entries into a consistent article schema.

Responsibilities include:

- field extraction;
- title cleanup;
- URL cleanup;
- timestamp normalisation;
- description handling;
- generic HTML-to-text cleanup;
- deterministic record identity;
- source metadata preservation.

Publication timestamps are converted to timezone-aware UTC datetimes.

Record identity remains deterministic.

### HTML Description Normalisation

Phase 4 added generic HTML-to-text handling after MIMIT exposed feed descriptions containing HTML markup.

The current normalization path now:

```text
feed description
→ HTML-to-text cleanup
→ whitespace cleanup
→ punctuation-safe normalized text
→ None if no meaningful text remains
```

This behaviour is generic.

It is not tied to MIMIT or any other individual source.

The change followed the architectural rule:

> when a source exposes a genuine general parsing defect, fix the common normalization layer rather than branching on source identity.

Normalisation should still not perform:

- semantic classification;
- summarisation;
- translation;
- entity extraction;
- source-specific article-body extraction.

---

## 5.5 `validate.py`

Rejects structurally unusable normalised records.

Validation currently checks required fields and record integrity.

Validation is intentionally structural rather than semantic.

A record can be structurally valid but later remain unclassified.

That is acceptable.

---

## 5.6 `filter_window.py`

Applies the publication-time eligibility window.

Current default:

```text
previous 24 hours relative to actual execution time
```

Records without usable publication timestamps are excluded.

The pipeline does not silently substitute retrieval time.

This preserves deterministic temporal semantics.

Assolombarda testing reinforced this design.

Its official feeds were technically collectable but produced:

```text
0/15 usable publication timestamps
```

for both tested streams.

The correct architectural response was:

```text
do not activate source
```

not:

```text
replace publication time with retrieval time
```

Known limitation:

GitHub Actions scheduling can start materially later than the nominal schedule, so the rolling 24-hour window moves with actual execution.

A fixed reporting cutoff remains an open future design decision.

Do not redesign the window without repeated evidence of meaningful information loss.

---

## 5.7 `deduplicate.py`

Performs exact deterministic duplicate reduction.

Current keys:

1. normalized URL;
2. normalized title.

First deterministic occurrence is retained.

Near-duplicate or semantic clustering is not implemented.

Italian Tech Alliance testing exposed a plausible future use case where multiple press-clipping entries may describe the same underlying event.

That is not yet sufficient to justify architectural expansion.

---

## 5.8 `classify.py`

Assigns topic domains using deterministic evidence.

Current evidence classes:

1. configured source defaults;
2. configured keyword matches against title and description.

Multi-domain classification is supported.

Unclassified records remain valid.

### Source Defaults

A source default acts as explicit classification evidence.

Current examples:

```text
Istat
→ Economics and Macroeconomics

Federal Reserve Board Monetary Policy
→ Economics and Macroeconomics

OpenAI News
→ Artificial Intelligence

Google DeepMind News
→ Artificial Intelligence

MIMIT News
→ Italy

Lavoce.info Imprese
→ Italy

Tech Europe Foundation
→ Milan and Bocconi Ecosystem
```

Broad heterogeneous sources may have no defaults.

Examples:

```text
BBC World
BBC Business
ECB
European Commission
Tech.eu
```

### Keyword Case Semantics

Current deterministic convention:

```text
configured keyword containing only lowercase characters
→ case-insensitive match

configured keyword containing uppercase characters
→ case-sensitive match
```

The motivating example was:

```text
AI
```

Using lowercase:

```text
ai
```

caused false Artificial Intelligence classifications in Italian-language content because `ai` is an ordinary Italian word.

The case convention preserved historical English AI recall while removing false Italian matches.

The same mechanism now supports:

```text
IA
```

for the Italian AI acronym.

This simple rule remains preferable to introducing:

- language detection;
- NLP;
- stemming;
- machine learning.

### Empty-Keyword Domains

A domain may contain:

```yaml
keywords: []
```

and still be classifiable through source defaults.

Current examples:

```text
Italy
Milan and Bocconi Ecosystem
```

This is a general architectural capability but should remain a deliberate policy choice.

---

## 5.9 `rank.py`

Computes deterministic relevance scores.

Current formula:

```text
source-tier score
+ 2 × assigned domains
+ 1 × matched keywords
```

Current source-tier values:

```text
Tier 1 = 4
Tier 2 = 3
Tier 3 = 2
Tier 4 = 1
```

The ranking model is intentionally simple.

Do not add:

- machine learning;
- semantic scoring;
- source-specific penalties;
- publisher-diversity penalties;
- AI relevance scoring;

until repeated report evidence shows that upstream source/classification correction is insufficient.

### Important Interaction

Classification evidence affects ranking.

Therefore:

```text
broad source default
→ extra domain
→ extra relevance score

broad keyword
→ extra keyword evidence
→ extra relevance score
```

This is why taxonomy changes require regression testing.

The Lavoce.info keyword audit reinforced that near-synonymous keywords should not be added merely because they describe the same concept.

Avoid duplicate lexical evidence that only inflates score.

---

## 5.10 `storage.py`

Persists processed article records.

Current format:

```text
JSON Lines
```

Current storage pattern is date-based and repository-native.

Storage prioritises:

- transparency;
- inspectability;
- simple diffs;
- no external database;
- zero recurring cost.

Historical processed records also function as a regression corpus for classification/taxonomy changes.

Do not introduce a database until JSONL becomes a demonstrated limitation.

---

## 5.11 `report.py`

Selects and renders report items from processed records.

Current report selection rules include:

```text
maximum items per primary domain = 5
maximum total items              = 30
```

These are upper bounds, not quotas.

Eligible records must:

- be classified;
- belong to an active domain;
- have a valid primary domain.

Selection order is deterministic.

Current ordering uses:

1. descending relevance score;
2. descending publication timestamp;
3. source tier;
4. normalized title;
5. record ID.

Primary placement is:

```text
record.domains[0]
```

Secondary domains are rendered as:

```text
Also:
```

A multi-domain story appears once.

Report sections follow configured domain order.

The report does not attempt semantic story clustering.

Descriptions are currently truncated according to configuration.

Current maximum:

```text
300 characters
```

This is a known product limitation and is intentionally deferred to the richer-report phase.

---

## 5.12 `run_summary.py`

Builds machine-readable operational run metadata.

Current run summary tracks aggregate information such as:

- active sources;
- successful sources;
- failed sources;
- empty sources;
- raw items;
- valid items;
- invalid items;
- duplicate items;
- displayed items;
- monitored window;
- warnings;
- run status.

Per-source details are available through logging during execution.

The current aggregate JSON summary does not persist a full per-source diagnostic registry.

No long-term source-health database exists.

Per-run logging and summaries remain sufficient for current needs.

---

## 5.13 `pipeline.py`

Orchestrates the complete deterministic workflow.

Current logical sequence:

```text
load configuration
→ collect sources
→ normalize
→ validate
→ filter collection window
→ deduplicate
→ classify
→ rank
→ persist processed records
→ build run summary
→ render report
→ persist outputs
```

The pipeline:

- isolates source failures;
- preserves successful source output;
- produces degraded status where appropriate;
- fails clearly for critical configuration or pipeline errors;
- writes operational logs.

There is no parallel AI processing path.

---

## 5.14 `cli.py`

Provides one-command local and production execution.

Current production-equivalent command:

```text
python -m daily_intelligence.cli run
```

When required by local environment layout:

```text
PYTHONPATH=src python -m daily_intelligence.cli run
```

GitHub Actions executes the same application entry point.

---

# 6. Current Source Architecture

Current active production sources:

```text
BBC News World
BBC News Business
European Central Bank
European Commission Highlighted News
Istat Press Releases
OpenAI News
Tech.eu
Tech Europe Foundation
Federal Reserve Board Monetary Policy
MIMIT News
Lavoce.info Imprese
Google DeepMind News
```

All current production collection routes use public structured RSS.

No current source requires:

- credentials;
- paid APIs;
- Bocconi authentication;
- premium article retrieval.

Current active source architecture remains deliberately uniform:

```text
public structured feed
→ standard collector
→ standard normalizer
→ ArticleRecord
```

No active source currently requires:

- a source-specific collector;
- a separate parser;
- a separate record model;
- a custom persistence path.

This remains a strong architectural success criterion for source expansion.

---

# 7. Current Domain Architecture

Current active domains:

```text
Global Politics and Geopolitics
Economics and Macroeconomics
Financial Markets
Companies and Corporate Strategy
Artificial Intelligence
Technology and Software
Startups and Venture Capital
Europe and the European Union
Italy
Milan and Bocconi Ecosystem
```

All ten strategic macroareas are now implemented.

Most domains use keyword evidence.

Two domains currently demonstrate source-defined classification:

```text
Italy
Milan and Bocconi Ecosystem
```

with empty keyword lists.

Their architecture is:

```text
validated narrow source
→ source default
→ domain
```

This is intentionally more conservative than inventing broad lexical keywords.

---

# 8. Configuration Architecture

Configuration remains repository-native YAML.

## Sources

`config/sources.yaml` defines fields such as:

```text
id
name
feed_url
source_type
source_tier
default_domains
language
geographic_scope
active
```

## Domains

`config/domains.yaml` defines:

```text
id
name
keywords
active
```

Domain keyword lists may be empty.

## Settings

`config/settings.yaml` defines ranking and report settings.

Current relevant values include:

```text
ranking:
  source_tier_scores:
    1: 4
    2: 3
    3: 2
    4: 1
  domain_match_score: 2
  keyword_match_score: 1
```

and:

```text
report:
  max_items_per_domain: 5
  max_total_items: 30
  max_description_length: 300
```

Configuration remains preferred over code changes when source/domain additions fit the current processing model.

The Federal Reserve, Lavoce.info and Google DeepMind integrations required no production Python changes.

The MIMIT integration required one general normalization improvement, not source-specific branching.

---

# 9. Current Milan/Bocconi Architecture

Milan/Bocconi is implemented through:

```text
Tech Europe Foundation News RSS
→ collect
→ normalize
→ validate
→ 24-hour filter
→ deduplicate
→ source-default classification
→ rank
→ standard ArticleRecord storage
→ standard report
```

Current source configuration conceptually behaves as:

```text
Tech Europe Foundation
Tier 1
default domain:
Milan and Bocconi Ecosystem
```

The domain currently contains:

```yaml
keywords: []
```

This architecture was chosen because TEF's information value comes from institutional identity rather than generic words such as:

```text
Milan
Bocconi
startup
event
```

The implementation required:

- source configuration;
- domain configuration;
- support for empty domain keyword lists;
- configuration tests.

It did **not** require:

- event scraping;
- Bocconi authentication;
- an opportunity data model;
- a deadline engine;
- a new ranking model;
- source-specific collector logic.

This remains an important architectural precedent:

> use the existing article pipeline for professional-ecosystem sources until article semantics become demonstrably insufficient.

---

# 10. Current Italy Architecture

Italy is now implemented through the same standard article pipeline.

Current architecture:

```text
Istat
→ Economics/Macro default

MIMIT News
→ Italy default

Lavoce.info Imprese
→ Italy default
```

The Italy domain contains:

```yaml
keywords: []
```

This is intentional.

Generic terms such as:

```text
Italia
azienda
impresa
investimenti
```

were not used as Italy-domain classifiers because they would create excessive noise.

Instead:

```text
source identity
→ Italy domain evidence
```

while narrow bilingual keywords provide additional topical domains.

Examples:

```text
tavoli di crisi
accordo di sviluppo
quadro industriale
rilevanza strategica
fusione e acquisizione
piano industriale
inflazione
IA
mercati dei capitali
```

The implementation required:

- one new domain;
- source configuration;
- narrow keyword configuration;
- deterministic multilingual regression;
- generic description normalization for MIMIT.

It did **not** require:

- Italian-language NLP;
- a second classifier;
- source-specific ranking;
- a separate Italy pipeline;
- a new record type.

This validates the source-defined-domain architecture beyond TEF.

---

# 11. Current AI Architecture

Current primary AI architecture:

```text
OpenAI News
→ Artificial Intelligence source default

Google DeepMind News
→ Artificial Intelligence source default
```

Both use the standard article pipeline.

DeepMind integration required only:

- source configuration;
- configuration tests.

Controlled classification review showed:

```text
100/100 DeepMind records
→ Artificial Intelligence

97/100
→ AI only

3/100
→ sensible secondary domains through existing taxonomy
```

No DeepMind-specific keywords or ranking rules were needed.

The architectural AI problem is therefore no longer:

```text
how to add a second primary lab
```

It is:

```text
whether a clean independent reporting source can be added
without special architecture
```

No special AI processing layer is justified.

---

# 12. Current Real Integration Evidence

The latest controlled production-equivalent checkpoint validated twelve active sources.

Observed 18 August 2026 run:

```text
12 active sources
12 successful
0 failed
0 invalid
0 warnings

1432 valid records
44 inside collection window
42 unique
37 unclassified
5 displayed

status: success
```

Google DeepMind collected:

```text
100 feed entries
```

No DeepMind items entered the processed 24-hour output because the newest feed item was outside the monitored window.

This was expected.

Earlier Phase 4 runs also validated:

```text
Federal Reserve integration
MIMIT + Italy integration
Lavoce.info integration
```

without requiring new pipeline architecture.

The current integration evidence therefore demonstrates:

- twelve-source collection;
- ten-domain configuration;
- multiple source defaults;
- two empty-keyword domains;
- bilingual keyword classification;
- general HTML description normalization;
- deterministic ranking;
- normal output generation;
- absence of stale-record leakage.

---

# 13. Collection Architecture

The collector should remain generic.

Preferred source order:

```text
RSS / Atom
→ official structured API
→ other explicitly permitted structured public endpoint
→ narrowly justified deterministic extraction
```

Avoid HTML scraping where a structured official source exists.

For each new source:

```text
endpoint research
→ direct technical probe
→ production collector test
→ normalizer test
→ configuration integration
```

Do not add source-specific collector modules unless unavoidable and justified by source value.

Recent source audits provide useful negative evidence:

```text
Bruegel
→ malformed useful feeds
→ also full-content persistence problem
→ no collector hardening justified

Assolombarda
→ technically collectable
→ no publication timestamps
→ no date-recovery branch justified
```

The architecture should reject incompatible sources rather than accumulate exceptions.

---

# 14. Network and Failure Architecture

Remote source retrieval can fail because of:

- DNS/network errors;
- HTTP errors;
- TLS errors;
- timeouts;
- malformed feeds;
- endpoint changes.

Current architecture isolates failures at source level.

A single failed source should not normally prevent:

- successful-source processing;
- report generation;
- output persistence.

Run status distinguishes:

```text
success
degraded
failure
```

Critical configuration or orchestration failures remain blocking.

Do not mask critical failures simply to publish a report.

---

# 15. Degraded-Run Architecture

A degraded run is legitimate when:

- one or more sources fail;
- enough successful source data remains to produce a meaningful output;
- the report and run summary expose the degraded state.

Degraded output is preferable to an invisible failure when partial information is still useful.

The report must not imply that all sources succeeded when they did not.

---

# 16. Automation Architecture

Production automation uses GitHub Actions.

Current production workflow:

```text
.github/workflows/daily-intelligence.yml
```

Supported triggers:

```text
workflow_dispatch
scheduled daily trigger
```

Current intended schedule:

```text
06:05 Europe/Rome
```

The workflow performs:

```text
checkout
→ Python setup
→ dependency installation
→ full tests
→ production CLI
→ output validation
→ git staging
→ no-change check
→ bot commit
→ push
```

Automation consumes no AI credits.

---

# 17. Scheduled-Execution Limitation

GitHub Actions scheduling is not guaranteed to start precisely at the configured minute.

Observed latency can shift the actual rolling report window because:

```text
window end = actual execution time
window start = execution time - 24h
```

Current decision:

> keep the simple rolling window until repeated real evidence shows that schedule latency causes meaningful information loss or inconsistent daily coverage.

Possible future alternative:

```text
fixed daily reporting cutoff
```

Not implemented.

---

# 18. Persistence Architecture

Current production outputs are committed back to the repository.

Primary persisted artefacts:

```text
data/processed/YYYY/MM/YYYY-MM-DD.jsonl
data/runs/YYYY/MM/YYYY-MM-DD.json
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

Benefits:

- no database;
- no hosting cost;
- transparent history;
- easy Git diffing;
- simple manual inspection;
- regression corpus naturally accumulates.

Costs:

- repository growth;
- public-storage copyright constraints;
- same-day reruns overwrite date-keyed outputs before commit if run locally.

Persistence architecture also creates an important source-selection constraint.

A public feed can still be unsuitable when it exposes:

```text
substantial article text
or
effectively complete publication bodies
```

Bruegel demonstrated this failure mode.

Therefore:

> feed accessibility and feed persistence compatibility are independent gates.

Do not introduce external storage until repository-native persistence becomes a measured limitation.

---

# 19. Historical Regression Architecture

Stored JSONL outputs are not only historical data.

They also function as a deterministic regression corpus.

Current validation pattern:

```text
proposed keyword/source-default change
→ replay against stored processed records
→ inspect changed classifications/scores
→ evaluate false positives
→ retain or reject change
```

This approach has already been used for:

- Tech.eu keyword refinement;
- Financial Markets;
- `startup` removal;
- Italian-source classification;
- `AI` case matching;
- Italian Tech Alliance candidate keywords;
- Federal Reserve Financial Markets keywords;
- MIMIT Italian keywords;
- Lavoce.info bilingual keywords.

This remains the preferred validation mechanism before introducing more sophisticated evaluation infrastructure.

---

# 20. Report Architecture

The report is intentionally simple Markdown.

It provides:

- report date;
- generated timestamp;
- run status;
- monitored window;
- source-health summary;
- items collected;
- displayed items;
- sections by primary domain;
- headline/link;
- source;
- publication time;
- relevance score;
- secondary domains;
- truncated description.

GitHub-hosted Markdown remains sufficient as the current delivery interface.

Do not build a frontend until repository browsing becomes a demonstrated usability problem.

---

# 21. Richer-Report Architecture

The user need is validated:

> reports should provide enough context to understand major developments without immediate click-through.

However, implementation architecture is intentionally deferred.

Current description limit:

```text
300 characters
```

Potential future solution order:

1. richer RSS/Atom metadata;
2. public structured summaries;
3. official free APIs;
4. narrowly permitted deterministic public extraction;
5. more complex methods only if required.

Do not assume LLM summarisation is necessary.

The future architecture must preserve:

- zero recurring cost;
- provenance;
- copyright safety;
- source transparency;
- low maintenance.

Phase 4 is now approaching the point where richer-report architecture should be compared directly with the expected value of another source.

That crossover has not yet been declared.

---

# 22. Premium-Source Architecture

Premium reading access and production ingestion are separate.

The architecture may support a premium source only when:

```text
legitimate user reading access
+
public / automation-compatible discovery route
+
no premium body retrieval
+
public-repository-compatible persistence
```

The system must not:

- automate OpenAthens;
- log into premium publishers;
- store publisher credentials;
- fetch premium article bodies;
- bypass paywalls.

The Premium Bocconi Exception changes acceptable user follow-up behaviour, not the authentication model.

Completed audits demonstrate why this boundary matters:

```text
Financial Times
→ strategically excellent
→ RSS persistence conflict
→ standby

Il Sole 24 Ore
→ technically strong
→ persistence/licensing boundary insufficiently clean
→ standby

Nasdaq
→ structured/public access exists
→ persistence terms conflict
→ standby

Ars Technica
→ official RSS exists
→ persistence rights insufficiently clean
→ standby
```

No premium publication is currently active through this exception.

---

# 23. Bank of Italy Structured-Data Architecture

Bank of Italy BDS exposed a potential future source class that does not fit the current article pipeline directly.

A statistical-event architecture would conceptually require:

```text
series configuration
→ structured data fetch
→ observation parsing
→ identify new period / release
→ compare previous observation
→ detect revisions
→ significance rule
→ generated intelligence event
→ normal domain/ranking/report pipeline
```

This architecture is **not implemented**.

Reason for deferral:

- article-source breadth remains a higher-value problem;
- event-generation semantics have not been designed;
- significance thresholds have not been validated;
- additional state would be required.

Bank of Italy BDS remains the strongest validated future use case.

Do not build generic statistical infrastructure before selected series demonstrate sufficient user value.

---

# 24. Opportunity and Deadline Architecture

Professional opportunities can have time semantics different from article publication.

Possible fields include:

```text
opportunity_name
organiser
application_open
deadline
event_date
location
application_url
source_url
```

The current system does not maintain these fields.

Current TEF implementation deliberately remains within:

```text
ArticleRecord
```

Potential future need:

```text
publication date
≠
deadline
≠
event date
```

A stateful opportunity/deadline architecture should be introduced only if repeated real-source usage shows that the current publication-based model causes important opportunities to disappear before they are useful.

Do not create an opportunity database merely because the Milan/Bocconi domain exists.

---

# 25. Security and Privacy Architecture

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

Even if GitHub Secrets could technically store institutional credentials, architecture policy prohibits using that mechanism to automate premium publisher or Bocconi access merely because the user has legitimate reading rights.

---

# 26. Copyright and Content Boundaries

The repository may store, where permitted:

- titles;
- source names;
- links;
- timestamps;
- limited feed descriptions;
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

## Full-Content Feed Boundary

A public RSS feed is not automatically suitable for persistence.

If a feed's description/content field exposes substantial or complete article bodies, the source must not be integrated merely because the feed parser can read it.

Bruegel validated this boundary.

## Richer-Report Boundary

The richer-context requirement does not override copyright rules.

Objective:

> enough lawful context for initial understanding.

Not:

> reproduction of the source article.

---

# 27. Architecture for ChatGPT and Copilot Use

ChatGPT remains outside the production dependency chain.

Production must remain useful without any ChatGPT API call.

ChatGPT may be used manually for:

- development reasoning;
- code review;
- project-document drafting;
- source/domain strategy;
- source-audit interpretation;
- product-quality review;
- classification/ranking analysis;
- deciding whether observed limitations justify implementation changes.

GitHub Copilot may be used selectively during development for:

- narrow mechanical edits;
- repetitive multi-file configuration/test updates;
- repository-local locating or completion work.

Copilot must not become:

- a production dependency;
- an architectural decision-maker;
- a substitute for validation;
- a recurring-credit requirement.

The working development principle remains:

```text
ChatGPT decides and writes
→ Copilot may locate/apply narrow mechanical edits
→ Git/tests verify
```

The production separation remains:

```text
Daily Intelligence System
= deterministic production infrastructure

ChatGPT / Copilot
= external development assistance
```

---

# 28. Implemented vs Active vs Deferred Architecture

## Implemented and Validated

- Python package;
- repository-native configuration;
- twelve-source public RSS registry;
- ten-domain active taxonomy;
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
- generic HTML-to-text description cleanup;
- deterministic URL cleaning;
- UTC-aware timestamps;
- deterministic record IDs;
- structural validation;
- previous-24-hours publication filtering;
- exact deduplication;
- deterministic classification;
- empty source defaults;
- empty domain keyword support;
- validated source-defined domains;
- uppercase-sensitive keyword handling;
- English/Italian deterministic keyword support;
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
- historical regression workflow;
- Tech.eu replacing Sifted;
- Financial Markets domain;
- Milan and Bocconi Ecosystem domain;
- Italy domain;
- Tech Europe Foundation source;
- Federal Reserve Board Monetary Policy source;
- MIMIT News source;
- Lavoce.info Imprese source;
- Google DeepMind News source;
- conservative bilingual keyword regression workflow.

## Active Architectural Evaluation

- further source correction/expansion against remaining information-function gaps;
- global Companies/Corporate Strategy coverage;
- broader Financial Markets source coverage;
- independent AI/Technology reporting;
- independent Europe/EU interpretation;
- Startups/VC diversification;
- broader Milan/Bocconi and Milan/Lombardy coverage;
- Italian Tech Alliance production readiness;
- source metadata richness;
- reporting-window cutoff independence;
- richer-report architecture after the next source-research cycle.

## Deferred Until Evidence

- retry logic;
- near-duplicate clustering;
- story clustering;
- entity extraction;
- article-level geography;
- content-type classification;
- separate opportunity record model;
- opportunity deadline state;
- statistical-event pipeline;
- long-term source-health database;
- advanced ranking;
- automatic publisher-diversity penalties;
- LLM summarisation;
- authenticated premium ingestion;
- authenticated Bocconi ingestion;
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

# 29. Current Architectural Limitations

Known limitations include:

- current production universe contains twelve feeds but still lacks complete information-function coverage;
- Financial Markets is stronger on monetary/rates evidence than broader capital markets;
- Companies/Corporate Strategy still lacks a strong international dedicated reporting source;
- Milan/Bocconi has only a first narrow production source;
- Milan/Lombardy established-company coverage remains incomplete;
- independent AI/technology reporting remains unresolved;
- primary AI evidence is now diversified across OpenAI and DeepMind;
- Startups/VC depends heavily on Tech.eu;
- Europe/EU still lacks a clean independent analytical source;
- current active automated sources are majority English-language;
- bilingual deterministic classification is validated but remains deliberately conservative;
- exact deduplication does not detect differently worded coverage of the same story;
- records without publication timestamps are excluded;
- ranking remains provisional;
- classification remains conservative;
- strategically useful records can still remain unclassified;
- no entity enrichment exists;
- no article-level geography exists;
- no content-type classification exists;
- no statistical-event processing exists;
- no opportunity-state model exists;
- no deadline persistence exists;
- no long-term source-health database exists;
- report descriptions remain capped at 300 characters;
- scheduled execution time influences the collection window;
- repository-native storage creates strict copyright/persistence requirements for candidate sources;
- malformed feeds are not generically repaired if the resulting content is unsuitable for persistence;
- no metadata-only alternate persistence path exists;
- no source-specific date-recovery path exists.

These are maturity limits, not automatic implementation requirements.

---

# 30. Open Architecture Decisions

## Reporting Window

Question:

> Should reports eventually use a fixed daily cutoff rather than actual workflow start time?

Status:

> open; no change without repeated evidence.

---

## Retry Behaviour

Question:

> Would limited retry logic materially improve source reliability?

Status:

> deferred.

---

## Near-Duplicate Handling

Question:

> Do sources such as Italian Tech Alliance create enough repeated same-story coverage to justify clustering?

Status:

> deferred pending repeated production evidence.

---

## Statistical Events

Question:

> Should official statistical series such as Bank of Italy BDS generate deterministic intelligence events?

Status:

> validated future use case, architecture not approved for implementation yet.

---

## Opportunity State

Question:

> Do Milan/Bocconi opportunities need deadline/event-state persistence rather than publication-only treatment?

Status:

> deferred pending production evidence.

---

## Independent AI / Technology Reporting

Current architecture:

```text
OpenAI
→ primary source

Google DeepMind
→ second primary source
```

Remaining information role:

```text
independent reporting / interpretation
```

Status:

> source role still open; no special architecture justified.

Ars Technica was audited and rejected under current persistence constraints.

The next source-research cycle may identify a cleaner candidate.

---

## Italy Architecture

Current implemented architecture:

```text
Istat
+ MIMIT News
+ Lavoce.info Imprese
```

with Bank of Italy structured data later if justified.

Status:

> implemented and architecturally validated.

Assolombarda and Italian Tech Alliance remain potential complementary roles, but neither is required to consider the basic Italy architecture complete.

---

## Metadata-Only Source Path

Question:

> Should the system eventually support deliberately title/link/date-only persistence for strategically important sources whose description fields cannot safely be stored?

Status:

> not approved.

Current evidence from Bruegel, Ars Technica and Assolombarda is insufficient to justify a second persistence path.

Prefer source replacement or standby unless several high-value sources demonstrate the same need.

---

## Source-Specific Date Recovery

Question:

> Should publication dates ever be recovered by scraping article pages when RSS timestamps are missing?

Status:

> not approved.

Assolombarda did not justify such a branch.

Publication-time semantics remain strict.

---

## Richer Report

Validated product need.

Architecture remains intentionally undefined until the next source-research cycle clarifies whether source expansion has reached diminishing returns.

---

# 31. Architecture Validation Gates

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
- degraded-source validation.

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

**Status: passed**

Evidence:

- Sifted replaced by Tech.eu;
- Financial Markets added without new processing modules;
- classification regression workflow established;
- Italian keyword collision reproduced;
- classifier case behaviour corrected;
- Tech Europe Foundation added;
- Milan/Bocconi domain added;
- empty-keyword domain support added;
- source-defined classification validated;
- Federal Reserve Monetary Policy added;
- MIMIT News added;
- Italy added as tenth domain;
- Lavoce.info Imprese added;
- Google DeepMind News added;
- bilingual classification validated;
- generic HTML description normalization added;
- full real twelve-source pipeline executed successfully.

This proves:

> the current architecture can support ordinary keyword-defined domains, narrow source-defined domains, multilingual deterministic classification and continued source expansion without new processing layers.

What remains open is the **information universe**, not the expansion architecture.

---

## Gate F — Italy Architecture

**Status: passed**

Evidence:

- dedicated Italy domain implemented;
- suitable public source set validated;
- Istat + MIMIT + Lavoce provide differentiated roles;
- MIMIT and Lavoce use validated Italy source defaults;
- Italy domain works with an empty keyword list;
- bilingual keyword regression completed;
- historical regression completed;
- real production-equivalent runs succeeded;
- no Italy-specific processing pipeline was required;
- no authenticated premium source is required.

This proves:

> the current `ArticleRecord` architecture is sufficient for a viable first Italy implementation.

Information breadth may still improve without reopening the architecture gate.

---

## Gate G — Richer Report Architecture

**Status: not passed**

Required before implementation:

- exact context requirement;
- source metadata audit;
- copyright/access boundary;
- premium-source fallback behaviour;
- output-length target;
- provenance design;
- candidate approach comparison;
- acceptance tests.

The user need is validated.

Implementation architecture is not.

The gate should be reconsidered after the next gap-driven source-research batch.

---

## Gate H — Advanced Quality Architecture

**Status: not passed**

Possible future examples:

- near-duplicate clustering;
- entities;
- content type;
- article-level geography;
- statistical intelligence events;
- deadline tracking;
- advanced ranking.

Entry requires:

- repeated real problem;
- simpler corrections insufficient;
- explicit evaluation method.

---

# 32. Current Architecture Summary

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
12 active public RSS sources
10 active domains

deterministic source defaults
deterministic keyword classification
source-defined domain support
empty-keyword domain support
deterministic keyword case semantics
English/Italian deterministic classification
generic HTML-to-text description normalization
deterministic ranking
repository-native historical data
historical regression workflow
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
Tech Europe Foundation
Federal Reserve Board Monetary Policy
MIMIT News
Lavoce.info Imprese
Google DeepMind News
```

Current active domains:

```text
Global Politics and Geopolitics
Economics and Macroeconomics
Financial Markets
Companies and Corporate Strategy
Artificial Intelligence
Technology and Software
Startups and Venture Capital
Europe and the European Union
Italy
Milan and Bocconi Ecosystem
```

Current architectural direction:

```text
run fresh gap-driven source research
→ audit only differentiated candidates
→ continue reusing existing ArticleRecord architecture
→ reject source-specific complexity without cross-source evidence
→ reassess source-expansion marginal value
→ design richer report context when it becomes higher ROI
```

Potential future architecture remains gated:

```text
Bank of Italy BDS
→ statistical-event pipeline only if justified

professional opportunities
→ state/deadline model only if justified

near-duplicate clusters
→ only after repeated report evidence

metadata-only persistence
→ only if multiple high-value sources justify it
```

The architecture should remain simple unless actual report usage proves otherwise.

---

# Changelog

## 2026-08-18 — Twelve-Source / Ten-Domain Architecture Checkpoint

- Reconciled architecture with the validated twelve-source / ten-domain production state.
- Added Federal Reserve Board Monetary Policy to the active source architecture.
- Added MIMIT News to the active source architecture.
- Added Lavoce.info Imprese to the active source architecture.
- Added Google DeepMind News to the active source architecture.
- Added Italy as the tenth implemented domain.
- Recorded Italy as a source-defined empty-keyword domain.
- Recorded MIMIT and Lavoce.info Italy source defaults.
- Recorded bilingual deterministic keyword classification as production-validated.
- Added the intentional uppercase Italian AI acronym `IA`.
- Recorded Federal Reserve Financial Markets keyword integration.
- Recorded MIMIT and Lavoce.info keyword regression as examples of the historical-regression architecture.
- Added generic HTML-to-text feed-description normalization after the MIMIT integration.
- Recorded that the fix was general rather than source-specific.
- Recorded Google DeepMind as the second Tier 1 frontier-lab source.
- Recorded that DeepMind required configuration/test changes only.
- Removed the stale DeepMind "source audit pending" architecture assumption.
- Marked Italy Architecture Gate F as passed.
- Recorded the latest twelve-source production-equivalent validation:
  - 12 active;
  - 12 successful;
  - 0 failed;
  - 0 invalid;
  - 0 warnings.
- Recorded Bruegel as evidence against blindly hardening the parser when useful feeds also expose full-content payloads.
- Recorded Assolombarda as evidence against source-specific publication-date recovery or retrieval-time substitution.
- Added metadata-only persistence as an explicit but unapproved future architecture question.
- Added source-specific date recovery as an explicit but unapproved future architecture question.
- Reframed the active architecture problem from "validate Italy / diversify AI" to "audit the remaining information-function gaps using the existing architecture."
- Preserved richer-report architecture as deferred, but moved it closer to explicit comparison against further source expansion.
- Recorded selective Copilot use as development assistance only, never as a production dependency.

## 2026-08-17 — TEF / Milan-Bocconi and Multilingual Classification Architecture

- Reconciled architecture with the pushed eight-source / nine-domain production checkpoint.
- Added Tech Europe Foundation as the eighth active RSS source.
- Added Milan and Bocconi Ecosystem as the ninth implemented domain.
- Added support for domain configurations with empty keyword lists.
- Recorded source-defined domains as a supported deterministic architecture.
- Recorded TEF's Milan/Bocconi source default.
- Recorded that the TEF implementation reused the standard `ArticleRecord` pipeline and required no scraper, event model, deadline engine or source-specific collector.
- Recorded full production-equivalent eight-source pipeline validation.
- Recorded the 8/8 successful-source result.
- Recorded that TEF correctly contributed no stale records outside the 24-hour publication window.
- Added deterministic case semantics for configured keywords.
- Recorded intentional case-sensitive `AI` matching to avoid Italian `ai` false positives.
- Recorded that historical English AI recall was preserved.
- Reframed Source/Domain Expansion Gate E as architecturally passed while information-universe expansion remained active.
- Added Bank of Italy BDS as the strongest validated future statistical-event architecture use case.
- Added opportunity/deadline state tracking as a future architecture gated by real Milan/Bocconi evidence.
- Added Italian Tech Alliance as a possible future near-duplicate evidence source without approving clustering.
- Preserved richer-report architecture as deferred.

## 2026-08-17 — Phase 4A Source and Domain Architecture Validation

- Replaced Sifted with Tech.eu in the active source registry.
- Recorded the controlled Tech.eu/Sifted comparison.
- Recorded 20/20 Tech.eu descriptions versus 0/24 Sifted descriptions in the tested samples.
- Recorded that source replacement was driven by product metadata/access quality rather than parser compatibility.
- Recorded Tech.eu as a broad Tier 2 source with no default domain.
- Added Financial Markets as the eighth implemented domain.
- Recorded that Financial Markets required configuration only and no processing-module changes.
- Added the evidence-backed classification changes `tariffs`, `acquired`, `early-stage fund` and `funding market`.
- Recorded removal of generic `startup`.
- Added the architectural warning that near-synonymous keywords may independently increase score.
- Added the historical regression pattern as a reusable source/taxonomy validation mechanism.
- Recorded the real 17 August 2026 pipeline validation.
- Established that classification percentage is not an architectural KPI.
- Added the narrow Premium Bocconi Exception while preserving the existing authentication prohibition.
- Upgraded Milan/Bocconi from candidate to validated product requirement.
- Recorded the preference to reuse the existing `ArticleRecord` pipeline for future Milan/Bocconi inputs before creating new event/opportunity architecture.
- Preserved ranking weights, report settings and core processing modules unchanged.

## 2026-08-14 — Phase 3 Automation Architecture Completed

- Reconciled architecture with completed GitHub Actions production automation.
- Added `.github/workflows/daily-intelligence.yml`.
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
- Recorded critical configuration failure validation.
- Recorded degraded source publication validation.
- Recorded concurrency protection.
- Recorded GitHub scheduler latency.
- Recorded scheduler-latency/report-window coupling as an open architecture decision.
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