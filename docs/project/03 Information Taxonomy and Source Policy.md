# Daily Intelligence System — Information Taxonomy and Source Policy

> **Purpose**
>
> This document defines what information the Daily Intelligence System should collect, how it should classify that information, which sources are acceptable, and which rules govern source selection, storage and public presentation.
>
> It is the quality-control framework for the information entering the system.
>
> ---
>
> **Primary Question**
>
> > *What information should the system collect, from which sources, and under which classification and quality rules?*
>
> ---
>
> **Update Frequency**
>
> Update when monitored domains, source-selection rules, metadata requirements or source-governance policies materially change.

---

# Information Objective

The system should provide broad but structured awareness of developments that may affect:

- economics;
- politics and geopolitics;
- financial markets;
- companies and industries;
- artificial intelligence;
- technology and software;
- startups and venture capital;
- Europe and the European Union;
- Italy;
- Milan and the Bocconi ecosystem.

The objective is not maximum coverage.

The objective is to identify a manageable set of high-value items from transparent and credible sources.

Information quality should be evaluated through:

1. relevance;
2. source credibility;
3. originality;
4. timeliness;
5. diversity;
6. transparency;
7. accessibility;
8. suitability for automated collection.

---

# Taxonomy Principles

## Configurable

Domains, keywords, entities, source tiers and geographic priorities should be maintained through configuration rather than embedded throughout the codebase.

## Multi-Domain

A single item may legitimately belong to more than one domain.

For example:

- an EU AI regulation may belong to Artificial Intelligence, Technology, Europe and Politics;
- a central-bank rate decision may belong to Economics, Financial Markets and Europe;
- a startup acquisition may belong to Startups, Corporate Strategy and Technology.

## Explainable

The system should be able to show why an item received a domain classification.

Classification should depend on visible factors such as:

- source defaults;
- title keywords;
- description keywords;
- tracked entities;
- geographic references;
- explicitly configured rules.

## Conservative

The system should prefer an unclassified or uncertain result over a misleading classification.

## Broad but Bounded

The taxonomy should preserve awareness across several domains without becoming an attempt to categorise every possible news topic.

## Independent Dimensions

Topic, geography, source tier and content type should be stored as separate dimensions.

An item can therefore be described as:

- topic: Artificial Intelligence;
- geography: United States and Global;
- source tier: Tier 1;
- content type: Company Announcement.

---

# Initial Topic Domains

The following domains form the initial taxonomy.

---

## 1. Global Politics and Geopolitics

### Scope

Major political, diplomatic, security and geopolitical developments with international relevance.

### Include

- elections with significant national or international consequences;
- wars, conflicts and peace negotiations;
- sanctions;
- trade disputes;
- diplomatic agreements;
- changes in government;
- major foreign-policy decisions;
- defence and security developments;
- political instability;
- geopolitical risks affecting markets, technology or supply chains.

### Exclude or Deprioritise

- routine political commentary;
- minor party disputes;
- personality-driven political coverage without broader implications;
- local political stories with no material connection to monitored priorities;
- opinion content that introduces no new evidence.

### Example Indicators

- election;
- government;
- sanctions;
- conflict;
- ceasefire;
- trade restriction;
- diplomatic agreement;
- defence;
- security;
- parliament;
- presidency;
- ministry.

---

## 2. Economics and Macroeconomics

### Scope

Developments affecting economic conditions, policy, growth, employment, inflation, trade and public finances.

### Include

- inflation data;
- GDP and economic growth;
- employment and unemployment;
- interest-rate decisions;
- monetary policy;
- fiscal policy;
- government budgets;
- public debt;
- international trade;
- productivity;
- industrial production;
- economic forecasts;
- major research from central banks and statistical agencies.

### Exclude or Deprioritise

- generic personal-finance content;
- unsupported economic predictions;
- routine commentary without new data;
- minor statistical releases with limited relevance.

### Example Indicators

- inflation;
- GDP;
- unemployment;
- interest rates;
- central bank;
- fiscal policy;
- monetary policy;
- productivity;
- public debt;
- trade balance;
- recession;
- economic forecast.

---

## 3. Financial Markets

### Scope

Major developments affecting listed securities, capital markets, asset allocation and financial-system conditions.

### Include

- significant market movements with identifiable causes;
- equity, bond, currency and commodity developments;
- central-bank effects on markets;
- major earnings surprises;
- market-structure changes;
- financial instability;
- liquidity and credit conditions;
- asset-management developments;
- material investment-industry changes.

### Exclude or Deprioritise

- routine daily price movements without explanation;
- speculative trading tips;
- unverified market rumours;
- promotional investment content;
- individual stock commentary without broader relevance.

### Example Indicators

- equities;
- bonds;
- yields;
- currencies;
- commodities;
- volatility;
- earnings;
- asset management;
- capital markets;
- credit;
- liquidity;
- market sell-off;
- market rally.

---

## 4. Companies and Corporate Strategy

### Scope

Important company actions and industry developments that reveal changes in strategy, competition or capital allocation.

### Include

- mergers and acquisitions;
- strategic partnerships;
- major product launches;
- restructurings;
- market entry or exit;
- significant leadership changes;
- major investments;
- bankruptcies;
- layoffs with strategic relevance;
- supply-chain decisions;
- material earnings or strategic guidance;
- competitive changes.

### Exclude or Deprioritise

- routine product promotions;
- minor executive appointments;
- small operational updates;
- marketing announcements without strategic relevance;
- company content with no meaningful new information.

### Example Indicators

- acquisition;
- merger;
- partnership;
- restructuring;
- investment;
- divestment;
- market entry;
- bankruptcy;
- earnings guidance;
- chief executive;
- strategic plan.

---

## 5. Artificial Intelligence

### Scope

Developments concerning AI models, products, research, infrastructure, regulation, adoption and business impact.

### Include

- major model releases;
- AI product launches;
- model evaluation and safety research;
- enterprise adoption;
- AI regulation;
- compute and semiconductor developments;
- agentic systems;
- AI infrastructure;
- significant funding and acquisitions;
- AI governance;
- major research papers;
- changes in AI economics or business models.

### Exclude or Deprioritise

- superficial AI product announcements;
- minor wrappers without differentiated value;
- generic prompt collections;
- unsupported claims about artificial general intelligence;
- repetitive commentary with no technical or commercial evidence.

### Example Indicators

- artificial intelligence;
- machine learning;
- large language model;
- foundation model;
- inference;
- training;
- agent;
- AI regulation;
- model evaluation;
- AI safety;
- compute;
- GPU;
- semiconductor.

---

## 6. Technology and Software

### Scope

Major developments in software, cloud infrastructure, cybersecurity, data systems and digital platforms.

### Include

- important software-platform changes;
- cloud and infrastructure developments;
- cybersecurity incidents;
- major developer-tool changes;
- enterprise-software developments;
- APIs and platform ecosystems;
- data infrastructure;
- digital regulation;
- significant open-source developments;
- technology-industry strategy.

### Exclude or Deprioritise

- routine consumer-device rumours;
- small software updates;
- generic tutorials;
- promotional technology content;
- minor feature releases with no broader importance.

### Example Indicators

- cloud;
- software;
- cybersecurity;
- data platform;
- database;
- API;
- developer tools;
- open source;
- enterprise software;
- infrastructure;
- privacy;
- digital platform.

---

## 7. Startups and Venture Capital

### Scope

Developments affecting startup formation, financing, scaling, exits and venture-capital ecosystems.

### Include

- significant funding rounds;
- new funds;
- acquisitions and exits;
- startup failures;
- accelerator and incubator developments;
- ecosystem policy;
- venture-capital strategy;
- founder and operator insights supported by evidence;
- business-model changes;
- European and Italian startup developments.

### Exclude or Deprioritise

- very small funding announcements without strategic relevance;
- promotional founder profiles;
- unverified fundraising rumours;
- generic entrepreneurship advice;
- content designed mainly to sell startup services.

### Example Indicators

- startup;
- venture capital;
- funding round;
- seed;
- Series A;
- accelerator;
- incubator;
- acquisition;
- exit;
- founder;
- venture fund;
- portfolio company.

---

## 8. Europe and the European Union

### Scope

Major European institutional, economic, political, regulatory and industrial developments.

### Include

- EU legislation;
- European Commission initiatives;
- European Central Bank actions;
- European Parliament decisions;
- European industrial policy;
- competition policy;
- digital regulation;
- trade policy;
- major cross-European economic developments;
- strategically relevant national developments.

### Exclude or Deprioritise

- minor national stories with no wider relevance;
- routine institutional communications;
- political commentary without new policy or evidence.

### Example Indicators

- European Union;
- European Commission;
- European Parliament;
- European Central Bank;
- euro area;
- European Council;
- EU regulation;
- European industry;
- single market.

---

## 9. Italy

### Scope

Italian developments with economic, political, technological, financial or career relevance.

### Include

- major government policy;
- Italian economic indicators;
- industrial-policy decisions;
- important company developments;
- banking and financial-sector developments;
- technology and startup ecosystem news;
- labour-market developments;
- regulatory changes;
- strategic infrastructure projects.

### Exclude or Deprioritise

- local crime;
- celebrity news;
- sport;
- routine party conflict;
- local stories without economic or professional relevance.

### Example Indicators

- Italy;
- Italian government;
- Bank of Italy;
- ISTAT;
- Milan;
- Italian companies;
- Italian economy;
- Italian startups;
- Italian regulation.

---

## 10. Milan and Bocconi Ecosystem

### Scope

High-value opportunities, events and developments connected to Milan, Bocconi University and relevant professional communities.

### Include

- selective public events;
- student-association opportunities;
- research opportunities;
- competitions;
- startup and innovation programmes;
- finance, consulting, AI and data events;
- B4i and related initiatives;
- public lectures;
- application deadlines;
- ecosystem programmes with meaningful learning or networking value.

### Exclude or Deprioritise

- generic social events;
- low-quality networking events;
- routine university communications;
- events with unclear participants or weak relevance;
- opportunities requiring excessive time without meaningful output.

### Example Indicators

- Bocconi;
- B4i;
- Milan;
- student association;
- career event;
- research assistant;
- competition;
- hackathon;
- accelerator;
- innovation programme;
- public lecture.

---

# Geographic Classification

Geography should be stored separately from topic domains.

Initial geographic tags may include:

- Global;
- European Union;
- Europe — Non-EU;
- Italy;
- Milan;
- United States;
- China;
- United Kingdom;
- Other named country or region.

An item may have more than one geographic tag.

For example:

- a trade dispute between the United States and China may receive both country tags and Global;
- an Italian implementation of an EU regulation may receive Italy and European Union;
- a Milan startup funding round may receive Milan and Italy.

Geographic priority should affect ranking only through explicit configuration.

---

# Content Types

Where practical, each item should receive one content-type label.

Initial content types:

| Content Type | Meaning |
|---|---|
| Official Announcement | Publication from a government, institution, regulator or company |
| Data Release | Statistical or economic data |
| Research | Academic, policy or technical research |
| News Reporting | Original journalistic reporting |
| Analysis | Evidence-based interpretation |
| Opinion | Argument or commentary |
| Company Update | Corporate communication |
| Funding or Transaction | Funding, acquisition, merger or exit |
| Event or Opportunity | Programme, event, competition or application |
| Technical Release | Model, software, platform or infrastructure release |
| Other | Content not fitting the configured categories |

Opinion should normally receive a lower default ranking than original reporting or primary evidence unless there is a specific reason otherwise.

---

# Source Hierarchy

Source tier represents evidentiary role and expected reliability. It does not guarantee that every item from the source is important or correct.

---

## Tier 1 — Primary and Official Sources

### Definition

Sources that directly produce the underlying decision, data, research, product or announcement.

### Examples of Source Types

- governments;
- regulators;
- central banks;
- statistical agencies;
- European institutions;
- company investor-relations pages;
- official company blogs;
- research laboratories;
- universities;
- original research publications;
- recognised international institutions.

### Strengths

- closest to the original evidence;
- authoritative for official decisions and data;
- lower risk of reporting distortion.

### Limitations

- may be promotional;
- may omit criticism or context;
- may publish technical material that is difficult to interpret;
- official status does not guarantee practical relevance.

### Policy

Tier 1 sources should be prioritised for confirmation and factual grounding.

They should not automatically receive the highest relevance score for every item.

---

## Tier 2 — High-Quality Reporting

### Definition

Established journalistic organisations that produce original reporting, verification and context.

### Strengths

- independent reporting;
- broader context;
- professional editorial standards;
- useful synthesis of complex developments.

### Limitations

- some content may be paywalled;
- headlines may still optimise for attention;
- access to full content may vary;
- different publications have different geographic and editorial biases.

### Policy

Tier 2 sources should form a major part of the daily source universe.

The system should store only permitted metadata and short feed-provided descriptions.

---

## Tier 3 — Specialist Analysis

### Definition

Specialist organisations, newsletters, venture funds, research groups, industry publications and expert technical sources.

### Strengths

- subject-matter depth;
- early identification of sector changes;
- practitioner insight;
- coverage missed by general publications.

### Limitations

- possible commercial incentives;
- narrower perspective;
- inconsistent editorial standards;
- promotional or portfolio bias.

### Policy

Tier 3 sources should be selected individually based on demonstrated quality.

Their analysis should be distinguishable from primary evidence.

---

## Tier 4 — Discovery Sources

### Definition

Aggregators, community platforms, social-media accounts, forums and other sources useful primarily for discovering possible stories.

### Strengths

- speed;
- breadth;
- detection of emerging discussions.

### Limitations

- weak verification;
- duplication;
- manipulation risk;
- unclear authorship;
- unstable access.

### Policy

Tier 4 sources are outside the initial MVP unless a specific structured source proves unusually valuable.

A Tier 4 source should not be the sole evidence supporting an important item.

---

# Source Inclusion Criteria

A source should normally satisfy most of the following conditions.

## Relevance

The source consistently publishes information related to one or more monitored domains.

## Credibility

The publisher has identifiable ownership, authorship or institutional responsibility.

## Originality

The source provides primary information, original reporting or meaningful specialist analysis.

## Structured Access

The source provides a stable RSS feed, Atom feed, official API or other approved structured endpoint.

## Timeliness

Publication timestamps are available and reasonably reliable.

## Metadata Quality

Titles, URLs and descriptions are sufficiently complete for automated processing.

## Public Accessibility

The system can legally and technically access the relevant metadata without private credentials.

## Stability

The endpoint is not excessively unstable or dependent on fragile browser behaviour.

## Value-to-Noise Ratio

A meaningful proportion of the source’s output is relevant to the project.

## Diversity Contribution

The source adds geographic, institutional, ideological, industry or technical diversity.

## Public Repository Compatibility

Storing its permitted metadata and links does not create an obvious copyright or privacy problem.

---

# Source Exclusion Criteria

A source should be rejected or disabled when one or more of the following materially apply.

- It requires prohibited scraping.
- It requires paid API access.
- It requires private account access for core collection.
- It republishes content without meaningful added value.
- It produces excessive promotional material.
- Its publication timestamps are unusable.
- It repeatedly generates malformed or misleading records.
- It has weak or unclear ownership.
- It primarily publishes rumours or unsupported claims.
- It systematically duplicates higher-quality sources.
- Its content is outside monitored domains.
- Its endpoint is too unstable for the value it provides.
- It creates copyright or privacy risks for the public repository.
- It consistently produces low-value items during evaluation.

---

# Initial Source-Universe Strategy

The MVP should begin with a deliberately limited source universe.

## Target Size

Initial target:

- approximately 20–30 active sources;
- enough to test every monitored domain;
- small enough to inspect manually during development.

This is a planning range, not a fixed requirement.

## Balance

The initial universe should include a mix of:

- primary institutions;
- high-quality general reporting;
- specialist AI and technology sources;
- startup and venture-capital sources;
- European institutions;
- Italian sources;
- Milan or Bocconi opportunity sources.

## Principle

A smaller high-quality source universe is preferable to a large unreviewed list.

Source expansion should follow demonstrated coverage gaps.

---

# Source Registry Requirements

The final source registry should support fields such as:

```text
id
name
feed_url
homepage_url
source_type
source_tier
default_domains
language
country
geographic_scope
active
notes