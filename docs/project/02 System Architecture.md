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
- eight active real public RSS sources;
- nine active topic domains;
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
- concurrency protection;
- domains whose classification evidence comes entirely from validated source defaults;
- empty domain keyword lists where explicitly permitted;
- deterministic case-sensitive acronym handling.

Phase 3 automation architecture is complete.

Phase 4 has demonstrated two important architectural properties.

First:

> substantial source/domain expansion can usually be performed through configuration and existing pipeline components.

Examples:

```text
Sifted
→ Tech.eu

7 domains
→ 8 domains
→ Financial Markets added
```

Second:

> a new strategic macroarea can be implemented through the existing article pipeline even when lexical keywords are not the correct classification evidence.

Example:

```text
Tech Europe Foundation
→ standard RSS collection
→ standard ArticleRecord
→ source default
→ Milan and Bocconi Ecosystem
```

The current architectural priority remains:

> **continue improving the information layer through controlled source/domain changes, while avoiding new processing architectures until repeated evidence proves they are necessary.**

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

This was deliberately enabled for domains whose classification evidence may come entirely from validated source defaults.

Current example:

```text
Milan and Bocconi Ecosystem
keywords: []
```

This does not mean all domains should omit keywords.

It means:

> empty keyword sets are a supported configuration state when source identity provides better evidence than invented lexical rules.

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

---

## 5.4 `normalize.py`

Converts collected feed entries into a consistent article schema.

Responsibilities include:

- field extraction;
- title cleanup;
- URL cleanup;
- timestamp normalisation;
- description handling;
- deterministic record identity;
- source metadata preservation.

Publication timestamps are converted to timezone-aware UTC datetimes.

Record identity remains deterministic.

Normalisation should not perform:

- semantic classification;
- summarisation;
- enrichment;
- translation;
- entity extraction.

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

Examples:

```text
Istat
→ Economics and Macroeconomics

OpenAI News
→ Artificial Intelligence

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

The motivating example is:

```text
AI
```

Using lowercase:

```text
ai
```

caused false Artificial Intelligence classifications in Italian-language content because `ai` is an ordinary Italian word.

The case convention preserved historical English AI recall while removing false Italian matches.

This simple rule is preferred to introducing:

- language detection;
- NLP;
- stemming;
- machine learning.

### Empty-Keyword Domains

A domain may contain:

```yaml
keywords: []
```

and still be classifiable through a source default.

Current example:

```text
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
```

All current production collection routes use public structured RSS.

No current source requires:

- credentials;
- paid APIs;
- Bocconi authentication;
- premium article retrieval.

Current source architecture remains deliberately uniform:

```text
public structured feed
→ standard collector
→ standard normalizer
→ ArticleRecord
```

No active source currently requires a custom parser or source-specific processing branch.

---

# 7. Current Domain Architecture

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
Milan and Bocconi Ecosystem
```

Strategically approved but not yet implemented:

```text
Italy
```

Most domains use keyword evidence.

Milan and Bocconi Ecosystem currently demonstrates a second valid architecture:

```text
validated narrow source
→ source default
→ domain
```

with no generic topic keywords required.

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

---

# 9. Current Milan/Bocconi Architecture

Milan/Bocconi is no longer only a planned architecture.

The first production implementation is:

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

This architecture was chosen because TEF's information value comes from institutional identity, not because generic words such as:

```text
Milan
Bocconi
startup
event
```

would provide sufficiently precise evidence.

The implementation required only:

- one new source configuration;
- one new domain configuration;
- general support for empty domain keyword lists;
- configuration tests.

It did **not** require:

- event scraping;
- Bocconi authentication;
- a new opportunity data model;
- a deadline engine;
- a new ranking model;
- source-specific collector logic.

This is an important architectural precedent:

> use the existing article pipeline for professional-ecosystem sources until article semantics become demonstrably insufficient.

---

# 10. Current Real Integration Evidence

The TEF/Milan-Bocconi integration was tested with a full production-equivalent run.

Observed result:

```text
8 active sources
8 successful
0 failed
0 invalid

1295 valid records
40 inside the collection window
37 unique
29 unclassified
8 displayed

status: success
```

TEF itself collected:

```text
10 feed entries
```

No TEF records entered the processed 24-hour output because the feed entries were older than the monitored window.

This was expected.

The integration therefore validated:

- eighth-source collection;
- source-default configuration;
- ninth-domain configuration;
- normal pipeline execution;
- output generation;
- absence of stale TEF leakage.

---

# 11. Ranking and TEF Architecture

Typical TEF baseline score:

```text
Tier 1
= 4

Milan/Bocconi domain
= +2

total
= 6
```

A TEF story can receive additional domains and keyword matches if normal classifier evidence exists.

One tested story reached a higher score because it also matched Companies and Technology.

No special TEF ranking rule exists.

No ranking change was required because:

- TEF remains in its own primary report section;
- report selection caps that section at five items;
- current total report volumes remain well below the 30-item cap.

Do not lower TEF's source tier merely to manipulate relevance scores.

---

# 12. Collection Architecture

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

---

# 13. Network and Failure Architecture

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

# 14. Degraded-Run Architecture

A degraded run is legitimate when:

- one or more sources fail;
- enough successful source data remains to produce a meaningful output;
- the report and run summary expose the degraded state.

Degraded output is preferable to an invisible failure when partial information is still useful.

The report must not imply that all sources succeeded when they did not.

---

# 15. Automation Architecture

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

# 16. Scheduled-Execution Limitation

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

# 17. Persistence Architecture

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

Do not introduce external storage until repository-native persistence becomes a measured limitation.

---

# 18. Historical Regression Architecture

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
- Italian Tech Alliance candidate keywords.

This is the preferred validation mechanism before introducing more sophisticated evaluation infrastructure.

---

# 19. Report Architecture

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

# 20. Richer-Report Architecture

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

---

# 21. Premium-Source Architecture

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
→ technically excellent
→ persistence/licensing boundary insufficiently clean
→ standby
```

No premium publication is currently active through this exception.

---

# 22. Bank of Italy Structured-Data Architecture

Bank of Italy BDS exposed a potential future source class that does not fit the current article pipeline directly.

A statistical event architecture would conceptually require:

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

# 23. Opportunity and Deadline Architecture

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

# 24. Security and Privacy Architecture

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

# 25. Copyright and Content Boundaries

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

## Richer-Report Boundary

The richer-context requirement does not override copyright rules.

Objective:

> enough lawful context for initial understanding.

Not:

> reproduction of the source article.

---

# 26. Architecture for ChatGPT Use

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

The separation remains:

```text
Daily Intelligence System
= deterministic production infrastructure

ChatGPT
= external development and reasoning layer
```

The richer-report requirement does not automatically change this boundary.

---

# 27. Implemented vs Active vs Deferred Architecture

## Implemented and Validated

- Python package;
- repository-native configuration;
- eight-source public RSS registry;
- nine-domain active taxonomy;
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
- deterministic record IDs;
- structural validation;
- previous-24-hours publication filtering;
- exact deduplication;
- deterministic classification;
- empty source defaults;
- empty domain keyword support;
- validated source-defined domains;
- uppercase-sensitive keyword handling;
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
- Milan and Bocconi Ecosystem domain;
- Tech Europe Foundation source;
- conservative keyword regression workflow.

## Active Architectural Evaluation

- further source correction/expansion;
- dedicated Financial Markets source coverage;
- Companies/Corporate Strategy source coverage;
- Italy domain implementation;
- broader Milan/Bocconi source coverage;
- AI source diversity;
- Italian Tech Alliance production readiness;
- Nasdaq feed suitability;
- Federal Reserve feed suitability;
- MIMIT suitability;
- Lavoce.info suitability;
- Bruegel suitability;
- Assolombarda suitability;
- Ars Technica suitability;
- Google DeepMind suitability;
- source metadata richness;
- reporting-window cutoff independence;
- richer-report architecture after Phase 4.

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

# 28. Current Architectural Limitations

Known limitations include:

- current production universe contains only eight feeds;
- Financial Markets has no dedicated production source;
- Companies/Corporate Strategy remains weakly sourced;
- Italy is not yet an explicit implemented domain;
- Milan/Bocconi has only a first narrow production source;
- independent AI reporting remains limited;
- AI primary evidence is concentrated on OpenAI;
- Startups/VC depends heavily on Tech.eu;
- current active automated sources are mostly English-language;
- full bilingual classification remains only partially validated;
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
- repository-native storage creates strict copyright/persistence requirements for candidate sources.

These are maturity limits, not automatic implementation requirements.

---

# 29. Open Architecture Decisions

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

## Independent AI Architecture

Current working hypothesis:

```text
OpenAI
→ primary source

Google DeepMind
→ second primary source

independent technology source
→ reporting / interpretation
```

Status:

> source audit pending; no special architecture expected.

---

## Italy Architecture

Current working hypothesis:

```text
Istat
+ MIMIT
+ Lavoce.info
+ Assolombarda
+ Italian Tech Alliance
```

with Bank of Italy structured data later if justified.

Status:

> source validation pending.

This is an information architecture hypothesis, not an implemented technical architecture.

---

## Richer Report

Validated product need.

Architecture remains intentionally undefined until source/domain work reaches diminishing returns.

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

**Status: passed for current architecture; source universe still under active expansion**

Evidence:

- Sifted replaced by Tech.eu;
- Financial Markets added without new processing modules;
- classification regression workflow established;
- Italian keyword collision reproduced;
- classifier case behaviour corrected;
- Tech Europe Foundation added;
- ninth domain added;
- empty-keyword domain support added;
- source-defined classification validated;
- full real eight-source pipeline executed successfully.

This proves:

> the current architecture can support both ordinary keyword-defined domains and narrow source-defined domains without adding new processing layers.

What remains open is the **information universe**, not the basic expansion architecture.

---

## Gate F — Italy Architecture

**Status: not passed**

Required before considering Italy implementation complete:

- suitable source set;
- production-safe endpoints;
- classification/default decision;
- bilingual regression;
- report contribution review;
- no unnecessary source-specific architecture.

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
8 active public RSS sources
9 active domains

deterministic source defaults
deterministic keyword classification
source-defined domain support
deterministic keyword case semantics
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
Tech Europe Foundation
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
Milan and Bocconi Ecosystem
```

Current architectural direction:

```text
continue domain-gap-driven source correction
→ strengthen Financial Markets / Companies
→ validate Italy
→ broaden Milan/Bocconi where justified
→ diversify AI sources
→ stop expansion when marginal source value falls
→ design richer report context
```

Potential future architecture remains gated:

```text
Bank of Italy BDS
→ statistical-event pipeline only if justified

professional opportunities
→ state/deadline model only if justified

near-duplicate clusters
→ only after repeated report evidence
```

The architecture should remain simple unless actual report usage proves otherwise.

---

# Changelog

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
- Reframed Source/Domain Expansion Gate E as architecturally passed while information-universe expansion remains active.
- Added Bank of Italy BDS as the strongest validated future statistical-event architecture use case.
- Added opportunity/deadline state tracking as a future architecture gated by real Milan/Bocconi evidence.
- Added Italian Tech Alliance as a possible future near-duplicate evidence source without approving clustering.
- Updated active architectural evaluation to the new domain-gap-driven source queue.
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