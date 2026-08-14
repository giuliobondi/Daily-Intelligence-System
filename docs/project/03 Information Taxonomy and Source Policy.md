# Daily Intelligence System — Information Taxonomy and Source Policy

> **Purpose**
>
> This document defines what information the Daily Intelligence System should collect, how that information should be classified, which sources are acceptable, and which rules govern source selection, accessibility, storage and public presentation.
>
> It is the quality-control framework for the information entering the system.
>
> ---
>
> **Primary Question**
>
> > *What information should the system collect, from which sources, and under which classification, accessibility and quality rules?*
>
> ---
>
> **Update Frequency**
>
> Update when monitored domains, source-selection rules, accessibility assumptions, metadata requirements or source-governance policies materially change.

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

The objective is to identify a manageable set of high-value items from transparent, credible and operationally suitable sources.

Information quality should be evaluated through:

1. relevance;
2. source credibility;
3. originality;
4. timeliness;
5. diversity;
6. transparency;
7. accessibility;
8. metadata richness;
9. suitability for automated collection;
10. maintenance burden.

The system should prefer a smaller set of high-quality and useful sources over broad but noisy coverage.

A technically compatible source is not automatically a good production source.

A source should create useful intelligence, not merely produce valid feed records.

---

# Current Implementation Status

The deterministic information-processing model is implemented and production-automated.

The current production configuration contains:

- seven active public RSS sources;
- seven active topic domains;
- deterministic title and description keyword rules;
- optional source-default domains;
- deterministic source-tier scoring;
- exact duplicate reduction;
- a previous-24-hours publication window;
- explicit handling of unclassified records;
- scheduled GitHub Actions execution;
- automated output persistence;
- source-level failure isolation;
- degraded-run reporting;
- no tracked-entity configuration;
- no article-level geographic classification;
- no content-type classification;
- no near-duplicate clustering;
- no multi-source story clustering.

The current active source registry contains:

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

The seven-source, seven-domain configuration successfully proved:

- real-source collection;
- deterministic processing;
- GitHub automation;
- failure isolation;
- automated persistence.

It should no longer be interpreted as sufficient evidence that the current information universe is optimal.

Production use has now demonstrated meaningful source and coverage limitations.

The current information-quality priority is therefore:

> **Correct and expand the production source and domain universe before implementing richer report-context logic.**

The first current-source review should include Sifted because production use exposed a concrete accessibility problem.

---

# Taxonomy Principles

## Configurable

Domains, keywords, source tiers and other classification signals should be maintained through configuration rather than embedded throughout core processing code.

Configuration should expand only when corresponding processing behaviour or information value is justified.

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

The primary-domain selection method may later become more sophisticated if production evidence demonstrates a need.

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

Real-report review confirmed that this principle is preferable to forcing broad feeds into publisher-level topic categories.

A high rate of relevant unclassified records should trigger taxonomy review.

---

## Broad but Bounded

The target taxonomy should preserve awareness across several strategically useful domains without trying to classify every possible news topic.

The system should not become a generic global-news taxonomy.

---

## Independent Dimensions

Topic, geography, source tier, accessibility and content type are conceptually separate dimensions.

For example, an item might eventually be described as:

```text
topic: Artificial Intelligence
geography: European Union
source tier: Tier 2
reader access: Bocconi Direct
automation access: Public RSS
content type: News Reporting
```

Only topic classification and source tier are currently implemented at article level.

Source-level geographic scope exists in configuration.

Accessibility is currently a source-policy evaluation dimension rather than an implemented article field.

Article-level geographic classification and content type remain optional future dimensions.

---

# Target Topic Taxonomy

The following ten domains define the intended strategic coverage.

Seven are currently implemented.

Three are now candidates for active reconsideration during the source/domain expansion phase.

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

The configured keyword list remains deliberately conservative.

Real BBC World records previously exposed a recall gap.

Candidate keywords were simulated against actual processed records before configuration was changed.

The following terms were added:

- war;
- conflict;
- parliament.

Broader candidates such as:

- government;
- defence;
- president;
- prime minister;

were tested but not added because they produced ambiguous or low-value matches.

This domain should continue to expand from observed errors rather than from copying the entire conceptual indicator list into configuration.

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

Istat Press Releases currently has this domain as a source default because the selected feed is sufficiently narrow for the default to represent genuine source-wide topical evidence.

BBC Business does not receive an Economics default because the feed contains many business and general-interest stories that are not meaningfully macroeconomic.

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

**Candidate for implementation during the active source/domain review**

This domain was not required for the original seven-source automation baseline.

The source/domain expansion phase should now determine:

- whether financial-market intelligence is materially underrepresented;
- which public structured sources can support the domain;
- whether official or high-quality reporting sources provide useful context;
- whether implementation would create excessive daily noise.

Do not activate the domain merely because financial markets are strategically relevant.

Suitable source coverage and classification rules must exist first.

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

This domain relies on content evidence rather than broad source defaults in the current registry.

Assigning BBC Business or OpenAI blanket Corporate Strategy defaults previously inflated classifications and scores for unrelated stories.

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

OpenAI News has Artificial Intelligence as its single source default because the selected feed has a sufficiently strong source-wide topical relationship to AI.

OpenAI does not receive automatic Technology or Corporate Strategy defaults.

Those additional domains require content evidence.

The active source-expansion phase should evaluate whether OpenAI News provides too narrow a publisher perspective and whether additional independent AI sources are justified.

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

No current real source receives Technology as a blanket source default.

Technology should be assigned from content evidence unless a future source is sufficiently narrow to justify a source-wide default.

Source expansion should evaluate whether current technology coverage is too dependent on BBC Business and OpenAI-related items.

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

**Implemented — source coverage under active review**

Sifted currently has Startups and Venture Capital as its single source default.

The topical default remains logically appropriate.

However, Sifted itself is now under source-policy review because production use exposed an accessibility problem.

At least one selected report item required Sifted Pro access.

Sifted feed entries have also been observed to provide limited descriptive context for some items.

This creates a poor user experience when:

```text
thin report entry
→ click required for basic understanding
→ linked article unavailable without Sifted Pro
```

The appropriate response is not automatically to scrape the restricted article.

The source should instead be evaluated against alternatives on:

- topical quality;
- public metadata richness;
- public or user-accessible follow-up;
- uniqueness of reporting;
- automation suitability;
- maintenance cost.

Sifted should remain classified as:

> **Active source under review**

until the source-expansion phase reaches a deliberate keep, replace or disable decision.

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

### Current Status

**Implemented**

Neither the European Central Bank feed nor the European Commission Highlighted News feed receives Europe/EU as a blanket source default.

Source identity alone should not imply item importance or topical relevance.

For example, a routine institutional item should not automatically enter an Economics or Europe section merely because the publisher is a European institution.

---

## 9. Italy

### Scope

Italian developments with economic, political, technological, financial or professional relevance.

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

**Candidate for implementation during the active source/domain review**

Istat currently contributes Italian macroeconomic evidence while its source-level `geographic_scope` records Italy.

The source-expansion phase should determine whether the current setup misses strategically relevant Italian:

- business;
- finance;
- public policy;
- technology;
- startup;
- regulatory developments.

Potential sources should be evaluated before deciding whether Italy requires a distinct topic domain rather than geographic metadata alone.

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

### Current Status

**Candidate for reconsideration, not automatically approved**

Earlier source research did not identify a sufficiently strong and stable public structured source to justify implementing this domain.

The current source/domain strategy phase should reconsider it because the broader intelligence requirements are now being reviewed.

Do not compensate for poor source availability with:

- authenticated scraping;
- private email ingestion;
- daily copy-and-paste;
- a separate complex ingestion system.

If suitable public structured sources do not exist, the domain may remain outside the automated system.

---

# Geographic Classification

Geography remains a target information dimension but is not currently implemented at article level.

Source configuration preserves `geographic_scope`.

Potential future article-level geographic tags include:

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

Article-level geographic classification should be introduced only if source/domain expansion demonstrates that topic domains plus source-level geography are insufficient for prioritisation or browsing.

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

Add it only if report quality or ranking materially benefits.

---

# Source Hierarchy

Source tier represents evidentiary role and expected reliability.

It does not guarantee:

- importance;
- accessibility;
- metadata richness;
- report usefulness.

These dimensions must be evaluated separately.

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
- specialist publications may have narrower coverage;
- public feeds may expose much less context than the linked article.

### Policy

Tier 2 status does not imply automatic production eligibility.

A Tier 2 source must still pass:

- automation suitability;
- metadata richness;
- accessibility;
- maintenance;
- public-repository compatibility.

Sifted is the current concrete example of why source tier and production suitability must remain separate.

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

Tier 4 sources remain outside the current production scope unless a specific structured source proves unusually valuable.

A Tier 4 source should not be the sole evidence supporting an important item.

---

# Current Source-Tier Scoring

The current ranking configuration assigns:

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

Previous real-report work showed that misleading classification evidence can distort scores even when the ranking formula is functioning correctly.

The preferred response is:

> fix misleading upstream evidence before compensating with downstream ranking complexity.

---

# Two-Axis Source Suitability Model

Production source evaluation must distinguish two separate questions.

## Axis 1 — Automation Suitability

> **Can the Daily Intelligence System safely, legally and reliably ingest this source?**

Evaluate:

- public structured endpoint;
- official feed or API;
- automation permission;
- absence of required private credentials;
- metadata quality;
- timestamp quality;
- technical reliability;
- public-repository compatibility;
- copyright constraints;
- maintenance burden.

## Axis 2 — Reader Accessibility

> **Can the user actually read or investigate the linked source when deeper reading is useful?**

Evaluate:

- public web access;
- direct institutional publisher access;
- SearchLib access;
- academic database access;
- other legitimate institutional access;
- additional personal paid subscription required;
- unclear or inconsistent access.

These axes are independent.

Examples:

```text
Source A
Automation: suitable public RSS
Reader access: free public web
→ strong production candidate
```

```text
Source B
Automation: suitable public RSS
Reader access: Bocconi direct subscription
→ potentially strong production candidate
```

```text
Source C
Automation: suitable public RSS
Reader access: requires extra paid subscription
Public feed context: rich
→ potentially usable, review carefully
```

```text
Source D
Automation: suitable public RSS
Reader access: requires extra paid subscription
Public feed context: very thin
→ weak production candidate
```

```text
Source E
Reader access: Bocconi database
Automation: authenticated database only
→ useful research source, not production-ingestion source
```

This distinction should govern the upcoming source-expansion work.

---

# Reader Accessibility Categories

The user's Bocconi research established four access modes that should not be treated as equivalent.

These categories describe personal reading access.

They do not automatically define production automation eligibility.

---

## 🟢 Direct Publisher Access

Bocconi provides institutional access that allows use of the publisher's normal website and, in several cases, official app.

Confirmed important examples include:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore.

Corriere della Sera is a special case because Bocconi provides archive/current-edition access without confirming unrestricted normal premium-site access.

### Product Implication

Direct institutional access can make a source highly valuable for manual follow-up.

It does not permit the Daily Intelligence System to authenticate into the publisher automatically unless a separate licence or endpoint explicitly permits that use.

---

## 🟡 SearchLib Access

Bocconi provides digital journal access through SearchLib.

Examples identified include:

- Foreign Affairs;
- Harvard Business Review;
- Time;
- Economia & Management.

### Product Implication

These sources may be highly valuable for manual research.

SearchLib availability does not automatically mean:

- publisher-site credentials exist;
- RSS feeds expose premium article content;
- automated collection is permitted.

---

## 🟠 Academic Database Access

Bocconi provides full-text or research access through systems including:

- Factiva;
- Nexis Uni;
- Business Source Ultimate.

Professional information platforms also include:

- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- S&P Capital IQ Pro;
- Aida.

These resources can expose a much larger publication universe.

### Product Implication

Database access is primarily a manual research layer.

It must not be interpreted as permission to:

- scrape database results;
- bulk-download licensed articles;
- redistribute full text;
- export restricted material into the public repository;
- automate authenticated access without explicit licence permission.

---

## 🔵 Public Web Access

The source can be read without Bocconi credentials.

Examples may include:

- BBC;
- official institutions;
- many public company or government sources;
- publications whose relevant content is freely accessible.

### Product Implication

Public reading accessibility is favourable but still does not by itself prove that automated scraping is permitted.

Prefer structured public feeds or official APIs.

---

## 🔴 Additional Paid / Not Confirmed

The user does not currently have confirmed direct access through Bocconi or the public web.

Examples from the current research include direct premium access to publications such as:

- Bloomberg.com;
- Reuters.com Premium;
- Washington Post;
- Politico Pro;
- Barron's;
- CNBC Pro;
- Business Insider Premium;
- Wired premium;
- MIT Technology Review.

Some of their content may still exist within institutional databases.

That database availability must not be confused with direct publisher access.

---

# Three-Layer Information Access Model

The source policy should distinguish three operational layers.

---

## Layer 1 — Automated Public Intelligence Sources

These are the only sources used continuously by the production pipeline.

Examples:

- public RSS feeds;
- public Atom feeds;
- official public APIs;
- official institutional releases;
- public company feeds;
- public structured metadata;
- other endpoints explicitly permitting the required automation.

Requirements:

- no private credentials;
- no paid API requirement;
- no authenticated premium scraping;
- public-repository-compatible metadata;
- acceptable maintenance burden.

This layer drives:

```text
collect
→ normalize
→ deduplicate
→ classify
→ rank
→ report
```

---

## Layer 2 — Bocconi Premium Reading Layer

These sources may be used manually for deeper reading when an important report item justifies it.

Examples include:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore;
- Foreign Affairs;
- Harvard Business Review;
- other legitimate Bocconi-accessible publications.

These sources may influence:

- preferred follow-up reading;
- source-selection decisions;
- manual verification;
- deeper understanding.

They are not automatically production-ingestion sources.

---

## Layer 3 — Research and Database Layer

These resources support targeted deeper investigations.

Examples include:

- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- S&P Capital IQ Pro;
- Aida.

Use cases include:

- reconstructing events;
- company research;
- historical coverage;
- source comparison;
- market research;
- industry investigation.

They are not part of daily automated ingestion by default.

---

# Source Inclusion Criteria

A production source should normally satisfy most of the following conditions.

## Relevance

The source consistently publishes information related to one or more monitored domains.

## Credibility

The publisher has identifiable ownership, authorship or institutional responsibility.

## Originality

The source provides:

- primary information;
- original reporting;
- meaningful specialist analysis.

## Structured Access

The source provides:

- stable RSS;
- Atom;
- official API;
- another explicitly approved structured endpoint.

## Automation Permission

The required automated retrieval must be compatible with:

- the source endpoint;
- relevant terms;
- licensing;
- public-repository use.

Personal access alone is insufficient.

## Timeliness

Publication timestamps should be available and reasonably reliable.

Because the current system filters using `published_at`, timestamp quality is particularly important.

## Metadata Quality

Titles and URLs must be sufficiently complete for automated processing.

Descriptions or other public context should be evaluated as a product-quality dimension.

Missing descriptions may remain technically valid.

They are no longer considered automatically harmless.

A source with systematically thin metadata may be a poor fit for a report expected to provide sufficient context.

## Reader Accessibility

Follow-up access should be evaluated explicitly.

Possible categories include:

- public web;
- Bocconi direct;
- Bocconi SearchLib;
- Bocconi database;
- additional paid subscription;
- unknown.

Restricted follow-up is not automatically disqualifying if the public structured metadata already provides enough lawful intelligence value.

## Stability

The endpoint should be sufficiently stable for low-maintenance automated collection.

## Value-to-Noise Ratio

A meaningful proportion of output should be relevant to the project.

## Diversity Contribution

The source should ideally add useful:

- geographic;
- institutional;
- industry;
- technical;
- evidentiary;
- editorial;
- perspective diversity.

## Public Repository Compatibility

Permitted metadata and links must be safe to store publicly.

## Operational Compatibility

The source should work with the bounded collector without disproportionate special handling.

## Context Contribution

The source should contribute enough public structured context to support the intended report experience.

This criterion becomes increasingly important as richer-report requirements are designed.

---

# Source Exclusion or Replacement Criteria

A source should be rejected, disabled, replaced or removed when one or more of the following materially apply:

- it requires prohibited scraping;
- it requires paid API access for core operation;
- it requires private account access for automated collection;
- its licence does not permit the intended automated use;
- it republishes content without meaningful added value;
- it produces excessive promotional material;
- its publication timestamps are unusable;
- it repeatedly generates malformed or misleading records;
- it has weak or unclear ownership;
- it primarily publishes unsupported rumours;
- it systematically duplicates better sources;
- its content falls outside monitored priorities;
- its endpoint is too unstable for the value provided;
- it creates copyright or privacy risk;
- maintaining it requires disproportionate manual intervention;
- its public structured metadata is consistently too thin;
- selected links are repeatedly inaccessible and the report cannot provide enough public context;
- an alternative source offers materially better accessibility, metadata or reliability.

A low-value source should normally be replaced rather than supported through increasingly complex source-specific code.

---

# Source Evaluation Scorecard

During the active source-expansion phase, each candidate should be reviewed against a common scorecard.

The scorecard does not need to become application code.

A structured manual review is sufficient.

Evaluate:

```text
Source name
Primary domain contribution
Source tier
Publisher type
Public RSS/Atom available?
Official free API available?
Automation permitted?
Private credentials required?
Publication timestamps reliable?
Description/context richness
Public article accessibility
Bocconi direct access
Bocconi SearchLib access
Bocconi database access
Unique coverage contribution
Overlap with existing sources
Expected noise
Expected publication frequency
Expected maintenance
Public-repository compatibility
Recommended status
```

Possible recommendations:

```text
Approve
Approve for controlled test
Monitor
Retain
Replace
Disable
Reject
Research further
```

Do not compress all of these properties into one numerical score unless later evidence shows that a score improves decision quality.

---

# Current Production Source Universe

The current source universe contains seven active feeds.

It is now a **baseline under review**, not a final production set.

## Active Sources

| Source ID | Source | Tier | Default Domains | Language | Geographic Scope | Current Policy Status |
|---|---|---:|---|---|---|---|
| `bbc_world` | BBC News World | 2 | None | English | Global | Active |
| `bbc_business` | BBC News Business | 2 | None | English | Global | Active |
| `ecb_press` | European Central Bank | 1 | None | English | EU; Euro Area | Active |
| `ec_highlights` | European Commission Highlighted News | 1 | None | English | European Union | Active |
| `istat_press_en` | Istat Press Releases | 1 | Economics and Macroeconomics | English | Italy | Active |
| `openai_news` | OpenAI News | 1 | Artificial Intelligence | English | Global | Active |
| `sifted_articles` | Sifted | 2 | Startups and Venture Capital | English | Europe | Active — Under Review |

All current active sources:

- use public RSS;
- require no paid API;
- require no private credentials for collection;
- were successfully collected through the project collector;
- expose usable publication timestamps in tested production runs.

These facts establish technical compatibility.

They do not establish permanent product suitability.

---

# Current Source Roles

| Source | Primary Current Role | Current Review Consideration |
|---|---|---|
| BBC News World | Broad international reporting | Evaluate relevance yield and geopolitical coverage |
| BBC News Business | Broad business reporting | Evaluate company/economic signal and noise |
| European Central Bank | Primary monetary-policy and institutional evidence | Retain authority while avoiding routine low-value material |
| European Commission Highlighted News | Primary EU policy evidence | Evaluate relevance density |
| Istat Press Releases | Primary Italian economic/statistical evidence | Evaluate role in broader Italy coverage |
| OpenAI News | Primary OpenAI/AI company information | Evaluate publisher concentration and independent AI coverage gap |
| Sifted | European startup and VC specialist coverage | Review paywall/accessibility and thin public metadata |

The source-expansion phase should compare candidate sources against these existing roles rather than simply adding more feeds.

---

# Sifted Review

Sifted is the first current source requiring explicit production-policy review.

## Why It Was Added

Sifted contributes:

- European startup coverage;
- venture-capital coverage;
- specialist reporting;
- a perspective absent from official institutional sources.

Its source default:

```text
Startups and Venture Capital
```

remains logically appropriate for the selected feed.

## Problem Observed

A production-selected Sifted article required a Sifted Pro subscription.

The current report entry did not contain enough context to remove the need for click-through.

Sifted entries have also been observed with missing or limited descriptions.

This creates a potential failure of the intended reading workflow.

## Current Decision

Do not automatically remove Sifted.

Do not build a paywall bypass.

Do not scrape Sifted Pro article bodies.

Instead evaluate:

- how frequently selected Sifted links require Pro access;
- how rich its public RSS fields actually are;
- whether the feed provides additional structured fields not currently used;
- how much unique startup/VC information it contributes;
- whether the user can access relevant content through another legitimate route;
- whether an alternative public specialist source provides better metadata or accessibility.

Possible outcomes:

```text
Keep
Keep with revised report handling
Replace
Disable
```

The decision should be evidence-based.

---

# Source Expansion Policy

There is no target number of sources.

The previous idea of approximately 20–30 sources should not be treated as an implementation objective.

The correct number is:

> the smallest source universe that provides strong coverage, useful diversity and manageable maintenance.

Add a source only when it solves a demonstrated:

- coverage gap;
- evidentiary gap;
- geographic gap;
- domain gap;
- source-diversity problem;
- accessibility problem;
- metadata-richness problem;
- opportunity-detection gap.

Source expansion should not become source accumulation.

---

# Source Expansion Workflow

The immediate source-expansion workflow should be:

```text
Career Agent
→ define desired information universe
→ identify priority domains and candidate publications

Development project
→ evaluate technical and policy eligibility
→ inspect public structured endpoints
→ inspect metadata richness
→ inspect accessibility
→ inspect overlap
→ test controlled collection
→ inspect generated report contribution
→ approve or reject
```

The Career Agent owns:

- strategic information priorities;
- professional relevance;
- desired source mix;
- source/domain ideas.

This Development project owns:

- automation suitability;
- feed/API validation;
- licence and access boundaries;
- metadata quality;
- collector compatibility;
- tests;
- production configuration;
- maintenance assessment.

---

# Source-Default Domain Policy

Source defaults are classification evidence.

They are not publisher categories.

A source should receive a default domain only when essentially every item in the selected feed can reasonably be treated as belonging to that topic.

This distinction is important because the current ranking system gives points for every assigned domain and the first assigned domain determines primary report placement.

## Broad Sources

Broad heterogeneous feeds should normally use:

```yaml
default_domains: []
```

Current broad sources with no defaults:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News.

This does not mean those publishers lack topical identity.

It means source identity alone is insufficient evidence to classify every individual item.

## Narrow Sources

Current narrow source defaults:

- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

No current source receives multiple blanket defaults.

Additional domains require content evidence.

## Production Evidence

Earlier broader source defaults caused:

- unrelated BBC Business items to appear under Economics;
- routine ECB material to appear under Economics and Europe/EU;
- inflated relevance scores caused by source defaults rather than article evidence.

The rule remains:

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

These fields remain sufficient for the current deterministic pipeline.

`source_type` currently represents feed protocol.

Supported values:

```text
rss
atom
```

It is not a descriptive publisher category.

## Default-Domain Validation

`default_domains` remains a required configuration field but may be empty.

Example:

```yaml
default_domains: []
```

`geographic_scope` remains required and non-empty.

## Accessibility Metadata

Accessibility information is now useful for source governance.

However, fields such as:

```text
reader_access
bocconi_access
automation_permission
metadata_richness
review_status
```

should not automatically be added to `sources.yaml`.

First determine whether storing these properties in production configuration creates operational value.

A policy document or source-review table may be sufficient.

Avoid turning descriptive research metadata into runtime configuration without a processing need.

## Potential Future Metadata

Fields such as:

```text
homepage_url
country
notes
date_added
date_reviewed
```

may be added only if required by maintenance.

Operational data such as:

```text
last_successful_run
failure_count
```

should generally be generated by the system rather than manually maintained.

---

# Article Metadata Policy

The current canonical article record preserves source-provided and derived fields including:

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

The Python model remains the implementation source of truth.

Potential richer-report fields should not be documented as implemented until the richer-report design phase determines what is needed.

Possible future fields may include:

```text
author
source_categories
public_summary
public_content_excerpt
canonical_url
geographies
content_type
matched_entities
duplicate_cluster_id
related_source_count
```

Any new source-content field must preserve provenance.

---

# Required Core Metadata

A structurally valid current record normally requires:

- source identifier;
- title;
- usable HTTP or HTTPS article URL;
- timezone-aware retrieval timestamp.

Publication timestamp is not required for structural validity.

However, the current collection-window policy requires a usable `published_at` value for inclusion.

A record may therefore be:

- structurally valid;
- available in validation results;
- excluded from current report processing because publication time is unavailable.

---

# Publication Timestamp Policy

Current behaviour remains conservative.

If `published_at` is missing:

- the record may remain structurally valid;
- the system does not invent a publication time;
- retrieval time is not treated as confirmed publication time;
- the record is excluded from collection-window eligibility.

The current production feeds generally expose usable publication timestamps.

No timestamp fallback is justified yet.

---

# Reporting-Window Timing Policy

The current production CLI uses:

```text
actual run start - 24 hours
through
actual run start
```

Both boundaries are inclusive.

Scheduled production use has exposed an important limitation:

GitHub Actions may start a scheduled workflow substantially later than the configured cron time.

Therefore:

```text
scheduler delay
→ later actual run start
→ shifted 24-hour publication window
→ potentially different report composition
```

This has become an evidence-based information-quality question.

A future deterministic reporting cutoff may be preferable.

No change should be made solely from one sparse report.

Continue collecting evidence before changing window semantics.

---

# Description and Public Context Policy

The current implementation stores short descriptions provided through public feeds.

Current report configuration truncates descriptions to:

```text
300 characters
```

Descriptions remain optional for structural validity.

Production evidence has changed the interpretation of missing descriptions.

Previously:

> missing description = acceptable optional metadata

Now:

> missing description = technically valid but potentially important product-quality limitation

A source with consistently missing or very short descriptions may be a poor fit for the future richer-report requirement.

## Current Rule

The system may store:

- public feed descriptions;
- public structured summaries;
- other permitted public metadata.

It must not fabricate source text.

## Future Richer Context

The richer-report design phase should investigate, in order:

1. richer fields already present in RSS/Atom;
2. public structured metadata;
3. official free APIs;
4. permitted public-page metadata or extraction only where clearly justified;
5. more complex solutions only if simpler mechanisms are insufficient.

Do not assume full-article ingestion is required.

---

# URL Metadata Policy

The original publisher-provided article URL should be preserved.

A separate normalised URL is used for deterministic identity and duplicate handling.

Current normalisation removes selected tracking parameters and fragments.

Some publisher-specific parameters may remain.

Further URL cleaning should be implemented only if remaining parameters materially affect:

- deduplication;
- report readability;
- repository quality.

---

# Classification Policy

## Current Classification Inputs

The classifier currently uses:

1. source default domains;
2. title keywords;
3. description keywords.

Keyword matching is deterministic, case-insensitive and protected by word-boundary behaviour.

## Multi-Domain Behaviour

A record may receive multiple domains.

For report display:

- one domain becomes primary;
- additional domains are displayed as secondary metadata.

## Unclassified Behaviour

Unclassified records:

- remain valid processed records;
- are not shown in the main report by default.

This is intentional.

The system should prefer missing a classification over confidently presenting a misleading one.

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

Avoid broad terms that create large numbers of false positives.

Ambiguous terms may require:

- multiple-word phrases;
- source context;
- exclusions;
- combinations.

Examples of ambiguous terms include:

- model;
- market;
- Apple;
- cloud;
- bank;
- government;
- defence;
- president;
- prime minister.

Keyword complexity should grow from observed errors.

---

# Evidence-Driven Keyword Procedure

When a recall problem is observed:

1. identify specific relevant unclassified records;
2. propose a small candidate keyword set;
3. simulate matches against real processed records;
4. inspect intended and unintended matches;
5. add only terms with acceptable precision;
6. rerun the report;
7. inspect output quality;
8. stop when the result is good enough.

This procedure produced the existing Global Politics additions:

- war;
- conflict;
- parliament.

It remains the default procedure for taxonomy changes.

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

Do not build a large entity registry without a validated classification or ranking need.

---

# Ranking Policy

The ranking system should prioritise practical relevance.

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

## Upstream Evidence Rule

If weak source defaults or classification rules inflate scores:

> fix the upstream evidence before changing ranking weights.

## Potential Future Factors

Only if justified:

- domain priority;
- geography priority;
- tracked entities;
- content type;
- recency;
- independent multi-source coverage;
- source accessibility;
- metadata richness.

Accessibility or metadata richness should not be added to the ranking formula merely because they matter to source selection.

Source eligibility may be the simpler place to address those problems.

---

# Duplicate Policy

Duplicate reduction should reduce repetition without discarding genuinely distinct information.

## Current Exact Duplicate Rules

Implemented checks use:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

## Near Duplicates

Near-duplicate detection is not currently implemented.

Possible future examples:

- minor headline variations;
- syndicated copies;
- multiple outlets reporting the same announcement;
- updated versions of the same story.

Add near-duplicate logic only if repeated production reports show a material problem.

## Conservative Principle

False merging is more harmful than modest repeated coverage.

When uncertain, preserve separate records.

---

# Multi-Source Coverage

The current system does not create story clusters or related-source counts.

If real use demonstrates a need, future clustering may preserve:

- primary record;
- related record IDs;
- unique source count;
- source diversity;
- publication range.

Multi-source coverage should not automatically increase relevance unless independent reporting can be distinguished from syndication.

---

# Language Policy

## Target Languages

The target system should support:

- English;
- Italian.

## Current Implementation

The current seven-source registry uses English-language feeds.

Istat is collected through its English press-release feed.

Full bilingual taxonomy behaviour has not yet been validated.

## Future Italian Sources

Source/domain expansion may introduce Italian-language sources.

When this happens:

- classification examples must include Italian;
- relevant keyword lists may include Italian terms;
- original source titles should remain preserved;
- translation should not become a hidden production dependency.

## Translation

The core system should not depend on automated translation.

Original source language should be preserved.

---

# Source Diversity Policy

A useful production report should not be unnecessarily dominated by one publisher, source tier, geography or source type.

Diversity should be reviewable across:

- publishers;
- source tiers;
- geographies;
- primary versus secondary evidence;
- general versus specialist coverage;
- domains.

The system does not need artificial quotas.

A highly relevant source may legitimately appear several times.

## Production Evidence

Scheduled production has produced at least one report that was substantially shorter and more concentrated than previous reports.

The run itself was technically healthy.

This demonstrates:

> technical source success does not guarantee adequate information diversity.

The observation is sufficient to justify monitoring:

- displayed share by publisher;
- displayed share by domain;
- unusually sparse reports;
- repeated empty domains.

It is not yet sufficient to justify automatic concentration penalties or quotas.

## Source-Expansion Implication

The next source expansion should seek diversity because coverage improves—not because a numeric quota requires more publishers.

---

# Opportunity-Source Policy

Milan and Bocconi opportunity monitoring requires particularly strong selectivity.

An opportunity should be relevant when it offers meaningful:

- learning;
- networking;
- career information;
- project experience;
- research exposure;
- competition exposure;
- startup or innovation access.

Potential metadata may include:

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

The core system does not currently require a separate opportunity database.

A dedicated opportunity workflow should be added only if suitable public structured sources and repeated user value justify it.

---

# Copyright and Public-Repository Policy

The repository may store and display, when permitted:

- headlines;
- source names;
- direct links;
- timestamps;
- short feed-provided descriptions;
- public structured summaries;
- other permitted public metadata;
- system-generated classifications;
- system-generated scores;
- run metadata;
- source-health metadata.

The repository must not store or display:

- complete copyrighted articles;
- substantial copied passages;
- paywalled article bodies;
- authenticated premium article bodies;
- private newsletter text;
- private email content;
- licensed database full text;
- unauthorised copyrighted material;
- credentials;
- authentication tokens.

When uncertainty exists:

> store less content and preserve provenance and the original source link.

---

# Bocconi Licence Boundary

Bocconi institutional access materially expands what the user may personally read.

It does not automatically expand what the production pipeline may retrieve.

The production system must never:

- embed Bocconi credentials;
- automate OpenAthens authentication;
- scrape authenticated FT, WSJ, NYT, Economist or Il Sole 24 Ore content merely because the user can read it;
- scrape Factiva;
- scrape Nexis Uni;
- scrape Business Source Ultimate;
- bulk-download licensed database content;
- ingest Bloomberg Terminal content automatically;
- ingest LSEG Workspace content automatically;
- redistribute restricted full text into the public repository.

A premium publication may still become a production source if it separately provides:

- a public feed;
- an official free API;
- public structured metadata;
- another automation-permitted endpoint.

The production eligibility decision must be based on that public interface, not the user's subscription.

---

# Source Lifecycle

A source may move conceptually through the following states.

## Candidate

Identified but not yet evaluated.

## Approved for Test

Passes preliminary source-policy review and is ready for controlled technical validation.

## Active

Enabled in production.

## Monitoring

Remains active or temporarily disabled while a reliability or quality concern is reviewed.

## Disabled

Retained in history/configuration but not collected.

## Removed

No longer retained because it is obsolete or clearly unsuitable.

Not every lifecycle state needs to become a runtime `sources.yaml` field.

Use configuration complexity only when it creates operational value.

## Current Example

Sifted is conceptually:

```text
Active
+
Monitoring / Under Review
```

Its exact status does not need a new configuration field yet.

---

# Adding a Source

Before adding a production source, ask:

1. What information gap does it solve?
2. Which domain or evidentiary role does it add?
3. Does it provide stable structured public access?
4. Is automated retrieval permitted?
5. Does it require private credentials?
6. Are timestamps reliable?
7. How rich are its public descriptions or metadata?
8. Can the user open the linked content?
9. If the article is restricted, is enough public context available anyway?
10. Does Bocconi provide legitimate personal follow-up access?
11. Does it duplicate a current source?
12. Is it primary evidence, reporting, specialist analysis or discovery?
13. How noisy is the feed?
14. How frequently does it publish?
15. Does it improve geographic or domain coverage?
16. Does it require special collector logic?
17. What maintenance cost does it add?
18. Can permitted metadata be stored in the public repository?
19. How will the source be tested?
20. What existing source could it replace rather than simply supplement?

A source should not be added because:

- it is prestigious;
- it is popular;
- it exists;
- the user can personally access it;
- increasing source count appears sophisticated.

---

# Reviewing an Existing Source

Review an active source when:

- repeated collection failures occur;
- its feed changes materially;
- its metadata quality degrades;
- relevant timestamps disappear;
- it produces excessive noise;
- its items are systematically unclassified;
- it dominates the report without corresponding value;
- linked content becomes inaccessible;
- feed descriptions are too thin for the intended report;
- an alternative source becomes clearly better;
- maintenance becomes disproportionate.

The review should result in an explicit decision:

```text
Retain unchanged
Retain with configuration correction
Monitor
Replace
Disable
Remove
```

---

# Source Replacement Principle

Adding a new source is not always the correct response to weak coverage.

Prefer:

```text
weak current source
→ identify limitation
→ compare alternatives
→ replace when appropriate
```

over:

```text
weak current source
→ keep indefinitely
→ add more sources
→ increase noise and maintenance
```

A smaller, stronger registry is preferable to source accumulation.

---

# Source Health

Current run summaries provide per-run source health.

Available source statuses:

```text
success
empty
failed
```

This is sufficient for current operations.

Long-term source-health history should be implemented only if repeated maintenance work demonstrates value.

Do not add source-health infrastructure merely because production automation now exists.

---

# Taxonomy Validation Strategy

Technical pipeline stability and information-quality stability are separate.

The system is now technically production-operational.

Information quality is the active development concern.

Use real production records and reports to evaluate:

- classification accuracy;
- false-positive classifications;
- relevant unclassified records;
- duplicate behaviour;
- source-tier usefulness;
- timestamp quality;
- report usefulness;
- report concentration;
- source-default quality;
- ranking order;
- accessibility;
- metadata richness;
- source overlap;
- missing strategic domains.

When Italian-language sources are introduced, include bilingual examples.

Do not build a large artificial validation dataset before sufficient real examples exist.

---

# Source Expansion Validation Strategy

For each candidate source:

## Step 1 — Policy Review

Confirm:

- purpose;
- domain contribution;
- source tier;
- public access mechanism;
- automation eligibility;
- likely accessibility;
- likely metadata richness.

## Step 2 — Technical Probe

Inspect:

- feed/API availability;
- HTTP behaviour;
- redirects;
- timestamps;
- descriptions;
- entry counts;
- malformed records;
- expected request requirements.

## Step 3 — Controlled Collector Test

Run through the actual collector.

Do not rely only on opening the URL manually.

## Step 4 — Normalisation Test

Confirm returned entries normalise correctly.

## Step 5 — Sample Classification Review

Inspect:

- expected domains;
- unclassified rate;
- obvious false positives;
- source-default suitability.

## Step 6 — Report Contribution

Generate or simulate report contribution.

Evaluate:

- usefulness;
- noise;
- repetition;
- source concentration;
- context richness.

## Step 7 — Maintenance Decision

Ask:

- did the source solve the intended gap?
- is the value worth recurring maintenance?
- should it replace an existing source?

## Step 8 — Production Approval

Only after validation:

- update configuration;
- update tests;
- inspect diff;
- rerun full suite;
- run real pipeline;
- inspect report;
- commit.

---

# Current Resolved Information Decisions

## Current Implemented Domains

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

---

## Domains Under Active Reconsideration

- Financial Markets;
- Italy;
- Milan and Bocconi Ecosystem.

They remain unimplemented until the source/domain strategy provides suitable evidence.

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

## Source Under Explicit Review

- Sifted.

---

## Source Defaults

Current defaults:

```text
BBC News World                → none
BBC News Business             → none
European Central Bank         → none
European Commission           → none
Istat Press Releases          → Economics and Macroeconomics
OpenAI News                   → Artificial Intelligence
Sifted                        → Startups and Venture Capital
```

---

## Multi-Domain Records

**Decision:** supported.

---

## Primary Report Placement

**Decision:** each story appears once.

Additional domains are shown as secondary metadata.

---

## Unclassified Records

**Decision:** preserved in processed data but omitted from the main report.

---

## Relevance Score

**Decision:** stored and displayed.

---

## Score Components

**Decision:** stored for transparency.

---

## Maximum Items Per Domain

**Current configured value:** 5.

---

## Maximum Total Items

**Current configured value:** 30.

---

## Description Length

**Current configured maximum:** 300 characters.

This value may change during richer-report design.

---

## Exact Duplicate Policy

**Decision:**

1. normalised URL;
2. normalised title.

---

## Collection Window

**Current CLI default:** previous 24 hours relative to actual execution.

A fixed reporting cutoff is now an open design question.

---

## Missing Publication Timestamp

**Current policy:** exclude from collection-window eligibility.

Do not replace missing publication time with retrieval time.

---

## Global Politics Keyword Refinement

Current evidence-based additions:

- war;
- conflict;
- parliament.

---

## Personal Institutional Access

**Decision:** Bocconi access affects manual reading value, not automatic ingestion permission.

---

## Premium Sources

**Decision:** a paywall does not automatically exclude a source.

Instead ask:

- is the public structured metadata useful enough?
- can the user access the article legitimately?
- is a better accessible source available?
- does the source add unique value?

---

# Open Information Decisions

## Sifted

Determine whether to:

- retain;
- replace;
- disable;
- retain only if richer public feed fields can be used.

---

## Future Source Universe

No fixed source-count target.

The Career Agent should define strategic priorities.

This project should determine technical eligibility.

---

## Financial Markets Domain

Evaluate during the active source/domain expansion phase.

---

## Italy Domain

Evaluate during the active source/domain expansion phase.

---

## Milan and Bocconi Domain

Evaluate only if suitable public structured sources exist.

---

## Additional AI Sources

Evaluate whether OpenAI News creates excessive single-publisher dependence.

---

## Additional European Sources

Evaluate whether current EU institutional coverage is too narrow or too official-source-heavy.

---

## Italian Sources

Evaluate whether stronger Italian political, business and financial coverage is required.

Bocconi access to Il Sole 24 Ore and other publications may make some sources valuable for manual follow-up, but production eligibility still depends on public automation-compatible endpoints.

---

## Publisher Concentration Controls

Continue observing production reports.

Do not add quotas from a single sparse day.

---

## Metadata-Richness Threshold

The richer-report design phase should determine what minimum public context a source needs.

No fixed character threshold exists yet.

---

## Domain Priority Weights

Not implemented.

Add only if report ordering demonstrates a need.

---

## Tracked Entities

Not implemented.

---

## Geographic Classification

Not implemented at article level.

---

## Content-Type Classification

Not implemented.

---

## Near-Duplicate Threshold

No threshold exists.

---

## Multi-Source Story Clustering

Deferred.

---

## Source-Health History

Per-run status remains sufficient.

---

## Ranking Weights

Remain provisional.

---

# Information Quality Decision Rules

Before adding a source, taxonomy rule, metadata field or classification dimension, ask:

1. What observed problem does it solve?
2. How often does the problem occur?
3. Does it materially reduce report usefulness?
4. Can replacing a weak source solve it?
5. Can a simpler configuration change solve it?
6. Does the source provide enough lawful public context?
7. Can the user access deeper reading if needed?
8. What false positives or false negatives could the change create?
9. How will the improvement be evaluated?
10. What recurring maintenance does it create?
11. Does it preserve explainability?
12. Does it preserve zero recurring monetary cost?
13. Does it preserve credential safety?
14. Does it preserve copyright/public-repository safety?
15. Is the change necessary now?

The default is not always to preserve the current configuration.

Now that production evidence exists, weak sources should be corrected or replaced when justified.

The preferred pattern remains:

```text
observe real problem
→ isolate the cause
→ compare the simplest solutions
→ test the smallest justified change
→ rerun
→ inspect information quality
→ stop when the improvement is sufficient
```

---

# Current Information-Policy Limitations

Known current limitations include:

- seven of ten target domains are implemented;
- the source universe contains only seven active sources;
- all current automated feeds are English-language;
- full bilingual behaviour is unvalidated;
- Financial Markets is not implemented;
- Italy is not implemented as a topic domain;
- Milan/Bocconi is not implemented;
- article-level geography is not implemented;
- content type is not implemented;
- entity tracking is not implemented;
- near-duplicate detection is not implemented;
- multi-source story clustering is not implemented;
- source-health history remains per-run;
- ranking weights remain provisional;
- keyword lists remain conservative;
- some relevant records remain unclassified;
- public descriptions vary substantially by source;
- some Sifted articles may require Sifted Pro;
- the current report may therefore contain items that are difficult to understand or access;
- source concentration can vary materially by day;
- the rolling collection window depends on actual scheduled execution time;
- personal Bocconi access is not represented in runtime source configuration.

These limitations define the current information-quality maturity.

They do not imply that every corresponding feature should be implemented.

The immediate priority is:

> correct and expand sources and domains first.

---

# Current Information-Quality Priorities

Priorities are currently ordered as follows.

## 1. Correct Weak Existing Sources

Beginning with Sifted.

Evaluate:

- accessibility;
- metadata richness;
- unique value;
- alternatives.

## 2. Expand Source Coverage Deliberately

Use Career Agent strategy followed by Development-project technical review.

## 3. Reconsider Deferred Domains

Especially:

- Financial Markets;
- Italy;
- Milan/Bocconi.

## 4. Improve Source Diversity

Address genuine coverage gaps without artificial quotas.

## 5. Design Richer Report Context

Only after the revised source universe is understood.

## 6. Revisit Ranking or Advanced Classification

Only if source correction and richer context do not solve the dominant problems.

---

# Current Status

**Status:** Phase 3 automation complete; source/domain correction and expansion active.

**Implemented and validated:**

- seven active public RSS sources;
- seven active topic domains;
- configurable domains;
- optional source-default domains;
- deterministic title/description classification;
- multiple domains;
- primary report placement;
- secondary-domain metadata;
- unclassified handling;
- deterministic source-tier scoring;
- exact URL/title deduplication;
- previous-24-hours filtering;
- public-safe metadata policy;
- real-source timestamp compatibility;
- source-level failure isolation;
- scheduled production execution;
- automated repository persistence.

**Current source-policy findings:**

- technical compatibility does not guarantee product suitability;
- accessibility must be evaluated explicitly;
- metadata richness matters for report usefulness;
- a paywalled destination can materially reduce usefulness when feed context is thin;
- Sifted is under review;
- Bocconi substantially expands personal reading access;
- institutional access does not authorize automated authenticated ingestion;
- public automation suitability and personal reader accessibility are separate dimensions;
- source concentration and sparse reports require observation;
- the existing seven-source set should now be corrected and expanded.

**Current controlled / provisional elements:**

- seven-source registry;
- seven-domain implemented subset;
- keyword lists;
- ranking weights;
- report limits;
- source-default assignments;
- source diversity;
- public-context richness;
- collection-window anchoring.

**Not implemented:**

- full ten-domain coverage;
- Financial Markets;
- Italy topic classification;
- Milan/Bocconi topic classification;
- tracked entities;
- article-level geography;
- content type;
- near-duplicate clustering;
- multi-source clustering;
- long-term source-health history;
- richer-context generation.

**Next information-quality milestone:**

> Use the Career Agent to define the desired expanded source/domain universe, then evaluate each proposed source here for automation suitability, accessibility, metadata richness, reliability, overlap, maintenance and public-repository compatibility before changing production configuration.

After the source/domain universe is corrected:

> begin the dedicated richer-report design phase.

---

# Changelog

## 2026-08-14 — Source Accessibility, Bocconi Access and Expansion Policy

- Reconciled the source policy with completed Phase 3 production automation.
- Changed the current priority from preserving the seven-source automation baseline to correcting and expanding the source/domain universe.
- Recorded that technical feed compatibility does not guarantee product usefulness.
- Added metadata richness as an explicit source-quality dimension.
- Added reader accessibility as an explicit source-quality dimension.
- Added the two-axis distinction between automation suitability and reader accessibility.
- Added public web, Bocconi Direct, SearchLib and Database access categories.
- Recorded confirmed Bocconi direct access to Financial Times, Wall Street Journal, New York Times, The Economist and Il Sole 24 Ore.
- Recorded Corriere della Sera as a special institutional archive-access case.
- Recorded the role of Foreign Affairs, Harvard Business Review, Time and Economia & Management as institutional reading resources.
- Recorded Factiva, Nexis Uni and Business Source Ultimate as research/database resources rather than automated production sources.
- Recorded Bloomberg, LSEG Workspace, FactSet, Capital IQ Pro and Aida as professional research resources rather than automated production sources.
- Added the three-layer model of automated public sources, Bocconi premium reading and research/database resources.
- Explicitly prohibited using Bocconi credentials as production automation credentials.
- Explicitly separated institutional reading rights from automated ingestion rights.
- Added source-accessibility and public-context criteria to source inclusion and exclusion rules.
- Added a standard source-evaluation scorecard.
- Changed the seven-source universe from a production-automation baseline to a baseline under active review.
- Marked Sifted as active but under explicit review.
- Recorded the Sifted Pro accessibility problem.
- Recorded limited Sifted feed descriptions as a related product-quality concern.
- Added the source replacement principle.
- Added the controlled source-expansion workflow separating Career Agent strategy from Development-project technical validation.
- Changed Financial Markets, Italy and Milan/Bocconi from passively deferred domains to candidates for active reconsideration.
- Recorded report concentration and sparse-output observations as source-diversity evidence.
- Recorded scheduler-delay/report-window coupling as an information-quality consideration.
- Preserved zero recurring cost, deterministic processing, copyright safety and public-repository constraints.
- Deferred richer-report implementation until source/domain correction is complete and the richer-context requirement has been designed.

## 2026-08-11 — Phase 2 Real-Source Taxonomy and Source-Policy Validation

- Replaced the one-sample-source implementation state with seven validated public RSS sources.
- Expanded the implemented taxonomy from two to seven active domains.
- Kept Financial Markets, Italy and Milan/Bocconi as deferred target domains.
- Recorded the exact active source universe.
- Recorded source tiers, language and geographic scope.
- Added the rule that source defaults represent genuine source-wide topical evidence rather than publisher categories.
- Added support for explicitly empty `default_domains`.
- Removed broad defaults from BBC World, BBC Business, ECB and European Commission.
- Restricted Istat to an Economics and Macroeconomics default.
- Restricted OpenAI to an Artificial Intelligence default.
- Restricted Sifted to a Startups and Venture Capital default.
- Recorded false positives caused by broad source defaults.
- Recorded `war`, `conflict` and `parliament` as evidence-based Global Politics keyword additions.
- Recorded that `government`, `defence`, `president` and `prime minister` were tested but not added.
- Confirmed real-source publication timestamps were usable.
- Confirmed descriptions are optional and may legitimately be missing.
- Recorded that the large OpenAI feed did not require special handling because collection-window filtering kept eligible output manageable.
- Recorded the distinction between source tier and story importance.
- Preserved conservative classification, exact deduplication, copyright boundaries and public-repository safety.

## 2026-08-11 — Phase 1 Taxonomy and Source-Policy Reconciliation

- Distinguished the target ten-domain taxonomy from the implemented two-domain Phase 1 configuration.
- Recorded current implemented classification behaviour.
- Recorded exact duplicate policy.
- Recorded ranking weights and source-tier scoring.
- Recorded report limits and description length.
- Recorded current collection-window and missing-publication-time policy.
- Replaced the earlier source-count planning target with a smallest-credible-source strategy.
- Moved geography, entities, content type and near-duplicate clustering behind evidence from real reports.
- Clarified that technical stability does not imply information-quality stability.
- Preserved the source hierarchy, inclusion/exclusion policy, copyright boundaries and broader strategic scope.

## Initial Information Taxonomy and Source Policy Baseline

- Established the ten target topic domains.
- Defined geographic and content-type dimensions.
- Defined source tiers.
- Defined source inclusion and exclusion criteria.
- Defined source lifecycle and evaluation principles.
- Defined classification, ranking and duplicate-reduction policy.
- Defined copyright and public-repository boundaries.