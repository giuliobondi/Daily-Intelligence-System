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

The full taxonomy and source policy in this document defines the intended information model.

The current Phase 1 implementation is deliberately narrower.

At Phase 1 closeout, the implemented configuration contains:

- one controlled sample source;
- two active domains:
  - Technology and Software;
  - Artificial Intelligence;
- simple deterministic keyword rules;
- source-default domains;
- deterministic source-tier scoring;
- no tracked-entity configuration;
- no geographic classification;
- no content-type classification;
- no near-duplicate clustering;
- no production source universe.

This narrow configuration was used to validate the processing pipeline.

It should not be interpreted as the final intended information coverage.

The next development phase will introduce only a small real-source set before broader taxonomy or source expansion.

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

The current implementation already supports multiple domains.

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

Only topic classification and source tier are currently implemented.

Geography and content type remain future optional dimensions.

---

# Target Topic Taxonomy

The following ten domains define the intended strategic coverage.

They are target information categories, not all currently implemented production domains.

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

### Current Phase 1 Status

**Implemented**

Current configured keywords include concepts such as:

- artificial intelligence;
- AI;
- machine learning;
- large language model;
- foundation model;
- model release.

The current list is intentionally small and provisional.

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

### Current Phase 1 Status

**Implemented**

Current configured keywords include concepts such as:

- software;
- cloud;
- cybersecurity;
- developer;
- open source;
- API.

The current list is intentionally small and provisional.

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

Geography remains a target information dimension but is not currently implemented in the processing pipeline.

Potential geographic tags include:

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

Geographic classification should be introduced only if real use shows that topic domains alone are insufficient for prioritisation or browsing.

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

The current ranking system already uses source tier as one deterministic input.

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
- metadata availability varies;
- different publications have different geographic and editorial biases.

### Policy

Tier 2 sources are likely to form an important part of the future production source universe.

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

Tier 3 sources should be approved individually based on demonstrated quality.

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

Tier 4 sources are outside the initial production scope unless a specific structured source proves unusually valuable.

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

These weights are Phase 1 defaults and should be evaluated using real reports before being treated as final.

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

Titles, URLs and descriptions are sufficiently complete for automated processing.

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

# Production Source-Universe Strategy

The previous planning range of approximately 20–30 sources should not be treated as an implementation target.

The next source-selection step should be deliberately smaller.

## Phase 2 Strategy

Start with the smallest credible real-source set sufficient to validate:

- live HTTP collection;
- source diversity;
- publication timestamps;
- real metadata;
- source-level failures;
- report usefulness.

The first production-like set should remain small enough for manual review.

A likely initial real-source set may include examples from several of these categories:

- one primary institutional source;
- one high-quality reporting source;
- one AI or technology source;
- one European or Italian source;
- optionally one startup, VC or opportunity source.

The exact number should be determined by coverage needs rather than by a predefined quota.

## Expansion Rule

Add a source only when it solves a demonstrated coverage or quality gap.

A smaller high-quality source universe is preferable to a large unreviewed list.

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

Current Phase 1 behaviour is conservative.

If `published_at` is missing:

- the record may remain structurally valid;
- the system does not invent a publication time;
- retrieval time is not treated as confirmed publication time;
- the record is excluded from collection-window eligibility.

This policy should be revisited only if useful real sources frequently omit publication timestamps.

---

# Description Policy

Only short descriptions already provided through permitted feeds or public metadata should be stored and displayed.

The system should not extract full article bodies during the MVP.

Current report configuration truncates descriptions to:

```text
300 characters
```

The value is configurable and should be evaluated during real use.

The system must not fabricate article summaries.

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

## Potential Future Inputs

Future deterministic classification may use:

- configured entities;
- geography;
- content types;
- exclusions;
- keyword groups;
- stronger context rules.

These should be introduced only when real classification errors demonstrate a need.

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

Examples of ambiguous terms include:

- model;
- market;
- Apple;
- cloud;
- bank.

Keyword complexity should grow from observed errors, not from speculative taxonomy design.

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

Current Phase 1 ranking uses:

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

## Potential Future Positive Factors

Only if justified by real reports:

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

A Tier 3 source may publish highly relevant specialist analysis.

Source quality should therefore remain only one component of relevance.

---

# Duplicate Policy

Duplicate reduction should reduce repetition without discarding genuinely distinct information.

## Current Exact Duplicate Rules

Implemented exact duplicate checks use:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

## Near Duplicates

Near-duplicate detection is not currently implemented.

Examples of potential future near duplicates include:

- minor headline variations;
- syndicated copies;
- multiple outlets reporting the same announcement;
- slightly updated versions of the same story.

Near-duplicate clustering should be added only if real reports demonstrate material repeated coverage.

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

---

# Language Policy

## Initial Languages

The target system should support:

- English;
- Italian.

The current controlled fixture and configuration do not yet constitute full bilingual validation.

## Translation

The core MVP should not depend on automated translation.

Original titles and descriptions should be preserved.

## Classification

Keyword configuration may include both English and Italian where needed.

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

A source should not be added merely because it is prestigious or well known.

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

No single metric should determine source quality.

A source can be reliable but low-value.

A source can also be strategically valuable but operationally expensive.

Both dimensions matter.

---

# Taxonomy Validation Strategy

Technical pipeline stability and information-quality stability are separate.

The local Phase 1 pipeline is technically validated.

The full target taxonomy is not yet quality-validated.

Before the production taxonomy is considered stable, use a manually reviewed real sample containing examples such as:

- multiple topic domains;
- English and Italian items;
- primary and secondary sources;
- multi-domain stories;
- ambiguous keywords;
- unclassified items;
- exact duplicates;
- possible near duplicates;
- opportunity announcements;
- promotional content;
- malformed or incomplete metadata.

Evaluate:

- classification accuracy;
- false-positive classifications;
- relevant unclassified records;
- duplicate behaviour;
- source-tier usefulness;
- timestamp quality;
- report usefulness;
- report concentration.

Do not build a large artificial validation dataset before enough real-source examples exist.

---

# Current Resolved Information Decisions

The following decisions are now implemented for the current MVP core.

## Current Implemented Domains

- Technology and Software;
- Artificial Intelligence.

The full ten-domain taxonomy remains the target.

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

# Open Information Decisions

The following remain intentionally unresolved.

## Production Source Universe

Determine during minimal real-source validation.

## Exact Source Count

No fixed target.

Choose the smallest source universe that produces useful coverage.

## Full Keyword Lists

Expand gradually from real classification errors.

## Domain Priority Weights

Not currently implemented.

Add only if report ordering needs them.

## Tracked Entities

Not currently implemented.

## Geographic Classification

Not currently implemented.

## Content-Type Classification

Not currently implemented.

## Near-Duplicate Threshold

No threshold exists because near-duplicate detection is not implemented.

## Multi-Source Story Clustering

Deferred pending real repetition.

## Publisher Concentration Controls

Evaluate only after real reports show concentration problems.

## Missing Publication Timestamp Fallback

Reconsider only if valuable real sources systematically omit timestamps.

## Opportunity-Specific Report Behaviour

Evaluate after the broader production source universe exists.

## Source-Health History

Current run summaries provide per-run status.

Long-term history should be added only if source maintenance requires it.

---

# Information Quality Decision Rules

Before adding a taxonomy rule, source field or classification dimension, ask:

1. What observed information-quality problem does it solve?
2. How often does the problem occur?
3. Does the problem materially reduce report usefulness?
4. Can a source change solve it instead?
5. Can a simpler keyword/configuration adjustment solve it?
6. What false positives or false negatives could the change create?
7. How will the improvement be evaluated?
8. Does the change increase recurring maintenance?
9. Does the change preserve explainability?
10. Is the change necessary before the system can be used?

The default should be to preserve the simpler current rule until evidence justifies more complexity.

---

# Current Information-Policy Limitations

The following limitations are known and accepted at the current stage:

- only two target domains are implemented;
- only one controlled sample source is active;
- bilingual taxonomy behaviour is not yet validated;
- full ten-domain coverage is not implemented;
- geography is not implemented;
- content type is not implemented;
- entity tracking is not implemented;
- near-duplicate detection is not implemented;
- multi-source story clustering is not implemented;
- source diversity has not yet been evaluated with production data;
- ranking weights are provisional;
- real-source timestamp quality remains unvalidated;
- current keyword lists are intentionally minimal.

These limitations define the current maturity level.

They do not imply that all corresponding features should be implemented next.

---

# Current Status

**Status:** Target information taxonomy retained; Phase 1 implementation state reconciled

**Implemented and validated:**

- configurable domains;
- source-default domains;
- deterministic title/description keyword classification;
- multiple domains;
- primary report placement;
- secondary-domain metadata;
- explicit unclassified handling;
- deterministic source-tier scoring;
- exact URL/title deduplication;
- 24-hour publication-window filtering;
- feed-description truncation;
- public-safe metadata policy.

**Currently controlled / provisional:**

- two-domain taxonomy;
- one sample source;
- keyword lists;
- ranking weights;
- report limits.

**Not yet implemented:**

- production source universe;
- broad ten-domain coverage;
- tracked entities;
- geography;
- content type;
- near-duplicate clustering;
- multi-source coverage;
- long-term source-health history.

**Next information-quality milestone:**

> Select and validate the smallest credible set of real public RSS/Atom sources before expanding taxonomy complexity.

---

# Changelog

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