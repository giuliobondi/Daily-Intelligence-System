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
- Do not keep extending Phase 4 merely because more candidate sources exist.

The project should not move to the next phase until the current phase has a clear completion condition or there is evidence that a different immediate priority creates materially more user value.

---

# Current Project Status

| Field | Current Status |
|---|---|
| Project Phase | Phase 4 — Source and Domain Correction / Expansion |
| Current Milestone | Milestone 4 — Complete the smallest high-value source/domain universe and determine whether further expansion still beats richer report context |
| Repository Status | Public Python repository with automated GitHub-native daily execution and repository-native historical outputs |
| Implementation Status | Deterministic collect → normalize → validate → filter → deduplicate → classify → rank → store → report pipeline implemented and production-validated |
| Automation Status | GitHub Actions implemented; manual and scheduled execution validated; outputs persisted automatically |
| Production Schedule | Daily at 06:05 Europe/Rome; GitHub scheduling latency remains an observed operational limitation |
| Source Registry | Twelve active production sources |
| Taxonomy Status | Ten implemented domains; all ten strategic macroareas now have production configuration |
| Testing Status | Targeted and full automated suites passing at the latest implementation checkpoints |
| Latest Local Validation | Real 18 August 2026 pipeline run completed successfully with 12/12 sources successful |
| Latest Integration Result | Google DeepMind News collected 100 items successfully; no stale DeepMind records entered the tested 24-hour window |
| Current Product-Quality Finding | Technical stability is strong; remaining limitations are concentrated in a smaller number of information-function gaps rather than missing basic architecture |
| Current Blockers | No automation blocker; remaining issue is whether another source batch still creates more value than richer report context |
| Current Priority | Complete this documentation checkpoint, commission a fresh Career Agent source-research pass, then start a new controlled Development audit batch |
| Current Git State | Latest implementation checkpoint through Google DeepMind validated and pushed; documentation checkpoint in progress |

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
- Phase 4 does not require an arbitrary number of sources per domain.
- Strong primary evidence and strong independent interpretation are different information roles.
- Missing global FT/Reuters-style corporate reporting can remain an explicit limitation rather than being filled with inferior substitutes.
- Public RSS availability does not automatically mean that full feed payloads are suitable for permanent public Git persistence.
- Missing publication timestamps do not justify substituting retrieval time.
- Full-content feeds do not justify source-specific truncation simply to activate a prestigious source.

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

Phase 1 also established the development pattern:

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

## Validation

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

Build the smallest source and domain universe strong enough for actual daily use before investing in richer report-context logic.

Infrastructure is no longer the main bottleneck.

The active questions are:

- which information functions remain materially under-covered;
- which gaps justify another source;
- which sources remain too noisy, inaccessible or legally awkward;
- whether another source now creates more value than richer context.

Current philosophy:

> **Correct information-function gaps before correcting publisher-count gaps.**

Phase 4 is now substantially more mature than at its previous checkpoint.

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

The replacement demonstrated that technical collectability alone is insufficient.

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

Initial Financial Markets taxonomy remains intentionally conservative.

## Historical Regression

The final Phase 4A taxonomy was tested against:

```text
114 stored historical records
```

Observed changes were interpretable and no unexpected regression was identified.

## Status

**Complete and pushed**

---

# Phase 4B — Premium, Institutional and Milan/Bocconi Source Research

This work established several durable source decisions and the first Milan/Bocconi production architecture.

---

## Financial Times

Strategically excellent.

Official RSS exists, but FT RSS-specific terms conflict with the system's permanent archival model.

### Decision

> **Standby — access/persistence conflict.**

---

## Il Sole 24 Ore

Technically strong.

Tested RSS feeds included:

```text
Italia
Finanza
Economia
```

Strongest product candidates:

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

Production configuration and classifier semantics were corrected.

Current convention:

```text
lowercase keyword
→ case-insensitive

keyword containing uppercase
→ case-sensitive
```

### Validation

- historical AI records reviewed;
- useful English recall preserved;
- false Italian AI matches removed;
- targeted tests passed;
- full suite passed.

### Status

**Complete and pushed**

---

## Bank of Italy RSS

Official narrow RSS feeds collected and normalised successfully.

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
→ change/release detection
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

The desired information function is:

> **Professional Ecosystem Intelligence**

not generic local news.

---

## B4i

### Decision

> **Legacy / superseded by Tech Europe Foundation.**

---

## Tech Europe Foundation

Official RSS:

```text
https://tef.tech/news/feed/
```

Technical validation passed.

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

### Real Validation

17 August 2026 run:

```text
8 active
8 successful
0 failed
0 invalid

1295 valid
40 window-eligible
37 unique
29 unclassified
8 displayed

status: success
```

TEF current-window records:

```text
0
```

expected because feed items were older than the monitored window.

### Status

**Complete and pushed**

---

## Bocconi Career Services

### Decision

> **Manual/private layer.**

Do not automate:

```text
yoU@B
JobGate
```

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

Technical sample:

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

Candidate Startups/VC terms:

```text
round
scaleup fund
```

passed historical regression.

### Decision

> **Production-readiness candidate.**

Do not restart basic source discovery.

Remaining question:

> Does its differentiated Italian VC/opportunity value justify activation despite thin descriptions and repetition?

---

# Phase 4E — First Gap-Driven Source Audit Batch

A Career Agent research pass identified a controlled candidate set based on information-function gaps rather than publisher prestige.

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

This batch is now complete.

---

## Nasdaq

### Expected Role

- Financial Markets;
- capital markets;
- IPOs;
- market structure;
- selected corporate finance.

### Outcome

Strategically valuable.

However, current Nasdaq legal terms conflict with:

```text
automated retrieval
→ JSONL persistence
→ Markdown persistence
→ permanent public Git history
```

Broad Markets/investing feeds would also introduce unwanted retail/prediction noise.

### Decision

> **Standby — access/persistence conflict.**

No repository changes.

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

Descriptions are often thin/title-like but evidence value is high.

Without source default:

```text
14/15
→ unclassified
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

Targeted tests:

```text
passed
```

Full suite:

```text
passed
```

Real production-equivalent run:

```text
9 active
9 successful
0 invalid
status: success
```

### Decision

> **Active.**

---

## Federal Reserve Banking / Regulatory

Technically valid but heterogeneous.

Sample included:

- stress tests;
- capital framework;
- stablecoins;
- narrow regulatory announcements;
- administrative/enforcement material.

### Decision

> **Standby.**

---

## MIMIT News

Official News RSS was technically strong and strategically differentiated.

Sample included:

- R&D investment;
- company crisis tables;
- Investimenti sostenibili;
- strategic industrial sites;
- cloud/cyber incentives;
- inflation/fuel monitoring;
- Ex Ilva;
- Ducati investment;
- data centres.

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

Historical regression:

```text
0 unintended matches
```

MIMIT also exposed HTML descriptions.

The fix was general:

```text
generic HTML-to-text normalization
```

not a MIMIT-specific branch.

Real production-equivalent run:

```text
10 active
10 successful
0 invalid
0 warnings
status: success
```

### Decision

> **MIMIT News active.**

---

## MIMIT Incentives

Technically valid but more administrative, sparse and duplicative.

### Decision

> **Standby.**

---

## Lavoce.info

Three streams were evaluated.

### General Feed

Technically strong but too broad.

### Decision

> **Rejected for production.**

---

### Banche e Finanza

High quality but sparse and partly overlaps with stronger monetary/financial primary evidence.

### Decision

> **Standby.**

---

### Imprese

Best differentiated production candidate.

Sample included:

- M&A and golden power;
- Italian technology industry;
- agentic AI;
- Stellantis industrial plan;
- cybersecurity;
- patents;
- greenwashing;
- corporate governance/control;
- capital markets;
- public guarantees.

Added source default:

```text
Lavoce.info Imprese
→ Italy
```

Adopted minimal bilingual keyword set:

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
for all adopted keywords
```

Real production-equivalent run:

```text
11 active
11 successful
0 invalid
0 warnings
status: success
```

### Decision

> **Lavoce.info Imprese active.**

---

## Bruegel

Strategically excellent for independent European interpretation.

### General RSS

Technically clean but dominated by:

- sessions;
- conference components;
- lunch;
- coffee breaks.

### Decision

> **Rejected — wrong information function.**

---

### Analysis Feed

HTTP succeeds.

Current collector fails because of malformed:

```text
&nbsp;
```

Direct parser recovery showed:

```text
bozo/error mode
```

and descriptions up to:

```text
61,500 characters
```

with substantial/full-content material.

### Decision

> **Standby — malformed/full-content feed incompatible with current architecture.**

---

### Publications Feed

Same malformed-entity problem.

One tested description exceeded:

```text
93,000 characters
```

Other items placed multi-thousand-character content in structured content fields.

### Decision

> **Standby — malformed/full-content feed incompatible with current architecture.**

No Bruegel-specific parser or persistence path justified.

---

## Assolombarda

Strategically strong for:

- established companies;
- Milan/Lombardy industry;
- local innovation;
- manufacturing AI;
- professional ecosystem;
- exports;
- infrastructure.

Official RSS discovered for:

```text
News
Comunicati stampa
```

No RSS found for:

```text
Centro Studi
```

### News Test

```text
15 collected
15 normalized
0/15 timestamps
14/15 descriptions
average description ≈ 109 chars
```

### Comunicati Stampa Test

```text
15 collected
15 normalized
0/15 timestamps
14/15 descriptions
average description ≈ 89 chars
```

Descriptions contain substantive publisher-authored text.

### Decision

```text
News
→ Standby

Comunicati stampa
→ Standby

Centro Studi
→ Manual/research layer
```

Reason:

```text
missing timestamps
+
persistence incompatibility
```

Do not:

- substitute retrieval time;
- scrape dates from article pages;
- discard descriptions only for Assolombarda.

---

## Ars Technica

Strategically strong for:

- independent AI reporting;
- systems/software;
- cybersecurity;
- infrastructure.

Official RSS exists.

However, current Condé Nast/Ars terms do not provide a sufficiently clean basis for permanent public RSS-content persistence.

### Decision

> **Standby — access/persistence conflict.**

Do not create a source-specific title-only exception.

---

## Google DeepMind News

Official RSS:

```text
https://deepmind.google/blog/rss.xml
```

Controlled technical test:

```text
100 received
100 normalized
100 timestamps
79 descriptions

average description ≈ 119 chars
max description = 354 chars
0 > 500 chars
```

This passed the metadata/persistence gate.

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

The three secondary classifications were sensible.

No new keywords were required.

Tests:

```text
passed
```

Real production-equivalent run — 18 August 2026:

```text
12 active sources
12 successful
0 failed
0 invalid
0 warnings

1432 valid
44 window-eligible
42 unique
37 unclassified
5 displayed

status: success
```

DeepMind collection:

```text
100
```

DeepMind current-window records:

```text
0
```

expected because the newest feed item was outside the monitored window.

### Decision

> **Google DeepMind News active.**

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
12. Google DeepMind News.

Current working position:

| Source | Current Position |
|---|---|
| BBC News World | Retain |
| BBC News Business | Retain temporarily; reassess after stronger global company/markets coverage |
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

Current language balance:

```text
English-language feeds → 10
Italian-language feeds → 2
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

---

# Current Domain Coverage Diagnosis

## Global Politics and Geopolitics

Current:

```text
BBC World
+ European Commission spillover
```

Assessment:

> Acceptable for now, but publisher-concentrated.

Not the highest current opportunity cost.

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
```

Assessment:

> Strong primary evidence; independent interpretation remains thinner.

The earlier US monetary-policy gap is materially closed.

Remaining useful role:

- independent European/global economic interpretation.

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

> **Materially improved, still globally incomplete.**

MIMIT and Lavoce solve meaningful Italy/company roles.

Remaining gap:

```text
global corporate strategy
M&A
capital allocation
corporate financing
restructuring
major international company developments
```

Do not attempt to reconstruct FT/Reuters with weak general-news sources.

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

> **Partially solved.**

Dedicated monetary/rates evidence now exists.

Remaining gap:

```text
capital markets
credit
corporate financing
market structure
IPOs
broader company/market interaction
```

This is no longer a zero-source domain.

---

## Artificial Intelligence

Current:

```text
OpenAI News
Google DeepMind News
Tech.eu/BBC spillover
```

Assessment:

> **Primary-source diversification achieved.**

Current structure:

```text
OpenAI
+ Google DeepMind
```

Remaining role:

```text
independent reporting / scrutiny
```

Do not add additional first-party labs merely to increase publisher count.

---

## Technology and Software

Current:

```text
Tech.eu
OpenAI spillover
DeepMind spillover
BBC spillover
```

Assessment:

> Moderate.

Independent systems/software reporting remains desirable if a clean source exists.

---

## Startups and Venture Capital

Current:

```text
Tech.eu
Tech Europe Foundation selective ecosystem activity
```

Assessment:

> Still dependent on a small number of specialist roles.

Italian Tech Alliance remains the strongest partly-audited complement.

Do not add several funding-round feeds.

---

## Europe and the EU

Current:

```text
ECB
European Commission
Tech.eu selective coverage
```

Assessment:

> Strong primary evidence; independent interpretation remains weak.

Bruegel failed current production compatibility.

A replacement role may be worth researching.

---

## Italy

Current:

```text
Istat
MIMIT News
Lavoce.info Imprese
```

Assessment:

> **Viable first implementation achieved.**

Italy is no longer a structural unimplemented gap.

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

> First production implementation complete; broader requirement remains incomplete.

Missing:

- established firms;
- industry;
- finance/business ecosystem;
- professional events;
- recruiting;
- selected deadlines.

Assolombarda validated the information need but failed current production compatibility.

---

# Current Source Audit Decision Summary

Detailed rationale is owned by:

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
| B4i | Legacy / superseded by TEF |
| Tech Europe Foundation | Active |
| Bocconi Career Services | Manual/private layer |
| Bocconi general Events/News | Not suitable for current architecture |
| Italian Tech Alliance | Production-readiness candidate |
| Fintech District | Standby candidate |

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

# Active Product-Quality Findings

## 1. Source Count Is No Longer the Main Problem

The system now has:

```text
12 active sources
10 implemented domains
```

The main remaining issue is a smaller set of information-function gaps.

### Consequence

Do not keep adding sources merely because more publishers are available.

---

## 2. Financial Markets Is Improved but Not Mature

Federal Reserve Monetary Policy provides meaningful dedicated evidence.

### Remaining Gap

```text
capital markets
credit
corporate financing
market structure
broader market-moving company developments
```

### Consequence

Future Markets research should seek complementary roles rather than another monetary-policy source.

---

## 3. Companies Is Improved but Still Globally Weak

MIMIT and Lavoce materially improved Italy/company intelligence.

### Remaining Gap

```text
international corporate strategy
M&A
capital allocation
major company developments
corporate financing
```

### Consequence

A new candidate should solve the international role rather than duplicate Italian industrial coverage.

---

## 4. Italy Is Implemented

Current architecture:

```text
Istat
+ MIMIT
+ Lavoce.info Imprese
```

### Consequence

Do not continue treating Italy as an unimplemented macroarea.

Further Italy sources must provide differentiated maturity value.

---

## 5. AI Primary Diversity Is Implemented

Current structure:

```text
OpenAI
+ Google DeepMind
```

### Consequence

The next AI source, if any, should add:

```text
independent scrutiny
```

rather than another first-party lab.

---

## 6. Europe Has a Real Independent-Analysis Gap

Bruegel validated the information need but failed production compatibility.

### Consequence

Search for a cleaner independent analytical source rather than creating a Bruegel-specific persistence path.

---

## 7. Milan/Lombardy Established-Firm Intelligence Remains Open

Assolombarda validated strong information value.

Its feed architecture failed because of:

```text
0 usable timestamps
+
persistence concerns
```

### Consequence

The gap remains valid.

The specific source is not currently viable.

---

## 8. Startups/VC Still Has Concentration Risk

Tech.eu remains the main specialist.

Italian Tech Alliance has passed basic audit but has thin descriptions and press-clipping repetition.

### Consequence

ITA remains a production-readiness question, not an automatic next implementation.

---

## 9. Public RSS Does Not Mean Safe Persistence

Bruegel demonstrated:

```text
public feed
+
successful direct retrieval
≠
safe metadata persistence
```

### Consequence

Always inspect field depth.

---

## 10. Missing Timestamps Remain a Hard Architecture Boundary

Assolombarda demonstrated:

```text
technically successful feed
+
0 timestamps
→ unusable for current 24-hour pipeline
```

### Consequence

Do not substitute retrieval time or scrape dates source-by-source.

---

## 11. Classification Rate Is Still Not a Product KPI

The 18 August run produced:

```text
42 processed
37 unclassified
5 displayed
```

This does not by itself prove a classifier defect.

### Consequence

Inspect missed records before changing taxonomy.

---

## 12. Existing Description Formatting Artifacts Remain Separate

Some reports have shown strings such as:

```text
andwhat
AIplatform
acrossEurope
```

These have not yet been tied reproducibly to the MIMIT HTML-normalization fix.

### Consequence

Do not modify normalization again without a reproducible persisted example and isolated cause.

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

## 1. Complete This Documentation Checkpoint

Update and replace:

```text
03 Information Taxonomy and Source Policy.md
01 Product Requirements.md
02 System Architecture.md
04 Development Roadmap and Status.md
```

`00 Project Brief.md` does not require a checkpoint update because:

- project purpose is unchanged;
- hard constraints are unchanged;
- strategic direction is unchanged;
- the detailed 12-source status belongs in 03/04.

---

## 2. Inspect Documentation Diff

After replacing the four documents:

```text
inspect only intended documentation changes
→ verify no implementation files changed
→ verify no stale 8-source / 9-domain references remain
→ verify Italy is no longer described as pending
→ verify DeepMind is no longer described as a future audit
→ verify Nasdaq-to-DeepMind is no longer described as an active queue
```

---

## 3. Commit and Push Documentation Checkpoint

The documentation update should become one stable checkpoint before new research begins.

---

## 4. Refresh Project Source Files

Upload or refresh the canonical versions used by the Development project.

Confirm that the project sources match the pushed repository versions.

---

## 5. Generate the Career Agent Research Prompt

The prompt should ask the Career Agent to research **new source candidates** against the current remaining information-function gaps.

The Career Agent should receive:

```text
current 12-source active universe
current 10-domain universe
completed audit decisions
hard zero-cost / persistence / credential constraints
remaining information-function gaps
instruction not to re-propose closed candidates without new evidence
```

The requested research output should be:

```text
one Markdown text box
suitable to paste back into this Development project
```

---

## 6. Run the Career Agent Research

The research should prioritise:

```text
Global Companies / Corporate Strategy
Broader Financial Markets
Independent AI / Technology reporting
Independent Europe/EU interpretation
Startups / VC diversification
Milan / Lombardy established-company and professional ecosystem
```

It should not optimise for source count.

It should rank candidates by expected differentiated value and practical compatibility.

---

## 7. Create a New Development-Chat Handoff

After the Career Agent research returns:

```text
updated canonical documents
+
completed audit-batch summary
+
new source-research output
+
current implementation baseline
```

should be condensed into a new Development handoff.

The new chat should then audit candidates one at a time.

---

# Next Highest-ROI Development Step

After this documentation checkpoint:

> **Commission the fresh Career Agent source-research pass.**

This is higher ROI than immediately auditing another source from the old candidate list because:

- the previous queue is complete;
- several original gaps have changed materially;
- Italy is now implemented;
- Financial Markets now has a dedicated monetary-policy source;
- AI primary diversity is now achieved;
- several attractive candidates proved incompatible;
- the next source universe should therefore be re-derived from the current state.

The Career Agent should answer:

> **Which new sources now offer the highest expected marginal value against the remaining information-function gaps?**

Development should then independently validate every recommended candidate.

---

# Current Research Gaps for the Career Agent

## 1. Global Companies / Corporate Strategy

Current weakness:

```text
MIMIT/Lavoce strong for Italy
BBC Business broad
Tech.eu selective
global dedicated role missing
```

Desired information:

- M&A;
- restructuring;
- capital allocation;
- corporate financing;
- strategic partnerships;
- material earnings/guidance;
- major international company developments.

Avoid:

- generic business-news duplication;
- press-release firehoses;
- inaccessible premium dependence.

---

## 2. Broader Financial Markets

Current strength:

```text
Fed Monetary Policy
ECB spillover
```

Current weakness:

```text
capital markets
credit
corporate financing
market structure
IPOs
broader market/company interactions
```

Avoid:

- trading tips;
- daily index recaps;
- stock picking;
- price predictions.

---

## 3. Independent AI / Technology Reporting

Current primary layer:

```text
OpenAI
Google DeepMind
```

Desired information function:

```text
external scrutiny
industry reporting
software/systems
cybersecurity
infrastructure
frontier-lab evaluation
```

Avoid:

- another first-party AI lab unless it fills a clearly different role;
- consumer gadget noise;
- sources with unclear persistence rights.

---

## 4. Independent Europe / EU Interpretation

Current primary layer:

```text
ECB
European Commission
```

Desired role:

- competitiveness;
- industrial policy;
- macro;
- capital markets;
- trade;
- strategic autonomy;
- regulation.

Bruegel proved the need but failed current feed/persistence compatibility.

---

## 5. Startups / VC Diversification

Current:

```text
Tech.eu
TEF selective ecosystem coverage
```

Potential differentiated roles:

- private-capital statistics;
- European VC market structure;
- Italian VC ecosystem;
- professional programmes;
- fund formation;
- exits.

Italian Tech Alliance remains a known production-readiness candidate.

Do not simply add more funding-round publishers.

---

## 6. Milan / Lombardy Business and Professional Ecosystem

Current:

```text
TEF
→ startups / innovation / entrepreneurship
```

Desired complementary roles:

- established firms;
- industry;
- finance/business events;
- professional ecosystem;
- local economic research;
- high-value opportunities.

Assolombarda proved the strategic value but failed production compatibility.

The research should search for alternative structured public sources.

---

# Parallel Existing Candidate — Italian Tech Alliance

Italian Tech Alliance should remain outside the new basic research pass unless the Career Agent has materially new evidence.

Current state:

```text
basic technical audit complete
classification candidates tested
historical regression passed
thin descriptions
press-clipping repetition unresolved
```

Next Development question:

> **Does ITA provide enough unique Italian VC/opportunity signal to justify activation in the actual final source universe?**

Do not build near-duplicate clustering merely to support it.

---

# Phase 4 Completion Criteria

Phase 4 is complete when:

- every active source has a deliberate strategic and technical role;
- weak/incompatible sources have explicit retain/replace/remove/standby decisions;
- Financial Markets has sufficiently useful coverage beyond merely having a configured domain;
- Companies/Corporate Strategy is materially stronger than incidental coverage;
- Italy has a validated low-maintenance implementation;
- Milan/Bocconi has useful public-source implementation or has reached a justified public-source limit;
- AI is no longer structurally defined by OpenAI alone;
- Startups/VC is sufficiently differentiated for actual use or an explicit residual limitation is accepted;
- high-value independent Europe/technology gaps have explicit source decisions;
- source/default/keyword changes have regression evidence;
- full automated tests pass;
- real collection remains reliable;
- generated reports are manually inspected;
- source concentration and accessibility are acceptable;
- no credentials or restricted article bodies are introduced;
- zero recurring monetary cost remains intact;
- additional source expansion has lower expected value than richer-report design.

Phase 4 does **not** require:

- every researched source to be implemented;
- every domain to have equal source counts;
- a fixed minimum number of publishers;
- perfect global corporate reporting;
- a replacement for FT or Reuters;
- activation of every strategic candidate;
- all ten macroareas to have identical technical architecture.

The correct stopping question remains:

> **Would another source/domain change create more user value than improving the context of stories already being selected?**

After the upcoming source-research/audit batch, this question should be answered explicitly.

## Status

> **Active — major structural gaps have been reduced; one fresh gap-driven source-research cycle remains justified before deciding whether to move to Phase 5.**

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

The current plan is to reconsider entry immediately after the next fresh source-research/audit batch.

## Design Questions

Determine:

- what “enough context” means;
- target context length;
- acceptable total report length;
- which public feed fields exist;
- which sources provide richer summaries;
- which official/free APIs provide lawful structured context;
- source-specific fallback behaviour;
- treatment of Premium Bocconi Exception sources;
- copyright boundaries;
- source attribution;
- inaccessible-link behaviour;
- objective acceptance tests.

## Preferred Solution Order

1. richer RSS/Atom fields;
2. public structured metadata;
3. official free APIs;
4. limited permitted deterministic public extraction if justified;
5. more complex methods only if simpler mechanisms fail.

Do not assume AI summarisation is required.

## Status

**Not started — validated requirement, intentionally deferred behind the current Phase 4 closeout decision**

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
- generic Bocconi event feeds;
- generic Politecnico event feeds;
- multiple additional central banks;
- multiple additional first-party AI labs;
- generic press-release aggregators;
- weak general business-news substitutes merely to increase source count.

Reconsider only if:

- source terms change;
- an official structured endpoint changes materially;
- a new general architecture is independently justified;
- the upcoming research identifies genuinely new evidence.

---

# Stop Condition Before Phase 5

Do not begin richer-report implementation until the next source research/audit cycle answers:

1. Are there still one or more clearly high-value, low-complexity source additions?
2. Do those additions solve important information-function gaps rather than publisher-count gaps?
3. Are remaining gaps increasingly caused by source availability/licensing rather than lack of research?
4. Is the current report now more limited by thin context than by missing sources?

If the answer becomes:

```text
few/no high-ROI source additions remain
+
report context is the higher-value limitation
```

then move to Phase 5.

The switch should not depend on:

- hitting a specific source count;
- hitting a specific domain count;
- auditing every possible candidate;
- eliminating every gap;
- frustration with source research.

---

# Current Status Summary

```text
Phase 0  Complete
Phase 1  Complete
Phase 2  Complete
Phase 3  Complete
Phase 4  Active — approaching explicit exit decision
Phase 5  Deferred
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
→ identify information-function gap
→ audit smallest useful source
→ validate
→ checkpoint
```

Current production checkpoint:

```text
12 active sources
10 active domains

Sifted
→ replaced by Tech.eu

Financial Markets
→ dedicated monetary/rates evidence now active

Milan/Bocconi
→ first production implementation through TEF

Italy
→ implemented through Istat + MIMIT + Lavoce.info

AI
→ OpenAI + Google DeepMind primary diversity achieved

Federal Reserve Monetary Policy
→ active

MIMIT News
→ active

Lavoce.info Imprese
→ active

Google DeepMind News
→ active

Nasdaq
→ standby

Bruegel
→ standby/rejected depending feed

Assolombarda
→ standby

Ars Technica
→ standby

Italian Tech Alliance
→ production-readiness candidate
```

Current immediate priority:

> **Finish the documentation checkpoint, then commission the fresh Career Agent source-research pass.**

Expected following sequence:

```text
documentation checkpoint
→ commit/push
→ refresh canonical project sources
→ Career Agent research prompt
→ Career Agent source research
→ Development handoff
→ new chat
→ controlled audit batch
→ explicit Phase 4 vs Phase 5 decision
```

---

# Changelog

## 2026-08-18 — Twelve-Source / Ten-Domain Phase 4 Checkpoint

- Updated active production sources from eight to twelve.
- Updated implemented domains from nine to ten.
- Recorded Italy as implemented rather than pending.
- Added Federal Reserve Board Monetary Policy as an active Tier 1 source.
- Recorded Economics/Macro source default for Fed Monetary Policy.
- Added `FOMC`, `Federal Open Market Committee` and `discount rate` after controlled testing and historical regression.
- Added MIMIT News as an active Tier 1 Italy source.
- Added Italy as the tenth domain with source-defined classification and an empty keyword list.
- Added MIMIT secondary classification terms:
  - `tavoli di crisi`;
  - `accordo di sviluppo`;
  - `quadro industriale`;
  - `rilevanza strategica`;
  - `inflazione`.
- Recorded the generic HTML-to-text normalisation improvement triggered by MIMIT.
- Added Lavoce.info Imprese as an active Tier 2 Italy source.
- Added:
  - `fusione e acquisizione`;
  - `piano industriale`;
  - `IA`;
  - `mercati dei capitali`.
- Recorded zero unintended historical regressions for the retained Lavoce keywords.
- Added Google DeepMind News as an active Tier 1 AI source.
- Recorded 100/100 DeepMind AI classification through source default.
- Recorded that no new DeepMind keywords were required.
- Recorded the real 18 August 2026 twelve-source run:
  - 12 active;
  - 12 successful;
  - 0 failed;
  - 0 invalid;
  - 0 warnings;
  - status success.
- Reframed Financial Markets from "no dedicated source" to "dedicated monetary/rates evidence exists; broader markets remain incomplete."
- Reframed Companies/Corporate Strategy from severe incidental coverage to materially improved but globally incomplete.
- Reframed Italy from structural gap to viable first implementation.
- Reframed AI from OpenAI concentration to OpenAI + DeepMind primary diversity, with independent reporting still missing.
- Closed Nasdaq as standby under current persistence terms.
- Closed Federal Reserve Banking/Regulatory as standby.
- Closed MIMIT Incentives as standby.
- Closed Lavoce General as rejected for production.
- Closed Lavoce Banche e finanza as standby.
- Closed Bruegel General RSS as rejected because of event/session noise.
- Closed Bruegel Analysis and Publications as standby because malformed feeds also expose excessive/full-content payloads.
- Closed Assolombarda News and Comunicati stampa as standby because of missing timestamps and persistence concerns.
- Kept Assolombarda Centro Studi in the manual/research layer.
- Closed Ars Technica as standby under current persistence terms.
- Retired the completed Nasdaq→DeepMind technical audit queue.
- Replaced the old queue with a fresh Career Agent source-research requirement.
- Set the remaining research gaps as:
  - global Companies/Corporate Strategy;
  - broader Financial Markets;
  - independent AI/Technology reporting;
  - independent Europe/EU interpretation;
  - Startups/VC diversification;
  - Milan/Lombardy business and professional ecosystem.
- Preserved Italian Tech Alliance as a production-readiness candidate whose basic audit should not be repeated.
- Added an explicit Phase 4 exit decision after the next source-research/audit cycle.
- Recorded selective GitHub Copilot use as an optional development speed-up for narrow mechanical multi-file edits.
- Preserved richer-report design as the next major product phase if marginal source expansion falls below the value of richer context.

## 2026-08-17 — Phase 4 Source-Audit Consolidation and New Expansion Strategy

- Reconciled the roadmap with the pushed eight-source / nine-domain production checkpoint.
- Recorded Tech Europe Foundation as the first active Milan/Bocconi source.
- Recorded Milan and Bocconi Ecosystem as an implemented source-defined domain with no keywords.
- Recorded the successful real eight-source pipeline integration.
- Recorded the Artificial Intelligence `AI` case-sensitivity correction following Italian false positives.
- Recorded completed Financial Times audit and standby decision.
- Recorded completed Il Sole 24 Ore audit and standby decision.
- Recorded Bank of Italy RSS as standby.
- Recorded Bank of Italy BDS as an approved future structured-data architecture.
- Recorded completed Reuters audit and zero-cost production limitation.
- Recorded B4i as legacy/superseded by TEF.
- Recorded Bocconi Career Services as a high-value manual/private layer.
- Recorded broad Bocconi Events/News as unsuitable for current automation.
- Recorded Italian Tech Alliance as a production-readiness candidate.
- Incorporated the second Career Agent strategic source-expansion research.
- Reframed source expansion around information-function gaps rather than publisher count.
- Identified Financial Markets, Companies, Italy and independent AI as the highest-cost gaps.
- Established the controlled Nasdaq→DeepMind audit queue.
- Preserved richer-report design as deferred until Phase 4 source/domain breadth became sufficiently mature.

## 2026-08-17 — Phase 4A Tech.eu Replacement and Financial Markets Activation

- Incorporated the first Career Agent strategic source/domain audit into the development sequence.
- Formalised the narrow Premium Bocconi Exception while preserving the prohibition on authenticated automated ingestion.
- Directly compared Tech.eu and Sifted through the real collector.
- Observed 20/20 Tech.eu descriptions versus 0/24 Sifted descriptions.
- Approved Tech.eu as the replacement for Sifted.
- Removed Sifted from the active source registry.
- Added Tech.eu as Tier 2, Europe, with no source-default domain.
- Tested Tech.eu with and without a Startups/VC source default.
- Rejected the blanket Startups/VC default because Tech.eu is heterogeneous.
- Added `acquired` to Companies and Corporate Strategy after a real M&A recall gap.
- Added `early-stage fund` and `funding market` to Startups/VC after real Tech.eu evidence.
- Removed generic `startup` because it promoted weak startup profiles too easily.
- Added `tariffs` to Global Politics and Geopolitics after a relevant trade/geopolitics miss.
- Activated Financial Markets as the eighth domain with a conservative keyword set.
- Validated taxonomy changes against stored historical records.
- Completed a real 17 August pipeline run.
- Manually inspected the generated report.
- Recorded that classification rate alone is not a product-quality KPI.
- Preserved zero recurring cost, deterministic processing, credential safety and public-repository constraints.

## 2026-08-14 — Phase 3 Production Closeout and Phase 4 Entry

- Reconciled the roadmap with completed GitHub Actions automation.
- Recorded manual and scheduled production execution.
- Recorded automated repository persistence.
- Recorded degraded and critical failure validation.
- Recorded GitHub scheduler latency.
- Recorded source accessibility and metadata richness as active product-quality concerns.
- Recorded Bocconi reading access as separate from automated-ingestion permission.
- Made source/domain correction the active milestone.
- Deferred richer-report design until after source correction.

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