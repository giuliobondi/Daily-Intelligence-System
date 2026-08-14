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

The system is intended to reduce the gap between the large amount of information published every day and the limited amount of time available to identify and understand what genuinely matters.

The project does not aim to collect every article, reproduce the work of a professional newsroom or mirror complete publisher content.

Its objective is to create a reliable process for:

- collecting relevant public information;
- reducing duplication and noise;
- organising stories by domain;
- ranking items transparently;
- preserving source links and metadata;
- providing enough context to understand important developments before deeper reading;
- generating a concise daily report;
- building a historical archive;
- exposing failures clearly;
- supporting deeper interpretation through a separate ChatGPT workflow.

The deterministic collection-to-report pipeline is implemented and production-automated through GitHub Actions.

The current strategic priority is no longer basic automation.

The project is now moving from:

```text
Can the system run reliably every day?
```

to:

```text
Does the system collect the right information and present enough useful context to make the daily report genuinely valuable?
```

The immediate next objective is to correct and expand the source and domain universe, beginning with weaknesses exposed by real production use.

After the information-source layer is improved, the next major design objective is to define and implement a richer report experience that provides sufficient lawful context without requiring immediate click-through for basic understanding.

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

---

## Information Overload

The volume of daily content is too high to review efficiently without filtering.

---

## Duplication

The same event may appear through many publications, creating the impression of greater importance while wasting reading time.

---

## Uneven Source Quality

Primary evidence, high-quality reporting, commentary, promotion and low-quality aggregation are often mixed together.

---

## Uneven Source Accessibility

A technically valid source may link to content that is difficult or impossible for the user to access.

Real production use has demonstrated that:

```text
technically collectable
```

does not necessarily mean:

```text
useful in the daily reading workflow
```

A source can therefore be operationally compatible while still being a poor product source because:

- linked articles require an additional subscription;
- public feed metadata is too thin;
- the report cannot provide enough context without the unavailable article;
- a more accessible alternative could provide equivalent information.

Source accessibility and metadata richness must therefore be considered alongside credibility and technical compatibility.

---

## Weak Prioritisation

Most news products optimise for broad engagement rather than the specific combination of economics, politics, markets, AI, technology, startups and professional relevance required by this project.

---

## Thin Context

A headline, relevance score and short feed description may be insufficient to understand why a development matters.

The system should reduce unnecessary click-through.

The desired user experience is:

```text
daily report
→ understand the core development
→ decide whether deeper reading is worthwhile
→ open selected source
```

rather than:

```text
daily report
→ identify headline
→ open article
→ only then understand what happened
```

The report should not replace original sources.

It should provide enough initial context that original sources become deeper-reading destinations rather than mandatory first steps.

---

## Limited Historical Memory

Daily reading is easily forgotten when stories, sources and recurring themes are not stored systematically.

---

## Passive Consumption

Reading more news does not necessarily produce better understanding.

The system should support informed judgment, professional conversations and durable learning rather than encourage endless content consumption.

---

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
- is willing to invest time in initial setup, source review and occasional maintenance;
- has working exposure to Python, GitHub, data analysis and software-system concepts;
- wants the system to remain understandable rather than become an unnecessarily complex engineering project;
- has legitimate institutional access through Bocconi to many high-quality publications and research resources.

Bocconi access materially expands the user’s personal reading and research options.

It does not automatically expand the set of sources that may be ingested programmatically.

The system must distinguish:

```text
what the user can legitimately read
```

from:

```text
what the automated pipeline may legitimately retrieve and store
```

Multi-user features remain outside the project scope.

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

---

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

---

## Career Exploration

It should provide better evidence about:

- which industries are changing;
- which skills are becoming more valuable;
- which companies and institutions deserve attention;
- which career paths appear attractive;
- which topics deserve deeper research.

---

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

---

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
- source-quality reasoning;
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

---

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
- source governance;
- opportunity cost.

---

# Agreed Operating Model

The complete information workflow contains two independent layers.

---

## Layer 1 — ChatGPT Intelligence and Development Layer

A separate ChatGPT workflow may independently research, interpret and synthesise developments.

Its role may include:

- interpretation;
- explanations;
- cross-domain connections;
- trend analysis;
- uncertainty;
- career-relevant implications;
- source/domain strategy;
- development reasoning.

This layer remains outside the production dependency chain.

The repository does not depend on automatic access to:

- ChatGPT;
- connectors;
- plugins;
- OpenAI API credits;
- paid model APIs.

The project may use ChatGPT manually as a development and reasoning tool without making it a production infrastructure dependency.

---

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
11. expose source and workflow failures;
12. run automatically through GitHub Actions;
13. persist production outputs automatically.

The two layers may cover overlapping stories, but they serve different purposes.

The ChatGPT layer provides optional reasoning and interpretation.

The GitHub layer provides controlled collection, transparency, reproducibility and historical memory.

The core production system does not require an automated connection between them.

---

# Information Access Model

The project should distinguish three information-access layers.

## Layer A — Automated Public Sources

These are eligible for continuous production ingestion when the required usage is compatible with the source and its access mechanism.

Examples include:

- public RSS feeds;
- public Atom feeds;
- official public APIs;
- government and institutional feeds;
- company public feeds;
- public structured metadata;
- other explicitly permitted public endpoints.

These sources drive the automated production system.

---

## Layer B — Personal Premium Reading

The user has legitimate institutional access through Bocconi to high-quality publications including several major newspapers and research publications.

These can be used manually when deeper reading is useful.

Examples may include:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore;
- Foreign Affairs;
- Harvard Business Review;
- other Bocconi-accessible publications.

Personal institutional access can increase the usefulness of a source as a follow-up destination.

It must not be interpreted as permission for authenticated automated ingestion.

---

## Layer C — Research and Database Resources

The user also has access to professional and academic research tools.

Examples include:

- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- S&P Capital IQ Pro;
- Aida.

These are valuable for targeted investigation.

They are not part of the normal automated production pipeline unless a specific public or explicitly licensed automation mechanism is separately identified.

---

# Project Objectives

The completed system should:

- run automatically every day;
- require negligible daily manual work;
- operate with zero recurring monetary cost;
- avoid recurring consumption of AI or Copilot credits;
- collect from a curated universe of permitted structured sources;
- preserve direct source links;
- enforce a clear publication window;
- reduce obvious duplication;
- organise content into configurable domains;
- rank stories using understandable deterministic rules;
- generate a concise and readable daily report;
- provide enough lawful context to understand selected developments before immediate click-through;
- store enough metadata for later inspection and analysis;
- preserve historical daily outputs;
- make degraded and failed runs visible;
- remain simple enough to understand and maintain;
- distinguish technical success from information-product success;
- create a foundation that can be improved without rebuilding the complete system.

---

# Core Constraints

## Cost

- Recurring monetary cost must remain zero.
- Paid APIs, paid news services and paid automation platforms must not be required by the core system.
- The project must not depend on OpenAI API credits.
- The project must not depend on recurring GitHub AI or Copilot usage.
- Cloud services that could create accidental charges should be avoided unless explicitly approved later.

Personal access to publications funded through Bocconi does not violate this constraint because it does not create an additional project-level recurring expense.

However, such access must not become a hidden production dependency.

---

## Automation

- Normal production operation should require no daily manual execution.
- Daily copying between GitHub, ChatGPT, email or other systems should not be required.
- Occasional source maintenance and quality review are acceptable.
- Manual workflow execution may remain available for testing and recovery.

---

## Technical Scope

- Ordinary Python and GitHub Actions should handle recurring production work.
- Deterministic logic should be preferred before machine learning or LLM calls.
- RSS, Atom, official APIs and other structured public sources should be preferred before scraping.
- The system should avoid infrastructure without a demonstrated requirement.
- Optional features must not become dependencies of the core workflow without evidence.

---

## Reliability

- Individual source failures should not necessarily stop the complete workflow.
- Failures should be logged and visible.
- Degraded output should be distinguishable from complete output.
- Critical failures should not produce falsely successful output.
- Processing should be deterministic where inputs are controlled.
- The system should fail clearly rather than silently produce misleading output.
- External scheduling delay should not be confused with pipeline failure.

---

## Information Quality

- Technical success alone is insufficient.
- A report that is noisy, repetitive, misleading, inaccessible, overly concentrated, too sparse or too thin to understand should be treated as a product-quality problem even if the pipeline executed correctly.
- Source quality should generally be improved before adding increasingly complex filtering logic.
- A technically compatible source is not automatically a useful production source.
- Source accessibility and metadata richness should be considered when evaluating production value.
- The system should prefer a smaller strong source universe over source accumulation.
- The report should provide enough initial context to support understanding without attempting to reproduce complete articles.

---

## Privacy, Credentials and Copyright

The public repository must not contain:

- credentials;
- Bocconi credentials;
- private account information;
- personal Career OS documents;
- private emails;
- private newsletter text;
- complete paid articles;
- authenticated premium article bodies;
- licensed database full text;
- restricted copyrighted content;
- authentication tokens;
- sensitive private datasets.

The production system must not:

- bypass paywalls;
- automate OpenAthens or other institutional authentication merely because credentials are available;
- scrape authenticated premium publications without explicit permission;
- bulk-download licensed database content;
- republish substantial restricted content.

When uncertain:

> preserve less source content and retain provenance and a direct source link.

---

# Core Production Scope

The core production workflow is:

```text
Permitted structured sources
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
GitHub Actions execution
        ↓
Output validation
        ↓
Automated repository persistence
```

This complete loop is now implemented.

The next phases should improve the quality of:

```text
sources
→ classification inputs
→ report context
→ user experience
```

without destabilising the validated production foundation.

---

# Current Production Baseline

The current production system contains seven active public RSS sources:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News;
- Istat Press Releases;
- OpenAI News;
- Sifted.

The current implemented taxonomy contains seven active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

Three target domains remain candidates for expansion:

- Financial Markets;
- Italy;
- Milan and the Bocconi ecosystem.

The seven-source universe should now be treated as:

> **a validated production baseline, not the final information universe.**

Production use has provided enough evidence to justify controlled source and domain correction.

---

# Current Production Capabilities

The current system has validated:

- real public-source collection;
- bounded network requests;
- source-level failure isolation;
- normalisation;
- validation;
- publication-window filtering;
- exact deduplication;
- deterministic classification;
- deterministic ranking;
- JSON Lines persistence;
- Markdown report generation;
- JSON run summaries;
- visible operational warnings;
- one-command local execution;
- 110 automated tests;
- GitHub Actions execution;
- manual workflow dispatch;
- scheduled execution;
- automated output validation;
- automated repository persistence;
- no-change commit protection;
- critical-failure behaviour;
- degraded-source publication;
- concurrency protection;
- historical repository-native reports.

The production automation baseline is therefore complete.

Detailed implementation evidence and chronology belong in:

```text
04 Development Roadmap and Status.md
```

---

# Current Product-Quality Findings

Real production use has exposed several issues that now justify the next development phases.

## Source Accessibility

At least one production-selected Sifted article required Sifted Pro access.

This demonstrated that:

```text
valid RSS source
≠
automatically useful reading source
```

Sifted should therefore be reviewed rather than assumed to remain permanently in the production registry.

The correct response is not to bypass the paywall.

The correct response is to evaluate:

- public metadata richness;
- unique source value;
- frequency of restricted links;
- legitimate user accessibility;
- alternative sources.

---

## Report Context

The current report often provides:

- headline;
- source;
- timestamp;
- relevance score;
- secondary domains;
- short feed description where available;
- source link.

This is useful for prioritisation but can be insufficient for understanding.

A new validated strategic requirement is:

> **The report should provide enough lawful context for the user to understand the core development without requiring immediate click-through.**

The exact implementation method remains deliberately undecided.

---

## Source and Domain Coverage

The current seven-source universe was selected to validate the system.

It was not designed to be the final optimal information universe.

The next development action is therefore to:

- review current sources;
- correct weak sources;
- identify missing information domains;
- expand sources only where justified;
- reconsider Financial Markets, Italy and Milan/Bocconi coverage.

The Career Agent may help define strategic source and domain priorities.

This Development project should evaluate candidate sources for technical and policy suitability before production integration.

---

## Report Concentration and Sparsity

A technically successful production run may still produce a short or concentrated report.

This reinforces the principle:

> technical execution and product quality are separate dimensions.

The response should begin with source and coverage review rather than automatic quotas or complex balancing logic.

---

## Scheduling Latency

GitHub scheduled workflows have been observed to start materially later than the configured time.

The production schedule has therefore been moved earlier to create delivery buffer.

The current rolling publication window is based on actual execution time.

This means scheduler delay can also shift report composition.

A fixed reporting cutoff is now a legitimate future design question.

It should not be implemented without additional evidence.

---

# MVP Outputs

The production system creates three main persistent output types.

## Structured Article Records

Processed records preserve enough metadata to:

- identify the source;
- inspect original and normalised fields;
- understand classifications;
- understand relevance scores;
- reconstruct report-selection behaviour where practical.

Current storage format:

```text
JSON Lines
```

---

## Daily Markdown Report

The current report supports:

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

The current report does not generate richer analytical summaries.

That limitation is now the subject of a future dedicated design phase.

The target is not to reproduce full articles.

The target is to provide enough permitted context for initial understanding.

---

## Run Summary

Each run creates a structured JSON operational summary containing:

- run identifier;
- timestamps;
- run status;
- monitored window;
- source counts;
- item counts;
- warnings.

---

## Historical Archive

Production daily reports, processed records and run summaries remain accessible through the repository.

---

## Execution Logs

The system makes it possible to understand:

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

The project is not intended to:

- replace professional news analysis;
- provide exhaustive global coverage;
- reproduce complete articles;
- bypass paywalls;
- scrape websites against their terms;
- automate authenticated Bocconi premium-content retrieval;
- bulk-ingest Factiva, Nexis, Bloomberg or other licensed databases;
- generate investment, legal or political recommendations;
- predict markets;
- verify every factual claim independently;
- eliminate human judgment;
- create a personalised social-media feed;
- support multiple users;
- build a mobile application;
- build a complex dashboard;
- create a sophisticated public frontend;
- require paid AI summarisation;
- use autonomous agents;
- implement RAG;
- use embeddings or vector databases;
- use machine-learning classification without evidence that deterministic logic is insufficient;
- ingest private newsletters or email into the core system;
- automatically edit the Career OS;
- automatically transfer GitHub reports into ChatGPT;
- build infrastructure merely because it is technically interesting.

These possibilities should be reconsidered only if later evidence demonstrates a clear workflow need and the core constraints remain satisfied.

---

# Success Criteria

The project should be judged on both technical operation and information usefulness.

---

## Functional Success

- The system collects items from a credible structured-source universe.
- Metadata is normalised consistently.
- The publication window is enforced correctly.
- Malformed records are handled visibly.
- Obvious exact duplicates are reduced.
- Items are assigned to useful domains.
- A transparent ranking process is applied.
- A readable Markdown report is generated.
- Structured records and run summaries are stored historically.
- The workflow runs automatically through GitHub Actions.
- Changed outputs are persisted automatically.
- Failed sources and workflow problems are visible.

The current production baseline satisfies these criteria.

---

## Cost Success

- Recurring monetary cost remains zero.
- Production runs do not consume GitHub AI or Copilot credits.
- No paid API is required.
- No commercial automation platform is required.

The current production baseline satisfies these criteria.

---

## User-Experience Success

- Normal daily manual work is negligible.
- The report can be read within a manageable amount of time.
- The user can understand the core development of selected stories without opening every source.
- Source links remain easy to access for deeper reading.
- The report is not dominated by duplicates or low-value content.
- The report is not systematically too sparse or concentrated.
- A degraded report is visibly degraded.
- Inaccessible source links do not routinely make selected items useless.

The current system only partially satisfies these criteria.

This is now a major focus of further development.

---

## Quality Success

- Important items are not systematically buried by low-value stories.
- Source quality remains transparent.
- Source accessibility is considered.
- Public metadata is sufficiently rich for the intended report experience.
- Classification is adequate for practical use.
- Ranking logic is understandable.
- The system does not fabricate unsupported context.
- Missing data and source failures are not hidden.
- The source universe covers the intended strategic domains adequately.
- Technical sophistication is added only when it improves real report quality.

These criteria require further production refinement.

---

## Reliability Success

- Individual source failures are isolated where appropriate.
- Critical failures do not create falsely successful output.
- Degraded runs preserve usable successful-source content.
- Repeated runs do not create uncontrolled duplication.
- No-change runs do not create empty commits.
- No-news runs behave predictably.
- Network requests cannot hang indefinitely.
- Scheduled automation functions without normal daily intervention.

The current production baseline substantially satisfies these criteria.

---

## Maintainability Success

- A future contributor can understand the repository from its documentation.
- Configuration is separated from application logic where appropriate.
- Sources can be added or disabled without rewriting the pipeline.
- Weak sources can be replaced without redesigning the system.
- Dependencies remain limited.
- Modules have clear responsibilities.
- The architecture remains proportional to the value created.
- Source expansion does not create disproportionate recurring maintenance.

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
3. Can a weaker source simply be replaced?
4. Can configuration solve the issue?
5. Can richer existing structured metadata solve it?
6. What maintenance does the change add?
7. What new failure modes does it introduce?
8. Does it preserve zero recurring monetary cost?
9. Does it preserve source transparency?
10. Does it preserve privacy and copyright boundaries?
11. How will success be measured?

This applies especially to:

- richer report generation;
- near-duplicate clustering;
- entity extraction;
- geography;
- content types;
- advanced ranking;
- source-health systems;
- dashboards;
- AI integration.

---

# Current Development Sequence

The current strategic sequence is:

```text
Production automation baseline
COMPLETE

↓

Source and domain correction / expansion
NEXT ACTIVE PRIORITY

↓

Richer-report product design

↓

Smallest justified richer-context implementation

↓

Longitudinal production-quality evaluation

↓

Only then:
optional advanced quality or delivery improvements
```

The current source/domain expansion should be informed by:

- observed production weaknesses;
- missing strategic coverage;
- source accessibility;
- public metadata richness;
- source reliability;
- Bocconi follow-up access;
- source diversity;
- maintenance burden.

The source universe should be improved before the richer-report architecture is finalised because source metadata quality may materially affect which richer-context solution is necessary.

---

# Risks

## Overengineering

The project may become focused on architecture rather than useful output.

**Response:** continue to make evidence-driven incremental changes and stop when the simpler system creates sufficient value.

---

## Excessive Source Volume

Adding too many sources may increase noise, duplication and failure rates.

**Response:** expand only where a source solves a demonstrated information gap or replaces a weaker source.

---

## Prestige Bias

High-profile publications may appear attractive even when they are unsuitable for automated ingestion or expose too little public metadata.

**Response:** separate publisher prestige and personal reading value from automation suitability.

---

## Paywalled Follow-Up

A report item may link to content requiring an additional subscription.

**Response:** evaluate whether enough public context exists, whether the user has legitimate access, and whether a better source should replace it.

Do not bypass the paywall.

---

## Misuse of Institutional Access

Bocconi access may create temptation to automate premium resources.

**Response:** treat Bocconi publications and databases as personal reading/research layers unless a separate public or explicitly automation-permitted endpoint exists.

---

## Weak Report Context

The report may identify relevant stories without explaining them sufficiently.

**Response:** design a richer report carefully before implementation, beginning with public structured metadata rather than automatically introducing full-article extraction or AI summarisation.

---

## Weak Ranking

Simple deterministic scoring may fail to reflect practical importance.

**Response:** keep scoring transparent, review real outputs and modify only observed weaknesses after source-quality problems are addressed.

---

## Poor Duplicate Detection

Different headlines may describe the same event.

**Response:** exact URL/title deduplication remains the current baseline. Add near-duplicate logic only if repeated reports demonstrate material remaining repetition.

---

## Source Instability

Feeds may change, fail or disappear.

**Response:** isolate source failures, expose run health and replace disproportionately expensive or low-value sources.

---

## Missing or Weak Timestamps

Some useful feeds may provide poor publication metadata.

**Response:** current policy excludes missing publication timestamps from the reporting window. Reconsider only if production evidence shows material coverage loss.

---

## Scheduler Latency

GitHub may run scheduled workflows later than configured.

**Response:** schedule earlier than the intended reading time and continue observing whether timing variability materially affects output.

---

## Reporting-Window Drift

The current reporting window depends on actual execution time.

**Response:** evaluate a fixed reporting cutoff if repeated production evidence shows scheduler latency materially changes information coverage.

---

## Public-Repository Exposure

Generated content may accidentally include restricted or private material.

**Response:** use only approved public structured inputs and maintain explicit repository boundaries.

---

## Passive Consumption

The system may increase reading without improving understanding.

**Response:** optimise for concise understanding and selective deeper reading rather than maximum article volume.

---

## Maintenance Burden

A complex pipeline may require more effort than the value it provides.

**Response:** prefer simple components, minimal dependencies, source replacement and occasional controlled maintenance.

---

## Misleading Success

A technically completed run may still produce a poor information product.

**Response:** evaluate technical status and report quality separately.

---

# Long-Term Possibilities

The following may be considered after source quality and richer-report design are validated:

- broader high-quality source coverage;
- Financial Markets implementation;
- Italy implementation;
- Milan and Bocconi opportunity monitoring;
- conservative near-duplicate clustering;
- multi-source story grouping;
- tracked companies and institutions;
- geographic classification;
- content-type classification;
- source-health history;
- weekly archive analytics;
- trend detection;
- stable latest-report links;
- GitHub Issue delivery;
- GitHub Pages;
- selected public-newsletter feeds.

These are possibilities, not commitments.

Each should be evaluated against:

- demonstrated user need;
- zero recurring monetary cost;
- reliability;
- daily manual work;
- information quality;
- maintainability;
- transparency;
- accessibility;
- privacy;
- copyright;
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
- permitted public descriptions or summaries;
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
- Bocconi credentials;
- authentication cookies;
- tokens;
- complete premium articles;
- licensed database full text;
- restricted copyrighted material.

Private contextual materials may inform development reasoning but must remain outside the public repository.

---

# Current Project Status

**Current development state:** production automation baseline complete; information-quality improvement active.

**Implemented and validated:**

- deterministic collection-to-report pipeline;
- seven active public RSS sources;
- seven active domains;
- bounded network collection;
- one-command local execution;
- publication-window enforcement;
- exact deduplication;
- deterministic classification;
- deterministic ranking;
- structured JSONL storage;
- Markdown reporting;
- JSON run summaries;
- degraded-source handling;
- critical-failure handling;
- operational logging;
- 110 automated tests;
- GitHub Actions;
- manual workflow execution;
- scheduled workflow execution;
- automated output validation;
- automated repository persistence;
- no-change commit protection;
- concurrency protection;
- repository-native historical reports.

**Current validated product-quality limitations:**

- the seven-source universe is not necessarily the optimal long-term source set;
- Sifted requires explicit review because selected content may require Sifted Pro;
- source accessibility must be considered alongside technical compatibility;
- public metadata richness varies materially by source;
- report entries can be too thin to understand without click-through;
- some reports may become unusually sparse or source/domain concentrated;
- GitHub schedule latency can shift the current rolling 24-hour reporting window.

**Current priority:**

> Correct and expand the source and domain universe, beginning with the problems exposed by current production use and the Sifted accessibility case.

**Following priority:**

> Conduct a deliberate richer-report product-design phase defining how much context each selected item should provide, which public information may be used, how source restrictions should be handled, and how success will be evaluated before implementation begins.

The detailed phase sequencing and implementation status belong in:

```text
04 Development Roadmap and Status.md
```

---

# Decision Rule

Every future project decision should answer:

> Does this change materially improve reliability, information quality or user value without violating the constraints on cost, manual work, maintainability, accessibility, transparency, privacy, copyright and scope?

If the answer is unclear, the change should be deferred until evidence is available.

---

# Changelog

## 2026-08-14 — Production Automation Closeout and Information-Quality Reorientation

- Reconciled the Project Brief with completed Phase 2 and Phase 3 implementation.
- Recorded the completed deterministic production automation baseline.
- Recorded seven active public sources and seven implemented domains as the current production baseline rather than the final information universe.
- Recorded 110 passing automated tests.
- Recorded GitHub Actions manual and scheduled execution.
- Recorded automated repository persistence and historical production outputs.
- Recorded validated degraded-source and critical-failure behaviour.
- Changed the immediate strategic priority from automation to source/domain correction and expansion.
- Added source accessibility as a strategic information-quality consideration.
- Added public metadata richness as a strategic source-quality consideration.
- Recorded the Sifted Pro access case as evidence requiring source review without pre-deciding removal.
- Added the requirement that reports provide enough lawful context for initial understanding before immediate click-through.
- Preserved original-source links as deeper-reading destinations.
- Added the distinction between automated public sources, Bocconi premium reading access and institutional research/database resources.
- Explicitly preserved the rule that institutional access does not authorise automated authenticated ingestion.
- Recorded scheduler latency and report-window drift as observed limitations requiring continued evaluation.
- Reframed technical success and information-product success as separate dimensions.
- Preserved zero recurring monetary cost, deterministic production, public-repository safety and no-production-AI constraints.

## 2026-08-11 — Phase 1 Project Brief Reconciliation

- Updated the brief from project-definition status to the validated Phase 1 delivery state.
- Preserved the original project purpose, target user, strategic rationale and hybrid operating model.
- Added publication-window enforcement and operational visibility to the core workflow.
- Recorded the completed deterministic local vertical slice.
- Recorded 104 passing automated tests at Phase 1 closeout.
- Distinguished the controlled two-domain/sample-source implementation from the intended broader information scope.
- Clarified the remaining production MVP work at that stage.
- Reframed advanced quality features as evidence-driven possibilities rather than automatic prerequisites.
- Reinforced the workflow-first, minimal-complexity development philosophy.

## Initial Project Brief Baseline

- Defined the Daily Intelligence System problem and strategic rationale.
- Defined the two-layer ChatGPT and GitHub operating model.
- Established zero recurring cost and negligible daily manual work as hard constraints.
- Defined MVP scope, outputs, non-goals, risks and success criteria.