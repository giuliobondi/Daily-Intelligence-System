# Daily Intelligence System — Development Roadmap and Status

> **Purpose**
>
> This document controls the implementation of the Daily Intelligence System.
>
> It records the current phase, completed decisions, active milestone, blockers, deferred work and next highest-priority action.
>
> It is not a long-term product vision document and should not duplicate the Project Brief, Product Requirements, System Architecture or Information Taxonomy and Source Policy.
>
> ---
>
> **Primary Question**
>
> > *What should be built now, what has already been completed, and what is the next highest-value step?*
>
> ---
>
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
- Prefer a smaller high-value source universe over accumulation of individually prestigious sources.
- Prefer unclassified records over misleading classification.
- Evaluate report quality from real selected and missed stories, not from classification rate alone.

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
| Source Registry | Seven active production sources; Sifted replaced by Tech.eu in the current validated Phase 4 checkpoint |
| Taxonomy Status | Eight implemented domains; Financial Markets now active; Italy remains pending; Milan/Bocconi is a validated requirement pending implementation |
| Testing Status | 110 automated tests passing |
| Latest Local Validation | Real pipeline run completed successfully on 17 August 2026 with 7/7 sources successful and generated report manually inspected |
| Current Product-Quality Findings | Source quality and classification selectivity matter more than raw classification rate; richer report context remains a validated later requirement |
| Current Blockers | No automation blocker; remaining source/domain quality work is the active constraint |
| Current Priority | Close the validated Tech.eu / Financial Markets checkpoint, then technically audit Financial Times |
| Current Git State | Phase 4 implementation locally validated; documentation reconciliation and commit still pending |

---

# Completed Project Decisions

The following decisions are established unless explicitly changed later:

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
- Bocconi institutional credentials and other private credentials must never be embedded in the production pipeline.
- Personal or institutional reading access does not automatically authorise automated ingestion.
- Processed records use JSON Lines.
- Run summaries use JSON.
- Daily reports use Markdown.
- Internal timestamps use timezone-aware UTC datetimes.
- Reports use one primary placement per item, with secondary domains shown as metadata.
- Relevance scoring is deterministic and explainable.
- Repository-native persistence is the current production delivery model.
- GitHub Issues, GitHub Pages and other interface layers remain optional and deferred.
- Broad heterogeneous feeds may use no default domain.
- Source defaults represent genuine source-wide topical evidence rather than publisher category.
- Unclassified records are preferable to misleading classifications.
- A high unclassified rate is not itself a defect.
- Classification quality should be judged by valuable misses and false positives.
- Retry logic should not be added without evidence.
- A technically compatible source is not automatically a good production source.
- Production source quality must consider both automation suitability and end-user usefulness.
- A source may be replaced instead of receiving source-specific complexity.
- Report quality must be evaluated independently from run success.
- Premium Bocconi-accessible publications may receive a narrow source-specific exception when their strategic value justifies thinner automated context.
- The Premium Bocconi Exception never permits authenticated automated article retrieval.
- The smallest strong source universe is preferred over maximum publication coverage.

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

The exact repository tree remains the source of truth if file names later change.

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

> **104 automated tests passed.**

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

## Network Hardening

Real-source testing justified:

- bounded remote HTTP retrieval;
- 10-second timeout;
- explicit User-Agent;
- explicit Accept headers;
- normal SSL verification;
- source-level collection isolation;
- explicit handling of HTTP, URL and timeout errors.

No retry policy was added because evidence did not require it.

## Source-Default Correction

Real reports showed that broad source defaults created misleading classifications and inflated relevance.

The policy became:

```text
broad heterogeneous source
→ no default domain
```

Narrow defaults were retained only when justified.

At Phase 2 closeout:

```text
BBC World           → none
BBC Business        → none
ECB                 → none
European Commission → none
Istat               → Economics and Macroeconomics
OpenAI              → Artificial Intelligence
Sifted              → Startups and Venture Capital
```

## Evidence-Based Keyword Refinement

Real BBC records led to tested additions:

- `war`;
- `conflict`;
- `parliament`.

Broader terms including:

- `government`;
- `defence`;
- `president`;
- `prime minister`;

were rejected because they generated ambiguous matches.

## Real Failure Validation

A controlled valid-source + invalid-source run confirmed:

- source failure isolation;
- `degraded` overall status;
- structured warning visibility;
- preservation of valid output.

At Phase 2 closeout:

> **110 automated tests passed.**

## Status

**Complete**

---

# Phase 3 — GitHub Automation

## Objective

Run the validated production pipeline automatically with zero recurring monetary cost and negligible manual work.

## Implemented Scope

Phase 3 implemented and validated:

- GitHub Actions workflow;
- manual `workflow_dispatch`;
- scheduled execution;
- Python 3.12 hosted runtime;
- deterministic dependency installation;
- full automated tests before production;
- production CLI execution;
- explicit workflow timeout;
- required repository-write permission;
- output validation;
- application logs;
- bot persistence;
- no-empty-commit guard;
- degraded-source publication;
- critical-failure blocking;
- concurrency protection;
- timezone-aware daily schedule.

Production flow:

```text
GitHub trigger
→ checkout
→ Python setup
→ install
→ test
→ run pipeline
→ validate output
→ stage generated artifacts
→ commit if changed
→ push
```

Production contains no:

- paid API;
- OpenAI API call;
- Copilot credit consumption;
- authenticated news access;
- private database;
- cloud infrastructure dependency.

## Production Schedule

Current schedule:

```text
06:05 Europe/Rome
```

GitHub scheduled execution has demonstrated significant latency.

The current report window remains:

```text
actual execution time - 24 hours
→ actual execution time
```

This creates a known coupling:

```text
scheduler delay
→ shifted report cutoff
→ potentially different report composition
```

The problem is recorded but not yet severe enough to justify immediate architecture change.

## Validated Failure Semantics

### Critical configuration failure

A deliberately invalid configuration correctly:

- failed validation/tests;
- stopped production;
- avoided misleading publication.

### Recoverable source failure

A deliberately invalid BBC World endpoint correctly:

- allowed other sources to succeed;
- produced `degraded` status;
- exposed the failed source;
- preserved usable output;
- allowed persistence.

## Status

**Complete**

---

# Phase 4 — Source and Domain Correction / Expansion

## Objective

Correct weak production sources and expand sources/domains only where the resulting information product becomes materially more useful.

This is the current active phase.

---

## Strategic Input Completed

A dedicated Career Agent source/domain audit has been completed.

Its main strategic conclusions were:

- optimize for the smallest high-value information universe;
- prioritize economics, companies, AI, Financial Markets and actionable Milan/Bocconi intelligence;
- retain broad geopolitical awareness without building a generic-news product;
- preserve Startups/VC but reduce low-value funding noise;
- prioritize Financial Times and Il Sole 24 Ore among premium Bocconi-accessible candidates;
- replace Sifted if a better European startup source can preserve its useful coverage;
- treat Milan/Bocconi as a professional ecosystem sensor rather than generic local news.

Strategic approval does not equal technical production approval.

Development remains responsible for:

- endpoint validation;
- automation permission;
- metadata quality;
- timestamp quality;
- collector compatibility;
- maintenance;
- copyright;
- public-repository safety;
- real report quality.

---

# Phase 4A — First Source and Taxonomy Correction

## Problem

Production evidence exposed a concrete weakness in Sifted:

```text
useful startup/VC headline
→ little or no feed description
→ click-through needed
→ Sifted Pro can block article
```

This reduced the usefulness of otherwise relevant report entries.

The objective was not simply to remove a paywall.

The objective was to preserve European startup/VC intelligence with better:

- reader accessibility;
- metadata richness;
- report usefulness;
- source balance.

---

## Sifted vs Tech.eu Audit

Both sources were tested through the project's real collector and normaliser.

### Tech.eu

Observed:

```text
20 items received
20 normalized
20 with descriptions
0 without descriptions
average description length ≈ 203 characters
```

### Sifted

Observed:

```text
24 items received
24 normalized
0 with descriptions
24 without descriptions
```

Both were technically collectible.

The deciding difference was product quality.

Tech.eu also supplied relevant European coverage including:

- startup funding;
- VC funds;
- M&A;
- corporate strategy;
- AI;
- fintech;
- industrial policy;
- European technology.

## Decision

> **Replace Sifted with Tech.eu.**

Current production configuration:

```text
Tech.eu
Tier 2
Europe
RSS
default domains: none
```

Sifted is no longer an active production source.

---

# Tech.eu Source-Default Decision

Tech.eu was initially simulated with a Startups/VC default.

That produced misleading classification because the general feed also contains:

- AI;
- corporate M&A;
- European policy;
- fintech strategy;
- technology;
- industrial developments.

Decision:

```yaml
default_domains: []
```

This preserves the principle:

> source defaults are evidence, not publisher labels.

---

# Phase 4 Keyword Evidence

Removing the blanket source default exposed legitimate classification misses.

Candidate keyword additions were tested on real Tech.eu records before configuration changes.

Initial candidates that showed value included:

```text
Companies / Corporate Strategy
- acquired

Startups / Venture Capital
- early-stage fund
- funding market
```

The candidates were then tested against the existing three-day production corpus:

```text
114 records tested
0 records changed
```

This established that the additions improved Tech.eu recall without observed regression in the previous production universe.

---

# Financial Markets Activation

The Career Agent had strategically approved Financial Markets as a high-value domain.

Real production evidence then provided a concrete missed story:

> a severe South Korean stock-market correction remained unclassified.

A conservative Financial Markets candidate domain was simulated.

The test recovered exactly the intended story through:

```text
stock market
```

without observed unrelated changes in that daily sample.

## Decision

Financial Markets is now the eighth active domain.

Initial conservative keywords:

```text
stock market
bond market
bond yields
yield curve
credit spreads
capital markets
financial stability
market sell-off
foreign exchange
equities
asset management
ipo
```

Broad terms such as:

```text
market
stocks
shares
bonds
rates
bank
investment
```

remain intentionally excluded until real evidence justifies them.

---

# Geopolitics Refinement

A BBC World story about countries helping China evade US tariffs remained unclassified.

The plural keyword:

```text
tariffs
```

was simulated and correctly recovered the story.

It was then included in the three-day regression.

---

# Startups/VC Precision Correction

The generic keyword:

```text
startup
```

caused a low-value Tech.eu startup profile to receive a full Startups/VC domain assignment and score uplift.

The Career Agent had explicitly recommended avoiding generic startup/funding volume.

The keyword was therefore tested for removal.

Observed result:

- low-value Tech.eu startup profile became unclassified;
- historical Sifted records retained their old Startups/VC source default but lost one generic keyword score point;
- no strategically harmful removal was observed in the tested corpus.

## Decision

Remove generic:

```text
startup
```

from the Startups/VC keyword list.

The domain should depend on stronger evidence.

---

# Phase 4A Three-Day Regression

Final candidate taxonomy changes were tested across:

```text
data/processed/2026/08/2026-08-12.jsonl
data/processed/2026/08/2026-08-13.jsonl
data/processed/2026/08/2026-08-14.jsonl
```

Total:

```text
114 records
```

Final changed records:

```text
6
```

They were all interpretable:

- three historical Sifted stories lost only the generic `startup` keyword point;
- one US-China tariff story gained Global Politics/Geopolitics;
- one South Korean stock-market story gained Financial Markets;
- one weak Tech.eu startup profile lost its unsupported Startups/VC classification.

No unexpected regression was observed.

---

# Phase 4A Configuration Changes

Current validated changes:

## Source

```text
Sifted
→ Tech.eu
```

## Global Politics and Geopolitics

Added:

```text
tariffs
```

## Companies and Corporate Strategy

Added:

```text
acquired
```

## Startups and Venture Capital

Added:

```text
early-stage fund
funding market
```

Removed:

```text
startup
```

## New Domain

Added:

```text
Financial Markets
```

---

# Phase 4A Test Validation

Targeted configuration tests:

```text
20 passed
```

after the source replacement.

Domain configuration validation after Financial Markets activation:

```text
5 passed
```

Full suite:

```text
110 passed
```

No application module required modification.

The implementation remained configuration-first.

---

# Phase 4A Real-Run Validation — 17 August 2026

A real local pipeline run after the source/taxonomy changes produced:

```text
7 active sources
7 successful
0 failed

1281 valid collected records
32 inside collection window
30 unique records
26 unclassified
4 displayed
status: success
```

The report was manually inspected.

Displayed stories included:

- a major US/South Korea/Iran geopolitical story;
- a Tech.eu AI + Series A story;
- a BBC Business AI deployment/governance story;
- an ECB euro-area defence-spending speech.

The 26 unclassified records were also reviewed.

The inspection established:

> **a high unclassified count is not automatically a classification failure.**

Most excluded records were correctly low-value or outside the product's intended intelligence scope.

Remaining misses should be corrected only when they represent strategically important lost information.

---

# Current Phase 4 Source Registry

Current validated active sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Tech.eu.

Current working strategic view:

| Source | Current Position |
|---|---|
| BBC News World | Retain |
| BBC News Business | Retain temporarily; likely replacement if stronger business coverage validates |
| ECB | Core |
| European Commission | Retain, selectively |
| Istat | Core |
| OpenAI News | Retain as primary AI source, not complete AI coverage |
| Tech.eu | Active Sifted replacement; monitor production quality |

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
8. Financial Markets.

Not yet implemented:

9. Italy;
10. Milan and Bocconi Ecosystem.

## Italy

Strategic decision:

> **Approved for implementation when suitable source coverage and classification evidence are validated.**

Priority candidates include:

- Il Sole 24 Ore;
- Bank of Italy;
- existing Istat coverage.

## Milan and Bocconi

Strategic decision:

> **Validated product requirement.**

It is no longer an optional candidate.

Implementation remains pending because the correct source architecture still needs validation.

The desired role is:

> **Professional Ecosystem Intelligence**

rather than generic local news.

Priority candidates:

1. B4i;
2. Bocconi Career Services;
3. Bocconi News & Events.

Possible later complements:

- Italian Tech Alliance;
- Fintech District;
- selected Comune di Milano sources.

---

# Premium Bocconi Source Exception

The source audit now distinguishes:

```text
automation suitability
```

from:

```text
reader accessibility
```

Some premium publications may be useful production sources even when their public metadata cannot support a rich automated summary.

A narrow exception is permitted when:

- the publication has unusually high strategic value;
- the user can legitimately access the linked article through Bocconi;
- a legitimate public/automation-compatible discovery endpoint exists;
- the pipeline does not authenticate as the user;
- premium article bodies are not automatically retrieved;
- thinner report context is an accepted source-specific trade-off.

Current strongest strategic candidates:

```text
Financial Times
Il Sole 24 Ore
```

The exception does not automatically approve either source technically.

---

# Current Milestone

## Milestone 4 — Correct and Expand the Source and Domain Universe

### Objective

Improve the information inputs before adding richer report logic.

The infrastructure is no longer the main problem.

The active problem is:

- weak or inaccessible sources;
- missing high-value domains;
- classification recall/precision;
- uneven metadata richness;
- source concentration;
- information gaps.

---

## Milestone 4 Completed Work

- [x] Career Agent source/domain strategy completed.
- [x] Bocconi access model incorporated into source policy.
- [x] Premium Bocconi Exception defined.
- [x] Sifted accessibility problem investigated.
- [x] Sifted metadata quality tested.
- [x] Tech.eu investigated as replacement.
- [x] Tech.eu collected through real project collector.
- [x] Tech.eu normalisation validated.
- [x] Tech.eu metadata richness inspected.
- [x] Tech.eu vs Sifted direct comparison completed.
- [x] Sifted replacement decision made.
- [x] Tech.eu configured without a blanket source default.
- [x] Evidence-backed keyword additions simulated.
- [x] Three-day classification regression completed.
- [x] Generic `startup` keyword removed after false-positive evidence.
- [x] Financial Markets strategically approved.
- [x] Financial Markets implemented conservatively.
- [x] Targeted configuration tests passed.
- [x] Full 110-test suite passed.
- [x] Real 17 August 2026 collection completed successfully.
- [x] Generated 17 August report manually inspected.
- [x] No paid API introduced.
- [x] No private credential introduced.
- [x] No premium-content ingestion introduced.
- [x] Zero recurring monetary cost preserved.

---

## Milestone 4 Remaining Work

- [ ] Commit the validated Tech.eu / Financial Markets checkpoint after canonical documentation reconciliation.
- [ ] Audit Financial Times technically.
- [ ] Audit Il Sole 24 Ore technically.
- [ ] Audit Bank of Italy technically.
- [ ] Audit Reuters if a clean zero-cost structured endpoint remains plausible.
- [ ] Decide whether stronger business coverage justifies removing BBC Business.
- [ ] Continue monitoring Tech.eu production value and noise.
- [ ] Design and validate Italy classification/source coverage.
- [ ] Technically audit B4i.
- [ ] Technically audit Bocconi Career Services.
- [ ] Technically audit Bocconi News & Events.
- [ ] Implement Milan/Bocconi macroarea only after source architecture is validated.
- [ ] Reassess remaining classification misses from real reports.
- [ ] Confirm the smallest useful final Phase 4 source universe.

---

# Phase 4 Completion Criteria

Phase 4 is complete when:

- every active source has a deliberate strategic and technical role;
- weak sources have explicit retain/replace/remove decisions;
- Sifted replacement is fully committed and production-observed;
- Financial Markets is stable in production;
- Italy has a validated implementation decision;
- Milan/Bocconi has a validated low-maintenance implementation;
- high-priority premium candidates have explicit technical decisions;
- the smallest useful source universe has been selected;
- source/default/keyword changes have regression evidence;
- full automated tests pass;
- real collection remains reliable;
- reports are manually inspected;
- source concentration and accessibility are acceptable;
- no credentials or restricted article bodies are introduced;
- zero recurring monetary cost remains intact.

Phase 4 does **not** require every possible strategically useful source to be implemented.

It requires the information universe to be good enough that richer-report design becomes the next highest-value bottleneck.

## Status

**Active — first validated source/taxonomy correction completed locally; checkpoint pending documentation reconciliation and commit.**

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

The current maximum description length is:

```text
300 characters
```

This is insufficient for some sources and stories.

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

**Not started. Validated requirement, intentionally deferred behind Phase 4.**

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

## 1. Source Metadata Quality Is a Product Requirement

### Evidence

Sifted and Tech.eu were both technically compatible.

However:

```text
Sifted  → 0/24 descriptions
Tech.eu → 20/20 descriptions
```

### Consequence

Feed richness can determine source replacement even when both sources collect successfully.

**Owner:** `03 Information Taxonomy and Source Policy.md`.

---

## 2. Reader Accessibility and Automation Eligibility Are Different

A source can be:

```text
technically collectible
but poor for the reader
```

or:

```text
excellent for the reader
but unsuitable for automated ingestion
```

### Consequence

Every source audit must treat the two dimensions separately.

**Owner:** `03 Information Taxonomy and Source Policy.md`.

---

## 3. Bocconi Access Creates a Narrow Premium Exception

Direct Bocconi access can justify a high-value premium publication appearing in the report even if the pipeline cannot create a rich summary.

It does not permit:

- authenticated automated retrieval;
- credential storage;
- paywall bypass;
- premium article-body storage.

### Consequence

FT and Il Sole 24 Ore deserve technical investigation despite potentially thinner public metadata.

**Owner:** `03 Information Taxonomy and Source Policy.md`.

---

## 4. Classification Rate Is Not a Product KPI

The 17 August run produced:

```text
30 unique records
26 unclassified
4 displayed
```

Manual inspection showed that most unclassified records were correctly excluded.

### Consequence

Do not optimize for a higher classified percentage.

Optimize for:

- valuable stories included;
- low-value stories excluded;
- correct domain assignment;
- useful ranking.

---

## 5. Broad Keywords Can Damage Ranking

Because relevance score contains:

```text
+ 2 per domain
+ 1 per matched keyword
```

careless keyword expansion can inflate relevance.

### Evidence

Testing morphological acquisition variants showed that multiple related keywords could match the same story.

### Consequence

Keyword expansion must remain simulation-driven.

---

## 6. Financial Markets Needs Causal, Not Trading, Coverage

The domain is now implemented.

Its objective is to capture:

- repricing mechanisms;
- rates;
- bonds;
- credit;
- liquidity;
- capital markets;
- financial stability;
- meaningful market reactions.

It should not become:

- daily index recaps;
- trading tips;
- technical analysis;
- speculative price commentary.

---

## 7. Milan/Bocconi Is a Fixed Requirement

Milan/Bocconi is no longer an optional domain candidate.

The remaining question is implementation, not product validity.

### Consequence

Phase 4 must eventually establish a safe, structured and selective source architecture.

---

## 8. Report Context Remains Too Thin

The richer-context need remains validated.

It should not yet distract from source/domain correction.

**Owner:** `01 Product Requirements.md`.

**Implementation phase:** Phase 5 design → Phase 6 implementation.

---

## 9. Scheduler Latency Remains an Operational Limitation

GitHub scheduled execution may start materially late.

The rolling 24-hour report window remains anchored to actual execution.

### Consequence

Continue observing.

Do not redesign the reporting window without stronger repeated evidence.

---

# Current Source Audit Queue

Use this order unless new evidence changes priorities.

## 1. Financial Times

Why first:

- highest strategic cross-domain value;
- direct Bocconi reader access;
- potential coverage of markets, companies, macro, geopolitics and technology;
- could reduce the future need for BBC Business and other overlapping publications.

Audit must establish:

- legitimate public structured discovery endpoint;
- metadata richness;
- timestamps;
- automation suitability;
- terms/licence compatibility;
- collector compatibility;
- likely report volume;
- overlap;
- value of Premium Bocconi Exception.

## 2. Il Sole 24 Ore

Potential role:

- Italy;
- Financial Markets;
- Italian companies;
- policy/regulation.

Could anchor the future Italy domain.

## 3. Bank of Italy

Potential role:

- Italian banking;
- financial stability;
- macroeconomic evidence;
- markets.

Likely primary-source complement.

## 4. Reuters

Strategically strong cross-domain candidate.

Do not allow Reuters investigation to block progress if no clean free production endpoint exists.

## 5. Milan/Bocconi Sources

After the core source upgrade:

```text
B4i
→ Bocconi Career Services
→ Bocconi News & Events
```

Then consider narrower complements only if gaps remain.

---

# Current Files in the Phase 4A Checkpoint

Validated implementation changes:

```text
config/sources.yaml
config/domains.yaml
tests/test_feed_fixture.py
tests/test_domain_config.py
```

Canonical documentation reconciliation includes:

```text
docs/project/03 Information Taxonomy and Source Policy.md
docs/project/04 Development Roadmap and Status.md
```

Additional canonical documents should be updated only where their owned information became stale.

Generated 17 August validation artifacts:

```text
data/processed/2026/08/2026-08-17.jsonl
data/runs/2026/08/2026-08-17.json
reports/daily/2026/08/2026-08-17.md
```

Unrelated local file:

```text
.obsidian/workspace.json
```

must remain outside the Phase 4 commit.

Historical 14 August outputs that were accidentally overwritten during local testing were restored to their committed state.

---

# Current Validation Record

## Configuration / Regression

- Tech.eu direct collection probe: passed.
- Tech.eu normalisation: 20/20 passed.
- Tech.eu description availability: 20/20.
- Sifted comparison description availability: 0/24.
- Tech.eu no-default simulation completed.
- Candidate keyword simulation completed.
- 114-record regression completed.
- Financial Markets simulation completed.
- `startup` removal simulation completed.
- `tariffs` recovery validated.

## Automated Tests

```text
targeted source/domain tests → passed
domain config tests          → 5 passed
full suite                   → 110 passed
```

## Real Pipeline

17 August 2026:

```text
7 active sources
7 successful
1281 valid records
32 window-eligible
30 unique
26 unclassified
4 displayed
status: success
```

## Manual Product Review

Completed.

Result:

> **Selective but acceptable checkpoint.**

No evidence justified reverting Tech.eu or forcing broad classification expansion before commit.

---

# Immediate Next Actions

## Current Action

Finish the documentation reconciliation for the validated Phase 4A checkpoint.

Then:

1. inspect final working-tree diff;
2. confirm only intended files are staged;
3. exclude `.obsidian/workspace.json`;
4. run final tests if documentation edits do not touch application/config logic;
5. commit the checkpoint;
6. push;
7. begin Financial Times technical audit.

---

# Next Highest-ROI Step

After the Phase 4A checkpoint is committed:

> **Technically audit Financial Times under the source scorecard and Premium Bocconi Exception.**

Do not simultaneously:

- add FT;
- add Il Sole;
- remove BBC Business;
- implement Italy;
- implement Milan/Bocconi;
- redesign report summaries.

Proceed one controlled source decision at a time.

---

# Stop Condition Before Phase 5

Do not begin richer-report implementation until Phase 4 has produced a sufficiently strong source/domain universe.

The switch to Phase 5 should occur when further source/domain work has lower expected value than improving context within already-selected stories.

That decision should be based on repeated report evidence, not a preselected date or source count.

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
→ correct sources/domains from evidence
```

Current Phase 4 checkpoint:

```text
Sifted replaced by Tech.eu
Financial Markets implemented
keyword precision/recall improved conservatively
110 tests passing
17 August real run successful
documentation reconciliation in progress
```

Current immediate priority:

> **Commit this stable checkpoint, then audit Financial Times.**

---

# Changelog

## 2026-08-17 — Phase 4A Tech.eu Replacement and Financial Markets Activation

- Incorporated the completed Career Agent strategic source/domain audit into the development sequence.
- Formalised the narrow Premium Bocconi Exception while preserving the prohibition on authenticated automated ingestion.
- Directly compared Tech.eu and Sifted through the real collector.
- Observed 20/20 Tech.eu descriptions versus 0/24 Sifted descriptions.
- Approved Tech.eu as the replacement for Sifted.
- Removed Sifted from the active source registry.
- Added Tech.eu as Tier 2, Europe, with no source-default domain.
- Tested Tech.eu with and without a Startups/VC source default.
- Rejected the blanket Startups/VC default because Tech.eu is a heterogeneous technology/startup/business source.
- Added `acquired` to Companies and Corporate Strategy after a real M&A recall gap.
- Added `early-stage fund` and `funding market` to Startups/VC after real Tech.eu evidence.
- Removed generic `startup` because it promoted weak startup profiles too easily.
- Added `tariffs` to Global Politics and Geopolitics after a relevant BBC trade/geopolitics miss.
- Activated Financial Markets as the eighth domain with a conservative first keyword set.
- Validated candidate taxonomy changes against 114 stored production records.
- Confirmed all observed changes were interpretable.
- Confirmed 110/110 automated tests passed.
- Completed a real 17 August 2026 pipeline run with 7/7 sources successful.
- Manually inspected the generated report and all 30 unique records.
- Recorded that classification rate alone is not a useful product-quality KPI.
- Confirmed that most 17 August unclassified records were correctly excluded.
- Restored accidentally overwritten 14 August production artifacts before preparing the checkpoint.
- Preserved zero recurring cost, deterministic processing, credential safety and public-repository constraints.
- Set Financial Times technical audit as the next source-level task after checkpoint commit.

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