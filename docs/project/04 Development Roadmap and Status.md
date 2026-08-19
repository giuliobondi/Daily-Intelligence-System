# Daily Intelligence System — Development Roadmap and Status

> **Purpose**
>
> This document controls the implementation of the Daily Intelligence System.
>
> It records the current phase, completed decisions, active milestone, blockers, deferred work and next highest-priority action.
>
> It is not a long-term product vision document and should not duplicate the Project Brief, Product Requirements, System Architecture or Information Taxonomy and Source Policy.

---

> **Primary Question**
>
> *What should be built now, what has already been completed, and what is the next highest-value step?*

---

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
- Do not introduce production AI calls or recurring AI-credit consumption.
- Keep daily manual work negligible.
- Prefer RSS, official APIs and other structured public sources before scraping.
- Prefer deterministic rules before machine learning or LLM-based logic.
- Use public or explicitly permitted source material in the automated pipeline.
- Do not treat personal or institutional reading access as permission for automated ingestion.
- Validate locally before changing production automation where practical.
- Use Git and tests as the verification layer for every material change.
- Keep the repository public-safe.
- Stop at stable checkpoints.
- Treat technically successful execution as insufficient if the report is noisy, repetitive, misleading, inaccessible, too sparse or too thin to understand without unnecessary click-through.
- Prefer differentiated information roles over accumulating publishers.
- Prefer unclassified records over misleading classification.
- Evaluate report quality from real selected and missed stories, not from classification rate alone.
- Correct source or classification evidence before increasing ranking complexity.
- Do not create new processing paradigms for sources that have not demonstrated enough value to justify them.
- Preserve durable source-audit conclusions in `03 Information Taxonomy and Source Policy.md` rather than reconstructing them from chat history.
- Use GitHub Copilot selectively for narrow mechanical multi-file edits when it materially reduces repetitive work.
- Keep ChatGPT responsible for reasoning, scope and drafting; keep Git/tests responsible for verification.
- Do not keep extending source research merely because more candidate publishers exist.
- Reopen source work only when real product use reveals a sufficiently costly information gap or a materially cleaner endpoint becomes available.
- Solve a validated quality problem at the narrowest layer that can satisfy the user need.
- Do not expand persistence, classification evidence or ingestion architecture when a presentation-layer change is sufficient.
- Do not retain speculative fixes once diagnostics show that the assumed defect does not originate in that layer.

The project should not move to implementation of a new phase until the current design requirement has a clear acceptance condition.

After implementation, the project should not automatically create another feature phase.

The next step should come from:

```text
real use
→ observed limitation
→ validated problem
→ smallest justified change
```

---

# Current Project Status

| Field | Current Status |
|---|---|
| Project Phase | Phase 6 — Richer-Report Implementation and Evaluation — implementation complete locally; closeout checkpoint active |
| Current Milestone | Milestone 6 — Close the validated richer-report implementation, reconcile canonical documentation, inspect the final Git diff and commit only intended changes |
| Repository Status | Public Python repository with automated GitHub-native daily execution and repository-native historical outputs |
| Implementation Status | Deterministic collect → normalize → validate → filter → deduplicate → classify → rank → store → report pipeline implemented and production-validated; richer source-context presentation implemented |
| Automation Status | GitHub Actions implemented; manual and scheduled execution validated; outputs persisted automatically |
| Production Schedule | Daily at 06:05 Europe/Rome; GitHub scheduling latency remains an observed operational limitation |
| Source Registry | Thirteen active production sources |
| Taxonomy Status | Ten implemented domains; all ten strategic macroareas have production configuration |
| Domain Maturity | All ten domains are sufficient for the current MVP boundary, but several remain intentionally incomplete |
| Richer-Report Status | Phase 5 design complete; Phase 6 implementation complete and locally validated |
| Report Context | Existing normalized description rendered as explicit `Source context`, bounded at 500 characters with deterministic sentence/word-aware truncation and transparent fallback |
| Testing Status | 122 automated tests passed at the latest implementation checkpoint |
| Targeted Validation | 20 feed-fixture tests passed; 14 report tests passed |
| Latest Local Validation | Real 19 August 2026 production-equivalent run completed successfully with 13/13 sources successful and 0 invalid records |
| Latest Run Snapshot | 1448 valid records; 50 inside the rolling collection window; 45 unique; 28 unclassified; status success |
| Current Product-Quality Finding | Richer context can be delivered through the existing description/report layer without article scraping, RSS body-content ingestion, a new record model or production AI |
| Current Blockers | No implementation or automation blocker |
| Current Priority | Finish documentation closeout, inspect the complete diff, validate the final intended file set, then commit and push the Phase 6 checkpoint |
| Current Git State | Intended richer-report implementation files modified; 19 August generated outputs untracked; unrelated `.obsidian/workspace.json` must remain excluded |

---

# Completed Project Decisions

The following decisions are established unless explicitly changed later.

## Core Operating Model

- Use a hybrid information model:
  - ChatGPT provides independent interpretation, planning and synthesis outside the production pipeline.
  - GitHub and Python provide deterministic collection, organisation, ranking, reporting and archiving.
- Zero recurring monetary cost is a hard constraint.
- Daily manual work should be negligible.
- Production must not consume GitHub AI, Copilot or other recurring AI credits.
- Public structured sources are the default automated input class.
- RSS and Atom are the first supported automated source types.
- Production automation uses ordinary Python and GitHub Actions.
- The core system does not depend on LLM calls, agents, RAG, embeddings, vector databases or paid APIs.
- The repository remains public.
- Private Career OS materials remain outside the repository.
- Bocconi institutional credentials and other private credentials must never be embedded in production.
- Personal or institutional reading access does not automatically authorise automated ingestion.
- Processed records use JSON Lines.
- Run summaries use JSON.
- Daily reports use Markdown.
- Internal timestamps use timezone-aware UTC datetimes.
- Reports use one primary placement per item, with secondary domains shown as metadata.
- Relevance scoring is deterministic and explainable.
- Repository-native persistence remains the production delivery model.
- GitHub Issues, GitHub Pages and other interface layers remain optional and deferred.

---

## Development Assistance

The working principle remains:

```text
ChatGPT decides and writes
→ Copilot may locate/apply narrow mechanical edits
→ Git/tests verify
```

Copilot may be useful when:

- several repetitive configuration assertions must be added;
- source IDs/counts must be updated mechanically across a few known files;
- a narrow repetitive repository edit has already been strategically decided.

Copilot should not be used by default.

Do not delegate:

- source policy;
- architecture;
- taxonomy decisions;
- source selection;
- test interpretation;
- report-quality judgment;
- broad repository redesign.

Production must remain independent from Copilot.

---

# Information-Quality Decisions

- Broad heterogeneous feeds may use no default domain.
- Source defaults represent genuine source-wide topical evidence rather than publisher category.
- A domain may use no keywords when a validated narrow source default provides the evidence.
- Unclassified records are preferable to misleading classifications.
- A high unclassified rate is not itself a defect.
- Classification quality should be judged by valuable misses and false positives.
- Keyword expansion must be simulation-driven because keywords affect ranking as well as classification.
- Lowercase configured keywords are matched case-insensitively.
- Intentionally uppercase-containing keywords are matched case-sensitively.
- `AI` is intentionally uppercase to prevent false matches against the common Italian word `ai`.
- `IA` is intentionally uppercase for the Italian Artificial Intelligence acronym.
- Retry logic should not be added without evidence.
- A technically compatible source is not automatically a good production source.
- Production source quality must consider automation suitability, persistence compatibility and end-user usefulness.
- A source may be replaced or deferred instead of receiving source-specific complexity.
- Report quality must be evaluated independently from run success.
- Source expansion should solve information-function gaps rather than target publisher count.
- Strong primary evidence and strong independent interpretation are different information roles.
- Missing global FT/Reuters-style corporate reporting can remain an explicit limitation rather than being filled with inferior substitutes.
- Public RSS availability does not automatically mean that full feed payloads are suitable for permanent public Git persistence.
- Missing publication timestamps do not justify substituting retrieval time.
- Full-content feeds do not justify source-specific truncation merely to activate a prestigious source.
- Event publication time must not be assumed to equal event date or application deadline.
- Access-control interstitials must not be treated as valid structured content merely because they return HTTP `200`.
- A source should not receive source-specific ranking penalties or filters merely to compensate for a broad/noisy upstream feed.
- Long page-like descriptions can distort deterministic classification and ranking through incidental keyword matches.
- Richer report presentation should not automatically imply richer classification evidence.
- The existing normalized description remains the shared article evidence field.
- RSS `content` fields should not be ingested generically merely because they are longer.
- Missing report context should be exposed transparently rather than fabricated.
- Publisher-provided source context should be labelled as source context rather than presented as an independently generated summary.
- Source-provided malformed text should not trigger speculative generic repair unless the system's own transformation layer is proven to be the cause.
- Report-selection breadth and context depth are separate product controls.

---

# Richer-Report Decisions

Phase 5 and Phase 6 established the following durable decisions.

## Context Source

Use:

```text
ArticleRecord.description
```

as the report-context source.

Do not create a second context field for the current MVP.

---

## Display Bound

Current configured report-context maximum:

```text
500 characters
```

The previous limit was:

```text
300 characters
```

The increase is presentation-only.

It does not change:

- persisted description semantics;
- classification evidence;
- ranking evidence;
- article identity;
- source selection.

---

## Provenance

Report context is labelled:

```text
Source context
```

because it is source/publisher-provided metadata.

Do not label it generically as:

```text
Summary
```

when no independent summarisation occurred.

---

## Truncation

Current deterministic behaviour:

```text
description <= limit
→ unchanged

description > limit
→ prefer complete sentence within bound
→ otherwise truncate at word boundary
→ append ... for word-boundary truncation
```

---

## Missing Context

If:

```text
description missing
or
description duplicates title
```

render:

```text
No additional source-provided context available.
```

Do not silently omit the context line.

Do not fabricate replacement text.

---

## Report Breadth

Keep:

```text
max 5 items per domain
max 30 items total
```

The Phase 5 audit did not justify reducing or increasing these caps.

Historical reports were generally well below the maximum total.

---

## Content Boundary

Do not generically use:

```text
RSS content
article body
first paragraph
scraped article text
```

for richer reports.

The metadata audit showed that some RSS `content` fields are thousands of characters long and body-like.

Using them would add:

- persistence risk;
- copyright risk;
- classification/ranking distortion risk;
- source-specific complexity.

---

## AI Boundary

Do not introduce:

- LLM summaries;
- OpenAI API calls;
- production ChatGPT dependency;
- agentic summarisation;
- RAG;
- embeddings.

The validated product need was solved without them.

---

# Premium / Institutional Access

- Bocconi reading access is distinct from production automation permission.
- A narrow Premium Bocconi Exception exists for unusually valuable publications.
- The exception never permits:
  - authenticated automated retrieval;
  - credential storage;
  - paywall bypass;
  - premium article-body persistence.
- Premium sources still require a legitimate public or automation-compatible discovery endpoint.
- Financial Times and Il Sole 24 Ore have been audited under this model and remain inactive.
- Private Bocconi Career Services remains a complementary manual layer rather than a production dependency.
- Public Career Services pages may be used manually, but authenticated `yoU@B` / JobGate automation remains prohibited.
- Richer report context does not relax any of these boundaries.

---

# Repository and Package Baseline

Completed repository foundations include:

- public GitHub repository;
- `README.md`;
- `.gitignore`;
- `LICENSE`;
- `pyproject.toml`;
- `config/`;
- `src/daily_intelligence/`;
- `tests/` and controlled fixtures;
- `docs/project/` for canonical project documentation;
- `.github/workflows/daily-intelligence.yml`;
- repository-native `data/`;
- repository-native `reports/`.

The Python package uses a `src/` layout and requires Python 3.12 or later.

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

The repository itself remains the source of truth if file names or structure change later.

---

# Development Phases

---

# Phase 0 — Definition and Repository Setup

## Objective

Create the minimum project definition required to begin implementation without major ambiguity.

## Completed Scope

Phase 0 established:

- project purpose;
- product behaviour;
- information taxonomy;
- source policy;
- architecture;
- implementation roadmap;
- repository structure;
- hard constraints;
- MVP boundary;
- initial implementation sequence.

## Status

**Complete**

---

# Phase 1 — Local Vertical Slice

## Objective

Build the smallest complete local pipeline proving the workflow from collection to readable output.

## Implemented Scope

Phase 1 implemented:

1. configuration loading;
2. RSS/Atom collection;
3. structured source-level collection results;
4. normalisation;
5. required-field validation;
6. publication-window filtering;
7. exact deduplication;
8. deterministic classification;
9. deterministic relevance scoring;
10. JSONL persistence;
11. Markdown report generation;
12. JSON run summaries;
13. local orchestration;
14. one-command CLI execution;
15. source-level failure isolation;
16. degraded-run behaviour;
17. operational logging;
18. automated tests.

Local execution:

```text
python -m daily_intelligence.cli run
```

Phase 1 established the development pattern:

```text
run real workflow
→ inspect output
→ identify concrete defect
→ make smallest correction
→ test
→ inspect again
```

At Phase 1 closeout:

```text
104 automated tests passed
```

## Status

**Complete**

---

# Phase 2 — Minimal Real-Source Production Readiness

## Objective

Validate the local system with a small real public source universe before automation.

## Initial Real-Source Baseline

Phase 2 validated seven public RSS sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Sifted.

This was a validation baseline, not a permanent source universe.

## Initial Implemented Taxonomy

Phase 2 validated seven domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Companies and Corporate Strategy;
4. Artificial Intelligence;
5. Technology and Software;
6. Startups and Venture Capital;
7. Europe and the European Union.

## Major Phase 2 Lessons

- Broad source defaults produced misleading classifications.
- Source defaults must be evidence, not publisher labels.
- Conservative keyword expansion is preferable to broad lexical coverage.
- A degraded source should not necessarily fail the whole run.
- Real feed behaviour must be tested before automation.
- Classification rate is not itself the goal.

At Phase 2 closeout:

```text
110 automated tests passed
```

## Status

**Complete**

---

# Phase 3 — Production Automation

## Objective

Run the validated deterministic pipeline automatically every day with visible failure behaviour and repository-native persistence.

## Implemented Scope

Phase 3 delivered:

- GitHub Actions workflow;
- daily schedule;
- manual workflow dispatch;
- dependency installation;
- automated tests before production execution;
- pipeline execution;
- output persistence;
- automated commit/push;
- degraded-run handling;
- critical failure visibility;
- repository-native history.

Production schedule:

```text
06:05 Europe/Rome
```

## Operational Finding

GitHub scheduled workflows may start materially later than the requested time.

The report window currently remains:

```text
actual execution time
minus 24 hours
```

Do not redesign this without repeated evidence that the latency materially harms the report.

## Status

**Complete**

---

# Phase 4 — Source and Domain Correction / Expansion

## Objective

Build the smallest source/domain universe sufficiently strong for daily MVP use before investing in richer-report context.

The phase was not intended to:

- maximise source count;
- eliminate every information gap;
- reproduce premium journalism;
- automate private Career Services;
- create new architectures for every attractive source.

The governing question became:

> **Would another source/domain change create more user value than improving the context of stories already being selected?**

After the final gap-driven audits, the answer became:

> **No for the current MVP boundary.**

## Status

**Complete for the current MVP boundary**

Residual information gaps remain documented and may be reopened when evidence changes.

---

# Phase 4A — Tech.eu Replacement and Financial Markets Activation

## Completed Work

- [x] Completed first Career Agent source/domain strategy.
- [x] Incorporated Bocconi access model into source policy.
- [x] Defined the Premium Bocconi Exception.
- [x] Investigated Sifted accessibility.
- [x] Tested Sifted metadata richness.
- [x] Investigated Tech.eu as replacement.
- [x] Collected Tech.eu through the real project collector.
- [x] Validated Tech.eu normalisation.
- [x] Compared Tech.eu and Sifted metadata directly.
- [x] Replaced Sifted with Tech.eu.
- [x] Configured Tech.eu without a blanket source default.
- [x] Added evidence-backed keywords.
- [x] Removed generic `startup` after false-positive evidence.
- [x] Implemented Financial Markets conservatively.
- [x] Ran historical regression.
- [x] Ran targeted tests.
- [x] Ran full test suite.
- [x] Ran real 17 August pipeline.
- [x] Inspected real report.
- [x] Preserved zero recurring cost.
- [x] Preserved credential and copyright constraints.
- [x] Committed and pushed the checkpoint.

## Key Source Decision

```text
Sifted
→ Tech.eu
```

Observed metadata comparison:

```text
Tech.eu → 20/20 tested entries with descriptions
Sifted  → 0/24 tested entries with descriptions
```

## Taxonomy Changes

Added:

```text
Global Politics / Geopolitics
- tariffs

Companies / Corporate Strategy
- acquired

Startups / Venture Capital
- early-stage fund
- funding market
```

Removed:

```text
Startups / Venture Capital
- startup
```

Added domain:

```text
Financial Markets
```

## Status

**Complete and pushed**

---

# Phase 4B — Premium, Institutional and Milan/Bocconi Source Research

## Financial Times

Strategically excellent.

Official RSS exists, but current RSS/persistence terms conflict with permanent archival use.

### Decision

> **Standby — access/persistence conflict.**

---

## Il Sole 24 Ore

Technically strong.

Strongest feed candidates:

```text
Economia
Finanza
```

Collector and normalizer worked without source-specific logic.

Persistence/licensing compatibility remains insufficiently clean.

### Decision

> **Standby.**

This is not a permanent rejection.

---

## Artificial Intelligence Case-Sensitivity Fix

Italian content exposed:

```text
AI
vs
Italian "ai"
```

Current convention:

```text
lowercase keyword
→ case-insensitive

keyword containing uppercase
→ case-sensitive
```

Validation preserved useful English recall while removing false Italian matches.

### Status

**Complete and pushed**

---

## Bank of Italy RSS

Official narrow feeds collected and normalised successfully.

Main weakness:

```text
no RSS descriptions
```

### Decision

> **Standby.**

---

## Bank of Italy BDS

Official structured statistical exports were identified.

A proper integration would require:

```text
series
→ observations
→ release/change detection
→ revisions
→ significance rules
→ intelligence event
→ standard downstream pipeline
```

### Decision

> **Approved future structured-data enhancement — deferred.**

---

## Reuters

Strategically exceptional.

No clean official zero-cost machine-delivery route compatible with the current architecture was identified.

### Decision

> **Standby / production-ineligible under current constraints.**

---

# Phase 4C — Milan/Bocconi First Production Implementation

## Requirement

Milan/Bocconi is a fixed strategic macroarea.

The target is:

> **Professional Ecosystem Intelligence**

not generic local news.

---

## B4i

### Decision

> **Legacy / superseded by Tech Europe Foundation for the first general startup/innovation sensor.**

B4i may only be revisited later if a different structured information function becomes evident, such as high-value programmes/deadlines.

---

## Tech Europe Foundation

Official RSS:

```text
https://tef.tech/news/feed/
```

Without a source default:

```text
9/10 tested records
→ unclassified
```

The correct solution was not generic keywords.

Added domain:

```text
Milan and Bocconi Ecosystem
```

with:

```yaml
keywords: []
```

Added source default:

```text
Tech Europe Foundation
→ Milan and Bocconi Ecosystem
```

No separate opportunity/event architecture was introduced.

### Status

**Complete and pushed**

---

## Bocconi Career Services — Initial Decision

### Decision

> **Manual/private layer.**

Do not automate:

```text
yoU@B
JobGate
```

Later Phase 4 research refined this decision by separately testing the public layer.

---

## Bocconi General Events / News

No clean narrow structured route was identified.

### Decision

> **Do not build a broad Bocconi crawler.**

---

# Phase 4D — Italian Tech Alliance Initial Audit

Official RSS:

```text
https://www.italiantechalliance.com/blog-feed.xml
```

Initial technical sample:

```text
20 entries
20 timestamps
20 links
20 descriptions
0 normalisation errors
```

Product strengths:

- Italian VC statistics;
- investor ecosystem developments;
- startup policy;
- Scaleup Fund;
- Venture Academy;
- Tech Transfer Academy.

Product weaknesses:

- extremely thin descriptions;
- repeated press-clipping stories around the same underlying developments.

### Initial Decision

> **Production-readiness candidate.**

The candidate was revisited during the final Milan/Bocconi gap audit.

---

# Phase 4E — First Gap-Driven Source Audit Batch

Audit batch:

```text
Nasdaq
Federal Reserve Board
MIMIT
Lavoce.info
Bruegel
Assolombarda
Ars Technica
Google DeepMind
```

This batch is complete.

---

## Nasdaq

Strategically valuable for Financial Markets.

Current persistence/legal conditions do not fit permanent public Git archival use.

### Decision

> **Standby — access/persistence conflict.**

---

## Federal Reserve Board Monetary Policy

Official RSS:

```text
https://www.federalreserve.gov/feeds/press_monetary.xml
```

Technical sample:

```text
15 items
15 normalized
15 timestamps
15 descriptions
```

Added:

```text
Federal Reserve Board Monetary Policy
→ Economics and Macroeconomics default
```

Validated Financial Markets keywords:

```text
FOMC
Federal Open Market Committee
discount rate
```

Historical regression:

```text
0 unintended matches
```

### Decision

> **Active.**

---

## Federal Reserve Banking / Regulatory

Technically valid but heterogeneous.

### Decision

> **Standby.**

---

## MIMIT News

Official News RSS was technically strong and strategically differentiated.

Added:

```text
Italy
```

as the tenth domain with:

```yaml
keywords: []
```

MIMIT receives:

```text
Italy source default
```

Validated keywords:

```text
Companies / Corporate Strategy
- tavoli di crisi
- accordo di sviluppo
- quadro industriale
- rilevanza strategica

Economics / Macroeconomics
- inflazione
```

MIMIT also exposed HTML descriptions.

The fix was general:

```text
generic HTML-to-text normalization
```

not a MIMIT-specific branch.

### Decision

> **MIMIT News active.**

---

## MIMIT Incentives

Technically valid but more administrative, sparse and duplicative.

### Decision

> **Standby.**

---

## Lavoce.info

### General Feed

Technically strong but too broad.

### Decision

> **Rejected for production.**

### Banche e Finanza

High quality but sparse and partly overlapping.

### Decision

> **Standby.**

### Imprese

Best differentiated production candidate.

Added source default:

```text
Lavoce.info Imprese
→ Italy
```

Adopted:

```text
Companies / Corporate Strategy
- fusione e acquisizione
- piano industriale

Artificial Intelligence
- IA

Financial Markets
- mercati dei capitali
```

Historical regression:

```text
0 unintended matches
```

### Decision

> **Lavoce.info Imprese active.**

---

## Bruegel

### General RSS

Technically clean but dominated by sessions/conference components.

### Decision

> **Rejected — wrong information function.**

### Analysis / Publications

Malformed feed entities plus very large/full-content descriptions.

### Decision

> **Standby — malformed/full-content feeds incompatible with current architecture.**

No Bruegel-specific parser or persistence path justified.

---

## Assolombarda

Strategically strong for:

- established companies;
- Milan/Lombardy industry;
- local innovation;
- manufacturing AI;
- exports;
- infrastructure.

Tested News:

```text
15 collected
15 normalized
0/15 timestamps
14/15 descriptions
```

Tested Comunicati Stampa:

```text
15 collected
15 normalized
0/15 timestamps
14/15 descriptions
```

### Decision

```text
News
→ Standby

Comunicati stampa
→ Standby

Centro Studi
→ Manual/research layer
```

Do not:

- substitute retrieval time;
- scrape dates from article pages;
- introduce source-specific persistence rules.

---

## Ars Technica

Strategically strong for independent technology/AI reporting.

Current persistence terms do not provide a sufficiently clean basis for permanent public feed-derived storage.

### Decision

> **Standby — access/persistence conflict.**

---

## Google DeepMind News

Official RSS:

```text
https://deepmind.google/blog/rss.xml
```

Technical sample:

```text
100 received
100 normalized
100 timestamps
79 descriptions
```

Added source default:

```text
Google DeepMind News
→ Artificial Intelligence
```

Classification review:

```text
Artificial Intelligence → 100/100
AI only                 → 97/100
multi-domain            → 3/100
```

No new keywords were required.

### Decision

> **Google DeepMind News active.**

---

# Phase 4F — Final Gap-Driven Audit and Phase 4 Closure

## Objective

Test whether the remaining highest-value information gaps could be improved through one or more clean public structured sources before deciding whether richer report context had become the higher-value limitation.

The final controlled sequence focused on:

```text
ISPI
DG Competition
ESMA
Milan/Bocconi complementary sources
```

The result was one additional source activation and several deliberate standby decisions.

This batch provided the evidence required to close Phase 4.

---

# ISPI Audit

## ISPI Geoeconomics

Official RSS:

```text
https://www.ispionline.it/it/ricerca/geoeconomia/feed
```

Real collector probe:

```text
status: success
items received: 10
```

Normalization:

```text
10 normalized
0 errors
```

Initial classification with no source default:

```text
3 classified
7 unclassified
```

No new broad geoeconomic keywords were justified.

Ranking remained:

```text
Tier 3
no source-specific boost
no source default
```

### Decision

> **Active.**

Production configuration:

```text
ISPI Geoeconomics
→ Tier 3
→ no default domains
→ Italian
→ Global / Europe / Italy
```

No production Python changes.

No `domains.yaml` changes.

No new keywords.

---

## ISPI Business Events

Narrow feed:

```text
https://www.ispionline.it/it/tipologia/eventi-per-le-imprese/feed
```

Collector result:

```text
success
10 entries
```

The strategic information value was high.

However, feed publication timestamps were not reliable proxies for:

```text
event date
or
actionability date
```

Some entries appeared after the event had occurred.

### Decision

> **Standby — event/actionability semantics.**

Do not build event/deadline architecture solely for ISPI.

---

# DG Competition Audit

Official broad RSS collected successfully:

```text
30 items
30 normalized
0 normalization errors
```

High-value examples included:

- mergers;
- competition cases;
- antitrust;
- Foreign Subsidies Regulation;
- major company-strategy developments.

The feed also contained substantial routine State-aid material.

Current classifier:

```text
26 classified
4 unclassified
```

Many routine records classified through:

```text
european commission
→ Europe/EU
```

At Tier 1, routine records often became too competitive in ranking.

Narrow Mergers / Antitrust / FSR RSS routes were tested and returned:

```text
404
```

### Decision

> **Standby — product quality / feed breadth.**

Do not:

- remove `european commission` globally;
- add a DG-specific ranking penalty;
- add source-specific inclusion/exclusion rules;
- build a custom Mergers/Antitrust scraper.

---

# ESMA Audit

Official RSS:

```text
https://www.esma.europa.eu/rss.xml
```

Collector result:

```text
success
10 items
```

Raw feed issue:

```text
published: None
updated: None
```

Publication dates existed only inside HTML description payloads.

Descriptions were large and remained long after normalization.

The current normalizer left:

```text
published_at = None
```

so current-window filtering would exclude them.

A non-production simulation showed that long descriptions also produced incidental multi-domain keyword matches.

### Decision

> **Standby — architecture.**

Do not add:

- source-specific timestamp extraction;
- source-specific description trimming;
- ESMA-specific classification rules.

---

# Phase 4G — Final Milan/Bocconi Gap Reassessment

## Tech Europe Foundation

Remains the active automated Milan/Bocconi sensor.

### Decision

> **Active.**

---

## Bocconi Career Services — Public Layer Reassessment

Public pages expose strategically valuable information such as:

- Investment Banking Days;
- Bocconi&Jobs;
- recruiting dates;
- employer events;
- registration windows;
- employer lists.

However:

- the most actionable layer remains partly inside `yoU@B` / JobGate;
- no clean narrow public RSS/Atom/API was established;
- event/application semantics do not naturally map to article publication time.

### Decision

> **High-value manual/private complementary layer; standby for automation.**

---

## Italian Tech Alliance — Deeper Probe

Official RSS remained technically clean.

Live sample showed:

- complete timestamps;
- stable links;
- mostly extremely thin press-clipping descriptions;
- repeated coverage of the same developments;
- occasional high-value programme/deadline content.

### Decision

> **Deferred production-readiness candidate.**

Do not activate merely for source diversification.

Do not give Milan/Bocconi source default.

---

## Fintech District

No clean public RSS/API was established.

The public sitemap is insufficient as a dated 24-hour article feed.

### Decision

> **Standby — structured-access limitation.**

Do not reverse-engineer hidden/internal Next.js APIs.

---

## Camera di Commercio Milano Monza Brianza Lodi

Tested machine endpoints returned:

```text
Incapsula / Imperva HTML interstitial
```

rather than usable structured content.

### Decision

> **Standby — access/architecture.**

Do not bypass the access-control layer.

---

# Phase 4 Completion Assessment

The Phase 4 stopping condition was met.

The system reached:

```text
13 active sources
10 implemented domains
```

with:

- deliberate information roles;
- viable Italy implementation;
- diversified primary AI evidence;
- dedicated Financial Markets monetary/rates evidence;
- materially improved Companies/Corporate Strategy;
- stronger Europe/geoeconomic interpretation;
- more than nominal Milan/Bocconi coverage;
- documented public-source/current-architecture limits.

Remaining gaps are real but no longer evidence that Phase 4 research is incomplete.

## Phase 4 Completion Decision

> **Phase 4 complete for the current MVP boundary.**

Future source work should reopen only when:

1. repeated report use demonstrates a costly information gap;
2. a previously blocked high-value source exposes a materially cleaner endpoint;
3. licensing/persistence conditions improve;
4. a new information need becomes validated;
5. source concentration demonstrably harms report quality.

---

# Phase 5 — Richer-Report Product Design

## Objective

Determine the smallest lawful, deterministic and zero-cost mechanism that provides enough context to understand selected developments without immediate click-through.

The phase began from the validated finding:

> the source universe was sufficient for the current MVP, but selected stories often provided too little context for efficient reading.

## Entry Condition

Phase 4 source/domain expansion complete for the current MVP boundary.

**Passed.**

---

# Phase 5A — Requirement Definition

The product requirement was refined from:

```text
show more description text
```

to:

> **Provide enough source-provided context to understand the core development before immediate click-through when the source metadata permits it.**

Minimum Useful Context should allow the reader to identify:

- what happened or changed;
- who or what is involved;
- at least one material qualifier where the source provides one.

Possible qualifiers include:

- scale;
- magnitude;
- consequence;
- rationale;
- next step;
- constraint;
- economic significance;
- strategic significance.

This is a manual product-quality rubric rather than an automatic score.

### Status

**Complete**

---

# Phase 5B — Thirteen-Source Metadata Audit

A read-only audit was performed across all thirteen active sources using the actual project:

```text
load_sources
collect_source
normalize_entry
```

The audit inspected:

- raw description;
- normalized description;
- summary;
- subtitle;
- `content`;
- description availability;
- description lengths;
- share above 300 characters;
- representative examples.

No production files or generated outputs were modified by the audit.

## Key Findings

### BBC World

```text
20/20 descriptions
median ≈ 110 characters
max ≈ 159
0 above 300
```

No richer distinct summary/content field.

### BBC Business

```text
20/20 descriptions
median ≈ 107
max ≈ 138
0 above 300
```

### ECB

```text
0/15 usable descriptions
```

No richer feed context.

### European Commission Highlighted News

```text
20/20 descriptions
median ≈ 226
max ≈ 290
0 above 300
```

### Istat

```text
10/10 descriptions
median ≈ 74
max ≈ 169
```

Richer `content` existed and was substantially longer.

### OpenAI

```text
20/20 descriptions
median ≈ 150
max ≈ 180
```

### Tech.eu

```text
20/20 descriptions
≈ 203 characters
```

Richer `content` existed and was body-like.

### Tech Europe Foundation

```text
10/10 descriptions
minimum ≈ 446
median ≈ 495
maximum ≈ 555
10/10 above 300
```

This source was materially constrained by the 300-character report cap.

### Federal Reserve Monetary Policy

```text
15/15 descriptions
median ≈ 65
max ≈ 118
```

Descriptions were often title-like.

### MIMIT

```text
10/10 descriptions
median ≈ 94
max ≈ 209
```

### Lavoce.info Imprese

```text
10/10 descriptions
minimum ≈ 330
median ≈ 342
maximum ≈ 359
10/10 above 300
```

The 300-character cap consistently removed some useful context.

### Google DeepMind

```text
11/20 descriptions
median ≈ 110
max ≈ 210
```

Description availability was partial.

### ISPI Geoeconomics

```text
10/10 descriptions
minimum ≈ 259
median ≈ 298
maximum ≈ 424
4/10 above 300
```

Richer body-like `content` was also available.

---

# Phase 5C — Metadata Interpretation

The audit demonstrated:

> **300 characters was not the primary context limitation for most active sources.**

Only:

```text
Tech Europe Foundation
Lavoce.info Imprese
some ISPI Geoeconomics items
```

lost substantial description text because of the 300-character limit.

Several sources were already naturally short.

Other sources were thin because the feed did not provide more metadata.

Therefore:

```text
increase character cap
```

could improve available context but could not solve:

```text
missing metadata
title-only metadata
very thin metadata
```

This prevented the project from treating:

```text
300 → 600
```

as a complete solution.

### Status

**Complete**

---

# Phase 5D — RSS Content Audit

Some active feeds exposed richer:

```text
content
```

fields.

Material examples included:

- Istat;
- Tech.eu;
- Tech Europe Foundation;
- ISPI Geoeconomics.

Observed lengths often ran into thousands of characters.

The fields behaved more like:

```text
article body / page body
```

than:

```text
bounded feed summary
```

Using them generically would have created:

- larger persisted copyrighted payloads;
- possible public-repository persistence problems;
- more incidental classification keywords;
- ranking inflation;
- source-specific complexity.

### Decision

> **Do not generically use RSS `content` for richer reports.**

### Status

**Complete**

---

# Phase 5E — Persistence and Copyright Boundary

The audit and prior source research established:

```text
more technically available text
≠
more text appropriate for permanent public storage
```

The accepted boundary remains:

```text
existing normalized description
→ classification
→ ranking
→ JSONL persistence
→ bounded report rendering
```

Do not create a new body-content persistence path.

Do not treat the richer-context requirement as permission to reproduce article text.

### Status

**Complete**

---

# Phase 5F — Candidate Comparison

Candidate solutions were compared.

## Candidate A — Increase 300 to 600 Only

Benefits:

- simple;
- zero new architecture.

Weaknesses:

- does not solve thin metadata;
- creates less protection against unexpectedly long descriptions;
- truncation remains awkward.

### Decision

**Rejected as the complete solution.**

---

## Candidate B — Increase 300 to 500 Only

Benefits:

- recovers essentially all Lavoce descriptions;
- recovers all tested ISPI descriptions;
- captures typical TEF descriptions;
- remains bounded.

Weakness:

- character-only truncation still creates awkward endings.

### Decision

**Improvement, but incomplete.**

---

## Candidate C — 500 + Deterministic Boundary-Aware Rendering

Design:

```text
500-character maximum
+
complete-sentence preference
+
word-boundary fallback
+
explicit Source context provenance
+
transparent thin-metadata fallback
```

Benefits:

- zero recurring cost;
- no new data model;
- no source-specific parser;
- no article scraping;
- no classification/ranking change;
- deterministic;
- testable;
- bounded.

### Decision

> **Selected.**

---

## Candidate D — Generic RSS `content`

### Decision

**Rejected for current production.**

---

## Candidate E — Article-Page Metadata Extraction

### Decision

**Deferred.**

No validated need remained after selecting the simpler solution.

---

## Candidate F — First-Paragraph / Body Extraction

### Decision

**Rejected for current MVP.**

---

## Candidate G — LLM Summaries

### Decision

**Rejected.**

Would introduce:

- production AI dependency;
- potential recurring cost;
- provenance complexity;
- unnecessary technical sophistication.

---

# Phase 5G — Accepted Design

Final design:

```text
existing normalized description
→ Source context label
→ maximum 500 characters

if description missing
or description == title
→ explicit fallback

if within bound
→ unchanged

if above bound
→ prefer complete sentence
→ otherwise last word boundary + ...
```

Fallback:

```text
No additional source-provided context available.
```

Report breadth remains:

```text
max 5 per domain
max 30 total
```

No changes to:

- `ArticleRecord`;
- classification;
- ranking;
- storage architecture;
- source registry;
- domain registry.

---

# Phase 5 Definition of Done

Phase 5 required:

- explicit context requirement;
- measured metadata baseline;
- defined persistence/copyright boundary;
- simple deterministic candidate;
- fallback behaviour;
- report-length implications;
- provenance;
- acceptance tests;
- known implementation files;
- rejected unnecessary architecture.

All conditions were satisfied.

## Phase 5 Status

> **Complete**

---

# Phase 6 — Richer-Report Implementation and Evaluation

## Objective

Implement the smallest compliant richer-report mechanism selected in Phase 5 and validate both technical correctness and actual report usefulness.

## Entry Condition

Phase 5 design complete.

**Passed.**

---

# Phase 6A — Intended Implementation Scope

The smallest coherent production change required:

```text
config/settings.yaml
src/daily_intelligence/report.py
tests/test_report.py
tests/test_settings_config.py
```

No intended changes were required in:

```text
normalize.py
classify.py
rank.py
models.py
storage.py
pipeline.py
sources.yaml
domains.yaml
```

This scope preserved the architectural conclusion that richer context is a report-presentation change.

---

# Phase 6B — Configuration Change

Changed:

```text
max_description_length
300
→
500
```

Kept:

```text
max_items_per_domain = 5
max_total_items = 30
```

The historical configuration name:

```text
max_description_length
```

remains unchanged.

Its current meaning is the maximum rendered source-context length.

---

# Phase 6C — Report Rendering

Implemented:

```text
**Source context:** ...
```

for report entries.

The source-context line is rendered even when the description is unavailable.

This allows transparent fallback behaviour.

---

# Phase 6D — Missing / Duplicate Context

Implemented:

```text
description is None
or
description equals title after normalized comparison
```

→

```text
No additional source-provided context available.
```

This prevents:

- silent omission;
- headline repetition;
- fabricated context.

---

# Phase 6E — Deterministic Truncation

Implemented:

```text
if len(description) <= max_length
→ return unchanged

otherwise
→ reserve space for ...
→ find latest sentence-ending punctuation within bound
→ return complete sentence when available

otherwise
→ truncate at last word boundary
→ append ...
```

The formatter does not generate new factual content.

---

# Phase 6F — Automated Test Expansion

Report tests now cover:

- short context unchanged;
- complete-sentence truncation;
- word-boundary fallback;
- missing-context fallback;
- title-duplicate fallback;
- report provenance.

Settings configuration tests were updated to expect:

```text
500
```

rather than:

```text
300
```

---

# Phase 6G — First Automated Validation

Targeted report validation:

```text
14 passed
```

Full-suite validation initially exposed one stale settings expectation:

```text
expected 300
actual 500
```

This was correctly identified as a test expectation mismatch.

No production code change was needed.

After correction:

```text
full suite passed
```

---

# Phase 6H — Real Report Validation

A production-equivalent pipeline run was executed on 19 August 2026.

The pipeline successfully collected all thirteen active sources.

Observed collection included:

```text
BBC World
BBC Business
ECB
European Commission
Istat
OpenAI
Tech.eu
Tech Europe Foundation
Federal Reserve
MIMIT
Lavoce.info
Google DeepMind
ISPI
```

The run completed:

```text
status: success
```

and generated:

```text
data/processed/2026/08/2026-08-19.jsonl
data/runs/2026/08/2026-08-19.json
reports/daily/2026/08/2026-08-19.md
```

The richer report remained readable and bounded.

The generated report demonstrated:

- short BBC/OpenAI descriptions remained compact;
- longer source descriptions could expose more context;
- `Source context` provenance was clear;
- report item caps remained unchanged.

---

# Phase 6I — Spacing Diagnostic

Initial terminal output appeared to contain joined words such as:

```text
JohnHealey
reportedmissing
newsafeguards
AI,and
```

and some malformed Tech.eu snippets.

The correct development response was to diagnose the transformation path rather than immediately retain a broad normalization change.

A temporary generic inline-HTML spacing experiment was tested.

Further diagnostics then established:

## BBC / OpenAI

Raw feed descriptions contained correct spacing.

`_normalize_description()` returned correct spacing.

Persisted JSONL contained correct spacing.

Literal Python inspection of the Markdown file confirmed:

```text
John Healey
reported missing
new safeguards
AI, and
```

and confirmed that the joined forms were absent.

Conclusion:

> the apparent BBC/OpenAI defects were terminal/paste presentation artefacts, not production-data defects.

## Tech.eu

Direct live-feed inspection showed malformed strings already present in the raw RSS description, including patterns such as:

```text
raised$8
platformin
withparticipa...
Edinburgh-basedsemiconductor
anoversubscribed
nextgeneration
```

Conclusion:

> these are publisher/source-metadata limitations.

They do not justify speculative generic word repair.

## Final Decision

The temporary normalization experiment and its synthetic tests were removed.

`normalize.py` returned to the existing validated implementation.

This preserved the smallest justified Phase 6 scope.

---

# Phase 6J — Final Automated Validation

After removing the speculative normalization change:

```text
tests/test_feed_fixture.py
→ 20 passed

tests/test_report.py
→ 14 passed

full suite
→ 122 passed

git diff --check
→ clean
```

No unintended remaining modifications existed in:

```text
src/daily_intelligence/normalize.py
tests/test_feed_fixture.py
```

---

# Phase 6K — Final Production-Equivalent Run

A final production-equivalent run was executed after the cleanup.

Result:

```text
13 active sources
13 successful
0 failed

1448 valid
0 invalid

50 inside rolling collection window
45 unique
28 unclassified

status: success
```

Outputs were written successfully to:

```text
data/processed/2026/08/2026-08-19.jsonl
reports/daily/2026/08/2026-08-19.md
data/runs/2026/08/2026-08-19.json
```

The small difference between earlier and later same-day rolling-window counts is expected because:

```text
window end = actual execution time
```

and the later validation run occurred several minutes later.

---

# Phase 6 Acceptance Assessment

The Phase 6 implementation satisfies the current acceptance condition.

## Requirement

Provide enough source-provided context to understand the core development without immediate click-through when source metadata permits it.

### Passed

The report now provides up to 500 characters of bounded source context.

---

## Zero Recurring Cost

### Passed

No paid API or external service added.

---

## Deterministic Behaviour

### Passed

Formatting and fallback rules are deterministic.

---

## Provenance

### Passed

Report labels publisher/source metadata as:

```text
Source context
```

---

## Thin Metadata

### Passed

Missing/title-duplicate descriptions receive an explicit fallback.

---

## Copyright / Persistence

### Passed

No generic body-content ingestion added.

No authenticated/premium text added.

---

## Classification / Ranking Stability

### Passed

No classifier or ranking logic was changed.

---

## Report Length

### Passed for current MVP checkpoint

The item-count caps remain unchanged.

The real report remained manageable.

---

## Technical Tests

### Passed

```text
20 feed-fixture tests
14 report tests
122 total tests
```

---

## Real Pipeline

### Passed

```text
13/13 sources successful
0 invalid
status success
```

---

## Real Output Inspection

### Passed

The generated report was manually reviewed.

---

# Phase 6 Status

> **Implementation complete and locally validated.**

The only remaining work in the current checkpoint is:

```text
documentation reconciliation
→ final diff inspection
→ staging discipline
→ commit
→ push
→ refresh canonical sources
```

This is closeout work, not new Phase 6 product development.

---

# Phase 7 — Optional Delivery and Interface Improvements

## Objective

Improve report delivery or interface only if repository-native Markdown becomes a demonstrated usability constraint.

Potential future options:

- stable latest-report link;
- GitHub Issues;
- GitHub Pages;
- weekly archive summaries;
- opportunity-specific views.

Excluded by default:

- paid APIs;
- automated ChatGPT integration;
- authenticated premium-content ingestion;
- private email ingestion;
- unrestricted article extraction;
- autonomous agents;
- RAG;
- vector databases;
- complex cloud infrastructure;
- sophisticated frontend;
- dedicated mobile application.

## Entry Condition

Phase 7 should **not** start automatically after Phase 6.

It requires evidence that:

```text
current repository-native report delivery
→ causes meaningful recurring usability cost
```

## Status

**Deferred / optional**

---

# Current Production Source Registry

Current active production sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Tech.eu;
8. Tech Europe Foundation;
9. Federal Reserve Board Monetary Policy;
10. MIMIT News;
11. Lavoce.info Imprese;
12. Google DeepMind News;
13. ISPI Geoeconomics.

Current working position:

| Source | Current Position |
|---|---|
| BBC News World | Retain |
| BBC News Business | Retain; broad business layer |
| European Central Bank | Core |
| European Commission Highlighted News | Core/selective institutional evidence |
| Istat Press Releases | Core |
| OpenAI News | Active frontier-lab primary source |
| Tech.eu | Active European startup/technology specialist |
| Tech Europe Foundation | Active Milan/Bocconi startup/innovation ecosystem source |
| Federal Reserve Board Monetary Policy | Active US monetary-policy primary source |
| MIMIT News | Active Italy industrial/company-policy primary source |
| Lavoce.info Imprese | Active independent Italian business-analysis source |
| Google DeepMind News | Active second frontier-lab AI primary source |
| ISPI Geoeconomics | Active specialist geoeconomic interpretation source |

Current language balance:

```text
English-language feeds → 10
Italian-language feeds → 3
```

This is not a quota.

---

# Current Domain Universe

Implemented:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Companies and Corporate Strategy;
4. Artificial Intelligence;
5. Technology and Software;
6. Startups and Venture Capital;
7. Europe and the European Union;
8. Financial Markets;
9. Milan and Bocconi Ecosystem;
10. Italy.

All ten strategic macroareas now have production configuration.

All ten are sufficient for the current MVP boundary.

This does **not** mean they are equally mature or complete.

---

# Current Domain Coverage Diagnosis

## Global Politics and Geopolitics

Current:

```text
BBC World
+ European Commission spillover
+ selective ISPI Geoeconomics contribution
```

Assessment:

> **MVP-sufficient, publisher-concentrated.**

Not a current development priority.

---

## Economics and Macroeconomics

Current:

```text
ECB
Federal Reserve Board Monetary Policy
Istat
European Commission
BBC Business
Lavoce.info spillover
ISPI Geoeconomics spillover
```

Assessment:

> **Strong primary evidence and sufficient MVP maturity.**

Independent interpretation remains thinner than institutional evidence.

---

## Companies and Corporate Strategy

Current:

```text
BBC Business
Tech.eu
MIMIT News
Lavoce.info Imprese
```

Assessment:

> **MVP-sufficient baseline, globally incomplete.**

Remaining gap:

```text
international corporate strategy
M&A
capital allocation
corporate financing
major company developments
```

DG Competition validated the information function but failed the current product-quality threshold.

---

## Financial Markets

Current:

```text
Federal Reserve Board Monetary Policy
Lavoce.info selective capital-markets analysis
ECB spillover
BBC Business spillover
```

Assessment:

> **MVP-sufficient baseline, broader markets incomplete.**

Remaining gap:

```text
capital markets
credit
corporate financing
market structure
settlement
broader securities-market supervision
```

ESMA validated the information value but failed current architecture compatibility.

---

## Artificial Intelligence

Current:

```text
OpenAI News
Google DeepMind News
Tech.eu/BBC spillover
ISPI selective spillover
```

Assessment:

> **Primary-source diversity achieved and MVP-sufficient.**

Remaining role:

```text
independent reporting / scrutiny
```

Do not add more first-party labs merely to increase source count.

---

## Technology and Software

Current:

```text
Tech.eu
OpenAI spillover
DeepMind spillover
BBC spillover
ISPI spillover
```

Assessment:

> **Moderate and MVP-sufficient.**

Independent systems/software reporting remains desirable but non-blocking.

---

## Startups and Venture Capital

Current:

```text
Tech.eu
Tech Europe Foundation
```

Assessment:

> **MVP-sufficient, still concentrated.**

Italian Tech Alliance remains a deferred production-readiness candidate.

---

## Europe and the EU

Current:

```text
ECB
European Commission
Tech.eu selective coverage
ISPI Geoeconomics
```

Assessment:

> **Strong primary evidence with partial independent interpretation.**

No immediate expansion requirement.

---

## Italy

Current:

```text
Istat
MIMIT News
Lavoce.info Imprese
ISPI selective spillover
```

Assessment:

> **Viable first production implementation and MVP-sufficient.**

Remaining maturity gaps:

- banking;
- broader capital markets;
- major-company reporting;
- Milan/Lombardy established-company intelligence.

---

## Milan and Bocconi Ecosystem

Current:

```text
Tech Europe Foundation
```

plus complementary manual/private Career Services access.

Assessment:

> **MVP-sufficient but deliberately incomplete.**

Remaining roles:

- recruiting;
- employer events;
- finance ecosystem;
- consulting ecosystem;
- established companies;
- industrial ecosystem;
- opportunity/deadline discovery.

Current audits show several of these roles are constrained by:

- authentication;
- missing structured feeds;
- event semantics;
- access controls;
- source-specific complexity.

---

# Sources Not Worth Current Development Time Without New Evidence

Do not currently prioritise:

- Sifted;
- Financial Times under current RSS archival terms;
- Reuters under current zero-cost machine-delivery constraints;
- Nasdaq under current persistence terms;
- Il Sole 24 Ore without a cleaner persistence route;
- Bruegel useful feeds under the current full-content/malformed architecture;
- Assolombarda under current timestamp/persistence constraints;
- Ars Technica under current persistence terms;
- DG Competition under the current broad-feed/noise structure;
- ESMA under the current timestamp/description structure;
- ISPI Business Events without event/actionability semantics;
- Fintech District without a clean structured public endpoint;
- Camera di Commercio Milano under current machine-access conditions;
- broad Bocconi crawlers;
- authenticated Bocconi Career Services automation;
- generic Politecnico event feeds;
- multiple additional central banks;
- multiple additional first-party AI labs;
- generic press-release aggregators;
- weak general business-news substitutes merely to increase source count.

Reconsider only if:

- source terms change;
- an official structured endpoint changes materially;
- actual report use demonstrates a costly gap;
- a general architecture is independently justified by multiple sources.

---

# Current Stable Validation Record

## Core Pipeline

Validated:

- deterministic collection;
- normalization;
- validation;
- rolling publication-window filtering;
- exact deduplication;
- deterministic classification;
- deterministic ranking;
- JSONL persistence;
- Markdown reporting;
- run summaries;
- failure isolation;
- GitHub automation.

Status:

> **Passed and production-operational.**

---

## Tech.eu / Financial Markets

Validated:

- collection;
- normalisation;
- metadata comparison;
- source-default simulation;
- keyword simulation;
- historical regression;
- Financial Markets activation;
- full tests;
- real pipeline;
- report review.

Status:

> **Passed and pushed.**

---

## AI Case-Sensitivity Fix

Validated:

- Italian false-positive reproduction;
- historical English AI recall;
- targeted tests;
- full suite;
- live Italian-source reruns.

Status:

> **Passed and pushed.**

---

## TEF / Milan-Bocconi

Validated:

- endpoint;
- collector;
- normalizer;
- empty-keyword domain;
- source-default classification;
- ranking;
- tests;
- real pipeline.

Status:

> **Passed and pushed.**

---

## Federal Reserve Monetary Policy

Validated:

- official RSS;
- rights/persistence;
- collector;
- normalizer;
- source default;
- Financial Markets keywords;
- historical regression;
- targeted tests;
- full suite;
- real pipeline.

Status:

> **Passed and pushed.**

---

## MIMIT / Italy

Validated:

- official RSS;
- source-default Italy architecture;
- Italian keywords;
- historical regression;
- general HTML-to-text normalization;
- targeted tests;
- full suite;
- real pipeline.

Status:

> **Passed and pushed.**

---

## Lavoce.info Imprese

Validated:

- official RSS;
- feed comparison;
- source-default Italy architecture;
- bilingual keyword testing;
- historical regression;
- tests;
- real pipeline.

Status:

> **Passed and pushed.**

---

## Google DeepMind News

Validated:

- official RSS;
- 100-record technical sample;
- timestamp completeness;
- metadata-size/persistence compatibility;
- classification review;
- no-keyword decision;
- tests;
- real pipeline.

Status:

> **Passed and pushed.**

---

## ISPI Geoeconomics

Validated:

- official RSS;
- collector;
- normalizer;
- conservative classification;
- ranking;
- candidate-keyword review;
- historical overlap check;
- cadence review;
- tests;
- real pipeline.

Status:

> **Passed and pushed.**

---

## Richer Report

Validated:

- read-only 13-source metadata/context audit;
- source-description availability;
- description-length distributions;
- `content`-field inspection;
- persistence/copyright boundary;
- candidate comparison;
- 500-character decision;
- provenance decision;
- fallback decision;
- sentence-aware truncation;
- word-boundary fallback;
- missing-context test;
- title-duplicate test;
- report-specific automated suite;
- full automated suite;
- production-equivalent pipeline;
- real report inspection;
- spacing diagnostics;
- removal of speculative normalization change;
- clean final diff check.

Latest automated validation:

```text
tests/test_feed_fixture.py
→ 20 passed

tests/test_report.py
→ 14 passed

full suite
→ 122 passed
```

Latest production-equivalent validation:

```text
13 active sources
13 successful
0 failed
0 invalid
status success
```

Status:

> **Passed locally; documentation/Git closeout in progress.**

---

# Lessons Confirmed by Phase 5 and Phase 6

## 1. Measure Before Expanding

Initial hypothesis:

```text
300 characters
→ main report-context problem
```

Audit result:

```text
true for some sources
not true for most sources
```

### Consequence

Do not choose a new limit without measuring real metadata.

---

## 2. Thin Metadata and Truncation Are Different Problems

Examples:

```text
TEF / Lavoce
→ useful source text exists
→ display cap was limiting

ECB
→ source text does not exist
→ cap increase cannot help
```

### Consequence

Do not treat all context limitations as one problem.

---

## 3. Longer Feed Fields Are Not Automatically Better Inputs

Some `content` fields were thousands of characters long.

### Consequence

Do not expand:

```text
description
→ body-like content
```

without considering:

- classification;
- ranking;
- persistence;
- copyright.

---

## 4. Presentation Can Be the Correct Layer

The user need was:

```text
understand selected stories better
```

not:

```text
classify using more article text
```

### Consequence

Report-only formatting was preferable to changing the data model.

---

## 5. Explicit Missing Context Is Better Than Fabricated Context

### Consequence

Use:

```text
No additional source-provided context available.
```

rather than pretending every source provides the same metadata depth.

---

## 6. Provenance Matters

The displayed text is publisher/source metadata.

### Consequence

Use:

```text
Source context
```

rather than implying independently generated summary content.

---

## 7. Diagnose the Actual Transformation Layer

The apparent spacing issue initially looked like a generic HTML-normalization defect.

Direct inspection showed:

```text
BBC / OpenAI
→ correct throughout pipeline and file

Tech.eu
→ malformed upstream RSS metadata
```

### Consequence

Do not retain a shared parser change merely because a synthetic test can demonstrate a hypothetical failure.

Locate the real defect before changing shared code.

---

## 8. Source Defects Can Remain Source Defects

### Consequence

Do not create brittle rules that guess:

```text
platformin
→ platform in

basedsemiconductor
→ based semiconductor
```

without reliable structural evidence.

---

## 9. More Context Does Not Require More Items

The current report-selection caps remain:

```text
5 per domain
30 total
```

### Consequence

Do not change breadth and depth simultaneously unless real use requires it.

---

## 10. Technical Success Is Still Not Enough

Phase 6 required:

```text
tests
+
real pipeline
+
real report inspection
+
literal file diagnostics
```

### Consequence

A passing suite alone is insufficient for report-quality changes.

---

# Documentation Ownership

To avoid duplication:

```text
00 Project Brief
→ purpose, constraints, strategic direction

01 Product Requirements
→ user-facing behaviour and acceptance

02 System Architecture
→ implemented technical behaviour

03 Information Taxonomy and Source Policy
→ source/domain policy and source-audit decisions

04 Development Roadmap and Status
→ completed work, current checkpoint and next action
```

Detailed source-audit rationale belongs in:

```text
03 Information Taxonomy and Source Policy.md
```

Detailed richer-report technical architecture belongs in:

```text
02 System Architecture.md
```

Detailed user-facing richer-context acceptance criteria belong in:

```text
01 Product Requirements.md
```

This roadmap should record only enough detail to control sequencing and establish the validation checkpoint.

`00 Project Brief.md` does not require an update for Phase 6 because:

- project purpose is unchanged;
- hard constraints are unchanged;
- operating model is unchanged;
- strategic scope is unchanged.

---

# Current Working Tree Checkpoint

Before documentation updates, the validated implementation working tree contained:

```text
M .obsidian/workspace.json
M config/settings.yaml
M src/daily_intelligence/report.py
M tests/test_report.py
M tests/test_settings_config.py
?? data/processed/2026/08/2026-08-19.jsonl
?? data/runs/2026/08/2026-08-19.json
?? reports/daily/2026/08/2026-08-19.md
```

Intended Phase 6 implementation changes:

```text
config/settings.yaml
src/daily_intelligence/report.py
tests/test_report.py
tests/test_settings_config.py
```

Expected generated validation outputs:

```text
data/processed/2026/08/2026-08-19.jsonl
data/runs/2026/08/2026-08-19.json
reports/daily/2026/08/2026-08-19.md
```

Unrelated local file:

```text
.obsidian/workspace.json
```

must remain excluded from the project checkpoint.

After documentation replacement, expected documentation changes are:

```text
docs/project/01 Product Requirements.md
docs/project/02 System Architecture.md
docs/project/03 Information Taxonomy and Source Policy.md
docs/project/04 Development Roadmap and Status.md
```

No intended Phase 6 changes remain in:

```text
src/daily_intelligence/normalize.py
tests/test_feed_fixture.py
```

---

# Immediate Next Actions

## 1. Finish Canonical Documentation Closeout

Replace:

```text
docs/project/01 Product Requirements.md
docs/project/02 System Architecture.md
docs/project/03 Information Taxonomy and Source Policy.md
docs/project/04 Development Roadmap and Status.md
```

with the updated versions reflecting:

```text
Phase 5 complete
Phase 6 implemented and validated
500-character Source context
deterministic sentence/word-aware truncation
transparent fallback
no RSS content/body ingestion
no classification/ranking expansion
no production AI
```

Do not update:

```text
docs/project/00 Project Brief.md
```

because no strategic project-level decision changed.

---

## 2. Inspect Repository Status

Run:

```text
git status --short
```

Expected intended groups:

```text
implementation
documentation
generated 19 August outputs
```

and separately:

```text
.obsidian/workspace.json
```

which must remain excluded.

---

## 3. Inspect the Full Diff

Inspect at minimum:

```text
config/settings.yaml
src/daily_intelligence/report.py
tests/test_report.py
tests/test_settings_config.py

docs/project/01 Product Requirements.md
docs/project/02 System Architecture.md
docs/project/03 Information Taxonomy and Source Policy.md
docs/project/04 Development Roadmap and Status.md

data/processed/2026/08/2026-08-19.jsonl
data/runs/2026/08/2026-08-19.json
reports/daily/2026/08/2026-08-19.md
```

Verify:

- 500-character production setting;
- unchanged report item caps;
- explicit `Source context`;
- explicit no-context fallback;
- deterministic sentence/word truncation;
- no normalization changes;
- no classification/ranking changes;
- no source/domain changes;
- documentation consistently marks Phase 5 complete;
- documentation consistently marks Phase 6 implementation validated;
- no document still says the report cap is 300 characters;
- no document still says Phase 6 is deferred;
- no document says generic RSS `content` is used;
- no document claims all domains are complete;
- no `.obsidian` change enters the intended diff.

---

## 4. Run Final Static Diff Validation

Run:

```text
git diff --check
```

Expected:

```text
no output
```

---

## 5. Final Automated Validation

The current implementation has already passed:

```text
122 tests
```

after the last intended code change.

If documentation replacement is the only work performed after that test run, another live pipeline run is unnecessary.

A final:

```text
PYTHONPATH=src pytest -q
```

may be used as the final pre-commit verification layer.

Do not rerun the production-equivalent pipeline merely for ceremony if implementation files have not changed.

---

## 6. Decide Generated Output Inclusion

The 19 August production-equivalent run generated:

```text
data/processed/2026/08/2026-08-19.jsonl
data/runs/2026/08/2026-08-19.json
reports/daily/2026/08/2026-08-19.md
```

These are normal repository-native production artefacts.

Before staging, inspect them and confirm they are intended to become the 19 August historical checkpoint rather than being superseded by an automated production commit.

Do not stage them blindly merely because they were created during validation.

---

## 7. Stage Only Intended Files

Do not use:

```text
git add .
```

while:

```text
.obsidian/workspace.json
```

remains modified.

Stage explicit intended paths only after the final diff has been inspected.

---

## 8. Commit and Push

The Phase 6 closeout commit should capture:

```text
richer source context
+
deterministic report formatting
+
tests
+
canonical documentation
+
intended generated outputs if approved
```

Exact `git add`, `git commit` and `git push` commands should be produced only after the final status/diff establishes the exact intended file set.

---

## 9. Refresh Canonical Project Sources

After the commit is pushed:

- refresh/upload the four updated canonical project documents;
- ensure project sources match repository state;
- use those refreshed documents as the starting point for future development work.

---

# Next Highest-ROI Development Step

After the Phase 6 checkpoint is committed and pushed:

> **Use the richer report in normal operation and gather evidence before starting another feature phase.**

Do not automatically proceed to:

- Phase 7 interface work;
- another source-research cycle;
- article-page enrichment;
- LLM summaries;
- near-duplicate clustering;
- opportunity/deadline architecture.

The next development question should be driven by real use.

Examples of evidence worth monitoring:

```text
Do selected stories still require too many immediate clicks?

Are reports now too long?

Are important developments still missing because source metadata is thin?

Does source concentration materially reduce usefulness?

Do duplicate stories become distracting?

Does the rolling 24-hour window cause repeated or missed intelligence?

Does Milan/Bocconi miss opportunities with material user cost?

Does repository-native Markdown become inconvenient enough to justify another delivery layer?
```

Only after one of these becomes a repeated meaningful limitation should a new implementation phase be opened.

---

# Current Status Summary

```text
Phase 0  Complete
Phase 1  Complete
Phase 2  Complete
Phase 3  Complete
Phase 4  Complete for current MVP boundary
Phase 5  Complete
Phase 6  Implementation complete and locally validated
Phase 7  Optional / deferred
```

Current production checkpoint:

```text
13 active sources
10 active domains

collect
→ normalize
→ validate
→ filter
→ deduplicate
→ classify
→ rank
→ store
→ report
→ persist automatically
```

Current report-context checkpoint:

```text
existing normalized description
→ Source context
→ max 500 characters
→ complete sentence preferred
→ word-boundary fallback
→ explicit no-context fallback
```

Current exclusions:

```text
no new record field
no RSS body-content ingestion
no article scraping
no production AI
no LLM summary
no ranking redesign
no classification redesign
no source expansion
no item-cap increase
```

Latest validation:

```text
20 feed-fixture tests passed
14 report tests passed
122 full-suite tests passed

13/13 active sources successful
0 invalid records
production-equivalent run status: success
```

Current immediate priority:

> **Finish the documentation/Git closeout and commit the validated Phase 6 checkpoint.**

After that:

> **observe normal report use before deciding what, if anything, deserves to be built next.**

---

# Changelog

## 2026-08-19 — Phase 5 Complete / Phase 6 Richer-Report Implementation Validated

- Completed the Phase 5 read-only metadata/context audit across all thirteen active production sources.
- Measured real description availability and approximate description-depth patterns.
- Confirmed that the former 300-character cap was not the dominant limitation across most sources.
- Confirmed that Tech Europe Foundation, Lavoce.info Imprese and some ISPI descriptions lost useful context under the 300-character display bound.
- Confirmed that ECB had no useful description in the tested sample.
- Confirmed that Federal Reserve descriptions were often title-like.
- Confirmed partial description availability for Google DeepMind.
- Audited richer RSS `content` fields.
- Confirmed body-like `content` fields for Istat, Tech.eu, Tech Europe Foundation and ISPI.
- Rejected generic RSS `content` ingestion because of persistence, copyright, classification and ranking risk.
- Defined Minimum Useful Context as:
  - core development;
  - actor/object;
  - material qualifier where available.
- Selected `Source context` as the report provenance label.
- Selected:
  - 500-character maximum;
  - complete-sentence preference;
  - word-boundary fallback;
  - explicit no-context fallback.
- Kept report item caps unchanged at:
  - 5 per domain;
  - 30 total.
- Rejected:
  - 600-character-only solution;
  - generic RSS body-content ingestion;
  - article-body extraction;
  - first-paragraph scraping;
  - LLM summaries;
  - a new context field.
- Closed Phase 5 as complete.
- Implemented Phase 6 through:
  - `config/settings.yaml`;
  - `src/daily_intelligence/report.py`;
  - `tests/test_report.py`;
  - `tests/test_settings_config.py`.
- Increased `max_description_length` from 300 to 500.
- Added explicit `Source context` rendering.
- Added explicit missing/title-duplicate fallback:
  - `No additional source-provided context available.`
- Added deterministic sentence-aware truncation.
- Added deterministic word-boundary fallback.
- Updated settings tests for the 500-character production value.
- Added report tests for:
  - unchanged short context;
  - sentence-boundary truncation;
  - word-boundary truncation;
  - missing context;
  - title-duplicate context;
  - provenance.
- Diagnosed a failed missing-context test and corrected report control flow so fallback rendering occurs even when the description is absent.
- Diagnosed the stale settings test expecting 300 and updated the assertion to 500.
- Ran a real production-equivalent report.
- Investigated apparent source-context spacing defects.
- Confirmed BBC/OpenAI raw feed text, normalization, persisted JSONL and literal Markdown output were correctly spaced.
- Confirmed apparent BBC/OpenAI joined words came from terminal/paste presentation rather than the production pipeline.
- Confirmed malformed Tech.eu word spacing already exists in raw RSS description metadata.
- Removed a temporary speculative generic normalization change and its tests after diagnostics showed it was not justified by the production defect.
- Preserved `normalize.py` and feed-fixture behaviour unchanged from the validated baseline.
- Final targeted validation:
  - `20 passed` in `tests/test_feed_fixture.py`;
  - `14 passed` in `tests/test_report.py`.
- Final full validation:
  - `122 passed`.
- Confirmed clean `git diff --check`.
- Ran the final 19 August production-equivalent pipeline:
  - 13 active;
  - 13 successful;
  - 0 failed;
  - 1448 valid;
  - 0 invalid;
  - 50 inside window;
  - 45 unique;
  - 28 unclassified;
  - status success.
- Confirmed Phase 6 implementation acceptance for the current MVP.
- Set documentation reconciliation, diff inspection, commit and push as the current closeout step.
- Set evidence from normal richer-report use as the trigger for any future development phase.

## 2026-08-18 — Thirteen-Source / Phase-4 Closure and Phase-5 Entry

- Updated active production sources from twelve to thirteen.
- Added ISPI Geoeconomics as the thirteenth active source.
- Kept ISPI Geoeconomics at Tier 3.
- Added no source-default domain for ISPI.
- Added no ISPI-specific keywords.
- Added no ISPI-specific collector or parser.
- Validated ISPI through:
  - real collector;
  - 10-item live sample;
  - 10/10 normalization;
  - classification review;
  - candidate-keyword historical searches;
  - ranking review;
  - cadence review;
  - historical overlap review;
  - configuration tests;
  - full automated suite;
  - real 13-source production-equivalent run.
- Recorded the full-suite validation:
  - `118 passed`.
- Recorded the 18 August 2026 production-equivalent run:
  - 13 active;
  - 13 successful;
  - 0 failed;
  - 0 invalid;
  - 0 warnings;
  - 1442 valid;
  - 45 inside window;
  - 43 unique;
  - 37 unclassified;
  - 6 displayed;
  - status success.
- Audited ISPI Business Events.
- Kept ISPI Business Events on standby because publication time is not a reliable event/actionability date.
- Audited DG Competition.
- Confirmed excellent M&A/antitrust/company-strategy value.
- Confirmed 30/30 normalisation for the broad RSS.
- Confirmed excessive routine State-aid classification/ranking under the current Europe evidence.
- Tested narrow Mergers/Antitrust/FSR feed routes and found no usable RSS endpoints.
- Kept DG Competition on standby rather than introducing source-specific filtering or ranking.
- Audited ESMA.
- Confirmed strong Financial Markets information value.
- Confirmed RSS collection but missing standard publication timestamps.
- Confirmed long description payloads and incidental keyword inflation.
- Kept ESMA on standby rather than introducing source-specific timestamp/description logic.
- Reassessed Milan/Bocconi MVP maturity.
- Revisited Italian Tech Alliance with a live 20-item feed probe.
- Confirmed technically clean timestamps but heavy thin press-clipping repetition.
- Kept Italian Tech Alliance as a deferred production-readiness candidate.
- Researched the public Bocconi Career Services layer.
- Confirmed strong public recruiting/employer-event value but no clean narrow structured feed and a partly authenticated action layer.
- Preserved authenticated Career Services as manual/private.
- Audited Fintech District.
- Confirmed strong Milan fintech ecosystem relevance.
- Found no usable RSS/API.
- Kept sitemap-only structure insufficient for current 24-hour ingestion.
- Rejected Next.js internal API reverse engineering.
- Audited Camera di Commercio Milano Monza Brianza Lodi.
- Confirmed strong local-company/business ecosystem value.
- Found Incapsula/Imperva interstitial responses across tested machine endpoints.
- Rejected access-control bypass.
- Reclassified Milan/Bocconi as MVP-sufficient but deliberately incomplete.
- Recorded the current public-source/current-architecture ceiling for several missing professional/business roles.
- Reclassified Companies/Corporate Strategy as MVP-sufficient baseline but globally incomplete.
- Reclassified Financial Markets as MVP-sufficient baseline but broader-markets incomplete.
- Preserved AI as primary-source diverse with independent scrutiny incomplete.
- Preserved Startups/VC as MVP-sufficient but concentrated.
- Recorded ISPI as a partial improvement to independent Europe/geoeconomic interpretation.
- Closed the active Phase 4 source-expansion cycle.
- Set Phase 5 richer-report product design as the active next phase.

## 2026-08-18 — Twelve-Source / Ten-Domain Production Checkpoint

- Added Federal Reserve Board Monetary Policy.
- Added MIMIT News.
- Added Italy as the tenth domain.
- Added Lavoce.info Imprese.
- Added Google DeepMind News.
- Validated bilingual classification.
- Added generic HTML-to-text description normalization.
- Completed Nasdaq, Bruegel, Assolombarda and Ars Technica audits.
- Ran successful twelve-source production-equivalent validation.
- Reframed source gaps from basic implementation blockers to maturity limitations.

## 2026-08-17 — Source Expansion and Milan/Bocconi Implementation

- Replaced Sifted with Tech.eu.
- Added Financial Markets.
- Added Tech Europe Foundation.
- Added Milan and Bocconi Ecosystem.
- Added empty-keyword domain support.
- Added deterministic keyword case semantics.
- Validated the Premium Bocconi Exception.
- Completed initial source-research sequence.
- Established historical processed records as the taxonomy regression corpus.

## 2026-08-14 — Phase 3 Automation Complete

- Added GitHub Actions production workflow.
- Validated manual and scheduled execution.
- Added automated testing before production execution.
- Added output validation.
- Added automated bot persistence.
- Added no-change guard.
- Added critical-failure protection.
- Added degraded-run publication.
- Added concurrency protection.
- Recorded scheduled-trigger latency limitation.
- Transitioned development priority from infrastructure to information quality.

## 2026-08-11 — Phase 2 Real-Source Production Readiness Complete

- Replaced fixture-only validation with seven real public RSS sources.
- Expanded implemented taxonomy to seven domains.
- Added bounded remote HTTP retrieval.
- Added explicit request headers.
- Added source failure isolation.
- Validated real publication timestamps.
- Corrected broad source-default assumptions.
- Validated degraded-source behaviour.
- Closed real-source production-readiness gate.

## 2026-08-11 — Phase 1 Local Vertical Slice Complete

- Implemented the complete local collection-to-report pipeline.
- Added deterministic storage, reporting and run summaries.
- Added CLI and logging.
- Added automated tests.
- Established the controlled development loop:
  - run;
  - inspect;
  - identify defect;
  - smallest correction;
  - test;
  - inspect again.
- Closed Phase 1 with 104 passing tests.

## Initial Roadmap Baseline

- Defined phased implementation strategy.
- Established zero-cost, deterministic, public-safe architecture.
- Established completion-before-sophistication principle.
- Defined Git/tests as the verification layer.
- Defined repository-native storage and Markdown reporting as the MVP delivery model.