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

- twelve active public RSS sources;
- ten active topic domains;
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
8. Tech Europe Foundation;
9. Federal Reserve Board Monetary Policy;
10. MIMIT News;
11. Lavoce.info Imprese;
12. Google DeepMind News.

Current active domains:

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

All ten strategic macroareas now have an implemented production domain.

The system is operational.

The main remaining limitation is no longer basic automation or missing domain implementation.

It is:

> **uneven information depth and incomplete source-role coverage across several domains.**

Current strongest residual gaps include:

- global Companies and Corporate Strategy;
- broader Financial Markets beyond monetary-policy evidence;
- independent AI and technology reporting;
- independent European economic-policy interpretation;
- Startups/VC diversification;
- Milan/Lombardy established-company and professional ecosystem coverage.

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

All ten now have implemented domains.

The product does not require equal source counts across all domains.

It does require enough useful coverage that major macroareas are not effectively defined by one weak or incidental source.

A domain being implemented does not mean that its source universe is mature.

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
Federal Reserve Board Monetary Policy
Istat
European Commission
BBC Business
Lavoce.info Imprese
```

The system now has substantial primary monetary and macroeconomic evidence across:

- euro area;
- United States;
- Italy;
- European Union.

## Requirement Status

> **Well served for primary evidence; independent interpretation remains less complete.**

The previous US monetary-policy gap has been materially closed through the Federal Reserve Board Monetary Policy source.

The main remaining role is:

- independent European/global economic interpretation that adds analytical value beyond primary institutions.

Bruegel was investigated for this role but did not fit the current production architecture safely.

The system should continue searching only if a cleaner differentiated source exists.

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

Dedicated upstream evidence now exists through:

```text
Federal Reserve Board Monetary Policy
```

Additional selective financial-market interpretation is available through:

```text
Lavoce.info Imprese
```

Validated current coverage is strongest for:

- monetary policy;
- rates;
- financial conditions;
- central-bank decisions;
- selected capital-market developments.

## Requirement Status

> **Partially satisfied — monetary/rates coverage is materially stronger, broader markets coverage remains incomplete.**

The previous condition:

```text
no dedicated production Financial Markets source exists
```

is no longer accurate.

Remaining high-value gaps include:

- capital markets;
- corporate financing;
- market structure;
- broader credit-market developments;
- material equity-market/company-market developments;
- stronger causal market reporting.

The product should continue to prefer explanatory market intelligence over price-centric coverage.

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

Current meaningful coverage now comes from:

```text
BBC Business
Tech.eu
MIMIT News
Lavoce.info Imprese
```

Current information roles:

```text
BBC Business
→ broad international business reporting

Tech.eu
→ European technology/startup and selected company developments

MIMIT News
→ primary Italian industrial policy,
  restructuring and strategic-investment evidence

Lavoce.info Imprese
→ independent Italian business/company interpretation
```

## Requirement Status

> **Materially improved but still incomplete.**

The domain is no longer served only incidentally by BBC Business and Tech.eu.

However, a strong global dedicated corporate-strategy/reporting role remains missing.

The product may retain an explicit residual gap in high-quality global corporate journalism if no legal, zero-cost substitute for FT/Reuters emerges.

It should not fill that gap with inferior or legally ambiguous sources solely for completeness.

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

Current first-party primary coverage:

```text
OpenAI News
Google DeepMind News
```

Additional incidental coverage comes from:

```text
Tech.eu
BBC
```

OpenAI and DeepMind now provide meaningfully different frontier-lab primary evidence.

## Requirement Status

> **Primary-source diversity achieved; independent scrutiny remains incomplete.**

The minimum diversity structure:

```text
one strong primary source
+
one meaningfully different primary or independent source
```

is now satisfied through:

```text
OpenAI
+ Google DeepMind
```

The stronger target remains:

```text
OpenAI
+ Google DeepMind
+ independent reporting
```

but this is a maturity objective, not a mandatory quota.

Ars Technica was investigated for the independent-reporting role but did not pass the current persistence-policy gate.

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
Google DeepMind spillover
OpenAI spillover
BBC spillover
```

## Requirement Status

> **Moderately served.**

Independent technology/systems reporting would improve the domain.

Ars Technica was strategically attractive but did not pass the current persistence-policy gate.

The product should not add another generic technology publication unless it provides clearly differentiated information value and clean automation/persistence compatibility.

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

Current specialist production source:

```text
Tech.eu
```

Additional ecosystem contribution comes from:

```text
Tech Europe Foundation
```

Italian Tech Alliance has already passed its basic technical/source audit.

## Requirement Status

> **Operational but still dependent on a small number of specialist roles.**

Italian Tech Alliance remains a production-readiness candidate.

Its expected differentiated role is:

```text
Tech.eu
→ European company/deal coverage

Tech Europe Foundation
→ selected startup / entrepreneurship / ecosystem activity

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

Additional selective specialist coverage comes from:

```text
Tech.eu
```

## Requirement Status

> **Strong primary evidence, incomplete independent interpretation.**

A high-quality independent analytical source remains desirable.

Bruegel was audited for this role and proved strategically strong but technically/persistence-incompatible under the current architecture.

The product should continue searching only if a cleaner source can provide the same information function without source-specific complexity.

---

# 19. Italy

## Product Need

Italy is a fixed strategic macroarea.

The system should surface high-value developments involving:

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

Italy now has a dedicated production domain.

Current differentiated production architecture:

```text
Istat
→ primary statistics and macroeconomic evidence

MIMIT News
→ industrial policy, company restructuring,
  strategic investment and company-policy evidence

Lavoce.info Imprese
→ independent economic/business interpretation
```

Italian-language deterministic classification has been validated through:

- live source records;
- narrow keyword additions;
- historical-regression checks;
- uppercase acronym handling;
- real production runs.

## Requirement Status

> **Viable first production implementation achieved; broader maturity remains incomplete.**

The previous requirement that Italy provide:

- meaningful coverage beyond Istat;
- at least one strong company/industrial or business role;
- useful economic interpretation or policy evidence;
- acceptable Italian-language classification;
- public/automation-compatible endpoints;
- manageable noise;
- no premium authenticated ingestion;

has now been satisfied at a first production level.

Remaining maturity gaps include:

- Italian banking;
- broader capital markets;
- major-company reporting beyond industrial-policy events;
- Milan/Lombardy established-company intelligence;
- selected startup/VC ecosystem depth.

Italy should therefore no longer be treated as an unimplemented strategic requirement.

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

The first automated implementation is active through:

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

Assolombarda was audited as a strong complement for established firms and the Milan/Lombardy economy, but its current feeds do not satisfy production timestamp and persistence requirements.

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

The source universe is not assumed complete.

Source expansion should continue to be driven by:

> **missing information functions**

rather than:

> **interesting publications.**

Current highest-cost residual gaps:

```text
Global Companies / Corporate Strategy
Broader Financial Markets
Independent AI / Technology reporting
Independent Europe/EU interpretation
```

Secondary concentration/maturity gaps:

```text
Startups / VC
Milan / Bocconi
Milan / Lombardy established-company coverage
```

Italy and AI primary-source diversity are no longer first-order implementation gaps.

The product does not require a fixed source count.

It requires enough differentiated coverage to support useful daily awareness.

After the next research batch, source expansion should be explicitly compared against the marginal value of richer report context.

---

# 28. Current Strategic Source-Research Requirement

The previous source-audit queue has been completed.

Completed audit batch:

```text
Nasdaq
Federal Reserve Board
MIMIT
Lavoce.info
Bruegel
Assolombarda
Ars Technica
Google DeepMind
```

Stable outcomes include:

```text
Federal Reserve Monetary Policy
→ Active

MIMIT News
→ Active

Lavoce.info Imprese
→ Active

Google DeepMind News
→ Active

Nasdaq
→ Standby

Bruegel
→ Standby / rejected depending feed

Assolombarda
→ Standby

Ars Technica
→ Standby
```

Detailed source-policy rationale belongs in:

```text
03 Information Taxonomy and Source Policy.md
```

The next source step should **not** be another preselected Development queue.

Instead:

> **Run a fresh strategic source-research pass against the current information-function gaps.**

The Career Agent may be used for this discovery step because it can evaluate source value against broader professional and analytical priorities.

The Development project remains responsible for:

- policy review;
- endpoint validation;
- technical testing;
- classification decisions;
- persistence review;
- production approval.

Parallel existing candidate:

```text
Italian Tech Alliance
→ production-readiness decision
```

Its basic audit should not be repeated.

---

# 29. Expected Roles for the Next Source Research Pass

The new research should search for sources that could solve specific remaining roles.

## Global Companies / Corporate Strategy

Desired role:

```text
M&A
restructuring
capital allocation
corporate financing
strategy
major company developments
```

The objective is not to find a generic business-news publisher.

It is to find a source that materially improves the missing global corporate-strategy layer.

---

## Broader Financial Markets

Desired role:

```text
capital markets
credit
corporate financing
market structure
financial stability
material market-moving developments
```

Federal Reserve Monetary Policy already supplies strong rates/monetary evidence.

A new source should add a different markets information function.

---

## Independent AI / Technology Reporting

Desired role:

```text
external scrutiny
software / systems context
AI industry reporting
cybersecurity
infrastructure
frontier-lab evaluation
```

The system already has:

```text
OpenAI
Google DeepMind
```

A new source should therefore add independent interpretation rather than another lab blog.

---

## Independent Europe/EU Interpretation

Desired role:

```text
economic-policy analysis
industrial policy
competitiveness
trade
capital markets
European strategic issues
```

ECB and European Commission already supply primary evidence.

A new source should add analysis rather than duplicate institutional announcements.

---

## Startups / VC Diversification

Desired role:

```text
private-capital trends
European venture strategy
Italian VC ecosystem
fundraising / investment statistics
professional programmes
```

Do not add multiple sources that simply repeat funding rounds.

---

## Milan / Lombardy Professional and Business Ecosystem

Desired role:

```text
established firms
industry
professional events
economic research
finance/business ecosystem
high-value opportunities
```

TEF already covers startup/innovation activity.

A new source should complement, not duplicate, that role.

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

Implementation remains intentionally deferred until the source/domain universe is sufficiently mature.

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

Current multilingual production evidence includes:

- MIMIT News;
- Lavoce.info Imprese;
- prior Il Sole 24 Ore testing;
- Italian Tech Alliance testing;
- historical-regression testing for Italian keywords.

The Artificial Intelligence acronyms must be represented intentionally as:

```text
AI
IA
```

rather than generic lowercase forms when those would create false matches.

Current deterministic behaviour deliberately distinguishes intentionally uppercase acronyms from lowercase keywords.

Do not introduce language detection unless current deterministic mechanisms become inadequate.

The product should remain comfortably majority English unless additional Italian sources provide differentiated information value.

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

Public structured feeds should still be evaluated for persistence compatibility.

A public RSS endpoint does not automatically mean that every field it exposes is suitable for permanent public storage.

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
- Italy has a validated practical implementation;
- Milan/Bocconi has more than nominal ecosystem coverage or has reached a justified public-source limit;
- AI is no longer structurally defined by OpenAI alone;
- Startups/VC has sufficiently differentiated coverage or a justified reason not to expand further;
- major active sources have clear information roles;
- source-access/persistence decisions are explicit;
- unresolved gaps are clearly identified rather than filled with inferior sources;
- further source work provides lower marginal value than improving report context.

Current progress against these criteria:

```text
Financial Markets
→ partially achieved;
  dedicated monetary/rates coverage exists

Companies / Corporate Strategy
→ materially improved;
  global role remains incomplete

Italy
→ achieved at viable first-production level

Milan / Bocconi
→ partially achieved

AI primary-source diversity
→ achieved

Startups / VC diversification
→ incomplete

source roles / persistence decisions
→ materially documented
```

This does not require:

- equal source counts;
- complete coverage;
- every researched source activated;
- a Reuters/FT replacement;
- perfect bilingual coverage;
- elimination of all residual information gaps.

---

# 45. Acceptance Criteria — Milan/Bocconi

The Milan/Bocconi requirement is considered **partially satisfied**.

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

If public structured sources cannot safely provide some of these roles, the product may explicitly accept that limit rather than build fragile private-source automation.

---

# 46. Acceptance Criteria — Italy

Italy has reached a **viable first production implementation**.

Current minimum achieved:

- dedicated active Italy domain;
- meaningful coverage beyond Istat;
- Tier 1 Italian industrial/company-policy evidence through MIMIT;
- independent business/company interpretation through Lavoce.info Imprese;
- acceptable Italian-language classification;
- tested bilingual keyword behaviour;
- public/automation-compatible production endpoints;
- no premium authenticated ingestion.

Italy should therefore no longer be treated as an unsatisfied implementation requirement.

For stronger maturity, the system may still add differentiated coverage of:

- banking;
- broader capital markets;
- major companies;
- Milan/Lombardy established-company activity;
- Italian private capital.

The exact number of sources is not fixed.

---

# 47. Acceptance Criteria — Financial Markets

Financial Markets should not be considered mature merely because the domain exists.

The current system has achieved a meaningful first dedicated layer through Federal Reserve Monetary Policy.

Maturity still requires useful recurring coverage of a broader combination of:

- rates;
- yields;
- credit;
- financial conditions;
- capital markets;
- IPOs;
- corporate financing;
- market structure;
- material equity-market developments.

Current status:

> **Partially satisfied.**

The report should remain explanatory rather than price-centric.

A future Markets source should complement the existing monetary-policy role rather than duplicate it.

---

# 48. Acceptance Criteria — AI Diversity

Minimum AI source diversity requires:

```text
at least one strong primary source
+
at least one meaningfully different primary or independent source
```

This minimum is now achieved through:

```text
OpenAI
+ Google DeepMind
```

Both are active Tier 1 first-party sources but represent meaningfully different frontier labs.

For stronger maturity, the system should ideally add:

```text
independent reporting / scrutiny
```

if a legally and technically clean source can be found.

The current stronger target is therefore:

```text
OpenAI
+ Google DeepMind
+ independent reporting
```

This remains directional rather than a mandatory three-source quota.

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

Phase 4 is now materially more mature than at the previous checkpoint.

Do not begin richer-report implementation while a small number of high-value source corrections still clearly dominate expected user value.

However, source expansion must not become open-ended.

The switch should occur when:

> **another source/domain change has lower expected user value than adding context to the stories already being selected.**

After the next fresh source-research batch, this crossover should be evaluated explicitly.

---

# 50. Current Product Priorities

Current priority order:

## Priority 1

Run a fresh gap-driven source research pass against:

```text
Global Companies / Corporate Strategy
Broader Financial Markets
Independent AI / Technology reporting
Independent Europe/EU interpretation
Startups / VC diversification
Milan / Lombardy business and professional ecosystem
```

Do not restart the completed Nasdaq-to-DeepMind audit queue.

---

## Priority 2

Audit only newly justified candidates that add differentiated information roles.

The Development project should validate:

```text
policy
→ endpoint
→ metadata
→ collector
→ normalisation
→ classification
→ persistence
→ report contribution
→ tests
→ real pipeline
```

Do not activate sources merely because the strategic research recommends them.

---

## Priority 3

Resolve existing production-readiness candidates only where still high ROI.

Main existing example:

```text
Italian Tech Alliance
```

Its basic source audit should not be repeated.

---

## Priority 4

After the new candidate research/audit batch, compare:

```text
marginal value of another source
```

against:

```text
marginal value of richer report context
```

This comparison should determine whether Phase 4 continues or the product moves into richer-report design.

---

## Priority 5

Preserve current stable operation while source research continues.

Do not introduce unrelated:

- architecture;
- dashboard work;
- AI summarisation;
- clustering;
- event databases;
- statistical pipelines;

without validated need.

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

- twelve active sources still do not provide complete information-function coverage;
- Financial Markets is stronger on monetary/rates evidence than broader markets;
- Companies/Corporate Strategy still lacks a strong global dedicated reporting layer;
- independent AI/technology scrutiny remains incomplete;
- Startups/VC remains strongly Tech.eu-dependent;
- Milan/Bocconi remains only partially covered;
- Milan/Lombardy established-company intelligence remains incomplete;
- Europe/EU lacks a clean independent analytical production source;
- English-language sources dominate production by design;
- Italian-language production coverage remains selective;
- report descriptions are capped at 300 characters;
- some descriptions contain source-formatting artefacts that require later quality review if reproducible;
- near-duplicate same-story coverage is not clustered;
- article-level geography is not implemented;
- content type is not implemented;
- long-term source-health trends are not tracked;
- private Career Services opportunities are not automated;
- statistical structured data is not yet converted into intelligence events;
- GitHub scheduler latency can shift the daily window;
- high-quality global corporate reporting remains an explicit residual gap;
- some strategically valuable sources cannot be used because their licensing/persistence terms conflict with the public repository;
- some strategically valuable feeds cannot be used because publication timestamps are absent;
- some public RSS feeds expose excessive/full-content payloads unsuitable for current metadata persistence.

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

**Active sources:** twelve.

**Active strategic domains:** ten of ten.

**Financial Markets:** partially satisfied; dedicated monetary/rates evidence exists, broader markets coverage remains incomplete.

**Companies/Corporate Strategy:** materially improved through MIMIT and Lavoce.info, but global corporate-strategy coverage remains incomplete.

**Milan/Bocconi:** implemented through TEF but only partially satisfies the broader requirement.

**Italy:** viable first production implementation achieved.

**AI primary-source diversity:** achieved through OpenAI + Google DeepMind.

**Independent AI/technology reporting:** still incomplete.

**Startups/VC diversification:** incomplete.

**Europe independent interpretation:** incomplete.

**Richer report context:** validated requirement, intentionally deferred.

Current active product objective:

> **Use one more gap-driven source-research cycle to determine whether remaining information-function gaps still justify expansion, then explicitly compare the value of additional sources with the value of richer report context.**

Current next strategic action:

> **Update the canonical project documents, commission a fresh Career Agent source-research pass against the remaining information-function gaps, and return the results to Development for a new controlled audit batch.**

---

# Changelog

## 2026-08-18 — Twelve-Source / Ten-Domain Product Checkpoint

- Updated the current production state from eight to twelve active sources.
- Updated the implemented taxonomy from nine to ten active domains.
- Recorded Italy as a viable first production implementation rather than a pending macroarea.
- Recorded the current Italy architecture:
  - Istat;
  - MIMIT News;
  - Lavoce.info Imprese.
- Recorded Italian-language classification as production-validated through live-source testing and historical regression.
- Recorded Federal Reserve Board Monetary Policy as active Tier 1 US monetary-policy evidence.
- Changed Financial Markets from "no dedicated source" to "partially satisfied with dedicated monetary/rates coverage."
- Reframed Financial Markets maturity around broader capital markets, credit, corporate financing and market structure.
- Recorded MIMIT News and Lavoce.info Imprese as material improvements to Companies/Corporate Strategy.
- Reframed Companies/Corporate Strategy from a severe incidental-coverage gap to a materially improved but globally incomplete domain.
- Added Google DeepMind News as the second active frontier-lab primary AI source.
- Recorded the minimum AI-diversity criterion as achieved through OpenAI + Google DeepMind.
- Preserved independent AI/technology reporting as a stronger maturity objective.
- Recorded Bruegel as strategically valuable but unsuitable under the current feed/persistence architecture.
- Recorded Assolombarda as strategically valuable but incompatible with current publication-time and persistence requirements.
- Recorded Ars Technica as unsuitable under current persistence terms.
- Recorded Nasdaq as standby under current access/persistence constraints.
- Retired the completed Nasdaq-to-DeepMind audit queue.
- Replaced the old queue with a fresh gap-driven source-research requirement.
- Set the next research gaps as:
  - global Companies/Corporate Strategy;
  - broader Financial Markets;
  - independent AI/Technology reporting;
  - independent Europe/EU interpretation;
  - Startups/VC diversification;
  - Milan/Lombardy business and professional ecosystem.
- Preserved Italian Tech Alliance as an existing production-readiness candidate whose basic audit should not be repeated.
- Added an explicit requirement to evaluate the source-expansion/richer-context crossover after the next research batch.
- Preserved richer-report context as a validated but deferred product requirement.

## 2026-08-17 — Milan/Bocconi First Implementation and Source-Expansion Reframing

- Updated the current production state from seven to eight active sources.
- Updated the current taxonomy from eight to nine active domains.
- Added Tech Europe Foundation as the first production Milan/Bocconi source.
- Changed Milan/Bocconi from fully pending to partially satisfied.
- Clarified that TEF mainly covers startup, entrepreneurship, deep-tech and innovation ecosystem activity.
- Preserved recruiting, employer events, finance/consulting opportunities and complete deadline coverage as remaining Milan/Bocconi gaps.
- Clarified that complete private Career Services replication is not a product requirement.
- Preserved authenticated yoU@B and JobGate as manual/private layers.
- Recorded Italy as the remaining strategically approved but unimplemented dedicated macroarea at that checkpoint.
- Recorded Financial Markets as implemented but still lacking dedicated source coverage at that checkpoint.
- Recorded Companies/Corporate Strategy as a major remaining information gap.
- Recorded AI vendor concentration as an active product-quality issue.
- Incorporated the information-function-before-publisher-count expansion principle.
- Replaced the obsolete FT-first next-source sequence with the Nasdaq-to-DeepMind audit queue.
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