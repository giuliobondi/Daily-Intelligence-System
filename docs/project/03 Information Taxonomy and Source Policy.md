# Daily Intelligence System — Information Taxonomy and Source Policy

> **Purpose**
>
> Define what information the Daily Intelligence System should collect, how it should classify that information, which sources are acceptable, and which rules govern source selection, accessibility, storage and public presentation.
>
> This document is the canonical quality-control and source-governance policy for information entering the system.

> **Primary question**
>
> *What information should the system collect, from which sources, and under which classification, accessibility and quality rules?*

> **Update frequency**
>
> Update when monitored domains, source-selection rules, accessibility assumptions, metadata requirements, source-audit conclusions or source-governance policies materially change.

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

The system should prefer a smaller set of strong, differentiated sources over broad but noisy coverage.

A technically compatible source is not automatically a good product source.

A prestigious source is not automatically a viable production source.

A source should be added because it closes an information-function gap, not merely because it increases publisher count.

---

# Current Implementation Status

The deterministic information-processing model is implemented and production-automated.

Current production configuration:

- eight active public RSS sources;
- nine active topic domains;
- deterministic title-and-description keyword rules;
- optional source-default domains;
- support for source-defined domains with empty keyword lists when explicitly justified;
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
7. Tech.eu;
8. Tech Europe Foundation.

Current implemented domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Financial Markets;
4. Companies and Corporate Strategy;
5. Artificial Intelligence;
6. Technology and Software;
7. Startups and Venture Capital;
8. Europe and the European Union;
9. Milan and Bocconi Ecosystem.

Still unimplemented as a dedicated domain:

- Italy.

Phase 4 has now produced several validated information-quality corrections and source-governance decisions:

- Sifted was replaced by Tech.eu;
- Tech.eu uses no blanket source-default domain;
- Financial Markets was implemented as the eighth domain;
- `tariffs`, `acquired`, `early-stage fund` and `funding market` were added after real-record testing;
- the generic Startups/VC keyword `startup` was removed after it promoted weak stories too easily;
- multilingual classification was corrected so intentional uppercase keywords such as `AI` are case-sensitive while lowercase keywords remain case-insensitive;
- this removed false Artificial Intelligence matches from the Italian word `ai` while preserving historical English AI recall;
- Financial Times, Il Sole 24 Ore, Bank of Italy, Reuters, B4i, Bocconi sources, Tech Europe Foundation and Italian Tech Alliance were audited;
- Tech Europe Foundation was implemented as the first production source for the Milan and Bocconi Ecosystem;
- `milan_bocconi_ecosystem` is currently source-defined with an empty keyword list;
- a real eight-source production-equivalent pipeline run completed successfully after the TEF integration;
- broader strategic source research identified a new domain-gap-driven audit queue.

The current priority remains:

> **Continue correcting and expanding sources and domains before implementing richer report-context logic.**

---

# Taxonomy Principles

## Configurable

Domains, keywords, source tiers and source defaults belong in configuration rather than being scattered through processing code.

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

A high unclassified share is not itself a defect.

The correct question is:

> **Are important stories being missed or weak stories being promoted?**

not:

> **Is the classification rate high?**

## Broad but Bounded

The system should not become a generic global-news taxonomy.

## Independent Dimensions

Topic, geography, source tier, reader accessibility and content type are conceptually separate.

Only topic classification and source tier are currently implemented at article level.

Source-level geographic scope exists in configuration.

## Information Functions Before Publisher Count

Source expansion should solve missing information functions.

Examples of distinct information roles include:

- primary institutional evidence;
- market/company reporting;
- independent analysis;
- specialist ecosystem intelligence;
- professional opportunity discovery;
- frontier-lab primary evidence.

Do not add several publications simply because they cover the same subject.

The operating principle is:

> **Correct information-function gaps before correcting publisher-count gaps.**

---

# Target Topic Taxonomy

The strategic target remains ten macroareas.

Nine are implemented.

Italy remains strategically approved but awaits a sufficiently strong source architecture and tested classification logic.

Milan and Bocconi Ecosystem is now implemented in a conservative first production version through Tech Europe Foundation.

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

Broad terms such as `government`, `defence`, `president` and `prime minister` were previously tested but rejected because they produced ambiguous or low-value matches.

Current production coverage is mainly BBC World plus selective European Commission spillover.

This is acceptable for now but remains publisher-concentrated.

The gap is lower-priority than Financial Markets, Companies, Italy and independent AI coverage.

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

ECB and Istat provide strong primary evidence, while the European Commission adds policy context.

Current coverage remains weighted toward Europe and Italy.

Highest-priority missing information roles include:

- US/global monetary and financial-condition evidence;
- independent European and Italian economic interpretation.

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
- major market reactions to macro or company developments;
- corporate financing conditions;
- material financial-system developments.

### Exclude or Deprioritise

- daily index recaps;
- isolated minor price moves;
- trading tips;
- technical-analysis commentary;
- price predictions;
- generic market colour without causal explanation.

### Current Status

**Implemented — conservative taxonomy, weak source coverage.**

Initial configured keywords include:

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

Broad terms such as `market`, `stocks`, `shares`, `bonds`, `rates`, `bank` and `investment` remain intentionally excluded.

The major current limitation is upstream:

> **There is no dedicated production Financial Markets source.**

Financial Markets is therefore one of the highest-priority source-expansion gaps.

Current strategic candidates for Development audit include:

1. Nasdaq;
2. Federal Reserve Board;
3. later MEF Treasury;
4. later ESMA;
5. later BIS;
6. later Euronext.

Do not turn the system into a real-time price monitor.

The desired information is causal and decision-relevant market intelligence.

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
- competitive shifts;
- corporate financing when strategically meaningful.

### Exclude or Deprioritise

- routine product promotion;
- minor executive appointments;
- small operational updates;
- marketing announcements without strategic significance.

### Current Status

**Implemented — source coverage remains weak.**

No broad current source receives a Corporate Strategy default.

Phase 4 added `acquired` after real Tech.eu records showed that the noun `acquisition` alone missed clear M&A stories.

Current production coverage is mainly incidental through BBC Business and Tech.eu.

This is a severe information-function gap.

Strategic candidates include:

- Nasdaq;
- MIMIT;
- Lavoce.info;
- later targeted SEC EDGAR use if a specific company/form universe is justified.

No clean source currently replicates the integrated global corporate-reporting role of Financial Times or Reuters.

Do not fill that residual gap with lower-quality sources merely for completeness.

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

Current coverage remains too dependent on one vendor.

The desired future information structure is:

```text
OpenAI
→ primary company/product evidence

Google DeepMind
→ second frontier-lab primary source

independent technology/AI reporting
→ external scrutiny and interpretation
```

Ars Technica and Google DeepMind are current strategic audit candidates.

Do not add every AI lab merely to increase source count.

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

Tech.eu provides the main specialist production layer.

OpenAI and BBC contribute selectively.

Independent systems/software reporting remains a useful but lower-priority gap than Financial Markets, Companies and Italy.

Ars Technica is the current strongest strategic candidate for this missing role.

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

Both feeds collected and normalised successfully.

The decision therefore turned on product quality, accessibility and metadata richness rather than basic technical compatibility.

Tech.eu uses:

```yaml
default_domains: []
```

because its general feed spans startups, AI, corporate strategy, technology and European policy.

Phase 4 added:

- `early-stage fund`;
- `funding market`.

The generic keyword `startup` was removed because it promoted weak profiles too easily.

The goal is meaningful startup/VC pattern recognition, not funding-round volume.

### Italian Tech Alliance

Italian Tech Alliance has completed basic technical evaluation and should not be re-audited from zero.

Validated findings:

- official public RSS works;
- 20/20 tested entries normalised successfully;
- timestamps and links were complete;
- descriptions are extremely thin;
- much of the feed is press clipping from third-party publications;
- repeated records may cover the same underlying VC statistics;
- real value exists in Italian VC, startup policy, ecosystem statistics and professional programmes;
- the Venture Academy feed item demonstrated genuine opportunity value;
- `round` and `scaleup fund` passed historical regression as precise Startups/VC candidate keywords.

Current status:

> **Production-readiness candidate — basic technical audit complete.**

Do not introduce near-duplicate clustering merely to support Italian Tech Alliance unless repeated production evidence justifies it.

Later differentiated candidates include Invest Europe and AIFI only if a real private-capital gap remains.

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

Primary institutional evidence is strong.

The main missing information role is:

> **independent economic and policy interpretation.**

Bruegel is the current strongest strategic candidate.

ESMA may later add specialised market/regulatory evidence.

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
- technology and startups;
- industrial investment and restructuring.

### Exclude or Deprioritise

- general national news without economic or professional significance;
- sport;
- celebrity;
- crime;
- routine party conflict.

### Current Status

**Strategically approved; dedicated domain implementation pending.**

Istat already contributes Italian macro evidence.

The current production system does not yet provide a sufficiently complete Italian economic/business information ecosystem.

Research has shown that Italy should not be solved by one generic national newspaper.

The desired differentiated architecture is currently:

```text
Istat
→ primary statistics

MIMIT
→ industrial policy, restructuring and company-policy evidence

Lavoce.info
→ independent economics/business interpretation

Assolombarda
→ Milan/Lombardy firms, economy and industry

Italian Tech Alliance
→ VC/startup ecosystem

Bank of Italy BDS later
→ structured financial-system/statistical layer
```

Il Sole 24 Ore remains strategically valuable and in standby.

MEF Treasury and AIFI are possible later specialist additions.

Current highest-priority Development audits for Italy are:

1. MIMIT;
2. Lavoce.info;
3. Assolombarda.

---

## 10. Milan and Bocconi Ecosystem

### Scope

High-value professional ecosystem intelligence connected to Milan, Bocconi and relevant local communities.

### Include

- recruiting and employer events;
- finance, consulting, AI/data, technology and startup events;
- entrepreneurship programmes and startup calls;
- research opportunities;
- competitions;
- high-value public lectures;
- Milan startup, VC and fintech developments;
- innovation programmes;
- relevant firm/industry developments;
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

**Implemented — conservative first production version.**

Tech Europe Foundation is the first active source supporting this domain.

Current configuration:

```text
Tech Europe Foundation
→ Tier 1
→ Milan and Bocconi Ecosystem source default
→ no topic keywords required for the domain
```

The domain currently has:

```yaml
keywords: []
```

This is intentional.

TEF's selected News feed was validated as a narrow enough institutional/professional ecosystem stream for source identity itself to act as classification evidence.

The first implementation therefore required no:

- custom scraper;
- authenticated Bocconi access;
- opportunity database;
- event-specific pipeline;
- deadline engine;
- source-specific collector logic.

TEF's News RSS provides rich descriptions, timestamps and links, but publication is relatively sparse and the feed does not expose every current TEF opportunity shown elsewhere on the site.

Current automated coverage is therefore strongest for:

- entrepreneurship;
- startup/deep-tech ecosystem;
- founder/programme activity;
- TEF/B4i-linked innovation;
- university-linked startup activity.

Remaining important gaps include:

- finance recruiting;
- consulting recruiting;
- employer events;
- complete opportunity/deadline coverage;
- selected high-value public lectures;
- broader established-company and industrial ecosystem intelligence.

Bocconi Career Services remains strategically extremely valuable but cannot be treated as a complete automated production source under current constraints because key infrastructure lives inside authenticated yoU@B / JobGate.

Do not automate authenticated Bocconi access.

Current strongest complementary strategic candidate:

- Assolombarda.

Later candidates include:

- ISPI;
- Camera di Commercio Milano Monza Brianza Lodi;
- Fintech District if a clean structured path proves valuable.

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
- original research publications;
- official programme/institutional sources.

Strength:

- closest to primary evidence.

Limitation:

- can be promotional, routine or context-poor.

## Tier 2 — High-Quality Reporting

Established journalistic or specialist organisations providing original reporting, verification or useful professional context.

Tier 2 does not imply automatic production eligibility.

The Sifted replacement decision is the clearest current example: Sifted remained strategically relevant but was replaced because Tech.eu offered better metadata and follow-up usability.

## Tier 3 — Specialist Analysis

Specialist organisations, research groups, industry associations, venture organisations and focused publications that do not fit the Tier 2 role.

Approve individually.

Italian Tech Alliance is currently best treated conservatively within this category unless later evidence supports another tier.

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

> **Fix upstream evidence before changing ranking weights.**

TEF ranking was explicitly reviewed after implementation.

Most TEF records receive a baseline score of:

```text
Tier 1 source       = 4
Milan/Bocconi domain = 2
Total               = 6
```

The current per-primary-domain report cap limits the domain to five displayed items.

No ranking change is currently justified by TEF.

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

Corriere della Sera remains a special archive/current-edition case rather than confirmed unrestricted premium-site access.

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

Public accessibility is favourable but still does not itself prove scraping permission.

Prefer structured public endpoints.

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

Current strongest strategic sources considered under this exception:

- Financial Times;
- Il Sole 24 Ore.

Both have now been technically/policy audited.

Neither is currently active.

Their detailed status is recorded in the Source Audit Decision Register below.

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

Descriptions and other public context are explicit product-quality dimensions.

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

Reject, disable, defer or replace a source when one or more of the following materially apply:

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
- an alternative source provides materially better accessibility, metadata or reliability;
- implementation requires a new processing paradigm before the information need is sufficiently validated.

Prefer replacing or deferring a weak/incompatible source over adding source-specific complexity.

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

Allowed recommendation language includes:

```text
Candidate
Approve for controlled test
Production-readiness candidate
Active
Monitoring
Standby — access/persistence
Standby — architecture
Manual/private layer
Legacy/superseded
Disable
Remove
Reject under current constraints
Research further
```

Do not reduce the scorecard to a numeric score unless evidence later shows that doing so improves decisions.

---

# Current Production Source Universe

| Source ID | Source | Tier | Default Domains | Geographic Scope | Policy Status |
|---|---|---:|---|---|---|
| `bbc_world` | BBC News World | 2 | None | Global | Active — retain during expansion |
| `bbc_business` | BBC News Business | 2 | None | Global | Active — temporary broad business layer |
| `ecb_press` | European Central Bank | 1 | None | EU; Euro Area | Active — core primary source |
| `ec_highlights` | European Commission Highlighted News | 1 | None | European Union | Active — primary EU policy evidence |
| `istat_press_en` | Istat Press Releases | 1 | Economics and Macroeconomics | Italy | Active — core primary source |
| `openai_news` | OpenAI News | 1 | Artificial Intelligence | Global | Active — one AI primary source |
| `tech_eu` | Tech.eu | 2 | None | Europe | Active — validated Sifted replacement |
| `tech_europe_foundation` | Tech Europe Foundation | 1 | Milan and Bocconi Ecosystem | Europe; Italy; Milan | Active — first Milan/Bocconi source |

All current sources use public RSS and require no paid API or private credentials for collection.

---

# Current Source Roles

## BBC News World

Broad global-news safety net.

Strategic status:

> Retain during expansion.

Main limitation:

- publisher concentration in Global Politics.

Do not add another generic world-news source until higher-priority gaps are addressed.

## BBC News Business

Broad accessible business reporting.

Strategic status:

> Retain temporarily.

It may become redundant once stronger Markets and Companies sources are technically validated.

Do not remove it before replacement coverage is demonstrated in real reports.

## European Central Bank

Primary euro-area monetary-policy and financial-system evidence.

Strategic status:

> Core.

## European Commission Highlighted News

Primary EU policy evidence.

Strategic status:

> Retain.

Classification should continue filtering routine communications.

## Istat Press Releases

Primary Italian macroeconomic evidence.

Strategic status:

> Core.

Istat alone is not sufficient for the future Italy information architecture.

## OpenAI News

Primary OpenAI/company evidence.

Strategic status:

> Retain as one AI primary source.

It must not define the entire AI information universe.

## Tech.eu

European startup/VC and technology specialist reporting.

Strategic status:

> Active Sifted replacement.

Monitor noise and classification recall without a source default.

## Tech Europe Foundation

Primary source for TEF programmes, entrepreneurship activity and associated Milan/Bocconi innovation ecosystem developments.

Strategic status:

> Active first Milan/Bocconi source.

It does not by itself satisfy the complete Milan/Bocconi requirement.

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
Istat Press Releases       → Economics and Macroeconomics
OpenAI News                → Artificial Intelligence
Tech Europe Foundation     → Milan and Bocconi Ecosystem
```

Tech.eu has no Startups/VC default because its general feed is broader than that domain.

TEF has a Milan/Bocconi default because the specific selected News feed was validated as belonging to that professional ecosystem even when individual stories do not contain generic topical keywords.

Earlier broad defaults inflated classifications and scores.

The rule remains:

> **Use a source default only when it represents a genuine source-wide guarantee for the selected feed.**

---

# Empty-Keyword Domain Policy

A domain may use an empty keyword list when:

- the domain is still meaningful and user-validated;
- classification evidence comes from one or more narrow source defaults;
- invented generic keywords would reduce precision;
- the behavior is explicit in configuration and tests.

Current example:

```text
Milan and Bocconi Ecosystem
keywords: []
```

This capability must not become a shortcut for broad source-driven classification.

Empty-keyword domains remain subject to the same evidence and report-quality requirements as keyword-defined domains.

---

# Classification Policy

Classification currently searches configured keywords in:

- title;
- description.

Source defaults are added where applicable.

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

## Keyword Case Policy

Configured keywords now use the following deterministic convention:

```text
keyword containing only lowercase characters
→ case-insensitive match

keyword intentionally containing uppercase characters
→ case-sensitive match
```

This convention was introduced after Italian-language testing revealed that the English acronym `AI` was being confused with the common Italian word `ai`.

Production configuration now uses:

```text
AI
```

rather than:

```text
ai
```

The change was validated against historical English AI records and current Italian-language test records.

It preserved useful English AI recall while removing false Italian classifications.

Do not introduce language detection or NLP while this simpler deterministic rule remains sufficient.

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

Changed:

```text
Artificial Intelligence
- ai
+ AI
```

Additional Italian-language candidates have been tested for future source use but should not enter production until their associated source is approved.

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

Report selection currently applies:

```text
maximum items per primary domain = 5
maximum total items              = 30
```

These are upper bounds, not targets.

TEF ranking behavior was reviewed after implementation.

No source-specific ranking rule is currently justified.

---

# Duplicate Policy

Current exact duplicate reduction uses:

1. normalized URL;
2. normalized title.

The first deterministic occurrence is retained.

Near-duplicate clustering is not implemented.

Italian Tech Alliance testing demonstrated a plausible future near-duplicate problem because multiple press-clipping records can describe the same underlying VC dataset.

That evidence is not yet sufficient to justify new clustering logic.

Add near-duplicate handling only if repeated production reports demonstrate material product degradation.

---

# Language Policy

Target languages:

- English;
- Italian.

The active production universe is currently primarily English-language.

Italian-language source testing has now occurred through Il Sole 24 Ore and Italian Tech Alliance.

If Italian-language sources are introduced:

- test Italian classification examples;
- add Italian keywords only when evidence justifies them;
- preserve original titles;
- use the `AI` case-sensitive convention;
- do not make automated translation a core dependency.

Full bilingual production behaviour remains only partially validated.

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

Current known concentration problems include:

- Financial Markets lacks a dedicated source;
- Companies/Corporate Strategy relies heavily on incidental coverage;
- AI is too dependent on OpenAI as a primary source;
- Startups/VC relies mainly on Tech.eu;
- Italy lacks a complete source architecture;
- Milan/Bocconi currently relies on TEF.

These are information-function gaps, not a requirement for equal source counts.

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

Current experience shows that publication time and opportunity time can differ materially.

Examples of future opportunity semantics may include:

- application opening date;
- application deadline;
- event date;
- registration deadline.

This does not yet justify a new stateful opportunity subsystem.

The trigger for such a subsystem should be repeated evidence that publication-only reporting causes meaningful opportunities to be missed.

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
- scrape authenticated yoU@B or JobGate;
- redistribute restricted full text into the public repository.

A Bocconi-accessible premium publication may become a production source only through a separate public or automation-compatible endpoint.

The Premium Bocconi Exception changes the acceptable **reader workflow**, not the credential boundary.

---

# Source Lifecycle

Conceptual lifecycle:

```text
Candidate
→ Approved for Test
→ Production-Readiness Candidate
→ Active
→ Monitoring
→ Standby / Disabled
→ Removed
```

Not every lifecycle state needs a runtime configuration field.

Additional policy statuses may be used where useful:

```text
Standby — access/persistence
Standby — architecture
Manual/private layer
Legacy/superseded
Rejected under current constraints
```

The runtime `active` field remains simpler than the policy lifecycle.

---

# Source Expansion Workflow

For every source candidate:

## 1. Strategic Need

Confirm the information gap and user/career value.

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

The source-expansion process should now be organised around **domain gaps**, not a linear list of prestigious publications.

---

# Source Audit Decision Register

This register records durable conclusions from completed source research.

Detailed transient probes remain in Git history, tests and development handoffs rather than being duplicated here.

---

## Active Sources and Completed Replacements

### Tech.eu

**Strategic role**

European startup/VC and technology specialist reporting.

**Technical result**

- public RSS validated;
- collector compatible;
- normalisation successful;
- strong description availability;
- no source-specific code required.

**Classification**

```text
default_domains: none
```

**Status**

> **Active.**

**Decision**

Replaced Sifted because Tech.eu offered materially better public metadata and follow-up usability without adding cost or complexity.

---

### Tech Europe Foundation

**Strategic role**

Milan/Bocconi entrepreneurship, innovation, deep-tech and professional ecosystem intelligence.

**Technical result**

- `https://tef.tech/news/feed/` validated;
- standard RSS;
- collector compatible;
- normalisation successful;
- rich descriptions;
- reliable timestamps and links;
- real eight-source pipeline integration successful.

**Classification**

```text
default domain:
Milan and Bocconi Ecosystem
```

Domain keywords remain empty.

**Limitations**

- sparse publication;
- feed is mostly stories/profiles rather than complete opportunity detection;
- some current programmes advertised elsewhere on the site are absent from the News RSS;
- does not cover complete recruiting or Career Services activity.

**Status**

> **Active — first Milan/Bocconi source.**

---

### Sifted

**Strategic role**

European startup/VC reporting.

**Technical result**

Feed technically collected and normalised, but public description metadata was materially inferior to Tech.eu.

**Status**

> **Removed.**

**Reason**

Better production alternative exists.

Do not introduce Sifted Pro scraping or authenticated access.

---

# Completed Premium / Major-Publisher Audits

## Financial Times

**Strategic value**

Very high across:

- Companies;
- Financial Markets;
- Economics;
- Geopolitics;
- Technology.

**Research result**

- official FT RSS infrastructure exists;
- RSS discovery is technically attractive;
- general FT terms allow limited headline/link usage under conditions;
- FT RSS-specific conditions prohibit archiving the feed or its content;
- public webpage scraping/spidering is not an acceptable alternative;
- professional API/headline licensing is not compatible with the current zero-cost architecture.

The Daily Intelligence System deliberately persists:

```text
processed JSONL
daily Markdown
Git history
```

so the RSS archival restriction conflicts with the existing persistence model.

**Status**

> **Standby — access/persistence conflict.**

**Revisit condition**

Reconsider only if a materially different €0 permission or public interface explicitly permits:

- automated discovery;
- deterministic classification/ranking;
- permanent public archive;
- Git repository persistence.

Do not reopen the same RSS analysis without new evidence.

---

## Il Sole 24 Ore

**Strategic value**

Very high for:

- Italy;
- Companies;
- Financial Markets;
- business/industry;
- policy.

**Technical result**

Public RSS endpoints tested successfully.

Strongest tested feeds:

```text
Economia
Finanza
```

`Italia` was substantially noisier.

Collector and normalizer compatibility passed without source-specific logic.

Descriptions and timestamps were usable.

Italian classification was technically feasible.

Validated candidate Italian topical terms included examples such as:

```text
Companies / Corporate Strategy
- acquisizione
- acquisizioni
- consolidamento

Financial Markets
- cartolarizzazione
- bond
```

These are not active production keywords because the source itself remains inactive.

**Important classifier finding**

Il Sole testing exposed the English `AI` versus Italian `ai` ambiguity and triggered the validated case-sensitive acronym fix.

**Policy concern**

The publisher's RSS/content terms do not provide a sufficiently clean basis for the current permanent public-Git persistence model.

Unlike Financial Times, no equally explicit RSS-specific "do not archive" rule was established, but the persistence/database boundary remains insufficiently clear.

**Status**

> **Standby — strategically strong and technically compatible, but persistence/licensing compatibility is not clean enough.**

This is **not** a permanent rejection.

**Revisit condition**

Revisit if a compliant, low-complexity persistence path becomes available.

---

## Reuters

**Strategic value**

Exceptional across:

- Companies;
- Financial Markets;
- Geopolitics;
- Business;
- Technology;
- AI reporting.

**Research result**

Reuters supports professional machine delivery through licensed systems including API/RSS/FTP-style delivery.

No clean official zero-cost public Reuters news endpoint suitable for the current production architecture was identified.

Scraping Reuters.com or reverse-engineering undocumented internal endpoints is not acceptable.

Third-party Reuters RSS generators are also unsuitable because they add:

- unclear rights;
- third-party reliability risk;
- unknown completeness;
- potential hidden scraping.

**Status**

> **Standby / rejected under current zero-cost constraints.**

**Revisit condition**

Reconsider if Reuters offers a genuinely public automation-compatible feed/API or if project constraints explicitly change.

Do not allow Reuters research to block progress.

---

# Bank of Italy Audit

## Bank of Italy RSS

**Strategic value**

Very high for:

- Italy;
- Economics/Macro;
- Financial Markets.

**Technical result**

Official RSS infrastructure exists.

Tested narrow feeds included:

```text
Financial Market
Italian Economy in Brief
```

Both:

- collected successfully;
- normalised successfully;
- provided valid timestamps and PDF links;
- provided no RSS descriptions.

Narrow source defaults were validated conceptually:

```text
Financial Market
→ Financial Markets

Italian Economy in Brief
→ Economics and Macroeconomics
```

**Limitations**

RSS metadata is thin.

Ordinary publication-content persistence is less clean than reusable statistical data.

**Status**

> **Standby.**

Do not add the RSS feeds merely because they are technically compatible.

---

## Bank of Italy BDS / Statistical Database

**Strategic value**

Very high.

**Research result**

Bank of Italy provides an official application-to-application statistical export system.

The BDS interface supports structured exports such as:

- CSV;
- data;
- metadata;
- domains;
- structure;
- full publication exports.

Relevant statistical areas include:

- Ita-coin;
- banking;
- interest rates;
- public finance;
- government debt;
- borrowing requirement;
- balance of payments;
- financial markets;
- financial conditions.

The Bank's statistical information has a materially cleaner reuse basis than ordinary article/publication content.

**Architecture implication**

A BDS integration would require a different processing path:

```text
fetch selected series
→ parse observations
→ detect new release
→ compare with previous observation
→ distinguish revision from new period
→ apply deterministic significance logic
→ create intelligence event
→ classify/rank/report
```

This is a new statistical-event pipeline, not a normal RSS source.

**Status**

> **Approved future enhancement — deferred architecture.**

**Revisit condition**

Implement only when evidence shows that structured statistical signals justify the additional architecture.

Do not restart basic BDS discovery research.

---

# Milan/Bocconi Source Audits

## B4i — Bocconi for Innovation

B4i is transitioning into / has been superseded by Tech Europe Foundation.

Its historical archive remains useful as calibration evidence for the types of programmes, startup calls and ecosystem intelligence that matter.

No durable RSS route suitable for future production was identified.

**Status**

> **Legacy / superseded by TEF.**

Do not add as a new production source.

---

## Bocconi Career Services / yoU@B / JobGate

**Strategic value**

Extremely high for:

- recruiting;
- finance;
- consulting;
- employer events;
- professional opportunities.

Public Career Services pages expose valuable events and registration windows.

However, complete event infrastructure and registration are partly contained inside authenticated:

```text
yoU@B
JobGate
```

No clean public RSS/API/iCal feed covering the full opportunity universe was identified.

**Status**

> **Manual/private layer.**

Production must not:

- log into yoU@B;
- scrape JobGate;
- embed Bocconi credentials;
- attempt authenticated calendar extraction.

The Daily Intelligence System should aim for the best public structured opportunity detection, not replication of private Career Services.

---

## Bocconi General News / Events

Bocconi's public event universe contains valuable:

- lectures;
- research seminars;
- policy events;
- conferences.

However, it also contains large volumes of:

- admissions activity;
- prospective-student events;
- generic campus activity;
- cultural events;
- low-relevance institutional material.

No clean narrow structured feed was established during the audit.

Automating the general catalogue would require:

- HTML/event crawling;
- event-date semantics;
- aggressive filtering;
- additional maintenance.

**Status**

> **Not suitable for current production architecture.**

Do not build a Bocconi event crawler without stronger evidence.

---

# Italian Tech Alliance Audit

**Strategic value**

High for:

- Italian Startups/VC;
- VC policy;
- innovation ecosystem;
- professional programmes.

**Technical result**

Official public RSS works.

Tested sample:

```text
20 entries
20 timestamps
20 links
20 descriptions
0 normalisation failures
```

Descriptions were very thin, often only identifying an external publication.

The feed includes substantial press-clipping activity and clusters of multiple articles around the same underlying Italian VC data.

**Valuable signals included**

- Italian VC investment statistics;
- Venture Academy;
- Tech Transfer Academy;
- startup-policy developments;
- Scaleup Fund;
- Italian investor ecosystem developments.

**Classification findings**

Current production classifier captured several `venture capital` stories.

Validated candidate terms:

```text
round
scaleup fund
```

Historical regression produced only relevant matches.

**Main unresolved issue**

Report contribution on press-clipping cluster days.

Do not build near-duplicate clustering specifically for this source without repeated production evidence.

**Status**

> **Production-readiness candidate.**

Basic strategic and technical audit is complete.

Do not restart the audit from zero.

---

# Additional Milan / Italy Candidates

## Fintech District

Strategic value exists for:

- Milan;
- fintech;
- Italian financial innovation;
- startup ecosystem.

No sufficiently compelling public structured route was established during the completed research.

**Status**

> **Standby candidate.**

Revisit only if TEF, Assolombarda and broader markets sources leave a demonstrated fintech/Milan gap.

---

# New Strategically Researched Candidates

The following candidates were identified through a later Career Agent source-expansion research pass.

These are **strategic research conclusions only**.

They are not production-approved until Development validates:

- endpoints;
- terms;
- metadata;
- persistence;
- collector compatibility;
- classification;
- report contribution.

---

## Nasdaq

**Expected information role**

- Financial Markets;
- Companies / Corporate Strategy;
- earnings;
- IPOs;
- corporate finance;
- market structure.

Career research identified official RSS infrastructure and multiple topical feed categories.

Main Development question:

> Which narrow Nasdaq feeds provide high-value market/company intelligence without retail-investor or stock-picking noise?

**Status**

> **Candidate for technical audit — highest priority.**

---

## Federal Reserve Board

**Expected information role**

- Financial Markets;
- Economics/Macro;
- rates;
- credit;
- financial conditions;
- banking.

Career research identified official RSS/statistical infrastructure and potentially favourable reuse conditions.

Main Development question:

> Which small subset of Fed feeds gives the strongest global monetary/financial-condition signal without overwhelming the report?

**Status**

> **Candidate for technical audit — very high priority.**

---

## MIMIT

Ministero delle Imprese e del Made in Italy.

**Expected information role**

- Italy;
- Companies / Corporate Strategy;
- industrial policy;
- restructuring;
- strategic investment;
- innovation.

Career research identified official RSS and potentially permissive CC BY reuse language.

Main Development question:

> Can a narrow subset of MIMIT feeds surface material Italian company/industrial developments while excluding routine ministerial noise?

**Status**

> **Candidate for technical audit — very high priority.**

---

## Lavoce.info

**Expected information role**

- independent Italian economic/business interpretation;
- Economics/Macro;
- Companies;
- Europe;
- Financial Markets.

Career research found promising content and reuse language but did not conclusively validate the current structured-feed route.

Main Development question:

> Does a current stable public structured feed exist with metadata and reuse terms compatible with production?

**Status**

> **Candidate for technical audit — high priority.**

---

## Bruegel

**Expected information role**

- Europe/EU;
- Economics/Macro;
- Financial Markets;
- industrial policy;
- competitiveness.

Career research identified RSS infrastructure and strong independent analytical value.

Main concerns include:

- broad-feed event noise;
- exact treatment required by CC BY-ND-style publication terms;
- whether narrower publication feeds exist.

**Status**

> **Candidate for technical audit — high priority.**

---

## Assolombarda

**Expected information role**

- Milan/Bocconi ecosystem;
- Italy;
- Companies;
- industry;
- technology adoption;
- labour/skills;
- credit;
- economic research;
- professional events.

This source is strategically complementary to TEF:

```text
TEF
→ startups / deep tech / university innovation

Assolombarda
→ established firms / industry / Milan economy
```

Career research found apparent RSS functionality and calendar export, but Development must validate exact current endpoints and reuse terms.

**Status**

> **Candidate for technical audit — high priority.**

---

## Ars Technica

**Expected information role**

- independent AI reporting;
- Technology;
- software/systems;
- cybersecurity;
- infrastructure.

Career research identified official RSS.

Main Development question:

> Can a narrow enough public feed provide high-signal independent AI/technology intelligence without consumer/gadget noise and with acceptable archive rights?

**Status**

> **Candidate for technical audit — high priority after Markets/Italy gaps.**

---

## Google DeepMind News

**Expected information role**

- second primary AI source;
- frontier research;
- models;
- robotics;
- AI safety;
- scientific AI.

Career research identified an official active RSS feed.

Strategic role is complementary to OpenAI, not a replacement for independent reporting.

**Status**

> **Candidate for technical audit — high priority but lower opportunity cost than Markets/Italy.**

---

# Secondary Strategic Candidates

These should not consume current Development time before Tier-A candidates.

## MEF — Dipartimento del Tesoro

Potential value:

- sovereign debt;
- issuance;
- government bonds;
- financial system.

Risk:

- routine auction-volume noise.

Status:

> Tier-B strategic candidate.

## ESMA

Potential value:

- EU market risk;
- securities regulation;
- market structure;
- asset management;
- private finance.

Status:

> Tier-B specialist candidate.

## Invest Europe

Potential value:

- European private capital;
- PE/VC fundraising;
- exits;
- asset-class trends.

Status:

> Tier-B candidate after Italian Tech Alliance.

## BIS

Potential value:

- global financial-system analysis;
- credit;
- sovereign markets;
- non-bank finance;
- global financial conditions.

Status:

> Tier-B research-heavy candidate.

## SEC EDGAR

Potential value:

- primary company filings;
- 8-K;
- S-1;
- 10-K;
- 10-Q.

Main constraint:

> Unfiltered EDGAR would create extreme noise.

Status:

> Tier-B candidate only if a deliberate company/form universe is validated.

## ISPI

Potential value:

- geopolitics;
- geoeconomics;
- Milan professional ecosystem;
- high-quality events.

Status:

> Tier-B candidate.

## Camera di Commercio Milano Monza Brianza Lodi

Potential value:

- Milan firms;
- SMEs;
- innovation;
- financing;
- business studies.

Status:

> Tier-B candidate after Assolombarda.

## Euronext

Potential value:

- European IPOs;
- listings;
- bonds;
- capital-market infrastructure.

Status:

> Tier-B specialist candidate.

## IMF

Potential value:

- global macro;
- global financial stability.

Status:

> Tier-B due slower cadence relative to current gaps.

## AIFI

Potential value:

- Italian PE;
- VC;
- private debt.

Status:

> Tier-B; evaluate only if Italian Tech Alliance leaves a demonstrated private-capital gap.

---

# Deliberately Low-Priority / Standby Sources

Do not currently spend Development time on:

- WSJ;
- CNBC;
- Guardian Business;
- WIRED;
- MarketWatch;
- Fortune;
- ANSA;
- TechCrunch;
- Business Wire / generic press-release aggregators;
- generic Politecnico event feeds;
- generic Bocconi event feeds;
- additional central banks beyond the Fed;
- additional AI labs beyond the current planned DeepMind test.

Reasons include:

- overlap;
- unclear archive rights;
- poor structured access;
- excessive noise;
- promotional bias;
- low marginal information value.

Anthropic remains strategically relevant but no equally clean official feed was established during the strategic research pass.

Do not force it into production merely for AI-lab symmetry.

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
Milan and Bocconi Ecosystem
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
Tech Europe Foundation
```

## Current Source Defaults

```text
BBC News World                → none
BBC News Business             → none
European Central Bank         → none
European Commission           → none
Istat Press Releases          → Economics and Macroeconomics
OpenAI News                   → Artificial Intelligence
Tech.eu                       → none
Tech Europe Foundation        → Milan and Bocconi Ecosystem
```

## Completed Source Replacement

```text
Sifted → Tech.eu
```

## Financial Markets

**Decision:** implemented as a domain; dedicated source coverage remains a priority.

## Italy

**Decision:** strategically approved; dedicated production domain/source architecture remains pending.

## Milan and Bocconi

**Decision:** first production implementation active through Tech Europe Foundation; requirement remains only partially satisfied.

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

However, strategic value does not override:

- automation permission;
- persistence compatibility;
- zero-cost constraints;
- credential boundaries.

FT and Il Sole remain standby after completed source-specific audits.

---

# Current Strategic Source-Audit Priorities

Source expansion is now organised around **domain gaps and differentiated information roles**.

Current Development audit order:

1. Nasdaq;
2. Federal Reserve Board;
3. MIMIT;
4. Lavoce.info;
5. Bruegel;
6. Assolombarda;
7. Ars Technica;
8. Google DeepMind News.

Parallel decision:

> **Italian Tech Alliance → production-readiness decision, not another basic audit.**

This ordering may change if early audits reveal a clearly cleaner or higher-value path.

The main current source-coverage gaps are:

```text
Financial Markets
→ no dedicated source

Companies / Corporate Strategy
→ weak dedicated coverage

Italy
→ incomplete economic/business ecosystem

Artificial Intelligence
→ overconcentrated on OpenAI primary evidence

Startups / VC
→ strongly dependent on Tech.eu

Milan / Bocconi
→ first source exists but complementary roles remain missing
```

---

# Open Information Decisions

## Future Source Universe

No fixed source-count target.

The source universe remains incomplete.

Stop expansion when the major information functions are strong enough for actual use, not when an arbitrary count is reached.

## Italy Domain Architecture

Still pending.

Current preferred direction is a differentiated set rather than one generic newspaper:

```text
Istat
+ MIMIT
+ Lavoce.info
+ Assolombarda
+ Italian Tech Alliance
+ Bank of Italy structured data later if justified
```

This is a strategic hypothesis until each source passes Development validation.

## Italian Tech Alliance Production Decision

Basic source audit is complete.

Remaining decision:

> Does the source add enough unique value despite thin descriptions and press-clipping repetition to justify production activation?

Do not restart basic feed discovery.

## BBC Business

Keep temporarily.

Likely to become redundant only after stronger business/markets coverage is proven in production.

## Independent AI Coverage

Current target:

```text
OpenAI
+ Google DeepMind
+ one independent reporting layer such as Ars Technica
```

Do not add multiple AI labs without demonstrated need.

## Milan/Bocconi Coverage

TEF is active.

Remaining missing roles include:

- established firms;
- industry;
- finance/business events;
- recruiting;
- high-value professional opportunities.

Assolombarda is the current highest-priority complementary candidate.

Career Services remains manual/private under current constraints.

## Publisher Concentration

Continue observing reports.

Do not add concentration penalties or quotas without repeated evidence.

## Richer Context

Validated product requirement.

Implementation remains deferred until source/domain correction is sufficiently mature.

## Ranking Weights

Remain provisional.

## Article-Level Geography

Not implemented.

## Content Type

Not implemented.

## Near-Duplicate Clustering

Not implemented.

Italian Tech Alliance provides a concrete candidate use case, but current evidence remains insufficient for implementation.

## Multi-Source Story Clustering

Not implemented.

## Long-Term Source Health History

Not implemented; per-run health remains sufficient for now.

## Statistical Event Pipeline

Not implemented.

Bank of Italy BDS is the strongest validated future use case.

Do not add the architecture before selected statistical signals justify it.

## Opportunity / Deadline State Tracking

Not implemented.

Do not create it until repeated use shows that publication-only reporting causes meaningful opportunity misses.

---

# Information Quality Decision Rules

Before adding a source, taxonomy rule or new classification dimension, ask:

1. What observed problem does it solve?
2. Is the problem validated?
3. Can a simpler source/configuration change solve it?
4. Does it improve actual report usefulness?
5. What information role does it add that current sources do not?
6. What false positives could it create?
7. What false negatives remain?
8. Does it preserve zero recurring cost?
9. Does it preserve low daily manual work?
10. Does it preserve credential safety?
11. Does it preserve copyright/public-repository safety?
12. What maintenance does it add?
13. How will success be validated?

Preferred pattern:

```text
observe real problem
→ identify missing information function
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

- nine of ten target domains are implemented;
- Italy is not yet implemented as a dedicated topic domain;
- Milan/Bocconi has only a first narrow production implementation;
- active automated coverage remains mostly English-language;
- full bilingual production behaviour is only partially validated;
- Financial Markets lacks a dedicated source;
- Companies/Corporate Strategy lacks strong dedicated reporting;
- AI primary coverage is concentrated on OpenAI;
- Startups/VC relies heavily on Tech.eu;
- article-level geography is not implemented;
- content type is not implemented;
- entity tracking is not implemented;
- near-duplicate clustering is not implemented;
- multi-source story clustering is not implemented;
- long-term source-health history is not implemented;
- ranking weights remain provisional;
- keyword lists remain conservative;
- some strategically relevant records remain unclassified;
- public description richness varies materially by source;
- Premium Bocconi Exception sources may intentionally provide thinner automated context;
- source concentration can vary materially by day;
- the rolling collection window depends on actual scheduled execution time;
- personal Bocconi access is not represented as runtime credentials and must remain outside production authentication;
- private Career Services information is not part of automated ingestion;
- statistical-event ingestion is not implemented.

These are maturity limits, not a list of features that must all be built.

---

# Current Information-Quality Priorities

## 1. Fill the Highest-Cost Information Gaps

Current order of concern:

```text
Financial Markets
Companies / Corporate Strategy
Italy
Independent AI / Technology
Startups / VC diversification
Milan / Bocconi complementarity
Europe independent analysis
```

## 2. Audit Sources by Function, Not Prestige

Current first audit batch:

```text
Nasdaq
Federal Reserve
MIMIT
Lavoce.info
Bruegel
Assolombarda
Ars Technica
Google DeepMind
```

## 3. Resolve Italian Tech Alliance Production Readiness

Do not repeat basic research.

Evaluate actual production value, repetition and report contribution.

## 4. Preserve Current Stable Architecture

Do not introduce:

- agents;
- RAG;
- embeddings;
- vector databases;
- custom opportunity databases;
- statistical-event pipelines;
- sophisticated clustering;
- premium authenticated scraping;

unless repeated evidence validates the need.

## 5. Improve Source Diversity Only Through Better Coverage

No artificial quotas.

Do not target a fixed number of sources per domain.

A domain should have differentiated information roles where feasible.

## 6. Design Richer Report Context After Source Correction

The report should eventually provide materially more context below the relevance score.

Do not redesign summarization while the source universe is still changing materially.

## 7. Revisit Ranking Only If Upstream Corrections Are Insufficient

Prefer:

- better sources;
- better source defaults;
- better keywords;
- better information roles;

before more complex ranking logic.

---

# Current Status

**Phase:** Phase 4 — Source and Domain Correction / Expansion.

**Validated current checkpoint:**

- eight active public RSS sources;
- nine active topic domains;
- Sifted replaced by Tech.eu;
- Tech.eu has no blanket source default;
- Financial Markets implemented conservatively;
- Milan and Bocconi Ecosystem implemented through Tech Europe Foundation;
- TEF uses a validated source-defined domain with an empty keyword list;
- uppercase keyword matching introduced to distinguish `AI` from Italian `ai`;
- targeted and full automated tests passed after the classifier and TEF changes;
- real eight-source pipeline run completed successfully;
- TEF collected successfully and correctly contributed no stale records to the tested 24-hour window;
- FT audit completed;
- Il Sole 24 Ore audit completed;
- Bank of Italy RSS/BDS audit completed;
- Reuters audit completed;
- B4i/TEF/Bocconi source research completed;
- Italian Tech Alliance basic technical audit completed;
- second strategic Career Agent source-expansion research completed;
- no recurring monetary cost introduced;
- no private credentials introduced;
- no authenticated premium-content ingestion introduced.

**Current expansion principle:**

> **Correct information-function gaps before correcting publisher-count gaps.**

**Next highest-ROI Development action:**

> **Begin the new domain-gap-driven source-audit batch with Nasdaq, then Federal Reserve, MIMIT and the remaining ranked candidates, while moving Italian Tech Alliance toward a production-readiness decision.**

After the source/domain universe is sufficiently corrected:

> **Begin the dedicated richer-report design phase.**

---

# Changelog

## 2026-08-17 — Source-Audit Consolidation, Milan/Bocconi Activation and New Expansion Queue

- Consolidated completed Financial Times, Il Sole 24 Ore, Bank of Italy, Reuters, B4i, Bocconi, TEF and Italian Tech Alliance source research.
- Recorded Financial Times as standby because official RSS archival conditions conflict with permanent public-Git persistence.
- Recorded Il Sole 24 Ore as standby rather than rejected; technical compatibility and strategic value remain strong, especially Economia and Finanza.
- Recorded Bank of Italy RSS as standby and BDS structured statistics as an approved future architectural enhancement.
- Recorded Reuters as strategically exceptional but incompatible with current zero-cost machine-delivery constraints.
- Recorded B4i as legacy/superseded by Tech Europe Foundation.
- Recorded Bocconi Career Services as a high-value manual/private layer that must not be authenticated or scraped by production.
- Recorded broad Bocconi Events/News as unsuitable for current automated architecture.
- Added Tech Europe Foundation as the eighth active production source.
- Implemented Milan and Bocconi Ecosystem as the ninth active domain.
- Allowed source-defined domains to use empty keyword lists when explicitly justified.
- Added TEF as a Tier 1 source with Milan and Bocconi Ecosystem as its narrow default.
- Validated TEF metadata, classification, ranking behavior and real pipeline integration.
- Recorded that TEF is the first implementation of the Milan/Bocconi requirement but does not fully solve recruiting, deadlines or Career Services coverage.
- Corrected Artificial Intelligence keyword handling by changing `ai` to intentional uppercase `AI`.
- Made uppercase-containing configured keywords case-sensitive while preserving lowercase keyword case-insensitive matching.
- Confirmed the change removed Italian `ai` false positives while retaining historical English AI recall.
- Recorded Italian Tech Alliance as a production-readiness candidate rather than an unexplored source.
- Recorded `round` and `scaleup fund` as validated candidate Startups/VC terms associated with future Italian Tech Alliance activation.
- Incorporated the second Career Agent source-expansion research.
- Reframed Phase 4 around information-function gaps rather than publisher count.
- Established the new Development audit queue:
  1. Nasdaq;
  2. Federal Reserve;
  3. MIMIT;
  4. Lavoce.info;
  5. Bruegel;
  6. Assolombarda;
  7. Ars Technica;
  8. Google DeepMind.
- Preserved richer-report implementation as deferred until the information universe is sufficiently mature.

## 2026-08-17 — Tech.eu Replacement and Financial Markets Activation

- Incorporated the first Career Agent strategic source/domain audit into Phase 4 priorities.
- Replaced Sifted with Tech.eu after controlled comparison.
- Recorded Tech.eu 20/20 description availability versus Sifted 0/24 in the tested samples.
- Activated Tech.eu as Tier 2 Europe with `default_domains: []`.
- Added `acquired` to Companies and Corporate Strategy after real M&A misses.
- Added `early-stage fund` and `funding market` to Startups and Venture Capital after controlled simulation.
- Removed generic `startup` after it promoted a low-value Tech.eu profile.
- Added `tariffs` after a relevant geopolitical trade story remained unclassified.
- Implemented Financial Markets as the eighth active domain with a conservative first keyword set.
- Validated taxonomy changes against the stored production regression corpus available at that checkpoint.
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