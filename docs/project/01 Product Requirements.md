# Daily Intelligence System — Product Requirements

> **Purpose**
>
> Define what the Daily Intelligence System must do for the user, which behaviours are required, which constraints are fixed, and which acceptance criteria determine whether the product is useful.
>
> This document defines product behaviour rather than technical implementation details.
>
> Technical architecture belongs in `02 System Architecture.md`.
>
> Source suitability, taxonomy and source-governance decisions belong in `03 Information Taxonomy and Source Policy.md`.
>
> Current implementation status and sequencing belong in `04 Development Roadmap and Status.md`.

---

> **Primary Question**
>
> *What must the Daily Intelligence System do to provide useful, reliable and low-maintenance daily intelligence?*

---

# 1. Product Objective

The Daily Intelligence System should provide a concise, reliable and transparent daily view of high-value developments relevant to:

- economics and macroeconomics;
- financial markets;
- companies and corporate strategy;
- politics and geopolitics;
- artificial intelligence;
- technology and software;
- startups and venture capital;
- Europe and the European Union;
- Italy;
- Milan and the Bocconi professional ecosystem.

The system should reduce the need to manually check many separate information sources.

The desired workflow is:

```text
automatic collection
→ selective filtering
→ readable daily report
→ understand important developments
→ click through only when deeper reading is useful
```

The system should not become:

- a generic news aggregator;
- a real-time trading terminal;
- a social-media monitor;
- a complete university event calendar;
- a replacement for professional research databases;
- an automated premium-news reader;
- an AI-generated newsletter.

The product should optimise for:

> **high-value awareness with negligible daily maintenance.**

---

# 2. Primary User Need

The user needs a single recurring information workflow that helps answer:

> **What happened that is important enough for me to know today?**

The system should surface developments that contribute to:

- economic understanding;
- financial-market literacy;
- company and strategy awareness;
- geopolitical awareness;
- AI and technology literacy;
- startup and venture-capital awareness;
- European institutional understanding;
- Italian economic/business awareness;
- Milan/Bocconi professional awareness.

The system should help build cumulative professional and analytical context over time.

---

# 3. Core User Workflow

The intended daily workflow is:

```text
system runs automatically
→ public sources are collected
→ records are normalized
→ invalid/out-of-window records are removed
→ duplicates are reduced
→ relevant domains are assigned
→ items are ranked
→ a bounded report is generated
→ outputs are stored
→ failures are visible
→ user reads one report
```

The user should not need to:

- manually trigger the normal daily run;
- manually copy articles between systems;
- manually classify stories;
- manually create daily reports;
- maintain credentials for production sources;
- repair the pipeline as part of normal daily use.

Manual work should be reserved for:

- deeper reading;
- occasional source evaluation;
- project development;
- reviewing important premium articles;
- opportunities that necessarily live behind private systems.

---

# 4. Hard Product Constraints

The following are fixed unless explicitly changed.

## 4.1 Zero Recurring Monetary Cost

The core production system must operate at zero recurring monetary cost.

It must not require:

- paid news APIs;
- paid automation services;
- paid hosting;
- paid databases;
- recurring OpenAI API usage;
- recurring GitHub AI/Copilot credits.

---

## 4.2 Negligible Daily Manual Work

Normal operation should be automatic.

The product should not depend on:

- daily copy-and-paste;
- manual report assembly;
- daily login to source websites;
- manual article classification;
- manual Git operations.

---

## 4.3 Transparent Sources

Every report item should preserve enough provenance to understand:

- where it came from;
- when it was published;
- how it was classified;
- why it received its relevance score;
- where to read the original item.

---

## 4.4 Public-Safe Production

The production pipeline must not require:

- private credentials;
- authenticated premium scraping;
- Bocconi authentication;
- paywall bypass;
- restricted copyrighted article bodies;
- private email or newsletter ingestion.

The public repository must remain safe to expose.

---

## 4.5 Deterministic Core

The production system should remain deterministic where practical.

Core operation should not depend on:

- LLM classification;
- LLM summarisation;
- agents;
- embeddings;
- RAG;
- vector databases;
- machine-learning ranking.

More sophisticated techniques require a validated product limitation that simpler mechanisms cannot solve.

---

# 5. Current Product State

The current production system provides:

- eight active public RSS sources;
- nine active topic domains;
- automated daily execution;
- source-level failure isolation;
- publication-window filtering;
- exact duplicate reduction;
- deterministic classification;
- deterministic ranking;
- processed JSONL outputs;
- daily Markdown reports;
- JSON run summaries;
- automated GitHub persistence;
- visible degraded/failure status.

Current active sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Tech.eu;
8. Tech Europe Foundation.

Current active domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Companies and Corporate Strategy;
4. Artificial Intelligence;
5. Technology and Software;
6. Startups and Venture Capital;
7. Europe and the European Union;
8. Financial Markets;
9. Milan and Bocconi Ecosystem.

Strategically required but not yet implemented as a dedicated domain:

10. Italy.

The system is operational.

The main remaining limitation is no longer basic automation.

It is:

> **insufficient information breadth and uneven domain coverage.**

---

# 6. Report Requirements

Each daily report should provide a readable bounded summary of the most relevant eligible stories.

Current report fields include:

- headline;
- original link;
- source;
- publication time;
- relevance score;
- primary domain;
- secondary domains when present;
- source-provided description;
- run metadata.

Current report limits:

```text
maximum items per domain = 5
maximum total items      = 30
```

These are upper bounds, not targets.

A sparse report is acceptable if few genuinely useful items exist.

The system should not fill space with low-value stories simply to reach a quota.

---

# 7. Report Selection Behaviour

A report item must:

- come from a configured active source;
- have a usable publication timestamp;
- fall within the monitored collection window;
- pass structural validation;
- survive exact deduplication;
- receive at least one active domain;
- remain within report caps.

Unclassified records should:

- remain in processed data;
- not appear in the main report by default.

This is intentional.

The product should prefer:

> **a smaller accurate report**

over:

> **a larger misleading report.**

---

# 8. Relevance Behaviour

Current relevance score is deterministic.

It uses:

- source tier;
- assigned domains;
- matched keywords.

The exact scoring formula is an implementation detail owned by the architecture/configuration documents.

Product requirement:

> Higher-ranked items should generally correspond to higher-value developments.

Ranking should remain:

- explainable;
- inspectable;
- stable enough for regression testing.

Do not optimise scoring independently from classification quality.

If weak evidence creates inflated scores:

> correct the evidence first.

---

# 9. Source Requirements

A source should contribute a clear information role.

Useful information roles include:

- primary institutional evidence;
- high-quality reporting;
- specialist intelligence;
- independent analysis;
- professional ecosystem information;
- official company/research-lab evidence.

A source should not be added merely because:

- it is prestigious;
- it has RSS;
- it increases source count;
- it covers a topic already covered by several sources.

The product should prefer:

> **complementary information functions**

over:

> **publisher accumulation.**

---

# 10. Current Coverage Requirements

The target information universe contains ten strategic macroareas.

The product does not require equal source counts across all domains.

It does require enough useful coverage that major macroareas are not effectively defined by one weak or incidental source.

---

# 11. Global Politics and Geopolitics

## Product Need

The system should provide awareness of major political and geopolitical developments with meaningful:

- economic;
- market;
- security;
- technological;
- trade;
- policy implications.

## Current State

Main current coverage:

```text
BBC World
+ European Commission spillover
```

## Requirement Status

> **Operational but publisher-concentrated.**

This is not currently the highest-priority gap.

The product does not require another generic global-news feed before higher-value weaknesses are addressed.

---

# 12. Economics and Macroeconomics

## Product Need

The report should surface important developments involving:

- growth;
- inflation;
- labour markets;
- monetary policy;
- fiscal policy;
- public debt;
- trade;
- productivity;
- financial conditions.

## Current State

Current meaningful sources include:

```text
ECB
Istat
European Commission
BBC Business
```

## Requirement Status

> **Reasonably served, but geographically/institutionally concentrated.**

Important missing roles include:

- US/global monetary-policy evidence;
- independent European economic interpretation.

The Federal Reserve is the highest-priority current candidate for the first role.

Bruegel is a leading candidate for the second.

---

# 13. Financial Markets

## Product Need

The system should provide high-signal awareness of:

- interest rates;
- bond yields;
- credit;
- financial conditions;
- capital markets;
- equity-market developments when material;
- IPOs;
- corporate financing;
- asset management;
- market structure;
- financial stability;
- major market reactions to macro/company developments.

The system should not become a real-time market-price monitor.

It should exclude or heavily deprioritise:

- trading tips;
- generic stock picking;
- routine daily market recaps;
- isolated price moves;
- technical-analysis content;
- price predictions.

## Current State

The domain is implemented.

However:

```text
no dedicated production Financial Markets source exists
```

## Requirement Status

> **Major unsatisfied coverage requirement.**

This is currently one of the highest-opportunity-cost product gaps.

Current highest-priority audit candidates:

1. Nasdaq;
2. Federal Reserve Board.

Later specialist candidates may include:

- MEF Treasury;
- ESMA;
- BIS;
- Euronext.

---

# 14. Companies and Corporate Strategy

## Product Need

The report should surface strategically meaningful developments involving:

- M&A;
- restructuring;
- capital allocation;
- corporate financing;
- major investment;
- business-model changes;
- market entry/exit;
- strategic partnerships;
- earnings/guidance when strategically important;
- bankruptcy/turnaround;
- material competitive shifts.

## Current State

Coverage is mainly incidental through:

```text
BBC Business
Tech.eu
```

## Requirement Status

> **Major unsatisfied coverage requirement.**

No current source provides a strong dedicated corporate-strategy layer.

Current strategic candidates include:

- Nasdaq;
- MIMIT;
- Lavoce.info;
- potentially targeted SEC filings later.

The product may retain an explicit residual gap in high-quality global corporate journalism if no legal, zero-cost substitute for FT/Reuters emerges.

It should not fill that gap with inferior sources solely for completeness.

---

# 15. Artificial Intelligence

## Product Need

The report should provide awareness of major:

- AI model developments;
- enterprise adoption;
- infrastructure;
- AI economics;
- safety/security;
- regulation;
- business-model shifts;
- workflow changes;
- material funding/M&A;
- frontier research.

## Current State

Current coverage:

```text
OpenAI News
+ incidental Tech.eu/BBC
```

## Requirement Status

> **Operational but excessively concentrated on one primary vendor.**

Desired information structure:

```text
OpenAI
→ primary source

second frontier lab
→ primary-source diversity

independent reporting
→ external analysis and scrutiny
```

Current strongest candidates:

```text
Google DeepMind
Ars Technica
```

The system does not need every major AI lab.

---

# 16. Technology and Software

## Product Need

The system should surface meaningful developments in:

- enterprise software;
- cloud;
- data infrastructure;
- cybersecurity;
- semiconductors;
- software platforms;
- developer systems;
- APIs;
- major open-source developments;
- digital infrastructure.

## Current State

Main coverage:

```text
Tech.eu
OpenAI spillover
BBC spillover
```

## Requirement Status

> **Moderately served.**

Independent technology reporting would improve the domain, but current opportunity cost is below Markets, Companies and Italy.

Ars Technica is the leading current candidate.

---

# 17. Startups and Venture Capital

## Product Need

The report should provide high-value awareness of:

- significant financing;
- major VC funds;
- exits;
- acquisitions;
- failures;
- venture strategy;
- startup policy;
- European/Italian ecosystem shifts;
- selected professional programmes/opportunities.

It should not become a funding-round ticker.

## Current State

Current specialist source:

```text
Tech.eu
```

Italian Tech Alliance has already passed its basic technical/source audit.

## Requirement Status

> **Operational but too dependent on one specialist.**

Italian Tech Alliance is the strongest current production-readiness candidate.

Its expected differentiated role is:

```text
Tech.eu
→ European company/deal coverage

Italian Tech Alliance
→ Italian VC ecosystem, policy, statistics and programmes
```

The product should not add several additional startup publications that mostly duplicate funding rounds.

---

# 18. Europe and the European Union

## Product Need

The system should surface meaningful developments involving:

- EU institutions;
- monetary policy;
- European regulation;
- competition;
- industrial policy;
- trade;
- capital markets;
- digital/AI policy;
- competitiveness;
- energy;
- strategic autonomy.

## Current State

Primary sources are strong:

```text
ECB
European Commission
```

## Requirement Status

> **Strong primary evidence, incomplete independent interpretation.**

A high-quality independent analytical source is desirable.

Bruegel is the current leading candidate.

---

# 19. Italy

## Product Need

Italy is a fixed strategic macroarea.

The system should eventually surface high-value developments involving:

- Italian macroeconomics;
- major companies;
- industrial developments;
- restructuring;
- banking;
- capital markets;
- corporate finance;
- industrial policy;
- investment;
- technology;
- innovation;
- startups;
- labour-market developments.

## Current State

Current production contribution comes mainly from:

```text
Istat
```

There is no dedicated Italy domain.

## Requirement Status

> **Major unsatisfied strategic requirement.**

Italy should not be solved through a single generic Italian newspaper.

The current preferred information architecture is differentiated:

```text
Istat
→ primary statistics

MIMIT
→ industrial policy / company situations

Lavoce.info
→ independent economic/business interpretation

Assolombarda
→ Milan/Lombardy firms and economy

Italian Tech Alliance
→ VC/startup ecosystem

Bank of Italy BDS later
→ structured financial/statistical signals
```

This remains a strategic target until each candidate is technically validated.

---

# 20. Milan and Bocconi Ecosystem

## Product Need

Milan/Bocconi is a fixed product requirement.

The system should surface high-value professional ecosystem intelligence such as:

- recruiting;
- employer events;
- finance events;
- consulting events;
- AI/data/technology events;
- startup/VC programmes;
- competitions;
- research opportunities;
- professional programmes;
- public lectures;
- relevant deadlines;
- Milan startup/VC/fintech developments;
- innovation ecosystems;
- strategically useful local business developments.

The product should avoid:

- generic campus noise;
- tourism;
- nightlife;
- irrelevant university administration;
- low-value networking events;
- broad city-event aggregation.

---

# 21. Current Milan/Bocconi Implementation

The first automated implementation is now active through:

```text
Tech Europe Foundation
```

TEF contributes mainly:

- entrepreneurship;
- deep tech;
- startup ecosystem;
- founder/programme activity;
- university-linked innovation.

The domain is classified through a validated TEF source default rather than generic keywords.

## Requirement Status

> **Partially satisfied.**

The first automated implementation exists and has passed pipeline validation.

However, TEF alone does not satisfy the full requirement.

Important remaining gaps:

- finance recruiting;
- consulting recruiting;
- employer events;
- complete opportunity/deadline discovery;
- established-company ecosystem;
- industrial ecosystem;
- selected high-value public lectures.

---

# 22. Bocconi Career Services Boundary

Bocconi Career Services is extremely valuable to the user.

However, key information and registration infrastructure exists partly inside authenticated:

```text
yoU@B
JobGate
```

The product does **not** require the Daily Intelligence System to replicate these private systems.

The automated acceptance target is instead:

> **Surface the highest-value public structured professional ecosystem intelligence that can be collected safely, automatically and at zero recurring cost.**

The system must not:

- log into yoU@B automatically;
- scrape JobGate;
- embed Bocconi credentials;
- bypass authenticated access.

Private Career Services remains a complementary manual layer.

---

# 23. Professional Opportunity Behaviour

If a public structured source provides meaningful opportunities, the report should prioritise items where missing the information could close a valuable opportunity.

Examples:

- application deadline;
- programme;
- competition;
- recruiting event;
- professional academy;
- startup call;
- research opportunity.

Current article-based pipeline uses publication time.

Future sources may reveal that:

```text
publication date
≠
application deadline
≠
event date
```

A dedicated opportunity/deadline state model is **not currently required**.

Introduce one only if repeated real use demonstrates that publication-only treatment causes meaningful opportunities to be missed.

---

# 24. Reader Accessibility Requirement

Technical ingestion and reader accessibility are different product dimensions.

The system should consider:

```text
Can the pipeline ingest the source?
```

and separately:

```text
Can the user read the linked story if deeper investigation is useful?
```

A technically usable source with consistently inaccessible links may still provide poor product value.

A premium publication accessible through Bocconi may have high user value while remaining unsuitable for automated ingestion.

Both dimensions matter.

---

# 25. Bocconi Premium Reading

The user has legitimate institutional reading access to several high-value premium publications.

These may include:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore;
- other SearchLib/database resources.

This access can increase the value of manual click-through.

It does **not** authorise production to:

- automate Bocconi login;
- scrape authenticated articles;
- store premium article bodies;
- bypass publisher restrictions.

---

# 26. Premium Bocconi Exception

A narrow premium-source exception exists.

A premium publication may be considered for production discovery when:

- the publication is unusually valuable;
- the user can legitimately read it;
- a public/automation-compatible discovery endpoint exists;
- the pipeline does not access premium article bodies;
- persistence and public-repository use remain lawful;
- a thinner automated entry is consciously accepted.

This exception does not override:

- zero-cost requirements;
- licensing;
- RSS terms;
- persistence restrictions.

Financial Times and Il Sole 24 Ore have already been audited under this framework.

Both remain inactive.

---

# 27. Source Expansion Requirement

The source universe is not yet complete.

Source expansion should now be driven by:

> **missing information functions**

rather than:

> **interesting publications.**

Current highest-cost gaps:

```text
Financial Markets
Companies / Corporate Strategy
Italy
Independent AI / Technology
```

Secondary concentration gaps:

```text
Startups / VC
Milan / Bocconi
```

The product does not require a fixed source count.

It requires enough differentiated coverage to support useful daily awareness.

---

# 28. Current Strategic Source-Audit Queue

Current Development audit order:

1. Nasdaq;
2. Federal Reserve Board;
3. MIMIT;
4. Lavoce.info;
5. Bruegel;
6. Assolombarda;
7. Ars Technica;
8. Google DeepMind News.

These are research priorities, not production approvals.

Each source must still pass:

- policy review;
- endpoint validation;
- metadata review;
- collector test;
- normalisation test;
- classification review;
- report contribution review;
- licensing/persistence review;
- automated tests.

Parallel:

```text
Italian Tech Alliance
→ production-readiness decision
```

Its basic audit should not be repeated.

---

# 29. Source Roles Expected From the New Audit Queue

## Nasdaq

Expected role:

```text
Financial Markets
+ Companies
+ earnings
+ IPOs
+ corporate finance
```

Product risk:

- retail-investor noise;
- routine stock stories;
- excessive volume.

The product requirement is not “add Nasdaq”.

It is:

> Find a narrow Nasdaq feed configuration that materially improves Markets/Companies without becoming a firehose.

---

## Federal Reserve

Expected role:

```text
US monetary policy
rates
credit
financial conditions
banking
```

Expected product value:

- reduce Europe-only macro bias;
- strengthen Financial Markets;
- complement ECB.

---

## MIMIT

Expected role:

```text
Italy
industrial policy
company restructuring
strategic investment
innovation
```

Expected product value:

- strengthen Italy;
- strengthen Companies/Corporate Strategy;
- provide primary evidence.

---

## Lavoce.info

Expected role:

```text
independent Italian economic/business interpretation
```

Expected product value:

- explain developments that primary institutional sources only report.

---

## Bruegel

Expected role:

```text
independent European economic-policy analysis
```

Expected product value:

- complement ECB and European Commission primary evidence.

---

## Assolombarda

Expected role:

```text
Milan/Lombardy firms
industry
economic research
professional ecosystem
```

Expected product value:

```text
TEF
→ startups / innovation

Assolombarda
→ established firms / industry / Milan economy
```

---

## Ars Technica

Expected role:

```text
independent AI / technology reporting
```

Expected product value:

- reduce vendor-driven AI coverage;
- improve software/systems context.

---

## Google DeepMind

Expected role:

```text
second frontier-lab primary AI source
```

Expected product value:

- diversify primary AI evidence.

---

# 30. Richer Context Requirement

The current report often provides too little context below the relevance score.

Current description limit:

```text
300 characters
```

The validated desired behaviour is:

> **The report should provide enough lawful context to understand the core development without requiring immediate click-through.**

The target workflow is:

```text
read report
→ understand core development
→ click only when deeper reading is worthwhile
```

not:

```text
read headline
→ click every source
→ discover what happened
```

This is a validated product requirement.

Implementation remains intentionally deferred until source/domain coverage is sufficiently mature.

---

# 31. Richer Context Constraints

Future richer-report design must preserve:

- zero recurring cost;
- copyright safety;
- source attribution;
- provenance;
- no premium article-body scraping;
- no production AI dependency unless explicitly justified later;
- manageable total report length;
- transparent source-specific fallback behaviour.

Preferred solution order:

1. richer feed metadata;
2. public structured summaries;
3. official free APIs;
4. narrowly permitted deterministic extraction;
5. more complex mechanisms only if required.

---

# 32. Failure Visibility Requirement

The user should be able to distinguish:

```text
success
degraded
failure
```

A degraded run should remain useful when:

- one or more sources fail;
- enough valid information remains;
- the failure is visible.

The product must not silently present degraded coverage as complete coverage.

A critical configuration or pipeline failure should fail clearly.

---

# 33. Reliability Requirement

Normal daily operation should:

- run without user intervention;
- tolerate isolated source failures;
- preserve successful records;
- generate deterministic outputs;
- expose meaningful failure information;
- avoid corrupting previous output;
- not publish broken critical runs.

Perfect source availability is not required.

Visible controlled degradation is acceptable.

---

# 34. Historical Record Requirement

Processed daily records should remain available as a historical archive.

This provides value for:

- review;
- trend reconstruction;
- taxonomy regression;
- classification testing;
- future evaluation.

Current JSONL/Git storage is sufficient.

No database is required unless the repository-native model becomes a demonstrated limitation.

---

# 35. Quality Evaluation Requirement

A technically successful run is not automatically a good product result.

Evaluation should inspect:

- important stories included;
- important stories missed;
- weak stories included;
- duplicated developments;
- misleading domains;
- inflated relevance scores;
- inaccessible links;
- source concentration;
- report length;
- context quality.

Primary product question:

> **Would reading this report make the user meaningfully better informed?**

---

# 36. Classification Quality Requirement

The product should not target a high classification percentage.

Correct behaviour may legitimately leave many records unclassified.

The quality objective is:

```text
high-value stories
→ classified appropriately

low-value / irrelevant stories
→ omitted

ambiguous stories
→ preferably unclassified rather than mislabeled
```

Keyword changes must be grounded in real missed or misclassified records.

---

# 37. Multilingual Classification Requirement

The system should support both English and Italian source material where strategically useful.

Current multilingual evidence includes:

- Il Sole 24 Ore testing;
- Italian Tech Alliance testing.

The Artificial Intelligence acronym must be represented intentionally as:

```text
AI
```

rather than generic lowercase:

```text
ai
```

to avoid false Italian matches.

Do not introduce language detection unless current deterministic mechanisms become inadequate.

---

# 38. Duplicate Requirement

Exact duplicates should not appear repeatedly.

Current exact reduction uses:

- URL;
- normalized title.

Near-duplicate clustering is not currently required.

Italian Tech Alliance provides a plausible future use case, but implementation requires repeated evidence of report degradation.

---

# 39. Source Diversity Requirement

The report should not become structurally dependent on one publisher where stronger differentiated coverage is feasible.

However:

> **source diversity is not a quota.**

Do not enforce equal publisher/domain counts.

Improve diversity through better sources and missing information roles.

---

# 40. Daily Schedule Requirement

The system should run automatically every day.

Current intended schedule:

```text
06:05 Europe/Rome
```

GitHub Actions may start later than the nominal minute.

Current product behaviour uses:

```text
actual execution time - previous 24 hours
```

This is acceptable until repeated evidence shows meaningful missed developments.

---

# 41. Public Repository Requirement

The repository should remain understandable and auditable.

It should contain:

- source configuration;
- domain configuration;
- processing code;
- tests;
- run summaries;
- processed metadata;
- reports;
- project documentation.

It should not contain:

- credentials;
- private Career OS material;
- premium article bodies;
- authenticated content;
- private emails;
- restricted database exports.

---

# 42. Product Non-Goals

The current product does **not** aim to become:

- Bloomberg;
- Reuters Terminal;
- Factiva;
- a research database;
- a portfolio-management system;
- a stock screener;
- a social network;
- a full recruiting CRM;
- a complete Bocconi Career Services mirror;
- an automated premium newspaper reader;
- an autonomous AI research agent;
- a generic personal assistant;
- a sophisticated news website.

These may overlap with future user workflows, but they are outside the current system boundary.

---

# 43. Acceptance Criteria — Core System

The core system is acceptable when:

- it runs automatically;
- it uses zero recurring monetary cost;
- source failures are visible;
- records are reproducibly processed;
- outputs are stored automatically;
- daily manual work is negligible;
- report provenance is clear;
- no credentials are exposed;
- no restricted premium bodies are stored;
- deterministic tests pass;
- the repository remains understandable.

These core criteria are currently substantially satisfied.

---

# 44. Acceptance Criteria — Information Universe

Phase 4 information expansion is sufficiently complete when:

- Financial Markets has meaningful dedicated coverage;
- Companies/Corporate Strategy is materially stronger than incidental coverage;
- Italy has a validated practical implementation decision;
- Milan/Bocconi has more than nominal ecosystem coverage or has reached a justified public-source limit;
- AI is no longer structurally defined by OpenAI alone;
- Startups/VC has sufficiently differentiated coverage;
- major active sources have clear information roles;
- source-access/persistence decisions are explicit;
- further source work provides lower marginal value than improving report context.

This does not require:

- equal source counts;
- complete coverage;
- every researched source activated;
- a Reuters/FT replacement;
- perfect bilingual coverage.

---

# 45. Acceptance Criteria — Milan/Bocconi

The Milan/Bocconi requirement is considered **partially satisfied** today.

Current minimum achieved:

- dedicated active domain;
- validated public structured source;
- automated integration;
- zero credentials;
- no private scraping;
- normal pipeline compatibility;
- useful startup/innovation ecosystem signal.

For stronger maturity, the system should additionally provide some combination of:

- established-company ecosystem intelligence;
- Milan/Lombardy economic/business information;
- selected high-value professional events;
- relevant opportunities/deadlines;
- finance/consulting/business ecosystem coverage.

It does not need to automate every private Bocconi opportunity.

---

# 46. Acceptance Criteria — Italy

Italy remains unsatisfied as a dedicated product macroarea.

A viable implementation should provide:

- meaningful coverage beyond Istat;
- at least one strong company/industrial or business role;
- useful economic interpretation or policy evidence;
- acceptable Italian-language classification;
- public/automation-compatible endpoints;
- manageable noise;
- no premium authenticated ingestion.

The exact number of sources is not fixed.

---

# 47. Acceptance Criteria — Financial Markets

Financial Markets should not be considered mature merely because the domain exists.

Maturity requires useful recurring coverage of some combination of:

- rates;
- yields;
- credit;
- financial conditions;
- capital markets;
- IPOs;
- corporate financing;
- market structure;
- material equity-market developments.

The report should remain explanatory rather than price-centric.

---

# 48. Acceptance Criteria — AI Diversity

AI coverage should eventually include:

```text
at least one strong primary source
+
at least one meaningfully different primary or independent source
```

The current working target is:

```text
OpenAI
+ Google DeepMind
+ independent reporting such as Ars Technica
```

This is a directional target, not a mandatory three-source quota.

---

# 49. Phase Sequencing Requirement

Current product sequence:

```text
Phase 4
source/domain correction and expansion

→

Phase 5
richer-report design

→

Phase 6
richer-report implementation/evaluation
```

Do not begin richer-report implementation while the information universe is still changing materially.

The switch should occur when:

> **another source/domain change has lower expected user value than adding context to the stories already being selected.**

---

# 50. Current Product Priorities

Current priority order:

## Priority 1

Strengthen:

```text
Financial Markets
Companies / Corporate Strategy
```

Current first Development audit:

```text
Nasdaq
```

---

## Priority 2

Add:

```text
US/global monetary-policy and financial-condition evidence
```

Current candidate:

```text
Federal Reserve Board
```

---

## Priority 3

Build a stronger Italian economic/business information layer.

Current candidates:

```text
MIMIT
Lavoce.info
Assolombarda
Italian Tech Alliance
```

---

## Priority 4

Reduce AI vendor concentration.

Current candidates:

```text
Ars Technica
Google DeepMind
```

---

## Priority 5

Improve independent Europe/EU interpretation.

Current candidate:

```text
Bruegel
```

---

## Priority 6

Continue Milan/Bocconi complementarity.

Current candidate:

```text
Assolombarda
```

Later possibilities:

```text
ISPI
Camera di Commercio
Fintech District
```

---

# 51. Deferred Product Requirements

The following are not current requirements unless evidence changes:

- real-time market prices;
- portfolio tracking;
- semantic story clustering;
- advanced entity tracking;
- automated translation;
- LLM summaries;
- opportunity database;
- deadline reminder system;
- statistical-event engine;
- custom mobile app;
- dashboard;
- search engine;
- vector database;
- private-email ingestion;
- authenticated Bocconi automation.

Each requires a separate validated need.

---

# 52. Current Product Limitations

Known limitations include:

- only eight active sources;
- only nine active domains;
- Italy lacks a dedicated implemented domain;
- Financial Markets lacks a dedicated source;
- Companies/Corporate Strategy is weak;
- AI remains vendor-concentrated;
- Startups/VC remains strongly Tech.eu-dependent;
- Milan/Bocconi is only partially covered;
- English-language sources dominate production;
- Italian-language coverage is limited;
- report descriptions are capped at 300 characters;
- near-duplicate same-story coverage is not clustered;
- article-level geography is not implemented;
- content type is not implemented;
- long-term source-health trends are not tracked;
- private Career Services opportunities are not automated;
- statistical structured data is not yet converted into intelligence events;
- GitHub scheduler latency can shift the daily window;
- high-quality global corporate reporting remains an explicit residual gap.

These are not automatic feature requests.

They are constraints to evaluate against actual user value.

---

# 53. Product Decision Rules

Before adding a feature, source or domain, ask:

1. What user problem does this solve?
2. Is the problem visible in actual reports or workflow?
3. What information role is missing?
4. Does the proposed change add genuinely differentiated value?
5. Is there a simpler option?
6. Can it remain zero-cost?
7. Can it remain low-maintenance?
8. Is the source legally and technically compatible?
9. Could it increase noise or misleading classifications?
10. How will success be tested?
11. What existing component can be reused?
12. Does the expected value exceed the implementation and maintenance cost?

Default decision:

> **Do less unless the evidence supports more.**

---

# 54. Definition of Done for a Product Change

A product change is complete only when:

- the requirement is clear;
- its user value is identified;
- the smallest appropriate implementation is selected;
- relevant source/policy constraints are checked;
- deterministic tests pass;
- real output is inspected where applicable;
- no unrelated files change;
- documentation matches implementation;
- limitations are explicit;
- the repository remains understandable;
- the change does not introduce recurring monetary cost.

---

# 55. Current Product Status

**Core production loop:** operational.

**Automation:** operational.

**Zero recurring cost:** preserved.

**Daily manual work:** negligible.

**Source transparency:** implemented.

**Failure visibility:** implemented.

**Financial Markets domain:** implemented but source coverage weak.

**Milan/Bocconi domain:** implemented through TEF but only partially satisfies the broader requirement.

**Italy domain:** pending.

**AI diversity:** insufficient.

**Companies/Corporate Strategy coverage:** insufficient.

**Startups/VC diversification:** incomplete.

**Richer report context:** validated requirement, intentionally deferred.

Current active product objective:

> **Strengthen the source and domain universe through differentiated information roles until the marginal value of additional source work falls below the value of richer report context.**

Current next Development action:

> **Begin the Nasdaq source audit, then proceed through the ranked domain-gap-driven audit queue while moving Italian Tech Alliance toward a production-readiness decision.**

---

# Changelog

## 2026-08-17 — Milan/Bocconi First Implementation and Source-Expansion Reframing

- Updated the current production state from seven to eight active sources.
- Updated the current taxonomy from eight to nine active domains.
- Added Tech Europe Foundation as the first production Milan/Bocconi source.
- Changed Milan/Bocconi from fully pending to partially satisfied.
- Clarified that TEF mainly covers startup, entrepreneurship, deep-tech and innovation ecosystem activity.
- Preserved recruiting, employer events, finance/consulting opportunities and complete deadline coverage as remaining Milan/Bocconi gaps.
- Clarified that complete private Career Services replication is not a product requirement.
- Preserved authenticated yoU@B and JobGate as manual/private layers.
- Recorded Italy as the remaining strategically approved but unimplemented dedicated macroarea.
- Recorded Financial Markets as implemented but still lacking dedicated source coverage.
- Recorded Companies/Corporate Strategy as a major remaining information gap.
- Recorded AI vendor concentration as an active product-quality issue.
- Incorporated the information-function-before-publisher-count expansion principle.
- Replaced the obsolete FT-first next-source sequence with the new audit queue:
  1. Nasdaq;
  2. Federal Reserve;
  3. MIMIT;
  4. Lavoce.info;
  5. Bruegel;
  6. Assolombarda;
  7. Ars Technica;
  8. Google DeepMind.
- Recorded Italian Tech Alliance as a production-readiness candidate rather than an unexplored source.
- Preserved richer-report context as a validated but deferred product requirement.

## 2026-08-17 — Tech.eu Replacement and Financial Markets Activation

- Replaced Sifted with Tech.eu as the active European startup/technology specialist.
- Added Financial Markets as an implemented domain.
- Recorded the source-quality lesson that metadata richness and follow-up usability matter independently from parser compatibility.
- Preserved BBC Business temporarily until stronger business/markets replacement coverage is demonstrated.
- Added the Premium Bocconi Exception while preserving the authentication boundary.
- Confirmed Milan/Bocconi as a fixed product requirement.

## 2026-08-14 — Production Automation and Richer-Context Requirement

- Reconciled product requirements with completed GitHub Actions automation.
- Recorded automated daily execution and repository persistence.
- Recorded GitHub scheduler latency as a known operational limitation.
- Added reader accessibility as a source-quality dimension.
- Added the three-layer public/premium/database reading model.
- Recorded the validated richer-report context requirement.
- Deferred richer-context implementation until source/domain correction is sufficiently mature.

## 2026-08-11 — Real-Source Production Validation

- Expanded production validation to seven real public RSS sources.
- Expanded implemented taxonomy to seven domains.
- Added explicit source-default quality rules.
- Preserved conservative classification and unclassified records.
- Validated degraded-source behaviour.

## 2026-08-11 — Local Vertical Slice Baseline

- Recorded the complete local collection-to-report product workflow.
- Added report limits and primary/secondary domain behaviour.
- Added collection-window eligibility requirements.
- Added deterministic ranking and output persistence requirements.

## Initial Product Requirements Baseline

- Defined the core user workflow.
- Defined zero-cost and negligible-manual-work constraints.
- Defined report, source, taxonomy, failure, storage and privacy requirements.