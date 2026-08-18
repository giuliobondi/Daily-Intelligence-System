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

The project should not move to implementation of a new phase until the current design requirement has a clear acceptance condition.

---

# Current Project Status

| Field | Current Status |
|---|---|
| Project Phase | Phase 5 — Richer-Report Product Design |
| Current Milestone | Milestone 5 — Design the smallest lawful, deterministic and zero-cost richer-context mechanism before implementation |
| Repository Status | Public Python repository with automated GitHub-native daily execution and repository-native historical outputs |
| Implementation Status | Deterministic collect → normalize → validate → filter → deduplicate → classify → rank → store → report pipeline implemented and production-validated |
| Automation Status | GitHub Actions implemented; manual and scheduled execution validated; outputs persisted automatically |
| Production Schedule | Daily at 06:05 Europe/Rome; GitHub scheduling latency remains an observed operational limitation |
| Source Registry | Thirteen active production sources |
| Taxonomy Status | Ten implemented domains; all ten strategic macroareas have production configuration |
| Domain Maturity | All ten domains are sufficient for the current MVP boundary, but several remain intentionally incomplete |
| Testing Status | 118 automated tests passed at the latest implementation checkpoint |
| Latest Local Validation | Real 18 August 2026 production-equivalent run completed successfully with 13/13 sources successful |
| Latest Integration Result | ISPI Geoeconomics collected successfully through the standard pipeline; its current feed records were outside the tested 24-hour window and did not leak into current outputs |
| Current Product-Quality Finding | Further speculative source expansion now has lower expected value than improving the context of already-selected stories |
| Current Blockers | No automation blocker; Phase 5 requires a careful richer-context design before implementation |
| Current Priority | Complete and commit the Phase 4 closeout checkpoint, refresh canonical project sources, then begin richer-report design |
| Current Git State | ISPI implementation validated locally; documentation closeout in progress; unrelated `.obsidian/workspace.json` change must remain excluded |

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

After the final gap-driven audits, the answer is now:

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

## Target Information Functions

ISPI was evaluated for two distinct roles:

```text
Geoeconomics
→ economic security
→ trade
→ industrial policy
→ strategic dependencies
→ technology competition
→ business implications of geopolitical developments

Business Events
→ Milan professional events
→ business/geoeconomic events
→ executive/networking opportunities
```

---

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

The useful subset was recovered through existing AI/Technology evidence.

Generic geopolitical material often remained unclassified.

No new broad geoeconomic keywords were justified.

Historical candidate-keyword searches found insufficient evidence to safely add terms such as:

```text
economic security
industrial policy
supply chain
semiconductors
foreign exchange
```

Ranking:

```text
Tier 3
no source-specific boost
no source default
```

No same-domain historical items were found within the tested ±3-day comparison window for the classified sample.

Cadence was episodic/bursty rather than daily.

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

## Target Information Function

```text
M&A
antitrust
competition
Foreign Subsidies Regulation
corporate strategy
```

Official broad RSS collected successfully:

```text
30 items
30 normalized
0 normalization errors
```

High-value examples included:

- Paramount / Warner;
- Saipem / Subsea7;
- Baker Hughes / Chart Industries;
- XXXLutz / Porta;
- SAP competition commitments;
- Amazon / Microsoft cloud/DMA developments;
- cartel and antitrust investigations.

However, the broad feed also contained substantial routine State-aid material.

Current classifier:

```text
26 classified
4 unclassified
```

Many routine State-aid records classified through:

```text
european commission
→ Europe/EU
```

At Tier 1, routine records often scored:

```text
7
```

which was directly competitive with stronger existing Europe/EU items.

Narrow feed candidates were tested for:

```text
Mergers
Antitrust and Cartels
Foreign Subsidies Regulation
```

All tested narrow RSS paths returned:

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

## Target Information Function

```text
market structure
trading
settlement
funds
market data
financial supervision
securities-market infrastructure
```

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

Publication date existed only inside HTML description payloads.

Descriptions were large:

```text
approximately 2,657–6,047 raw characters
```

Normalized records remained:

```text
approximately 997–2,402 characters
```

The current normalizer accepted the records structurally but left:

```text
published_at = None
```

so the current 24-hour filter would exclude them.

A non-production simulation extracted embedded HTML dates to assess information quality.

Result:

```text
10 items
5 classified
5 unclassified
```

Important Financial Markets items such as:

- commodity derivatives reporting;
- T+1 settlement;
- ESAP data collection;

remained unclassified.

Long descriptions also caused incidental multi-domain matches.

Example:

```text
bilateral margin requirements
→ Global Politics + Europe/EU
```

through incidental occurrences of:

```text
parliament
European Union
European Commission
European Parliament
```

### Decision

> **Standby — architecture.**

Do not add:

- source-specific timestamp extraction;
- source-specific description trimming;
- ESMA-specific classification rules.

A generic improvement may be reconsidered only if several high-value sources independently justify it.

---

# Phase 4G — Final Milan/Bocconi Gap Reassessment

## Objective

Determine whether Milan/Bocconi still lacked enough public-source research to block MVP maturity.

The answer was:

> **No.**

The domain remains incomplete, but the highest-value missing roles now have documented public-source/current-architecture limits.

---

## Tech Europe Foundation

Remains the active automated Milan/Bocconi sensor.

Current role:

```text
startup ecosystem
entrepreneurship
deep tech
university-linked innovation
programmes/founder activity
```

### Decision

> **Active.**

---

## Bocconi Career Services — Public Layer Reassessment

Public pages expose strategically valuable information such as:

- Investment Banking Days;
- Bocconi&Jobs;
- Banking / Financial Services / Fintech Recruiting Dates;
- sector-specific employer events;
- registration windows;
- employer lists.

However:

- the most actionable layer remains partly inside `yoU@B` / JobGate;
- no clean narrow public RSS/Atom/API was established;
- event/application semantics do not naturally map to article publication time.

### Decision

> **High-value manual/private complementary layer; standby for automation.**

Do not automate authenticated access.

Do not build a broad Career Services scraper.

---

## Italian Tech Alliance — Deeper Probe

Official RSS remained technically clean.

Live 20-item sample showed:

- complete timestamps;
- stable links;
- mostly extremely thin descriptions.

Examples:

```text
Articolo su Corriere della Sera
Articolo sul Sole24Ore
Articolo su Repubblica
```

The feed contained repeated coverage of the same underlying Italian VC developments.

A meaningful exception was:

```text
Venture Academy
→ registrations open until 18 September 2026
```

which demonstrated occasional high-value opportunity/programme content.

### Decision

> **Deferred production-readiness candidate.**

Do not activate merely for source diversification.

Do not give Milan/Bocconi source default.

---

## Fintech District

Strategic fit:

```text
Milan fintech
finance ecosystem
corporate innovation
professional ecosystem
```

Structured endpoint probe:

```text
WordPress API routes → 404
RSS/feed routes      → 404
sitemap.xml          → 200
```

The site is a Next.js application.

The sitemap is machine-readable but insufficient as a dated 24-hour article feed.

### Decision

> **Standby — structured-access limitation.**

Do not reverse-engineer hidden/internal Next.js APIs.

---

## Camera di Commercio Milano Monza Brianza Lodi

Strategic fit:

```text
local companies
business demography
Milan economic ecosystem
business initiatives
```

Endpoint probes for:

```text
rss
rss.xml
feed
feed.xml
press-release feed variants
sitemap.xml
robots.txt
```

all returned the same:

```text
Incapsula / Imperva HTML interstitial
```

rather than usable structured content.

### Decision

> **Standby — access/architecture.**

Do not bypass or work around the access-control layer.

---

# Phase 4 Completion Assessment

The Phase 4 stopping condition is now met.

## Why

The system now has:

```text
13 active sources
10 implemented domains
```

and:

- every active source has a deliberate role;
- Italy has a viable first production implementation;
- AI primary-source diversity is implemented;
- Financial Markets has dedicated monetary/rates evidence;
- Companies/Corporate Strategy is materially improved;
- Europe has strong primary evidence and now some independent geoeconomic interpretation;
- Milan/Bocconi has more than nominal automated coverage;
- the strongest obvious Milan/Bocconi complementary roles have been investigated;
- several strategically excellent sources were deliberately rejected or deferred because of:
  - feed breadth/noise;
  - persistence constraints;
  - missing timestamps;
  - event/actionability semantics;
  - missing structured endpoints;
  - access controls;
  - disproportionate source-specific complexity.

The remaining source gaps are real.

They are no longer evidence that Phase 4 source research is incomplete.

They are accepted MVP maturity limitations.

## Phase 4 Completion Decision

> **Phase 4 complete for the current MVP boundary.**

Future source work should reopen only when:

1. repeated report use demonstrates a costly information gap;
2. a previously blocked high-value source exposes a materially cleaner endpoint;
3. licensing/persistence conditions improve;
4. a new information need becomes validated;
5. source concentration demonstrably harms report quality.

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

ISPI partially improves the geoeconomic-analysis role.

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

Do not fill the gap with inferior broad feeds solely for completeness.

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

Do not add additional funding-round publishers without differentiated value.

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

> **Strong primary evidence; independent interpretation partially improved.**

ISPI closes part of the previous analytical gap.

Broader independent Europe interpretation remains incomplete but non-blocking.

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

> **Viable first implementation achieved and MVP-sufficient.**

Remaining maturity areas:

- banks;
- broader capital markets;
- major-company coverage;
- private capital;
- Milan/Lombardy established firms.

---

## Milan and Bocconi Ecosystem

Current:

```text
Tech Europe Foundation
```

Assessment:

> **MVP-sufficient but deliberately incomplete.**

TEF provides:

- entrepreneurship;
- startup ecosystem;
- deep tech;
- founder/programme activity;
- university-linked innovation.

Still incomplete:

- established firms;
- industry;
- finance/business ecosystem;
- recruiting;
- employer events;
- high-value opportunities/deadlines.

However, the latest controlled audits demonstrate a current public-source/architecture ceiling:

```text
Assolombarda
→ strong value
→ timestamps/persistence fail

Bocconi Career Services
→ strong value
→ partly authenticated
→ no narrow structured public feed

Italian Tech Alliance
→ technically clean
→ thin/repetitive press-clipping

Fintech District
→ strong value
→ no usable RSS/API

Camera di Commercio Milano
→ strong value
→ automated access blocked by Incapsula
```

The domain should therefore no longer be treated as an unfinished source-research task.

---

# Current Source Audit Decision Summary

Detailed rationale belongs in:

```text
03 Information Taxonomy and Source Policy.md
```

| Source | Current Development Status |
|---|---|
| Sifted | Removed; replaced by Tech.eu |
| Tech.eu | Active |
| Financial Times | Standby — persistence/access conflict |
| Il Sole 24 Ore | Standby — technically strong; persistence/licensing unresolved |
| Reuters | Standby / incompatible with current zero-cost machine-delivery constraints |
| Nasdaq | Standby — access/persistence conflict |
| Federal Reserve Monetary Policy | Active |
| Federal Reserve Banking/Regulatory | Standby |
| Bank of Italy RSS | Standby |
| Bank of Italy BDS | Approved future structured-data enhancement |
| MIMIT News | Active |
| MIMIT Incentives | Standby |
| Lavoce.info Imprese | Active |
| Lavoce.info General | Rejected — too broad |
| Lavoce.info Banche e finanza | Standby |
| Bruegel General RSS | Rejected — event/session noise |
| Bruegel Analysis | Standby — malformed/full-content feed |
| Bruegel Publications | Standby — malformed/full-content feed |
| Assolombarda News | Standby — timestamps/persistence |
| Assolombarda Comunicati Stampa | Standby — timestamps/persistence |
| Assolombarda Centro Studi | Manual/research layer |
| Ars Technica | Standby — access/persistence conflict |
| Google DeepMind News | Active |
| B4i | Legacy / superseded by TEF for current general ecosystem role |
| Tech Europe Foundation | Active |
| Bocconi Career Services | High-value manual/private layer; standby for automation |
| Bocconi general Events/News | Not suitable for current architecture |
| Italian Tech Alliance | Deferred production-readiness candidate |
| Fintech District | Standby — structured-access limitation |
| Camera di Commercio Milano Monza Brianza Lodi | Standby — access/architecture |
| ISPI Geoeconomics | Active |
| ISPI Business Events | Standby — event/actionability semantics |
| DG Competition | Standby — product quality / feed breadth |
| ESMA | Standby — architecture |

---

# Current Stable Validation Record

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
- real 11-source pipeline.

Status:

> **Passed and pushed.**

---

## Google DeepMind News

Validated:

- official RSS;
- 100-record technical sample;
- timestamp completeness;
- metadata-size/persistence compatibility;
- 100-record classification review;
- no-keyword decision;
- tests;
- real 12-source pipeline.

Status:

> **Passed and pushed.**

---

## ISPI Geoeconomics

Validated:

- differentiated information function;
- official public RSS;
- real project collector;
- 10-item live sample;
- 10/10 normalization;
- timestamps;
- description/persistence boundary;
- current classifier;
- no-source-default decision;
- candidate-keyword historical checks;
- deterministic ranking;
- Tier 3 choice;
- cadence review;
- same-domain historical overlap review;
- source configuration;
- configuration assertions;
- targeted source-configuration test;
- full feed-fixture test;
- full test suite;
- real 13-source production-equivalent pipeline;
- run summary;
- report inspection;
- stale-record exclusion.

Full automated suite:

```text
118 passed
```

Real 18 August 2026 production-equivalent run:

```text
13 active sources
13 successful
0 empty
0 failed
0 invalid
0 warnings

1442 valid
45 inside collection window
43 unique
37 unclassified
6 displayed

status: success
```

ISPI collection:

```text
10
```

Current-window ISPI records:

```text
0
```

expected because the feed's newest items were outside the monitored 24-hour window.

Status:

> **Implementation validated; documentation/commit checkpoint in progress.**

---

# Active Product-Quality Findings

## 1. Further Source Expansion Is No Longer the Main MVP Bottleneck

The system now has:

```text
13 active sources
10 implemented domains
```

The final source audits produced only one activation:

```text
ISPI Geoeconomics
```

while several strategically strong candidates failed because of product, endpoint or architecture constraints.

### Consequence

Do not continue a standing source-audit queue.

Future source work must be evidence-triggered.

---

## 2. Financial Markets Is Sufficient for the MVP but Not Mature

Current dedicated role:

```text
Federal Reserve Monetary Policy
```

ESMA demonstrated the value of:

```text
market structure
settlement
trading
financial supervision
```

but failed the architecture gate.

### Consequence

Keep the limitation explicit.

Do not build ESMA-specific timestamp/description handling.

---

## 3. Companies Is Sufficient for the MVP but Still Globally Weak

Current useful layer:

```text
BBC Business
Tech.eu
MIMIT
Lavoce.info Imprese
```

DG Competition demonstrated strong M&A/antitrust value but broad-feed ranking noise.

### Consequence

Do not distort the classifier or add publisher-specific ranking rules merely to activate DG Competition.

---

## 4. Italy Is Implemented

Current architecture:

```text
Istat
+ MIMIT
+ Lavoce.info Imprese
+ selective ISPI spillover
```

### Consequence

Further Italy sources must provide differentiated maturity value.

---

## 5. AI Primary Diversity Is Implemented

Current structure:

```text
OpenAI
+ Google DeepMind
```

### Consequence

Future AI sourcing, if reopened, should prioritise independent scrutiny.

---

## 6. Europe Independent Interpretation Is Partially Improved

Current structure:

```text
ECB
European Commission
ISPI Geoeconomics
```

### Consequence

Independent interpretation remains incomplete but is no longer a Phase 4 blocker.

---

## 7. Milan/Bocconi Public-Source Limits Are Now Demonstrated

The domain is no longer merely waiting for more research.

High-value complementary roles were tested across:

```text
Assolombarda
Bocconi Career Services
Italian Tech Alliance
Fintech District
Camera di Commercio Milano
```

### Consequence

Milan/Bocconi is:

> **MVP-sufficient but deliberately incomplete.**

Do not introduce authenticated scraping, access-control workarounds or a new event model merely to increase nominal coverage.

---

## 8. High-Value Sources Can Still Be Wrong for the Current Architecture

Examples:

```text
DG Competition
→ excellent content
→ broad/noisy feed

ESMA
→ excellent Financial Markets role
→ incompatible timestamp/description shape

ISPI Business Events
→ excellent event content
→ publication-time semantics wrong for actionability
```

### Consequence

Strategic value is necessary but not sufficient for source activation.

---

## 9. Public Structured Access and Public Human Access Are Different

Examples:

```text
Fintech District
→ public site
→ no suitable RSS/API

Camera di Commercio Milano
→ public site
→ machine requests intercepted by Incapsula
```

### Consequence

A source cannot be considered automation-compatible merely because a browser can read it.

---

## 10. Public RSS Does Not Mean Safe or Useful Persistence

Bruegel demonstrated:

```text
public feed
+
successful retrieval
≠
safe metadata persistence
```

ESMA demonstrated:

```text
public feed
+
large page-like descriptions
→ classification/ranking distortion
```

### Consequence

Always inspect field depth and downstream behaviour.

---

## 11. Missing Timestamps Remain a Hard Architecture Boundary

Assolombarda and ESMA reinforce:

```text
collectable source
+
no suitable structured publication timestamp
→ not eligible for current 24-hour architecture
```

### Consequence

Do not substitute retrieval time or scrape dates source-by-source.

---

## 12. Classification Rate Is Still Not a Product KPI

Latest validated run:

```text
43 processed
37 unclassified
6 displayed
```

This does not by itself prove a classifier defect.

### Consequence

Inspect missed records before changing taxonomy.

---

## 13. Thin Report Context Is Now the Highest-ROI Product Limitation

Current report descriptions are capped at:

```text
300 characters
```

The system can often identify useful stories but still provides insufficient context to understand them without immediate click-through.

This limitation affects:

```text
every source
every domain
every useful report
```

whereas another source would affect only a subset of days and domains.

### Consequence

Phase 5 richer-context design becomes the active product-development priority.

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

This roadmap records only enough detail to control implementation sequencing.

---

# Immediate Next Actions

## 1. Complete the Phase 4 Documentation Closeout

Update and replace:

```text
03 Information Taxonomy and Source Policy.md
01 Product Requirements.md
02 System Architecture.md
04 Development Roadmap and Status.md
```

`00 Project Brief.md` does not require an update because:

- project purpose is unchanged;
- hard constraints are unchanged;
- strategic direction is unchanged.

---

## 2. Inspect the Full Git Diff

Expected implementation changes:

```text
config/sources.yaml
tests/test_feed_fixture.py
```

Expected documentation changes:

```text
docs/project/01 Product Requirements.md
docs/project/02 System Architecture.md
docs/project/03 Information Taxonomy and Source Policy.md
docs/project/04 Development Roadmap and Status.md
```

Unrelated file that must remain excluded:

```text
.obsidian/workspace.json
```

Verify:

- no generated same-day validation outputs remain modified;
- source count is consistently 13 where current production state is described;
- ISPI Geoeconomics is active;
- DG Competition is standby;
- ESMA is standby;
- Milan/Bocconi is described as MVP-sufficient but incomplete;
- Phase 4 is closed;
- Phase 5 is the active design phase;
- no stale Career Agent source-research queue remains active;
- no document claims that all domains are complete.

---

## 3. Run Final Validation

Because the implementation has already passed:

```text
118 tests
+
13-source production-equivalent run
```

the closeout should rerun at least:

```text
pytest -q
git diff --check
```

A second live pipeline run is unnecessary unless implementation files change again.

---

## 4. Stage Only Intended Files

Stage:

```text
config/sources.yaml
tests/test_feed_fixture.py
docs/project/01 Product Requirements.md
docs/project/02 System Architecture.md
docs/project/03 Information Taxonomy and Source Policy.md
docs/project/04 Development Roadmap and Status.md
```

Do not stage:

```text
.obsidian/workspace.json
```

---

## 5. Commit and Push the Phase 4 Closeout

The commit should capture:

```text
ISPI production integration
+
Phase 4 source-audit closeout
+
Phase 5 transition
```

Exact commands should be provided only after final diff inspection confirms the intended file set.

---

## 6. Refresh Canonical Project Sources

After push:

- upload/refresh the four canonical project documents;
- ensure the Development project source files match the repository;
- begin Phase 5 from those updated sources rather than from chat history.

---

## 7. Start Phase 5 Richer-Report Design

Do not immediately edit:

```text
max_description_length
```

The design must first settle:

- what “enough context” means;
- target per-item context length;
- acceptable total report length;
- which current feed fields are available;
- which descriptions are safe to persist;
- how thin sources should behave;
- whether richer structured fields exist;
- fallback behaviour;
- provenance;
- copyright boundaries;
- acceptance tests.

Only then should implementation begin.

---

# Next Highest-ROI Development Step

After the Phase 4 closeout commit:

> **Design the smallest lawful, deterministic and zero-cost richer-report context mechanism that materially improves understanding without requiring immediate click-through.**

This is now higher ROI than another speculative source audit because:

- the source universe is operational across all ten domains;
- several important information gaps have been investigated;
- multiple attractive sources failed for structural reasons rather than lack of research;
- Milan/Bocconi now has both meaningful automated coverage and a documented public-source ceiling;
- another source would improve a subset of the system;
- richer context improves the daily value of every useful selected story.

The active question is:

> **How much additional lawful context is necessary for a report entry to communicate what happened, who is involved and why the development matters?**

---

# Residual Source Gaps — Not Active Work

These remain visible but are not current audit tasks.

## Global Companies / Corporate Strategy

Current weakness:

```text
strong global dedicated role still missing
```

DG Competition remains standby.

Reopen if:

- a clean narrow official feed appears;
- real report use demonstrates material missed company intelligence.

---

## Broader Financial Markets

Current weakness:

```text
market structure
credit
corporate financing
settlement
broader capital-markets intelligence
```

ESMA remains standby.

Reopen if:

- a cleaner official endpoint appears;
- a generic timestamp/metadata improvement becomes independently justified;
- report use demonstrates material cost.

---

## Independent AI / Technology Reporting

Current primary layer:

```text
OpenAI
Google DeepMind
```

Remaining role:

```text
external scrutiny
systems/software
cybersecurity
infrastructure
frontier-lab evaluation
```

Not currently blocking MVP use.

---

## Independent Europe / EU Interpretation

Current layer:

```text
ECB
European Commission
ISPI Geoeconomics
```

Further independent analysis remains desirable.

Not currently blocking MVP use.

---

## Startups / VC Diversification

Current:

```text
Tech.eu
TEF
```

Italian Tech Alliance remains the strongest known deferred complement.

Do not activate without new evidence.

---

## Milan / Bocconi Professional and Business Ecosystem

Current:

```text
TEF
→ startups / innovation / entrepreneurship
```

Still incomplete:

```text
recruiting
finance/business ecosystem
established firms
industry
selected opportunities/deadlines
```

Current source research has reached a justified public-source/current-architecture limit.

Reopen only if actual use demonstrates meaningful missed-opportunity cost or a new structured endpoint appears.

---

# Phase 5 — Richer-Report Product Design

## Objective

Design a report that provides enough lawful context for understanding key developments without requiring immediate click-through.

## Validated Problem

Current items typically contain:

- headline;
- source;
- timestamp;
- relevance score;
- optional secondary domains;
- feed-provided description;
- link.

Current maximum description length:

```text
300 characters
```

This remains insufficient for some sources and stories.

Desired workflow:

```text
report
→ understand core development
→ selectively click for deeper reading
```

not:

```text
report
→ see headline
→ click everything to understand it
```

## Entry Condition

Phase 4 source/domain correction must be sufficiently mature.

### Status

> **Entry condition passed.**

The current source/domain universe is sufficiently mature for the MVP boundary.

This does not mean coverage is complete.

It means further speculative source expansion now has lower expected value than solving the validated context problem.

---

# Phase 5 Design Questions

The design should answer the following before production code changes.

## 1. Minimum Useful Context

What should the user understand without opening the article?

At minimum, likely:

```text
what happened
who is involved
why it matters
```

This must be specified precisely enough to evaluate outputs.

---

## 2. Target Context Length

Current cap:

```text
300 characters
```

Determine whether the right target is:

- a larger character cap;
- one or two sentences;
- different treatment by metadata availability;
- another bounded deterministic rule.

Do not select a number arbitrarily.

---

## 3. Source Metadata Audit

For all 13 active sources, determine:

- description availability;
- description length distribution;
- whether descriptions are actual summaries or title-like text;
- whether richer feed fields exist;
- whether content fields are present;
- whether those fields are safe to persist.

This should be empirical.

---

## 4. Persistence and Copyright Boundary

Determine:

- how much feed-provided text can safely remain in public Git;
- whether all active sources can use the same rule;
- whether longer descriptions expose substantial source content;
- whether the report should display more text than the stored normalized record currently preserves.

Do not assume that technically available content is automatically suitable for persistence.

---

## 5. Thin-Metadata Fallback

Some sources provide weak descriptions.

The design must determine what happens when:

```text
description missing
or
description too short
```

Possible outcomes may include:

- headline-only fallback;
- source-specific structured metadata if available;
- no additional context;
- later rejection of a source if context quality proves too poor.

Do not invent article summaries without a lawful input.

---

## 6. Report-Length Constraint

Richer entries increase total report length.

The design should determine whether existing limits remain suitable:

```text
max 5 per domain
max 30 total
```

Potential trade-off:

```text
fewer items
+
better context
```

may create more user value than:

```text
more items
+
thin context
```

Do not optimise only for description length.

---

## 7. Provenance

The user should be able to distinguish:

- source-provided description;
- deterministic transformation;
- any future generated summary.

Current preferred Phase 5 approach should avoid generated summaries if structured metadata is sufficient.

---

## 8. Premium / Inaccessible Source Behaviour

The design should remain compatible with:

- public links;
- Premium Bocconi Exception;
- sources where click-through may require legitimate institutional access.

Richer context must not become an excuse to ingest premium article bodies.

---

## 9. Acceptance Tests

Before implementation, define how richer report quality will be judged.

Possible evaluation dimensions:

- can the user understand the core development without clicking?
- are important details preserved?
- is text misleading or truncated awkwardly?
- is the report too long?
- is content repetitive?
- is provenance clear?
- are copyright boundaries preserved?
- are thin sources handled predictably?
- does ranking/classification remain unchanged unless explicitly intended?

The design should include a representative multi-source sample rather than evaluate one convenient feed.

---

# Preferred Phase 5 Solution Order

Evaluate in this order:

1. richer use of existing RSS/Atom metadata;
2. other public structured metadata already exposed by active sources;
3. official free APIs where directly relevant;
4. narrowly permitted deterministic public extraction if independently justified;
5. more complex mechanisms only if simpler methods fail.

Do not assume:

```text
LLM summary
```

is required.

Do not introduce:

- recurring API cost;
- production ChatGPT dependency;
- RAG;
- embeddings;
- agentic summarisation.

---

# Phase 5 Definition of Done

Phase 5 design is complete when:

- the context requirement is explicit;
- the source metadata baseline is measured;
- copyright/persistence boundaries are defined;
- at least one simple deterministic candidate solution is specified;
- fallback behaviour is specified;
- report-length implications are understood;
- provenance is specified;
- acceptance tests are defined;
- implementation files affected are known;
- unnecessary architecture has been rejected.

Only then should Phase 6 begin.

## Status

> **Active — design not yet complete**

---

# Phase 6 — Richer-Report Implementation and Evaluation

## Objective

Implement the smallest compliant richer-report solution selected in Phase 5.

## Entry Condition

Phase 5 design complete.

## Validation

Must include:

- deterministic tests;
- source-specific fixtures where appropriate;
- missing-context cases;
- malformed-input cases;
- real report inspection;
- copyright-safe output review;
- report-length comparison;
- source accessibility review;
- source concentration review;
- classification/ranking regression;
- repeated real-use evaluation.

## Status

**Deferred**

---

# Phase 7 — Optional Delivery and Interface Improvements

## Objective

Improve access only if repository-native Markdown becomes a demonstrated usability constraint.

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

## Status

**Deferred**

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

# Phase 4 Stop Condition — Final Result

The Phase 4 exit questions were:

1. Are there still one or more clearly high-value, low-complexity source additions?
2. Do those additions solve important information-function gaps rather than publisher-count gaps?
3. Are remaining gaps increasingly caused by source availability/licensing/architecture rather than lack of research?
4. Is the current report now more limited by thin context than by missing sources?

Final assessment:

```text
1. Few clearly high-ROI low-complexity additions remain.

2. ISPI Geoeconomics was the final clean differentiated addition
   from the latest audit cycle.

3. Remaining high-value gaps increasingly reflect:
   - feed breadth
   - missing timestamps
   - persistence constraints
   - event semantics
   - missing structured endpoints
   - access controls
   - source-specific complexity

4. Thin report context now affects more daily product value
   than another speculative source addition.
```

Therefore:

> **Phase 4 exit condition passed.**

---

# Current Status Summary

```text
Phase 0  Complete
Phase 1  Complete
Phase 2  Complete
Phase 3  Complete
Phase 4  Complete for current MVP boundary
Phase 5  Active — richer-report design
Phase 6  Deferred
Phase 7  Optional
```

Current validated production direction:

```text
collect
→ normalize
→ deduplicate
→ classify selectively
→ rank deterministically
→ store
→ report
→ inspect real usefulness
```

Current production checkpoint:

```text
13 active sources
10 active domains

Sifted
→ replaced by Tech.eu

Financial Markets
→ dedicated monetary/rates evidence active

Milan/Bocconi
→ active through TEF
→ MVP-sufficient but intentionally incomplete

Italy
→ Istat + MIMIT + Lavoce.info
→ viable first production implementation

AI
→ OpenAI + Google DeepMind primary diversity achieved

Europe interpretation
→ partially strengthened by ISPI Geoeconomics

ISPI Geoeconomics
→ active

ISPI Business Events
→ standby

DG Competition
→ standby

ESMA
→ standby

Italian Tech Alliance
→ deferred production-readiness candidate

Fintech District
→ standby

Camera di Commercio Milano
→ standby
```

Current immediate priority:

> **Finish the Phase 4 closeout commit and begin Phase 5 richer-report design.**

Expected sequence:

```text
finish documentation
→ inspect full diff
→ pytest -q
→ git diff --check
→ stage only intended files
→ commit
→ push
→ refresh canonical project sources
→ begin richer-context design
```

---

# Changelog

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
- Recorded the current full-suite validation:
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
- Confirmed that ISPI collected 10 records and that none entered the current report because all were outside the monitored publication window.
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
- Removed the standing future source-audit queue.
- Made future source work evidence-triggered.
- Activated Phase 5 richer-report product design.
- Made richer report context the next highest-ROI product-development problem.
- Preserved richer-context implementation as deferred until the design gate is passed.

## 2026-08-18 — Twelve-Source / Ten-Domain Phase 4 Checkpoint

- Updated active production sources from eight to twelve.
- Updated implemented domains from nine to ten.
- Recorded Italy as implemented rather than pending.
- Added Federal Reserve Board Monetary Policy as an active Tier 1 source.
- Added MIMIT News as an active Tier 1 Italy source.
- Added Italy as the tenth domain.
- Added Lavoce.info Imprese as an active Tier 2 Italy source.
- Added Google DeepMind News as an active Tier 1 AI source.
- Recorded the generic HTML-to-text normalisation improvement triggered by MIMIT.
- Recorded zero unintended historical regressions for retained Lavoce keywords.
- Recorded the real twelve-source production run.
- Reframed Financial Markets from no dedicated source to dedicated monetary/rates evidence.
- Reframed Companies/Corporate Strategy as materially improved but globally incomplete.
- Reframed Italy as a viable first implementation.
- Reframed AI as OpenAI + DeepMind primary diversity achieved.
- Closed Nasdaq, Bruegel, Assolombarda and Ars Technica according to their audited constraints.
- Retired the completed Nasdaq→DeepMind audit queue.
- Set the remaining information-function gaps for the final gap-driven research cycle.

## 2026-08-17 — Phase 4 Source-Audit Consolidation and New Expansion Strategy

- Reconciled the roadmap with the eight-source / nine-domain production checkpoint.
- Recorded Tech Europe Foundation as the first active Milan/Bocconi source.
- Recorded Milan and Bocconi Ecosystem as a source-defined domain with no keywords.
- Recorded the successful real eight-source pipeline integration.
- Recorded the Artificial Intelligence `AI` case-sensitivity correction.
- Recorded Financial Times, Il Sole 24 Ore, Bank of Italy and Reuters audit conclusions.
- Recorded B4i as legacy/superseded by TEF.
- Recorded Bocconi Career Services as a high-value manual/private layer.
- Recorded Italian Tech Alliance as a production-readiness candidate.
- Reframed source expansion around information-function gaps rather than publisher count.

## 2026-08-17 — Phase 4A Tech.eu Replacement and Financial Markets Activation

- Incorporated the first Career Agent strategic source/domain audit.
- Formalised the narrow Premium Bocconi Exception.
- Compared Tech.eu and Sifted through the real collector.
- Observed 20/20 Tech.eu descriptions versus 0/24 Sifted descriptions.
- Replaced Sifted with Tech.eu.
- Added Tech.eu as Tier 2 with no source default.
- Added evidence-backed keywords.
- Removed generic `startup`.
- Activated Financial Markets with a conservative keyword set.
- Validated taxonomy changes against stored historical records.
- Completed a real 17 August pipeline run.
- Recorded that classification rate alone is not a product-quality KPI.

## 2026-08-14 — Phase 3 Production Closeout and Phase 4 Entry

- Reconciled the roadmap with completed GitHub Actions automation.
- Recorded manual and scheduled production execution.
- Recorded automated repository persistence.
- Recorded degraded and critical failure validation.
- Recorded GitHub scheduler latency.
- Made source/domain correction the active milestone.
- Deferred richer-report design until source correction.

## 2026-08-11 — Phase 2 Real-Source Validation

- Validated seven real public RSS sources.
- Expanded the taxonomy to seven implemented domains.
- Added bounded HTTP retrieval and explicit request headers.
- Corrected broad source-default classification.
- Added evidence-backed politics keywords.
- Validated degraded real-source behaviour.
- Reached 110 passing tests.

## 2026-08-11 — Phase 1 Local Vertical Slice

- Implemented the complete local deterministic pipeline.
- Added automated tests.
- Added CLI execution.
- Added run summaries and reporting.
- Reached 104 passing tests.

## Initial Roadmap Baseline

- Defined the development phases.
- Established zero-cost and low-manual-work constraints.
- Established the MVP processing loop.
- Defined Git/tests as the implementation verification layer.