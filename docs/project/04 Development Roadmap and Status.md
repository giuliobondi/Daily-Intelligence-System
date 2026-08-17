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

The project should not move to the next phase until the current phase has a clear completion condition or there is evidence that a different immediate priority creates materially more user value.

---

# Current Project Status

| Field | Current Status |
|---|---|
| Project Phase | Phase 4 — Source and Domain Correction / Expansion |
| Current Milestone | Milestone 4 — Correct and expand the source and domain universe |
| Repository Status | Public Python repository with automated GitHub-native daily execution and repository-native historical outputs |
| Implementation Status | Deterministic collect → normalize → validate → filter → deduplicate → classify → rank → store → report pipeline implemented and production-validated |
| Automation Status | GitHub Actions implemented; manual and scheduled execution validated; outputs persisted automatically |
| Production Schedule | Daily at 06:05 Europe/Rome; GitHub scheduling latency remains an observed operational limitation |
| Source Registry | Eight active production sources |
| Taxonomy Status | Nine implemented domains; Financial Markets and Milan/Bocconi active; Italy remains the only strategic macroarea without a dedicated implemented domain |
| Testing Status | Targeted and full automated suites passing at the latest pushed checkpoint |
| Latest Local Validation | Real 17 August 2026 pipeline run completed successfully with 8/8 sources successful |
| Latest Integration Result | Tech Europe Foundation collected successfully; no stale TEF records entered the tested 24-hour window |
| Current Product-Quality Finding | Information breadth remains insufficient despite technical stability; Financial Markets, Companies, Italy and independent AI coverage remain structurally weak |
| Current Blockers | No automation blocker; source/domain breadth and information quality are the active constraints |
| Current Priority | Begin the next domain-gap-driven source-audit batch; Nasdaq first |
| Current Git State | Latest implementation checkpoint pushed; canonical documentation reconciliation in progress |

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

## Information-Quality Decisions

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
- Retry logic should not be added without evidence.
- A technically compatible source is not automatically a good production source.
- Production source quality must consider both automation suitability and end-user usefulness.
- A source may be replaced instead of receiving source-specific complexity.
- Report quality must be evaluated independently from run success.
- Source expansion should solve information-function gaps rather than target publisher count.
- Phase 4 does not require an arbitrary number of sources per domain.
- Strong primary evidence and strong independent interpretation are different information roles.
- Missing global FT/Reuters-style corporate reporting can remain an explicit limitation rather than being filled with inferior substitutes.

## Premium / Institutional Access

- Bocconi reading access is distinct from production automation permission.
- A narrow Premium Bocconi Exception exists for unusually valuable publications.
- The exception never permits:
  - authenticated automated retrieval;
  - credential storage;
  - paywall bypass;
  - premium article-body persistence.
- Premium sources still require a legitimate public or automation-compatible discovery endpoint.
- Financial Times and Il Sole 24 Ore have been audited under this model and remain inactive.

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

Build a source and domain universe strong enough for actual daily use before investing in richer report-context logic.

Infrastructure is no longer the main bottleneck.

The active problems are:

- missing information functions;
- weak domain coverage;
- source concentration;
- reader accessibility;
- uneven metadata richness;
- classification recall/precision;
- source-specific persistence/licensing constraints.

The current expansion philosophy is:

> **Correct information-function gaps before correcting publisher-count gaps.**

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

# Phase 4B — Major Source Audits and Milan/Bocconi Implementation

This work established durable source decisions and the first Milan/Bocconi production architecture.

---

## 1. Financial Times Audit

### Outcome

Strategically excellent.

Official RSS exists, but FT RSS-specific terms conflict with the system's permanent archival model.

The production system deliberately persists:

```text
processed JSONL
daily Markdown
Git history
```

The RSS archival constraint is therefore incompatible with current architecture.

### Decision

> **Standby — access/persistence conflict.**

Revisit only if a materially different zero-cost permission or public interface supports automated discovery plus permanent public persistence.

---

## 2. Il Sole 24 Ore Audit

### Outcome

Technically strong.

Tested RSS feeds:

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

Italian classification was feasible.

### Important Secondary Finding

Italian content exposed a false Artificial Intelligence classification:

```text
Italian word "ai"
→ incorrectly matched English AI keyword
```

### Decision

Il Sole remains:

> **Standby — strategically valuable and technically compatible, but persistence/licensing compatibility is not sufficiently clean.**

This is not a permanent rejection.

---

## 3. Artificial Intelligence Case-Sensitivity Fix

### Observed Failure

The lowercase configured keyword:

```text
ai
```

matched the ordinary Italian word:

```text
ai
```

This created false Artificial Intelligence classifications.

### Smallest Correction

Production config changed to:

```text
AI
```

Classifier convention changed to:

```text
lowercase keyword
→ case-insensitive

keyword containing uppercase
→ case-sensitive
```

### Validation

- historical AI records reviewed;
- useful English AI recall preserved;
- false Italian AI matches removed;
- targeted tests passed;
- full suite passed.

### Decision

The case convention is now part of deterministic classifier behaviour.

No language detector or NLP layer is justified.

---

## 4. Bank of Italy RSS Audit

### Outcome

Official RSS infrastructure exists.

Narrow feeds tested successfully included:

```text
Financial Market
Italian Economy in Brief
```

Both passed collection and normalisation.

Main weakness:

```text
no RSS descriptions
```

### Decision

> **Standby.**

Do not add merely because the feeds are technically compatible.

---

## 5. Bank of Italy BDS Discovery

A more important longer-term route was identified through the official Bank of Italy statistical database.

### Capability

Official structured exports support data and metadata suitable for machine use.

Potential intelligence areas include:

- Ita-coin;
- interest rates;
- public debt;
- borrowing requirement;
- balance of payments;
- banking;
- financial markets.

### Architecture Requirement

Proper use would require:

```text
selected series
→ observations
→ release/change detection
→ revision handling
→ deterministic significance rules
→ intelligence event
→ normal classification/ranking/reporting
```

### Decision

> **Approved future structured-data enhancement — deferred.**

Do not add a statistical-event pipeline while article-source breadth remains the higher-value bottleneck.

---

## 6. Reuters Audit

### Outcome

Strategically exceptional.

Official machine-delivery products exist, but the discovered routes are professional/licensed.

No clean official zero-cost production endpoint suitable for the current architecture was found.

### Rejected Alternatives

Do not use:

- scraping;
- undocumented internal endpoints;
- third-party Reuters feed generators.

### Decision

> **Standby / production-ineligible under current constraints.**

Do not allow Reuters research to block Phase 4.

---

# Phase 4C — Milan/Bocconi Research and First Production Implementation

## Product Requirement

Milan/Bocconi is a fixed macroarea.

The desired function is:

> **Professional Ecosystem Intelligence**

not generic local news.

Priority information includes:

- recruiting;
- finance/consulting/AI/startup events;
- programmes;
- competitions;
- research opportunities;
- professional deadlines;
- Milan startup/VC/innovation developments.

---

## B4i

B4i was investigated as a candidate.

### Finding

B4i is transitioning into / has been superseded by Tech Europe Foundation.

No useful durable B4i feed was identified.

### Decision

> **Legacy / superseded by TEF.**

---

## Tech Europe Foundation

Official News RSS:

```text
https://tef.tech/news/feed/
```

### Technical Validation

Observed test sample:

```text
10 entries
10 descriptions
10 timestamps
10 links
```

Collector:

```text
passed
```

Normalizer:

```text
passed
```

### Classification Finding

Without a source default:

```text
9 of 10 tested TEF records remained unclassified
```

The problem was not missing generic keywords.

TEF's value comes from institutional/ecosystem identity.

### Architecture Decision

Added domain:

```text
Milan and Bocconi Ecosystem
```

with:

```yaml
keywords: []
```

Added TEF source default:

```text
Tech Europe Foundation
→ Milan and Bocconi Ecosystem
```

This required a small general configuration capability:

> domains may use an empty keyword list when classification is deliberately source-defined.

No special collector, scraper, opportunity database or event subsystem was added.

---

## TEF Ranking Review

Current ranking formula:

```text
source-tier score
+ 2 × domains
+ 1 × matched keywords
```

Typical TEF baseline:

```text
Tier 1         = 4
Milan domain   = 2
total          = 6
```

One multi-domain test story reached:

```text
12
```

because of additional topical classifications and keywords.

Report selection is constrained by:

```text
max 5 items per primary domain
max 30 items total
```

### Decision

No ranking change justified.

Do not lower TEF's source tier merely to manipulate scores.

---

## TEF Real Pipeline Validation — 17 August 2026

A real local production-equivalent run after TEF integration produced:

```text
8 active sources
8 successful sources
0 failed
0 invalid

1295 valid collected records
40 inside the collection window
37 unique records
29 unclassified
8 displayed

status: success
```

TEF collection:

```text
10 source entries collected
```

Processed TEF records inside the current window:

```text
0
```

This was expected because the current TEF feed entries were older than the rolling 24-hour window.

### Decision

> **TEF integration passed the production gate.**

---

## Bocconi Career Services

### Finding

Strategically extremely valuable.

Public pages expose some:

- recruiting events;
- finance events;
- employer activity;
- registration windows.

However, complete infrastructure sits partly behind:

```text
yoU@B
JobGate
```

No clean public structured route covering the full universe was found.

### Decision

> **Manual/private layer.**

Do not automate authenticated Bocconi access.

---

## Bocconi General Events / News

### Finding

Contains some high-value events but large amounts of:

- admissions;
- prospective-student activity;
- generic campus events;
- cultural noise.

No clean narrow structured feed was established.

### Decision

> **Do not build a broad Bocconi crawler during Phase 4.**

---

# Phase 4D — Italian Tech Alliance Initial Audit

Official RSS:

```text
https://www.italiantechalliance.com/blog-feed.xml
```

### Technical Result

Tested sample:

```text
20 entries
20 timestamps
20 links
20 descriptions
0 normalisation errors
```

### Product Strength

Real signals include:

- Italian VC statistics;
- investor ecosystem developments;
- startup policy;
- Scaleup Fund;
- Venture Academy;
- Tech Transfer Academy.

### Product Weakness

Descriptions are extremely thin.

The feed also includes repeated press-clipping stories about the same underlying event or dataset.

### Classification

Candidate Startups/VC keywords tested:

```text
round
scaleup fund
```

Historical regression produced only relevant changes.

### Decision

> **Production-readiness candidate.**

Basic feed and classification research is complete.

Do not repeat the audit from zero.

Remaining question:

> Does the unique Italian VC/opportunity value justify activation despite thin descriptions and repetition?

Do not implement near-duplicate clustering specifically for ITA until real production evidence proves it necessary.

---

# Phase 4E — Second Strategic Source-Expansion Research

A second Career Agent research pass was completed after the user determined that the information universe remained too narrow.

## Core Finding

The concern is justified.

The main issue is not simply source count.

The highest-cost information gaps are:

```text
1. Financial Markets / Companies
2. Italy
3. independent AI / Technology
```

Additional concentration remains in:

```text
Startups / VC
Milan / Bocconi
```

## Strategic Principle

Do not attempt to recreate Reuters or Financial Times by accumulating weaker general-news publications.

Build breadth through complementary information roles.

Strategic examples:

```text
Nasdaq
→ markets / earnings / IPOs / corporate finance

Federal Reserve
→ monetary policy / rates / credit / financial conditions

MIMIT
→ Italian industrial policy / company situations

Lavoce.info
→ independent Italian economic interpretation

Bruegel
→ independent European policy/economic analysis

Assolombarda
→ Milan/Lombardy firms / industry / professional ecosystem

Ars Technica
→ independent AI/technology reporting

Google DeepMind
→ second frontier-lab AI primary source
```

These conclusions are strategic research inputs.

They are **not technical production approvals**.

Detailed source reasoning belongs in:

```text
03 Information Taxonomy and Source Policy.md
```

---

# Current Phase 4 Source Registry

Current active production sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Tech.eu;
8. Tech Europe Foundation.

Current working position:

| Source | Current Position |
|---|---|
| BBC News World | Retain |
| BBC News Business | Retain temporarily; reconsider only after stronger business/markets coverage is proven |
| European Central Bank | Core |
| European Commission Highlighted News | Retain selectively |
| Istat Press Releases | Core |
| OpenAI News | Retain as one AI primary source |
| Tech.eu | Active European startup/technology specialist |
| Tech Europe Foundation | Active first Milan/Bocconi source |

---

# Current Phase 4 Domain Universe

Implemented:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Companies and Corporate Strategy;
4. Artificial Intelligence;
5. Technology and Software;
6. Startups and Venture Capital;
7. Europe and the European Union;
8. Financial Markets;
9. Milan and Bocconi Ecosystem.

Not yet implemented:

10. Italy.

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

Not the highest Phase 4 opportunity cost.

---

## Economics and Macroeconomics

Current:

```text
ECB
Istat
European Commission
BBC Business
```

Assessment:

> Reasonable but Europe/Italy-heavy and institutionally concentrated.

Main missing roles:

- US/global monetary evidence;
- independent European interpretation.

---

## Companies and Corporate Strategy

Current:

```text
BBC Business
Tech.eu incidental coverage
```

Assessment:

> **Severe gap.**

Missing:

- structured company developments;
- earnings;
- capital allocation;
- corporate financing;
- restructuring;
- broader corporate strategy.

---

## Financial Markets

Current:

```text
domain exists
no dedicated production source
```

Assessment:

> **Major gap.**

Missing:

- rates/yields context;
- financial conditions;
- market structure;
- capital markets;
- IPOs;
- company/market interaction.

---

## Artificial Intelligence

Current:

```text
OpenAI News
+ incidental Tech.eu/BBC
```

Assessment:

> Too concentrated on one primary vendor.

Desired structure:

```text
OpenAI
+ second primary AI lab
+ independent reporting
```

---

## Technology and Software

Current:

```text
Tech.eu
OpenAI spillover
BBC spillover
```

Assessment:

> Moderate.

Independent systems/software reporting would improve it, but other domains currently have higher opportunity cost.

---

## Startups and Venture Capital

Current:

```text
Tech.eu
```

Assessment:

> Too dependent on one specialist.

Italian Tech Alliance is the strongest already-audited complement.

---

## Europe and the EU

Current:

```text
ECB
European Commission
```

Assessment:

> Strong primary evidence, weak independent interpretation.

---

## Italy

Current:

```text
Istat contribution only
no dedicated Italy domain
```

Assessment:

> **Major structural gap.**

Italy should eventually be built through differentiated information functions rather than one generic national publication.

---

## Milan and Bocconi Ecosystem

Current:

```text
Tech Europe Foundation
```

Assessment:

> First production implementation complete, broader requirement still incomplete.

Missing:

- established firms;
- industry;
- finance/business ecosystem;
- professional events;
- recruiting;
- selected deadlines.

---

# Current Source Audit Decision Summary

Detailed rationale is owned by `03 Information Taxonomy and Source Policy.md`.

| Source | Current Development Status |
|---|---|
| Sifted | Removed; replaced by Tech.eu |
| Tech.eu | Active |
| Financial Times | Standby — persistence/access conflict |
| Il Sole 24 Ore | Standby — technically strong; persistence/licensing unresolved |
| Reuters | Standby / incompatible with current zero-cost machine-delivery constraints |
| Bank of Italy RSS | Standby |
| Bank of Italy BDS | Approved future structured-data enhancement |
| B4i | Legacy / superseded by TEF |
| Tech Europe Foundation | Active |
| Bocconi Career Services | Manual/private layer |
| Bocconi general Events/News | Not suitable for current architecture |
| Italian Tech Alliance | Production-readiness candidate |
| Fintech District | Standby candidate |

---

# Current Domain-Gap-Driven Technical Audit Queue

Use this order unless Development evidence changes the expected value.

---

## 1. Nasdaq

### Expected Role

- Financial Markets;
- Companies / Corporate Strategy;
- earnings;
- IPOs;
- corporate finance;
- market structure.

### Development Questions

- Which exact official feeds exist?
- Which narrow categories provide the highest signal?
- Are terms compatible with permanent public repository persistence?
- How rich are titles/descriptions/timestamps?
- How much retail-investor or stock-picking noise appears?
- Can 1–3 narrow feeds solve the gap without creating a firehose?
- How much overlap exists with BBC Business?

### Why First

Financial Markets currently has no dedicated production source and Companies remains weak.

---

## 2. Federal Reserve Board

### Expected Role

- Economics/Macro;
- Financial Markets;
- monetary policy;
- rates;
- credit;
- financial conditions;
- banking.

### Development Questions

- Which official RSS feeds are highest-value?
- Are reuse/public-domain conditions as clean as strategic research suggests?
- Which subset avoids excessive routine material?
- Can the current article pipeline support the useful feeds without new architecture?

### Why Second

Likely a high-quality, low-complexity Tier 1 addition with global market relevance.

---

## 3. MIMIT

Ministero delle Imprese e del Made in Italy.

### Expected Role

- Italy;
- Companies;
- industrial policy;
- restructuring;
- strategic investment;
- technology/innovation.

### Development Questions

- Which official RSS feeds exist?
- Are reuse terms compatible with public repository persistence?
- How noisy are routine ministerial announcements?
- Can deterministic classification isolate company/industry developments?
- Should the Italy domain be introduced with or after MIMIT?

### Why Before Lavoce

Strategic research suggests clearer official structured access and potentially cleaner reuse conditions.

---

## 4. Lavoce.info

### Expected Role

- independent Italian economic interpretation;
- Economics/Macro;
- Companies;
- Europe;
- Financial Markets.

### Development Questions

- Is there a current stable official RSS/structured feed?
- What metadata does it expose?
- Are reuse conditions compatible with stored feed descriptions?
- How selective and frequent is publication?
- Does it complement rather than duplicate Istat/MIMIT?

---

## 5. Bruegel

### Expected Role

- independent Europe/EU analysis;
- economics;
- capital markets;
- industrial policy;
- trade/competitiveness.

### Development Questions

- Which RSS feeds are available?
- Can event/session noise be avoided?
- What does CC BY-ND permit for stored feed descriptions and deterministic truncation?
- Is the source sufficiently frequent for daily intelligence?

---

## 6. Assolombarda

### Expected Role

- Milan/Bocconi ecosystem;
- Italy;
- companies;
- industry;
- credit;
- labour/skills;
- economic research;
- professional events.

### Development Questions

- What current RSS endpoints exist?
- Is calendar export useful and automation-compatible?
- What reuse rules apply?
- Can member-service and routine webinar noise be controlled?
- Does the source materially complement TEF?

### Strategic Complementarity

```text
TEF
→ startups / deep tech / university innovation

Assolombarda
→ established companies / industry / Milan economy
```

---

## 7. Ars Technica

### Expected Role

- independent AI;
- Technology;
- software;
- cybersecurity;
- infrastructure.

### Development Questions

- Which official feeds best isolate AI/technology value?
- What archive/reuse conditions apply?
- How much consumer/gadget noise remains?
- Does the source materially reduce vendor concentration?

---

## 8. Google DeepMind News

### Expected Role

- second frontier-lab AI primary source;
- research;
- models;
- robotics;
- safety;
- scientific AI.

### Development Questions

- Validate official RSS endpoint.
- Inspect metadata.
- Verify terms/persistence compatibility.
- Inspect overlap with OpenAI/Tech.eu/BBC.
- Confirm that one additional lab is enough before considering more.

---

# Parallel Phase 4 Action — Italian Tech Alliance

Italian Tech Alliance should not re-enter basic source discovery.

The next decision is production readiness.

## Remaining Questions

- How much unique Italian VC/opportunity value appears over a realistic recent sample?
- How often does press-clipping repetition degrade the report?
- Are `round` and `scaleup fund` still justified when tested in the final source configuration?
- Does activating ITA materially improve Startups/VC and Italy without creating excessive duplication?

## Constraint

Do not build near-duplicate clustering solely to support ITA unless repeated real reports demonstrate a meaningful problem.

---

# Secondary Candidate Queue

Do not audit these before higher-priority gaps unless evidence changes.

## MEF — Dipartimento del Tesoro

Potential role:

- sovereign debt;
- government bond issuance;
- Italian financial system.

Risk:

- routine auction noise.

## ESMA

Potential role:

- EU securities markets;
- market risk;
- asset management;
- financial regulation.

## Invest Europe

Potential role:

- European PE/VC ecosystem;
- fundraising;
- exits;
- private capital.

## BIS

Potential role:

- global financial conditions;
- credit;
- non-bank finance;
- financial-system research.

## SEC EDGAR

Potential role:

- primary company-event evidence.

Constraint:

> Requires a deliberately narrow company/form universe.

## ISPI

Potential role:

- geopolitics;
- geoeconomics;
- Milan professional ecosystem.

## Camera di Commercio Milano Monza Brianza Lodi

Potential role:

- firms;
- SMEs;
- innovation;
- financing;
- local business research.

## Euronext

Potential role:

- European IPOs;
- listings;
- bonds;
- capital-market infrastructure.

## IMF

Potential role:

- global macro;
- financial stability.

## AIFI

Potential role:

- Italian private equity;
- venture capital;
- private debt.

---

# Sources Not Worth Current Development Time

Do not currently prioritise:

- WSJ;
- CNBC;
- Guardian Business;
- WIRED;
- MarketWatch;
- Fortune;
- ANSA;
- TechCrunch;
- Business Wire and generic press-release aggregators;
- generic Bocconi event feeds;
- generic Politecnico event feeds;
- additional central banks beyond the Fed;
- multiple additional AI labs.

These sources may be reconsidered only if higher-priority audits fail or a clearly differentiated need appears.

---

# Phase 4 Completion Criteria

Phase 4 is complete when:

- every active source has a deliberate strategic and technical role;
- weak sources have explicit retain/replace/remove decisions;
- Sifted replacement remains stable in production;
- Financial Markets has sufficiently useful source coverage;
- Companies/Corporate Strategy is no longer dependent almost entirely on incidental coverage;
- Italy has a validated low-maintenance implementation decision and, if justified, an active dedicated domain;
- Milan/Bocconi has a sufficiently useful low-maintenance public-source implementation rather than merely nominal coverage;
- AI coverage is no longer structurally defined by OpenAI alone;
- Startups/VC coverage is sufficiently differentiated for actual use;
- high-priority source candidates have explicit technical decisions;
- additional source expansion has lower expected value than richer-report design;
- source/default/keyword changes have regression evidence;
- full automated tests pass;
- real collection remains reliable;
- generated reports are manually inspected;
- source concentration and accessibility are acceptable;
- no credentials or restricted article bodies are introduced;
- zero recurring monetary cost remains intact.

Phase 4 does **not** require:

- every target source to be implemented;
- every domain to have equal source counts;
- a fixed minimum number of publishers;
- perfect global business coverage;
- a replacement for every premium publication;
- all ten macroareas to have identical technical architecture.

The correct stopping question is:

> **Would another source/domain change create more user value than improving the context of stories already being selected?**

If the answer becomes no across repeated reports, move to Phase 5.

## Status

> **Active — first source-correction and Milan/Bocconi implementation checkpoints are complete; Phase 4 continues with domain-gap-driven source expansion.**

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

Do not begin implementation merely because the richer-context problem is already validated.

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

**Not started — validated requirement, intentionally deferred behind Phase 4**

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

# Active Product-Quality Findings

## 1. Information Breadth Remains Insufficient

The system is technically stable, but several macroareas remain too narrow.

Current highest-cost gaps:

```text
Financial Markets
Companies / Corporate Strategy
Italy
independent AI / Technology
```

Secondary concentration problems:

```text
Startups / VC
Milan / Bocconi
```

### Consequence

Continue Phase 4.

Do not move to richer-report design merely because automation and first source corrections are complete.

---

## 2. Source Metadata Quality Is a Product Requirement

Sifted and Tech.eu were both technically compatible.

Observed comparison:

```text
Sifted  → 0/24 tested descriptions
Tech.eu → 20/20 tested descriptions
```

### Consequence

Feed richness can justify source replacement even when both sources collect successfully.

---

## 3. Automation Suitability and Reader Accessibility Are Independent

A source can be:

```text
technically excellent
but inaccessible to the user
```

or:

```text
excellent for the reader
but unsuitable for automated ingestion
```

### Consequence

Every source audit must evaluate both dimensions.

Owner:

```text
03 Information Taxonomy and Source Policy.md
```

---

## 4. Premium Reading Access Does Not Solve Persistence Constraints

FT and Il Sole demonstrated that legitimate reader access does not automatically create a lawful permanent public ingestion path.

### Consequence

Do not weaken the credential or copyright boundary to add a prestigious source.

---

## 5. Classification Rate Is Not a Product KPI

Recent reports have shown high unclassified shares.

Manual inspection established that most excluded records were correctly low-value or out of scope.

### Consequence

Do not optimise for a higher classified percentage.

Optimise for:

- valuable stories included;
- weak stories excluded;
- correct domain assignment;
- useful ranking.

---

## 6. Broad Keywords Can Damage Ranking

Because relevance score contains:

```text
+ 2 per domain
+ 1 per matched keyword
```

broad keywords can create both classification and ranking inflation.

### Consequence

Keyword expansion remains simulation-driven.

---

## 7. Multilingual Keyword Collisions Are Real

Italian source testing exposed:

```text
AI
vs
Italian "ai"
```

### Consequence

The intentional case-sensitive acronym convention is now part of production behaviour.

Do not add more complex language tooling unless simpler deterministic rules fail.

---

## 8. Financial Markets Needs Causal, Not Trading, Coverage

The domain should capture:

- rates;
- bonds;
- credit;
- liquidity;
- capital markets;
- financial stability;
- meaningful repricing;
- corporate financing.

It should not become:

- daily index recaps;
- trading tips;
- price predictions;
- stock-picking content.

### Consequence

Nasdaq must be audited at category/feed level rather than ingested broadly.

---

## 9. Milan/Bocconi Is Implemented but Not Solved

TEF proves that the macroarea can fit the existing architecture without custom infrastructure.

It currently covers mainly:

- entrepreneurship;
- startup/deep-tech activity;
- innovation;
- selected ecosystem developments.

Missing:

- established companies;
- finance/business events;
- recruiting;
- complete deadlines;
- broader Milan professional intelligence.

### Consequence

Continue complementary source research.

Do not build private Career Services scraping.

---

## 10. New Architecture Requires Stronger Evidence Than New Sources

Bank of Italy BDS would require a statistical-event pipeline.

Bocconi opportunities could eventually justify deadline/state tracking.

Italian Tech Alliance could eventually motivate near-duplicate clustering.

None currently justifies immediate architecture expansion.

### Consequence

Prefer current pipeline reuse first.

---

## 11. Residual Gaps Can Remain Explicit

No clean candidate currently reproduces Reuters/FT-quality global corporate journalism under the project's constraints.

### Consequence

Accept the gap rather than filling it with inferior or legally ambiguous sources.

---

# Current Validation Record

## Phase 4A — Tech.eu / Financial Markets

Validated:

- Tech.eu direct collection;
- Tech.eu normalisation;
- description-richness comparison;
- source-default simulation;
- keyword simulation;
- historical regression;
- Financial Markets activation;
- `startup` removal;
- full automated tests;
- real pipeline;
- manual report review.

Status:

> **Passed and pushed.**

---

## AI Case-Sensitivity Fix

Validated:

- Italian false-positive reproduction;
- historical English AI recall;
- targeted tests;
- full suite;
- Il Sole rerun.

Observed result:

```text
false Italian AI matches removed
```

Status:

> **Passed and pushed.**

---

## TEF / Milan-Bocconi Integration

Validated:

- RSS endpoint;
- metadata;
- collector;
- normalizer;
- empty-keyword domain configuration;
- source-default classification;
- ranking behaviour;
- targeted tests;
- full suite;
- real pipeline run;
- processed-output inspection.

Real integration run:

```text
8 active
8 successful
0 failed
1295 valid
40 window-eligible
37 unique
29 unclassified
8 displayed
status: success
```

TEF inside current processed 24-hour output:

```text
0
```

Expected because feed entries were older than the monitored window.

Status:

> **Passed and pushed.**

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

The full source audit register belongs in:

```text
03 Information Taxonomy and Source Policy.md
```

This roadmap should contain only enough source-status information to control implementation sequencing.

---

# Immediate Next Actions

## Current Documentation Checkpoint

Complete the canonical document reconciliation:

1. `03 Information Taxonomy and Source Policy.md`;
2. `04 Development Roadmap and Status.md`;
3. `02 System Architecture.md`;
4. `01 Product Requirements.md`;
5. `00 Project Brief.md`.

Then:

1. inspect documentation diffs;
2. confirm no unintended files are staged;
3. commit documentation reconciliation;
4. push;
5. refresh project source files;
6. verify the refreshed documents;
7. move to a new Development chat with a concise handoff.

---

# Next Highest-ROI Development Step

After the documentation checkpoint:

> **Begin the Nasdaq technical/source-policy audit.**

The audit should answer:

```text
Which exact official Nasdaq feed(s)
solve the Financial Markets + Companies gap
with acceptable noise, metadata, rights,
maintenance and public-repository compatibility?
```

Do not activate Nasdaq merely because an RSS directory exists.

Proceed through the standard source audit:

```text
strategic role
→ endpoint/terms research
→ technical probe
→ collector
→ normalizer
→ classification
→ historical regression
→ report contribution
→ production decision
```

---

# Following Controlled Steps

If Nasdaq reaches a stable decision:

```text
Federal Reserve
→ stable decision

MIMIT
→ stable decision

Lavoce.info
→ stable decision

Bruegel
→ stable decision

Assolombarda
→ stable decision

Ars Technica
→ stable decision

Google DeepMind
→ stable decision
```

In parallel, when convenient:

```text
Italian Tech Alliance
→ production-readiness decision
```

Do not audit several candidates deeply at once.

One controlled source decision at a time remains the default.

---

# Stop Condition Before Phase 5

Do not begin richer-report implementation until:

- the largest domain gaps have explicit source decisions;
- Financial Markets has meaningful production coverage;
- Companies/Corporate Strategy is materially stronger;
- Italy has an implementation decision;
- Milan/Bocconi has more than nominal ecosystem coverage or has reached a justified public-source limit;
- AI has an explicit diversity decision;
- further source work shows lower expected marginal value than richer context.

The switch to Phase 5 should be based on repeated real-report evidence rather than:

- a date;
- a source count;
- a domain-count quota;
- exhaustion with source research.

---

# Current Status Summary

```text
Phase 0  Complete
Phase 1  Complete
Phase 2  Complete
Phase 3  Complete
Phase 4  Active
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
8 active sources
9 active domains

Sifted
→ replaced by Tech.eu

Financial Markets
→ implemented

AI keyword collision
→ fixed

Milan/Bocconi
→ first production implementation through TEF

FT
→ standby

Il Sole
→ standby

Bank of Italy RSS
→ standby

Bank of Italy BDS
→ future structured-data enhancement

Reuters
→ standby under current constraints

Italian Tech Alliance
→ production-readiness candidate
```

Current immediate priority:

> **Finish canonical documentation reconciliation, then begin the Nasdaq technical audit in a new Development chat.**

---

# Changelog

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
- Established the new controlled audit queue:
  1. Nasdaq;
  2. Federal Reserve;
  3. MIMIT;
  4. Lavoce.info;
  5. Bruegel;
  6. Assolombarda;
  7. Ars Technica;
  8. Google DeepMind.
- Preserved Italian Tech Alliance as a parallel production-readiness decision.
- Preserved richer-report design as deferred until Phase 4 source/domain breadth is sufficiently mature.
- Confirmed that the next Development chat should begin with Nasdaq after canonical documentation reconciliation.

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
- Validated taxonomy changes against 114 stored historical records.
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

- Completed local deterministic collection-to-report pipeline.
- Added collection-window enforcement.
- Added deterministic identity, deduplication, classification, ranking, storage and reporting.
- Added run summaries and logging.
- Reached 104 passing tests.

## Initial Baseline

- Defined the implementation phases.
- Defined the zero-cost, low-maintenance and deterministic development philosophy.
- Established Git and tests as the verification layer.