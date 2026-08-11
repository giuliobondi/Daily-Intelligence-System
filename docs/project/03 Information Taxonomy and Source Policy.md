````markdown
# Daily Intelligence System — Information Taxonomy and Source Policy

> **Purpose**
>
> This document defines what information the Daily Intelligence System should collect, how that information should be classified, which sources are acceptable, and which rules govern source selection, storage and public presentation.
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

The system should prefer a smaller set of high-quality sources and useful items over broad but noisy coverage.

---

# Current Implementation Status

The full taxonomy and source policy in this document define the intended information model.

The current implementation deliberately remains narrower than the complete target model.

At Phase 2 closeout, the implemented configuration contains:

- seven active validated public RSS sources;
- seven active topic domains;
- deterministic title and description keyword rules;
- optional source-default domains;
- deterministic source-tier scoring;
- exact duplicate reduction;
- a previous-24-hours publication window;
- explicit handling of unclassified records;
- no tracked-entity configuration;
- no article-level geographic classification;
- no content-type classification;
- no near-duplicate clustering;
- no multi-source story clustering.

The current active real-source registry contains:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Sifted.

The current implemented topic domains are:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Companies and Corporate Strategy;
4. Artificial Intelligence;
5. Technology and Software;
6. Startups and Venture Capital;
7. Europe and the European Union.

The following target domains remain unimplemented:

- Financial Markets;
- Italy;
- Milan and Bocconi Ecosystem.

This seven-source, seven-domain configuration is sufficient for the first production-automation phase.

It should not be interpreted as the final information universe.

Source and taxonomy expansion should continue only when repeated real reports demonstrate a meaningful coverage or quality gap.

---

# Taxonomy Principles

## Configurable

Domains, keywords, source tiers and other future classification signals should be maintained through configuration rather than embedded throughout core processing code.

Configuration should expand only when the corresponding processing behaviour is actually needed.

---

## Multi-Domain

A single item may legitimately belong to more than one domain.

For example:

- an EU AI regulation may belong to Artificial Intelligence, Technology, Europe and Politics;
- a central-bank rate decision may belong to Economics, Financial Markets and Europe;
- a startup acquisition may belong to Startups, Corporate Strategy and Technology.

The current implementation supports multiple domains.

---

## One Primary Report Placement

A multi-domain record should appear once in the main report.

Current policy:

- the first assigned eligible domain becomes the primary report section;
- additional domains are displayed as secondary metadata.

This avoids unnecessary repetition while preserving cross-domain information.

The primary-domain selection method may later become more sophisticated if real usage demonstrates a need.

---

## Explainable

The system should be able to show why an item received a classification.

Current classification evidence includes:

- source defaults;
- matched configured keywords.

Future classification evidence may include:

- entities;
- geography;
- content type;
- exclusions;
- stronger rule groups.

Any future classification mechanism should remain inspectable.

---

## Conservative

The system should prefer an unclassified result over a misleading classification.

Unclassified records:

- remain valid processed records;
- remain available for evaluation;
- are omitted from the main report by default.

Phase 2 real-report review confirmed that this principle is preferable to forcing broad feeds into publisher-level topic categories.

A high relevant-unclassified rate during production evaluation should trigger taxonomy review.

---

## Broad but Bounded

The target taxonomy should preserve awareness across several strategically useful domains without trying to classify every possible news topic.

The system should not become a generic global news taxonomy.

---

## Independent Dimensions

Topic, geography, source tier and content type are conceptually separate dimensions.

For example, an item might eventually be described as:

```text
topic: Artificial Intelligence
geography: European Union
source tier: Tier 1
content type: Official Announcement
```

Only topic classification and source tier are currently implemented at article level.

Source-level geographic scope exists in configuration.

Article-level geographic classification and content type remain future optional dimensions.

---

# Target Topic Taxonomy

The following ten domains define the intended strategic coverage.

They are target information categories.

Seven are currently implemented.

Three remain deferred until real usage demonstrates a need.

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
- major changes in government;
- major foreign-policy decisions;
- defence and security developments;
- political instability;
- geopolitical risks affecting markets, technology or supply chains.

### Exclude or Deprioritise

- routine political commentary;
- minor party disputes;
- personality-driven political coverage without broader implications;
- local political stories with no material connection to monitored priorities;
- opinion content that introduces no meaningful evidence.

### Example Indicators

Conceptually relevant indicators include:

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

Not every conceptual indicator should automatically become an implemented keyword.

### Current Status

**Implemented**

The current configured keyword list is deliberately conservative.

During Phase 2, real BBC World records exposed a recall gap.

Candidate keywords were simulated against the actual processed sample before configuration was changed.

The following terms were added because they recovered clearly relevant political or geopolitical stories without observed false positives in that sample:

- war;
- conflict;
- parliament.

Broader candidates such as:

- government;
- defence;
- president;
- prime minister;

were tested but not added because they produced ambiguous or low-value matches.

This domain should continue to expand from observed classification errors rather than by copying the entire conceptual indicator list into configuration.

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

### Current Status

**Implemented**

The current keyword list remains intentionally small and deterministic.

Istat Press Releases currently has this domain as a source default because the selected feed is sufficiently narrow for the default to be treated as genuine source-wide topical evidence.

BBC Business does not receive an Economics default because Phase 2 showed that the feed contains many business and general-interest stories that are not meaningfully macroeconomic.

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

### Current Status

**Not yet implemented**

The domain remains part of the target taxonomy.

Phase 2 did not demonstrate that it was necessary for the first automation milestone.

Implement only when repeated real reports show that meaningful financial-market developments are being missed or badly classified.

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

### Current Status

**Implemented**

This domain relies on content evidence rather than broad source defaults in the current real-source registry.

Phase 2 showed that assigning BBC Business or OpenAI a blanket Companies and Corporate Strategy default inflated classifications and scores for unrelated stories.

The current policy therefore avoids those broad defaults.

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

### Current Status

**Implemented**

Current configured keywords include concepts such as:

- artificial intelligence;
- AI;
- machine learning;
- large language model;
- foundation model;
- model release.

The current list is intentionally small and provisional.

OpenAI News has Artificial Intelligence as its single source default because the selected feed has a sufficiently strong source-wide topical relationship to AI.

OpenAI does not receive automatic Technology or Corporate Strategy defaults.

Those additional domains require content evidence.

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

### Current Status

**Implemented**

Current configured keywords include concepts such as:

- software;
- cloud;
- cybersecurity;
- developer;
- open source;
- API.

The current list is intentionally small and provisional.

No current real source receives Technology as a blanket source default.

Technology should be assigned from content evidence unless a future source is sufficiently narrow to justify a source-wide default.

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

### Current Status

**Implemented**

Sifted currently has Startups and Venture Capital as its single source default.

This reflects the selected feed's sufficiently narrow startup and venture-capital focus.

Sifted does not automatically receive Technology or Companies and Corporate Strategy.

Those domains require content evidence.

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

### Current Status

**Implemented**

Neither the European Central Bank feed nor the European Commission Highlighted News feed receives Europe/EU as a blanket source default.

Phase 2 demonstrated why source identity alone should not imply item importance or topical relevance.

For example, a routine ECB concert announcement should not automatically enter an Economics or Europe section merely because the publisher is the ECB.

Europe/EU classification therefore relies on content evidence unless a future source is narrow enough to justify otherwise.

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

### Current Status

**Not yet implemented**

Istat currently contributes through Economics and Macroeconomics while its source-level `geographic_scope` records Italy.

A separate Italy topic domain should be implemented only if real reports demonstrate that geography metadata plus existing topic domains are insufficient.

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

### Current Status

**Not yet implemented**

Phase 2 source research did not identify a sufficiently strong, stable public structured source that justified adding this domain to the current production-like configuration.

Do not compensate for the absence of a suitable structured source with scraping, manual copy-and-paste or a dedicated complex ingestion system.

---

# Geographic Classification

Geography remains a target information dimension but is not currently implemented at article level in the processing pipeline.

Source configuration currently preserves `geographic_scope`.

Potential article-level geographic tags include:

- Global;
- European Union;
- Europe — Non-EU;
- Italy;
- Milan;
- United States;
- China;
- United Kingdom;
- other named country or region.

An item may eventually receive multiple geographic tags.

Examples:

- a trade dispute between the United States and China may receive both country tags and Global;
- an Italian implementation of an EU regulation may receive Italy and European Union;
- a Milan startup funding round may receive Milan and Italy.

Article-level geographic classification should be introduced only if real use shows that topic domains plus source-level geography are insufficient for prioritisation or browsing.

Geography should remain conceptually independent from topic domains.

---

# Content Types

Content-type classification is not currently implemented.

Potential future types include:

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
| Other | Content not fitting configured categories |

This dimension should not be implemented merely because it appears in the target information model.

Add it only if production report quality or ranking materially benefits from it.

---

# Source Hierarchy

Source tier represents evidentiary role and expected reliability.

It does not guarantee that every item from the source is important or correct.

The current ranking system uses source tier as one deterministic input.

---

## Tier 1 — Primary and Official Sources

### Definition

Sources that directly produce the underlying decision, data, research, product or announcement.

### Examples

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

- close to original evidence;
- authoritative for official decisions and data;
- lower risk of reporting distortion.

### Limitations

- may be promotional;
- may omit criticism or context;
- may publish technical material that is difficult to interpret;
- official status does not guarantee practical relevance.

### Policy

Tier 1 sources should be prioritised for factual grounding.

They should not automatically outrank every other item regardless of relevance.

Phase 2 directly confirmed this principle: a Tier 1 official source can publish an item that is operationally valid but strategically irrelevant.

---

## Tier 2 — High-Quality Reporting

### Definition

Established journalistic or specialist reporting organisations that provide original reporting, verification or useful professional context.

### Strengths

- independent reporting;
- broader context;
- professional editorial standards;
- useful synthesis of complex developments.

### Limitations

- some content may be paywalled;
- metadata availability varies;
- different publications have different geographic and editorial biases;
- specialist publications may have narrower coverage.

### Policy

Tier 2 sources are part of the current real-source universe.

The system should store only permitted metadata and short feed-provided descriptions.

---

## Tier 3 — Specialist Analysis

### Definition

Specialist organisations, newsletters, venture funds, research groups, industry publications and expert technical sources that do not meet the current Tier 2 role.

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

Tier 3 sources should be approved individually based on demonstrated quality.

No current active source is configured as Tier 3.

---

## Tier 4 — Discovery Sources

### Definition

Aggregators, community platforms, social-media accounts, forums and similar discovery-oriented sources.

### Strengths

- speed;
- breadth;
- detection of emerging discussions.

### Limitations

- weak verification;
- duplication;
- manipulation risk;
- unclear authorship;
- unstable structured access.

### Policy

Tier 4 sources are outside the current production-like scope unless a specific structured source proves unusually valuable.

A Tier 4 source should not be the sole evidence supporting an important item.

---

# Current Source-Tier Scoring

The current provisional ranking configuration assigns:

```text
Tier 1 = 4 points
Tier 2 = 3 points
Tier 3 = 2 points
Tier 4 = 1 point
```

Source tier is only one score component.

Current scoring also includes:

- 2 points per assigned domain;
- 1 point per matched keyword.

These weights remain provisional.

Phase 2 showed that misleading domain assignment can distort relevance score even when the ranking formula itself is functioning correctly.

The preferred response is to fix bad classification evidence before changing score weights.

Ranking weights should be reconsidered only after repeated automated reports provide longitudinal evidence.

---

# Source Inclusion Criteria

A production source should normally satisfy most of the following conditions.

## Relevance

The source consistently publishes information related to one or more monitored domains.

## Credibility

The publisher has identifiable ownership, authorship or institutional responsibility.

## Originality

The source provides primary information, original reporting or meaningful specialist analysis.

## Structured Access

The source provides:

- stable RSS;
- Atom;
- official API;
- another explicitly approved structured endpoint.

## Timeliness

Publication timestamps are available and reasonably reliable.

Because the current system filters using `published_at`, timestamp quality is particularly important.

## Metadata Quality

Titles and URLs must be sufficiently complete for automated processing.

Descriptions are useful but may be absent.

Phase 2 confirmed that some valid feeds omit descriptions entirely or for individual entries.

## Public Accessibility

The relevant metadata can be accessed without private credentials.

## Stability

The endpoint is sufficiently stable for low-maintenance automated collection.

## Value-to-Noise Ratio

A meaningful proportion of output is relevant to the project.

## Diversity Contribution

The source adds useful:

- geographic;
- institutional;
- industry;
- technical;
- evidentiary;
- perspective diversity.

## Public Repository Compatibility

Permitted metadata and links can be stored safely in a public repository.

## Operational Compatibility

The source should work with the bounded current collector without disproportionate special handling.

A source that requires excessive exception logic should normally be reconsidered before the collector is made more complex.

---

# Source Exclusion Criteria

A source should be rejected, disabled or removed when one or more of the following materially apply:

- it requires prohibited scraping;
- it requires paid API access for core operation;
- it requires private account access;
- it republishes content without meaningful added value;
- it produces excessive promotional material;
- its publication timestamps are unusable for the collection-window policy;
- it repeatedly generates malformed or misleading records;
- it has weak or unclear ownership;
- it primarily publishes unsupported rumours;
- it systematically duplicates better sources;
- its content falls outside monitored priorities;
- its endpoint is too unstable for the value provided;
- it creates copyright or privacy risk;
- maintaining it requires disproportionate manual intervention.

A low-quality source should normally be removed rather than supported through increasingly complex code.

---

# Current Production-Like Source Universe

The previous planning range of approximately 20–30 sources should not be treated as an implementation target.

Phase 2 validated a deliberately small seven-source set.

The current source universe is sufficient for the first GitHub Actions automation milestone.

## Active Sources

| Source ID | Source | Tier | Default Domains | Language | Geographic Scope |
|---|---|---:|---|---|---|
| `bbc_world` | BBC News World | 2 | None | English | Global |
| `bbc_business` | BBC News Business | 2 | None | English | Global |
| `ecb_press` | European Central Bank | 1 | None | English | European Union; Euro Area |
| `ec_highlights` | European Commission Highlighted News | 1 | None | English | European Union |
| `istat_press_en` | Istat Press Releases | 1 | Economics and Macroeconomics | English | Italy |
| `openai_news` | OpenAI News | 1 | Artificial Intelligence | English | Global |
| `sifted_articles` | Sifted | 2 | Startups and Venture Capital | English | Europe |

All current active sources:

- are public;
- require no paid API;
- require no private credentials;
- expose structured RSS metadata;
- were successfully collected through the actual project collector during Phase 2;
- exposed usable publication timestamps in the tested sample.

## Why These Sources Are Useful

The current set is not merely a prestige list.

Each source contributes a different information or system-testing role.

| Source | Primary Role |
|---|---|
| BBC News World | Broad international reporting and geopolitical relevance filtering |
| BBC News Business | Broad business reporting and content-based classification |
| European Central Bank | Primary institutional evidence and authority-versus-importance testing |
| European Commission Highlighted News | Primary European policy and institutional material |
| Istat Press Releases | Primary Italian statistical and macroeconomic releases |
| OpenAI News | Primary AI company announcements and source-bias awareness |
| Sifted | European startup and venture-capital specialist coverage |

The set includes:

- primary institutional sources;
- primary company information;
- general reporting;
- business reporting;
- specialist startup reporting;
- European coverage;
- Italian economic coverage;
- AI coverage.

It is small enough for human inspection while spanning several source roles.

## Expansion Rule

Do not expand this set merely because more feeds exist.

Add a source only when it solves a demonstrated:

- coverage gap;
- evidentiary gap;
- geographic gap;
- domain gap;
- source-diversity problem;
- opportunity-detection gap.

A smaller high-quality source universe remains preferable to a large unreviewed list.

---

# Source-Default Domain Policy

Source defaults are classification evidence.

They are not publisher categories.

A source should receive a default domain only when essentially every item in the selected feed can reasonably be treated as belonging to that topic.

This distinction is critical because the current ranking system gives points for every assigned domain and the first assigned domain determines primary report placement.

## Broad Sources

Broad heterogeneous feeds should normally use:

```yaml
default_domains: []
```

Current broad sources with no defaults are:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News.

This does not mean those publishers lack topical identity.

It means source identity alone is insufficient evidence to classify every individual item.

## Narrow Sources

Current narrow source defaults are:

- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

No current source receives multiple blanket defaults.

Additional domains must come from content evidence.

## Phase 2 Evidence

The first real report used broader source defaults.

That produced misleading results including:

- unrelated BBC Business items appearing under Economics;
- an ECB concert announcement appearing under Economics and Europe/EU;
- inflated relevance scores caused by default domains rather than article content.

The correction was to permit explicitly empty `default_domains` and remove weak defaults from broad feeds.

This materially improved report precision.

The rule going forward is:

> use a source default only when it represents a genuine source-wide topical guarantee.

---

# Source Registry

## Current Implemented Fields

The current source configuration supports:

```text
id
name
feed_url
source_type
source_tier
default_domains
language
geographic_scope
active
```

These fields are sufficient for the current deterministic pipeline.

`source_type` currently represents feed protocol.

Supported values are:

```text
rss
atom
```

It is not a descriptive publisher category.

## Default-Domain Validation

`default_domains` remains a required configuration field but may be explicitly empty.

Example:

```yaml
default_domains: []
```

This is intentional.

`geographic_scope` remains required and non-empty.

## Potential Future Metadata

Fields such as the following may be added only if required:

```text
homepage_url
country
notes
date_added
date_reviewed
```

Operational data such as:

```text
last_successful_run
failure_count
```

should generally be generated by the system rather than manually maintained.

Do not expand the source schema merely to make it more descriptive.

---

# Article Metadata Policy

The current canonical article record preserves important source-provided and derived fields including:

```text
record_id
source_id
title
normalized_title
article_url
normalized_url
published_at
retrieved_at
description
domains
matched_keywords
relevance_score
score_components
```

The exact Python model remains the implementation source of truth.

Potential future fields such as:

```text
author
geographies
content_type
matched_entities
duplicate_cluster_id
related_source_count
```

should not be documented as implemented until the corresponding behaviour exists.

---

# Required Core Metadata

A structurally valid current record normally requires:

- source identifier;
- title;
- usable HTTP or HTTPS article URL;
- timezone-aware retrieval timestamp.

Publication timestamp is not required for structural validity.

However, current reporting-window policy requires a usable `published_at` value for inclusion in the reporting window.

This distinction is intentional.

A record may therefore be:

- valid;
- stored in validation results;
- excluded from current report processing because publication time is unavailable.

---

# Publication Timestamp Policy

Current behaviour is conservative.

If `published_at` is missing:

- the record may remain structurally valid;
- the system does not invent a publication time;
- retrieval time is not treated as confirmed publication time;
- the record is excluded from collection-window eligibility.

Phase 2 validation found usable publication timestamps across all observed entries from the seven selected real feeds.

Therefore no timestamp fallback logic was added.

This policy should be revisited only if valuable future sources systematically omit usable publication timestamps.

---

# Description Policy

Only short descriptions already provided through permitted feeds or public metadata should be stored and displayed.

The system should not extract full article bodies during the MVP.

Current report configuration truncates descriptions to:

```text
300 characters
```

Descriptions are optional.

Phase 2 confirmed that:

- ECB entries may omit descriptions;
- Sifted entries may omit descriptions;
- some OpenAI entries may omit descriptions.

Missing descriptions do not invalidate a record.

The system must not fabricate article summaries.

---

# URL Metadata Policy

The original publisher-provided article URL should be preserved.

A separate normalised URL is used for deterministic identity and duplicate handling.

Current normalisation removes selected tracking parameters and fragments.

Publisher-specific tracking parameters may still remain in some URLs.

Phase 2 exposed BBC parameters such as:

```text
at_medium
at_campaign
```

in real output.

This is a known lower-priority limitation.

Do not expand URL cleaning until the remaining parameters materially affect:

- deduplication;
- report readability;
- repository quality.

---

# Classification Policy

## Current Classification Inputs

The implemented classifier currently uses:

1. source default domains;
2. title keywords;
3. description keywords.

Keyword matching is deterministic, case-insensitive and protected by word-boundary behaviour.

## Current Multi-Domain Behaviour

A record may receive multiple domains.

For report display:

- one domain becomes primary;
- additional domains are displayed as secondary metadata.

## Current Unclassified Behaviour

Unclassified records:

- remain valid processed records;
- are not shown in the main report by default.

This is intentional.

Phase 2 showed that broad source defaults can improve apparent recall while damaging precision.

The current policy therefore prefers leaving a record unclassified when evidence is weak.

## Potential Future Inputs

Future deterministic classification may use:

- configured entities;
- geography;
- content types;
- exclusions;
- keyword groups;
- stronger context rules.

These should be introduced only when repeated real classification errors demonstrate a need.

---

# Keyword Policy

Keyword lists should be:

- explicit;
- human-readable;
- small enough to review;
- conservative;
- tested against real examples.

Avoid overly broad terms that create large numbers of false positives.

Ambiguous terms may require:

- multiple-word phrases;
- source context;
- exclusions;
- combinations of terms.

Examples of potentially ambiguous terms include:

- model;
- market;
- Apple;
- cloud;
- bank;
- government;
- defence;
- president;
- prime minister.

Keyword complexity should grow from observed errors, not from speculative taxonomy design.

## Evidence-Driven Keyword Procedure

When a recall problem is observed:

1. identify specific relevant unclassified records;
2. propose a small candidate keyword set;
3. simulate matches against real processed records;
4. inspect both intended and unintended matches;
5. add only terms with an acceptable precision trade-off;
6. rerun the report;
7. stop tuning when output becomes useful enough for the current phase.

Phase 2 followed this procedure for Global Politics.

The result was the addition of:

- war;
- conflict;
- parliament.

The procedure should remain the standard for future keyword changes.

---

# Tracked Entities

Tracked entities are not currently implemented.

Potential entity groups include:

- institutions;
- central banks;
- regulators;
- companies;
- AI laboratories;
- technology platforms;
- venture funds;
- universities;
- accelerators;
- Bocconi organisations;
- Milan ecosystem organisations.

If introduced later, an entity configuration might support:

```text
canonical_name
aliases
entity_type
domains
geographies
priority
active
```

An entity registry should remain small and purpose-driven.

The system should not build a large entity database without a validated ranking or classification need.

---

# Ranking Policy

The ranking system should prioritise practical relevance to the user.

It should remain:

- deterministic;
- configurable;
- inspectable;
- reproducible.

## Current Implemented Factors

Current ranking uses:

- source tier;
- number of assigned domains;
- number of matched keywords.

Current conceptual formula:

```text
relevance_score
=
source_tier_score
+ 2 × domain_matches
+ 1 × keyword_matches
```

Score components are stored.

## Phase 2 Ranking Lesson

The first real report initially contained inflated scores caused by weak source defaults.

The ranking formula itself behaved as designed.

The bad input evidence came from classification.

The correction was therefore made by removing weak default domains rather than by changing score weights.

This establishes a useful rule:

> fix misleading upstream evidence before compensating with downstream ranking complexity.

## Potential Future Positive Factors

Only if justified by repeated real reports:

- domain priority;
- geography priority;
- tracked entities;
- content type;
- recency;
- independent multi-source coverage.

## Potential Future Negative Factors

Only if justified by observed quality problems:

- promotional content;
- missing metadata;
- repeated syndicated coverage;
- source-specific quality penalties.

## Source Tier Is Not Importance

A Tier 1 source may publish a routine low-value update.

A lower-tier source may publish highly relevant specialist reporting.

Source quality should therefore remain only one component of relevance.

Phase 2 directly validated this distinction.

---

# Duplicate Policy

Duplicate reduction should reduce repetition without discarding genuinely distinct information.

## Current Exact Duplicate Rules

Implemented exact duplicate checks use:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

Phase 2 real runs observed exact duplicates and confirmed that the current implementation provides useful reduction.

## Near Duplicates

Near-duplicate detection is not currently implemented.

Examples of potential future near duplicates include:

- minor headline variations;
- syndicated copies;
- multiple outlets reporting the same announcement;
- slightly updated versions of the same story.

Near-duplicate clustering should be added only if repeated automated reports demonstrate material repeated coverage.

## Related but Distinct Items

Items should remain separate when they represent materially different information.

Examples:

- a company earnings release;
- later independent analysis of those earnings;
- a regulatory investigation;
- a separate acquisition announcement.

## Conservative Principle

False merging is more harmful than modest repeated coverage during early production.

When uncertain, preserve separate records.

---

# Multi-Source Coverage

The current system does not create story clusters or related-source counts.

If real usage demonstrates that the same important event frequently appears across multiple independent sources, future clustering may preserve:

- primary record;
- related record IDs;
- unique source count;
- source diversity;
- publication range.

Multi-source coverage should not automatically increase relevance unless the system can distinguish independent reporting from syndicated duplication.

Do not add story clustering during the automation phase merely because several real sources are now active.

---

# Language Policy

## Target Languages

The target system should support:

- English;
- Italian.

## Current Implementation

The current seven-source real registry uses English-language feeds.

Istat is collected through its English press-release feed.

Therefore Phase 2 does not constitute full bilingual validation.

## Translation

The core MVP should not depend on automated translation.

Original titles and descriptions should be preserved.

## Classification

Keyword configuration may include both English and Italian when an Italian-language source is introduced and validated.

## Report Presentation

Original source language should be preserved.

The system should not fabricate translations.

---

# Source Diversity Policy

A useful production report should not be unnecessarily dominated by one publisher, source tier, geography or source type.

Diversity should be reviewable across:

- publishers;
- source tiers;
- geographies;
- primary versus secondary evidence;
- general versus specialist coverage.

The system does not need artificial quotas.

A highly relevant publisher may legitimately appear several times.

Potential future evaluation metrics include:

- displayed share by publisher;
- displayed share by source tier;
- displayed share by geography;
- displayed share by domain.

These metrics should be added only if concentration becomes a practical quality issue.

## Current Position

The seven-source set is deliberately diverse enough to begin automation but has not yet been evaluated over a sustained period.

A single day's output should not drive publisher quotas or concentration penalties.

Source diversity should be assessed during the initial production-evaluation period after scheduled automation is stable.

---

# Opportunity-Source Policy

Milan and Bocconi opportunity monitoring requires particularly strong selectivity.

An opportunity should be considered relevant when it offers meaningful:

- learning;
- networking;
- career information;
- project experience;
- research exposure;
- competition exposure;
- startup or innovation access.

Potential opportunity metadata may include:

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

The MVP does not require a separate opportunity database.

Opportunity records may later use the normal article-record model if the relevant source metadata fits the pipeline.

A dedicated report section should be added only if real usage demonstrates value.

No suitable structured Milan/Bocconi source was added during Phase 2 merely to complete the target taxonomy.

---

# Copyright and Public-Repository Policy

The repository may store and display:

- headlines;
- source names;
- direct links;
- timestamps;
- short feed-provided descriptions;
- system-generated classifications;
- system-generated scores;
- run and source-health metadata.

The repository must not store or display:

- complete articles;
- substantial copied passages;
- paywalled article bodies;
- private newsletter text;
- private email content;
- unauthorised copyrighted material;
- credentials;
- authentication tokens.

When uncertainty exists:

> store less content and preserve the original source link.

The current seven-source registry satisfies the public-repository boundary through public structured metadata.

---

# Source Lifecycle

A source may move through the following states conceptually.

## Candidate

Identified but not yet evaluated.

## Approved

Passes source-policy review and is ready for testing.

## Active

Enabled in the production source configuration.

## Monitoring

Remains active or temporarily disabled while reliability or quality concerns are reviewed.

## Disabled

Retained in configuration history but not collected.

## Removed

No longer retained because it is clearly unsuitable or obsolete.

Not every lifecycle state needs to become a field in `sources.yaml`.

Use configuration complexity only when it creates operational value.

---

# Adding a Source

Before adding a production source, ask:

1. Which real coverage gap does it fill?
2. Is it primary, journalistic or specialist?
3. Is the endpoint public and permitted?
4. Is the endpoint stable?
5. Does it provide usable timestamps?
6. Does it provide usable URLs?
7. Is the metadata sufficient for the current pipeline?
8. Does it significantly duplicate existing sources?
9. Is its signal-to-noise ratio acceptable?
10. Does it add meaningful diversity?
11. Can its metadata be stored safely in a public repository?
12. Will supporting it create disproportionate maintenance?
13. Does it work with the current bounded collector without special-case infrastructure?
14. Does it justify any source default, or should `default_domains` remain empty?

A source should not be added merely because it is prestigious or well known.

During the automation and initial-evaluation phases, a new source should normally require evidence that the current seven-source set misses something materially useful.

---

# Disabling or Removing a Source

A source should be reviewed when it:

- fails repeatedly;
- changes endpoint format;
- becomes mostly promotional;
- creates excessive repetition;
- stops publishing relevant information;
- becomes inaccessible without private credentials;
- creates copyright concerns;
- requires excessive special-case handling;
- adds little value relative to maintenance cost.

Disabling should often be preferred before permanent removal because it preserves decision history.

Source instability should not automatically trigger increasingly complex retry or scraping logic.

Replacing a weak source may be the simpler solution.

---

# Source Evaluation Metrics

During initial production evaluation, review sources using:

| Metric | Question |
|---|---|
| Availability | How often did collection succeed? |
| Relevance | How much collected material matched monitored needs? |
| Display Rate | How often did the source contribute displayed items? |
| Originality | Did it add information not already available elsewhere? |
| Duplication | How often did it repeat other sources? |
| Metadata Quality | Were titles, URLs and timestamps reliable? |
| Strategic Value | Did it improve awareness or opportunity detection? |
| Maintenance Cost | Did it require recurring manual intervention? |
| Default-Domain Quality | Does any configured source default remain valid across the feed? |
| Classification Contribution | Does the source produce useful classified items without excessive noise? |

No single metric should determine source quality.

A source can be reliable but low-value.

A source can also be strategically valuable but operationally expensive.

Both dimensions matter.

---

# Real-Source Validation Findings

Phase 2 produced several source-policy findings that should remain explicit.

## All Seven Sources Were Technically Compatible

All selected feeds were successfully collected through the actual project collector.

All observed returned entries normalised successfully.

All observed entries had usable publication timestamps.

Missing descriptions were acceptable because descriptions are optional.

## Feed Size Alone Is Not a Blocker

The OpenAI feed returned more than one thousand entries during validation.

This did not require special pagination or feed-size logic because the existing publication-window filter reduced the eligible set to a manageable number.

Do not optimise large-feed handling without evidence of a practical execution or maintenance problem.

## Source Tier Does Not Imply Relevance

A high-authority source may publish routine or irrelevant items.

The ECB concert announcement demonstrated this clearly.

Source tier should remain evidentiary input, not a guarantee of report placement.

## Broad Defaults Harm Precision

Broad source defaults forced unrelated stories into report sections and inflated scores.

This led to the current default-domain policy.

## Conservative Classification Is Acceptable

After removing broad defaults, many BBC World items remained unclassified.

Manual review showed that some of those omissions were appropriate and some represented a narrow recall gap.

A small keyword correction recovered clearly relevant political stories without returning to broad forced classification.

This is the preferred pattern.

---

# Taxonomy Validation Strategy

Technical pipeline stability and information-quality stability are separate.

Phase 2 established that:

- the real-source pipeline is technically viable;
- the current seven-domain taxonomy can produce a useful report;
- classification remains intentionally provisional;
- the full ten-domain taxonomy is not yet quality-validated;
- one day's report is insufficient to optimise ranking, source diversity or taxonomy coverage.

The next meaningful taxonomy evaluation should occur after automated execution produces repeated real reports.

Use a manually reviewed sample containing examples such as:

- multiple topic domains;
- primary and secondary sources;
- multi-domain stories;
- ambiguous keywords;
- relevant unclassified items;
- exact duplicates;
- possible near duplicates;
- promotional content;
- malformed or incomplete metadata;
- source concentration;
- repeated publisher patterns.

When Italian-language sources are later introduced, include bilingual examples as well.

Evaluate:

- classification accuracy;
- false-positive classifications;
- relevant unclassified records;
- duplicate behaviour;
- source-tier usefulness;
- timestamp quality;
- report usefulness;
- report concentration;
- source-default quality;
- ranking order.

Do not build a large artificial validation dataset before repeated real-source examples exist.

---

# Current Resolved Information Decisions

The following decisions are implemented for the current MVP core.

## Current Implemented Domains

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

The full ten-domain taxonomy remains the target.

---

## Deferred Target Domains

- Financial Markets;
- Italy;
- Milan and Bocconi Ecosystem.

These are not required before GitHub Actions automation.

---

## Current Active Sources

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News;
- Istat Press Releases;
- OpenAI News;
- Sifted.

---

## Source Defaults

**Decision:** defaults are optional topical evidence, not mandatory publisher categories.

Current defaults:

- BBC News World → none;
- BBC News Business → none;
- European Central Bank → none;
- European Commission Highlighted News → none;
- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

---

## Multi-Domain Records

**Decision:** supported.

Records may receive multiple domains.

---

## Primary Report Placement

**Decision:** each story appears once.

The first assigned eligible domain becomes the primary report section.

Additional domains are shown as secondary metadata.

---

## Unclassified Records

**Decision:** preserved in processed data but omitted from the main report by default.

---

## Relevance Score

**Decision:** stored and displayed.

---

## Score Components

**Decision:** stored for transparency.

They are not currently shown in full in the Markdown report.

---

## Maximum Items Per Domain

**Current configured value:** 5.

---

## Maximum Total Items

**Current configured value:** 30.

---

## Description Length

**Current configured maximum:** 300 characters.

---

## Exact Duplicate Policy

**Decision:**

1. normalised URL;
2. normalised title.

---

## Collection Window

**Current CLI default:** previous 24 hours.

Boundaries are inclusive.

---

## Missing Publication Timestamp

**Current policy:** exclude from collection-window eligibility.

Do not replace missing publication time with retrieval time.

---

## Global Politics Keyword Refinement

**Current evidence-based additions:**

- war;
- conflict;
- parliament.

These were added only after testing candidate terms against real processed records.

---

# Open Information Decisions

The following remain intentionally unresolved.

## Future Source Expansion

No fixed source-count target.

Add sources only when the current seven-source universe demonstrates a real coverage or quality gap.

## Full Keyword Lists

Continue expanding gradually from real classification errors.

## Financial Markets Domain

Implement only if repeated real reports demonstrate missed market intelligence that cannot be handled adequately through current domains.

## Italy Domain

Implement only if topic classification plus source geography proves insufficient.

## Milan and Bocconi Domain

Implement only when a suitable structured public source or validated workflow exists.

## Domain Priority Weights

Not currently implemented.

Add only if report ordering needs them.

## Tracked Entities

Not currently implemented.

## Geographic Classification

Not currently implemented at article level.

## Content-Type Classification

Not currently implemented.

## Near-Duplicate Threshold

No threshold exists because near-duplicate detection is not implemented.

## Multi-Source Story Clustering

Deferred pending repeated real repetition.

## Publisher Concentration Controls

Evaluate only after automated reports show a concentration problem.

## Missing Publication Timestamp Fallback

Reconsider only if valuable real sources systematically omit timestamps.

## Opportunity-Specific Report Behaviour

Evaluate only after suitable structured opportunity sources exist.

## Source-Health History

Current run summaries provide per-run status.

Long-term history should be added only if automated source maintenance requires it.

## Ranking Weights

Current weights remain provisional.

Change only after repeated report review shows systematic ordering problems.

---

# Information Quality Decision Rules

Before adding a taxonomy rule, source field or classification dimension, ask:

1. What observed information-quality problem does it solve?
2. How often does the problem occur?
3. Does the problem materially reduce report usefulness?
4. Can a source change solve it instead?
5. Can a simpler keyword or configuration adjustment solve it?
6. What false positives or false negatives could the change create?
7. How will the improvement be evaluated?
8. Does the change increase recurring maintenance?
9. Does the change preserve explainability?
10. Is the change necessary before the system can be used?

The default should be to preserve the simpler current rule until evidence justifies more complexity.

Phase 2 provides the model:

```text
observe real report problem
→ isolate the cause
→ test the smallest deterministic correction
→ rerun
→ inspect report quality
→ stop when good enough for the current phase
```

---

# Current Information-Policy Limitations

The following limitations are known and accepted at the current stage:

- seven of ten target domains are implemented;
- the current source universe contains seven real sources;
- all current real feeds are English-language feeds;
- full bilingual taxonomy behaviour is not yet validated;
- Financial Markets is not implemented;
- Italy is not implemented as a topic domain;
- Milan and Bocconi is not implemented;
- article-level geography is not implemented;
- content type is not implemented;
- entity tracking is not implemented;
- near-duplicate detection is not implemented;
- multi-source story clustering is not implemented;
- source diversity has not yet been evaluated longitudinally;
- ranking weights remain provisional;
- keyword lists remain intentionally conservative;
- some relevant records may remain unclassified;
- publisher-specific tracking parameters may remain in some normalised URLs;
- source-health history is per-run rather than longitudinal.

These limitations define the current maturity level.

They do not imply that all corresponding features should be implemented next.

The next priority is automation, not taxonomy expansion.

---

# Current Status

**Status:** Phase 2 real-source taxonomy and source policy validated; ready for Phase 3 automation

**Implemented and validated:**

- seven active real public RSS sources;
- seven active topic domains;
- configurable domains;
- optional source-default domains;
- deterministic title/description keyword classification;
- multiple domains;
- primary report placement;
- secondary-domain metadata;
- explicit unclassified handling;
- deterministic source-tier scoring;
- exact URL/title deduplication;
- 24-hour publication-window filtering;
- feed-description truncation;
- public-safe metadata policy;
- real-source timestamp compatibility;
- real-source metadata compatibility;
- conservative broad-source default policy;
- evidence-based keyword refinement;
- source-level failure isolation.

**Currently controlled / provisional:**

- seven-source universe;
- seven-domain implemented subset;
- keyword lists;
- ranking weights;
- report limits;
- source-default assignments;
- source diversity.

**Not yet implemented:**

- full ten-domain coverage;
- Financial Markets;
- Italy topic classification;
- Milan and Bocconi topic classification;
- tracked entities;
- article-level geography;
- content type;
- near-duplicate clustering;
- multi-source story clustering;
- long-term source-health history.

**Next information-quality milestone:**

> Preserve the current source and taxonomy configuration through initial GitHub Actions automation, then evaluate repeated real reports before expanding quality logic.

---

# Changelog

## 2026-08-11 — Phase 2 Real-Source Taxonomy and Source-Policy Validation

- Replaced the one-sample-source implementation state with seven validated public RSS sources.
- Expanded the implemented taxonomy from two to seven active domains.
- Kept Financial Markets, Italy and Milan/Bocconi as deferred target domains.
- Recorded the exact current active source universe.
- Recorded source tiers, language and geographic scope for the seven-source set.
- Added the rule that source defaults represent genuine source-wide topical evidence rather than publisher categories.
- Added support and policy for explicitly empty `default_domains`.
- Removed broad defaults from BBC World, BBC Business, ECB and European Commission.
- Restricted Istat to an Economics and Macroeconomics default.
- Restricted OpenAI to an Artificial Intelligence default.
- Restricted Sifted to a Startups and Venture Capital default.
- Recorded the real-report false positives caused by broad source defaults.
- Recorded `war`, `conflict` and `parliament` as evidence-based Global Politics keyword additions.
- Recorded that `government`, `defence`, `president` and `prime minister` were tested but not added because of ambiguity or noise.
- Confirmed real-source publication timestamps were usable across the observed seven-feed sample.
- Confirmed descriptions are optional and may legitimately be missing.
- Recorded that the large OpenAI feed did not require special handling because collection-window filtering kept eligible output manageable.
- Recorded the distinction between source tier and story importance using real report evidence.
- Updated taxonomy validation from pre-production planning to repeated-real-report evaluation.
- Preserved conservative classification, exact deduplication, copyright boundaries and public-repository safety.
- Made automation, rather than further taxonomy expansion, the next project priority.

## 2026-08-11 — Phase 1 Taxonomy and Source-Policy Reconciliation

- Distinguished the target ten-domain taxonomy from the implemented two-domain Phase 1 configuration.
- Recorded current implemented classification behaviour.
- Recorded current exact duplicate policy.
- Recorded current ranking weights and source-tier scoring.
- Recorded current report limits and description length.
- Recorded current collection-window and missing-publication-time policy.
- Replaced the previous 20–30 source planning target with a smallest-credible-source strategy.
- Moved geography, entities, content type and near-duplicate clustering behind evidence from real reports.
- Clarified that technical Phase 1 stability does not imply full taxonomy quality stability.
- Updated the article metadata section to distinguish implemented fields from future possibilities.
- Preserved the original source hierarchy, inclusion/exclusion policy, copyright boundaries and broader ten-domain strategic scope.

## Initial Information Taxonomy and Source Policy Baseline

- Established the ten target topic domains.
- Defined geographic and content-type dimensions.
- Defined source tiers.
- Defined source inclusion and exclusion criteria.
- Defined source lifecycle and evaluation principles.
- Defined classification, ranking and duplicate-reduction policy.
- Defined copyright and public-repository boundaries.
````
