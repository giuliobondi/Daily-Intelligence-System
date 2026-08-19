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

- thirteen active public RSS sources;
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
- visible degraded/failure status;
- richer bounded source context in report entries.

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
12. Google DeepMind News;
13. ISPI Geoeconomics.

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

The main remaining limitation is no longer basic automation, missing domain implementation, an obviously incomplete source-discovery cycle, or the former 300-character report-context cap.

Current residual limitations are primarily:

- uneven information depth across some domains;
- thin or missing source-provided metadata for some publishers;
- malformed source metadata in isolated feeds;
- incomplete global Companies and Corporate Strategy coverage;
- broader Financial Markets coverage beyond monetary-policy evidence;
- independent AI and technology reporting;
- independent European economic-policy interpretation;
- Startups/VC diversification;
- Milan/Bocconi professional, recruiting and established-company coverage.

These gaps should remain visible.

The latest richer-report design and implementation cycle established that report context can be materially improved without adding article scraping, LLM summaries, new record fields or additional recurring cost.

The current product therefore uses bounded source-provided context in the report while preserving existing classification, ranking and storage semantics.

The latest controlled source-audit cycle also demonstrated that several high-value missing information roles remain constrained by:

- absence of suitable narrow public structured feeds;
- persistence restrictions;
- access-control barriers;
- publication-time limitations;
- event/deadline semantics;
- source-specific complexity that is not justified for the MVP.

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
- explicitly labelled source-provided context;
- run metadata.

Current report limits:

```text
maximum items per domain = 5
maximum total items      = 30
maximum source context   = 500 characters
```

These are upper bounds, not targets.

A sparse report is acceptable if few genuinely useful items exist.

The system should not fill space with low-value stories simply to reach a quota.

Source context should remain bounded and presentation-focused.

The report should not imply that source-provided context is AI-generated analysis or an independent editorial summary.

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

Future source expansion should be triggered by demonstrated information gaps in real report use rather than by a standing queue of unaudited publications.

---

# 10. Current Coverage Requirements

The target information universe contains ten strategic macroareas.

All ten now have implemented domains.

The product does not require equal source counts across all domains.

It does require enough useful coverage that major macroareas are not effectively defined by one weak or incidental source.

A domain being implemented does not mean that its source universe is complete or equally mature.

For the current MVP boundary:

> **all ten domains have sufficient baseline implementation or a justified public-source/architecture limit.**

This is not a claim of comprehensive coverage.

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
+ selective ISPI Geoeconomics contribution
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
ISPI Geoeconomics spillover
```

The system now has substantial primary monetary and macroeconomic evidence across:

- euro area;
- United States;
- Italy;
- European Union.

## Requirement Status

> **Well served for primary evidence; independent interpretation remains less complete.**

The previous US monetary-policy gap has been materially closed through the Federal Reserve Board Monetary Policy source.

ISPI Geoeconomics now adds some differentiated geoeconomic interpretation.

The remaining analytical gap is no longer an MVP blocker.

Future source work should occur only if real report use shows a meaningful deficiency that richer context or the existing source universe cannot address.

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

Dedicated upstream evidence exists through:

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

ESMA was audited as a potential source for:

- market structure;
- trading;
- settlement;
- market data;
- financial supervision.

Its information value was confirmed, but the current public RSS is not compatible enough with the existing production model because:

- standard publication timestamps are absent;
- dates are embedded inside HTML descriptions;
- descriptions are unusually long;
- classification becomes distorted by incidental keyword matches;
- activation would require multiple compensating processing changes.

## Requirement Status

> **Sufficient for the current MVP baseline, but broader markets coverage remains incomplete.**

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

Future source expansion should be reopened only when a materially cleaner source becomes available or real report use demonstrates that the current gap is costly.

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

Current meaningful coverage comes from:

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

DG Competition was audited as a potential high-value source for:

- M&A;
- antitrust;
- competition;
- Foreign Subsidies Regulation;
- strategic company developments.

The information function was strongly validated.

However, the only verified general RSS feed also contains substantial routine State-aid volume.

Under the current classification and ranking rules, many routine notices would compete too strongly with higher-value Europe/EU intelligence.

No clean narrow Mergers/Antitrust/FSR RSS route was found.

## Requirement Status

> **Sufficient for the current MVP baseline, but globally incomplete.**

The domain is no longer served only incidentally.

However, a strong global dedicated corporate-strategy/reporting role remains missing.

The product may retain this explicit residual gap if no legal, zero-cost, low-complexity substitute for high-quality corporate journalism emerges.

It should not fill that gap with inferior, noisy or technically fragile sources solely for completeness.

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
ISPI Geoeconomics
```

OpenAI and DeepMind provide meaningfully different frontier-lab primary evidence.

## Requirement Status

> **Primary-source diversity achieved; independent scrutiny remains incomplete.**

The minimum diversity structure:

```text
one strong primary source
+
one meaningfully different primary or independent source
```

is satisfied through:

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

but this is a maturity objective rather than an MVP blocker.

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
ISPI Geoeconomics spillover
```

## Requirement Status

> **Moderately served and sufficient for the current MVP baseline.**

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

Italian Tech Alliance has now undergone a deeper production-readiness probe.

Its feed is technically compatible and contains some strong material around:

- Italian VC statistics;
- training programmes;
- ecosystem initiatives;
- professional opportunities.

However, much of the tested feed consists of:

- very short press-clipping descriptions;
- repeated external-media references to the same underlying developments.

## Requirement Status

> **Sufficient for the current MVP baseline, but still concentrated.**

Italian Tech Alliance remains a deferred production-readiness candidate rather than an active source.

Its potential differentiated role remains:

```text
Tech.eu
→ European company/deal coverage

Tech Europe Foundation
→ selected startup / entrepreneurship / ecosystem activity

Italian Tech Alliance
→ Italian VC ecosystem, policy, statistics and programmes
```

The product should not activate Italian Tech Alliance merely to increase source count or publisher diversity.

The product should not add several additional startup publications that mostly duplicate funding rounds.

Future Startups/VC expansion should require evidence that concentration is degrading report usefulness.

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

Additional selective specialist and interpretative coverage comes from:

```text
Tech.eu
ISPI Geoeconomics
```

ISPI contributes differentiated geoeconomic interpretation around:

- economic security;
- trade;
- industrial policy;
- strategic dependencies;
- technology competition;
- supply chains;
- business implications of geopolitical change.

## Requirement Status

> **Strong primary evidence with partially improved independent interpretation.**

Independent analytical depth remains incomplete.

Bruegel was audited for this role and proved strategically strong but technically/persistence-incompatible under the current architecture.

ISPI now fills part of the independent interpretation gap without requiring new processing architecture.

The product should not continue adding European analytical sources unless real report use demonstrates material missing context that cannot be solved through the richer-report layer.

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

Italy has a dedicated production domain.

Current differentiated production architecture:

```text
Istat
→ primary statistics and macroeconomic evidence

MIMIT News
→ industrial policy, company restructuring,
  strategic investment and company-policy evidence

Lavoce.info Imprese
→ independent economic/business interpretation

ISPI Geoeconomics
→ selective geoeconomic and strategic interpretation
```

Italian-language deterministic classification has been validated through:

- live source records;
- narrow keyword additions;
- historical-regression checks;
- uppercase acronym handling;
- real production runs.

## Requirement Status

> **Viable first production implementation achieved; broader maturity remains incomplete.**

The requirement that Italy provide:

- meaningful coverage beyond Istat;
- at least one strong company/industrial or business role;
- useful economic interpretation or policy evidence;
- acceptable Italian-language classification;
- public/automation-compatible endpoints;
- manageable noise;
- no premium authenticated ingestion;

has been satisfied at a first production level.

Remaining maturity gaps include:

- Italian banking;
- broader capital markets;
- major-company reporting beyond industrial-policy events;
- Milan/Lombardy established-company intelligence;
- selected startup/VC ecosystem depth.

Italy should not be treated as an unsatisfied implementation requirement.

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

> **MVP-sufficient but deliberately incomplete.**

The automated implementation exists and has passed pipeline validation.

TEF alone does not provide comprehensive Milan/Bocconi professional intelligence.

Important remaining gaps include:

- finance recruiting;
- consulting recruiting;
- employer events;
- complete opportunity/deadline discovery;
- established-company ecosystem;
- industrial ecosystem;
- selected high-value public lectures.

However, controlled Phase 4 research has now tested several of the strongest obvious complementary information roles.

Stable findings include:

```text
Assolombarda
→ strategically strong established-company / industrial complement
→ current feeds fail timestamp and persistence requirements

Bocconi Career Services
→ extremely high professional/recruiting value
→ key actionable layer partly authenticated
→ no clean narrow public structured feed established

Italian Tech Alliance
→ technically compatible
→ useful Italian VC / programme signal
→ feed dominated by thin press-clipping
→ not a source-wide Milan/Bocconi sensor

Fintech District
→ strong Milan finance / fintech ecosystem value
→ no usable RSS/API established

Camera di Commercio Milano Monza Brianza Lodi
→ strong local-company / economic-ecosystem value
→ automated endpoint access blocked by Incapsula/Imperva responses
```

The remaining weakness therefore reflects a combination of:

- public structured-source availability;
- authenticated information boundaries;
- event/deadline semantics;
- current article-model limitations.

For the current MVP boundary, this constitutes a justified public-source/current-architecture limit.

---

# 22. Bocconi Career Services Boundary

Bocconi Career Services is extremely valuable to the user.

Public pages expose meaningful information around:

- Investment Banking Days;
- Bocconi&Jobs;
- sector-specific Recruiting Dates;
- employer participation;
- registration windows;
- selected professional events.

However, key information and registration infrastructure exists partly inside authenticated:

```text
yoU@B
JobGate
```

The product does **not** require the Daily Intelligence System to replicate these private systems.

The automated acceptance target is:

> **Surface the highest-value public structured professional ecosystem intelligence that can be collected safely, automatically and at zero recurring cost.**

The system must not:

- log into yoU@B automatically;
- scrape JobGate;
- embed Bocconi credentials;
- bypass authenticated access.

No sufficiently narrow public structured Career Services feed has currently been established.

Private Career Services therefore remains a complementary manual layer.

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

The latest source audits provide direct evidence that:

```text
publication date
≠
application deadline
≠
event date
```

Examples include:

- ISPI Business Events;
- Bocconi Career Services public event information.

A dedicated opportunity/deadline state model is **not currently required**.

Introduce one only if repeated real use demonstrates that publication-only treatment causes meaningful opportunities to be missed.

Do not introduce a second data model merely because strategically valuable event sources exist.

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

The source universe is sufficient for the current MVP boundary but is not permanently complete.

The active Phase 4 source-expansion cycle is closed.

Future source expansion should be driven by:

> **demonstrated information-function gaps in real product use**

rather than:

> **a standing queue of interesting publications.**

Known residual gaps remain:

```text
Global Companies / Corporate Strategy
Broader Financial Markets
Independent AI / Technology reporting
Independent Europe/EU interpretation
Milan / Bocconi recruiting and established-company coverage
Startups / VC diversification
```

These should remain visible.

They are not all mandatory blockers for richer-report work.

Future source research should reopen only when:

- repeated report use shows a costly information gap;
- a previously blocked high-value source exposes a cleaner structured endpoint;
- a persistence/licensing condition materially improves;
- a new user need becomes validated;
- source concentration demonstrably harms report quality.

The product does not require a fixed source count.

It requires enough differentiated coverage to support useful daily awareness.

---

# 28. Completed Strategic Source-Research Cycle

The previous source-audit queues and the subsequent gap-driven research cycle have now been completed for the current MVP boundary.

Important active additions from Phase 4 include:

```text
Federal Reserve Monetary Policy
MIMIT News
Lavoce.info Imprese
Google DeepMind News
ISPI Geoeconomics
```

Important stable deferred/standby decisions include:

```text
Nasdaq
Bruegel
Assolombarda
Ars Technica
ISPI Business Events
DG Competition
ESMA
Fintech District
Camera di Commercio Milano Monza Brianza Lodi
```

Italian Tech Alliance remains:

```text
deferred production-readiness candidate
```

Detailed source-policy rationale belongs in:

```text
03 Information Taxonomy and Source Policy.md
```

The Development project should no longer maintain a mandatory next-source audit queue.

Future source work is evidence-triggered.

---

# 29. Residual Information Roles

The product should preserve explicit awareness of the following unresolved information roles.

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

DG Competition validated the information value of this role but did not provide a clean enough production feed under the current classifier.

The gap may remain explicit until a better source or endpoint emerges.

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

ESMA validated the value of a broader market-structure source but not a sufficiently clean current production path.

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

A future source should therefore add independent interpretation rather than another lab blog.

This is currently a maturity gap rather than an MVP blocker.

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

ECB and European Commission supply primary evidence.

ISPI now adds differentiated geoeconomic interpretation.

Further independent depth remains desirable but is not a current Phase 4 blocker.

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

Italian Tech Alliance remains a potential later complement.

Do not add multiple sources that simply repeat funding rounds.

---

## Milan / Bocconi Professional and Business Ecosystem

Desired role:

```text
established firms
industry
professional events
recruiting
finance/business ecosystem
high-value opportunities
```

TEF already covers startup/innovation activity.

The latest research indicates that several remaining roles are constrained by:

- authenticated access;
- absent structured feeds;
- anti-bot/access-control systems;
- event/deadline semantics.

Future work should be triggered by actual missed-opportunity cost.

---

# 30. Richer Context Requirement

The report should provide enough lawful source-provided context to understand the core development without requiring immediate click-through when the source metadata permits it.

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

This is a validated and implemented product requirement.

The accepted report behaviour is:

```text
source-provided description
→ preserve unchanged when already within the display limit
→ otherwise prefer a complete sentence before the limit
→ otherwise fall back to a word boundary
→ never exceed the configured display limit
```

Current display limit:

```text
500 characters
```

The former 300-character limit was found not to be the main context constraint across most sources, but it unnecessarily truncated useful descriptions from several feeds.

The 500-character limit was selected because it captures materially more context from sources such as Tech Europe Foundation, Lavoce.info and ISPI while keeping report entries bounded.

Minimum Useful Context should allow the reader, where the source provides enough metadata, to identify:

- the core development;
- the relevant actor or object;
- at least one material qualifier such as scale, consequence, rationale, next step, constraint or strategic/economic significance.

This is a manual product-quality rubric rather than an automated scoring requirement.

---

# 31. Richer Context Constraints

Richer report context must preserve:

- zero recurring cost;
- copyright safety;
- source attribution;
- provenance;
- no premium article-body scraping;
- no production AI dependency;
- manageable total report length;
- deterministic behaviour;
- transparent fallback when metadata is thin.

The accepted production mechanism is deliberately narrow:

1. use the existing normalized source description;
2. label it explicitly as `Source context`;
3. render up to 500 characters;
4. prefer complete-sentence truncation;
5. otherwise truncate at a word boundary;
6. show an explicit fallback when the description is missing or duplicates the headline.

Current fallback text:

```text
No additional source-provided context available.
```

The richer-context design does **not** require:

- a new `context` field in the article model;
- generic use of RSS `content` fields;
- article-page scraping;
- first-paragraph extraction;
- LLM summarisation;
- source-specific text repair heuristics;
- changes to classification or ranking evidence.

Body-like feed `content` fields may contain materially richer text for some sources, but they are not part of the current production solution because they can:

- resemble article bodies rather than bounded metadata;
- create public-repository persistence concerns;
- distort deterministic classification/ranking if reused as evidence;
- introduce unnecessary source-specific complexity.

Malformed source-provided snippets should remain visible as source-quality limitations unless a clean structured alternative is validated.

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
- context quality;
- whether context ends cleanly;
- whether missing context is exposed transparently;
- whether richer context materially reduces unnecessary click-through;
- whether source-provided snippets remain readable and bounded.

Primary product question:

> **Would reading this report make the user meaningfully better informed?**

For richer-context evaluation, the product should also ask:

> **Can the reader understand the core development from the report entry alone when the source provides enough metadata?**

The system should not optimise only description length or item count.

A report may be technically correct but still fail product acceptance if it becomes noisy, repetitive, misleading or excessively long.

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

The DG Competition and ESMA audits reinforce that high classification rates or high relevance scores can themselves be undesirable when driven by incidental evidence.

---

# 37. Multilingual Classification Requirement

The system should support both English and Italian source material where strategically useful.

Current multilingual production evidence includes:

- MIMIT News;
- Lavoce.info Imprese;
- ISPI Geoeconomics;
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

A known concentration may be explicitly accepted when stronger alternatives are incompatible with zero-cost, public-safe, low-maintenance production.

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
→ sufficient MVP baseline;
  dedicated monetary/rates coverage exists;
  broader markets coverage remains incomplete

Companies / Corporate Strategy
→ sufficient MVP baseline;
  materially improved;
  strong global corporate-strategy role remains incomplete

Italy
→ achieved at viable first-production level

Milan / Bocconi
→ MVP-sufficient but deliberately incomplete;
  more than nominal coverage exists;
  public-source/current-architecture ceiling documented

AI primary-source diversity
→ achieved

Startups / VC
→ sufficient MVP baseline;
  concentration remains;
  Italian Tech Alliance deferred after deeper audit

source roles / persistence decisions
→ sufficiently documented for current Phase 4 closure
```

Therefore:

> **The Phase 4 information-universe acceptance threshold is met for the current MVP.**

This does not require:

- equal source counts;
- complete coverage;
- every researched source activated;
- a Reuters/FT replacement;
- perfect bilingual coverage;
- elimination of all residual information gaps.

---

# 45. Acceptance Criteria — Milan/Bocconi

The Milan/Bocconi requirement is considered:

> **MVP-sufficient but deliberately incomplete.**

Current minimum achieved:

- dedicated active domain;
- validated public structured source;
- automated integration;
- zero credentials;
- no private scraping;
- normal pipeline compatibility;
- useful startup/innovation ecosystem signal;
- targeted evaluation of major complementary public-source roles.

Still missing or incomplete:

- established-company ecosystem intelligence;
- Milan/Lombardy economic/business depth;
- finance/consulting recruiting;
- employer events;
- high-value professional opportunities;
- complete deadline discovery.

The current source audits demonstrate that several of these roles are limited by:

- authenticated Bocconi systems;
- unavailable public structured feeds;
- unsuitable event/publication-time semantics;
- public access-control barriers;
- source-quality or persistence constraints.

The product does not need to automate every private Bocconi opportunity.

If public structured sources cannot safely provide a role, the product may explicitly accept that limit rather than build fragile private-source automation or new architecture without evidence.

A dedicated event/deadline architecture should be reconsidered only if actual product use shows meaningful opportunity cost.

---

# 46. Acceptance Criteria — Italy

Italy has reached a **viable first production implementation**.

Current minimum achieved:

- dedicated active Italy domain;
- meaningful coverage beyond Istat;
- Tier 1 Italian industrial/company-policy evidence through MIMIT;
- independent business/company interpretation through Lavoce.info Imprese;
- additional selective geoeconomic interpretation through ISPI;
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

Financial Markets should not be considered complete merely because the domain exists.

The current system has achieved a meaningful first dedicated layer through Federal Reserve Monetary Policy.

Current status:

> **Sufficient for the MVP baseline, but not mature.**

Broader maturity would include recurring coverage of a stronger combination of:

- rates;
- yields;
- credit;
- financial conditions;
- capital markets;
- IPOs;
- corporate financing;
- market structure;
- material equity-market developments.

ESMA validated the value of some of these missing roles but did not justify production integration under the current architecture.

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

This minimum is achieved through:

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

The product sequence is now:

```text
Phase 4
source/domain correction and expansion
→ current MVP acceptance threshold reached

→

Phase 5
richer-report product design
→ complete

→

Phase 6
richer-report implementation and evaluation
→ implemented and locally validated
```

Phase 4 does not imply perfect information coverage.

It reached its stopping condition because:

- all ten domains are implemented;
- the major first-order gaps were investigated;
- several differentiated sources were added;
- several attractive sources were deliberately rejected or deferred;
- Milan/Bocconi now has both meaningful automated coverage and a demonstrated public-source/current-architecture ceiling;
- additional source work increasingly requires disproportionate complexity;
- richer report context had become a higher-value improvement than another speculative source addition.

Phase 5 is complete because the richer-context design question was resolved through a source-metadata audit and explicit comparison of simpler and more complex options.

The selected design uses:

```text
existing normalized source description
+ explicit Source context provenance
+ 500-character display bound
+ sentence-aware truncation
+ word-boundary fallback
+ explicit no-context fallback
```

Phase 6 is implemented and locally validated because:

- report-specific tests pass;
- the full deterministic test suite passes;
- a production-equivalent run completed successfully across all thirteen active sources;
- generated report output was manually inspected;
- classification/ranking/storage semantics were not expanded;
- no paid, AI-dependent or scraping-based mechanism was introduced.

Future source expansion remains allowed.

It should be reopened when real report use demonstrates a meaningful information gap with higher expected value than further report-quality refinement.

The next product question should therefore come from observed use rather than an assumed feature roadmap.

---

# 50. Acceptance Criteria — Richer Report Context

The richer-report requirement is accepted when:

- source-provided context is explicitly labelled;
- short descriptions are preserved unchanged;
- longer descriptions remain bounded at 500 characters;
- truncation prefers a complete sentence when practical;
- word-boundary truncation prevents mid-word cuts;
- missing descriptions produce a transparent fallback;
- title-duplicate descriptions are not repeated as context;
- report item caps remain unchanged;
- no article-body scraping is introduced;
- no generic RSS body-content ingestion is introduced;
- no production LLM summarisation is introduced;
- no additional recurring monetary cost is introduced;
- classification and ranking continue to use the existing article evidence model;
- generated output remains readable and bounded in real production-equivalent runs.

Current status:

> **The richer-report acceptance threshold is met for the current MVP implementation.**

Known limitations remain source-dependent.

Some feeds provide:

- no description;
- very short descriptions;
- descriptions that duplicate the headline;
- malformed publisher-provided spacing or truncation.

The product should expose those limitations transparently rather than fabricate context or introduce speculative text-repair heuristics.

Future enrichment mechanisms should be reconsidered only if real use demonstrates that these source-level limitations create material decision or awareness costs.