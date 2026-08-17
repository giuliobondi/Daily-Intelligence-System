# Daily Intelligence System — Information Taxonomy and Source Policy

> **Purpose**
>
> Define what information the Daily Intelligence System should collect, how it should classify that information, which sources are acceptable, and which rules govern source selection, accessibility, storage and public presentation.
>
> This document is the canonical quality-control policy for information entering the system.

> **Primary question**
>
> *What information should the system collect, from which sources, and under which classification, accessibility and quality rules?*

> **Update frequency**
>
> Update when monitored domains, source-selection rules, accessibility assumptions, metadata requirements or source-governance policies materially change.

---

# Information Objective

The system should provide broad but selective awareness of developments that may affect:

- economics and macroeconomics;
- politics and geopolitics;
- financial markets;
- companies and corporate strategy;
- artificial intelligence;
- technology and software;
- startups and venture capital;
- Europe and the European Union;
- Italy;
- Milan and the Bocconi ecosystem.

The objective is not maximum coverage.

The objective is to identify a manageable set of high-value items from transparent, credible and operationally suitable sources.

Information quality should be evaluated through:

1. relevance;
2. source credibility;
3. originality;
4. timeliness;
5. diversity;
6. transparency;
7. reader accessibility;
8. metadata richness;
9. suitability for automated collection;
10. maintenance burden.

The system should prefer a smaller set of strong sources over broad but noisy coverage.

A technically compatible source is not automatically a good product source.

---

# Current Implementation Status

The deterministic information-processing model is implemented and production-automated.

Current production configuration:

- seven active public RSS sources;
- eight active topic domains;
- deterministic title-and-description keyword rules;
- optional source-default domains;
- deterministic source-tier scoring;
- exact duplicate reduction;
- previous-24-hours publication window;
- explicit handling of unclassified records;
- scheduled GitHub Actions execution;
- automated output persistence;
- source-level failure isolation;
- degraded-run reporting.

Current active sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Tech.eu.

Current implemented domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Financial Markets;
4. Companies and Corporate Strategy;
5. Artificial Intelligence;
6. Technology and Software;
7. Startups and Venture Capital;
8. Europe and the European Union.

Still unimplemented:

- Italy;
- Milan and Bocconi Ecosystem.

Phase 4 has now produced its first validated information-quality correction:

- Sifted was replaced by Tech.eu;
- Tech.eu uses no blanket source-default domain;
- Financial Markets was implemented as the eighth domain;
- `tariffs`, `acquired`, `early-stage fund` and `funding market` were added after real-record testing;
- the generic Startups/VC keyword `startup` was removed after it promoted low-value stories too easily;
- the configuration passed the full 110-test suite and a real 17 August 2026 pipeline run whose report was manually inspected.

The current priority remains:

> **Continue correcting and expanding sources and domains before implementing richer report-context logic.**

---

# Taxonomy Principles

## Configurable

Domains, keywords, source tiers and source defaults belong in configuration rather than scattered through processing code.

Configuration should expand only when corresponding information value is justified.

## Multi-Domain

A story may legitimately belong to more than one domain.

Examples:

- an EU AI regulation may belong to Artificial Intelligence, Technology and Europe/EU;
- an ECB rate decision may belong to Economics, Financial Markets and Europe/EU;
- a startup acquisition may belong to Startups/VC and Companies/Corporate Strategy.

## One Primary Report Placement

A multi-domain item should appear once in the report.

Current policy:

- first assigned eligible domain becomes primary placement;
- additional domains appear as secondary metadata.

## Explainable

Current classification evidence consists of:

- source defaults;
- matched configured keywords.

Any future mechanism should remain inspectable.

## Conservative

Prefer an unclassified record over a misleading classification.

Unclassified records remain valid processed records but are omitted from the main report by default.

A high unclassified share is not itself a defect. The 17 August 2026 review showed that many unclassified BBC records were correctly excluded low-value or out-of-scope stories.

The correct question is:

> **Are important stories being missed?**

not:

> **Is the classification rate high?**

## Broad but Bounded

The system should not become a generic global-news taxonomy.

## Independent Dimensions

Topic, geography, source tier, reader accessibility and content type are conceptually separate.

Only topic classification and source tier are currently implemented at article level.

Source-level geographic scope exists in configuration.

---

# Target Topic Taxonomy

The strategic target remains ten macroareas.

Eight are implemented.

Italy is strategically approved but awaits suitable source coverage and tested classification logic.

Milan and Bocconi Ecosystem is a validated product requirement but awaits suitable public structured sources and a low-maintenance implementation.

---

## 1. Global Politics and Geopolitics

### Scope

Major political, diplomatic, security and geopolitical developments with international or material economic relevance.

### Include

- wars and conflicts;
- peace negotiations;
- sanctions;
- tariffs and trade restrictions;
- major elections with material consequences;
- major foreign-policy changes;
- defence and security developments;
- geopolitical shocks affecting markets, technology, energy or supply chains.

### Exclude or Deprioritise

- routine political theatre;
- personality-driven coverage;
- minor party disputes;
- local politics without wider consequence.

### Current Status

**Implemented.**

Current evidence-backed refinements include:

- `war`;
- `conflict`;
- `parliament`;
- `tariffs`.

`tariffs` was added after a relevant BBC World US-China trade story remained unclassified. A three-day, 114-record regression produced no unintended additional classification changes beyond the intended recovery.

Broad terms such as `government`, `defence`, `president` and `prime minister` were previously tested but rejected because they produced ambiguous or low-value matches.

---

## 2. Economics and Macroeconomics

### Scope

Developments affecting growth, inflation, employment, monetary policy, fiscal policy, trade, productivity and public finances.

### Include

- inflation;
- GDP and growth;
- employment and unemployment;
- interest-rate decisions;
- monetary and fiscal policy;
- public debt;
- trade;
- productivity;
- industrial production;
- economic forecasts;
- major central-bank and statistical-agency research.

### Exclude or Deprioritise

- generic personal finance;
- unsupported forecasts;
- routine commentary without new evidence.

### Current Status

**Implemented.**

Istat Press Releases has Economics and Macroeconomics as a source default because its selected feed is sufficiently narrow.

BBC Business does not receive an Economics default because it is heterogeneous.

---

## 3. Financial Markets

### Scope

Major developments affecting capital markets, asset pricing and financial-system conditions.

### Include

- meaningful equity repricing;
- rates and bond yields;
- yield-curve changes;
- credit conditions and spreads;
- currencies when macro-relevant;
- commodities when economically relevant;
- capital markets;
- financial stability;
- asset management;
- IPO conditions;
- major market reactions to macro or company developments.

### Exclude or Deprioritise

- daily index recaps;
- isolated minor price moves;
- trading tips;
- technical-analysis commentary;
- price predictions;
- generic market colour without causal explanation.

### Current Status

**Implemented — conservative first version.**

Initial configured keywords:

- stock market;
- bond market;
- bond yields;
- yield curve;
- credit spreads;
- capital markets;
- financial stability;
- market sell-off;
- foreign exchange;
- equities;
- asset management;
- IPO.

Broad terms such as `market`, `stocks`, `shares`, `bonds`, `rates`, `bank` and `investment` are intentionally excluded for now.

The first implementation was simulated against real records before editing configuration. On 17 August 2026 it correctly surfaced a BBC Business story about a severe South Korean stock-market correction without creating observed false-positive classifications in the tested sample.

Expand only from observed missed stories and controlled regression tests.

---

## 4. Companies and Corporate Strategy

### Scope

Company actions and industry developments that reveal changes in strategy, competition, business models or capital allocation.

### Include

- M&A;
- divestments;
- restructuring;
- strategic partnerships;
- significant investment;
- market entry or exit;
- business-model change;
- strategically material earnings or guidance;
- bankruptcy or turnaround;
- material leadership changes;
- competitive shifts.

### Exclude or Deprioritise

- routine product promotion;
- minor executive appointments;
- small operational updates;
- marketing announcements without strategic significance.

### Current Status

**Implemented.**

No broad current source receives a Corporate Strategy default.

Phase 4 added `acquired` after real Tech.eu records showed that the noun `acquisition` alone missed clear M&A stories. `acquired` produced no changes across the 114-record existing production regression corpus used for validation.

---

## 5. Artificial Intelligence

### Scope

Major developments in AI models, products, research, infrastructure, regulation, enterprise adoption and business impact.

### Include

- major model and platform changes;
- enterprise AI adoption;
- workflow automation and agents;
- compute and infrastructure;
- AI regulation and governance;
- AI economics and business models;
- significant AI funding and M&A;
- material safety, security or research developments.

### Exclude or Deprioritise

- superficial feature launches;
- minor wrappers;
- generic prompt content;
- unsupported AGI claims;
- repetitive promotional announcements.

### Current Status

**Implemented.**

OpenAI News has Artificial Intelligence as its single source default.

It does not receive automatic Technology or Corporate Strategy defaults.

Independent AI reporting remains a future source-coverage question.

---

## 6. Technology and Software

### Scope

Major developments in software, cloud infrastructure, cybersecurity, semiconductors, data systems and digital platforms.

### Include

- enterprise software;
- cloud and data infrastructure;
- cybersecurity;
- semiconductors;
- developer platforms and APIs;
- major open-source developments;
- platform strategy;
- commercially meaningful computing shifts.

### Exclude or Deprioritise

- consumer gadget rumours;
- minor feature releases;
- generic tutorials;
- low-impact product updates.

### Current Status

**Implemented.**

No current source receives Technology as a blanket default.

---

## 7. Startups and Venture Capital

### Scope

Developments affecting startup financing, scaling, exits, failures and venture-capital ecosystems.

### Include

- significant funding rounds;
- new VC funds;
- exits and acquisitions;
- startup failures and restructurings;
- ecosystem shifts;
- venture strategy;
- strategically relevant European and Italian startup developments;
- AI, enterprise software, fintech and deeptech when material.

### Exclude or Deprioritise

- very small funding announcements without strategic relevance;
- promotional founder profiles;
- generic startup listicles;
- unverified fundraising rumours;
- generic entrepreneurship advice.

### Current Status

**Implemented — Tech.eu is the current specialist production source.**

Sifted was replaced after a direct controlled comparison.

Observed comparison:

```text
Tech.eu: 20 tested items, 20 descriptions, average description length ≈ 203 characters
Sifted:  24 tested items, 0 descriptions
```

Both feeds collected and normalised successfully. The decision therefore turned on product quality, accessibility and metadata richness rather than basic technical compatibility.

Tech.eu uses:

```yaml
default_domains: []
```

because its general feed spans startups, AI, corporate strategy, technology and European policy.

Phase 4 added:

- `early-stage fund`;
- `funding market`.

Both recovered useful Tech.eu stories and caused zero changes across the 114-record existing production regression corpus.

The generic keyword `startup` was removed because it promoted weak profiles too easily. The three-day regression showed that removing it mainly reduced keyword scores for historical Sifted items whose old source default already supplied Startups/VC evidence, while suppressing a low-value Tech.eu profile in the live test.

The goal is meaningful startup/VC pattern recognition, not funding-round volume.

---

## 8. Europe and the European Union

### Scope

Major European institutional, regulatory, economic and industrial developments.

### Include

- EU legislation;
- Commission initiatives;
- ECB developments;
- competition policy;
- industrial policy;
- trade policy;
- digital and AI regulation;
- capital-markets integration;
- energy and strategic autonomy;
- major cross-European economic developments.

### Exclude or Deprioritise

- routine institutional communications;
- procedural politics without consequence;
- minor national stories without wider relevance.

### Current Status

**Implemented.**

ECB and European Commission feeds do not receive Europe/EU as blanket defaults.

---

## 9. Italy

### Scope

Italian developments with economic, corporate, financial, technological or professional relevance.

### Include

- macroeconomic indicators;
- major Italian companies;
- banks and financial institutions;
- capital markets and M&A;
- industrial policy;
- economically significant regulation and taxation;
- infrastructure and energy;
- labour-market developments;
- technology and startups.

### Exclude or Deprioritise

- general national news without economic or professional significance;
- sport;
- celebrity;
- crime;
- routine party conflict.

### Current Status

**Strategically approved; production implementation pending source validation.**

Istat already contributes Italian macro evidence.

Highest-priority candidate sources include Il Sole 24 Ore and Bank of Italy, subject to technical validation.

---

## 10. Milan and Bocconi Ecosystem

### Scope

High-value professional ecosystem intelligence connected to Milan, Bocconi and relevant local communities.

### Include

- recruiting and employer events;
- finance, consulting, AI/data, technology and startup events;
- B4i programmes and startup calls;
- research opportunities;
- competitions;
- high-value public lectures;
- Milan startup, VC and fintech developments;
- innovation programmes;
- time-sensitive deadlines where missing the information would close a meaningful opportunity.

### Exclude or Deprioritise

- routine university administration;
- generic campus activity;
- tourism;
- nightlife;
- low-quality networking events;
- opportunities clearly irrelevant to the user;
- generic city events.

### Current Status

**Validated product requirement — production implementation pending source validation.**

This macroarea is no longer optional.

The Daily Intelligence System should act as the external sensor.

Personal decisions, applications, networking follow-up and relationship management remain in the Career OS.

Strategically approved first candidates for technical audit:

1. B4i;
2. Bocconi Career Services;
3. Bocconi News & Events.

Possible later complements:

- Italian Tech Alliance;
- Fintech District;
- narrowly filtered Comune di Milano sources.

Do not force implementation through authenticated scraping, email ingestion, manual daily copy-and-paste or automated Bocconi/OpenAthens login.

---

# Source Hierarchy

Source tier represents evidentiary role and expected reliability.

It does not guarantee:

- importance;
- accessibility;
- metadata richness;
- report usefulness.

## Tier 1 — Primary and Official Sources

Examples:

- governments;
- regulators;
- central banks;
- statistical agencies;
- European institutions;
- official company or research-lab publications;
- universities;
- original research publications.

Strength:

- closest to primary evidence.

Limitation:

- can be promotional, routine or context-poor.

## Tier 2 — High-Quality Reporting

Established journalistic or specialist organisations providing original reporting, verification or useful professional context.

Tier 2 does not imply automatic production eligibility.

The Sifted replacement decision is the clearest current example: Sifted remained strategically relevant but was replaced because Tech.eu offered better metadata and follow-up usability.

## Tier 3 — Specialist Analysis

Specialist organisations, research groups, venture funds and industry publications that do not fit the Tier 2 role.

Approve individually.

## Tier 4 — Discovery Sources

Aggregators, forums, social media and similar discovery-oriented sources.

Remain outside production unless a specific structured source proves unusually useful.

---

# Current Source-Tier Scoring

```text
Tier 1 = 4 points
Tier 2 = 3 points
Tier 3 = 2 points
Tier 4 = 1 point
```

Current relevance score also includes:

```text
+ 2 points per assigned domain
+ 1 point per matched keyword
```

These weights remain provisional.

If misleading classification evidence inflates scores:

> **fix upstream evidence before changing ranking weights.**

---

# Source Suitability Model

Production source evaluation must distinguish at least two independent questions.

## Axis 1 — Automation Suitability

Can the system safely, legally and reliably ingest the source?

Evaluate:

- public structured endpoint;
- official feed/API;
- automation permission;
- private credentials required or not;
- timestamps;
- metadata quality;
- technical stability;
- copyright/licence constraints;
- public-repository compatibility;
- maintenance burden.

## Axis 2 — Reader Accessibility

Can the user actually read or investigate the linked article when deeper reading is useful?

Evaluate:

- public web;
- Bocconi Direct;
- Bocconi SearchLib;
- Bocconi database;
- additional personal subscription required;
- unknown or inconsistent access.

These axes are independent.

---

# Bocconi Access Model

Bocconi substantially expands what the user can legitimately read.

It does **not** automatically expand what the production pipeline may retrieve.

## Direct Publisher Access

Confirmed important direct-access publications include:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore.

Corriere della Sera is a special archive/current-edition case rather than confirmed unrestricted premium-site access.

## SearchLib Access

Examples include:

- Foreign Affairs;
- Harvard Business Review;
- Time;
- Economia & Management.

## Database / Professional Research Access

Includes:

- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- S&P Capital IQ Pro;
- Aida.

These belong primarily to manual research, not automated ingestion.

## Public Web

Sources readable without Bocconi credentials.

Public accessibility is favourable but still does not itself prove scraping permission. Prefer structured public endpoints.

---

# Three-Layer Information Access Model

## Layer 1 — Automated Public Intelligence

Used continuously by production.

Allowed inputs include:

- public RSS/Atom;
- official free APIs;
- official public structured metadata;
- other automation-compatible public endpoints.

Requirements:

- no private credentials;
- no paid API dependency;
- no authenticated premium scraping;
- public-repository-compatible metadata;
- acceptable maintenance burden.

## Layer 2 — Bocconi Premium Reading

Used manually for deeper reading.

Examples:

- FT;
- WSJ;
- NYT;
- The Economist;
- Il Sole 24 Ore;
- Foreign Affairs;
- HBR.

## Layer 3 — Research and Databases

Used for targeted investigations.

Examples:

- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg;
- LSEG Workspace;
- FactSet;
- Capital IQ Pro;
- Aida.

Not part of daily automated ingestion by default.

---

# Premium Bocconi Production Exception

A paywall does not automatically exclude a source.

A narrow exception is allowed for unusually valuable premium publications that the user can legitimately read through Bocconi.

A premium publication may be approved even when the public feed or metadata is too thin to support the same rich automated context as a fully public source, provided that:

- its strategic information value is unusually high and difficult to replace;
- the user has legitimate Bocconi access to the linked article;
- the pipeline uses a separate public or automation-compatible discovery endpoint;
- Bocconi credentials are never used by production;
- authenticated premium article bodies are never scraped or stored;
- a thinner report entry and manual click-through are deliberately accepted as the source-specific trade-off.

This is an exception, not a loophole for adding prestigious publications.

Current strongest strategic candidates for this exception:

- Financial Times;
- Il Sole 24 Ore.

Both still require separate technical and policy validation of their public automation interfaces before production approval.

---

# Source Inclusion Criteria

A production source should normally satisfy most of the following.

## Relevance

Consistently contributes to one or more monitored domains.

## Credibility

Identifiable publisher, authorship or institutional responsibility.

## Originality

Provides primary information, original reporting or meaningful specialist analysis.

## Structured Access

Provides stable RSS, Atom, official API or another explicitly approved endpoint.

## Automation Permission

The required automated retrieval must be compatible with the endpoint, terms, licensing and public-repository use.

## Timeliness

Publication timestamps should be available and reasonably reliable.

## Metadata Quality

Titles and links must be usable.

Descriptions and other public context are now explicit product-quality dimensions.

Missing descriptions may remain technically valid but can still make a source a poor product fit.

## Reader Accessibility

Follow-up access must be reviewed separately from automation eligibility.

## Stability

The source should be low-maintenance enough for unattended operation.

## Value-to-Noise Ratio

A meaningful share of output should be relevant.

## Diversity Contribution

A source should add useful evidence, geography, sector or editorial perspective rather than merely duplicate existing coverage.

## Public Repository Compatibility

Only permitted metadata and links should be stored.

## Context Contribution

The source should ideally provide enough lawful public context to support the richer-report requirement.

Premium Bocconi Exception sources may deliberately fall short of this ideal when their strategic value justifies thinner entries.

---

# Source Exclusion or Replacement Criteria

Reject, disable or replace a source when one or more of the following materially apply:

- prohibited scraping is required;
- a paid API is required for core operation;
- private account access is required for automated collection;
- the licence does not permit intended use;
- timestamps are unusable;
- the endpoint is unstable relative to its value;
- the source creates disproportionate maintenance;
- public structured metadata is consistently too thin;
- selected links are repeatedly inaccessible and public context is insufficient;
- the source is excessively promotional or noisy;
- the source systematically duplicates better sources;
- an alternative source provides materially better accessibility, metadata or reliability.

Prefer replacing a weak source over adding source-specific complexity.

---

# Source Evaluation Scorecard

For every candidate review:

```text
Source name
Strategic role
Primary domain contribution
Source tier
Publisher type
Public RSS/Atom?
Official free API?
Automation permission/access model
Credentials required?
Publication timestamps reliable?
Description/context richness
Public article accessibility
Bocconi Direct access
Bocconi SearchLib access
Bocconi database access
Unique contribution
Overlap with existing sources
Expected noise
Expected publication frequency
Expected maintenance
Public-repository compatibility
Recommended status
```

Allowed recommendation language:

```text
Approve for controlled test
Retain
Replace
Disable
Reject
Research further
```

Do not reduce the scorecard to a numeric score unless evidence later shows that doing so improves decisions.

---

# Current Production Source Universe

| Source ID | Source | Tier | Default Domains | Geographic Scope | Policy Status |
|---|---|---:|---|---|---|
| `bbc_world` | BBC News World | 2 | None | Global | Active — retain during expansion |
| `bbc_business` | BBC News Business | 2 | None | Global | Active — likely replacement if stronger business coverage validates |
| `ecb_press` | European Central Bank | 1 | None | EU; Euro Area | Active — core primary source |
| `ec_highlights` | European Commission Highlighted News | 1 | None | European Union | Active — retain, event-driven relevance |
| `istat_press_en` | Istat Press Releases | 1 | Economics and Macroeconomics | Italy | Active — core primary source |
| `openai_news` | OpenAI News | 1 | Artificial Intelligence | Global | Active — retain; independent AI gap remains |
| `tech_eu` | Tech.eu | 2 | None | Europe | Active — validated Sifted replacement |

All seven current sources use public RSS and require no paid API or private credentials for collection.

---

# Current Source Roles

## BBC News World

Broad global-news safety net.

Strategic status: retain during expansion.

## BBC News Business

Broad accessible business reporting.

Strategic status: likely replace after stronger business/markets sources are technically validated.

## European Central Bank

Primary monetary-policy and financial-system evidence.

Strategic status: core.

## European Commission Highlighted News

Primary EU policy evidence.

Strategic status: retain, but article-level filtering should keep routine communications out.

## Istat Press Releases

Primary Italian macroeconomic evidence.

Strategic status: core.

## OpenAI News

Primary OpenAI/company evidence.

Strategic status: retain as one AI primary source, not the whole AI information universe.

## Tech.eu

European startup/VC and technology specialist reporting.

Strategic status: active Sifted replacement; monitor noise and classification recall without a source default.

---

# Sifted Replacement Decision

Sifted is no longer an active production source.

## Why It Was Originally Useful

- European startup coverage;
- VC coverage;
- specialist reporting;
- strong thematic fit.

## Production Problem

- selected stories could require Sifted Pro;
- no approved Bocconi direct Sifted Pro access was established;
- public feed descriptions were missing in the direct comparison;
- thin report entries therefore often required click-through exactly when the article could be inaccessible.

## Direct Comparison

```text
Tech.eu: 20 items, 20 descriptions, average ≈ 203 characters
Sifted:  24 items, 0 descriptions
```

## Decision

> **Replace Sifted with Tech.eu.**

The replacement preserves European startup/VC discovery while improving public context and follow-up usability without adding cost or collector complexity.

No paywall bypass or Sifted Pro scraping should be introduced.

---

# Source-Default Domain Policy

A source default is classification evidence, not a publisher category.

Use a default only when essentially every item in the selected feed genuinely belongs to that domain.

## Current No-Default Sources

```text
BBC News World
BBC News Business
European Central Bank
European Commission Highlighted News
Tech.eu
```

## Current Narrow Defaults

```text
Istat Press Releases → Economics and Macroeconomics
OpenAI News          → Artificial Intelligence
```

Tech.eu has no Startups/VC default because its general feed is broader than that domain.

Earlier broad defaults inflated classifications and scores. The rule remains:

> **Use a source default only when it represents a genuine source-wide topical guarantee.**

---

# Classification Policy

Classification currently searches configured keywords in:

- title;
- description.

Source defaults are added first where applicable.

## Keyword Expansion Rule

Do not copy broad conceptual vocabularies directly into production.

Use:

```text
observe missed/weak real records
→ propose candidate keywords
→ simulate against real records
→ inspect false positives
→ retain only justified terms
→ rerun report
→ inspect product quality
```

Keyword matches affect both classification and relevance score, so careless synonym expansion can inflate scores.

Phase 4 demonstrated this with acquisition variants: multiple related terms can match one story and generate multiple score points.

## Current Evidence-Backed Phase 4 Changes

Added:

```text
Global Politics / Geopolitics
- tariffs

Companies / Corporate Strategy
- acquired

Startups / VC
- early-stage fund
- funding market
```

Removed:

```text
Startups / VC
- startup
```

These changes were tested against real Tech.eu examples and a three-day 114-record production regression corpus.

---

# Ranking Policy

Current formula:

```text
source-tier score
+ 2 × assigned domains
+ 1 × matched keywords
```

Ranking remains deterministic and explainable.

The formula is provisional.

Do not compensate for bad source defaults or classification evidence by increasing ranking sophistication.

---

# Duplicate Policy

Current exact duplicate reduction uses:

1. normalized URL;
2. normalized title.

The first deterministic occurrence is retained.

Near-duplicate clustering is not implemented.

Add it only if repeated production reports demonstrate material duplication that exact matching cannot solve.

---

# Language Policy

Target languages:

- English;
- Italian.

Current active automated feeds are English-language.

If Italian-language sources are introduced:

- test Italian classification examples;
- add Italian keywords only when evidence justifies them;
- preserve original titles;
- do not make automated translation a core dependency.

---

# Source Diversity Policy

A useful report should not be unnecessarily dominated by one publisher, source tier, geography or source type.

Monitor:

- publisher concentration;
- domain concentration;
- primary vs secondary evidence;
- unusually sparse reports;
- repeated empty domains.

Do not introduce artificial quotas merely because one day is sparse.

Source diversity should improve because coverage improves.

---

# Milan/Bocconi Opportunity-Source Policy

Milan/Bocconi monitoring requires stronger selectivity than generic news.

A useful opportunity should offer meaningful:

- learning;
- networking;
- career information;
- research exposure;
- competition exposure;
- startup/innovation access;
- project experience.

Potential metadata may eventually include:

```text
opportunity_name
organiser
deadline
event_date
location
domain
application_url
source_url
```

Do not create a separate opportunity database unless actual source metadata and repeated user value require it.

---

# Copyright and Public-Repository Policy

The repository may store permitted metadata such as:

- titles;
- URLs;
- publication timestamps;
- source identity;
- limited feed-provided descriptions;
- classification metadata;
- relevance scores;
- run metadata.

The repository must not store:

- complete copyrighted articles;
- substantial copied passages;
- authenticated premium article bodies;
- private newsletter text;
- private email content;
- licensed database full text;
- credentials;
- authentication tokens.

When uncertain:

> **Store less content and preserve provenance plus the original link.**

---

# Bocconi Licence Boundary

The production system must never:

- embed Bocconi credentials;
- automate OpenAthens authentication;
- scrape authenticated FT, WSJ, NYT, Economist or Il Sole 24 Ore content merely because the user can read it;
- scrape Factiva, Nexis or Business Source Ultimate;
- automate Bloomberg/LSEG/FactSet/Capital IQ/Aida extraction without explicit permitted interfaces;
- redistribute restricted full text into the public repository.

A Bocconi-accessible premium publication may become a production source only through a separate public or automation-compatible endpoint.

The Premium Bocconi Exception changes the acceptable **reader workflow**, not the credential boundary.

---

# Source Lifecycle

Conceptual lifecycle:

```text
Candidate
→ Approved for Test
→ Active
→ Monitoring
→ Disabled
→ Removed
```

Not every lifecycle state needs a runtime configuration field.

Current examples:

```text
Tech.eu
→ Active
→ early production monitoring

Sifted
→ Removed from production
→ retained only as historical decision evidence
```

---

# Source Expansion Workflow

For every source candidate:

## 1. Strategic Need

Confirm the information gap and career/user value.

## 2. Policy Review

Confirm:

- source role;
- tier;
- access model;
- automation suitability;
- likely metadata richness;
- reader accessibility.

## 3. Technical Probe

Inspect:

- endpoint availability;
- HTTP behaviour;
- redirects;
- timestamps;
- descriptions;
- entry count;
- malformed records.

## 4. Actual Collector Test

Run through the production collector.

## 5. Normalisation Test

Confirm records normalize correctly.

## 6. Classification Review

Inspect:

- correct domains;
- source-default suitability;
- relevant unclassified items;
- false positives;
- likely score inflation.

## 7. Report Contribution

Inspect:

- usefulness;
- noise;
- repetition;
- context richness;
- source concentration;
- accessibility.

## 8. Production Approval

Only then:

- edit configuration;
- update relevant tests;
- run targeted tests;
- run full suite;
- run real pipeline;
- inspect report;
- inspect diff;
- commit.

---

# Current Resolved Information Decisions

## Current Implemented Domains

```text
Global Politics and Geopolitics
Economics and Macroeconomics
Financial Markets
Companies and Corporate Strategy
Artificial Intelligence
Technology and Software
Startups and Venture Capital
Europe and the European Union
```

## Current Active Sources

```text
BBC News World
BBC News Business
European Central Bank
European Commission Highlighted News
Istat Press Releases
OpenAI News
Tech.eu
```

## Completed Source Replacement

```text
Sifted → Tech.eu
```

Decision date: 17 August 2026.

## Current Source Defaults

```text
BBC News World                → none
BBC News Business             → none
European Central Bank         → none
European Commission           → none
Istat Press Releases          → Economics and Macroeconomics
OpenAI News                   → Artificial Intelligence
Tech.eu                       → none
```

## Financial Markets

**Decision:** implemented.

## Italy

**Decision:** strategically approved; implementation pending technical source validation.

## Milan and Bocconi

**Decision:** validated product requirement; implementation pending source/architecture validation.

## Multi-Domain Records

**Decision:** supported.

## Primary Report Placement

**Decision:** one report placement per story; secondary domains displayed as metadata.

## Unclassified Records

**Decision:** preserve in processed data, omit from main report by default.

## Report Limits

```text
maximum items per domain = 5
maximum total items      = 30
```

These are upper bounds, not targets.

## Description Length

Current configured maximum:

```text
300 characters
```

This remains temporary pending richer-report design.

## Collection Window

Current CLI default:

```text
previous 24 hours relative to actual execution
```

A fixed reporting cutoff remains an open design question because scheduled GitHub Actions may start late.

## Missing Publication Timestamp

**Decision:** exclude from collection-window eligibility.

Do not silently substitute retrieval time.

## Premium Sources

**Decision:** paywall alone is not disqualifying.

Preferred sources remain fully accessible and metadata-rich.

The Premium Bocconi Exception may be approved source by source when unusual strategic value justifies thinner automated context and the user can legitimately open the article through Bocconi.

---

# Current Strategic Source-Audit Priorities

The Career Agent strategic audit has been completed.

Highest-priority candidates for Development technical audit:

1. Financial Times;
2. Il Sole 24 Ore;
3. Reuters;
4. Bank of Italy;
5. later, B4i;
6. later, Bocconi Career Services;
7. later, Bocconi News & Events.

Supplemental candidates only if they solve demonstrated gaps:

- WSJ;
- Italian Tech Alliance;
- Anthropic News;
- Google DeepMind News;
- Bruegel;
- Fintech District;
- EU-Startups;
- selected Comune di Milano sources.

Manual/deep-reading sources include:

- The Economist;
- Foreign Affairs;
- Harvard Business Review;
- Economia & Management;
- institutional databases and professional financial platforms.

Do not add all strategically good publications to production.

The objective remains the smallest strong source universe.

---

# Open Information Decisions

## Future Source Universe

No fixed source-count target.

Technical audit must continue source by source.

## Italy Source Architecture

Validate whether Il Sole 24 Ore plus Istat plus Bank of Italy provides sufficient coverage before adding more Italian sources.

## Milan and Bocconi Source Architecture

Test the smallest high-value public source set, beginning with:

- B4i;
- Bocconi Career Services;
- Bocconi News & Events.

## Additional Independent AI Coverage

Evaluate only after broader cross-domain sources such as FT/Reuters are tested.

## BBC Business

Keep temporarily.

Strategically likely to be replaced if stronger business/markets sources validate.

## Publisher Concentration

Continue observing reports.

Do not add concentration penalties or quotas without repeated evidence.

## Richer Context

Validated product requirement, but implementation remains deferred until source/domain correction is sufficiently mature.

## Ranking Weights

Remain provisional.

## Article-Level Geography

Not implemented.

## Content Type

Not implemented.

## Near-Duplicate Clustering

Not implemented.

## Multi-Source Story Clustering

Not implemented.

## Long-Term Source Health History

Not implemented; per-run health remains sufficient for now.

---

# Information Quality Decision Rules

Before adding a source, taxonomy rule or new classification dimension, ask:

1. What observed problem does it solve?
2. Is the problem validated?
3. Can a simpler source/configuration change solve it?
4. Does it improve actual report usefulness?
5. What false positives could it create?
6. What false negatives remain?
7. Does it preserve zero recurring cost?
8. Does it preserve low daily manual work?
9. Does it preserve credential safety?
10. Does it preserve copyright/public-repository safety?
11. What maintenance does it add?
12. How will success be validated?

Preferred pattern:

```text
observe real problem
→ isolate cause
→ compare simplest solutions
→ test smallest justified change
→ rerun
→ inspect information quality
→ stop at stable checkpoint
```

---

# Current Information-Policy Limitations

Known limitations:

- eight of ten target domains are implemented;
- Italy is not yet implemented as a topic domain;
- Milan/Bocconi is not yet implemented;
- all active automated feeds are currently English-language;
- full bilingual behaviour is unvalidated;
- article-level geography is not implemented;
- content type is not implemented;
- entity tracking is not implemented;
- near-duplicate clustering is not implemented;
- multi-source story clustering is not implemented;
- long-term source-health history is not implemented;
- ranking weights remain provisional;
- keyword lists remain conservative;
- some strategically relevant records remain unclassified;
- public description richness still varies by source;
- future Premium Bocconi Exception sources may intentionally provide thinner automated context;
- source concentration can vary materially by day;
- the rolling collection window depends on actual scheduled execution time;
- personal Bocconi access is not represented as runtime credentials and must remain outside production authentication.

These are maturity limits, not a list of features that must all be built.

---

# Current Information-Quality Priorities

## 1. Continue High-ROI Source Audits

The first weak-source correction is complete: Sifted was replaced by Tech.eu.

Next priority:

> **Financial Times technical audit.**

Then, if still justified:

- Il Sole 24 Ore;
- Bank of Italy;
- Reuters.

## 2. Preserve the Current Stable Checkpoint

Do not mix unrelated source changes into the Tech.eu / Financial Markets checkpoint.

## 3. Implement Remaining Approved Domains Deliberately

- Financial Markets: implemented;
- Italy: approved, pending source validation;
- Milan/Bocconi: required, pending source/architecture validation.

## 4. Improve Source Diversity Only Through Better Coverage

No artificial quotas.

## 5. Design Richer Report Context After Source Correction

The report should eventually provide materially more context below the relevance score.

Do not redesign summarization while the source universe is still changing materially.

## 6. Revisit Ranking Only If Upstream Corrections Are Insufficient

Prefer better sources and better classification evidence over more complex ranking logic.

---

# Current Status

**Phase:** Phase 4 — Source and Domain Correction / Expansion.

**Validated current checkpoint:**

- seven active public RSS sources;
- eight active topic domains;
- Sifted replaced by Tech.eu;
- Tech.eu has no blanket source default;
- Financial Markets implemented conservatively;
- four evidence-backed keyword additions;
- generic `startup` keyword removed;
- 110/110 automated tests passing;
- real 17 August 2026 pipeline run successful;
- resulting report manually inspected;
- no recurring monetary cost introduced;
- no private credentials introduced;
- no authenticated premium-content ingestion introduced.

**Next highest-ROI action:**

> **Audit Financial Times technically under the source scorecard and Premium Bocconi Exception rules before making another production change.**

After the source/domain universe is sufficiently corrected:

> **begin the dedicated richer-report design phase.**

---

# Changelog

## 2026-08-17 — Tech.eu Replacement and Financial Markets Activation

- Incorporated the Career Agent strategic source/domain audit into Phase 4 priorities.
- Replaced Sifted with Tech.eu after controlled comparison.
- Recorded Tech.eu 20/20 description availability versus Sifted 0/24 in the tested samples.
- Activated Tech.eu as Tier 2 Europe with `default_domains: []`.
- Added `acquired` to Companies and Corporate Strategy after real M&A misses.
- Added `early-stage fund` and `funding market` to Startups and Venture Capital after controlled simulation.
- Removed generic `startup` after it promoted a low-value Tech.eu profile.
- Added `tariffs` after a relevant geopolitical trade story remained unclassified.
- Implemented Financial Markets as the eighth active domain with a conservative first keyword set.
- Validated taxonomy changes against 114 stored production records.
- Confirmed 110/110 automated tests passed.
- Ran the real pipeline successfully on 17 August 2026 and manually inspected the resulting report.
- Recorded that high unclassified share is not itself a defect when excluded records are correctly low-value or out of scope.
- Recorded Milan and Bocconi Ecosystem as a validated product requirement.
- Added the narrow Premium Bocconi Exception while preserving the prohibition on authenticated automated ingestion.
- Preserved zero recurring cost, deterministic processing, public-repository safety and negligible daily manual work.

## 2026-08-14 — Source Accessibility, Bocconi Access and Expansion Policy

- Reconciled source policy with completed Phase 3 automation.
- Added metadata richness and reader accessibility as explicit source-quality dimensions.
- Added the two-axis distinction between automation suitability and reader accessibility.
- Recorded Bocconi Direct, SearchLib, Database and Public Web access modes.
- Recorded the three-layer information-access model.
- Prohibited production use of Bocconi credentials and authenticated premium scraping.
- Added the controlled source-expansion workflow.
- Marked Sifted for explicit review after production accessibility and metadata problems.
- Preserved richer-report implementation as a later phase after source/domain correction.

## 2026-08-11 — Phase 2 Real-Source Taxonomy and Source-Policy Validation

- Expanded the implementation from one sample source to seven validated public RSS sources.
- Expanded the implemented taxonomy from two to seven domains.
- Added the rule that source defaults represent genuine source-wide topical evidence rather than publisher categories.
- Removed broad defaults from BBC World, BBC Business, ECB and European Commission.
- Restricted Istat to Economics and Macroeconomics and OpenAI to Artificial Intelligence.
- Added `war`, `conflict` and `parliament` after real-record testing.
- Rejected overly broad politics keywords after false-positive review.
- Preserved conservative classification, exact deduplication and public-repository safety.

## 2026-08-11 — Phase 1 Taxonomy and Source-Policy Reconciliation

- Recorded implemented classification, ranking and duplicate policies.
- Replaced source-count targets with a smallest-credible-source strategy.
- Kept advanced geography, entity, content-type and clustering logic behind evidence from real reports.

## Initial Baseline

- Established the ten target topic domains.
- Defined source tiers and source inclusion/exclusion criteria.
- Defined classification, ranking and duplicate-reduction policy.
- Defined copyright and public-repository boundaries.