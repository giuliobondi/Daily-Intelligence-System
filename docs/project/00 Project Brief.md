


# Daily Intelligence System — Project Brief

> **Purpose**
>
> This document defines why the Daily Intelligence System exists, what problem it solves, what the project is intended to achieve, and what is deliberately outside its scope.
>
> It is the strategic reference for all later product, architecture and implementation decisions.
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
- building a searchable historical archive;
- supporting better interpretation through a separate ChatGPT briefing workflow.

---

# Problem

Important information is distributed across:

- news publications;
- official institutions;
- company announcements;
- research organisations;
- technical blogs;
- startup and venture-capital sources;
- public newsletters;
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

Most news products optimise for broad engagement rather than the specific combination of economics, politics, markets, AI, technology, startups and career relevance required by this project.

## Limited Historical Memory

Daily reading is easily forgotten when stories, sources and recurring themes are not stored systematically.

## Passive Consumption

Reading more news does not necessarily produce better understanding.

The system should support informed judgment, professional conversations and durable learning rather than encourage endless content consumption.

---

# Target User

The primary user is a university student building knowledge and professional awareness across economics, politics, finance, AI, technology, startups and business strategy.

The user:

- values source quality over content volume;
- wants broad but structured awareness;
- has limited time for daily manual research;
- wants to avoid recurring monetary costs;
- is willing to invest time in initial setup and occasional maintenance;
- has working exposure to Python, GitHub, data analysis and software-system concepts;
- does not want the system to become an unnecessarily complex engineering project.

The initial version is designed for one user.

Multi-user features are outside the MVP.

---

# Strategic Rationale

The project has value across several dimensions.

## Knowledge

It should improve understanding of:

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
- managers and recruiters.

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
- automation;
- information architecture;
- data-pipeline design;
- deterministic classification and ranking;
- documentation;
- testing;
- workflow-oriented problem solving.

The project should preserve optionality across data, consulting, AI strategy, finance, venture capital, startups, economic research and technology-oriented roles.

---

# Agreed Operating Model

The complete information workflow contains two independent layers.

## Layer 1 — ChatGPT Intelligence Briefing

A scheduled ChatGPT workflow independently researches and synthesises current developments.

Its role is to provide:

- interpretation;
- explanations;
- cross-domain connections;
- trend analysis;
- uncertainty;
- career-relevant implications.

This layer is outside the GitHub repository.

The repository does not depend on automatic access to ChatGPT, plugins, connectors or paid model APIs.

## Layer 2 — GitHub Intelligence Pipeline

The GitHub repository owns the deterministic collection and archive system.

Its role is to:

1. collect items from permitted public structured sources;
2. normalise metadata;
3. clean URLs and timestamps;
4. detect likely duplicate stories;
5. classify items by domain;
6. calculate transparent relevance scores;
7. store structured records;
8. generate daily Markdown reports;
9. preserve historical outputs;
10. expose source or workflow failures.

The two layers may cover overlapping stories, but they serve different purposes.

The ChatGPT layer provides interpretation.

The GitHub layer provides controlled coverage, transparency and historical memory.

The MVP does not require an automated connection between them.

---

# Project Objectives

The system should:

- run automatically every day;
- require negligible daily manual work;
- operate with zero recurring monetary cost;
- avoid recurring consumption of AI or Copilot credits;
- collect from a curated universe of public sources;
- preserve direct source links;
- reduce obvious duplication;
- organise content into configurable domains;
- rank stories using understandable rules;
- generate a concise and readable daily report;
- store enough metadata for later analysis;
- make failures visible;
- remain simple enough to understand and maintain;
- create a foundation that can be improved without rebuilding the entire system.

---

# Core Constraints

## Cost

- Recurring monetary cost must remain zero.
- Paid APIs, paid news products and paid automation platforms must not be required.
- The project must not depend on OpenAI API credits.
- The project must not depend on recurring GitHub AI or Copilot usage.
- Cloud services that could create accidental charges should be avoided unless explicitly approved later.

## Automation

- Daily manual work should be close to zero.
- Daily copying between GitHub, ChatGPT, email or other systems should not be required.
- Occasional source maintenance and quality review are acceptable.

## Technical Scope

- Ordinary Python and GitHub Actions should handle recurring production work.
- Deterministic logic should be preferred before machine learning or LLM calls.
- RSS feeds, official APIs and structured public sources should be preferred before scraping.
- The MVP should avoid complex infrastructure.

## Reliability

- Individual source failures should not necessarily stop the entire workflow.
- Failures should be logged and visible.
- Generated reports should be reproducible from stored inputs where practical.
- The system should fail clearly rather than silently produce misleading output.

## Privacy and Copyright

The public repository must not contain:

- credentials;
- private account information;
- personal Career OS documents;
- private emails;
- full paid articles;
- restricted newsletter content;
- unauthorised copies of copyrighted material;
- sensitive personal reading data.

---

# MVP Scope

The MVP must support one complete end-to-end workflow:

    Public structured sources
            ↓
    Collection
            ↓
    Metadata normalisation
            ↓
    Duplicate reduction
            ↓
    Domain classification
            ↓
    Relevance ranking
            ↓
    Structured storage
            ↓
    Daily Markdown report
            ↓
    Automated GitHub execution
            ↓
    Visible success or failure

The MVP should be built using a limited initial source universe.

The first version should prioritise proof that the full loop works reliably over broad source coverage.

---

# MVP Outputs

The MVP should produce:

## Structured Article Records

Each record should preserve the available core metadata required for filtering, ranking and later inspection.

The final schema will be defined in the Information Taxonomy and Source Policy document.

## Daily Markdown Report

The report should contain:

- report date;
- monitored period;
- grouped domains;
- ranked headlines;
- source name;
- publication time;
- short available description where permitted;
- direct source link;
- indication of duplicate or multi-source coverage where available;
- visible warnings about failed sources or incomplete runs.

## Historical Archive

Daily reports and processed records should remain accessible for later review.

## Execution Logs

The system should make it possible to understand:

- whether the workflow completed;
- which sources failed;
- how many items were collected;
- how many items remained after filtering and deduplication;
- whether the report was successfully generated.

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
- ingest private newsletters or email during the MVP;
- automatically edit the Career OS;
- automatically transfer GitHub reports into ChatGPT.

These may be reconsidered only if later evidence shows a clear need and the core constraints remain satisfied.

---

# Success Criteria

The MVP will be considered successful when all of the following are true.

## Functional Success

- The system collects items from a small but diverse initial source universe.
- Metadata is normalised consistently.
- Obvious duplicate items are reduced.
- Items are assigned to useful domains.
- A transparent ranking process is applied.
- A readable Markdown report is generated.
- Reports are stored historically.
- The workflow runs automatically through GitHub Actions.
- Failed sources or workflow problems are visible.

## Cost Success

- Recurring monetary cost is zero.
- Production runs do not consume GitHub AI or Copilot credits.
- No paid API is required.

## User-Experience Success

- Daily manual work is negligible.
- The report can be scanned quickly.
- Source links are easy to access.
- The report is not dominated by duplicates or low-value content.
- The output is concise enough to be used consistently.

## Quality Success

- Important items are not systematically buried by low-value stories.
- Source quality and source type are visible.
- Classification is adequate for practical use.
- Ranking logic is understandable.
- The system does not fabricate analytical summaries.
- Missing data and source failures are not hidden.

## Maintainability Success

- A future contributor can understand the repository from its documentation.
- Configuration is separated from application logic where appropriate.
- The source universe can be updated without rewriting the core pipeline.
- Dependencies remain limited.
- The architecture remains proportional to the actual value created.

---

# Evaluation Period

The MVP should not be judged only from technical tests.

After the automated workflow is stable, it should be used for an initial evaluation period of approximately two weeks.

During this period, evaluate:

- whether the report is actually read;
- whether it is too long or too short;
- whether important stories are missed;
- whether low-value stories are overrepresented;
- whether duplicate reduction is effective;
- whether domain classification is useful;
- whether source diversity is adequate;
- whether maintenance remains minimal;
- whether the system improves knowledge or merely increases content volume.

Further development should depend on evidence from this evaluation.

---

# Risks

## Overengineering

The project may become focused on architecture rather than useful output.

**Response:** build the smallest complete vertical slice before adding secondary components.

## Excessive Source Volume

Adding too many sources may increase noise and failure rates.

**Response:** begin with a small curated source universe and expand only when coverage gaps are demonstrated.

## Weak Ranking

Simple deterministic scoring may fail to reflect real importance.

**Response:** keep the scoring transparent, review real outputs and improve it iteratively.

## Poor Duplicate Detection

Different headlines may describe the same event.

**Response:** begin with simple URL and title-based methods, then improve only if real reports show a material problem.

## Source Instability

Feeds may change, fail or disappear.

**Response:** isolate source failures, record source health and avoid depending on a single source.

## Public-Repository Exposure

Generated content may accidentally include restricted or personal material.

**Response:** use only public structured sources during the MVP and maintain explicit repository boundaries.

## Passive Consumption

The system may increase reading without improving understanding.

**Response:** keep reports concise and maintain the separate ChatGPT interpretation layer.

## Maintenance Burden

A complex pipeline may require more effort than the value it provides.

**Response:** prefer simple components, minimal dependencies and occasional controlled maintenance.

---

# Long-Term Possibilities

The following may be considered after the MVP has been validated:

- a larger source universe;
- improved story clustering;
- tracked companies, institutions and topics;
- source-health dashboards;
- GitHub issue delivery;
- GitHub Pages;
- weekly archive analytics;
- trend detection;
- selected public-newsletter support;
- improved opportunity monitoring for Milan and Bocconi;
- better integration with weekly knowledge-review workflows.

These are possibilities, not commitments.

They should be evaluated against:

- recurring cost;
- reliability;
- manual work;
- information quality;
- maintenance;
- privacy;
- demonstrated user need.

---

# Public Repository Boundary

This repository is intended to remain public and may later function as proof of work.

It may contain:

- public project documentation;
- source code;
- public-source configuration;
- structured public metadata;
- generated headlines and links;
- tests;
- sample outputs;
- GitHub Actions workflows.

Private Career OS sources are contextual inputs used inside the dedicated GPT project and must not be copied into this repository.

---

# Current Project Status

**Phase:** Project definition

**Completed:**

- Selected the hybrid operating model.
- Confirmed zero recurring monetary cost as a hard constraint.
- Confirmed negligible daily manual work as a hard constraint.
- Confirmed that production must not consume AI credits.
- Created the public GitHub repository.
- Created the initial project-document structure.

**Current task:**

- 

**Next document:**

- 

---

# Decision Rule

Every future project decision should answer:

> Does this change materially improve reliability, information quality or user value without violating the constraints on cost, manual work, maintainability and scope?

If the answer is unclear, the change should be deferred until evidence is available.