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
> Update only when the project's purpose, scope, constraints or success criteria materially change.

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

- collecting relevant information from permitted structured sources;
- reducing duplication and noise;
- organising stories by domain;
- ranking items transparently;
- preserving source links and provenance;
- providing enough context to understand important developments before deeper reading;
- generating a concise daily report;
- building a historical archive;
- exposing failures clearly;
- surfacing professionally relevant Milan/Bocconi developments and opportunities;
- supporting deeper interpretation through a separate ChatGPT workflow.

The deterministic collection-to-report pipeline is implemented and production-automated through GitHub Actions.

The strategic question is no longer:

```text
Can the system run reliably every day?
```

It is now:

```text
Does the system collect the right information
and present it with enough context
to make the daily report genuinely valuable?
```

The active development focus is therefore information quality:

```text
source quality
→ information-function coverage
→ domain coverage
→ classification quality
→ report context
```

The current source/domain correction phase should be completed before richer-report implementation becomes the main focus.

---

# Problem

Important information is distributed across:

- news publications;
- official institutions;
- company announcements;
- research organisations;
- technical publications;
- startup and venture-capital sources;
- university channels;
- professional and local ecosystem sources.

Following these manually creates several recurring problems.

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

Primary evidence, high-quality reporting, commentary, promotion and low-quality aggregation are mixed together.

---

## Uneven Source Accessibility

A technically valid source may still be a poor product source.

Real production use has demonstrated that:

```text
technically collectable
```

does not necessarily mean:

```text
useful in the daily reading workflow
```

A source may be operationally compatible while still providing:

- inaccessible follow-up links;
- insufficient public metadata;
- excessive noise;
- unnecessary overlap;
- poor value relative to a better alternative;
- persistence or licensing constraints incompatible with the public repository.

Source credibility, accessibility, metadata richness, uniqueness, automation suitability and persistence compatibility must therefore be evaluated together.

---

## Weak Prioritisation

Most information products optimise for broad engagement rather than the specific combination of economics, markets, politics, business, AI, technology, startups and professional relevance required by this project.

---

## Uneven Domain Coverage

A technically operational system can still provide poor intelligence if some domains depend almost entirely on:

- one publisher;
- one institutional source;
- incidental keyword matches;
- a source that performs a different information function from what the user actually needs.

The goal is not equal source counts.

The goal is sufficient coverage of distinct information functions.

For example:

```text
primary institutional evidence
≠
market/company reporting
≠
independent analysis
≠
specialist ecosystem intelligence
```

The project should therefore correct missing information functions before increasing publisher count.

---

## Thin Context

A headline, relevance score and short feed description may not be enough to understand why a development matters.

The intended workflow is:

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

It should provide enough lawful initial context that source articles become deeper-reading destinations rather than mandatory first steps.

---

## Missed Professional Opportunities

Relevant opportunities can be scattered across:

- Bocconi;
- Milan;
- startup ecosystems;
- recruiting channels;
- innovation organisations;
- professional events.

Missing a time-sensitive event, programme or application deadline can have a higher opportunity cost than missing an ordinary news article.

The system should therefore provide selective professional ecosystem intelligence for Milan and Bocconi.

This is a validated product requirement rather than an optional feature.

The first production implementation now exists through Tech Europe Foundation.

The broader requirement remains only partially satisfied.

---

## Limited Historical Memory

Daily reading is easily forgotten when stories, sources and recurring themes are not stored systematically.

---

## Passive Consumption

Reading more information does not necessarily produce better understanding.

The system should support informed judgment, professional conversations, opportunity awareness and durable learning rather than encourage endless content consumption.

---

## Maintenance Friction

A useful information system becomes counterproductive if it requires daily copying, manual source checking or constant technical intervention.

The system should automate repetitive work while keeping source maintenance occasional and deliberate.

---

# Target User

The initial system is designed for one user.

The user:

- wants structured awareness across economics, politics, finance, business strategy, AI, technology and startups;
- wants dedicated European and Italian awareness;
- wants professionally relevant Milan/Bocconi intelligence;
- values source quality over content volume;
- has limited time for daily manual research;
- wants zero recurring project cost;
- accepts occasional source review and maintenance;
- wants the system to remain understandable rather than become an unnecessarily complex engineering project;
- has legitimate institutional access through Bocconi to high-quality publications and research resources.

Bocconi access materially expands personal reading and research options.

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

The project creates value across several dimensions.

## Knowledge

It should improve awareness of:

- economic conditions;
- political and geopolitical developments;
- financial-market mechanisms;
- company and industry changes;
- AI and technology evolution;
- startup and venture-capital activity;
- European developments;
- Italian developments;
- relevant Milan/Bocconi ecosystem developments.

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

It should be capable of surfacing high-value:

- events;
- programmes;
- application deadlines;
- startup opportunities;
- professional communities;
- research opportunities;
- recruiting events;
- networking opportunities;
- project ideas.

The Daily Intelligence System should detect the external opportunity.

Personal decisions, applications, networking follow-up and relationship management belong in the Career OS.

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

Technical sophistication remains secondary to actual usefulness.

---

## Systems Thinking

The project is a practical exercise in building a small information system rather than simply writing isolated scripts.

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
- information-function design;
- opportunity cost.

---

# Agreed Operating Model

The complete information workflow contains two independent layers.

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

ChatGPT may be used manually as a development and reasoning tool without becoming production infrastructure.

---

## Layer 2 — GitHub Intelligence Pipeline

The GitHub repository owns the deterministic collection and archive system.

Its role is to:

1. collect items from permitted structured sources;
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

The ChatGPT layer provides optional reasoning and interpretation.

The GitHub layer provides controlled collection, transparency, reproducibility and historical memory.

The core production system does not require an automated connection between them.

---

# Information Access Model

The project distinguishes three information-access layers.

## Layer A — Automated Public Intelligence

Eligible for continuous production ingestion when the required usage is compatible with the source and its access mechanism.

Examples include:

- public RSS;
- public Atom;
- official free APIs;
- government and institutional feeds;
- company public feeds;
- public structured metadata;
- other explicitly permitted automation-compatible endpoints.

These sources drive production.

---

## Layer B — Personal Premium Reading

The user has legitimate institutional access through Bocconi to high-quality publications including:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore;
- Foreign Affairs;
- Harvard Business Review;
- other Bocconi-accessible publications.

These can be used manually when deeper reading is useful.

Institutional access does not authorise authenticated automated ingestion.

### Premium Bocconi Exception

A narrow source-specific exception may allow an unusually valuable premium publication to appear in production discovery even when public metadata is thinner than ideal, provided that:

- the user can legitimately access the linked article;
- the publication's information value is unusually high;
- a legitimate public or automation-compatible discovery endpoint exists;
- Bocconi credentials are never used by production;
- authenticated premium article bodies are never automatically retrieved;
- persistence remains compatible with the public-repository model;
- thinner report context and manual click-through are deliberately accepted.

This exception changes the acceptable reader workflow.

It does not change the authentication or copyright boundary.

Completed source audits have shown that legitimate personal reading access alone is insufficient to justify production activation.

---

## Layer C — Research and Database Resources

Examples include:

- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- S&P Capital IQ Pro;
- Aida.

These are useful for targeted investigation.

They are not part of the normal automated production pipeline unless a separate explicitly permitted automation mechanism is identified.

---

# Project Objectives

The completed system should:

- run automatically every day;
- require negligible daily manual work;
- operate with zero recurring monetary cost;
- avoid recurring consumption of AI or Copilot credits;
- collect from a curated universe of permitted structured sources;
- prefer the smallest strong source universe rather than maximum source count;
- fill important information-function gaps rather than maximise publisher count;
- preserve source links and provenance;
- enforce a clear publication window;
- reduce obvious duplication;
- organise information into configurable domains;
- support the ten intended strategic macroareas;
- rank stories using understandable deterministic rules;
- generate a concise and readable daily report;
- provide enough lawful context to understand selected developments before immediate click-through;
- surface high-value Milan/Bocconi professional ecosystem intelligence;
- preserve structured historical outputs;
- expose degraded and failed runs clearly;
- remain simple enough to understand and maintain;
- distinguish technical success from information-product success;
- create a foundation that can improve incrementally without rebuilding the system.

---

# Core Constraints

## Cost

- Recurring monetary cost must remain zero.
- Paid APIs, paid news services and paid automation platforms must not be required by the core system.
- The project must not depend on OpenAI API credits.
- The project must not depend on recurring GitHub AI or Copilot usage.
- Cloud services that could create accidental charges should be avoided unless explicitly approved later.

Personal Bocconi access does not violate this constraint because it creates no additional project-level recurring expense.

It must not become a hidden production dependency.

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
- RSS, Atom, official APIs and structured public sources should be preferred before scraping.
- Infrastructure without demonstrated need should not be introduced.
- Optional features must not become dependencies of the core workflow without evidence.
- Existing processing components should be reused before introducing new source-specific architectures.

---

## Reliability

- Individual source failures should not necessarily stop the complete workflow.
- Failures should be logged and visible.
- Degraded output should be distinguishable from complete output.
- Critical failures should not produce falsely successful output.
- Processing should be deterministic where inputs are controlled.
- External scheduling delay should not be confused with pipeline failure.

---

## Information Quality

- Technical success alone is insufficient.
- A report that is noisy, repetitive, misleading, inaccessible, overly concentrated, too sparse or too thin should be treated as a product-quality problem even if the pipeline executed correctly.
- Source quality should generally be improved before adding more complex filtering logic.
- A technically compatible source is not automatically a useful source.
- Source accessibility and metadata richness should be considered alongside credibility and automation suitability.
- Source persistence/licensing compatibility must be evaluated against the public repository model.
- The system should prefer a smaller strong source universe over accumulation.
- The system should prefer differentiated information functions over redundant publishers.
- Unclassified records are preferable to misleading classifications.
- Classification percentage is not itself a success metric.
- The report should provide enough context for initial understanding without reproducing complete articles.

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
- scrape authenticated yoU@B or JobGate;
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

This loop is implemented.

Future work should improve:

```text
sources
→ information-function coverage
→ classification inputs
→ domain coverage
→ report context
→ user experience
```

without destabilising the production foundation.

---

# Target Information Universe

The strategic target consists of ten macroareas:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Financial Markets;
4. Companies and Corporate Strategy;
5. Artificial Intelligence;
6. Technology and Software;
7. Startups and Venture Capital;
8. Europe and the European Union;
9. Italy;
10. Milan and the Bocconi Ecosystem.

Current strategic state:

```text
Financial Markets
→ implemented as a domain
→ dedicated source coverage still weak

Milan and Bocconi Ecosystem
→ implemented through a first production source
→ broader requirement only partially satisfied

Italy
→ approved target macroarea
→ dedicated implementation still pending
```

Detailed implementation state belongs in:

```text
04 Development Roadmap and Status.md
```

---

# Current Information-Quality Direction

Real production use and source research have established several durable lessons.

## Source Quality

A source should be judged on more than technical collectability.

Production suitability depends on:

- strategic value;
- credibility;
- automation suitability;
- metadata richness;
- reader accessibility;
- uniqueness;
- noise;
- maintenance burden;
- persistence compatibility.

The Sifted case demonstrated this principle in practice.

Sifted was replaced by Tech.eu because Tech.eu provided materially better usable public metadata while preserving relevant European startup/technology coverage.

Separate audits of Financial Times, Il Sole 24 Ore and Reuters further demonstrated that:

> **high strategic value does not override production-access and persistence constraints.**

The specific technical evidence and source-decision history belong in:

```text
03 Information Taxonomy and Source Policy.md
04 Development Roadmap and Status.md
```

---

## Information-Function Coverage

The system should not optimise source expansion around publisher count.

A strong information universe may require different roles such as:

```text
primary institutional evidence
market/company reporting
independent interpretation
specialist ecosystem intelligence
professional opportunity discovery
```

The current strategic principle is:

> **Correct information-function gaps before correcting publisher-count gaps.**

This has become particularly important because current weaknesses are concentrated in:

- Financial Markets;
- Companies and Corporate Strategy;
- Italy;
- independent AI/technology coverage.

---

## Selective Classification

The system should not attempt to classify every collected record.

The correct product objective is:

```text
capture important developments
+
exclude low-value noise
```

not:

```text
maximise classified-record percentage
```

The multilingual `AI` / Italian `ai` correction also demonstrated that precise deterministic rules are preferable to broad recall when the latter creates misleading output.

---

## Domain Expansion

Missing strategic domains should be implemented only when:

- the need is validated;
- suitable sources exist;
- classification can be tested;
- the result improves the actual report.

Financial Markets has passed the taxonomy threshold but still requires stronger dedicated source coverage.

Milan/Bocconi has passed the first implementation threshold through Tech Europe Foundation.

Italy remains pending.

---

## Milan/Bocconi

Milan/Bocconi Professional Ecosystem Intelligence is a validated product requirement.

The first production implementation now exists through Tech Europe Foundation.

This proves that useful ecosystem intelligence can enter through the existing article pipeline without requiring:

- private Bocconi access;
- a custom event database;
- a deadline engine;
- source-specific scraping.

Current TEF coverage remains concentrated on:

- startups;
- entrepreneurship;
- deep tech;
- innovation;
- founder/programme activity.

The wider requirement still includes complementary information such as:

- established firms;
- finance/business ecosystem activity;
- recruiting;
- selected professional events;
- time-sensitive opportunities.

Authenticated Career Services systems remain outside production.

---

## Richer Context

The current report can still be too thin.

A validated requirement is:

> **Selected stories should provide enough lawful context for initial understanding without requiring immediate click-through.**

The exact architecture remains deliberately undecided.

It should be designed only after the information-source layer is sufficiently mature.

---

# Outputs

The system creates three primary persistent output types.

## Structured Article Records

Processed records preserve enough metadata to:

- identify the source;
- inspect original and normalised fields;
- understand classifications;
- understand relevance scores;
- support later deterministic quality analysis.

Current storage format:

```text
JSON Lines
```

---

## Daily Markdown Report

The report includes:

- report date;
- monitored period;
- generation timestamp;
- run status;
- source health;
- item counts;
- domain sections;
- ranked headlines;
- source identity;
- publication time;
- relevance score;
- secondary domains;
- permitted source-provided context;
- direct source links;
- visible degraded-run warnings.

The target is not to reproduce full articles.

The target is enough lawful context for initial understanding.

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

# Historical Archive

Production reports, processed records and run summaries remain accessible through the repository.

The historical processed-record layer also provides useful deterministic evidence for later regression testing of classification and ranking changes.

This regression value has already become an important part of controlled taxonomy development.

---

# Non-Goals

The project is not intended to:

- replace professional news analysis;
- provide exhaustive global coverage;
- reproduce complete articles;
- bypass paywalls;
- scrape websites against their terms;
- automate authenticated Bocconi premium-content retrieval;
- automate authenticated Career Services / JobGate retrieval;
- bulk-ingest Factiva, Nexis, Bloomberg or similar licensed databases;
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
- build infrastructure merely because it is technically interesting;
- recreate Financial Times or Reuters through a collection of weaker redundant sources;
- force every strategic macroarea to have the same number of sources.

These possibilities should be reconsidered only when real evidence demonstrates a clear workflow need and all core constraints remain satisfied.

---

# Success Criteria

The project should be judged on both technical operation and information usefulness.

## Functional Success

- Relevant items are collected from a credible structured-source universe.
- Metadata is normalised consistently.
- The publication window is enforced correctly.
- Malformed records are handled visibly.
- Obvious duplicates are reduced.
- Important items receive useful domain classifications.
- Unclassified low-value material does not need to be forced into the report.
- Ranking is transparent.
- A readable daily report is generated.
- Structured history is preserved.
- Production runs automatically.
- Changed outputs persist automatically.
- Failures are visible.

---

## Cost Success

- Recurring monetary cost remains zero.
- Production does not consume recurring AI or Copilot credits.
- No paid API is required.
- No commercial automation platform is required.

---

## User-Experience Success

- Normal daily manual work is negligible.
- The report can be consumed within manageable time.
- Important developments can be understood without opening every article.
- Source links remain useful for selective deeper reading.
- Reports are not dominated by duplicates or low-value material.
- Relevant professional ecosystem opportunities are surfaced when available.
- Degraded reports are visibly degraded.
- Inaccessible links do not routinely make selected items useless.

---

## Quality Success

- Important stories are not systematically buried by noise.
- Source provenance is transparent.
- Accessibility, metadata richness and persistence compatibility are considered.
- Classification is adequate for practical use.
- Ranking remains understandable.
- Unsupported context is not fabricated.
- Missing data and failures are visible.
- The source universe adequately covers the intended strategic information functions.
- Major domains are not unnecessarily dependent on one weak or incidental source.
- Technical sophistication is introduced only when it improves real information quality.

---

## Reliability Success

- Source failures are isolated where appropriate.
- Critical failures do not create falsely successful output.
- Degraded runs preserve usable content.
- Repeated runs do not create uncontrolled duplication.
- No-change runs do not create empty commits.
- Network requests are bounded.
- Scheduled automation works without normal daily intervention.

---

## Maintainability Success

- The repository remains understandable.
- Configuration remains separated from logic where appropriate.
- Sources can be replaced without pipeline redesign.
- Domains can normally be added through configuration.
- Source-defined domains can reuse existing classification architecture where justified.
- Dependencies remain limited.
- Modules retain clear responsibilities.
- Architecture remains proportional to value.
- Source expansion does not create disproportionate recurring maintenance.
- New processing paradigms are introduced only after their information value is validated.

---

# Development Philosophy

The project should evolve through evidence rather than speculative architecture.

Preferred loop:

```text
observe real problem
→ isolate cause
→ identify simplest solution
→ implement smallest coherent change
→ validate
→ inspect actual output
→ stop at stable checkpoint
```

For source expansion:

```text
identify information-function gap
→ research high-value candidate
→ validate endpoint and policy
→ test real collector
→ test classification
→ inspect report contribution
→ approve / standby / reject
→ checkpoint
```

Before adding complexity, ask:

1. What user problem does this solve?
2. Has it occurred in real use?
3. What information function is missing?
4. Can a weak source simply be replaced?
5. Can configuration solve it?
6. Can existing structured metadata solve it?
7. What maintenance does the change add?
8. What new failure modes appear?
9. Does it preserve zero recurring cost?
10. Does it preserve negligible daily manual work?
11. Does it preserve transparency?
12. Does it preserve credential and copyright boundaries?
13. How will success be tested?

This applies especially to:

- richer report generation;
- near-duplicate clustering;
- entity extraction;
- geography;
- content types;
- ranking;
- source-health systems;
- statistical-event processing;
- opportunity/deadline tracking;
- dashboards;
- AI integration.

---

# Current Strategic Sequence

The strategic sequence is:

```text
Production automation
COMPLETE

↓

Source and domain correction / expansion
ACTIVE

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

Source/domain work should stop when additional expansion has lower expected value than improving understanding of already-selected items.

The active expansion process is now driven by domain gaps rather than source prestige.

Current highest-priority information weaknesses are:

```text
Financial Markets
Companies / Corporate Strategy
Italy
independent AI / Technology coverage
```

Milan/Bocconi and Startups/VC also require further diversification, but first implementations already exist.

---

# Risks

## Overengineering

The project may become focused on architecture instead of useful output.

**Response:** prefer simple evidence-driven corrections.

---

## Excessive Source Volume

More sources may increase noise, duplication and failure rates.

**Response:** optimise for the smallest strong source universe with differentiated information roles.

---

## Prestige Bias

High-profile publications may appear attractive even when their marginal information value or automation suitability is poor.

**Response:** evaluate actual contribution, access, metadata and persistence compatibility.

Completed FT, Reuters and Il Sole audits demonstrate that prestige alone is not sufficient.

---

## Redundant Source Accumulation

Several sources may report the same type of development without adding a distinct information function.

**Response:** prioritise complementarity.

For example:

```text
primary evidence
+
independent analysis
```

is usually more useful than:

```text
general news source
+
similar general news source
```

---

## Paywalled Follow-Up

A useful item may link to premium content.

**Response:** prefer accessible sources where value is comparable. Apply the Premium Bocconi Exception only deliberately and source by source.

Never bypass the paywall.

---

## Misuse of Institutional Access

Bocconi access may create temptation to automate premium resources.

**Response:** preserve a strict separation between personal reading access and production retrieval.

---

## Weak Report Context

The report may identify important stories without explaining them sufficiently.

**Response:** design the richer-context layer deliberately, beginning with lawful structured metadata.

---

## Weak Ranking

Simple deterministic scoring may not perfectly represent practical importance.

**Response:** fix source and classification evidence first. Increase ranking sophistication only if necessary.

---

## Poor Duplicate Detection

Different headlines may describe the same event.

**Response:** retain exact deduplication until repeated evidence justifies more.

Italian Tech Alliance provides a possible future use case but does not yet justify new clustering architecture.

---

## Source Instability

Feeds may change, fail or disappear.

**Response:** isolate failures and replace sources whose maintenance cost becomes disproportionate.

---

## Scheduler Latency

GitHub may execute scheduled workflows later than configured.

**Response:** continue monitoring whether this materially affects report usefulness before changing architecture.

---

## Multilingual Classification

English keywords may collide with common Italian words.

**Response:** prefer the smallest deterministic correction before introducing language-processing complexity.

The `AI` versus Italian `ai` case has already validated this principle.

---

## Public-Repository Exposure

Generated content may accidentally contain restricted or private material.

**Response:** use only approved inputs and preserve explicit repository boundaries.

---

## Passive Consumption

The system may increase reading without improving understanding.

**Response:** optimise for concise understanding, selective deeper reading and actionable opportunity awareness.

---

# Long-Term Possibilities

Possible later improvements include:

- broader high-quality source coverage where justified;
- structured statistical signals from official sources;
- conservative near-duplicate clustering;
- multi-source story grouping;
- tracked companies and institutions;
- article-level geography;
- content-type classification;
- source-health history;
- opportunity/deadline state where justified;
- weekly archive analytics;
- trend detection;
- stable latest-report links;
- GitHub Issue delivery;
- GitHub Pages.

These are possibilities, not commitments.

Current strategic macroarea state:

```text
Financial Markets
→ implemented, dedicated source coverage still incomplete

Milan/Bocconi
→ first production implementation active through TEF
→ broader professional ecosystem requirement remains incomplete

Italy
→ approved target macroarea pending implementation
```

---

# Public Repository Boundary

The repository is intended to remain public and may function as proof of work.

It may contain:

- project documentation;
- source code;
- public-source configuration;
- structured permitted metadata;
- generated headlines and links;
- permitted public descriptions;
- deterministic classifications and scores;
- run summaries;
- tests;
- controlled fixtures;
- GitHub Actions workflows;
- public-safe reports.

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

# Current Strategic Status

Production automation is complete.

The project is currently in:

> **source and domain correction / expansion**

Phase 4 has already validated several durable principles:

- a weak source can be replaced without redesigning the pipeline;
- taxonomy coverage can expand through configuration;
- source-defined domains can reuse the existing pipeline;
- real historical records can be used for regression testing;
- report quality must be inspected separately from technical success;
- premium reading access and automation permission are independent;
- multilingual edge cases can often be solved with simple deterministic logic;
- strategic source value does not override persistence/licensing constraints;
- the source universe should expand according to information-function gaps rather than publisher count.

Milan/Bocconi now has a first production implementation through Tech Europe Foundation.

Italy remains the major target macroarea without a dedicated implementation.

The most important remaining information gaps are:

```text
Financial Markets
Companies / Corporate Strategy
Italy
independent AI / Technology
```

Detailed implementation state, source counts, source audits and immediate tasks belong in:

```text
03 Information Taxonomy and Source Policy.md
04 Development Roadmap and Status.md
```

Current strategic priority:

> **Continue building the smallest high-value source and domain universe, prioritising missing information functions rather than publisher count.**

Following strategic priority:

> **Design and implement a richer report experience that provides enough lawful context for initial understanding.**

---

# Decision Rule

Every future project decision should answer:

> Does this change materially improve reliability, information quality or user value without violating the constraints on cost, manual work, maintainability, accessibility, transparency, privacy, copyright and scope?

For source expansion, also ask:

> Does this source add a meaningful information function that the current system lacks?

If the answer is unclear, defer the change until evidence exists.

---

# Changelog

## 2026-08-17 — Milan/Bocconi Activation and Information-Function Source Strategy

- Preserved the stable project purpose, constraints and two-layer operating model.
- Recorded Milan/Bocconi as having a first production implementation through Tech Europe Foundation rather than remaining fully pending.
- Preserved Milan/Bocconi as only partially satisfied because TEF does not cover complete recruiting, employer-event or deadline intelligence.
- Preserved authenticated Bocconi Career Services and JobGate as outside automated production.
- Preserved Italy as the remaining approved strategic macroarea without a dedicated implementation.
- Recorded Financial Markets as implemented but still lacking sufficient dedicated source coverage.
- Added information-function coverage as an explicit source-expansion principle.
- Recorded the durable rule: correct information-function gaps before publisher-count gaps.
- Recorded Financial Markets, Companies/Corporate Strategy, Italy and independent AI/Technology as the current highest-cost information gaps.
- Recorded the durable conclusion from FT, Reuters and Il Sole research that strategic value does not override automation, licensing or public-repository persistence constraints.
- Recorded source-defined domains as a validated low-complexity expansion pattern.
- Recorded the multilingual `AI` versus Italian `ai` lesson as evidence for minimal deterministic corrections before language-processing complexity.
- Preserved richer report context as the following major product objective.
- Kept detailed source decisions, audit results, counts and implementation sequencing in `03` and `04`.

## 2026-08-17 — Phase 4 Strategic Reconciliation

- Preserved the stable project purpose, constraints and operating model.
- Removed unnecessary transient implementation detail from the strategic brief.
- Recorded Financial Markets as an implemented strategic macroarea rather than a future possibility.
- Recorded Milan/Bocconi Professional Ecosystem Intelligence as a validated product requirement.
- Preserved Italy as an approved target macroarea pending implementation.
- Recorded the durable lesson from the Sifted → Tech.eu replacement: technical compatibility alone does not establish source quality.
- Added the narrow Premium Bocconi Exception while preserving the prohibition on authenticated automated premium-content retrieval.
- Recorded selective classification rather than classification percentage as the intended information-quality philosophy.
- Preserved source/domain correction as the active strategic phase.
- Preserved richer report context as the following major product objective.
- Kept detailed implementation status and chronology in the dedicated roadmap/status document.

## 2026-08-14 — Production Automation Closeout and Information-Quality Reorientation

- Reconciled the Project Brief with completed Phase 2 and Phase 3 implementation.
- Recorded the completed deterministic production automation baseline.
- Changed the strategic priority from automation to source/domain quality.
- Added source accessibility and metadata richness as strategic information-quality considerations.
- Added the requirement for sufficient lawful context before immediate click-through.
- Added the distinction between automated public sources, Bocconi premium reading and institutional research/database resources.
- Preserved zero recurring monetary cost, deterministic production, public-repository safety and no-production-AI constraints.

## 2026-08-11 — Phase 1 Project Brief Reconciliation

- Reconciled the brief with the validated local vertical slice.
- Preserved the original project purpose and strategic rationale.
- Reinforced evidence-driven, minimal-complexity development.

## Initial Project Brief Baseline

- Defined the Daily Intelligence System problem and strategic rationale.
- Defined the two-layer ChatGPT and GitHub operating model.
- Established zero recurring cost and negligible daily manual work as hard constraints.
- Defined scope, outputs, non-goals, risks and success criteria.