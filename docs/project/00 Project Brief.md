# Daily Intelligence System — Project Brief

> **Purpose**
>
> This document defines why the Daily Intelligence System exists, what problem it solves, what the project is intended to achieve, and what is deliberately outside its scope.
>
> It is the strategic reference for product, architecture and implementation decisions.
>
> It should remain relatively stable and should not become a detailed implementation-status document.
>
> ---
>
> **Primary Question**
>
> > *What problem is this project solving, under which constraints, and what would make it successful?*
>
> ---
>
> **Update Frequency**
>
> Update only when the project’s purpose, scope, constraints or success criteria materially change.

---

# Project Summary

The Daily Intelligence System is a zero-cost, highly automated information workflow designed to improve awareness of important developments across:

- global politics and geopolitics;
- economics and macroeconomics;
- financial markets;
- companies and corporate strategy;
- artificial intelligence;
- technology and software;
- startups and venture capital;
- Europe and the European Union;
- Italy;
- Milan and the Bocconi ecosystem.

The system is intended to reduce the gap between the large amount of information published every day and the limited amount of time available to identify what genuinely matters.

The project does not aim to collect every article or reproduce the work of a professional newsroom.

Its objective is to create a reliable process for:

- collecting relevant public information;
- reducing duplication and noise;
- organising stories by domain;
- ranking items transparently;
- preserving source links and metadata;
- generating a concise daily report;
- building a historical archive;
- exposing failures clearly;
- supporting deeper interpretation through a separate ChatGPT briefing workflow.

The deterministic local processing core is now implemented and validated.

The next objective is to validate the same system with a deliberately small real-source set before introducing scheduled GitHub automation.

---

# Problem

Important information is distributed across:

- news publications;
- official institutions;
- company announcements;
- research organisations;
- technical blogs;
- startup and venture-capital sources;
- public newsletters and feeds;
- university and local ecosystem channels.

Following these sources manually creates several problems.

## Fragmentation

Relevant information is spread across many websites, feeds and publication formats.

## Information Overload

The volume of daily content is too high to review efficiently without filtering.

## Duplication

The same event may appear through many publications, creating the impression of greater importance while wasting reading time.

## Uneven Source Quality

Primary evidence, high-quality reporting, commentary, promotion and low-quality aggregation are often mixed together.

## Weak Prioritisation

Most news products optimise for broad engagement rather than the specific combination of economics, politics, markets, AI, technology, startups and professional relevance required by this project.

## Limited Historical Memory

Daily reading is easily forgotten when stories, sources and recurring themes are not stored systematically.

## Passive Consumption

Reading more news does not necessarily produce better understanding.

The system should support informed judgment, professional conversations and durable learning rather than encourage endless content consumption.

## Maintenance Friction

A useful information system can become counterproductive if it requires daily copying, manual source checking or constant technical intervention.

The system should therefore automate repetitive collection and organisation while keeping source maintenance occasional and deliberate.

---

# Target User

The initial system is designed for one user.

The user:

- wants structured awareness across economics, politics, finance, AI, technology, startups and business strategy;
- values source quality over content volume;
- has limited time for daily manual research;
- wants to avoid recurring monetary costs;
- is willing to invest time in initial setup and occasional maintenance;
- has working exposure to Python, GitHub, data analysis and software-system concepts;
- wants the system to remain understandable rather than become an unnecessarily complex engineering project.

Multi-user features are outside the MVP.

---

# Strategic Rationale

The project has value across several dimensions.

## Knowledge

It should improve awareness of:

- current economic conditions;
- political and geopolitical developments;
- market movements;
- company and industry changes;
- AI and technology evolution;
- startup and venture-capital activity;
- European and Italian developments.

## Professional Conversations

It should make it easier to participate intelligently in conversations with:

- students;
- professors;
- analysts;
- consultants;
- investors;
- founders;
- technology professionals;
- managers;
- recruiters.

## Career Exploration

It should provide better evidence about:

- which industries are changing;
- which skills are becoming more valuable;
- which companies and institutions deserve attention;
- which career paths appear attractive;
- which topics deserve deeper research.

## Opportunity Detection

It may surface:

- events;
- programmes;
- companies;
- technologies;
- sectors;
- policy developments;
- networking opportunities;
- project ideas.

## Technical Proof of Work

The repository may demonstrate:

- Python development;
- Git and GitHub use;
- deterministic data-pipeline design;
- information architecture;
- testing;
- configuration-driven software;
- workflow automation;
- failure handling;
- transparent ranking and classification;
- technical documentation;
- incremental software development.

The project should preserve optionality across:

- data analytics;
- consulting;
- AI strategy;
- finance;
- venture capital;
- startups;
- economic research;
- technology-oriented roles.

## Systems Thinking

The project is also a practical exercise in building a small business system rather than simply writing isolated scripts.

Its value includes understanding:

- workflows;
- inputs;
- processing rules;
- failure modes;
- output quality;
- automation;
- observability;
- maintenance;
- opportunity cost.

---

# Agreed Operating Model

The complete information workflow contains two independent layers.

## Layer 1 — ChatGPT Intelligence Briefing

A separate ChatGPT workflow may independently research and synthesise current developments.

Its role is to provide:

- interpretation;
- explanations;
- cross-domain connections;
- trend analysis;
- uncertainty;
- career-relevant implications.

This layer remains outside the GitHub repository.

The repository does not depend on automatic access to:

- ChatGPT;
- connectors;
- plugins;
- OpenAI API credits;
- paid model APIs.

## Layer 2 — GitHub Intelligence Pipeline

The GitHub repository owns the deterministic collection and archive system.

Its role is to:

1. collect items from permitted public structured sources;
2. normalise metadata;
3. validate records;
4. enforce the reporting window;
5. reduce obvious duplicates;
6. classify items by domain;
7. calculate transparent relevance scores;
8. store structured records;
9. generate daily Markdown reports;
10. preserve historical outputs;
11. expose source and workflow failures.

The two layers may cover overlapping stories, but they serve different purposes.

The ChatGPT layer provides optional interpretation.

The GitHub layer provides controlled collection, transparency, reproducibility and historical memory.

The core system does not require an automated connection between them.

---

# Project Objectives

The completed system should:

- run automatically every day;
- require negligible daily manual work;
- operate with zero recurring monetary cost;
- avoid recurring consumption of AI or Copilot credits;
- collect from a curated universe of public structured sources;
- preserve direct source links;
- enforce a clear publication window;
- reduce obvious duplication;
- organise content into configurable domains;
- rank stories using understandable deterministic rules;
- generate a concise and readable daily report;
- store enough metadata for later inspection and analysis;
- make degraded and failed runs visible;
- remain simple enough to understand and maintain;
- create a foundation that can be improved without rebuilding the complete system.

---

# Core Constraints

## Cost

- Recurring monetary cost must remain zero.
- Paid APIs, paid news products and paid automation platforms must not be required.
- The project must not depend on OpenAI API credits.
- The project must not depend on recurring GitHub AI or Copilot usage.
- Cloud services that could create accidental charges should be avoided unless explicitly approved later.

## Automation

- Normal production operation should require no daily manual execution.
- Daily copying between GitHub, ChatGPT, email or other systems should not be required.
- Occasional source maintenance and quality review are acceptable.

## Technical Scope

- Ordinary Python and GitHub Actions should handle recurring production work.
- Deterministic logic should be preferred before machine learning or LLM calls.
- RSS, Atom, official APIs and other structured public sources should be preferred before scraping.
- The system should avoid infrastructure without a demonstrated requirement.

## Reliability

- Individual source failures should not necessarily stop the complete workflow.
- Failures should be logged and visible.
- Degraded output should be distinguishable from complete output.
- Processing should be deterministic where inputs are controlled.
- The system should fail clearly rather than silently produce misleading output.

## Information Quality

- Technical success alone is insufficient.
- A report that is noisy, repetitive, misleading or too long should be treated as a product-quality failure even if the pipeline executed correctly.
- Source quality should generally be improved before adding increasingly complex filtering logic.

## Privacy and Copyright

The public repository must not contain:

- credentials;
- private account information;
- personal Career OS documents;
- private emails;
- private newsletter text;
- complete paid articles;
- restricted copyrighted content;
- authentication tokens;
- sensitive private datasets.

---

# MVP Scope

The production MVP must support one complete end-to-end workflow:

```text
Public structured sources
        ↓
Collection
        ↓
Metadata normalisation
        ↓
Validation
        ↓
Publication-window filtering
        ↓
Exact duplicate reduction
        ↓
Domain classification
        ↓
Relevance ranking
        ↓
Structured storage
        ↓
Daily Markdown report
        ↓
Run summary and visible status
        ↓
Automated GitHub execution
        ↓
Automated persistence
```

The MVP should use a limited source universe.

The priority is proof that the complete workflow produces useful output reliably, not maximum coverage.

---

# Current Delivery State

The project has completed the local deterministic vertical slice.

Implemented and validated locally:

- configuration loading;
- controlled RSS/Atom collection;
- structured source-level outcomes;
- record normalisation;
- record validation;
- publication-window filtering;
- exact duplicate reduction;
- deterministic multi-domain classification;
- deterministic relevance scoring;
- JSON Lines persistence;
- Markdown report selection and rendering;
- JSON run summaries;
- degraded-source handling;
- operational report warnings;
- lightweight run-level logging;
- local end-to-end orchestration;
- one-command CLI execution.

The current local command is:

```text
python -m daily_intelligence.cli run
```

At Phase 1 closeout:

> **104 automated tests pass.**

The current controlled configuration intentionally contains:

- one sample source;
- Technology and Software;
- Artificial Intelligence.

This configuration proves system behaviour.

It does not represent the intended final production coverage.

---

# Production Work Still Required

The system should not yet be described as production-complete.

Remaining production MVP work includes:

- select a small credible real-source set;
- validate live RSS/Atom behaviour;
- confirm network timeout and error-handling requirements;
- add minimal network hardening where justified;
- inspect real publication timestamps and metadata quality;
- inspect report usefulness with real information;
- implement GitHub Actions;
- validate manual GitHub workflow execution;
- automate output persistence;
- enable scheduled execution;
- evaluate real reports over time.

Potential quality features such as near-duplicate clustering, entities, geographic classification and content types are not prerequisites unless real usage demonstrates that they solve meaningful problems.

---

# MVP Outputs

The production MVP should produce three main persistent outputs.

## Structured Article Records

Processed records should preserve enough metadata to:

- identify the source;
- inspect original and normalised fields;
- understand classifications;
- understand relevance scores;
- reconstruct report-selection behaviour where practical.

Current storage format:

```text
JSON Lines
```

## Daily Markdown Report

The current report structure already supports:

- report date;
- monitored period;
- generation timestamp;
- run status;
- active source count;
- source success/failure counts;
- collected-item count;
- displayed-item count;
- domain sections;
- ranked headlines;
- source name;
- publication time;
- relevance score;
- secondary domains;
- short feed-provided description;
- direct source link;
- visible warnings for degraded runs.

The report does not fabricate article summaries.

## Run Summary

Each run should create a structured JSON operational summary containing:

- run identifier;
- timestamps;
- run status;
- monitored window;
- source counts;
- item counts;
- warnings.

## Historical Archive

Production daily reports, processed records and run summaries should remain accessible for later review.

## Execution Logs

The system should make it possible to understand:

- whether the workflow completed;
- which sources succeeded or failed;
- how many records were validated;
- how many remained inside the publication window;
- how many duplicates were removed;
- how many items were processed;
- which output paths were written;
- whether the run completed successfully or in degraded state.

---

# Non-Goals

The initial project is not intended to:

- replace professional news analysis;
- provide exhaustive global coverage;
- reproduce complete articles;
- bypass paywalls;
- scrape websites against their terms;
- generate investment, legal or political recommendations;
- predict markets;
- verify every factual claim independently;
- eliminate human judgment;
- create a personalised social-media feed;
- support multiple users;
- build a mobile application;
- build a complex dashboard;
- create a sophisticated public frontend;
- use paid AI summarisation;
- use autonomous agents;
- implement RAG;
- use embeddings or vector databases;
- use machine-learning classification without evidence that deterministic logic is insufficient;
- ingest private newsletters or email during the MVP;
- automatically edit the Career OS;
- automatically transfer GitHub reports into ChatGPT;
- build infrastructure merely because it is technically interesting.

These possibilities should be reconsidered only if later evidence demonstrates a clear workflow need and the core constraints remain satisfied.

---

# Success Criteria

The MVP will be considered successful when the following conditions are satisfied.

## Functional Success

- The system collects items from a small but credible real-source universe.
- Metadata is normalised consistently.
- The publication window is enforced correctly.
- Malformed records are handled visibly.
- Obvious exact duplicates are reduced.
- Items are assigned to useful domains.
- A transparent ranking process is applied.
- A readable Markdown report is generated.
- Structured records and run summaries are stored historically.
- The workflow runs automatically through GitHub Actions.
- Failed sources or workflow problems are visible.

## Cost Success

- Recurring monetary cost remains zero.
- Production runs do not consume GitHub AI or Copilot credits.
- No paid API is required.

## User-Experience Success

- Normal daily manual work is negligible.
- The report can be scanned quickly.
- Source links are easy to access.
- The report is not dominated by duplicates or low-value content.
- The output is concise enough to be used consistently.
- A degraded report is visibly degraded.

## Quality Success

- Important items are not systematically buried by low-value stories.
- Source quality remains transparent.
- Classification is adequate for practical use.
- Ranking logic is understandable.
- The system does not fabricate analytical summaries.
- Missing data and source failures are not hidden.
- Technical sophistication is added only when it improves real report quality.

## Reliability Success

- Individual source failures are isolated where appropriate.
- Critical failures do not create falsely successful output.
- Repeated runs do not create uncontrolled duplication.
- No-news runs behave predictably.
- Network requests cannot hang indefinitely in production.

## Maintainability Success

- A future contributor can understand the repository from its documentation.
- Configuration is separated from application logic where appropriate.
- Sources can be added or disabled without rewriting the pipeline.
- Dependencies remain limited.
- Modules have clear responsibilities.
- The architecture remains proportional to the value created.

---

# Evaluation Period

The production MVP should not be judged only from automated technical tests.

After scheduled automation is stable, the system should be used for an initial evaluation period of approximately two weeks.

During this period, evaluate:

- whether the report is actually opened;
- whether it can be scanned in approximately 10–15 minutes;
- whether important stories are missed;
- whether low-value stories are overrepresented;
- whether exact duplicate reduction is sufficient;
- whether near-duplicate logic is actually needed;
- whether domain classification is useful;
- whether relevant items remain unclassified;
- whether source diversity is adequate;
- whether the ranking formula produces sensible ordering;
- whether source maintenance remains low;
- whether the system improves knowledge or merely increases content volume.

Further quality development should depend on evidence from this evaluation.

---

# Development Philosophy

The project should evolve through evidence rather than speculative architecture.

The preferred development loop is:

```text
Build smallest useful behaviour
→ validate
→ inspect real output
→ identify actual limitation
→ make smallest justified correction
→ validate again
```

A technically possible feature is not automatically a useful feature.

Before adding complexity, ask:

1. What problem does this solve?
2. Has that problem occurred in real use?
3. Can a simpler change solve it?
4. What maintenance does it add?
5. What new failure modes does it introduce?
6. How will success be measured?

This applies especially to:

- near-duplicate clustering;
- entity extraction;
- geography;
- content types;
- advanced ranking;
- source-health systems;
- dashboards;
- AI integration.

---

# Risks

## Overengineering

The project may become focused on architecture rather than useful output.

**Response:** build and evaluate the smallest complete workflow before adding secondary components.

## Excessive Source Volume

Adding too many sources may increase noise and failure rates.

**Response:** begin with a small real-source set and expand only when coverage gaps are demonstrated.

## Weak Ranking

Simple deterministic scoring may fail to reflect practical importance.

**Response:** keep scoring transparent, review real outputs and modify only observed weaknesses.

## Poor Duplicate Detection

Different headlines may describe the same event.

**Response:** exact URL/title deduplication is already implemented. Add near-duplicate logic only if real reports show material remaining repetition.

## Source Instability

Feeds may change, fail or disappear.

**Response:** isolate source failures, expose run health and remove disproportionately expensive sources.

## Missing or Weak Timestamps

Some useful feeds may provide poor publication metadata.

**Response:** current policy excludes missing publication timestamps from the reporting window. Reconsider only if real-source evidence shows the rule creates material coverage loss.

## Public-Repository Exposure

Generated content may accidentally include restricted or private material.

**Response:** use only approved public structured sources and maintain explicit repository boundaries.

## Passive Consumption

The system may increase reading without improving understanding.

**Response:** keep reports concise and preserve the separate optional ChatGPT interpretation layer.

## Maintenance Burden

A complex pipeline may require more effort than the value it provides.

**Response:** prefer simple components, minimal dependencies and occasional controlled maintenance.

## Misleading Success

A technically completed run may hide failed sources.

**Response:** keep run status, report warnings, structured summaries and logs aligned.

---

# Long-Term Possibilities

The following may be considered after the production MVP has been validated:

- broader source coverage;
- conservative near-duplicate clustering;
- multi-source story grouping;
- tracked companies and institutions;
- geographic classification;
- content-type classification;
- source-health history;
- weekly archive analytics;
- trend detection;
- GitHub Issue delivery;
- GitHub Pages;
- selected public-newsletter feeds;
- improved Milan and Bocconi opportunity monitoring.

These are possibilities, not commitments.

Each should be evaluated against:

- demonstrated user need;
- zero recurring monetary cost;
- reliability;
- daily manual work;
- information quality;
- maintainability;
- transparency;
- privacy;
- opportunity cost.

---

# Public Repository Boundary

This repository is intended to remain public and may function as proof of work.

It may contain:

- public project documentation;
- source code;
- public-source configuration;
- structured permitted metadata;
- generated headlines and links;
- deterministic classifications and scores;
- run summaries;
- tests;
- controlled fixtures;
- GitHub Actions workflows;
- public-safe generated reports.

It must not contain:

- private Career OS sources;
- proprietary internship data;
- private email;
- private newsletter text;
- credentials;
- tokens;
- restricted copyrighted material.

Private contextual materials may inform development reasoning but must remain outside the public repository.

---

# Current Project Status

**Current development state:** Phase 1 local vertical slice complete.

**Validated locally:**

- deterministic processing pipeline;
- one-command execution;
- publication-window enforcement;
- exact deduplication;
- classification;
- ranking;
- structured storage;
- Markdown reporting;
- run summaries;
- degraded-source handling;
- logging;
- 104 automated tests.

**Not yet production-complete:**

- real-source universe;
- network production readiness;
- GitHub Actions;
- automated repository persistence;
- scheduled daily execution;
- production-use evaluation.

**Current milestone:**

> Validate a minimal real-source run before automation.

The detailed implementation status and development sequence belong in `04 Development Roadmap and Status.md`.

---

# Decision Rule

Every future project decision should answer:

> Does this change materially improve reliability, information quality or user value without violating the constraints on cost, manual work, maintainability and scope?

If the answer is unclear, the change should be deferred until evidence is available.

---

# Changelog

## 2026-08-11 — Phase 1 Project Brief Reconciliation

- Updated the brief from project-definition status to the validated Phase 1 delivery state.
- Preserved the original project purpose, target user, strategic rationale and hybrid operating model.
- Added publication-window enforcement and operational visibility to the core workflow.
- Recorded the completed deterministic local vertical slice.
- Recorded 104 passing automated tests at Phase 1 closeout.
- Distinguished the controlled two-domain/sample-source implementation from the intended broader information scope.
- Clarified the remaining production MVP work: real-source validation, network readiness, GitHub Actions, automated persistence and scheduled execution.
- Reframed advanced quality features as evidence-driven possibilities rather than automatic prerequisites.
- Reinforced the workflow-first, minimal-complexity development philosophy.

## Initial Project Brief Baseline

- Defined the Daily Intelligence System problem and strategic rationale.
- Defined the two-layer ChatGPT and GitHub operating model.
- Established zero recurring cost and negligible daily manual work as hard constraints.
- Defined MVP scope, outputs, non-goals, risks and success criteria.