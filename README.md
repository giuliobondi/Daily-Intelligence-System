# Daily Intelligence System

A zero-cost, automated daily intelligence pipeline that collects, filters, classifies and ranks high-value developments across economics, markets, business, geopolitics, AI, technology, startups, Europe, Italy and the Milan/Bocconi ecosystem.

Instead of manually checking many separate publications and institutions every day, the system produces one bounded Markdown report containing the most relevant developments, their sources, relevance scores and source-provided context.

---

## README Guide

This README is intentionally divided into two parts.

### Part I — What This Project Does

A short overview for anyone who wants to understand:

- what the system is;
- why it exists;
- what it produces;
- what information it covers;
- what makes the project different.

**If you only want the high-level explanation, Part I is enough.**

### Part II — How the System Works

A technical deep dive covering:

- repository structure;
- configuration;
- collection;
- normalisation;
- validation;
- time-window filtering;
- deduplication;
- classification;
- ranking;
- storage;
- report generation;
- automation;
- failure handling;
- testing;
- local execution;
- design boundaries.

---

# Part I — What This Project Does

## 1. The Problem

Important professional information is distributed across many separate places:

- newspapers;
- central banks;
- public institutions;
- technology companies;
- research organisations;
- startup publications;
- policy organisations;
- local and professional ecosystem sources.

Following all of these manually creates several problems:

- **fragmentation** — relevant information is spread across many websites;
- **information overload** — too much content is published to review efficiently;
- **duplication** — the same event may appear repeatedly;
- **uneven source quality** — primary evidence, reporting and low-value material are mixed together;
- **weak prioritisation** — most feeds are not tailored to this project's information needs;
- **thin context** — a headline alone often does not explain what actually happened;
- **limited historical memory** — useful developments are easily forgotten after daily reading.

The Daily Intelligence System turns this fragmented workflow into one repeatable process.

---

## 2. What the System Does

Every day, the system automatically:

```text
collects public structured sources
→ normalises article metadata
→ removes invalid or out-of-window records
→ reduces exact duplicates
→ classifies useful stories into domains
→ calculates transparent relevance scores
→ selects a bounded set of stories
→ generates a Markdown intelligence report
→ stores the underlying structured records
→ records the operational run status
→ persists the outputs through GitHub
```

The intended user workflow is:

```text
open one report
→ understand the important developments
→ selectively open original sources when deeper reading is useful
```

rather than:

```text
check many websites
→ scan many headlines
→ manually decide what matters
→ repeatedly open articles just to understand the basic development
```

---

## 3. Why It Is Useful

The system is designed to improve **high-value awareness with negligible daily maintenance**.

It can help a reader:

- stay informed across several professional domains without monitoring each source manually;
- distinguish higher-value developments from routine content;
- see where each story came from;
- understand why a story was selected;
- receive enough source-provided context to reduce unnecessary click-through;
- preserve a historical archive of processed information;
- identify gaps or failures in the information workflow rather than silently assuming coverage is complete.

The system is intentionally selective.

A short report containing only genuinely useful developments is preferable to a large report filled with low-value material.

---

## 4. Information Coverage

The system currently monitors ten strategic domains:

1. **Global Politics and Geopolitics**
2. **Economics and Macroeconomics**
3. **Financial Markets**
4. **Companies and Corporate Strategy**
5. **Artificial Intelligence**
6. **Technology and Software**
7. **Startups and Venture Capital**
8. **Europe and the European Union**
9. **Italy**
10. **Milan and Bocconi Ecosystem**

All ten domains are implemented.

They are not equally mature, and the project does not claim comprehensive coverage.

Known residual gaps include:

- broader global Companies and Corporate Strategy reporting;
- Financial Markets coverage beyond monetary-policy and rates evidence;
- independent AI and technology reporting;
- independent European economic-policy interpretation;
- Startups/VC diversification;
- Milan/Bocconi recruiting, employer-event and established-company coverage.

These gaps are documented rather than hidden.

---

## 5. Current Production Sources

The current production system uses thirteen public RSS sources:

1. BBC News World
2. BBC News Business
3. European Central Bank
4. European Commission Highlighted News
5. Istat Press Releases
6. OpenAI News
7. Tech.eu
8. Tech Europe Foundation
9. Federal Reserve Board Monetary Policy
10. MIMIT News
11. Lavoce.info Imprese
12. Google DeepMind News
13. ISPI Geoeconomics

The source universe is deliberately curated.

A source is not added merely because it is prestigious or technically accessible.

It must contribute a useful information function while remaining compatible with:

- zero recurring cost;
- automated access;
- public-repository persistence;
- source transparency;
- reasonable maintenance;
- copyright and credential boundaries.

---

## 6. What a Daily Report Contains

A normal report contains:

- report date;
- generation timestamp;
- monitored time window;
- run status;
- source-health summary;
- number of collected items;
- number of displayed items;
- domain sections;
- story headline and original link;
- source;
- publication time;
- relevance score;
- secondary domains when relevant;
- bounded source-provided context.

Example structure:

```text
## Artificial Intelligence

### Story headline

Source: Example Source
Published: ...
Relevance score: 7

Source context: Source-provided description explaining the core development.
```

The system does not generate independent AI summaries.

`Source context` is explicitly source-provided metadata.

---

## 7. Richer Source Context

The report is designed to provide enough initial context to understand the core development when the source metadata permits it.

Current source-context behaviour:

```text
description available and <= 500 characters
→ render unchanged

description > 500 characters
→ prefer a complete sentence within the limit
→ otherwise truncate at a word boundary

description missing
or description duplicates the title
→ show an explicit no-context fallback
```

Fallback text:

```text
No additional source-provided context available.
```

The report-context limit is currently:

```text
500 characters
```

The system deliberately does not use:

- article-body scraping;
- generic RSS body-content ingestion;
- LLM summarisation;
- generated filler text.

If the source provides weak metadata, that limitation remains visible.

---

## 8. Current System Snapshot

Current validated MVP checkpoint:

```text
13 active public RSS sources
10 active domains
daily GitHub Actions automation
zero recurring monetary cost
deterministic classification
deterministic ranking
JSONL historical storage
Markdown daily reports
structured JSON run summaries
source-level failure isolation
122 automated tests passed at the 2026-08-19 checkpoint
```

The core pipeline is operational.

Current development is evidence-driven rather than feature-driven: new complexity should be introduced only when real report use demonstrates a meaningful limitation.

---

## 9. Core Design Principles

The project follows several fixed principles.

### Zero recurring monetary cost

The core system does not require:

- paid news APIs;
- paid automation platforms;
- paid hosting;
- OpenAI API credits;
- recurring GitHub AI or Copilot credits.

### Deterministic before AI

The production pipeline uses ordinary deterministic Python logic for:

- filtering;
- classification;
- ranking;
- deduplication;
- reporting.

### Public structured sources first

Preferred inputs are:

```text
RSS / Atom
→ official free APIs
→ other explicitly permitted structured public endpoints
```

### Transparent provenance

Every displayed story retains a direct link to its original source.

### Public-safe repository

The production repository must not contain:

- credentials;
- authenticated premium article bodies;
- private Bocconi systems;
- private email;
- restricted database exports;
- private Career OS content.

### Minimal manual maintenance

Normal daily operation should require no manual report construction or source checking.

### Simplicity over sophistication

The project deliberately avoids introducing:

- agents;
- RAG;
- embeddings;
- vector databases;
- machine-learning ranking;
- a cloud database;
- a complex frontend;

unless real evidence later demonstrates a need.

---

## 10. The Project in One Diagram

```text
PUBLIC STRUCTURED SOURCES
          │
          ▼
      COLLECTION
          │
          ▼
     NORMALISATION
          │
          ▼
      VALIDATION
          │
          ▼
    24-HOUR FILTER
          │
          ▼
    DEDUPLICATION
          │
          ▼
    CLASSIFICATION
          │
          ▼
        RANKING
          │
          ▼
   STRUCTURED STORAGE
          │
          ▼
    REPORT SELECTION
          │
          ▼
    MARKDOWN REPORT
          │
          ▼
      GITHUB HISTORY
```

---

# Part II — How the System Works

> **Technical deep dive**
>
> Everything above is sufficient if you only wanted to understand what the project does and why it exists.
>
> The following sections explain the complete implementation and production workflow.

---

## 11. End-to-End Architecture

The application pipeline is:

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
→ Report selection
→ Report rendering
→ Run-summary generation
→ Output persistence
```

Production wraps the same application pipeline with GitHub Actions:

```text
GitHub trigger
→ checkout repository
→ set up Python
→ install dependencies
→ run automated tests
→ run production pipeline
→ validate generated outputs
→ stage generated output directories
→ detect whether anything changed
→ create bot commit when needed
→ push
```

There is no separate local pipeline and production pipeline.

The same Python application is used in both environments.

---

# 12. Repository Structure

The main repository structure is:

```text
Daily-Intelligence-System/
│
├── .github/
│   └── workflows/
│       └── daily-intelligence.yml
│
├── config/
│   ├── domains.yaml
│   ├── settings.yaml
│   └── sources.yaml
│
├── data/
│   ├── processed/
│   └── runs/
│
├── docs/
│   └── project/
│
├── reports/
│   └── daily/
│
├── src/
│   └── daily_intelligence/
│       ├── __init__.py
│       ├── cli.py
│       ├── classify.py
│       ├── collect.py
│       ├── config.py
│       ├── deduplicate.py
│       ├── filter_window.py
│       ├── models.py
│       ├── normalize.py
│       ├── pipeline.py
│       ├── rank.py
│       ├── report.py
│       ├── run_summary.py
│       ├── storage.py
│       └── validate.py
│
├── tests/
│
├── LICENSE
├── pyproject.toml
└── README.md
```

The main responsibilities are:

| Path | Responsibility |
|---|---|
| `config/` | Sources, domains, ranking and report configuration |
| `src/daily_intelligence/` | Production Python pipeline |
| `tests/` | Automated deterministic tests and controlled fixtures |
| `data/processed/` | Historical processed article records |
| `data/runs/` | Structured operational run summaries |
| `reports/daily/` | Human-readable daily intelligence reports |
| `.github/workflows/` | Scheduled and manual production automation |
| `docs/project/` | Canonical project/product/architecture documentation |

---

# 13. Configuration

The project separates configuration from processing logic.

This allows many source, domain and ranking changes to be made without rewriting pipeline code.

---

## 13.1 `config/sources.yaml`

Defines the production source registry.

Typical source configuration includes:

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

A source may have one or more default domains when its entire information function genuinely supports that classification.

Examples:

```text
OpenAI News
→ Artificial Intelligence

Google DeepMind News
→ Artificial Intelligence

Federal Reserve Monetary Policy
→ Economics and Macroeconomics

MIMIT News
→ Italy

Lavoce.info Imprese
→ Italy

Tech Europe Foundation
→ Milan and Bocconi Ecosystem
```

Broad sources such as BBC, Tech.eu or ISPI Geoeconomics do not receive blanket defaults simply because they often publish stories in certain domains.

---

## 13.2 `config/domains.yaml`

Defines the topic taxonomy.

Each domain contains:

```text
id
name
keywords
active
```

Most domains use deterministic lexical evidence.

Some domains intentionally contain no keywords.

For example:

```text
Italy
Milan and Bocconi Ecosystem
```

can be classified through validated source defaults instead of generic words that would create excessive false positives.

---

## 13.3 `config/settings.yaml`

Defines ranking and report behaviour.

Current ranking settings conceptually implement:

```text
Tier 1 = 4 points
Tier 2 = 3 points
Tier 3 = 2 points
Tier 4 = 1 point

domain match  = 2 points
keyword match = 1 point
```

Current report limits:

```text
maximum items per domain = 5
maximum total items      = 30
maximum source context   = 500 characters
```

These are upper bounds, not targets.

---

# 14. Core Data Model

The article is the core production record.

The pipeline normalises collected feed entries into a consistent `ArticleRecord`.

Conceptually, a processed record contains information such as:

```text
record identity
source identity
title
article URL
publication timestamp
retrieval timestamp
normalized description
assigned domains
matched keywords
relevance score
```

The system intentionally keeps one article-oriented production model.

It does not currently maintain separate models for:

- events;
- opportunities;
- application deadlines;
- statistical releases;
- enriched AI summaries.

Those would require separate validated product needs.

---

# 15. Collection — `collect.py`

The collector retrieves configured RSS or Atom feeds.

The collection layer handles:

- HTTP/HTTPS retrieval;
- explicit request headers;
- RSS/Atom parsing;
- redirects;
- source-level result reporting;
- source-level failure isolation.

Current network behaviour includes:

```text
10-second request timeout
normal TLS verification
explicit User-Agent
explicit Accept header
```

Each source produces a structured outcome.

A source may therefore be:

```text
success
empty
failed
```

without automatically terminating the entire pipeline.

---

## Why Source-Level Isolation Matters

External feeds can fail independently because of:

- network errors;
- HTTP errors;
- endpoint changes;
- malformed feeds;
- temporary publisher outages.

The system is designed so that one failed source does not normally destroy all successful information collected from other sources.

---

# 16. Normalisation — `normalize.py`

RSS feeds expose metadata in slightly different shapes.

Normalisation converts those differences into one consistent article representation.

The normaliser handles:

- title extraction and cleanup;
- article URL cleanup;
- publication timestamps;
- description extraction;
- HTML-to-text conversion;
- whitespace cleanup;
- deterministic record identity;
- preservation of source metadata.

Publication timestamps are converted to timezone-aware UTC values when suitable structured timestamps exist.

---

## HTML Description Normalisation

Some RSS descriptions contain markup.

The generic normalisation path is:

```text
feed description
→ HTML parser
→ visible text extraction
→ whitespace cleanup
→ normalized description
```

The logic is generic rather than publisher-specific.

The system does not attempt to infer missing words or repair arbitrary malformed publisher text.

---

# 17. Validation — `validate.py`

Validation checks whether normalized records are structurally usable.

It verifies required fields and record integrity.

A structurally valid record is not automatically a report item.

A valid record may later be:

- outside the current reporting window;
- removed as an exact duplicate;
- left unclassified;
- excluded by report limits.

This distinction is important:

```text
valid record
≠
displayed story
```

---

# 18. Publication-Window Filtering — `filter_window.py`

The system currently uses a rolling reporting window:

```text
actual execution time
minus the previous 24 hours
```

A record must contain a usable publication timestamp to enter this stage successfully.

The pipeline deliberately does not substitute retrieval time when publication time is unavailable.

That prevents an old article retrieved today from being treated as newly published.

---

## Known Scheduling Limitation

GitHub Actions may begin later than its nominal scheduled minute.

Because the reporting window is based on actual execution time:

```text
later GitHub start
→ slightly later 24-hour cutoff
```

This is a known limitation.

A fixed daily cutoff has not been introduced because the current behaviour has not demonstrated enough product harm to justify additional complexity.

---

# 19. Exact Deduplication — `deduplicate.py`

The system performs deterministic exact duplicate reduction.

Current duplicate evidence includes:

```text
normalized article URL
normalized title
```

When an exact duplicate is found, the first deterministic occurrence is retained.

The system does not currently perform:

- semantic similarity;
- embeddings;
- fuzzy clustering;
- multi-source story clustering.

These remain deferred until real reports show that exact deduplication is insufficient.

---

# 20. Classification — `classify.py`

Classification determines which strategic domains apply to each article.

The system currently uses two evidence types:

```text
source-default domains
+
keyword matches against title and description
```

A record can receive multiple domains.

---

## 20.1 Source Defaults

Source defaults are used only when the source itself provides reliable domain evidence.

Examples:

```text
Istat
→ Economics and Macroeconomics

OpenAI News
→ Artificial Intelligence

Google DeepMind News
→ Artificial Intelligence

Federal Reserve Monetary Policy
→ Economics and Macroeconomics

MIMIT News
→ Italy

Lavoce.info Imprese
→ Italy

Tech Europe Foundation
→ Milan and Bocconi Ecosystem
```

Broad publications are intentionally not assigned blanket defaults.

---

## 20.2 Keyword Evidence

Other classification evidence comes from configured keywords found in:

```text
title
+
normalized description
```

Keyword sets are deliberately conservative.

A new keyword is normally added only after:

- examining real missed stories;
- checking likely false positives;
- inspecting historical processed records;
- evaluating ranking consequences.

---

## 20.3 Case-Sensitive Acronyms

The classifier uses a simple deterministic case convention:

```text
all-lowercase configured keyword
→ case-insensitive matching

configured keyword containing uppercase characters
→ case-sensitive matching
```

This became important for:

```text
AI
```

because lowercase Italian:

```text
ai
```

is an ordinary word.

Keeping `AI` uppercase avoids large numbers of false Artificial Intelligence matches in Italian-language articles.

The same principle supports:

```text
IA
```

as an intentional Italian Artificial Intelligence acronym.

---

## 20.4 Unclassified Records

The system does not try to classify every collected article.

A record can remain:

```text
unclassified
```

and still be retained in the processed historical dataset.

Unclassified records are omitted from the main report by default.

This is deliberate.

The system prefers:

```text
smaller accurate report
```

over:

```text
larger report created by forcing ambiguous classifications
```

---

# 21. Ranking — `rank.py`

After classification, the system calculates a deterministic relevance score.

Current formula:

```text
source-tier score
+ 2 × number of assigned domains
+ 1 × number of matched keywords
```

Current source-tier scores:

| Source Tier | Score |
|---|---:|
| Tier 1 | 4 |
| Tier 2 | 3 |
| Tier 3 | 2 |
| Tier 4 | 1 |

This ranking model is intentionally simple.

Its advantages are:

- transparency;
- reproducibility;
- easy testing;
- easy debugging.

A higher score does not guarantee that a story is objectively more important.

The score represents the current configured evidence available to the deterministic system.

---

## Why Ranking Is Not More Complex

The project deliberately avoids:

- machine-learned ranking;
- LLM relevance scoring;
- semantic embeddings;
- source-specific penalties;
- opaque publisher adjustments.

If poor source or classification evidence creates inflated scores, the preferred response is:

```text
correct the evidence
```

rather than:

```text
add another ranking exception
```

---

# 22. Processed Storage — `storage.py`

Processed records are stored as:

```text
JSON Lines
```

under date-based paths:

```text
data/processed/YYYY/MM/YYYY-MM-DD.jsonl
```

JSONL was chosen because it is:

- human-inspectable;
- simple;
- Git-friendly;
- deterministic;
- database-free;
- zero-cost.

The stored historical records also provide a regression corpus for later taxonomy changes.

For example:

```text
proposed keyword
→ replay/search historical records
→ inspect changed classifications
→ detect false positives
→ retain or reject change
```

---

## Report Limit vs Storage

The report displays at most:

```text
500 characters
```

of source context.

That does **not** mean the stored normalized description is capped at 500 characters.

The 500-character limit belongs to the report presentation layer.

Storage semantics remain independent.

---

# 23. Report Selection — `report.py`

Not every classified record is displayed.

The report uses bounded selection rules:

```text
maximum 5 stories per primary domain
maximum 30 stories overall
```

These are maximums.

The system does not attempt to fill every section.

If only three stories deserve inclusion, a three-story report is acceptable.

---

## Deterministic Selection Order

Selection uses deterministic ordering based on factors including:

1. relevance score;
2. publication time;
3. source tier;
4. normalized title;
5. record identity.

This keeps repeated processing reproducible.

---

## Primary and Secondary Domains

A story appears once.

Its first eligible domain becomes its primary report section.

Additional domains are displayed as:

```text
Also:
```

Example:

```text
Primary:
Economics and Macroeconomics

Also:
Artificial Intelligence
```

This avoids repeating the same story in several sections.

---

# 24. Source Context Rendering — `report.py`

Selected stories receive a bounded source-context line.

The context comes from the existing:

```text
ArticleRecord.description
```

No separate enrichment field is created.

---

## Context Rules

### Description is missing

```text
No additional source-provided context available.
```

### Description duplicates the title

```text
No additional source-provided context available.
```

### Description fits within 500 characters

Render it unchanged.

### Description exceeds 500 characters

The formatter:

1. looks for the latest complete sentence that fits;
2. returns the complete sentence when one is available;
3. otherwise finds the last usable word boundary;
4. appends `...` when word-boundary truncation is required.

---

## Why It Is Called `Source context`

The text may be a publisher:

- summary;
- abstract;
- description;
- teaser.

The system therefore labels it:

```text
Source context
```

rather than implying that it is an independently written or AI-generated summary.

---

## Why RSS `content` Is Not Used

Some feeds expose richer `content` fields containing thousands of characters.

These can behave more like article bodies than compact metadata.

Using them generically could:

- increase copyright and persistence risk;
- inject much more incidental text into classification;
- distort relevance scores;
- increase report size;
- create source-specific maintenance.

The current implementation therefore uses the existing normalized description only.

---

# 25. Run Summary — `run_summary.py`

Each execution generates a machine-readable operational summary.

Stored path:

```text
data/runs/YYYY/MM/YYYY-MM-DD.json
```

The summary records information such as:

- run identifier;
- timestamps;
- monitored window;
- run status;
- active sources;
- successful sources;
- failed sources;
- empty sources;
- raw items;
- valid items;
- invalid items;
- duplicates;
- displayed items;
- warnings.

This provides a machine-readable operational record separate from the human report.

---

# 26. Pipeline Orchestration — `pipeline.py`

`pipeline.py` coordinates the complete application flow.

Conceptually:

```text
load configuration

→ collect all active sources

→ normalize successful entries

→ validate records

→ keep records inside the current publication window

→ deduplicate

→ classify

→ rank

→ write processed JSONL

→ build operational run summary

→ render Markdown report

→ persist report and run summary
```

The pipeline is responsible for coordinating components.

Individual modules remain focused on their own deterministic responsibilities.

---

# 27. Command-Line Interface — `cli.py`

The application exposes one production-equivalent command:

```bash
python -m daily_intelligence.cli run
```

The same command is used by GitHub Actions.

This means local testing and production execute the same application path.

---

# 28. GitHub Actions Production Automation

Production automation is defined in:

```text
.github/workflows/daily-intelligence.yml
```

The workflow supports:

```text
manual execution
+
daily scheduled execution
```

Current intended schedule:

```text
06:05 Europe/Rome
```

---

## Workflow Sequence

```text
1. Check out repository

2. Set up Python 3.12

3. Install package and development/test dependencies

4. Run automated tests

5. Run the production pipeline

6. Validate that the three expected output files exist and are non-empty

7. Stage:
   data/processed/
   data/runs/
   reports/daily/

8. Check whether generated outputs actually changed

9. If nothing changed:
   stop without creating a commit

10. If something changed:
    create a github-actions[bot] commit

11. Push the new outputs
```

The automated commit message is:

```text
data: update daily intelligence outputs
```

---

## Concurrency

The workflow uses a production concurrency group.

A second scheduled execution does not cancel an already-running production execution.

This reduces the risk of competing runs writing the same daily outputs.

---

# 29. Failure Behaviour

The system distinguishes three operational states:

```text
success
degraded
failure
```

---

## Success

All required pipeline components complete successfully.

Individual source outcomes and counts remain visible.

---

## Degraded

One or more sources may fail while enough successful information remains to create a useful report.

The successful sources continue through the pipeline.

The report/run summary makes the degraded state visible.

---

## Failure

Critical configuration, orchestration or pipeline errors prevent a valid production result.

Critical failures should not silently publish output as successful.

---

## Design Principle

The system prefers:

```text
useful partial information
+
visible degradation
```

over:

```text
discard all successful information because one external source failed
```

while still preserving strict failure behaviour for critical internal errors.

---

# 30. Generated Outputs

Each normal production run writes three main output types.

---

## 30.1 Processed Records

```text
data/processed/YYYY/MM/YYYY-MM-DD.jsonl
```

Contains structured processed article records.

Use cases:

- historical archive;
- inspection;
- debugging;
- taxonomy regression;
- future deterministic quality analysis.

---

## 30.2 Daily Report

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

Contains the human-readable intelligence report.

This is the main daily consumption layer.

---

## 30.3 Run Summary

```text
data/runs/YYYY/MM/YYYY-MM-DD.json
```

Contains operational execution metadata.

---

# 31. Testing

The project uses `pytest`.

Tests cover important deterministic behaviour including:

- source configuration;
- domain configuration;
- settings;
- RSS fixtures;
- collection;
- normalisation;
- validation;
- publication-window filtering;
- deduplication;
- classification;
- multilingual/case-sensitive keyword behaviour;
- ranking;
- storage;
- report selection;
- source-context rendering;
- run summaries;
- pipeline integration.

At the 2026-08-19 richer-report implementation checkpoint:

```text
20 feed-fixture tests passed
14 report tests passed
122 tests passed in the complete suite
```

The test count is a checkpoint, not a fixed project requirement.

Future development may change the total.

---

# 32. Product Validation Beyond Tests

Passing tests is necessary but not sufficient.

Every meaningful product change should also inspect real output.

The project evaluates questions such as:

- Were important stories included?
- Were useful stories missed?
- Were weak stories promoted?
- Did classification become misleading?
- Did relevance scores become inflated?
- Is the report repetitive?
- Is the report too long?
- Is the report too sparse?
- Does source context actually explain the development?
- Are source-quality defects visible?
- Did a source fail silently?
- Are generated outputs understandable to a human reader?

A technically successful pipeline can still produce a poor intelligence product.

---

# 33. Running the Project Locally

## Requirements

```text
Python >= 3.12
Git
```

Clone the repository and move into it.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the package and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the test suite:

```bash
python -m pytest
```

Run the production-equivalent pipeline:

```bash
python -m daily_intelligence.cli run
```

After execution, inspect:

```text
data/processed/
data/runs/
reports/daily/
```

---

# 34. Adding or Changing a Source

A new source should not begin with configuration editing.

The preferred workflow is:

```text
identify a real information gap
→ evaluate the source's information function
→ verify public structured access
→ verify persistence/copyright compatibility
→ test with the real collector
→ inspect normalized records
→ inspect metadata quality
→ test existing classification
→ test ranking consequences
→ determine whether keywords/defaults are justified
→ make the smallest configuration/code change
→ run targeted tests
→ run full tests
→ run production-equivalent pipeline
→ inspect generated report
→ inspect Git diff
```

Possible source outcomes are:

```text
Active
Standby
Rejected
Manual/research layer
Deferred production-readiness candidate
```

A technically functional RSS feed can still be rejected.

---

# 35. Adding or Changing a Domain

Domain changes normally belong in:

```text
config/domains.yaml
```

Before adding broad keywords:

1. inspect real missed records;
2. simulate the proposed keyword;
3. search historical processed records;
4. check false positives;
5. inspect relevance-score effects.

Some domains may deliberately use:

```yaml
keywords: []
```

when validated source defaults provide better evidence.

The project does not optimise for maximum classification coverage.

---

# 36. Current Source-Selection Philosophy

The project prefers **information-function coverage** over publisher accumulation.

Useful source roles include:

```text
primary institutional evidence
high-quality reporting
independent analysis
specialist intelligence
frontier-lab primary evidence
professional ecosystem information
```

Adding several publishers that all perform the same role can increase:

- duplication;
- noise;
- failures;
- maintenance;

without materially improving intelligence quality.

The smallest strong source universe is preferred.

---

# 37. Source Access and Copyright Boundaries

The repository is public.

Automated production may use:

- public RSS;
- public Atom;
- official free APIs;
- approved public structured metadata.

The production system must not:

- store credentials;
- automate Bocconi authentication;
- scrape authenticated premium publications;
- bypass paywalls;
- automate `yoU@B`;
- automate JobGate;
- bulk-ingest licensed databases;
- store complete premium articles;
- store private email/newsletter content;
- bypass anti-bot or access-control systems.

---

## Personal Reading vs Automated Ingestion

The user may legitimately have access to premium publications through institutional services.

That does not automatically give the automated pipeline permission to retrieve or store the premium article body.

The project deliberately separates:

```text
what a person can legitimately read
```

from:

```text
what a public automated repository can retrieve and persist
```

---

# 38. Why the System Does Not Use LLMs in Production

The project uses AI during development and reasoning, but AI is not part of the production dependency chain.

The production problem can currently be solved through:

- structured feeds;
- deterministic rules;
- transparent ranking;
- bounded source metadata.

Adding production LLM calls would introduce:

- recurring cost risk;
- nondeterminism;
- provenance complexity;
- new failure modes;
- evaluation burden.

The current system therefore deliberately contains:

```text
no LLM classification
no LLM ranking
no LLM summaries
no agents
no RAG
no embeddings
no vector database
```

These are not missing features.

They are intentionally deferred technologies whose value has not been demonstrated for the current workflow.

---

# 39. Why There Is No Database

Current storage uses Git + JSONL + JSON + Markdown.

That is sufficient for the current scale.

Benefits:

- zero external infrastructure;
- transparent history;
- inspectable data;
- easy version control;
- no database administration;
- no recurring hosting cost.

A database should be introduced only if repository-native storage becomes a demonstrated limitation.

---

# 40. Why There Is No Frontend

The current delivery interface is Markdown inside the repository.

This keeps the project:

- simple;
- transparent;
- free;
- easy to maintain.

Possible future interfaces could include:

- a stable latest-report view;
- GitHub Pages;
- GitHub Issues;
- another lightweight delivery layer.

None is justified until the existing Markdown workflow creates meaningful recurring friction.

---

# 41. Known Limitations

The current system deliberately accepts several limitations.

### Coverage is not comprehensive

All ten domains exist, but some are stronger than others.

### Exact deduplication only

Different headlines describing the same event may still appear separately.

### Rolling reporting window

The 24-hour window moves with actual execution time.

### Missing source descriptions

Some publishers provide little or no source context.

### Publisher metadata defects

Malformed source-provided descriptions may remain visible.

### No article-level entity extraction

The system does not yet identify structured companies, people or institutions.

### No content-type model

The system does not separately classify:

- analysis;
- news;
- event;
- opportunity;
- press release.

### No opportunity/deadline state

Publication date is not always equivalent to application deadline or event date.

### No statistical-event pipeline

Structured statistical databases are not currently converted into synthetic intelligence events.

### No near-duplicate clustering

The system does not use semantic similarity or embeddings.

These are tracked limitations, not automatic implementation tasks.

---

# 42. Development Philosophy

The project evolves through a controlled evidence loop:

```text
observe real problem
→ identify exact cause
→ test the simplest explanation
→ choose smallest sufficient change
→ implement
→ run targeted validation
→ run full validation
→ inspect real output
→ inspect Git diff
→ commit only after evidence supports the change
```

The project deliberately avoids building a large speculative roadmap.

A future feature should answer:

1. What real problem does it solve?
2. Has the problem actually occurred?
3. Can configuration solve it?
4. Can a simpler deterministic change solve it?
5. What maintenance burden does it add?
6. What new failure modes appear?
7. Does it preserve zero recurring monetary cost?
8. Does it preserve negligible daily manual work?
9. Does it preserve source transparency?
10. How will success be validated?

---

# 43. Current Development State

The major completed phases are:

```text
Phase 0
Project definition and repository setup
→ complete

Phase 1
Local vertical pipeline
→ complete

Phase 2
Real-source production readiness
→ complete

Phase 3
GitHub Actions production automation
→ complete

Phase 4
Source and domain correction / expansion
→ complete for current MVP boundary

Phase 5
Richer-report product design
→ complete

Phase 6
Richer-report implementation and evaluation
→ implemented and locally validated
```

The current system is therefore operational rather than a prototype awaiting its first complete pipeline.

Future development should be driven by evidence from normal report use.

---

# 44. Current Highest-Level Architecture Decisions

The following decisions are intentionally preserved:

```text
Python
→ core implementation language

RSS / Atom
→ primary source-delivery mechanism

YAML
→ source/domain/settings configuration

ArticleRecord
→ core production data model

deterministic rules
→ classification and ranking

JSONL
→ processed historical records

JSON
→ operational run summaries

Markdown
→ daily human-readable reports

GitHub Actions
→ production automation

Git repository
→ history and persistence
```

No additional infrastructure is required for the current MVP.

---

# 45. Canonical Project Documentation

This README explains the repository for an external or first-time reader.

The detailed project decisions remain in the canonical project documents.

## [`docs/project/00 Project Brief.md`](docs/project/00%20Project%20Brief.md)

Defines:

- why the project exists;
- strategic scope;
- hard constraints;
- success criteria;
- major non-goals.

## [`docs/project/01 Product Requirements.md`](docs/project/01%20Product%20Requirements.md)

Defines:

- required user behaviour;
- report requirements;
- information coverage requirements;
- richer-context acceptance criteria;
- product boundaries.

## [`docs/project/02 System Architecture.md`](docs/project/02%20System%20Architecture.md)

Defines:

- component responsibilities;
- processing architecture;
- configuration architecture;
- automation architecture;
- persistence;
- failure behaviour;
- technical gates;
- deferred architecture.

## [`docs/project/03 Information Taxonomy and Source Policy.md`](docs/project/03%20Information%20Taxonomy%20and%20Source%20Policy.md)

Defines:

- domain taxonomy;
- source-selection policy;
- source tiers;
- keyword/default-domain policy;
- access and copyright rules;
- source-audit conclusions;
- metadata policy.

## [`docs/project/04 Development Roadmap and Status.md`](docs/project/04%20Development%20Roadmap%20and%20Status.md)

Defines:

- completed phases;
- latest validation state;
- current checkpoint;
- deferred work;
- next development action.

The repository and these documents together are the source of truth.

---

# 46. License

This repository is licensed under the terms of the included [`LICENSE`](LICENSE) file.

---

# 47. Summary

The Daily Intelligence System is intentionally a small, transparent intelligence pipeline rather than a sophisticated AI application.

Its current production model is:

```text
13 curated public RSS sources
→ deterministic collection
→ normalization
→ validation
→ rolling-window filtering
→ exact deduplication
→ deterministic domain classification
→ deterministic relevance ranking
→ repository-native storage
→ bounded source-context rendering
→ daily Markdown report
→ GitHub Actions persistence
```

Its design philosophy is:

```text
useful before sophisticated
deterministic before AI
structured sources before scraping
transparent before opaque
evidence before complexity
```

The system is designed to make daily information consumption more selective, reproducible and useful while preserving:

```text
zero recurring monetary cost
negligible daily manual work
public-source transparency
public-repository safety
simple maintainable architecture
```