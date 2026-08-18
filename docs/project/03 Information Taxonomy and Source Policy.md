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

- twelve active public RSS sources;
- ten active topic domains;
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
- degraded-run reporting;
- generic HTML-to-text normalisation for feed descriptions.

Current active sources:

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

Current implemented domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Financial Markets;
4. Companies and Corporate Strategy;
5. Artificial Intelligence;
6. Technology and Software;
7. Startups and Venture Capital;
8. Europe and the European Union;
9. Italy;
10. Milan and Bocconi Ecosystem.

All ten strategic topic macroareas now have an implemented domain.

Phase 4 has produced several validated information-quality corrections and source-governance decisions:

- Sifted was replaced by Tech.eu;
- Tech.eu uses no blanket source-default domain;
- Financial Markets was implemented conservatively;
- Milan and Bocconi Ecosystem was implemented through Tech Europe Foundation;
- `milan_bocconi_ecosystem` is source-defined with an empty keyword list;
- multilingual classification was corrected so intentionally uppercase keywords such as `AI` are case-sensitive while lowercase keywords remain case-insensitive;
- Financial Times, Il Sole 24 Ore, Reuters, Bank of Italy, B4i, Bocconi sources, Italian Tech Alliance and other strategic sources were audited;
- Federal Reserve Board Monetary Policy was added as a Tier 1 US monetary-policy source;
- Italy was implemented as the tenth domain;
- MIMIT News was added as a Tier 1 Italian industrial-policy and company-policy source;
- Lavoce.info Imprese was added as a Tier 2 independent Italian business-analysis source;
- narrow Italian-language keywords were added only after live-record testing and historical-regression checks;
- Google DeepMind News was added as a second Tier 1 frontier-lab primary AI source;
- Nasdaq, Bruegel, Assolombarda and Ars Technica were evaluated but not forced into production because access, persistence, metadata or architecture constraints outweighed their incremental value;
- a real twelve-source production-equivalent run completed successfully on 18 August 2026 with twelve successful sources, zero invalid records and no warnings.

The current priority remains:

> **Complete a fresh source-research cycle against the remaining information-function gaps, then decide whether further source expansion still has higher expected value than richer report-context work.**

---

# Taxonomy Principles

## Configurable

Domains, keywords, source tiers and source defaults belong in configuration rather than being scattered through processing code.

Configuration should expand only when corresponding information value is justified.

## Multi-Domain

A story may legitimately belong to more than one domain.

Examples:

- an EU AI regulation may belong to Artificial Intelligence, Technology and Europe/EU;
- an ECB or Federal Reserve decision may belong to Economics and Financial Markets;
- a startup acquisition may belong to Startups/VC and Companies/Corporate Strategy;
- an Italian industrial-policy story may belong to Italy and Companies/Corporate Strategy.

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
- monetary-policy evidence;
- market/company reporting;
- independent analysis;
- specialist ecosystem intelligence;
- professional opportunity discovery;
- frontier-lab primary evidence;
- independent technology scrutiny.

Do not add several publications simply because they cover the same subject.

The operating principle is:

> **Correct information-function gaps before correcting publisher-count gaps.**

---

# Target Topic Taxonomy

The strategic target remains ten macroareas.

All ten now have implemented domains.

Implementation does not imply maturity.

Several domains still lack the differentiated source roles required for strong long-term coverage.

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

Evidence-backed refinements include:

- `war`;
- `conflict`;
- `parliament`;
- `tariffs`.

Broad terms such as `government`, `defence`, `president` and `prime minister` were previously tested but rejected because they produced ambiguous or low-value matches.

Current production coverage is mainly BBC World plus selective spillover from institutional and business sources.

This remains somewhat publisher-concentrated but is not currently among the highest-cost information gaps.

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

**Implemented — strong primary evidence, incomplete independent interpretation.**

Istat Press Releases has Economics and Macroeconomics as a source default because its selected feed is sufficiently narrow.

Federal Reserve Board Monetary Policy also receives Economics and Macroeconomics as its source default.

BBC Business does not receive an Economics default because it is heterogeneous.

ECB, Federal Reserve and Istat now provide substantial primary evidence across the euro area, United States and Italy.

The European Commission adds policy context.

Lavoce.info adds a narrower independent analytical layer for Italian business/economic developments.

Current remaining information-function gaps include:

- broader independent European economic interpretation;
- selected global economic interpretation beyond institutional evidence;
- structured financial/statistical signals where they justify additional architecture.

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

**Implemented — dedicated monetary/rates evidence now exists, broader markets coverage remains incomplete.**

Core configured concepts remain conservative.

Broad terms such as:

- `market`;
- `stocks`;
- `shares`;
- `bonds`;
- `rates`;
- `bank`;
- `investment`;

remain intentionally excluded when they would create excessive false positives.

Federal Reserve Board Monetary Policy materially improves upstream source coverage.

Validated Financial Markets terms added through the Fed audit include:

- `FOMC`;
- `Federal Open Market Committee`;
- `discount rate`.

Lavoce.info testing added:

- `mercati dei capitali`.

This means the system now has strong Tier 1 monetary-policy evidence relevant to rates and financial conditions.

However, the broader Financial Markets information function remains incomplete.

Still under-covered:

- capital-markets activity;
- market structure;
- corporate financing;
- major equity-market developments;
- credit-market developments;
- broader causal market reporting.

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

**Implemented — materially improved, but global source coverage remains incomplete.**

No broad general source receives a Corporate Strategy default.

Previous Phase 4 testing added:

- `acquired`.

MIMIT implementation added narrow Italian corporate/industrial terms:

- `tavoli di crisi`;
- `accordo di sviluppo`;
- `quadro industriale`;
- `rilevanza strategica`.

Lavoce.info Imprese implementation added:

- `fusione e acquisizione`;
- `piano industriale`.

Current source roles now include:

```text
BBC Business
→ broad international business reporting

Tech.eu
→ European startups, technology and selected company developments

MIMIT News
→ primary Italian industrial/company-policy evidence

Lavoce.info Imprese
→ independent Italian company/business interpretation
```

This is a material improvement over the earlier BBC Business + Tech.eu-only architecture.

The major remaining gap is broader international corporate strategy and company reporting.

No clean current source replicates the integrated global corporate-reporting role of sources such as Financial Times or Reuters under the project's zero-cost and public-persistence constraints.

Do not fill that gap with weaker sources merely for completeness.

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

**Implemented — primary-source diversification achieved; independent scrutiny remains incomplete.**

OpenAI News has Artificial Intelligence as its single source default.

Google DeepMind News now also has Artificial Intelligence as its single source default.

Neither receives blanket Technology or Corporate Strategy defaults.

The current primary-source structure is:

```text
OpenAI News
→ Tier 1 primary OpenAI/product/company evidence

Google DeepMind News
→ Tier 1 second frontier-lab primary evidence
```

The DeepMind feed passed:

- public RSS access;
- 100/100 collection in the controlled test;
- 100/100 publication timestamps;
- 100/100 normalisation;
- short feed descriptions rather than full article bodies;
- 100/100 Artificial Intelligence classification through the source default.

No DeepMind-specific keywords were required.

Existing taxonomy correctly added secondary domains only selectively.

The remaining AI information-function gap is:

> **independent reporting and scrutiny outside first-party lab sources.**

Ars Technica was investigated for that role but remains unsuitable for production under current persistence terms.

Do not add frontier labs merely to increase source count.

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

OpenAI, DeepMind and BBC contribute selectively when existing keywords justify a secondary Technology classification.

Independent systems/software reporting remains a useful gap.

Ars Technica was strategically attractive but did not pass the public-persistence policy gate.

A replacement candidate should be sought only if it provides a differentiated information role and clean automation/persistence compatibility.

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

Later differentiated candidates such as Invest Europe or AIFI should be considered only if a real private-capital gap remains after the next source-research cycle.

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

**Implemented — strong institutional evidence, weak independent interpretation.**

ECB and European Commission feeds do not receive Europe/EU as blanket defaults.

Primary institutional evidence is strong.

Tech.eu adds selective specialist European technology/startup reporting.

Bruegel was audited as the strongest independent economic/policy-analysis candidate.

The audit found:

- high strategic value;
- a technically clean general RSS feed dominated by event/session infrastructure;
- more relevant Analysis and Publications feeds that contain malformed XML entities under the current collector;
- feed payloads containing extremely long or effectively full-content article bodies.

The general feed was therefore rejected as a product source.

The Analysis and Publications feeds remain on standby because fixing their parse errors would not solve the more important full-content persistence problem.

The main missing Europe information role therefore remains:

> **independent economic and policy interpretation compatible with the existing public-repository architecture.**

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

**Implemented — viable first production architecture.**

Italy is now an active dedicated domain.

The domain is source-defined and currently uses:

```yaml
keywords: []
```

This is intentional.

Broad generic Italian keywords such as:

```text
Italia
aziende
imprese
investimenti
```

would create excessive classification noise.

Instead, Italy classification is supplied by narrow source defaults where source identity itself is reliable evidence.

Current architecture:

```text
Istat
→ Tier 1 primary statistical and macroeconomic evidence

MIMIT News
→ Tier 1 industrial policy, restructuring,
  strategic investment and company-policy evidence
→ Italy source default

Lavoce.info Imprese
→ Tier 2 independent business/company interpretation
→ Italy source default
```

### MIMIT News

The official MIMIT News RSS passed technical and product testing.

Validated characteristics included:

- standard public RSS;
- successful collection and normalisation;
- complete publication timestamps;
- useful descriptions;
- strong material on industrial policy, strategic investment, company crises, data centres, cloud/cyber programmes and restructuring.

The broader Incentives feed was not activated because it contained more administrative and duplicative material.

MIMIT also exposed a general feed-normalisation issue: HTML descriptions were entering the processing layer.

The solution was not source-specific.

A generic standard-library HTML-to-text normalisation improvement was implemented and validated.

Narrow Italian classification terms adopted through MIMIT testing include:

```text
Companies / Corporate Strategy
- tavoli di crisi
- accordo di sviluppo
- quadro industriale
- rilevanza strategica

Economics / Macroeconomics
- inflazione
```

### Lavoce.info Imprese

The dedicated Imprese category was selected over the general feed and Banche e finanza.

The general Lavoce feed was rejected because its information scope was too broad.

Banche e finanza remains standby because it is high-quality but sparse and overlaps with stronger monetary/financial primary sources.

Lavoce.info Imprese passed:

- official public WordPress RSS access;
- complete timestamps;
- complete descriptions in the tested sample;
- strong analytical content;
- controlled classification testing;
- historical-regression testing.

Validated Italian keywords added through Lavoce testing:

```text
Companies / Corporate Strategy
- fusione e acquisizione
- piano industriale

Artificial Intelligence
- IA

Financial Markets
- mercati dei capitali
```

Broader or redundant candidates such as:

```text
M&A
piano strategico
quotazione
azienda
impresa
investimenti
```

were not added because they either duplicated stronger terms or risked broader false positives.

### Current Italy Limitations

Italy is implemented, but coverage is not complete.

Remaining gaps include:

- banks and financial institutions;
- broader Italian capital markets;
- major-company coverage outside industrial-policy events;
- independent macro interpretation beyond the current Lavoce Imprese role;
- selected Milan/Lombardy established-company intelligence.

Il Sole 24 Ore remains strategically valuable and on standby rather than permanently rejected.

Bank of Italy statistical data remains a strong future architecture candidate.

Italian Tech Alliance remains a production-readiness candidate for VC/startup ecosystem coverage.

The Italy domain should therefore be considered:

> **implemented and useful, but still open to differentiated expansion where evidence supports it.**

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

Current automated coverage is strongest for:

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

Assolombarda was audited as the strongest obvious complement to TEF.

Its public News and Comunicati stampa feeds were technically reachable and normalised successfully, and their contents were strategically valuable for:

- established firms;
- industry;
- manufacturing AI;
- local exports;
- infrastructure;
- Search Funds;
- innovation;
- Milan/Lombardy economic activity.

However:

```text
publication timestamps
→ 0/15 in both tested feeds
```

and the feeds contain substantive publisher-authored descriptions.

Under current terms and architecture, Assolombarda therefore fails both the publication-window and public-persistence gates.

Assolombarda remains standby rather than being forced into production through source-specific date scraping or description stripping.

Bocconi Career Services remains strategically extremely valuable but key infrastructure lives inside authenticated yoU@B / JobGate.

Do not automate authenticated Bocconi access.

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

Current production Tier 1 examples include:

- European Central Bank;
- European Commission;
- Istat;
- Federal Reserve Board;
- MIMIT;
- OpenAI;
- Google DeepMind;
- Tech Europe Foundation.

## Tier 2 — High-Quality Reporting

Established journalistic or specialist organisations providing original reporting, verification or useful professional context.

Tier 2 does not imply automatic production eligibility.

Current examples include:

- BBC;
- Tech.eu;
- Lavoce.info Imprese.

The Sifted replacement decision remains a useful example: strategic relevance was insufficient when another source provided materially better metadata and follow-up usability.

## Tier 3 — Specialist Analysis

Specialist organisations, research groups, industry associations, venture organisations and focused publications that do not fit the Tier 2 role.

Approve individually.

Italian Tech Alliance and Assolombarda-type industry-association sources should be evaluated conservatively within this category unless evidence supports another tier.

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

Source-default domains therefore require particular discipline because they affect both classification and score.

No source-specific ranking rules are currently justified.

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

Both have been technically/policy audited.

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

Missing timestamps are not repaired by substituting retrieval time.

## Metadata Quality

Titles and links must be usable.

Descriptions and other public context are explicit product-quality dimensions.

Missing descriptions may remain technically valid but can still make a source a poor product fit.

Full-content RSS is not automatically better metadata.

If feed fields contain substantial or effectively complete article bodies, public-repository persistence must be evaluated before integration.

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
- retrieval time would have to substitute publication time;
- the endpoint is unstable relative to its value;
- the source creates disproportionate maintenance;
- public structured metadata is consistently too thin;
- the feed exposes substantial/full article bodies that are incompatible with public persistence;
- selected links are repeatedly inaccessible and public context is insufficient;
- the source is excessively promotional or noisy;
- the source systematically duplicates better sources;
- an alternative source provides materially better accessibility, metadata or reliability;
- implementation requires a new processing paradigm before the information need is sufficiently validated.

Prefer replacing or deferring a weak/incompatible source over adding source-specific complexity.

The Bruegel and Assolombarda audits reinforce two general rules:

```text
malformed-feed repair
≠ sufficient reason to ingest full-content payloads

missing publication timestamp
≠ permission to substitute retrieval time
```

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
Full-content persistence risk?
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
| `openai_news` | OpenAI News | 1 | Artificial Intelligence | Global | Active — frontier-lab primary source |
| `tech_eu` | Tech.eu | 2 | None | Europe | Active — validated Sifted replacement |
| `tech_europe_foundation` | Tech Europe Foundation | 1 | Milan and Bocconi Ecosystem | Europe; Italy; Milan | Active — first Milan/Bocconi source |
| `federal_reserve_monetary` | Federal Reserve Board Monetary Policy | 1 | Economics and Macroeconomics | United States | Active — US monetary-policy primary source |
| `mimit_news` | MIMIT News | 1 | Italy | Italy | Active — industrial/company-policy primary source |
| `lavoce_imprese` | Lavoce.info Imprese | 2 | Italy | Italy; Europe | Active — independent Italian business analysis |
| `google_deepmind_news` | Google DeepMind News | 1 | Artificial Intelligence | Global | Active — second frontier-lab primary source |

All current production sources use public structured feeds and require no paid API or private credentials for collection.

Current language balance is intentionally majority English:

```text
English-language active feeds → 10
Italian-language active feeds → 2
```

This is not a quota.

English remains the default information layer.

Italian sources are added when they offer differentiated Italy/Milan information value that is difficult to replicate through English-language sources.

---

# Current Source Roles

## BBC News World

Broad global-news safety net.

Strategic status:

> **Retain during expansion.**

Main limitation:

- publisher concentration in Global Politics.

Do not add another generic world-news source until higher-priority differentiated gaps are addressed.

## BBC News Business

Broad accessible business reporting.

Strategic status:

> **Retain temporarily.**

It may become more redundant if future Markets and Companies coverage improves.

Do not remove it before replacement coverage is demonstrated in real reports.

## European Central Bank

Primary euro-area monetary-policy and financial-system evidence.

Strategic status:

> **Core.**

## European Commission Highlighted News

Primary EU policy evidence.

Strategic status:

> **Retain.**

Classification should continue filtering routine communications.

## Istat Press Releases

Primary Italian macroeconomic evidence.

Strategic status:

> **Core.**

Istat is now one component of the broader Italy architecture rather than its only Italian source.

## Federal Reserve Board Monetary Policy

Primary United States monetary-policy evidence.

Strategic status:

> **Active — core addition for Economics/Macro and Financial Markets.**

Its descriptions are relatively thin, but the source provides high-value Tier 1 evidence.

## MIMIT News

Primary Italian industrial-policy, restructuring, strategic-investment and company-policy evidence.

Strategic status:

> **Active — core Italy source.**

## Lavoce.info Imprese

Independent Italian business/company analysis.

Strategic status:

> **Active — differentiated Tier 2 Italy source.**

It complements MIMIT rather than duplicating it.

## OpenAI News

Primary OpenAI/company evidence.

Strategic status:

> **Retain as one AI primary source.**

It no longer defines the full primary AI universe because DeepMind is now active.

## Google DeepMind News

Primary Google DeepMind AI evidence.

Strategic status:

> **Active — second frontier-lab source.**

It adds Gemini, robotics, scientific AI, safety and related developments.

It does not replace the need for independent AI reporting.

## Tech.eu

European startup/VC and technology specialist reporting.

Strategic status:

> **Active Sifted replacement.**

Monitor noise and classification recall without a source default.

## Tech Europe Foundation

Primary source for TEF programmes, entrepreneurship activity and associated Milan/Bocconi innovation ecosystem developments.

Strategic status:

> **Active first Milan/Bocconi source.**

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
Istat Press Releases
→ Economics and Macroeconomics

Federal Reserve Board Monetary Policy
→ Economics and Macroeconomics

OpenAI News
→ Artificial Intelligence

Google DeepMind News
→ Artificial Intelligence

MIMIT News
→ Italy

Lavoce.info Imprese
→ Italy

Tech Europe Foundation
→ Milan and Bocconi Ecosystem
```

Tech.eu has no Startups/VC default because its general feed is broader than that domain.

MIMIT and Lavoce.info use Italy defaults because their selected streams were validated as reliably belonging to the Italian economic/business information universe.

DeepMind uses an AI default because all 100 tested records were appropriately AI-related.

TEF has a Milan/Bocconi default because the selected News feed was validated as belonging to that professional ecosystem even when individual stories do not contain generic topical keywords.

Earlier broad defaults inflated classifications and scores.

The rule remains:

> **Use a source default only when it represents a genuine source-wide guarantee for the selected feed.**

---

# Empty-Keyword Domain Policy

A domain may use an empty keyword list when:

- the domain is still meaningful and user-validated;
- classification evidence comes from one or more narrow source defaults;
- invented generic keywords would reduce precision;
- the behaviour is explicit in configuration and tests.

Current examples:

```text
Italy
keywords: []

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
→ run historical regression
→ retain only justified terms
→ rerun report
→ inspect product quality
```

Keyword matches affect both classification and relevance score, so careless synonym expansion can inflate scores.

## Keyword Case Policy

Configured keywords use the following deterministic convention:

```text
keyword containing only lowercase characters
→ case-insensitive match

keyword intentionally containing uppercase characters
→ case-sensitive match
```

This convention was introduced after Italian-language testing revealed that the English acronym `AI` was being confused with the common Italian word `ai`.

Production configuration therefore uses:

```text
AI
```

rather than:

```text
ai
```

The change was validated against historical English AI records and Italian-language records.

It preserved useful English AI recall while removing false Italian classifications.

The later Lavoce.info audit also added the intentional uppercase Italian acronym:

```text
IA
```

Do not introduce language detection or NLP while this simpler deterministic rule remains sufficient.

## Current Evidence-Backed Phase 4 Changes

Added:

```text
Global Politics / Geopolitics
- tariffs

Companies / Corporate Strategy
- acquired
- tavoli di crisi
- accordo di sviluppo
- quadro industriale
- rilevanza strategica
- fusione e acquisizione
- piano industriale

Economics / Macroeconomics
- inflazione

Artificial Intelligence
- IA

Financial Markets
- FOMC
- Federal Open Market Committee
- discount rate
- mercati dei capitali

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

Important rejected/deferred candidate terms include:

```text
Companies
- M&A
- piano strategico

Artificial Intelligence
- intelligenza artificiale

Financial Markets
- quotazione
```

These were not added because the tested samples did not justify their incremental value or they duplicated stronger evidence.

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

English is the default information layer.

Italian specialist sources should be added when they provide uniquely valuable:

- Italian macroeconomic evidence;
- industrial/company intelligence;
- business analysis;
- Milan/Lombardy intelligence;
- Italian startup/VC information.

There is no hard language quota.

The production source universe should remain comfortably majority English unless evidence shows that additional Italian sources materially improve information quality.

Current production balance:

```text
10 English-language feeds
2 Italian-language feeds
```

Italian production behaviour is now materially validated through:

- MIMIT News;
- Lavoce.info Imprese;
- Italian keyword classification;
- case-sensitive `AI` / `IA` handling;
- historical-regression checks;
- production-equivalent pipeline runs.

When further Italian-language sources are considered:

- test Italian classification examples;
- add Italian keywords only when evidence justifies them;
- preserve original titles;
- keep translation outside the core ingestion dependency;
- do not add broad Italian words merely to increase classification coverage.

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

Current information-function state:

```text
Global Politics
→ still largely BBC-led

Economics/Macro
→ strong primary evidence through ECB, Fed and Istat

Financial Markets
→ monetary/rates evidence materially improved;
  broader markets reporting still weak

Companies/Corporate Strategy
→ materially improved through MIMIT + Lavoce;
  global corporate reporting still weak

Artificial Intelligence
→ OpenAI + DeepMind primary diversity achieved;
  independent scrutiny still missing

Technology
→ Tech.eu plus selective spillover;
  independent systems/software role still open

Startups/VC
→ still relies heavily on Tech.eu

Europe/EU
→ strong institutional evidence;
  independent interpretation still weak

Italy
→ viable first source architecture implemented

Milan/Bocconi
→ TEF active;
  established-firm and recruiting/event coverage incomplete
```

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

- full copyrighted articles without permission;
- substantial copied passages where permission is absent;
- authenticated premium content;
- restricted database exports;
- private Career Services content;
- credentials;
- tokens;
- session cookies;
- private user data.

A public RSS feed is not automatically permission to persist every field it contains.

The Bruegel audit demonstrated that an RSS description can effectively contain an entire publication body.

Feed payload depth must therefore be evaluated separately from endpoint accessibility.

The system should store only what is both technically necessary and compatible with the intended public-repository use.

---

# Bocconi Licence Boundary

Personal or institutional access through Bocconi changes what the user may legitimately read.

It does not grant the automated system permission to:

- log into premium publisher sites;
- scrape authenticated pages;
- persist licensed full text;
- redistribute restricted content;
- embed Bocconi credentials;
- automate private Career Services infrastructure.

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
Standby — metadata/timestamps
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
- reader accessibility;
- persistence compatibility.

## 3. Technical Probe

Inspect:

- endpoint availability;
- HTTP behaviour;
- redirects;
- timestamps;
- descriptions;
- entry count;
- malformed records;
- feed-content depth.

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

## 7. Historical Regression

For proposed keyword changes:

- test against stored historical processed records;
- identify newly classified historical records;
- reject terms that create ambiguous or low-value regressions.

## 8. Report Contribution

Inspect:

- usefulness;
- noise;
- repetition;
- context richness;
- source concentration;
- accessibility.

## 9. Production Approval

Only then:

- edit configuration;
- update relevant tests;
- run targeted tests;
- run full suite;
- run real pipeline;
- inspect report;
- inspect diff;
- commit.

The source-expansion process should remain organised around **information-function gaps**, not a linear list of prestigious publications.

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

- public News RSS validated;
- standard RSS;
- collector compatible;
- normalisation successful;
- rich descriptions;
- reliable timestamps and links;
- real pipeline integration successful.

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

### Federal Reserve Board Monetary Policy

**Strategic role**

US/global monetary-policy primary evidence for:

- Economics/Macro;
- Financial Markets;
- rates;
- monetary conditions.

**Technical result**

Official Monetary Policy RSS:

```text
https://www.federalreserve.gov/feeds/press_monetary.xml
```

passed:

- public access;
- collector compatibility;
- normalisation;
- publication timestamps;
- production integration.

Descriptions are generally thin and often duplicate titles, but the source's Tier 1 evidence value remains strong.

**Classification**

```text
default domain:
Economics and Macroeconomics
```

Validated Financial Markets terms:

```text
FOMC
Federal Open Market Committee
discount rate
```

These passed historical-regression checks.

**Production validation**

The real pipeline completed successfully after activation.

**Status**

> **Active.**

---

### MIMIT News

**Strategic role**

Italian primary evidence for:

- industrial policy;
- company restructuring;
- strategic investment;
- industrial competitiveness;
- company-policy interventions.

**Technical result**

Official MIMIT News RSS passed:

- public access;
- collector compatibility;
- complete sample normalisation;
- timestamp availability;
- description availability.

A general HTML-to-text normalisation improvement was implemented because the feed exposed HTML descriptions.

No MIMIT-specific branch was introduced.

**Classification**

```text
default domain:
Italy
```

Validated secondary keywords:

```text
Companies / Corporate Strategy
- tavoli di crisi
- accordo di sviluppo
- quadro industriale
- rilevanza strategica

Economics / Macroeconomics
- inflazione
```

**Status**

> **Active.**

---

### Lavoce.info Imprese

**Strategic role**

Independent Italian business/company interpretation.

**Technical result**

The dedicated Imprese WordPress RSS passed:

- public access;
- collector compatibility;
- timestamp coverage;
- description coverage;
- controlled classification testing.

**Classification**

```text
default domain:
Italy
```

Validated keywords:

```text
Companies / Corporate Strategy
- fusione e acquisizione
- piano industriale

Artificial Intelligence
- IA

Financial Markets
- mercati dei capitali
```

Each retained keyword produced zero unintended historical-regression matches in the tested stored corpus.

**Status**

> **Active.**

---

### Google DeepMind News

**Strategic role**

Second frontier-lab Tier 1 AI primary source.

**Technical result**

Official RSS:

```text
https://deepmind.google/blog/rss.xml
```

controlled test:

```text
100 collected
100 normalised
100 timestamps
79 descriptions
average description ≈ 119 characters
maximum description = 354 characters
0 descriptions > 500 characters
```

This confirmed a metadata-scale feed rather than a full-content persistence problem.

**Classification**

```text
default domain:
Artificial Intelligence
```

Classification review:

```text
Artificial Intelligence → 100/100
AI-only                 → 97/100
multi-domain            → 3/100
```

The three secondary classifications were sensible and produced by existing taxonomy rules.

No new DeepMind-specific keywords were required.

**Production validation**

A real twelve-source run completed successfully:

```text
12 active
12 successful
0 failed
0 invalid
0 warnings
status: success
```

**Status**

> **Active.**

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

Do not reopen the same RSS analysis without materially new evidence.

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

**Policy concern**

Persistence/licensing compatibility with the permanent public Git archive is not sufficiently clean.

**Status**

> **Standby — strategically strong and technically compatible, but persistence/licensing compatibility is not clean enough.**

This is not a permanent rejection.

Revisit if a compliant low-complexity implementation path becomes available.

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

No clean official zero-cost public Reuters news endpoint suitable for the current production architecture was identified.

Scraping Reuters.com or relying on third-party RSS generators is not acceptable.

**Status**

> **Standby / rejected under current zero-cost constraints.**

Reconsider only if Reuters offers a genuinely public automation-compatible feed/API or project constraints explicitly change.

---

## Nasdaq

**Strategic value**

High for:

- capital markets;
- market structure;
- IPOs;
- selected corporate-finance developments.

**Research result**

Current Nasdaq terms materially conflict with the system's automated public-persistence workflow.

The relevant legal terms broadly restrict automated/manual capture, storage and redistribution of associated content/metadata without permission.

No current source-specific public licence overriding that restriction was established.

Generic Markets/stocks/investing feeds would also introduce undesirable retail-investor and prediction noise.

**Status**

> **Standby — access/persistence conflict.**

Do not depend on bespoke publisher permission for the MVP.

Reopen only if terms or a clearly licensed public endpoint materially change.

---

## Ars Technica

**Strategic value**

High for:

- independent AI reporting;
- software/systems;
- cybersecurity;
- technology infrastructure.

**Research result**

Official RSS infrastructure exists.

However, applicable Condé Nast/Ars terms do not provide a clean basis for republishing/persisting RSS-derived content in the public repository.

A title-only source-specific exception was considered but rejected because it would introduce an ambiguous legal/persistence workaround for one publisher.

**Status**

> **Standby — access/persistence conflict.**

The independent AI/technology-reporting gap remains open.

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

**Status**

> **Standby.**

Do not add the RSS feeds merely because they are technically compatible.

---

## Bank of Italy BDS / Statistical Database

**Strategic value**

Very high.

**Research result**

Bank of Italy provides an official application-to-application statistical export system.

Relevant areas include:

- Ita-coin;
- banking;
- interest rates;
- public finance;
- government debt;
- borrowing requirement;
- balance of payments;
- financial markets;
- financial conditions.

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

Do not implement until selected statistical signals justify the architecture.

---

# Milan/Bocconi Source Audits

## B4i — Bocconi for Innovation

B4i has been superseded by Tech Europe Foundation for the current production role.

Its historical archive remains useful as calibration evidence.

**Status**

> **Legacy / superseded by TEF.**

---

## Bocconi Career Services / yoU@B / JobGate

**Strategic value**

Extremely high for:

- recruiting;
- finance;
- consulting;
- employer events;
- professional opportunities.

Complete event infrastructure and registration are partly contained inside authenticated:

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

---

## Bocconi General News / Events

Bocconi's public event universe contains valuable lectures, seminars, policy events and conferences.

However, it also contains large amounts of low-relevance campus and admissions activity.

No clean narrow structured feed was established.

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

Validated candidate terms:

```text
round
scaleup fund
```

Historical regression produced only relevant matches.

**Main unresolved issue**

Report contribution on press-clipping cluster days.

**Status**

> **Production-readiness candidate.**

Basic strategic and technical audit is complete.

Do not restart the audit from zero.

---

# Additional Completed Phase 4 Audits

## Federal Reserve Banking / Consumer Regulatory Feed

**Strategic value**

Potentially useful for:

- banking;
- regulation;
- financial stability;
- Financial Markets.

**Technical result**

The feed collected and normalised successfully.

However, the sample was heterogeneous, mixing:

- major capital/stress-test developments;
- stablecoin/regulatory developments;
- narrow administrative items;
- enforcement-related material.

**Status**

> **Standby.**

The Monetary Policy feed provides a cleaner first Fed production role.

---

## MIMIT Incentives

**Strategic value**

Potentially useful for:

- industrial investment;
- incentives;
- Italian company policy.

**Technical result**

Technically valid but more administrative, sparse in descriptions and partly duplicative of the News feed.

**Status**

> **Standby.**

MIMIT News is the preferred production stream.

---

## Lavoce.info General Feed

**Strategic value**

Broad Italian economic-policy analysis.

**Technical result**

Technically strong but too broad for the specific information role needed.

Sample topics ranged from labour and AI to migration, schools, taxation and emergency management.

**Status**

> **Rejected for production — too broad.**

---

## Lavoce.info Banche e finanza

**Strategic value**

High-quality analysis of:

- banks;
- finance;
- monetary policy;
- Italian capital markets.

**Technical result**

Technically strong but sparse.

Its incremental value currently overlaps materially with the Fed and future specialist Financial Markets candidates.

**Status**

> **Standby.**

---

## Bruegel General RSS

**Strategic value**

Bruegel itself is highly valuable for independent European policy analysis.

**Technical result**

The general RSS was technically clean but dominated by:

- conference sessions;
- lunch;
- coffee breaks;
- programme components.

**Status**

> **Rejected for production — wrong information function.**

---

## Bruegel Analysis

**Strategic value**

Very high for independent European economic-policy analysis.

**Technical result**

- HTTP access succeeds;
- current collector fails on malformed `&nbsp;` entities;
- direct feedparser recovery returns entries in bozo/error mode;
- descriptions can contain thousands or tens of thousands of characters;
- sample maximum exceeded 60,000 characters;
- the feed mixes datasets, newsletters, podcasts, policy briefs and other content.

**Status**

> **Standby — malformed/full-content feed incompatible with current architecture.**

Fixing the entity error alone would not solve the public-persistence problem.

---

## Bruegel Publications

**Strategic value**

Very high.

**Technical result**

- HTTP access succeeds;
- current collector fails on malformed XML entities;
- direct parser recovery is partial/error-mode;
- tested descriptions/content fields include very large publication bodies;
- one tested description exceeded 90,000 characters.

**Status**

> **Standby — malformed/full-content feed incompatible with current architecture.**

Do not create Bruegel-specific truncation or a second persistence path merely to activate this source.

---

## Assolombarda News

**Strategic value**

Very high for:

- Milan/Lombardy economy;
- established firms;
- industry;
- local innovation;
- technology adoption;
- professional ecosystem developments.

**Technical result**

Official RSS exists and collected successfully.

Tested sample:

```text
15 collected
15 normalised
0/15 publication timestamps
14/15 descriptions
average description ≈ 109 characters
```

Descriptions contain substantive Assolombarda-authored prose rather than only metadata.

**Status**

> **Standby — timestamp and persistence incompatibility.**

Do not substitute retrieval time for publication time.

Do not add source-specific page scraping to recover dates.

---

## Assolombarda Comunicati Stampa

**Technical result**

Official RSS exists and collected successfully.

Tested sample:

```text
15 collected
15 normalised
0/15 publication timestamps
14/15 descriptions
average description ≈ 89 characters
```

**Status**

> **Standby — timestamp and persistence incompatibility.**

---

## Assolombarda Centro Studi

Strategically valuable for:

- Lombardy economic research;
- industrial structure;
- labour and skills;
- investment;
- territorial competitiveness.

No RSS/feed link was exposed on the tested current page.

**Status**

> **Manual/research layer under current architecture.**

Do not introduce scraping without a validated requirement.

---

# Additional Milan / Italy Candidates

## Fintech District

Strategic value exists for:

- Milan;
- fintech;
- Italian financial innovation;
- startup ecosystem.

No sufficiently compelling public structured route was established during completed research.

**Status**

> **Standby candidate.**

Revisit only if the Milan/financial-innovation gap remains material after the next source-research cycle.

---

# Secondary Strategic Candidates

These have not been fully audited in the current completed batch.

They should be reconsidered only through a new gap-driven source-research pass or when an existing unresolved information role clearly points to them.

## MEF — Dipartimento del Tesoro

Potential value:

- sovereign debt;
- issuance;
- government bonds;
- financial system.

## ESMA

Potential value:

- European market regulation;
- securities;
- capital markets;
- financial stability.

## Invest Europe

Potential value:

- European private capital;
- venture capital;
- private equity;
- fundraising and investment statistics.

## BIS

Potential value:

- global banking;
- monetary policy;
- financial stability;
- cross-border financial conditions.

## SEC EDGAR

Potential value:

- primary company filings;
- material corporate events.

Do not add EDGAR without a defined company/form universe.

## ISPI

Potential value:

- Milan;
- geopolitics;
- policy;
- events.

## Camera di Commercio Milano Monza Brianza Lodi

Potential value:

- local companies;
- business demography;
- Milan economic ecosystem.

## Euronext

Potential value:

- European capital markets;
- listings;
- market infrastructure.

## IMF

Potential value:

- global macroeconomic evidence;
- forecasts;
- country assessments.

## AIFI

Potential value:

- Italian private equity;
- venture capital;
- investment ecosystem.

These are not an automatic next queue.

The next source universe should be selected by a fresh Career Agent research pass against current information-function gaps.

---

# Deliberately Low-Priority / Standby Sources

Sources may remain strategically interesting without deserving current Development time.

Examples include:

- Financial Times under current RSS archival terms;
- Il Sole 24 Ore under current persistence uncertainty;
- Reuters under current zero-cost access constraints;
- Nasdaq under current persistence terms;
- Bank of Italy RSS;
- Bank of Italy BDS until statistical-event architecture is justified;
- Italian Tech Alliance pending report-value decision;
- Fintech District;
- Lavoce Banche e finanza;
- Federal Reserve Banking/Regulatory;
- MIMIT Incentives;
- Bruegel Analysis/Publications;
- Assolombarda;
- Ars Technica.

Standby does not mean permanent rejection.

Reopen only when:

- source terms change;
- a cleaner endpoint appears;
- a new general architecture is independently justified;
- report evidence shows that the unresolved information gap has become materially costly.

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
Italy
Milan and Bocconi Ecosystem
```

All ten strategic macroareas now have production configuration.

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
Federal Reserve Board Monetary Policy
MIMIT News
Lavoce.info Imprese
Google DeepMind News
```

## Current Source Defaults

```text
Istat Press Releases
→ Economics and Macroeconomics

Federal Reserve Board Monetary Policy
→ Economics and Macroeconomics

OpenAI News
→ Artificial Intelligence

Google DeepMind News
→ Artificial Intelligence

MIMIT News
→ Italy

Lavoce.info Imprese
→ Italy

Tech Europe Foundation
→ Milan and Bocconi Ecosystem
```

## Completed Source Replacement

```text
Sifted
→ replaced by Tech.eu
```

## Financial Markets

Implemented.

Dedicated monetary/rates primary evidence now exists through the Federal Reserve.

Broader capital-market/company-market coverage remains incomplete.

## Italy

Implemented.

Current first architecture:

```text
Istat
+ MIMIT News
+ Lavoce.info Imprese
```

Further differentiated sources may be added, but Italy is no longer an unimplemented domain.

## Milan and Bocconi

Implemented in a conservative first version through Tech Europe Foundation.

Assolombarda was validated as strategically complementary but is not production-compatible under current timestamp/persistence constraints.

## Artificial Intelligence

Primary-source diversification achieved through:

```text
OpenAI
+ Google DeepMind
```

Independent reporting remains unresolved.

## Multi-Domain Records

Allowed and expected.

## Primary Report Placement

One primary placement per item.

Secondary domains shown as metadata.

## Unclassified Records

Valid processed records.

Omitted from the main report by default.

High unclassified share is not itself a defect.

## Report Limits

```text
maximum 5 items per primary domain
maximum 30 displayed items
```

These are upper bounds.

## Description Length

Current report descriptions remain bounded.

Richer report-context logic remains deferred.

## Collection Window

Previous 24 hours based on actual publication timestamps.

## Missing Publication Timestamp

Do not substitute retrieval time.

Assolombarda testing reinforced this rule.

## Premium Sources

Personal/Bocconi reading access does not authorize authenticated automated ingestion.

---

# Open Information Decisions

## Future Source Universe

The current twelve-source set is not assumed final.

The correct next question is:

> **Which unresolved information-function gaps still justify another source before richer report-context work becomes the higher-value intervention?**

A fresh Career Agent research pass should identify candidates from the current gap structure rather than restart the completed audit queue.

## Global Companies / Corporate Strategy

Still incomplete.

MIMIT and Lavoce materially improve Italian company intelligence.

A strong international corporate-strategy layer remains missing.

Do not force a weaker source into this role simply because FT and Reuters are unavailable under current constraints.

## Broader Financial Markets

Federal Reserve Monetary Policy solves part of the rates/monetary evidence gap.

Still unresolved:

- capital markets;
- corporate financing;
- market structure;
- broader market-moving company developments.

## Independent AI / Technology Reporting

OpenAI + DeepMind satisfy primary-source diversity.

Independent scrutiny remains unresolved.

Ars Technica failed the current persistence gate.

A new source should add a genuinely different information function rather than another first-party AI lab.

## Europe Independent Analysis

ECB and European Commission provide strong primary evidence.

Bruegel was strategically excellent but incompatible with the current feed/persistence architecture.

A cleaner independent analytical source remains desirable.

## Startups / VC Diversification

Tech.eu remains the main specialist production source.

Italian Tech Alliance remains a production-readiness candidate.

Additional sources should be added only if they provide differentiated private-capital or Italian ecosystem evidence.

## Milan/Bocconi Coverage

TEF is active.

Remaining missing roles include:

- established firms;
- industry;
- finance/business events;
- recruiting;
- high-value professional opportunities.

Assolombarda remains standby.

Career Services remains manual/private.

## Italian Tech Alliance Production Decision

Basic technical research is complete.

Remaining question:

> **Does its unique Italian VC/opportunity value outweigh thin descriptions and press-clipping repetition in real report use?**

Do not restart feed discovery.

## BBC Business

Keep temporarily.

Reassess only after stronger Companies and Financial Markets coverage is demonstrated in real reports.

## Publisher Concentration

Continue observing reports.

Do not add concentration penalties or quotas without repeated evidence.

## Richer Context

Validated product requirement.

Implementation remains deferred until the next source-research batch clarifies whether marginal source expansion still has higher expected value.

## Ranking Weights

Remain provisional.

## Article-Level Geography

Not implemented.

## Content Type

Not implemented.

## Near-Duplicate Clustering

Not implemented.

Italian Tech Alliance remains the strongest current candidate use case.

Do not implement without repeated production evidence.

## Multi-Source Story Clustering

Not implemented.

## Long-Term Source Health History

Not implemented.

Per-run health remains sufficient for now.

## Statistical Event Pipeline

Not implemented.

Bank of Italy BDS remains the strongest validated future use case.

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
13. Does it require source-specific architecture?
14. Is that architecture justified by more than one source or a validated user need?
15. How will success be validated?

Preferred pattern:

```text
observe real problem
→ identify missing information function
→ isolate cause
→ compare simplest solutions
→ test smallest justified change
→ run historical regression when taxonomy changes
→ rerun
→ inspect information quality
→ stop at stable checkpoint
```

---

# Current Information-Policy Limitations

Known limitations:

- all ten target domains are implemented, but implementation maturity varies;
- Milan/Bocconi has only a first narrow production implementation;
- Financial Markets remains stronger on monetary/rates evidence than broader capital markets;
- Companies/Corporate Strategy still lacks a strong international dedicated reporting layer;
- independent AI/technology reporting remains unresolved;
- Startups/VC relies heavily on Tech.eu;
- Europe/EU lacks a clean independent analysis source;
- Milan/Lombardy established-company coverage remains incomplete;
- active automated coverage is deliberately majority English-language;
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
- statistical-event ingestion is not implemented;
- some strategically valuable publishers remain unusable because persistence rights are incompatible with the public Git archive;
- some strategically valuable structured feeds remain unusable because publication timestamps are absent;
- some official feeds expose full-content payloads that are unsuitable for the existing metadata persistence model.

These are maturity limits, not a list of features that must all be built.

---

# Current Information-Quality Priorities

## 1. Reassess the Highest-Cost Remaining Information Gaps

Current gap structure:

```text
Global Companies / Corporate Strategy
Broader Financial Markets
Independent AI / Technology reporting
Europe independent analysis
Startups / VC diversification
Milan / Lombardy established-company and professional ecosystem coverage
```

Italy and AI primary-source diversification are no longer unimplemented problems.

They remain areas for maturity improvement, not first-order architecture gaps.

## 2. Run a Fresh Gap-Driven Source Research Pass

The previous audit queue:

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

is now complete.

Do not continue treating it as an active queue.

The next candidate universe should be researched from the current information-function gaps.

The Career Agent can be used for strategic source discovery because it has broader context on career/professional information value.

The Development project remains responsible for:

- source-policy review;
- endpoint verification;
- technical testing;
- persistence analysis;
- classification design;
- implementation decisions.

## 3. Resolve Italian Tech Alliance Only If It Remains High ROI

Do not repeat basic research.

Evaluate actual differentiated value, repetition and likely report contribution.

It should not displace stronger newly identified candidates merely because it is already partly audited.

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
- source-specific date scrapers;
- source-specific content-persistence exceptions;

unless repeated evidence validates the need.

## 5. Improve Source Diversity Only Through Better Coverage

No artificial quotas.

Do not target a fixed number of sources per domain.

A domain should have differentiated information roles where feasible.

## 6. Evaluate the Source-Expansion / Richer-Context Crossover

After the next source-research batch, explicitly ask:

> **Would another source improve the product more than making each selected item materially more understandable without click-through?**

This is the Phase 4 exit question.

Source expansion should not become endless.

## 7. Design Richer Report Context After Source Correction

The report should eventually provide materially more context below the relevance score.

The existing short feed-description model is not the final product experience.

Do not redesign summarization while source selection is still changing materially.

## 8. Revisit Ranking Only If Upstream Corrections Are Insufficient

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

- twelve active public RSS sources;
- ten active topic domains;
- all ten strategic macroareas implemented;
- Sifted replaced by Tech.eu;
- Tech.eu has no blanket source default;
- Financial Markets implemented conservatively;
- Federal Reserve Board Monetary Policy active as Tier 1 US monetary-policy evidence;
- Milan and Bocconi Ecosystem implemented through Tech Europe Foundation;
- TEF uses a validated source-defined domain with an empty keyword list;
- Italy implemented as the tenth domain;
- MIMIT News active as Tier 1 Italian industrial/company-policy evidence;
- Lavoce.info Imprese active as Tier 2 independent Italian business analysis;
- Italy uses a validated source-defined domain with an empty keyword list;
- Italian-language classification tested through live samples and historical regression;
- generic HTML-to-text feed-description normalisation implemented and validated;
- Google DeepMind News active as a second Tier 1 frontier-lab AI source;
- OpenAI + DeepMind now provide differentiated primary AI coverage;
- Nasdaq remains standby because of access/persistence conflict;
- Bruegel remains strategically valuable but its useful feeds are incompatible with the current parsing/persistence architecture;
- Assolombarda remains strategically valuable but current feeds lack usable publication timestamps and raise persistence concerns;
- Ars Technica remains standby because current persistence rights are insufficiently compatible;
- Federal Reserve Banking/Regulatory remains standby;
- MIMIT Incentives remains standby;
- Lavoce Banche e finanza remains standby;
- real twelve-source production-equivalent run completed successfully on 18 August 2026;
- that run produced:
  - 12 active sources;
  - 12 successful sources;
  - 0 failed sources;
  - 0 invalid records;
  - 0 warnings;
  - successful pipeline status.

**Immediate information-policy next step:**

> **Use the updated canonical state to commission a fresh Career Agent source-research pass against the remaining information-function gaps.**

After that research:

1. return the research to the Development project;
2. create a clean new-chat handoff;
3. audit newly justified candidates one at a time;
4. reassess whether further source expansion still has higher value than richer report context.

Do not re-audit closed sources unless materially new evidence changes their viability.

---

# Changelog

## 2026-08-18 — Twelve-Source / Ten-Domain Checkpoint and First Gap-Driven Audit Batch Closeout

- Updated production state from eight to twelve active public RSS sources.
- Updated implemented taxonomy from nine to ten active domains.
- Implemented Italy as the tenth strategic macroarea.
- Added Federal Reserve Board Monetary Policy as a Tier 1 source with Economics/Macro source default.
- Added `FOMC`, `Federal Open Market Committee` and `discount rate` to Financial Markets after controlled testing and historical regression.
- Added MIMIT News as a Tier 1 Italy source.
- Added narrow Italian Companies/Corporate Strategy terms:
  - `tavoli di crisi`;
  - `accordo di sviluppo`;
  - `quadro industriale`;
  - `rilevanza strategica`.
- Added `inflazione` to Economics/Macro after MIMIT testing.
- Implemented generic HTML-to-text feed-description normalisation rather than a MIMIT-specific branch.
- Added Lavoce.info Imprese as a Tier 2 Italy source.
- Added:
  - `fusione e acquisizione`;
  - `piano industriale`;
  - `IA`;
  - `mercati dei capitali`.
- Validated the retained Lavoce keywords against historical processed records with zero unintended regressions.
- Added Google DeepMind News as a Tier 1 Artificial Intelligence source.
- Validated 100/100 DeepMind records as appropriate for the AI source default.
- Added no new DeepMind-specific keywords because existing classification was sufficient.
- Closed Nasdaq as standby under current access/persistence terms.
- Closed Bruegel general RSS as rejected for production because of event/session noise.
- Kept Bruegel Analysis and Publications on standby because malformed feeds also expose excessive/full-content payloads incompatible with current public persistence.
- Kept Assolombarda News and Comunicati stampa on standby because both tested feeds exposed 0/15 publication timestamps and substantive copyrighted descriptions.
- Kept Assolombarda Centro Studi in the manual/research layer because no public RSS/feed route was identified.
- Kept Ars Technica on standby because current terms do not provide a clean basis for permanent public-RSS persistence.
- Kept Federal Reserve Banking/Regulatory, MIMIT Incentives and Lavoce Banche e finanza on standby.
- Completed a real twelve-source production-equivalent run successfully on 18 August 2026 with:
  - twelve successful sources;
  - zero failed sources;
  - zero invalid records;
  - zero warnings.
- Reframed Financial Markets from "no dedicated source" to "dedicated monetary/rates evidence exists; broader market coverage remains incomplete."
- Reframed Companies/Corporate Strategy from a severe general gap to a materially improved but still globally incomplete domain.
- Reframed Artificial Intelligence from OpenAI-concentrated primary evidence to diversified OpenAI + DeepMind primary evidence, with independent scrutiny still missing.
- Reframed Italy from pending to implemented and useful, while preserving remaining maturity gaps.
- Retired the completed Nasdaq-to-DeepMind audit queue.
- Set the next source step as a fresh Career Agent research pass against current information-function gaps.
- Added an explicit Phase 4 crossover question: whether another source now has more expected product value than richer report context.

## 2026-08-17 — Source-Audit Consolidation, Milan/Bocconi Activation and New Expansion Queue

- Consolidated completed source-accessibility and policy research.
- Recorded the Bocconi access model and Premium Bocconi Exception.
- Implemented Tech Europe Foundation as the first Milan/Bocconi Ecosystem source.
- Added support for source-defined domains with empty keyword lists.
- Recorded Financial Times, Il Sole 24 Ore, Reuters, Bank of Italy, Bocconi and Italian Tech Alliance audit conclusions.
- Established the first gap-driven candidate queue:
  - Nasdaq;
  - Federal Reserve;
  - MIMIT;
  - Lavoce.info;
  - Bruegel;
  - Assolombarda;
  - Ars Technica;
  - Google DeepMind.
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
- Implemented Financial Markets with a conservative first keyword set.
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