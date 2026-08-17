# Daily Intelligence System — Product Requirements

> **Purpose**
>
> This document defines what the Daily Intelligence System must do from the user’s perspective.
>
> It translates the Project Brief into functional requirements, non-functional requirements, user workflows, output requirements and acceptance criteria.
>
> It defines required behaviour without prescribing unnecessary implementation details.
>
> ---
>
> **Primary Question**
>
> > *What must the system do, and how will we know that it is useful and working correctly?*
>
> ---
>
> **Update Frequency**
>
> Update when product behaviour, user workflow, MVP scope or acceptance criteria materially change.

---

# Product Objective

The Daily Intelligence System should automatically collect, organise, rank, archive and present relevant information so that the user can maintain broad, selective awareness without manually scanning many sources.

The product should reduce:

- source fragmentation;
- duplicated stories;
- low-value content;
- manual research time;
- dependence on engagement-optimised algorithms;
- unnecessary click-through before understanding a development;
- inaccessible or low-value follow-up links;
- source concentration;
- missed high-value developments;
- loss of historical information.

The system should increase:

- source transparency;
- information quality;
- domain coverage;
- reading efficiency;
- consistency;
- historical memory;
- accessibility of important developments;
- awareness of important developments;
- confidence that technically successful runs also produce useful reports;
- awareness of professionally relevant Bocconi and Milan opportunities.

The product should optimise for:

```text
signal
> volume
```

and:

```text
usefulness
> prestige
> comprehensiveness
```

The GitHub system is primarily an information collection, organisation and reporting product.

It is not intended to become a general AI assistant.

Interpretation, strategic discussion and deeper synthesis may still be handled separately through ChatGPT.

The production pipeline should remain deterministic unless later evidence justifies a different approach.

---

# Product Status

The deterministic processing core, real-source layer and GitHub production automation are implemented and validated.

The system can currently:

- load repository configuration;
- collect real public RSS feeds;
- collect controlled local feed fixtures;
- use bounded remote HTTP requests;
- send an explicit User-Agent where required;
- preserve normal SSL verification;
- isolate source-level failures;
- distinguish successful, empty and failed sources;
- normalise real feed entries;
- validate required fields;
- enforce a publication-time collection window;
- reduce exact duplicates;
- classify records deterministically;
- support explicitly unclassified records;
- assign deterministic relevance scores;
- persist processed JSON Lines;
- generate a bounded Markdown report;
- generate a structured JSON run summary;
- expose degraded-run warnings;
- emit run-level logs;
- run locally from one command;
- run manually through GitHub Actions;
- run automatically through GitHub Actions scheduling;
- validate generated outputs before persistence;
- persist production outputs automatically;
- avoid empty commits when outputs do not change;
- distinguish critical failures from degraded runs;
- preserve usable output when one source fails;
- archive dated production history in the repository.

The validated local command remains:

```text
python -m daily_intelligence.cli run
```

The current active production configuration contains seven public RSS sources:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News;
- Istat Press Releases;
- OpenAI News;
- Tech.eu.

Sifted is no longer an active production source.

It was replaced by Tech.eu after controlled source-quality testing showed materially better public metadata and follow-up usability.

The implemented taxonomy currently contains eight active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Financial Markets;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

The remaining target macroareas are:

- Italy;
- Milan and the Bocconi ecosystem.

Their current product status differs:

```text
Italy
→ strategically approved
→ implementation pending source/classification validation

Milan and Bocconi ecosystem
→ validated product requirement
→ implementation pending source/architecture validation
```

The automated test suite currently contains:

> **110 passing tests.**

A real 17 August 2026 local validation run completed successfully with:

```text
7 active sources
7 successful sources
30 unique processed records
4 displayed items
status: success
```

The report and all 30 processed records were manually inspected.

The current scheduled production time remains:

```text
06:05 Europe/Rome
```

Scheduled execution is validated, but GitHub scheduler latency remains an observed limitation.

The active product-development priority is:

> **Continue correcting and expanding the source/domain universe, then design the richer report-context requirement deliberately.**

The next source-level technical audit is Financial Times.

---

# Primary User

The initial product is designed for one user.

The user wants structured daily awareness across ten target macroareas:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Financial Markets;
4. Companies and Corporate Strategy;
5. Artificial Intelligence;
6. Technology and Software;
7. Startups and Venture Capital;
8. Europe and the European Union;
9. Italy;
10. Milan and the Bocconi ecosystem.

The user has limited time for daily research and wants negligible recurring manual work.

The information product should particularly support:

- economic understanding;
- finance and markets awareness;
- company and industry understanding;
- AI and technology literacy;
- startup and VC pattern recognition;
- European and Italian awareness;
- high-quality professional conversations;
- opportunity awareness in the Milan/Bocconi ecosystem.

The user has legitimate institutional access through Bocconi to many high-quality publications and research resources.

That access can improve manual follow-up.

It does not create automated-ingestion permission.

The user is willing to perform:

- initial setup;
- occasional source review;
- periodic quality evaluation;
- limited maintenance when sources or platform behaviour change;
- deliberate source/domain redesign when production evidence exposes weaknesses.

The user should not need to:

- search each source manually;
- copy content between systems every day;
- start production manually under normal conditions;
- review raw logs unless a failure occurs;
- make daily classification or ranking decisions;
- open every article merely to understand the basic development.

---

# Core User Jobs

The product should help the user complete seven main jobs.

## Job 1 — Discover Important Developments

Identify relevant items published by monitored sources during the configured time window.

## Job 2 — Reduce Noise

Suppress malformed, duplicate, irrelevant and low-value records.

The product should prefer fewer useful items over filling the report artificially.

## Job 3 — Organise Information

Group stories into meaningful configurable domains.

The system should prefer leaving an item unclassified over assigning a misleading domain.

## Job 4 — Prioritise Attention

Rank items using transparent deterministic criteria.

## Job 5 — Understand the Development

Provide enough lawful context that the user can understand the key development before deciding whether deeper reading is worthwhile.

## Job 6 — Preserve Information

Store structured article records and historical reports for later review.

## Job 7 — Detect High-Value Professional Opportunities

Surface unusually relevant Milan/Bocconi events, programmes, deadlines and ecosystem developments when suitable public structured sources are available.

The Daily Intelligence System should act as the external information sensor.

Personal decisions, application tracking, networking follow-up and relationship management remain outside this product and belong in the Career OS.

---

# Primary User Workflow

Under normal production operation, the daily workflow should be:

1. The system runs automatically.
2. It collects new items from configured automated sources.
3. It processes and validates the collected metadata.
4. It selects items inside the configured publication window.
5. It reduces exact duplicates.
6. It classifies and ranks eligible records.
7. It generates the daily report.
8. It stores the report, processed records and run summary.
9. It makes success, degradation or failure visible.
10. The user opens the latest report.
11. The user understands the core development of selected items where lawful source information is sufficient.
12. The user follows only links that justify deeper reading.
13. Premium Bocconi-accessible sources may be opened manually where a deliberately approved source provides thinner automated context.
14. Actionable Milan/Bocconi items may then be transferred conceptually into the Career OS when the user decides to act.

Normal daily use should require:

- no configuration;
- no data entry;
- no manual workflow execution;
- no copying between systems.

The intended reading model is:

```text
daily report
→ understand important developments
→ identify high-value opportunities
→ decide what deserves deeper reading or action
→ open selected source links
```

not:

```text
daily report
→ scan headlines
→ open almost every article
→ understand what happened only after click-through
```

---

# Functional Requirements

Requirements are classified as:

- **MUST** — required for the accepted production product;
- **SHOULD** — important but may follow the current stable production loop;
- **COULD** — optional future enhancement;
- **WILL NOT** — explicitly outside the current product scope.

---

# 1. Source Configuration

## FR-1.1 — Configurable Source Registry

**Priority:** MUST

The system must use a manually maintained source registry.

Each source entry should support, where relevant:

- unique source identifier;
- source name;
- feed or endpoint URL;
- source type;
- source tier;
- default domain or domains;
- language;
- geographic scope;
- active or inactive status.

A source may explicitly have no default domain when the selected feed is too broad for a source-wide topical assumption.

### Acceptance Criteria

- A new compatible source can be added through configuration without modifying core collection logic.
- A source can be disabled or replaced without redesigning the pipeline.
- Invalid required source configuration produces a visible error.
- Source configuration remains separate from collection logic.
- Broad sources can rely entirely on article-level classification.
- Source defaults are used only when essentially every record in the selected feed genuinely supports that domain.

### Current Status

**Implemented and production-validated**

Current active source defaults:

```text
BBC News World                → none
BBC News Business             → none
European Central Bank         → none
European Commission           → none
Istat Press Releases          → Economics and Macroeconomics
OpenAI News                   → Artificial Intelligence
Tech.eu                       → none
```

Tech.eu deliberately receives no Startups/VC default because its general feed also covers AI, technology, corporate strategy and European policy.

---

## FR-1.2 — Public Structured Sources

**Priority:** MUST

The automated production system must collect only from permitted public structured sources or other explicitly approved automation-compatible endpoints.

Examples include:

- RSS;
- Atom;
- official public APIs;
- public structured metadata;
- other endpoints whose terms and licence permit the required use.

### Acceptance Criteria

- Production does not require private user credentials for normal collection.
- Production does not depend on authenticated browser automation.
- Production does not depend on prohibited scraping.
- The origin of every record is identifiable.
- Stored metadata is safe for the public repository.
- Bocconi credentials are never embedded in the production system.
- Institutional reading access is not treated as automated-ingestion permission.
- Premium article bodies are not fetched merely because the user can read them manually.

### Current Status

**Implemented and production-validated for current RSS sources**

Current production requires:

- no paid API;
- no private credentials;
- no browser automation;
- no authenticated publisher scraping.

---

## FR-1.3 — Partial Source Failure

**Priority:** MUST

A failure affecting one source should not automatically prevent successful sources from being processed.

### Acceptance Criteria

- The workflow records which source failed.
- Successful source results remain available.
- The report and run summary indicate incomplete coverage.
- Source failure is not silently ignored.
- Final status becomes degraded rather than falsely successful where appropriate.

### Current Status

**Implemented and production-validated**

---

## FR-1.4 — Source Accessibility and Follow-Up Value

**Priority:** MUST

A production source must be evaluated both for technical collectability and for whether its selected items remain useful to the user.

A source may be technically valid but still be a poor product source when:

- selected links are frequently inaccessible;
- feed metadata is too thin;
- a user cannot perform useful follow-up;
- the source adds little unique value;
- a comparable source provides materially better metadata or access;
- the source disproportionately dominates scarce report space.

### Acceptance Criteria

For each source, the source policy or audit should establish:

- automation suitability;
- public metadata richness;
- publication timestamp quality;
- reader accessibility;
- institutional-access status where relevant;
- unique information value;
- overlap;
- noise;
- maintenance;
- public-repository compatibility.

A weak source may be replaced instead of receiving source-specific complexity.

### Current Status

**Implemented as an active source-selection requirement**

The first completed source-quality decision was:

```text
Sifted
→ replaced by Tech.eu
```

The direct controlled comparison found:

```text
Tech.eu: 20/20 tested items with descriptions
Sifted:  0/24 tested items with descriptions
```

Sifted also had unresolved Sifted Pro follow-up friction.

---

## FR-1.5 — Premium Bocconi Source Exception

**Priority:** SHOULD

A small number of unusually valuable premium publications may be approved for production discovery even when the automated pipeline cannot retrieve sufficient article content to create the same rich context available from a fully public source.

This exception is allowed only when:

- the user can legitimately access the article through Bocconi;
- the publication has unusually high strategic value;
- a legitimate public or automation-compatible discovery endpoint exists;
- production does not authenticate as the user;
- premium article bodies are not automatically retrieved;
- a thinner report entry and deliberate manual click-through remain useful.

### Acceptance Criteria

- Exception is approved source by source.
- Premium status alone is not enough.
- Prestige alone is not enough.
- A comparable accessible source is preferred where value is similar.
- Bocconi/OpenAthens credentials never enter production.
- The report does not imply that premium content was automatically read or summarized.

### Current Status

**Validated product rule — no premium exception source yet active**

Highest-priority candidates for technical audit:

- Financial Times;
- Il Sole 24 Ore.

---

# 2. Collection

## FR-2.1 — Scheduled Collection

**Priority:** MUST

The system must support automatic daily execution.

### Acceptance Criteria

- Production runs without daily manual initiation.
- Schedule is version-controlled.
- Manual execution remains available for testing/recovery.
- Scheduled execution has been observed successfully.

### Current Status

**Implemented and production-validated**

Current schedule:

```text
06:05 Europe/Rome
```

---

## FR-2.2 — Configurable Collection Window

**Priority:** MUST

The system must use an explicit publication window.

Current production behaviour:

```text
actual run time - 24 hours
→ actual run time
```

### Acceptance Criteria

- Window is visible in the report.
- Items outside the window are excluded.
- Comparisons use timezone-aware datetimes.
- Boundaries behave deterministically.
- Missing publication timestamps are handled explicitly.

### Current Status

**Implemented and production-validated**

### Open Product Question

GitHub scheduler delay shifts the current reporting window.

A fixed daily reporting cutoff remains a candidate future improvement.

Do not change it without further production evidence.

---

## FR-2.3 — Metadata Retrieval

**Priority:** MUST

The system must collect the source metadata required for later processing.

Current required/desired fields include, where available:

- title;
- article URL;
- source;
- publication timestamp;
- feed description or summary;
- retrieval timestamp.

Potential future richer-context inputs may include:

- author;
- categories/tags;
- structured summary fields;
- public content metadata;
- canonical URL;
- richer feed content.

### Acceptance Criteria

- Original source identity is preserved.
- Missing optional metadata does not necessarily invalidate the record.
- Missing required metadata is handled explicitly.
- Retrieval timestamps are recorded.
- Source-provided information remains distinguishable from derived metadata.

### Current Status

**Implemented for the current metadata model**

Production evidence has established that missing descriptions are technically acceptable but may still make a source unsuitable for the product.

---

## FR-2.4 — Bounded Remote Collection

**Priority:** MUST

Remote collection must not wait indefinitely or weaken normal transport security.

### Acceptance Criteria

- Explicit bounded timeout.
- Identifiable User-Agent where appropriate.
- Network failures become visible source failures.
- Standard SSL verification remains enabled.
- One failed source does not terminate unrelated successful sources.
- No paid HTTP service is required.

### Current Status

**Implemented and production-validated**

Current timeout:

```text
10 seconds
```

No retry logic is implemented.

---

# 3. Normalisation and Validation

## FR-3.1 — Standard Record Format

**Priority:** MUST

Collected items must become a consistent internal record before downstream processing.

The record should preserve:

- source identity;
- original title;
- normalised title;
- original URL;
- normalised URL;
- publication timestamp;
- retrieval timestamp;
- optional description;
- derived domains;
- matched keywords;
- relevance score;
- score components;
- deterministic record ID.

### Current Status

**Implemented and production-validated**

---

## FR-3.2 — Timestamp Normalisation

**Priority:** MUST

Publication and retrieval times must be represented consistently.

### Acceptance Criteria

- timezone-aware datetimes;
- UTC-compatible comparison;
- explicit missing/invalid handling;
- no silent incorrect window inclusion.

### Current Status

**Implemented and production-validated**

---

## FR-3.3 — URL Normalisation

**Priority:** MUST

The system must normalise URLs where practical while preserving usable originals.

### Current Status

**Implemented and tested**

---

## FR-3.4 — Invalid Record Handling

**Priority:** MUST

Malformed or incomplete records must not corrupt the whole run.

### Current Status

**Implemented at the validation layer**

No broader per-entry normalization isolation is justified yet.

---

# 4. Duplicate Reduction

## FR-4.1 — Exact Duplicate Detection

**Priority:** MUST

The system must reduce obvious duplicates using deterministic URL and title evidence.

### Current Status

**Implemented and production-exercised**

Current precedence:

1. normalised URL;
2. normalised title.

---

## FR-4.2 — Similar Story Detection

**Priority:** SHOULD

Near-duplicate handling may be introduced only if repeated real reports show that exact deduplication is insufficient.

### Current Status

**Deferred pending evidence**

---

## FR-4.3 — Multi-Source Coverage

**Priority:** SHOULD

The system may later preserve explicit multi-source story coverage when that creates material value.

### Current Status

**Deferred pending evidence**

---

# 5. Domain Classification

## FR-5.1 — Configurable Domain Taxonomy

**Priority:** MUST

The system must classify items using a configurable domain taxonomy.

### Acceptance Criteria

- Domains remain outside core application logic.
- Domains can be changed through configuration.
- Disabled domains do not participate in selection.
- Taxonomy can expand without redesigning the pipeline.
- Target scope may be broader than current implementation.

### Current Status

**Implemented and production-validated**

Current active domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Financial Markets;
4. Companies and Corporate Strategy;
5. Artificial Intelligence;
6. Technology and Software;
7. Startups and Venture Capital;
8. Europe and the European Union.

Still pending:

- Italy;
- Milan and the Bocconi ecosystem.

---

## FR-5.2 — Deterministic Classification

**Priority:** MUST

Production classification must remain transparent and deterministic unless real evidence later justifies another method.

Current evidence may include:

- source defaults;
- configured keywords;
- title;
- description.

### Acceptance Criteria

- Assignment can be explained.
- No LLM is required.
- Rules change through configuration.
- Source-wide defaults are not used when they misclassify broad feeds.
- Keyword additions are tested against real records.
- Closely related synonyms are not added carelessly when they create scoring inflation.

### Current Status

**Implemented and actively refined from production evidence**

Current evidence-backed Phase 4 refinements include:

```text
Global Politics and Geopolitics
+ tariffs

Companies and Corporate Strategy
+ acquired

Startups and Venture Capital
+ early-stage fund
+ funding market
- startup
```

The generic `startup` keyword was removed after it caused a low-value Tech.eu profile to receive an unjustified domain assignment and score uplift.

---

## FR-5.3 — Multiple Domains

**Priority:** SHOULD

An item may belong to multiple domains.

### Current Status

**Implemented and tested**

---

## FR-5.4 — Unclassified Items

**Priority:** MUST

Records matching no domain must remain valid and reviewable.

### Acceptance Criteria

- Unclassified items do not cause failure.
- They remain in processed storage.
- They can be inspected during quality review.
- Main-report inclusion behaviour is explicit.
- A high unclassified share is not automatically treated as a defect.

### Current Status

**Implemented and production-validated**

Current policy:

```text
unclassified
→ preserve in processed data
→ omit from main report
```

A real 17 August 2026 run produced:

```text
30 unique records
26 unclassified
4 displayed
```

Manual review showed that most unclassified records were correctly excluded as low-value or outside the intended scope.

Therefore:

> classification percentage is not a product-quality KPI.

The relevant question is whether important stories are being missed.

---

## FR-5.5 — Financial Markets Coverage

**Priority:** MUST

The Financial Markets domain should capture market developments that improve understanding of capital allocation, macro-financial transmission and financial-system conditions.

### Include

- stock-market corrections or major repricing;
- bond markets;
- bond yields;
- yield curve;
- credit spreads;
- capital markets;
- financial stability;
- foreign exchange when meaningful;
- asset management;
- meaningful IPO conditions;
- major market reactions connected to macro/company developments.

### Exclude or Deprioritise

- ordinary daily price recaps;
- isolated minor moves;
- technical analysis;
- stock tips;
- speculative predictions;
- low-context “markets up/down” content.

### Current Status

**Implemented — conservative initial version**

Initial keyword set remains intentionally narrow.

Broad words such as:

```text
market
stocks
shares
bonds
rates
bank
investment
```

must not be added without controlled evidence.

---

## FR-5.6 — Italy Macroarea

**Priority:** MUST

The final product should contain a dedicated Italy macroarea focused on economically and professionally relevant developments.

### Include

- Italian macro;
- banks;
- major companies;
- capital markets;
- industrial policy;
- economically material regulation;
- technology;
- startup/VC;
- infrastructure;
- labour-market developments.

### Exclude

- generic national news;
- sport;
- celebrity;
- routine crime;
- political theatre without material economic or professional relevance.

### Current Status

**Validated strategic requirement — implementation pending**

Current relevant source:

- Istat.

Highest-priority candidates:

- Il Sole 24 Ore;
- Bank of Italy.

---

## FR-5.7 — Milan and Bocconi Professional Ecosystem Macroarea

**Priority:** MUST

The final product must include a Milan/Bocconi macroarea.

This is a validated product requirement.

Its purpose is not generic local news.

It should function as:

> **Professional Ecosystem Intelligence**

### Include

Where structured public sources permit:

- Bocconi recruiting events;
- employer events;
- finance, consulting, AI/data and startup events;
- B4i programmes;
- startup calls;
- competitions;
- research opportunities;
- selected high-value public lectures;
- relevant application deadlines;
- Milan startup and VC developments;
- fintech/innovation ecosystem activity;
- important local business or innovation initiatives.

### Exclude or Deprioritise

- routine university administration;
- generic campus notices;
- tourism;
- nightlife;
- generic cultural events;
- low-value networking;
- events clearly irrelevant to the user;
- generic local crime/news.

### Product Boundary

The Daily Intelligence System should surface the external fact.

The Career OS should own:

- decision to attend/apply;
- application tracking;
- networking follow-up;
- contact management;
- reflection and career strategy.

### Current Status

**Validated product requirement — source architecture pending**

First sources to investigate later in Phase 4:

1. B4i;
2. Bocconi Career Services;
3. Bocconi News & Events.

No authenticated Bocconi scraping, email ingestion or daily manual copying should be introduced.

---

# 6. Relevance Ranking

## FR-6.1 — Transparent Relevance Score

**Priority:** MUST

The system must calculate a deterministic relevance score.

Current formula:

```text
source-tier score
+ 2 × domain matches
+ 1 × keyword matches
```

Current source-tier scores:

```text
Tier 1 → 4
Tier 2 → 3
Tier 3 → 2
Tier 4 → 1
```

### Acceptance Criteria

- score contributions documented;
- weights configurable;
- stable results from equivalent input/configuration;
- components inspectable;
- no paid model required.

### Current Status

**Implemented and production-exercised**

The formula remains provisional.

Upstream source/default/classification evidence should be corrected before increasing ranking complexity.

---

## FR-6.2 — Stable Ordering

**Priority:** MUST

Items must be ordered deterministically.

### Current Status

**Implemented and tested**

---

## FR-6.3 — Report-Length Control

**Priority:** MUST

Reports must remain bounded.

Current maximums:

```text
5 items per domain
30 items overall
```

These are maximums, not minimum targets.

A short report may be correct when few important stories exist.

### Current Status

**Implemented**

---

## FR-6.4 — Report Coverage and Concentration Quality

**Priority:** SHOULD

The report should not become unhelpfully sparse, repetitive or dominated by a single source when broader meaningful information is available.

No fixed quotas are required.

### Acceptance Criteria

Quality review should consider:

- displayed-item count;
- source concentration;
- domain concentration;
- meaningful missed records;
- low-value selected records;
- unexpectedly empty strategic domains.

### Current Status

**Validated ongoing quality requirement**

The earlier Sifted concentration problem was resolved through source replacement rather than ranking penalties.

Do not introduce concentration quotas without repeated evidence.

---

# 7. Structured Storage

## FR-7.1 — Processed Record Persistence

**Priority:** MUST

Processed records must be retained for inspection and historical use.

### Current Status

**Implemented and production-persisted**

Format:

```text
JSON Lines
```

---

## FR-7.2 — Historical Daily Reports

**Priority:** MUST

Dated daily reports must be retained.

Current path:

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

### Current Status

**Implemented and production-validated**

---

## FR-7.3 — Reproducibility

**Priority:** SHOULD

Generated reports should be reproducible from processed records and configuration where practical.

### Current Status

**Implemented for the current deterministic model**

---

# 8. Daily Report

## FR-8.1 — Markdown Output

**Priority:** MUST

The system must generate a readable Markdown report.

### Current Status

**Implemented and production-validated**

---

## FR-8.2 — Report Header

**Priority:** MUST

The report header must show:

- report date;
- monitored time window;
- generation timestamp;
- run status;
- active-source count;
- successful-source count;
- empty-source count;
- failed-source count;
- collected-item count;
- displayed-item count.

### Current Status

**Implemented**

---

## FR-8.3 — Domain Sections

**Priority:** MUST

Selected stories must be grouped into relevant domain sections.

### Current Status

**Implemented**

Current policy:

- first eligible assigned domain = primary placement;
- secondary domains = metadata;
- each story appears once.

---

## FR-8.4 — Story Entry

**Priority:** MUST

Each story should include, where available:

- headline;
- source;
- publication timestamp;
- relevance score;
- direct article link;
- secondary domains;
- permitted source-provided context.

Current maximum feed-description length:

```text
300 characters
```

### Current Status

**Implemented, but current context depth is insufficient for the target product**

FR-8.6 defines the stronger requirement.

---

## FR-8.5 — Failure Notice

**Priority:** MUST

Incomplete or degraded runs must be visibly marked.

### Current Status

**Implemented and production-validated**

---

## FR-8.6 — Sufficient Context Without Immediate Click-Through

**Priority:** MUST

Each selected story should provide enough lawful context for initial understanding whenever source information permits.

The original article should be primarily for deeper reading, not basic comprehension.

### Acceptance Criteria

A satisfactory item should allow the user to understand:

- what happened;
- who/what is involved;
- essential context;
- basic significance;
- why the story was selected.

The implementation must preserve:

- attribution;
- source link;
- copyright safety;
- no paywall bypass;
- no authenticated premium scraping;
- no fabricated context;
- zero recurring API cost;
- manageable report length.

### Premium Exception

For a deliberately approved Premium Bocconi Exception source, the report may provide thinner context if:

- the article itself is legitimately accessible to the user through Bocconi;
- the source's information value justifies click-through;
- production did not access the premium article body.

### Current Status

**Validated requirement — architecture/design pending**

Implementation remains deferred until the source/domain universe is sufficiently mature.

---

## FR-8.7 — Inaccessible-Link Resilience

**Priority:** SHOULD

A selected item should remain useful even if follow-up access is restricted.

Normally this means either:

- enough lawful public context exists; or
- the source should be reconsidered.

The Premium Bocconi Exception creates a narrow third case:

- article is premium;
- user has legitimate direct Bocconi access;
- source is sufficiently valuable to justify the click-through.

### Current Status

**Validated and incorporated into source policy**

Sifted failed this trade-off and was replaced.

---

## FR-8.8 — Honest Context Availability

**Priority:** MUST

The report must not imply that the system has read or summarized content that was not available to the automated pipeline.

### Acceptance Criteria

- Missing description/context is not fabricated.
- Premium article bodies are not implicitly represented as automatically understood.
- Derived commentary is distinguishable from source-provided text if introduced later.
- Source limitations remain transparent.

### Current Status

**Required for future richer-report implementation**

---

# 9. Automation and Delivery

## FR-9.1 — GitHub Actions Execution

**Priority:** MUST

Production must run through GitHub Actions or another explicitly approved zero-cost repository-native mechanism.

### Current Status

**Implemented and production-validated**

---

## FR-9.2 — Automated Persistence

**Priority:** MUST

Legitimate successful/degraded outputs must be persisted automatically.

### Current Status

**Implemented and production-validated**

---

## FR-9.3 — Failure Visibility

**Priority:** MUST

Failed and degraded runs must be visibly distinguishable.

### Current Status

**Implemented and production-validated**

---

## FR-9.4 — Daily GitHub Issue

**Priority:** COULD

Optional future delivery mechanism if repository Markdown becomes insufficient.

### Current Status

**Deferred**

---

## FR-9.5 — GitHub Pages

**Priority:** COULD

Optional future presentation layer if actual reading friction justifies it.

### Current Status

**Deferred**

---

## FR-9.6 — Scheduling Latency Tolerance

**Priority:** SHOULD

The product must remain understandable when GitHub starts a scheduled run later than configured.

### Current Status

**Partially satisfied**

The visible monitored window prevents false assumptions.

A fixed reporting cutoff remains an open decision.

---

# 10. Source Health and Quality

## FR-10.1 — Source Success Tracking

**Priority:** MUST

Each source must produce an inspectable status.

Current statuses:

```text
success
empty
failed
```

### Current Status

**Implemented**

---

## FR-10.2 — Empty Feed Handling

**Priority:** MUST

A valid empty feed must not be treated as technical failure.

### Current Status

**Implemented and tested**

---

## FR-10.3 — Source Maintenance

**Priority:** SHOULD

Sources should be periodically reviewed for:

- availability;
- metadata richness;
- accessibility;
- information value;
- overlap;
- concentration;
- noise;
- format changes;
- maintenance burden.

### Acceptance Criteria

- Weak sources can be disabled or replaced through configuration.
- Source-specific complexity remains proportional to source value.
- Replacement is preferred over unnecessary parser complexity.
- Current source decisions can be revised from repeated report evidence.

### Current Status

**Active Phase 4 requirement**

Completed example:

```text
Sifted
→ replace with Tech.eu
```

---

## FR-10.4 — Automated-Source Eligibility

**Priority:** MUST

A candidate must pass explicit source-quality review before production inclusion.

### Acceptance Criteria

Evaluate:

- strategic usefulness;
- public structured access;
- automation permission;
- credentials required;
- timestamps;
- metadata richness;
- reader accessibility;
- Bocconi-access mode where relevant;
- overlap;
- noise;
- maintenance;
- repository safety;
- report contribution.

### Current Status

**Active Phase 4 requirement**

Next candidate:

```text
Financial Times
```

---

# 11. Professional Ecosystem Opportunity Quality

## FR-11.1 — Actionability Threshold

**Priority:** MUST

Milan/Bocconi items should enter the report only when they have meaningful learning, networking, recruiting, research, startup or professional value.

The macroarea must not become a generic events calendar.

### Acceptance Criteria

A selected item should normally create one or more plausible actions such as:

- attend;
- apply;
- research;
- contact;
- monitor;
- discuss;
- investigate.

### Current Status

**Validated requirement — implementation pending**

---

## FR-11.2 — Eligibility Awareness

**Priority:** SHOULD

Where public metadata makes eligibility clear, the product should avoid prioritising opportunities the user clearly cannot access.

Do not introduce a complex eligibility engine without evidence.

### Current Status

**Future requirement for Milan/Bocconi implementation**

---

## FR-11.3 — Time-Sensitive Opportunity Awareness

**Priority:** MUST

The macroarea should be capable of surfacing time-sensitive deadlines or events early enough to act.

### Current Status

**Requirement established; not implemented**

---

# Non-Functional Requirements

# 1. Cost

## NFR-1.1

Recurring monetary cost must remain zero.

**Status:** Satisfied.

## NFR-1.2

Production must not consume GitHub Copilot, GitHub AI or other recurring AI credits.

**Status:** Satisfied.

## NFR-1.3

The core system must not depend on temporary promotional cloud credits.

**Status:** Satisfied.

## NFR-1.4

Richer-report improvements must not introduce a required paid API or subscription dependency.

**Status:** Fixed constraint.

## NFR-1.5

Existing Bocconi institutional access may improve personal reader access but may not become an automated paid/credential dependency.

**Status:** Fixed constraint.

---

# 2. Manual Work

## NFR-2.1

Normal production operation should require no daily manual execution.

**Status:** Satisfied.

## NFR-2.2

Normal daily operation should require no copying between GitHub and ChatGPT.

**Status:** Satisfied.

## NFR-2.3

Periodic source review is acceptable.

**Status:** Established.

## NFR-2.4

Milan/Bocconi implementation must not create recurring manual ingestion.

**Status:** Fixed future requirement.

---

# 3. Performance

## NFR-3.1

Daily execution should remain lightweight enough for ordinary GitHub Actions use.

**Status:** Satisfied.

## NFR-3.2

The system should avoid unnecessary repeated retrieval.

## NFR-3.3

Production workflow must use an explicit timeout.

**Status:** Implemented.

## NFR-3.4

Individual remote requests must be bounded.

Current timeout:

```text
10 seconds
```

**Status:** Implemented.

---

# 4. Reliability

## NFR-4.1

One source failure must not automatically invalidate successful sources.

**Status:** Implemented.

## NFR-4.2

Critical processing/configuration failures must prevent false successful publication.

**Status:** Implemented.

## NFR-4.3

Repeated runs must not create uncontrolled duplication.

**Status:** Implemented.

## NFR-4.4

No-news runs must remain understandable and valid.

**Status:** Existing deterministic behaviour present; output-validation edge case remains to be tested if encountered in real production.

## NFR-4.5

Remote failures must be visible rather than hanging silently.

**Status:** Implemented.

## NFR-4.6

Scheduler latency must not be mistaken for application failure.

**Status:** Established.

---

# 5. Maintainability

## NFR-5.1

Configuration should remain separate from processing logic.

**Status:** Implemented.

## NFR-5.2

Dependencies should remain minimal.

**Status:** Implemented.

## NFR-5.3

Modules should have clear responsibilities.

**Status:** Implemented.

## NFR-5.4

A future contributor should be able to add, replace or disable a source without redesigning the system.

**Status:** Demonstrated by Sifted → Tech.eu replacement.

## NFR-5.5

Source-specific complexity must remain proportionate to source value.

**Status:** Fixed operating rule.

## NFR-5.6

Replacing a weak source is preferable to supporting it with disproportionate technical complexity.

**Status:** Demonstrated by Sifted replacement.

## NFR-5.7

Domain expansion should prefer configuration-only changes when the existing architecture already supports them.

**Status:** Demonstrated by Financial Markets activation.

---

# 6. Transparency and Auditability

## NFR-6.1

Every report item must preserve source identity.

## NFR-6.2

Relevance scoring must remain inspectable.

## NFR-6.3

Run health must remain visible.

## NFR-6.4

Source-selection decisions should be documented in canonical project documents.

## NFR-6.5

The system must distinguish source-provided metadata from derived system information.

**Status:** Current architecture satisfies these requirements.

---

# 7. Security, Privacy and Copyright

## NFR-7.1

No credentials may be committed.

## NFR-7.2

Bocconi/OpenAthens credentials must never be embedded in production.

## NFR-7.3

Authenticated publisher content must not be scraped merely because the user can access it manually.

## NFR-7.4

Factiva, Nexis, Business Source Ultimate, Bloomberg, LSEG, FactSet, Capital IQ and similar licensed resources must not be automatically ingested unless an explicitly permitted interface is later validated.

## NFR-7.5

The public repository must not store complete copyrighted articles or substantial restricted excerpts.

## NFR-7.6

Richer-report implementation must use the smallest lawful source-content footprint sufficient for the user need.

**Status:** Fixed constraints.

---

# 8. Product Quality

## NFR-8.1 — Signal Over Volume

More displayed stories are not automatically better.

A sparse report may be correct.

## NFR-8.2 — Classification Percentage Is Not a Target

The system should not maximise classification rate.

A story should remain unclassified rather than receive weak classification evidence.

## NFR-8.3 — Source Prestige Is Not a Selection Criterion

A prestigious publication should enter production only when its marginal value justifies report attention and maintenance.

## NFR-8.4 — Report Attention Is Scarce

The source/domain universe should remain intentionally small.

## NFR-8.5 — Product Inspection Is Required

A technically successful run is insufficient if the generated report is:

- noisy;
- repetitive;
- misleading;
- inaccessible;
- disproportionately concentrated;
- too thin;
- too long;
- strategically irrelevant.

---

# Current Product Decisions

## Source Registry

Current production sources:

```text
BBC News World
BBC News Business
European Central Bank
European Commission Highlighted News
Istat Press Releases
OpenAI News
Tech.eu
```

Sifted has been removed.

---

## Financial Markets

**Decision:** implemented as an active domain.

---

## Italy

**Decision:** validated target macroarea; implementation pending technical source validation.

---

## Milan and Bocconi

**Decision:** validated product requirement.

The requirement itself is no longer open.

Only its source architecture and implementation remain unresolved.

---

## Sifted

**Decision:** replace with Tech.eu.

Reason is owned in detail by `03 Information Taxonomy and Source Policy.md`.

---

## Tech.eu

**Decision:** active Tier 2 production source with no source-default domain.

---

## Premium Bocconi Sources

**Decision:** eligible for a narrow source-specific production exception only when:

- strategically exceptional;
- legitimately accessible to the user;
- discoverable through a permitted public endpoint;
- no authenticated premium retrieval is required.

Current priority candidates:

- Financial Times;
- Il Sole 24 Ore.

---

## Source Defaults

**Decision:** optional classification evidence, not broad publisher categories.

---

## Unclassified Records

**Decision:** valid, stored and omitted from the report by default.

A high unclassified rate alone does not require correction.

---

## Multi-Domain Records

**Decision:** supported.

---

## Primary Report Placement

**Decision:** each story appears once under one primary domain.

Secondary domains remain visible metadata.

---

## Maximum Items Per Domain

Current default:

```text
5
```

---

## Maximum Total Items

Current default:

```text
30
```

---

## Feed Description Length

Current default:

```text
300 characters
```

Temporary pending richer-report design.

---

## Collection Window

Current:

```text
previous 24 hours relative to actual run start
```

---

## Missing Publication Timestamp

Current:

```text
exclude from collection-window eligibility
```

---

## Remote Timeout

Current:

```text
10 seconds
```

---

## Retry Behaviour

**Decision:** none.

Reconsider only from repeated evidence.

---

## Production Schedule

Current:

```text
06:05 Europe/Rome
```

---

## Automated Persistence

**Decision:** production outputs committed automatically when changed.

---

## Degraded Publication

**Decision:** usable output survives recoverable single-source failures.

---

# Remaining Open Product Decisions

## 1. Final Source Universe

The active seven-source registry is not final.

Source selection remains Phase 4 work.

Current technical-audit priority:

```text
Financial Times
```

Then, if still justified:

```text
Il Sole 24 Ore
Bank of Italy
Reuters
```

Do not activate all strategically attractive sources.

---

## 2. BBC Business

Current status:

> **retain temporarily**

Strategic evidence suggests it may become redundant if stronger business/markets sources validate.

Do not remove it before replacements are technically proven.

---

## 3. Italy Source Mix

Determine whether:

```text
Il Sole 24 Ore
+ Istat
+ Bank of Italy
```

is sufficient before adding more Italian sources.

---

## 4. Milan/Bocconi Source Architecture

Determine the smallest public structured source set capable of satisfying the fixed macroarea requirement.

Start with:

- B4i;
- Bocconi Career Services;
- Bocconi News & Events.

---

## 5. Independent AI Coverage

Current OpenAI primary coverage is insufficient as the whole AI information universe.

Evaluate whether future cross-domain sources solve the independent-reporting gap before adding additional specialist feeds.

---

## 6. Richer Report Context

Define:

- required context depth;
- target item length;
- acceptable total reading length;
- usable public metadata fields;
- source-specific fallback behaviour;
- Premium Bocconi Exception presentation;
- copyright boundaries;
- acceptance tests.

Do not implement before Phase 4 is sufficiently mature.

---

## 7. Fixed Reporting Cutoff

Determine whether the daily information window should become independent of actual GitHub Actions start time.

---

## 8. Sponsored Content Handling

Tech.eu testing exposed explicit `[Sponsored]` content.

No new filtering rule should be introduced until repeated evidence establishes a meaningful problem.

---

# Product Acceptance Criteria

The Daily Intelligence System should be considered successful when the following remain true.

## Core Pipeline

- [x] Source configuration loads correctly.
- [x] Public feeds can be collected automatically.
- [x] Records normalize predictably.
- [x] Invalid records are handled explicitly.
- [x] Publication-window filtering is deterministic.
- [x] Exact duplicates are reduced.
- [x] Classification is deterministic.
- [x] Unclassified records are supported.
- [x] Relevance scores are transparent.
- [x] Processed records persist.
- [x] Markdown reports are generated.
- [x] Run summaries persist.

## Automation

- [x] Manual GitHub Actions execution works.
- [x] Scheduled execution works.
- [x] Outputs persist automatically.
- [x] No-change runs do not create empty commits.
- [x] Recoverable source failure creates degraded output.
- [x] Critical configuration failure prevents false publication.
- [x] No production AI credits are consumed.
- [x] No recurring paid API is required.

## Source Quality

- [x] Source accessibility is an explicit evaluation dimension.
- [x] Metadata richness is an explicit evaluation dimension.
- [x] Weak sources can be replaced through configuration.
- [x] Sifted received a final source decision.
- [x] Tech.eu was technically validated before production replacement.
- [ ] Financial Times technical audit complete.
- [ ] Il Sole 24 Ore technical audit complete.
- [ ] Final Phase 4 source universe selected.

## Domain Quality

- [x] Seven original production domains validated.
- [x] Financial Markets implemented.
- [ ] Italy implemented.
- [ ] Milan/Bocconi macroarea implemented.
- [x] Keyword changes tested against real records.
- [x] Generic `startup` false-positive behaviour corrected.
- [ ] Remaining high-value classification misses reviewed over repeated runs.

## Report Quality

- [x] Report is bounded.
- [x] Run completeness is visible.
- [x] Selected items include source links.
- [x] Multi-domain records appear once.
- [x] Sparse reports can be accepted when excluded records are genuinely low-value.
- [ ] Report provides sufficient lawful context without immediate click-through.
- [ ] Premium Bocconi Exception presentation validated.
- [ ] Report length remains manageable after richer-context implementation.

## Milan/Bocconi

- [x] Macroarea accepted as a product requirement.
- [x] Daily Intelligence vs Career OS boundary defined.
- [ ] Public structured sources validated.
- [ ] High-value event/opportunity filtering validated.
- [ ] Time-sensitive opportunity surfacing validated.

---

# Current Product Validation Record

## Source Replacement

Sifted and Tech.eu were compared using the real collector and normaliser.

Observed:

```text
Tech.eu
20 items
20 descriptions

Sifted
24 items
0 descriptions
```

Decision:

```text
Sifted → Tech.eu
```

---

## Keyword and Domain Regression

Candidate Phase 4 taxonomy changes were tested against stored production records.

Regression corpus:

```text
114 records
```

Final observed changed records:

```text
6
```

All were manually interpretable.

The changes:

- removed generic `startup` score inflation;
- recovered a US-China tariffs geopolitical story;
- recovered a South Korean stock-market story;
- preserved historical Sifted domain evidence.

---

## Automated Tests

Current suite:

```text
110 passed
```

---

## Real 17 August 2026 Run

Observed:

```text
7 active
7 successful
1281 valid
32 inside collection window
30 unique
26 unclassified
4 displayed
success
```

The report and all processed records were manually reviewed.

Conclusion:

> **The taxonomy remains intentionally selective. Most unclassified records were correctly omitted.**

---

# Current Priority

The current product-development sequence is:

```text
finish Phase 4A checkpoint
→ technical audit of Financial Times
→ continue highest-value source audits
→ validate Italy source architecture
→ validate Milan/Bocconi source architecture
→ stop source/domain expansion when marginal value falls
→ begin richer-report design
```

Do not simultaneously:

- add many premium publications;
- redesign ranking;
- add AI summarisation;
- add a frontend;
- add advanced deduplication;
- implement agents/RAG;
- expand source count for its own sake.

---

# Current Status

**Status:** Product requirements reconciled with the first validated Phase 4 source/domain correction.

**Current production state:**

- deterministic pipeline complete;
- seven active production sources;
- Sifted replaced by Tech.eu;
- eight active domains;
- Financial Markets implemented;
- Italy pending;
- Milan/Bocconi fixed as a future required macroarea;
- network hardening complete;
- GitHub Actions operational;
- automated persistence operational;
- degraded and critical failure semantics validated;
- 110 tests passing;
- Premium Bocconi Exception defined;
- richer-report requirement validated but not yet implemented.

**Immediate next product-development focus:**

> **Complete the current checkpoint, then technically audit Financial Times under the source-accessibility and Premium Bocconi Exception requirements.**

After source/domain quality becomes sufficiently mature:

> **Begin the dedicated richer-report design phase.**

---

# Changelog

## 2026-08-17 — Phase 4A Source, Domain and Accessibility Requirements Reconciliation

- Replaced Sifted with Tech.eu in the active source registry.
- Recorded Tech.eu as a broad Tier 2 source with no blanket Startups/VC default.
- Recorded direct Tech.eu/Sifted metadata comparison.
- Added Financial Markets as the eighth implemented domain.
- Added Financial Markets product scope and noise exclusions.
- Added `tariffs`, `acquired`, `early-stage fund` and `funding market` as evidence-backed classification refinements.
- Removed generic `startup` after validated low-value classification behaviour.
- Recorded that classification rate is not a product KPI.
- Recorded the successful 17 August 2026 real run and manual record/report inspection.
- Upgraded Milan/Bocconi from candidate to validated product requirement.
- Defined Milan/Bocconi as Professional Ecosystem Intelligence rather than generic local news.
- Added the Daily Intelligence vs Career OS product boundary.
- Added the narrow Premium Bocconi Exception.
- Preserved the prohibition on authenticated automated premium-content access.
- Recorded Financial Times as the next technical source-audit priority.
- Preserved richer-report design as the next major product phase after source/domain correction.

## 2026-08-14 — Phase 3 Production Requirements Reconciliation

- Reconciled requirements with completed GitHub Actions automation.
- Marked scheduled execution as implemented and production-validated.
- Marked automated persistence as implemented.
- Recorded deliberate critical and degraded failure validation.
- Recorded current 06:05 Europe/Rome schedule.
- Added source-accessibility and metadata-richness requirements.
- Added sufficient-context requirement.
- Added inaccessible-link resilience requirement.
- Recorded Bocconi access as personal reading/research rather than automated-ingestion entitlement.
- Deferred richer-context implementation until after source/domain correction.

## 2026-08-11 — Phase 2 Requirements Reconciliation

- Reconciled requirements with seven-source real-source implementation.
- Updated configurable source-registry requirements.
- Added bounded remote collection.
- Recorded 10-second timeout and explicit User-Agent.
- Recorded normal SSL verification.
- Updated metadata and timestamp requirements.
- Recorded seven implemented domains.
- Recorded conservative source-default policy.
- Recorded evidence-based keyword refinement.
- Validated real degraded-source behaviour.
- Reached 110 passing tests.

## 2026-08-11 — Phase 1 Requirements Reconciliation

- Reconciled requirements with the validated local vertical slice.
- Recorded collection-window behaviour.
- Recorded exact duplicate handling.
- Recorded multi-domain and unclassified policies.
- Recorded provisional ranking formula.
- Recorded report limits and description-length defaults.
- Recorded operational report requirements.
- Deferred near-duplicate and multi-source clustering.

## Initial Product Requirements Baseline

- Defined core user jobs.
- Defined functional and non-functional requirements.
- Defined Markdown report requirements.
- Defined automation, source-health, privacy and copyright constraints.
- Defined end-to-end product acceptance criteria.