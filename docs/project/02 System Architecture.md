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
- replacement or deferral of weak sources before disproportionate source-specific complexity;
- configuration-first source and domain changes where the existing pipeline already supports them;
- conservative classification over forced coverage;
- reuse of the existing `ArticleRecord` pipeline before introducing new record models;
- source-specific complexity only when information value independently justifies it;
- presentation-layer improvements before expanding persistence or content-ingestion architecture when the user need can be solved there.

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
- new processing paradigms introduced only to increase source count;
- generic ingestion of article-body-like feed fields without a validated persistence and product requirement.

---

# 2. Architectural Status

The core system is implemented as a repository-native deterministic production pipeline.

The current architecture supports:

- repository-native configuration loading;
- thirteen active real public RSS sources;
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
- explicitly labelled source-provided report context;
- bounded 500-character report context;
- deterministic sentence-aware report truncation;
- deterministic word-boundary fallback;
- explicit missing-context fallback;
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

Phase 4 source/domain architecture has been validated and the active source-expansion cycle reached its current MVP stopping point.

Phase 5 richer-report architecture design is complete.

Phase 6 richer-report implementation has been locally validated.

Phase 4 demonstrated five important architectural properties.

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

ISPI Geoeconomics
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

Fourth:

> a strategically strong source should still be rejected or deferred if integration would require disproportionate source-specific filtering, timestamp recovery or persistence logic.

Examples:

```text
DG Competition
→ high-value M&A / antitrust signal
→ broad feed creates ranking/classification noise
→ no source-specific filtering layer added

ESMA
→ high-value Financial Markets signal
→ timestamps embedded in HTML
→ long feed bodies distort classification
→ no source-specific date-recovery or description pipeline added

ISPI Business Events
→ high-value events
→ publication time does not equal actionability/event time
→ no event/deadline architecture added
```

Fifth:

> endpoint and access limitations can legitimately define the current architecture ceiling for a domain.

Examples:

```text
Bocconi Career Services
→ high strategic value
→ authenticated/manual boundary retained

Fintech District
→ no clean RSS/API
→ no hidden Next.js API reverse engineering

Camera di Commercio Milano
→ machine access returns Incapsula interstitials
→ no access-control bypass

Assolombarda
→ missing usable publication timestamps
→ no source-specific date recovery
```

Phase 5 and Phase 6 added a sixth architectural property:

> a validated information-quality problem should be solved at the narrowest layer that can satisfy the user need.

For richer report context:

```text
existing ArticleRecord.description
→ report-only formatting improvement
```

was sufficient.

The implementation therefore did not introduce:

- a new record model;
- a new persisted context field;
- generic RSS `content` ingestion;
- article-page scraping;
- LLM summarisation;
- new classification evidence;
- new ranking evidence.

The active architectural priority is now:

> **preserve the validated thirteen-source / ten-domain deterministic pipeline, keep the richer-report implementation as a presentation-layer extension of the existing `ArticleRecord` architecture, and reopen source or advanced architecture only against demonstrated product gaps.**

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

The richer-report implementation remains inside the same report-rendering path.

There is no parallel enrichment pipeline.

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

The richer-report implementation deliberately preserves:

```text
ArticleRecord.description
```

as the only production field used for source-provided descriptive context.

No separate:

```text
context
summary
report_context
```

field has been added.

Do not introduce a separate event, opportunity, statistical or enriched-context record model without a validated requirement.

Recent source audits strengthen this constraint rather than weaken it.

ISPI Business Events and Bocconi Career Services demonstrate that event and opportunity semantics can differ materially from article semantics.

That evidence is sufficient to document the limitation.

It is not yet sufficient to justify a second production record model.

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

ISPI Geoeconomics reinforces the opposite case:

```text
valid strategically narrow source
→ no default domain required
→ existing taxonomy remains sufficient
```

Configuration should not force a source default merely because a source has a thematic identity.

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

Recent source audits reinforce this:

```text
DG Competition
→ generic collector already works
→ product-quality problem is not collection

ESMA
→ generic collector works
→ metadata shape is unsuitable downstream

Fintech District
→ no clean feed/API
→ do not reverse-engineer application internals

Camera di Commercio Milano
→ protected machine access
→ do not bypass access control
```

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

Publication timestamps are converted to timezone-aware UTC datetimes when the feed exposes suitable structured date fields.

Record identity remains deterministic.

### HTML Description Normalisation

Phase 4 added generic HTML-to-text handling after MIMIT exposed feed descriptions containing HTML markup.

The current normalization path is:

```text
feed description
→ HTML-to-text cleanup
→ whitespace cleanup
→ normalized text
→ None if no meaningful text remains
```

This behaviour is generic.

It is not tied to MIMIT or any other individual source.

The change followed the architectural rule:

> when a source exposes a genuine general parsing defect, fix the common normalization layer rather than branching on source identity.

### Richer-Report Boundary

Phase 6 did **not** modify description normalization.

The richer-report implementation consumes the description produced by the existing normalizer.

Architecture:

```text
normalize once
→ use normalized description for deterministic article evidence
→ persist it
→ format it separately for report presentation
```

This prevents report-display requirements from silently changing classification and ranking semantics.

### Source-Provided Malformation Boundary

The Phase 6 production validation exposed apparent spacing defects in some displayed text.

Controlled diagnostics established two different cases.

BBC/OpenAI examples:

```text
raw feed
→ correct spacing

normalizer
→ correct spacing

persisted JSONL
→ correct spacing

Markdown file
→ correct spacing
```

The apparent joined words were caused by terminal/paste presentation rather than the production pipeline.

Tech.eu examples showed:

```text
malformed spacing
→ already present in raw RSS description
```

The architecture therefore did **not** add speculative generic word-repair heuristics.

This reinforces:

> do not modify shared normalization logic until the defect is demonstrated to originate in that logic.

### Timestamp Boundary

The ESMA audit demonstrated an important limit.

ESMA entries contain publication dates inside embedded HTML while standard RSS `published` / `updated` fields are absent.

The existing normalizer correctly does **not** scrape arbitrary HTML fragments to synthesize a publication timestamp.

Current architecture therefore remains:

```text
structured feed timestamp
→ normalize

missing structured timestamp
→ published_at = None
→ later excluded from current-window processing
```

Do not add a source-specific ESMA date parser.

A generic embedded-date fallback may be reconsidered only if several strategically valuable sources independently justify it.

Normalisation should still not perform:

- semantic classification;
- summarisation;
- translation;
- entity extraction;
- source-specific article-body extraction;
- speculative reconstruction of malformed publisher text.

---

## 5.5 `validate.py`

Rejects structurally unusable normalised records.

Validation currently checks required fields and record integrity.

Validation is intentionally structural rather than semantic.

A record can be structurally valid but later:

- have no eligible publication timestamp;
- remain unclassified;
- fail to enter the current report.

That is acceptable.

ESMA demonstrated this distinction:

```text
records normalized
+
no usable structured publication time
→ structurally valid but not current-window eligible
```

Structural normalization success is therefore not equivalent to production eligibility.

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

Multiple audits reinforce this design.

Assolombarda and ESMA both demonstrated that a technically collectable source without suitable structured publication timestamps is not automatically compatible with the current production architecture.

The correct architectural response remains:

```text
do not activate source
```

rather than:

```text
replace publication time with retrieval time
```

or:

```text
introduce a source-specific page/date parser
```

Known limitation:

GitHub Actions scheduling can start later than the nominal schedule, so the rolling 24-hour window moves with actual execution.

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

Italian Tech Alliance testing exposed a plausible use case where multiple press-clipping entries may describe the same underlying development.

That remains insufficient evidence for architectural expansion because:

- Italian Tech Alliance is not active;
- the problem has not yet degraded repeated production reports;
- upstream source selection remains simpler than clustering.

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

Broad or analytically heterogeneous sources may have no defaults.

Examples:

```text
BBC World
BBC Business
ECB
European Commission
Tech.eu
ISPI Geoeconomics
```

ISPI is intentionally active without a source default.

Its useful records should classify only when existing article-level evidence supports them.

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

The same mechanism supports:

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

### Long-Description Classification Risk

The ESMA audit exposed another architectural constraint.

When feeds expose long page-body-like descriptions:

```text
long description
→ many incidental keywords
→ extra domains
→ extra relevance score
```

The architecture should not solve this with source-specific exclusions.

Preferred responses are:

1. use a cleaner source/endpoint;
2. improve a generic metadata boundary if independently justified;
3. keep the source on standby.

This risk is one reason the richer-report implementation does not copy long RSS `content` fields into `ArticleRecord.description`.

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

The DG Competition audit demonstrated this directly.

The architectural response was:

```text
do not activate the broad feed
```

rather than:

```text
add a source-specific ranking penalty
```

This reinforces:

> fix source evidence before ranking complexity.

The richer-report implementation does not affect relevance scoring because report formatting occurs after classification and ranking.

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

The public persistence model remains an architectural source-selection gate.

A technically accessible source can still be unsuitable if it exposes:

- excessive article body text;
- content with unclear persistence rights;
- private/authenticated content.

### Richer-Report Persistence Boundary

Phase 6 does not change JSONL persistence semantics.

The report uses the same persisted normalized:

```text
description
```

field.

The system does not persist a separate enlarged report context.

Therefore:

```text
500-character report display limit
≠
500-character persistence limit
```

The existing normalized description remains stored as before.

The 500-character bound applies only when rendering the Markdown report.

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

### Source-Context Rendering

Phase 6 extends only the report presentation layer.

The existing normalized:

```text
ArticleRecord.description
```

remains the source of report context.

The report renders it explicitly as:

```text
**Source context:** ...
```

Current maximum display length:

```text
500 characters
```

Formatting behaviour is deterministic:

```text
description missing
or description == title
→ explicit no-context fallback

length <= 500
→ render unchanged

length > 500
→ prefer a complete sentence within the bound
→ otherwise truncate at the last word boundary
→ append ... only for word-boundary truncation
```

Current fallback text:

```text
No additional source-provided context available.
```

This mechanism does not:

- mutate `ArticleRecord.description`;
- add a new context field;
- change classification evidence;
- change ranking evidence;
- change JSONL persistence semantics;
- use feed `content` fields;
- fetch article pages;
- call an LLM.

The richer-report implementation is therefore a bounded presentation-layer transformation rather than a new content-ingestion architecture.

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

Phase 6 preserves this single pipeline.

No enrichment orchestration stage was added.

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
ISPI Geoeconomics
```

All current production collection routes use public structured RSS.

No current active source requires:

- credentials;
- paid APIs;
- Bocconi authentication;
- premium article retrieval;
- custom HTML scraping;
- source-specific collectors;
- hidden application APIs.

Current active source architecture remains deliberately uniform:

```text
public structured feed
→ standard collector
→ standard normalizer
→ ArticleRecord
```

ISPI Geoeconomics follows exactly this path.

Its integration required:

- source configuration;
- configuration tests.

It did **not** require:

- a source default;
- new keywords;
- a new parser;
- a new record model;
- a ranking exception;
- a custom persistence path.

This remains a strong architectural success criterion for future source expansion.

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

All ten strategic macroareas are implemented.

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

All ten domains are sufficient for the current MVP boundary.

This does not mean all ten are equally mature.

Known maturity limits include:

- broader Financial Markets;
- global Companies/Corporate Strategy;
- independent AI/Technology scrutiny;
- independent Europe analysis;
- Startups/VC diversity;
- professional/recruiting depth in Milan/Bocconi.

These are information-universe limitations rather than missing domain architecture.

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
  max_description_length: 500
```

`max_description_length` remains the historical configuration name.

Its current role is:

```text
maximum rendered Source context length
```

It does not alter the stored `ArticleRecord.description`.

Configuration remains preferred over code changes when source/domain additions fit the current processing model.

The Federal Reserve, Lavoce.info, Google DeepMind and ISPI integrations required no production Python changes.

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

### Current Architecture Ceiling

The Phase 4 Milan/Bocconi audits provide direct evidence around the remaining roles.

```text
Bocconi Career Services
→ public professional information exists
→ actionable layer partly authenticated
→ no narrow structured public feed established

Assolombarda
→ strong company / industrial value
→ publication-time / persistence incompatibility

Fintech District
→ strong finance / fintech ecosystem fit
→ no usable RSS/API established

Camera di Commercio Milano
→ strong local-business value
→ Incapsula/Imperva machine-access barrier

Italian Tech Alliance
→ structured RSS
→ thin/repetitive press-clipping
→ weak fit as a source-wide Milan/Bocconi sensor
```

The architectural conclusion is:

> the current Milan/Bocconi limitation is no longer evidence that a new source should automatically be added.

Instead, several remaining information roles would require:

- authenticated systems;
- custom scraping;
- access-control workarounds;
- event/deadline semantics;
- source-specific normalization.

Those are not justified for the MVP.

This remains an important architectural precedent:

> use the existing article pipeline for professional-ecosystem sources until repeated real use demonstrates that article semantics are insufficient.

---

# 10. Current Italy Architecture

Italy is implemented through the standard article pipeline.

Current architecture:

```text
Istat
→ Economics/Macro default

MIMIT News
→ Italy default

Lavoce.info Imprese
→ Italy default

ISPI Geoeconomics
→ selective classification through article evidence
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

for validated Italy-focused sources, while narrow bilingual keywords provide additional topical domains.

ISPI is different:

```text
Italian-language source
≠ automatic Italy classification
```

It uses no Italy source default because its feed is geoeconomic and geographically broader.

The implementation required:

- one dedicated domain;
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

No DeepMind-specific keywords or ranking rules were needed.

ISPI Geoeconomics can also produce AI/Technology records through ordinary keyword evidence.

This provides selective interpretative spillover without a source default.

The architectural AI problem is therefore no longer:

```text
how to add a second primary lab
```

It is:

```text
whether a clean independent reporting source can later be added
without special architecture
```

No special AI processing layer is justified.

---

# 12. Current Real Integration Evidence

The Phase 4 production checkpoint validated thirteen active sources and ten active domains.

The Phase 6 richer-report implementation was then validated against the same production architecture.

Latest local production-equivalent validation on 19 August 2026:

```text
13 active sources
13 successful
0 failed
0 invalid

1448 valid records
50 inside collection window
45 unique
28 unclassified

status: success
```

The exact inside-window, unique, unclassified and displayed counts can vary between same-day runs because the monitored window ends at actual execution time.

The important architectural result is:

```text
same 13-source collection architecture
+
same ArticleRecord processing model
+
same deterministic classification/ranking/storage semantics
+
richer report presentation
→ successful production-equivalent run
```

The full automated test suite passed:

```text
122 passed
```

Targeted report validation passed:

```text
14 passed
```

Targeted feed-fixture validation passed:

```text
20 passed
```

The richer-report validation additionally confirmed:

- source context can be rendered without a new record field;
- short descriptions remain unchanged;
- missing descriptions receive an explicit fallback;
- title-duplicate descriptions are not repeated;
- sentence-aware truncation remains deterministic;
- word-boundary fallback avoids mid-word cuts;
- report caps remain unchanged;
- classification/ranking output semantics remain unchanged;
- no RSS body-content field is required;
- no article-page retrieval is required;
- no production AI dependency is introduced.

A diagnostic review also separated two different text-quality cases:

```text
BBC / OpenAI examples
→ raw feed text correct
→ normalized text correct
→ persisted JSONL correct
→ Markdown file correct
→ apparent joined words were terminal/paste display artefacts

Tech.eu examples
→ malformed spacing already present in raw RSS description
→ source-quality limitation
→ no speculative generic text-repair heuristic added
```

This reinforces the architecture rule:

> only change a shared processing layer when the observed defect actually originates there and the correction is justified by evidence.

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
information-function validation
→ endpoint research
→ direct technical probe
→ production collector test
→ normalizer test
→ classification/ranking test
→ configuration integration
```

Do not add source-specific collector modules unless unavoidable and independently justified by source value.

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

DG Competition
→ collector works
→ feed breadth/product quality fails
→ no source-specific filter added

ESMA
→ collector works
→ metadata shape fails downstream
→ no special date parser added

Fintech District
→ no clean feed/API
→ no Next.js reverse engineering

Camera di Commercio Milano
→ machine access blocked/interstitial
→ no bypass
```

The architecture should reject or defer incompatible sources rather than accumulate exceptions.

---

# 14. Network and Failure Architecture

Remote source retrieval can fail because of:

- DNS/network errors;
- HTTP errors;
- TLS errors;
- timeouts;
- malformed feeds;
- endpoint changes;
- access-control responses.

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

Access-control interstitials should not be treated as usable structured content merely because they return HTTP `200`.

The Camera di Commercio audit reinforces this distinction.

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

Persistence architecture creates an important source-selection constraint.

A public feed can still be unsuitable when it exposes:

```text
substantial article text
or
effectively complete publication bodies
```

Bruegel demonstrated this failure mode.

ESMA demonstrated a related product-quality problem:

```text
large normalized feed descriptions
→ incidental classification evidence
→ ranking distortion
```

Therefore:

> feed accessibility, metadata quality and persistence compatibility are independent gates.

The Phase 5 metadata audit strengthens this boundary.

Some active sources expose body-like RSS `content` fields containing thousands of characters.

Those fields are not part of the current production persistence architecture.

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

This approach has been used for:

- Tech.eu keyword refinement;
- Financial Markets;
- `startup` removal;
- Italian-source classification;
- `AI` case matching;
- Italian Tech Alliance candidate keywords;
- Federal Reserve Financial Markets keywords;
- MIMIT Italian keywords;
- Lavoce.info bilingual keywords;
- ISPI geoeconomic candidate keyword review;
- DG Competition ranking comparison.

This remains the preferred validation mechanism before introducing more sophisticated evaluation infrastructure.

---

# 20. Report Architecture

The report remains intentionally simple Markdown.

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
- explicitly labelled source-provided context.

GitHub-hosted Markdown remains sufficient as the current delivery interface.

Do not build a frontend until repository browsing becomes a demonstrated usability problem.

Current report bounds are:

```text
maximum items per domain = 5
maximum total items      = 30
maximum source context   = 500 characters
```

The richer-context change does not alter report-selection caps.

The architecture intentionally separates:

```text
selection / ranking
```

from:

```text
presentation of already-selected source context
```

This prevents richer display text from silently changing which stories are selected.

---

# 21. Richer-Report Architecture

The richer-report architecture is implemented and locally validated.

Validated user need:

> reports should provide enough context to understand major developments without immediate click-through when source metadata permits it.

The accepted architecture is:

```text
existing normalized ArticleRecord.description
→ report-only source-context formatter
→ explicit provenance label
→ bounded deterministic rendering
```

Current provenance label:

```text
Source context
```

Current display limit:

```text
500 characters
```

## 21.1 Why 500 Characters

The Phase 5 metadata audit found that 300 characters was not the dominant context limitation across most sources.

However, the 300-character cap unnecessarily truncated useful source descriptions from sources including:

```text
Tech Europe Foundation
Lavoce.info Imprese
some ISPI Geoeconomics items
```

The audit showed approximately:

```text
TEF
→ descriptions commonly around 450–550 characters

Lavoce.info Imprese
→ descriptions around 330–360 characters

ISPI Geoeconomics
→ some descriptions above 300 characters
```

A 500-character bound was selected because it materially improves those cases while keeping entries bounded and avoiding a generic expansion into article-body text.

A 600-character bound was not necessary to satisfy the validated need.

The report item-count caps remain unchanged because historical reports were well below the existing 30-item maximum and richer context should be evaluated before increasing breadth.

---

## 21.2 Deterministic Formatting

Current behaviour:

```text
if description is missing
or normalized description equals title
→ No additional source-provided context available.

if description length <= max length
→ render unchanged

if description length > max length
→ prefer a complete sentence that fits within the bound
→ otherwise use the final word boundary
→ append ... for word-boundary truncation
```

The formatter does not generate new factual content.

The implementation is deterministic and testable.

---

## 21.3 Provenance

The report uses:

```text
**Source context:**
```

rather than:

```text
Summary
```

because the text is publisher/source-provided metadata.

Depending on the source, it may represent:

- a summary;
- an abstract;
- a teaser;
- a short description.

The system does not claim that it is:

- independently written analysis;
- an AI-generated summary;
- a verified article-body synopsis.

This preserves transparent provenance.

---

## 21.4 Persistence and Evidence Boundary

The richer-report implementation deliberately does **not** enrich `ArticleRecord.description` from feed `content` fields.

Phase 5 source auditing found materially richer `content` fields for some sources, including:

```text
Istat
Tech.eu
Tech Europe Foundation
ISPI Geoeconomics
```

These fields can contain thousands of characters and behave more like article bodies than bounded metadata.

Using them generically would introduce two architectural risks:

```text
larger persisted copyrighted payloads
+
more text entering deterministic classification/ranking
```

The existing description therefore remains the shared classification, ranking and persistence evidence field.

The richer report transforms only how that existing field is displayed.

This distinction is important:

```text
classification / ranking / storage
→ existing normalized description

report presentation
→ bounded formatting of that same description
```

---

## 21.5 Thin-Metadata Behaviour

Some feeds expose little or no usable description metadata.

Examples identified during the audit include:

```text
ECB
→ no usable description in tested items

Federal Reserve
→ descriptions often title-like

Google DeepMind
→ description availability partial
```

The current architecture handles this transparently rather than inventing context.

Fallback:

```text
No additional source-provided context available.
```

This fallback also creates a visible signal for whether future enrichment is genuinely needed.

---

## 21.6 Source-Quality Boundary

The richer-report implementation does not include generic speculative repair of publisher text.

Tech.eu testing demonstrated descriptions where malformed spacing already existed in the raw feed.

The architecture preserves source-provided metadata rather than guessing word boundaries.

A future source-specific or generic repair should require evidence that:

- the defect originates in a deterministic transformation controlled by the system; or
- a safe generic correction is supported across multiple valuable sources.

---

## 21.7 Rejected Richer-Context Alternatives

The following were considered and rejected or deferred for the current MVP:

```text
300 → 600 character increase only
→ broader than necessary
→ does not solve thin metadata

generic RSS content ingestion
→ body-like payload and persistence/classification risk

article-page metadata extraction
→ deferred
→ no validated need after simpler solution

first-paragraph / article-body extraction
→ unnecessary complexity and copyright risk

LLM summaries
→ recurring dependency, cost and provenance complexity

new ArticleRecord context field
→ unnecessary
→ existing description is sufficient for current requirement
```

The accepted architecture is therefore intentionally smaller than the alternatives considered.

---

## 21.8 Acceptance Boundary

The architecture is considered validated because:

- report-specific tests pass;
- the complete deterministic test suite passes;
- a production-equivalent run succeeds across all thirteen active sources;
- real report output was inspected;
- report context is materially richer where source metadata permits it;
- report length remains bounded;
- provenance is explicit;
- classification/ranking/storage semantics remain stable;
- no new paid or AI-dependent production mechanism was introduced.

Future context enrichment should reopen only when repeated report use demonstrates that bounded feed descriptions still create material information loss.

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

Richer-report work does not alter this boundary.

The pipeline must not fetch premium article bodies merely to improve report context.

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

- current article-source coverage is sufficient for the MVP boundary;
- event-generation semantics have not been designed;
- significance thresholds have not been validated;
- additional state would be required;
- no current evidence shows this has higher value than using and evaluating the completed richer-report architecture.

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

The Phase 4 audits provide repeated evidence that:

```text
publication date
≠
deadline
≠
event date
```

Examples:

```text
ISPI Business Events
Bocconi Career Services
```

This evidence validates the architectural limitation.

It does **not** yet validate implementation of a second stateful model.

A stateful opportunity/deadline architecture should be introduced only if repeated real usage shows that the current publication-based model causes meaningful opportunities to disappear before they are useful.

Do not create an opportunity database merely because the Milan/Bocconi domain is strategically important.

The current Milan/Bocconi MVP boundary accepts some manual/private opportunity discovery rather than forcing incompatible data into `ArticleRecord`.

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

The same conservative policy applies to anti-bot/access-control systems.

Do not:

- bypass Incapsula/Imperva;
- automate hidden authentication;
- impersonate logged-in sessions;
- reverse-engineer private application interfaces.

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

## Long-Metadata Boundary

Even when persistence rights are less problematic, unusually long feed descriptions can create another architectural problem:

```text
long page-like description
→ irrelevant keyword matches
→ classification inflation
→ ranking inflation
```

ESMA validated this risk.

The richer-report implementation therefore distinguishes:

```text
more useful presentation context
```

from:

```text
persisting larger feed bodies
```

## Richer-Report Boundary

The richer-context requirement does not override copyright rules.

Current production remains limited to source-provided descriptions already carried through the standard `ArticleRecord` pipeline.

The report may display up to:

```text
500 characters
```

from that existing description field.

The implementation does not generically persist or render body-like RSS `content` payloads.

Objective:

> enough lawful source-provided context for initial understanding.

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
- thirteen-source public RSS registry;
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
- UTC-aware timestamps when structured publication dates exist;
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
- explicit `Source context` provenance;
- 500-character bounded report context;
- deterministic sentence-aware source-context truncation;
- deterministic word-boundary fallback;
- explicit missing/title-duplicate context fallback;
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
- ISPI Geoeconomics source;
- conservative bilingual keyword regression workflow;
- configuration-only source expansion when the standard article architecture fits.

## Active Architectural Evaluation

No new architecture project is automatically active after the richer-report checkpoint.

The next architecture change should be triggered by observed use.

Potential evidence areas include:

- whether bounded source context remains too thin in repeated real reports;
- whether reporting-window cutoff dependence causes meaningful missed coverage;
- whether same-story duplication materially harms reading quality;
- whether opportunity/deadline semantics create real missed-opportunity cost;
- whether source-health history becomes necessary for maintenance.

Residual information-function gaps remain documented but are not active architecture projects unless new evidence emerges:

- global Companies/Corporate Strategy coverage;
- broader Financial Markets source coverage;
- independent AI/Technology reporting;
- independent Europe/EU interpretation;
- Startups/VC diversification;
- broader Milan/Bocconi and Milan/Lombardy coverage.

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
- article-page context extraction;
- generic RSS body-content ingestion;
- LLM summarisation;
- authenticated premium ingestion;
- authenticated Bocconi ingestion;
- source-specific ranking rules;
- source-specific publication-date recovery;
- speculative source-text repair;
- hidden/internal API reverse engineering;
- access-control bypass;
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

- the current production universe contains thirteen feeds but does not provide complete information-function coverage;
- Financial Markets is stronger on monetary/rates evidence than broader capital markets and market structure;
- Companies/Corporate Strategy still lacks a strong international dedicated reporting source;
- Milan/Bocconi has meaningful automated ecosystem coverage but remains incomplete for recruiting, employer events and established-company intelligence;
- several Milan/Bocconi complements are blocked by authentication, endpoint quality, event semantics or access controls;
- Milan/Lombardy established-company coverage remains incomplete;
- independent AI/technology reporting remains unresolved;
- primary AI evidence is diversified across OpenAI and DeepMind;
- Startups/VC depends heavily on Tech.eu for deal/company coverage;
- Europe/EU independent analytical depth remains incomplete despite ISPI improvement;
- active automated sources remain majority English-language;
- bilingual deterministic classification is validated but deliberately conservative;
- exact deduplication does not detect differently worded coverage of the same story;
- records without publication timestamps are excluded;
- ranking remains intentionally simple;
- classification remains conservative;
- strategically useful records can remain unclassified;
- long feed descriptions can create incidental keyword inflation;
- no entity enrichment exists;
- no article-level geography exists;
- no content-type classification exists;
- no statistical-event processing exists;
- no opportunity-state model exists;
- no deadline persistence exists;
- no long-term source-health database exists;
- report source context remains bounded at 500 characters and therefore cannot create information that the source does not provide;
- some sources provide no description, title-like descriptions or malformed publisher metadata;
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

> Do active sources eventually create enough repeated same-story coverage to justify clustering?

Status:

> deferred pending repeated production evidence.

Italian Tech Alliance provided useful test evidence but is not itself enough to justify implementation.

---

## Statistical Events

Question:

> Should official statistical series such as Bank of Italy BDS generate deterministic intelligence events?

Status:

> validated future use case, architecture not approved for implementation.

---

## Opportunity State

Question:

> Do Milan/Bocconi opportunities need deadline/event-state persistence rather than publication-only treatment?

Evidence:

```text
ISPI Business Events
Bocconi Career Services
```

shows that article publication semantics can be insufficient.

Status:

> deferred pending real user-cost evidence.

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

> information role remains open; no special architecture justified.

Ars Technica was audited and rejected under current persistence constraints.

Future source work should reopen only if report use demonstrates a meaningful gap or a materially cleaner endpoint appears.

---

## Italy Architecture

Current implemented architecture:

```text
Istat
+ MIMIT News
+ Lavoce.info Imprese
+ selective ISPI spillover
```

with Bank of Italy structured data later if justified.

Status:

> implemented and architecturally validated for the current MVP.

Assolombarda and Italian Tech Alliance remain possible complementary roles, but neither is required to consider the basic Italy architecture sufficient.

---

## Milan/Bocconi Architecture

Current implemented architecture:

```text
Tech Europe Foundation
→ Milan/Bocconi source-default classification
→ standard ArticleRecord pipeline
```

Known complementary roles remain:

```text
recruiting
employer events
finance ecosystem
established firms
industrial ecosystem
opportunities/deadlines
```

Current audit evidence shows that major candidate sources are limited by:

- authentication;
- missing structured endpoints;
- timestamp/event semantics;
- access-control barriers;
- product-quality limitations.

Status:

> MVP-sufficient but deliberately incomplete.

Do not create a new event/opportunity pipeline solely to increase nominal domain completeness.

---

## Metadata-Only Source Path

Question:

> Should the system eventually support deliberately title/link/date-only persistence for strategically important sources whose description fields cannot safely be stored?

Status:

> not approved.

Current evidence from Bruegel, Ars Technica and Assolombarda remains insufficient to justify a second persistence path.

Prefer source replacement or standby unless several high-value sources demonstrate the same need and real product value is high.

---

## Source-Specific Date Recovery

Question:

> Should publication dates ever be recovered from embedded HTML or article pages when RSS timestamps are missing?

Status:

> not approved.

Assolombarda and ESMA did not justify such a branch.

Publication-time semantics remain strict.

A future generic fallback would require cross-source evidence.

---

## Source-Specific Filtering

Question:

> Should broad feeds support publisher-specific inclusion or exclusion rules?

Status:

> not approved.

DG Competition demonstrated a plausible use case.

The current decision remains:

> reject or defer a noisy broad source rather than introduce source-specific classification/ranking policy solely to make it usable.

---

## Richer Report

Validated and implemented.

Current architecture:

```text
ArticleRecord.description
→ report-only formatter
→ Source context provenance
→ 500-character bound
→ sentence-aware truncation
→ word-boundary fallback
→ explicit no-context fallback
```

Status:

> **architecture gate passed and implementation locally validated.**

No additional context-ingestion architecture is approved.

Reopen this decision only if repeated real report use demonstrates that source-provided descriptions remain materially insufficient.

Potential future escalation order remains:

1. better public structured metadata;
2. source replacement;
3. narrowly justified public article metadata extraction;
4. more complex methods only if simpler options fail.

Generic RSS body-content ingestion and LLM summarisation remain deferred.

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
- usable timestamps for active sources;
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

**Status: passed and current active expansion cycle closed**

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
- ISPI Geoeconomics added;
- bilingual classification validated;
- generic HTML description normalization added;
- full real thirteen-source pipeline executed successfully.

This proves:

> the current architecture can support ordinary keyword-defined domains, narrow source-defined domains, multilingual deterministic classification and clean configuration-driven source expansion without new processing layers.

The Phase 4 audits also proved that the architecture can **refuse** strategically attractive sources when they would require disproportionate exceptions.

What remains open is information maturity, not basic source/domain expansion architecture.

---

## Gate F — Italy Architecture

**Status: passed**

Evidence:

- dedicated Italy domain implemented;
- suitable public source set validated;
- Istat + MIMIT + Lavoce provide differentiated roles;
- MIMIT and Lavoce.info use validated Italy source defaults;
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

**Status: passed**

The richer-report design and implementation gate is complete for the current MVP.

Validated design decisions:

- source-provided description remains the context source;
- no new `ArticleRecord` field;
- no generic RSS `content` ingestion;
- no article-page scraping;
- no LLM summarisation;
- explicit `Source context` provenance;
- 500-character display bound;
- sentence-aware deterministic truncation;
- word-boundary fallback;
- transparent missing/title-duplicate fallback;
- report item caps remain unchanged;
- classification/ranking/storage semantics remain unchanged.

Validation evidence:

```text
20 feed-fixture tests passed
14 report tests passed
122 full-suite tests passed
13/13 active sources successful in production-equivalent run
0 invalid records
git diff --check clean
report output generated and manually inspected
```

The gate demonstrates:

> the existing `ArticleRecord` and persistence architecture can support materially richer report context through a small presentation-layer change.

Future enrichment is not automatically approved.

Reopen only if repeated report use demonstrates a material remaining context problem that the current bounded metadata approach cannot solve.

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
- advanced ranking;
- article-page context enrichment.

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
13 active public RSS sources
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

Current report architecture:

```text
existing ArticleRecord.description
→ explicit Source context label
→ 500-character display bound
→ sentence-aware truncation
→ word-boundary fallback
→ explicit no-context fallback
```

The richer-report layer is presentation-only:

```text
no new record model
no new persisted context field
no generic RSS body-content ingestion
no article-page scraping
no LLM summarisation
no classification/ranking expansion
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
ISPI Geoeconomics
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
preserve the 13-source / 10-domain production architecture
→ preserve ArticleRecord as the single production record model
→ preserve bounded deterministic report context
→ observe real report use
→ reopen source or architecture work only against demonstrated product cost
```

Potential future architecture remains gated:

```text
Bank of Italy BDS
→ statistical-event pipeline only if justified

professional opportunities
→ state/deadline model only if real use justifies it

near-duplicate clusters
→ only after repeated production-report evidence

metadata-only persistence
→ only if multiple high-value sources justify it

article-page context extraction
→ only if bounded feed context proves materially insufficient

source-specific date recovery
→ not approved

source-specific ranking/filtering
→ not approved
```

The architecture should remain simple unless actual report usage proves otherwise.

---

# Changelog

## 2026-08-19 — Richer-Report Architecture Implemented and Validated

- Closed richer-report Architecture Gate G for the current MVP.
- Preserved `ArticleRecord.description` as the only production context field.
- Increased configured report context display bound from 300 to 500 characters.
- Added explicit `Source context` provenance in report rendering.
- Added transparent fallback when source context is missing or duplicates the title.
- Added deterministic sentence-aware truncation with word-boundary fallback.
- Kept maximum report breadth unchanged at 5 items per domain and 30 items total.
- Confirmed the richer-report change is presentation-only and does not alter classification, ranking or JSONL persistence semantics.
- Rejected generic use of RSS `content` fields after metadata auditing showed body-like payloads for several sources.
- Kept article-page extraction, first-paragraph extraction and LLM summarisation deferred.
- Confirmed source metadata limitations remain visible rather than being hidden by fabricated or speculative repair.
- Diagnosed apparent BBC/OpenAI spacing defects and confirmed raw feeds, normalized descriptions, persisted JSONL and Markdown files were correct; terminal/paste presentation caused the apparent joining.
- Confirmed malformed Tech.eu spacing is already present in raw RSS descriptions and did not add speculative generic word-repair logic.
- Validated the implementation with:
  - 20 feed-fixture tests passed;
  - 14 report tests passed;
  - 122 full-suite tests passed;
  - clean `git diff --check`;
  - successful production-equivalent run across all 13 active sources;
  - 0 invalid records;
  - manual inspection of generated report output.
- Reframed future architecture work as evidence-triggered rather than automatically proceeding to another feature or source-expansion phase.

## 2026-08-18 — Thirteen-Source / Phase-4 Closure Architecture Checkpoint

- Reconciled architecture with the validated thirteen-source / ten-domain production state.
- Added ISPI Geoeconomics to the active source architecture.
- Recorded ISPI as a configuration-only integration requiring no source-specific parser, record model or ranking exception.
- Recorded successful ISPI real-collector and normalization testing.
- Recorded that stale ISPI records did not leak into current-window output.
- Preserved `ArticleRecord` as the only production record model.
- Kept opportunity/deadline architecture deferred.
- Recorded DG Competition as evidence against source-specific ranking/filtering.
- Recorded ESMA as evidence against source-specific timestamp recovery.
- Recorded Italian Tech Alliance as evidence that technically clean feeds may still fail product-quality thresholds.
- Recorded Bocconi Career Services as evidence that valuable professional information may legitimately remain manual/private where the actionable layer is authenticated.
- Recorded Fintech District as evidence against reverse-engineering hidden application APIs.
- Recorded Camera di Commercio Milano as evidence against bypassing access-control systems.
- Reframed Milan/Bocconi architecture as MVP-sufficient but deliberately incomplete.
- Closed the active Phase 4 source-expansion architecture cycle.
- Moved richer-report architecture into the next active design gate.

## 2026-08-18 — Twelve-Source / Ten-Domain Architecture Checkpoint

- Added Federal Reserve Board Monetary Policy.
- Added MIMIT News.
- Added Lavoce.info Imprese.
- Added Google DeepMind News.
- Added Italy as the tenth implemented domain.
- Recorded Italy as a source-defined empty-keyword domain.
- Recorded MIMIT and Lavoce.info Italy source defaults.
- Recorded bilingual deterministic keyword classification as production-validated.
- Added the intentional uppercase Italian AI acronym `IA`.
- Added generic HTML-to-text feed-description normalization after MIMIT exposed a general normalization requirement.
- Recorded Google DeepMind as the second Tier 1 frontier-lab source.
- Marked Italy Architecture Gate F as passed.
- Recorded Bruegel as evidence against blindly hardening parsing where useful feeds also expose full-content payloads.
- Recorded Assolombarda as evidence against source-specific publication-date recovery.
- Added metadata-only persistence and source-specific date recovery as explicit but unapproved future architecture questions.
- Preserved selective Copilot use as development assistance only.

## 2026-08-17 — TEF / Milan-Bocconi and Multilingual Classification Architecture

- Added Tech Europe Foundation.
- Added Milan and Bocconi Ecosystem.
- Added support for empty domain keyword lists.
- Recorded source-defined domains as a supported deterministic architecture.
- Recorded TEF's Milan/Bocconi source default.
- Preserved the standard `ArticleRecord` pipeline.
- Added deterministic case semantics for configured keywords.
- Recorded case-sensitive `AI` matching to avoid Italian `ai` false positives.
- Added Bank of Italy BDS as a future statistical-event use case.
- Added opportunity/deadline state tracking as a future gated architecture question.
- Kept near-duplicate clustering deferred.

## 2026-08-17 — Phase 4A Source and Domain Architecture Validation

- Replaced Sifted with Tech.eu.
- Added Financial Markets.
- Recorded that Financial Markets required configuration only.
- Established historical regression as a reusable taxonomy-validation method.
- Established that classification percentage is not an architectural KPI.
- Added the narrow Premium Bocconi Exception while preserving the authentication prohibition.
- Upgraded Milan/Bocconi from candidate to fixed product requirement.
- Preserved ranking weights and core processing modules.

## 2026-08-14 — Phase 3 Automation Architecture Completed

- Added `.github/workflows/daily-intelligence.yml`.
- Recorded manual `workflow_dispatch`.
- Recorded scheduled execution.
- Recorded the 06:05 Europe/Rome schedule.
- Recorded Python 3.12 hosted execution.
- Recorded full automated testing before production processing.
- Recorded workflow timeout and `contents: write` permission.
- Recorded output validation before persistence.
- Recorded automated bot persistence.
- Recorded no-change commit protection.
- Recorded critical configuration failure validation.
- Recorded degraded source publication validation.
- Recorded concurrency protection.
- Recorded GitHub scheduler latency and its coupling with the rolling report window.
- Added automated-public / Bocconi-premium-reading / research-database separation.
- Explicitly prohibited authenticated premium-content ingestion.

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