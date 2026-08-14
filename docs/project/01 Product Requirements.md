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

The Daily Intelligence System should automatically collect, organise, rank, archive and present relevant public information so that the user can maintain broad awareness without manually scanning many sources.

The product should reduce:

- source fragmentation;
- duplicated stories;
- low-value content;
- manual research time;
- dependence on algorithms optimised for engagement;
- unnecessary click-through before understanding a development;
- inaccessible or low-value follow-up links;
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
- confidence that technically successful runs also produce useful reports.

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
- Sifted.

The current production source set is now under active quality review.

The implemented taxonomy currently contains seven active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

The following target domains remain candidates for expansion:

- Financial Markets;
- Italy;
- Milan and the Bocconi ecosystem.

The automated test suite currently contains:

> **110 passing tests.**

GitHub Actions production execution is operational.

The current scheduled production time is:

```text
06:05 Europe/Rome
```

Scheduled execution has been validated, but GitHub scheduler latency has been observed.

The next product-development priority is no longer automation.

The next priority is:

> **Correct and expand the source/domain universe, then design a richer report that provides enough lawful context to understand important developments without requiring immediate click-through.**

---

# Primary User

The initial product is designed for one user.

The user wants structured daily awareness across:

- global politics and geopolitics;
- economics and macroeconomics;
- financial markets;
- companies and corporate strategy;
- artificial intelligence;
- technology and software;
- startups and venture capital;
- Europe and the European Union;
- Italy;
- Milan and the Bocconi ecosystem.

The user has limited time for daily research and wants negligible recurring manual work.

The user has personal institutional access through Bocconi to many high-quality publications and research resources.

This access can improve the user’s ability to follow source links manually.

It does not change the automated ingestion rules.

The user is willing to perform:

- initial setup;
- occasional source review;
- periodic quality evaluation;
- limited maintenance when sources or platform behaviour change;
- deliberate source and domain redesign when production evidence exposes weaknesses.

The user should not need to:

- search each source manually;
- copy content between systems every day;
- start the production workflow manually under normal conditions;
- review raw logs unless a failure occurs;
- make daily classification or ranking decisions;
- open every article merely to understand the basic development.

---

# Core User Jobs

The product should help the user complete six main jobs.

## Job 1 — Discover Important Developments

Identify relevant items published by monitored sources during the configured time window.

## Job 2 — Reduce Noise

Remove or suppress malformed records and obvious duplicates.

More advanced near-duplicate handling should be added only if repeated production reports demonstrate a material problem.

## Job 3 — Organise Information

Group stories into meaningful and configurable domains.

The system should prefer leaving an item unclassified over assigning a misleading domain.

## Job 4 — Prioritise Attention

Rank items using transparent and deterministic criteria.

## Job 5 — Understand the Development

Provide enough lawful context in the daily report that the user can understand the core development before deciding whether deeper reading is worthwhile.

The report should not function merely as a list of headlines and links.

## Job 6 — Preserve Information

Store structured article records and historical daily reports for later review.

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
11. The user understands the core development of the selected items from the report itself where permitted source information is sufficient.
12. The user follows only the links that justify deeper reading.
13. Premium or research sources may be used manually for deeper understanding where personally accessible.

The normal daily user interaction should require:

- no configuration;
- no data entry;
- no manual workflow execution;
- no copying between systems.

The desired reading model is:

```text
daily report
→ understand important developments
→ decide what deserves deeper reading
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

Implementation status is summarised later in this document.

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

A source may explicitly have no default domain when the feed is too broad for a source-wide topical assumption.

### Acceptance Criteria

- A new compatible source can be added through configuration without modifying core collection logic.
- A source can be disabled without deleting it.
- Invalid required source configuration produces a visible error.
- Source configuration remains separate from collection logic.
- Broad sources can rely entirely on article-level classification without being forced into a default topic.

### Current Status

**Implemented and production-validated**

The active registry contains seven real public RSS sources.

Current source-default policy allows:

```yaml
default_domains: []
```

for broad heterogeneous feeds.

Current active source defaults are:

- BBC News World → none;
- BBC News Business → none;
- European Central Bank → none;
- European Commission Highlighted News → none;
- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

The seven-source registry is no longer considered final.

Production use has now justified a source-quality correction and expansion phase.

---

## FR-1.2 — Public Structured Sources

**Priority:** MUST

The automated production system must collect only from permitted public structured sources or other explicitly approved automation-compatible endpoints.

Examples include:

- RSS;
- Atom;
- official public APIs;
- public structured metadata;
- other endpoints whose terms and licence permit the required automated use.

### Acceptance Criteria

- Production does not require private user credentials for normal source collection.
- Production does not depend on authenticated browser automation.
- Production does not depend on prohibited scraping.
- The origin of every collected record is identifiable.
- Collected content can be stored safely in the public repository.
- Bocconi credentials are never embedded in the production system.
- Institutional reading access is not treated as automatic ingestion permission.

### Current Status

**Implemented and production-validated for RSS**

The current seven-source production registry requires:

- no paid API;
- no browser automation;
- no private credentials;
- no prohibited scraping.

Atom remains supported but is not currently represented in the production registry.

---

## FR-1.3 — Partial Source Failure

**Priority:** MUST

A failure affecting one source should not automatically prevent successful sources from being processed.

### Acceptance Criteria

- The workflow records which source failed.
- Successful source results remain available.
- The report and run summary indicate that the run was incomplete.
- A source failure is not silently ignored.
- The final run status becomes degraded rather than falsely successful where appropriate.

### Current Status

**Implemented and production-validated**

This behaviour has been validated through:

- fixture tests;
- local real-network testing;
- deliberate GitHub Actions degraded-source testing.

Observed production semantics:

- failed source recorded;
- successful sources preserved;
- `degraded` status produced;
- warning shown in Markdown;
- warning preserved in JSON run summary;
- outputs persisted.

---

## FR-1.4 — Source Accessibility and Follow-Up Value

**Priority:** MUST

A production source must be evaluated not only for technical collectability but also for whether its selected items are useful to the user.

A source may be technically valid but still be a poor product source when:

- selected links are frequently inaccessible;
- public feed metadata is too thin to understand the item;
- the source adds little unique value;
- a comparable source offers materially better accessibility or metadata.

### Acceptance Criteria

For each production source, the system design or source policy should make it possible to determine:

- whether automated access is permitted;
- whether the public feed contains enough useful metadata;
- whether linked articles are publicly accessible;
- whether linked articles are accessible to the user through legitimate institutional access;
- whether inaccessible links materially reduce report usefulness;
- whether a better alternative source exists.

A source should be reviewed for replacement when:

- useful context is consistently unavailable;
- follow-up access regularly requires an additional paid subscription;
- source-specific support becomes disproportionate to value.

### Current Status

**Validated requirement — active source review pending**

The requirement was validated by production use.

A selected Sifted story required Sifted Pro access.

Sifted should therefore be reviewed alongside the complete source registry before deciding whether to retain, replace or disable it.

---

# 2. Collection

## FR-2.1 — Scheduled Collection

**Priority:** MUST

The system must support automatic daily execution.

### Acceptance Criteria

- The production workflow runs without daily manual initiation.
- The schedule is visible in repository configuration.
- The workflow can also be started manually for testing or recovery.
- Manual workflow execution is validated before scheduled execution.
- Scheduled execution is observed successfully in production.

### Current Status

**Implemented and production-validated**

GitHub Actions supports:

- `workflow_dispatch`;
- daily scheduled execution.

The current production schedule is:

```text
06:05 Europe/Rome
```

Scheduled workflows have been observed to run successfully.

GitHub scheduler latency has also been observed and remains an external operational limitation.

---

## FR-2.2 — Configurable Collection Window

**Priority:** MUST

The system must support a defined publication window for selecting relevant items.

The current production CLI uses the previous 24 hours relative to actual execution time.

### Acceptance Criteria

- The monitored period is explicit in the generated report.
- Items outside the window are excluded.
- Time comparisons use timezone-aware datetimes.
- Window boundaries behave deterministically.
- Missing publication timestamps are handled explicitly.

### Current Status

**Implemented and production-validated**

Current behaviour:

- previous 24 hours;
- timezone-aware boundaries;
- inclusive boundaries;
- items before the start excluded;
- items after the end excluded;
- reversed windows rejected;
- missing publication timestamps excluded from eligibility.

### Open Product Question

Production scheduling has shown that GitHub may start a scheduled workflow materially later than configured.

Because the current window is based on actual execution time:

```text
scheduler delay
→ later collection-window boundary
→ different eligible article set
```

A deterministic reporting cutoff independent of actual job start time is now an evidence-based design option.

It is not yet an implemented requirement.

---

## FR-2.3 — Metadata Retrieval

**Priority:** MUST

The system must collect the available source metadata required for later processing.

This should include, where available:

- title;
- article URL;
- source;
- publication timestamp;
- feed description or summary;
- retrieval timestamp.

Additional metadata may be added if required by the richer-report design.

Possible future fields include:

- author;
- categories/tags;
- structured summary fields;
- public content metadata;
- canonical URL;
- additional source-provided context.

### Acceptance Criteria

- Records preserve the original source identifier.
- Missing optional metadata does not necessarily stop processing.
- Missing required metadata is handled explicitly.
- Retrieval timestamps are recorded.
- Real-source metadata remains usable after collection and normalisation.
- Source-provided content remains distinguishable from derived system metadata.

### Current Status

**Implemented for current metadata model**

Production evidence shows that missing descriptions are technically acceptable but can be a product-quality problem.

The current metadata model may therefore need expansion during richer-report design.

---

## FR-2.4 — Bounded Remote Collection

**Priority:** MUST

Remote source collection must not wait indefinitely.

Remote requests should use normal public HTTP behaviour and must not weaken standard transport security.

### Acceptance Criteria

- Remote requests use an explicit bounded timeout.
- Requests use an identifiable User-Agent where appropriate.
- Ordinary HTTP and network failures become visible source failures.
- Standard SSL verification remains enabled.
- A failed remote source does not automatically terminate unrelated successful sources.
- No paid HTTP or automation service is required.

### Current Status

**Implemented and production-validated**

Current behaviour:

- 10-second request timeout;
- explicit User-Agent;
- explicit Accept header;
- normal SSL verification;
- ordinary redirect behaviour;
- HTTP/network/timeout errors converted into `CollectionError`.

No retry logic is currently implemented.

---

# 3. Normalisation and Validation

## FR-3.1 — Standard Record Format

**Priority:** MUST

Collected items must be converted into a consistent internal record format before later processing.

The record should preserve:

- original source identity;
- original title;
- normalised title;
- original URL;
- normalised URL;
- publication timestamp where available;
- retrieval timestamp;
- optional description;
- derived domains;
- matched keywords;
- relevance score;
- score components;
- deterministic record identifier.

Future richer-report metadata should remain distinguishable from the current canonical fields.

### Acceptance Criteria

- Logical fields are represented consistently.
- Required fields are validated before later processing.
- Derived metadata remains distinguishable from source-provided metadata.
- Record changes remain backward understandable where practical.

### Current Status

**Implemented, tested and production-exercised**

---

## FR-3.2 — Timestamp Normalisation

**Priority:** MUST

Publication and retrieval times must be normalised to a consistent machine-readable format.

### Acceptance Criteria

- Valid timestamps use timezone-aware datetimes.
- Internal comparison uses UTC-compatible timestamps.
- Missing or invalid publication timestamps are represented explicitly.
- Timestamp failures do not silently produce incorrect ordering or window inclusion.

### Current Status

**Implemented and production-validated**

---

## FR-3.3 — URL Normalisation

**Priority:** MUST

The system must normalise article URLs where practical.

Normalisation may include:

- removing common tracking parameters;
- handling fragments;
- preserving the original URL;
- avoiding aggressive canonicalisation that damages valid links.

### Acceptance Criteria

- Obvious recognised tracking variations are reduced.
- The system does not invent replacement URLs.
- The original publisher URL remains available.
- The final report contains a usable direct link.

### Current Status

**Implemented and tested**

Some publisher-specific parameters remain.

This is a known low-priority limitation.

---

## FR-3.4 — Invalid Record Handling

**Priority:** MUST

Malformed or incomplete records must be handled without corrupting the complete run.

### Acceptance Criteria

- Invalid records are separated according to explicit rules.
- The reason for invalidity is inspectable.
- One malformed item does not automatically stop unrelated valid items where the implemented boundary supports isolation.
- Validation results distinguish valid and invalid records.

### Current Status

**Implemented and tested at the validation layer**

No production evidence has yet justified broader per-entry normalization isolation.

---

# 4. Duplicate Reduction

## FR-4.1 — Exact Duplicate Detection

**Priority:** MUST

The system must detect obvious duplicates using deterministic identifiers such as normalised URLs and exact normalised titles.

### Acceptance Criteria

- Records with the same normalised URL are not shown separately.
- Exact normalised-title duplicates are reduced.
- Duplicate handling is deterministic.
- Duplicate counts remain inspectable.

### Current Status

**Implemented, tested and production-exercised**

Current order:

1. normalised URL;
2. normalised title.

---

## FR-4.2 — Similar Story Detection

**Priority:** SHOULD

The system may later identify closely related items when production reports demonstrate that exact deduplication is insufficient.

### Acceptance Criteria

If implemented:

- logic remains deterministic or fully inspectable;
- thresholds are documented;
- uncertain stories are not silently discarded;
- false merging is evaluated explicitly.

### Current Status

**Deferred pending repeated evidence**

---

## FR-4.3 — Multi-Source Coverage

**Priority:** SHOULD

When several independent sources cover the same event, the system may preserve evidence of multi-source coverage.

### Acceptance Criteria

If implemented:

- related sources remain recoverable;
- source diversity is preserved;
- multi-source coverage does not create artificial ranking inflation.

### Current Status

**Deferred pending evidence**

---

# 5. Domain Classification

## FR-5.1 — Configurable Domain Taxonomy

**Priority:** MUST

The system must classify items using a configurable set of domains.

### Acceptance Criteria

- Domains remain outside core application logic.
- Domains can be changed through configuration.
- Disabled domains do not participate in selection.
- The data model supports later taxonomy expansion.
- The configured taxonomy may be narrower than the complete target taxonomy.

### Current Status

**Implemented and production-validated**

Current active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

Candidate additions now under strategic review:

- Financial Markets;
- Italy;
- Milan and the Bocconi ecosystem.

Source and domain expansion is now the next active product-development priority.

---

## FR-5.2 — Deterministic Classification

**Priority:** MUST

The production system must use transparent deterministic classification logic unless later evidence justifies a different method.

Current inputs include:

- source defaults;
- configured keywords;
- title;
- description.

Future deterministic inputs may include additional metadata.

### Acceptance Criteria

- Classification can be explained from configuration and record content.
- The system does not require an LLM.
- Rules can be changed without rewriting the pipeline.
- Keyword matching avoids obvious substring false positives where practical.
- Source-wide defaults are not used where they systematically misclassify broad feeds.

### Current Status

**Implemented, tested and refined from production evidence**

Broad feeds may use:

```yaml
default_domains: []
```

Current evidence-based Global Politics keyword additions include:

- `war`;
- `conflict`;
- `parliament`.

Broader candidates previously tested and rejected include:

- `government`;
- `defence`;
- `president`;
- `prime minister`.

---

## FR-5.3 — Multiple Domains

**Priority:** SHOULD

An item should be able to belong to more than one domain when justified.

### Acceptance Criteria

- The model does not force exactly one domain.
- Multi-domain records appear once in the main report.
- Secondary domains remain visible where useful.

### Current Status

**Implemented and tested**

---

## FR-5.4 — Unclassified Items

**Priority:** MUST

The system must handle items that match no configured domain.

### Acceptance Criteria

- Unclassified items do not cause failure.
- They remain in processed storage.
- They can be reviewed during quality evaluation.
- Main-report inclusion behaviour is explicit.

### Current Status

**Implemented and production-validated**

Current policy:

- unclassified records remain processed;
- they are omitted from the main Markdown report.

---

# 6. Relevance Ranking

## FR-6.1 — Transparent Relevance Score

**Priority:** MUST

The system must calculate a deterministic relevance score for eligible items.

The current formula remains provisional.

### Current Score Model

```text
source-tier score
+ 2 × domain matches
+ 1 × keyword matches
```

Current source-tier scores:

- Tier 1 → 4;
- Tier 2 → 3;
- Tier 3 → 2;
- Tier 4 → 1.

### Acceptance Criteria

- Score contributions are documented.
- Scoring weights are configurable.
- Unchanged input and configuration produce the same score.
- Score components remain inspectable.
- No paid model or API is required.

### Current Status

**Implemented, tested and production-exercised**

Ranking changes remain deferred until repeated reports demonstrate a systematic ordering problem.

---

## FR-6.2 — Stable Ordering

**Priority:** MUST

Items must be ordered consistently within reports.

### Acceptance Criteria

- Primary sorting uses relevance score.
- Tie-breaking uses documented deterministic fields.
- Repeated generation from unchanged records and configuration produces the same ordering.

### Current Status

**Implemented and tested**

---

## FR-6.3 — Report-Length Control

**Priority:** MUST

The system must prevent the daily report from becoming unbounded.

### Acceptance Criteria

- Maximum items per domain are configurable.
- Maximum total items are configurable.
- Higher-ranked eligible items are retained before lower-ranked items.
- Selection is deterministic.

### Current Status

**Implemented and production-validated**

Current defaults:

- maximum 5 items per domain;
- maximum 30 items overall.

These are maximum bounds, not minimum quality guarantees.

Production evidence has shown that an overly short report can also be undesirable.

---

## FR-6.4 — Report Coverage and Concentration Quality

**Priority:** SHOULD

The report should avoid becoming unhelpfully sparse or excessively concentrated when broader meaningful eligible information is available.

This requirement does not impose fixed quotas.

### Acceptance Criteria

Quality evaluation should make visible:

- displayed-item count;
- source concentration;
- domain concentration;
- unexpectedly empty domains;
- unusually sparse reports.

A technically successful run should not automatically be treated as a satisfactory information product.

### Current Status

**Validated requirement — implementation policy pending**

A scheduled production report completed successfully with healthy source collection but produced a substantially shorter and more concentrated report than preceding days.

This is sufficient to justify monitoring the problem.

It is not yet sufficient to justify automatic quotas or ranking penalties.

---

# 7. Structured Storage

## FR-7.1 — Processed Record Persistence

**Priority:** MUST

The system must persist processed article records required for inspection and historical use.

### Acceptance Criteria

- Records survive beyond a single run.
- Stored records preserve enough metadata to explain report output.
- Storage remains compatible with the public Git repository.
- Repeated writes do not create uncontrolled duplication.

### Current Status

**Implemented, tested and production-persisted**

Current format:

- JSON Lines.

Production outputs are stored under date-based paths and committed automatically.

---

## FR-7.2 — Historical Daily Reports

**Priority:** MUST

The system must preserve dated daily reports in production.

### Acceptance Criteria

- Each report has a date-based repository location.
- Previous reports are not unintentionally overwritten.
- The archive can be browsed without running code.
- Automated persistence has visible success/failure semantics.

### Current Status

**Implemented and production-validated**

Current path pattern:

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

Historical production reports are committed automatically through GitHub Actions.

---

## FR-7.3 — Reproducibility

**Priority:** SHOULD

Where practical, generated reports should be reproducible from processed records and configuration.

### Acceptance Criteria

- Report generation remains separate from live collection logic.
- Selection and rendering remain deterministic.
- Unchanged processed inputs produce materially identical report content.

### Current Status

**Implemented for current deterministic reporting**

---

# 8. Daily Report

## FR-8.1 — Markdown Output

**Priority:** MUST

The production system must generate a readable Markdown report.

### Acceptance Criteria

- The report renders correctly in GitHub-compatible Markdown.
- It can be read without specialised software.
- It contains valid source links.
- It remains bounded and scan-friendly.
- It remains usable on desktop and mobile GitHub views.

### Current Status

**Implemented and production-validated**

---

## FR-8.2 — Report Header

**Priority:** MUST

The report header must include:

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

### Acceptance Criteria

- The user can determine whether the report is operationally complete.
- Failed-source counts are visible.
- The monitored period is visible.
- Collected and displayed counts are distinguishable.

### Current Status

**Implemented and production-validated**

---

## FR-8.3 — Domain Sections

**Priority:** MUST

Displayed items must be grouped into domain sections.

### Acceptance Criteria

- Only domains containing selected records need to appear.
- Cross-domain items are not repeated excessively.
- Section placement is deterministic.
- Misleading source-wide classification is not used merely to populate sections.

### Current Status

**Implemented and production-validated**

Current policy:

- one primary section;
- secondary domains displayed as metadata.

---

## FR-8.4 — Story Entry

**Priority:** MUST

Each displayed story should include, where available:

- headline;
- source;
- publication timestamp;
- relevance score;
- direct article link;
- secondary-domain information;
- permitted source-provided context.

### Current Implemented Fields

The current report may include:

```text
Headline and publisher link
Source
Publication timestamp
Relevance score
Secondary domains
Short feed-provided description
```

Current maximum feed-description length:

```text
300 characters
```

### Acceptance Criteria

- Missing optional fields do not break formatting.
- Restricted full-text content is not reproduced.
- Source-provided text is clearly attributable.
- Report context remains bounded.
- Direct source links remain visible.

### Current Status

**Current fields implemented; product requirement now insufficient**

Production use has shown that the current story entry can be too thin.

This requirement is therefore extended by FR-8.6.

---

## FR-8.5 — Failure Notice

**Priority:** MUST

Incomplete or degraded runs must be visible in the report.

### Acceptance Criteria

- Degraded status is explicit.
- Warnings identify failed sources or equivalent operational problems.
- The report does not present a degraded run as fully successful.

### Current Status

**Implemented and production-validated**

---

## FR-8.6 — Sufficient Context Without Immediate Click-Through

**Priority:** MUST

Each selected report item should provide enough lawful context for the user to understand the key development without requiring immediate click-through.

The report should not necessarily replace the original article.

It should make the original article a deeper-reading destination rather than the only place where the user can understand what happened.

### Acceptance Criteria

A satisfactory item should, where permitted source information supports it, allow the user to understand:

- what happened;
- who or what is involved;
- the basic significance or context of the development;
- why the item was selected.

The implementation must also satisfy:

- source transparency remains visible;
- original article link remains available;
- no paywall bypass;
- no authenticated premium-content scraping;
- no reproduction of complete copyrighted articles;
- no substantial copying beyond permitted source usage;
- no recurring paid API or AI cost;
- missing context is handled explicitly rather than fabricated;
- the report remains readable in approximately the intended daily reading time.

### Current Status

**Validated requirement — design pending**

The current report often functions primarily as a triage index.

Real use showed that the user may need to open the article merely to understand the development.

A dedicated richer-report design phase is therefore required before implementation.

---

## FR-8.7 — Inaccessible-Link Resilience

**Priority:** SHOULD

An inaccessible source link should not automatically make a report item useless.

Where a linked article is restricted, either:

- the report should contain enough permitted public context to make the item useful on its own; or
- the source/item should be reconsidered for production inclusion.

### Acceptance Criteria

- The report does not imply that access is guaranteed.
- The system does not bypass restrictions.
- Production source review considers whether restricted follow-up is acceptable.
- A restricted destination with minimal public context can justify source replacement.

### Current Status

**Validated requirement — source review active**

The Sifted Pro access case provides direct evidence for this requirement.

---

# 9. Automation and Delivery

## FR-9.1 — GitHub Actions Execution

**Priority:** MUST

The production workflow must run through GitHub Actions or another approved zero-cost repository-native mechanism.

### Acceptance Criteria

- Workflow configuration is version-controlled.
- Manual execution is supported.
- Scheduled execution is supported.
- No paid AI service is called.
- An explicit timeout is present.
- Required repository permissions are limited to production needs.
- The workflow uses the same deterministic processing path as local execution.

### Current Status

**Implemented and production-validated**

The workflow uses GitHub Actions with:

- manual dispatch;
- scheduled execution;
- Python 3.12;
- full test suite;
- production CLI;
- output validation;
- automated persistence.

---

## FR-9.2 — Automated Persistence

**Priority:** MUST

Successful or legitimately degraded production runs must automatically preserve intended outputs.

### Acceptance Criteria

- The user does not download and re-upload reports.
- Generated changes are committed automatically.
- No-change runs do not create unnecessary commits.
- Invalid critical output is not published as successful.
- Repository history makes production persistence understandable.

### Current Status

**Implemented and production-validated**

Observed behaviour includes:

- coherent bot output commits;
- dated JSONL;
- dated run summary;
- dated Markdown report;
- no-change guard;
- degraded output persistence.

---

## FR-9.3 — Failure Visibility

**Priority:** MUST

The user must be able to detect failed production runs.

### Acceptance Criteria

- Failed automation runs are visible.
- Logs identify the failing stage.
- A failed workflow does not create a falsely successful report.
- Degraded runs remain distinguishable from failed runs.
- Source-level degradation does not erase useful successful-source output.

### Current Status

**Implemented and production-validated**

Critical configuration failure was deliberately tested.

The workflow failed before valid publication.

Degraded source failure was separately tested and produced persisted degraded output.

---

## FR-9.4 — Daily GitHub Issue

**Priority:** COULD

The system may create a daily GitHub issue as an additional delivery channel if repository-native Markdown becomes a demonstrated usability limitation.

### Current Status

**Deferred**

---

## FR-9.5 — GitHub Pages

**Priority:** COULD

The system may publish a simple GitHub Pages interface if direct repository browsing becomes a demonstrated usability problem.

### Current Status

**Deferred**

---

## FR-9.6 — Scheduling Latency Tolerance

**Priority:** SHOULD

The product should remain useful even when GitHub starts a scheduled run later than the configured cron time.

### Acceptance Criteria

- Scheduler latency does not create false failure states.
- The actual monitored window remains visible.
- Delivery expectations account for possible GitHub delay.
- If schedule latency materially reduces information consistency, the collection-window design should be reconsidered.

### Current Status

**Partially satisfied**

The production schedule was moved to:

```text
06:05 Europe/Rome
```

to create a delivery buffer.

The deeper issue of execution-time-dependent collection windows remains open.

---

# 10. Source Health and Source Quality

## FR-10.1 — Source Success Tracking

**Priority:** MUST

The system must track whether each source succeeds, returns no entries or fails.

### Acceptance Criteria

- Source status is inspectable.
- Failure details are preserved.
- Run-level counts distinguish successful, empty and failed sources.
- Source outcomes are visible in logs or structured output.

### Current Status

**Implemented and production-validated**

Current statuses:

- `success`;
- `empty`;
- `failed`.

---

## FR-10.2 — Empty Feed Handling

**Priority:** MUST

A valid source containing no entries must be distinguished from a failed source.

### Acceptance Criteria

- Empty valid source is not treated as technical failure.
- Empty-source count is preserved.
- Report does not falsely imply technical failure.

### Current Status

**Implemented and tested**

---

## FR-10.3 — Source Maintenance

**Priority:** SHOULD

The system should support periodic review of sources that are:

- repeatedly unavailable;
- consistently low-value;
- highly duplicative;
- no longer relevant;
- changed in format;
- inaccessible to the user;
- too thin in public metadata;
- disproportionately maintenance-heavy.

### Acceptance Criteria

- Sources can be disabled through configuration.
- Maintenance does not require changing core processing logic where avoidable.
- Low-value sources can be removed or replaced.
- Source support should not expand merely to preserve a poor feed.
- Source quality review considers both technical reliability and user usefulness.

### Current Status

**Active requirement**

Production evidence now justifies a structured review of all seven current sources.

Sifted is the first concrete source requiring explicit review.

---

## FR-10.4 — Automated-Source Eligibility

**Priority:** MUST

A candidate automated source should enter production only if it satisfies an explicit source-quality and access review.

### Acceptance Criteria

Candidate evaluation should consider:

- public structured access;
- automation permission;
- timestamp quality;
- description/context richness;
- source reliability;
- topical quality;
- overlap with existing sources;
- maintenance cost;
- public-repository safety;
- linked-content accessibility;
- whether the source adds unique value.

### Current Status

**Validated requirement — active source/domain expansion phase**

---

# Non-Functional Requirements

# 1. Cost

## NFR-1.1

Recurring monetary cost must remain zero.

**Status:** Satisfied.

## NFR-1.2

Production must not consume GitHub Copilot or other GitHub AI credits.

**Status:** Satisfied.

## NFR-1.3

The core system must not depend on limited promotional cloud credits.

**Status:** Satisfied.

## NFR-1.4

Richer-report improvements must not introduce a required paid API or subscription dependency.

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

Periodic source review and maintenance are acceptable.

**Status:** Established operating rule.

## NFR-2.4

Source/domain expansion should not materially increase recurring manual work.

**Status:** Requirement for upcoming expansion.

---

# 3. Performance

## NFR-3.1

The daily workflow should complete within a lightweight GitHub Actions runtime.

**Status:** Satisfied by current production runs.

## NFR-3.2

The system should avoid unnecessary repeated downloads and processing where practical.

Current design performs one feed request per active source per run.

## NFR-3.3

Production automation must use an explicit execution timeout.

**Status:** Implemented.

## NFR-3.4

Individual remote requests must be bounded.

**Status:** Implemented.

Current timeout:

- 10 seconds.

---

# 4. Reliability

## NFR-4.1

One source failure should not automatically invalidate successful source results.

**Status:** Implemented and production-validated.

## NFR-4.2

A failure in a critical processing stage must prevent false success.

**Status:** Implemented and production-validated.

## NFR-4.3

Repeated runs should not create uncontrolled duplicate records or reports.

**Status:** Implemented.

## NFR-4.4

The system should behave predictably when no eligible stories are found.

**Status:** Implemented and tested.

## NFR-4.5

Remote collection should fail visibly rather than hanging indefinitely.

**Status:** Implemented.

## NFR-4.6

External scheduler latency must not be mistaken for application failure.

**Status:** Established from production evidence.

---

# 5. Maintainability

## NFR-5.1

Configuration should be separated from core processing logic.

**Status:** Implemented.

## NFR-5.2

Dependencies should remain limited and documented.

**Status:** Implemented.

## NFR-5.3

Files and modules should have clear responsibilities.

**Status:** Implemented.

## NFR-5.4

A future contributor should be able to understand how to add a source, run the project and inspect a failure.

**Status:** Mostly satisfied; documentation is being reconciled with Phase 3.

## NFR-5.5

Source-specific complexity should remain proportionate to source value.

**Status:** Fixed operating rule.

## NFR-5.6

Replacing a weak source is preferable to introducing disproportionate source-specific complexity.

**Status:** Active design rule for source expansion.

---

# 6. Transparency

## NFR-6.1

Every displayed report item must retain a direct source link.

**Status:** Implemented.

## NFR-6.2

Classification and ranking logic must be inspectable.

**Status:** Implemented.

## NFR-6.3

Incomplete runs, missing metadata and failed sources must not be concealed.

**Status:** Implemented and production-validated.

## NFR-6.4

Source-provided text must remain distinguishable from derived system metadata.

**Status:** Implemented for current report.

Any future richer context must preserve this distinction.

## NFR-6.5

Source-wide classification assumptions must remain visible in configuration.

**Status:** Implemented.

## NFR-6.6

The report must not imply access rights that the system or user does not have.

**Status:** New requirement.

---

# 7. Security and Privacy

## NFR-7.1

No credentials or secrets may be committed to the repository.

## NFR-7.2

Production should avoid requiring secrets where possible.

## NFR-7.3

Private Career OS documents must remain outside the public repository.

## NFR-7.4

Private emails, restricted newsletters and personal account information must not be ingested.

## NFR-7.5

Bocconi credentials must never be embedded in GitHub Actions, code, repository configuration or automated collection.

## NFR-7.6

Institutional-access publications may be used manually for personal reading and research without becoming production ingestion sources.

**Current Status:** All are fixed constraints.

---

# 8. Copyright and Source Compliance

## NFR-8.1

The system may store and display only content whose use is compatible with the source endpoint, licence and public-repository model.

## NFR-8.2

The system must not reproduce complete copyrighted articles.

## NFR-8.3

The system must not bypass paywalls.

## NFR-8.4

Automated sources should be accessed through permitted public endpoints or explicitly authorised automation mechanisms.

## NFR-8.5

Institutional access through Bocconi does not itself grant automated ingestion or redistribution rights.

## NFR-8.6

The richer-report requirement must be satisfied without unauthorised copying of restricted full text.

**Current Status:** Fixed design constraints.

---

# 9. Usability

## NFR-9.1

The report should remain scannable in approximately 10–15 minutes.

**Status:** Still a target; richer context must be designed within this constraint.

## NFR-9.2

The most relevant items should be easy to identify.

**Status:** Current deterministic ranking supports this but continues to require production evaluation.

## NFR-9.3

The report should remain readable on normal GitHub desktop and mobile views.

**Status:** Markdown implementation supports this.

## NFR-9.4

The report should not require understanding the underlying code.

**Status:** Satisfied.

## NFR-9.5

The report should prefer a smaller credible output over a larger misleading one.

**Status:** Established.

## NFR-9.6

The report should not become so sparse that meaningful coverage is lost without explanation.

**Status:** New evaluation requirement.

## NFR-9.7

The report should provide enough context to understand the core development before immediate source click-through.

**Status:** Validated requirement; design pending.

## NFR-9.8

The report should remain useful when a linked source is not directly accessible, provided sufficient lawful context is available.

**Status:** Validated requirement; source/design work pending.

---

# Report Requirements

The daily report should optimise for:

1. relevance;
2. source quality;
3. sufficient context;
4. diversity;
5. novelty;
6. manageable length;
7. transparency;
8. accessibility;
9. reliability.

It should not optimise for:

- maximum article count;
- maximum copied text;
- maximum source count;
- headline volume alone.

---

# Current Implemented Report Structure

```text
Report title and date

Operational header
- generation timestamp
- run status
- monitored period
- active sources
- successful sources
- empty sources
- failed sources
- items collected
- items displayed

Run warnings when present

Domain section
- ranked story entries

Additional domain sections where selected items exist
```

---

# Current Story Structure

Current production stories may include:

```text
Headline and direct publisher link
Source
Publication timestamp
Relevance score
Secondary domains
Short feed-provided description
```

The system currently does not generate richer article summaries.

---

# Target Story Experience

The future story entry should remain concise but provide enough context to answer, where the permitted source material supports it:

```text
What happened?
Who or what is involved?
Why is it relevant?
What is the source?
When did it happen?
Where can I read more?
```

The exact structure is not yet decided.

The design phase should determine:

- whether context is paragraph-based or bullet-based;
- maximum context length;
- permitted source inputs;
- fallback behaviour;
- whether sources with insufficient public context should be excluded;
- whether additional metadata fields are required.

---

# Current Product Decisions

## Relevance Score Display

**Decision:** currently displayed.

Rationale:

- improves ranking transparency;
- useful during evaluation.

May be reconsidered if richer context makes the report visually overloaded.

---

## Unclassified Items

**Decision:** remain processed but omitted from the main report.

Rationale:

- prevents weak classification from polluting the report;
- preserves evidence for taxonomy review.

---

## Multi-Domain Items

**Decision:** appear once under one primary domain.

Secondary domains remain metadata.

---

## Source Defaults

**Decision:** source defaults are optional evidence, not broad publisher categories.

Broad sources may use:

```yaml
default_domains: []
```

---

## Maximum Items Per Domain

**Current default:**

```text
5
```

---

## Maximum Total Items

**Current default:**

```text
30
```

---

## Feed Description Length

**Current default:**

```text
300 characters
```

This may change during richer-report design.

---

## Collection Window

**Current behaviour:**

```text
previous 24 hours relative to actual run start
```

Boundaries are inclusive.

A deterministic daily cutoff is now an open design option because scheduler latency can shift the window.

---

## Missing Publication Timestamp

**Current behaviour:**

Records with:

```text
published_at = None
```

are excluded from collection-window eligibility.

---

## Remote Request Timeout

**Decision:**

```text
10 seconds per remote source request
```

---

## Retry Behaviour

**Decision:** no retry logic.

Reconsider only if repeated production evidence justifies it.

---

## Run Status Visibility

**Decision:** Markdown report must expose operational completeness.

Current visible fields include:

- run status;
- monitored window;
- source health;
- collected count;
- displayed count;
- warnings.

---

## Production Schedule

**Current decision:**

```text
06:05 Europe/Rome
```

This time provides buffer against observed GitHub scheduling delay.

---

## Automated Persistence

**Decision:** changed production outputs are committed automatically.

No-change runs should not create empty commits.

---

## Degraded Publication

**Decision:** a recoverable source failure produces a degraded report rather than discarding usable successful-source output.

---

## Critical Failure

**Decision:** a critical configuration or processing failure prevents successful publication.

---

## Source Expansion

**Decision:** the current seven-source registry is no longer treated as final.

Source expansion is now justified by real product-quality evidence.

The immediate source review should include:

- Sifted;
- missing strategic domain coverage;
- metadata richness;
- accessibility;
- source concentration;
- alternative source quality.

---

## Bocconi Access

**Decision:** Bocconi access is a personal reading/research advantage.

It is not an automated ingestion entitlement.

Source evaluation should distinguish:

```text
automation suitability
```

from:

```text
personal reading accessibility
```

---

# Remaining Open Product Decisions

## Source Registry Correction

Determine:

- whether Sifted should remain active;
- whether restricted or thin feeds should be replaced;
- which current sources add sufficient unique value;
- whether any source creates disproportionate concentration.

---

## Source Expansion

Determine the desired information-source universe with the Career Agent, then evaluate candidate sources technically.

Candidate evaluation must consider:

- public feed/API availability;
- metadata richness;
- reliability;
- accessibility;
- overlap;
- source quality;
- maintenance;
- automation permission.

---

## Domain Expansion

Reconsider:

- Financial Markets;
- Italy;
- Milan and Bocconi ecosystem.

Do not activate automatically without suitable sources and classification logic.

---

## Richer Report Context

Define precisely:

- what constitutes enough context;
- target item length;
- permitted source material;
- fallback behaviour;
- context presentation;
- acceptable report length;
- how inaccessible links should be handled.

---

## Fixed Reporting Cutoff

Determine whether the daily publication window should remain tied to actual execution time.

A possible future model is:

```text
fixed daily cutoff
→ deterministic 24-hour window
→ GitHub delay affects delivery only
```

rather than:

```text
actual workflow start
→ rolling 24-hour window
→ GitHub delay changes report composition
```

---

## Near-Duplicate Detection

Implement only if repeated reports demonstrate meaningful repeated coverage.

---

## Multi-Source Coverage Indicator

Implement only if clustering becomes useful.

---

## Publisher Concentration Controls

Evaluate only after additional production history.

---

## Ranking Weights

Change only when repeated reports demonstrate systematic ordering problems.

---

## Delivery Interface

Evaluate GitHub Pages, GitHub Issues, stable latest-report links or Obsidian-oriented workflows only if direct GitHub Markdown reading creates demonstrated friction.

---

# Production MVP Acceptance Criteria

The core production MVP is accepted when the complete end-to-end automation works with real structured sources.

## Scenario

Given:

- valid configured public feeds;
- deterministic configuration;
- repository automation;

When the production pipeline runs:

- sources are collected;
- source failures are recorded;
- remote requests remain bounded;
- records are normalised;
- malformed records are handled according to explicit rules;
- publication-window eligibility is enforced;
- exact duplicates are reduced;
- items are classified;
- relevance scores are calculated;
- processed records are persisted;
- Markdown report is generated;
- JSON run summary is generated;
- warnings are visible;
- outputs are automatically preserved;
- run status is visible.

Then:

- the report is readable;
- source links are present;
- failed sources are visible;
- no paid AI or paid API is required;
- no normal daily manual step is required;
- unchanged deterministic input produces consistent processing behaviour;
- report length remains bounded;
- invalid critical output is not published as successful;
- degraded source-level failure preserves successful-source output;
- no-change automation runs do not create unnecessary commits.

## Current Acceptance Status

**Core production automation accepted**

Phase 3 validated:

- GitHub Actions;
- manual execution;
- scheduled execution;
- automated persistence;
- no-change guard;
- degraded publication;
- critical-failure semantics;
- visible logs;
- output validation;
- zero-cost execution.

The remaining work is now product-quality improvement rather than core production automation.

---

# Post-MVP Product-Quality Acceptance

The system should not be considered mature merely because the production loop runs successfully.

The information product should also satisfy:

- useful source coverage;
- reasonable domain coverage;
- sufficient story context;
- acceptable source accessibility;
- bounded reading time;
- transparent failures;
- limited source concentration;
- acceptable scheduler/window behaviour;
- negligible daily manual work.

These quality criteria are now the focus of the next project phases.

---

# Current Quality-Evaluation Questions

## Usage

- Is the report opened consistently?
- Can it be read within the intended time?
- Are links followed selectively rather than necessarily for basic understanding?

## Coverage

- Are important developments missed?
- Are strategic domains absent?
- Is the current source universe too narrow?
- Do Financial Markets, Italy or Milan/Bocconi require implementation?

## Source Quality

- Are selected links accessible?
- Does the source provide enough public context?
- Does the source add unique value?
- Is Sifted worth retaining?
- Are better accessible alternatives available?
- Does Bocconi access make manual follow-up practical?

## Context

- Can the user understand the development from the report?
- Are descriptions too thin?
- Does missing feed text make the story effectively headline-only?
- Would richer public structured metadata solve the problem?

## Noise

- Are low-value stories frequently included?
- Is promotional content overrepresented?
- Is exact deduplication adequate?
- Do repeated stories justify near-duplicate logic?

## Classification

- Are items placed in useful domains?
- Are too many relevant items unclassified?
- Do the seven current domains cover the intended information universe?
- Do source defaults create systematic false positives?

## Ranking

- Do high-value stories appear near the top?
- Does source tier overwhelm actual relevance?
- Do keyword matches inflate weak items?
- Does domain count inflate weak items?

## Concentration

- Does one source dominate the report?
- Does one domain dominate the report?
- Are reports sometimes too sparse despite healthy collection?
- Would source expansion improve breadth?

## Operations

- Do scheduled runs complete reliably?
- How large are scheduler delays?
- Does scheduler delay materially shift report composition?
- Are source failures visible?
- Is maintenance acceptably low?
- Do degraded runs remain useful?
- Does the system remain zero-cost?

Further development should be based on this evidence.

---

# Requirements Traceability

Each material implementation component should be traceable to one or more requirements in this document.

Primary ownership remains:

- `00 Project Brief.md` — purpose, constraints and strategic success definition;
- `01 Product Requirements.md` — required user-visible behaviour;
- `02 System Architecture.md` — technical implementation model;
- `03 Information Taxonomy and Source Policy.md` — source, taxonomy and information-quality rules;
- `04 Development Roadmap and Status.md` — sequencing and canonical current status.

This document should not become the detailed implementation changelog.

Detailed implementation history belongs primarily in:

```text
04 Development Roadmap and Status.md
```

---

# Current Requirement Status Summary

## Implemented and Validated

- FR-1.1 — Configurable Source Registry
- FR-1.2 — Public Structured Sources
- FR-1.3 — Partial Source Failure
- FR-2.1 — Scheduled Collection
- FR-2.2 — Configurable Collection Window
- FR-2.3 — Current Metadata Retrieval
- FR-2.4 — Bounded Remote Collection
- FR-3.1 — Standard Record Format
- FR-3.2 — Timestamp Normalisation
- FR-3.3 — URL Normalisation
- FR-3.4 — Invalid Record Handling at validation layer
- FR-4.1 — Exact Duplicate Detection
- FR-5.1 — Configurable Domain Taxonomy
- FR-5.2 — Deterministic Classification
- FR-5.3 — Multiple Domains
- FR-5.4 — Unclassified Items
- FR-6.1 — Transparent Relevance Score
- FR-6.2 — Stable Ordering
- FR-6.3 — Report-Length Control
- FR-7.1 — Processed Record Persistence
- FR-7.2 — Historical Daily Reports
- FR-7.3 — Deterministic Report Reproducibility
- FR-8.1 — Markdown Output
- FR-8.2 — Report Header
- FR-8.3 — Domain Sections
- FR-8.4 — Current Story Entry Fields
- FR-8.5 — Failure Notice
- FR-9.1 — GitHub Actions Execution
- FR-9.2 — Automated Persistence
- FR-9.3 — Failure Visibility
- FR-10.1 — Source Success Tracking
- FR-10.2 — Empty Feed Handling

## Validated Requirement / Active Design or Review

- FR-1.4 — Source Accessibility and Follow-Up Value
- FR-6.4 — Report Coverage and Concentration Quality
- FR-8.6 — Sufficient Context Without Immediate Click-Through
- FR-8.7 — Inaccessible-Link Resilience
- FR-9.6 — Scheduling Latency Tolerance
- FR-10.3 — Source Maintenance
- FR-10.4 — Automated-Source Eligibility

## Deferred Pending Evidence

- FR-4.2 — Similar Story Detection
- FR-4.3 — Multi-Source Coverage
- FR-9.4 — Daily GitHub Issue
- FR-9.5 — GitHub Pages

---

# Current Status

**Status:** Product requirements reconciled with completed Phase 3 GitHub Automation and initial production-quality evidence.

**Core production status:**

- deterministic pipeline complete;
- seven-source production registry operational;
- seven-domain taxonomy operational;
- network request hardening complete;
- GitHub Actions implemented;
- manual workflow validated;
- scheduled workflow validated;
- automated persistence implemented;
- no-change guard validated;
- degraded source publication validated;
- critical failure semantics validated;
- historical reports operational;
- operational logs visible;
- 110 tests passing.

**New validated product-quality findings:**

- report context can be too thin;
- some selected links may be inaccessible;
- Sifted requires explicit review;
- source accessibility must become a source-selection criterion;
- personal Bocconi access expands manual follow-up but not automation rights;
- current source/domain universe may be too narrow;
- some reports may be unusually sparse or concentrated;
- GitHub scheduler latency can shift the rolling reporting window.

**Next product-development focus:**

> Correct and expand the source and domain universe first, beginning with the weaknesses exposed by Sifted and current coverage gaps. After the source universe is improved, conduct a deliberate richer-report design phase before implementing additional context logic.

---

# Changelog

## 2026-08-14 — Phase 3 Production Requirements Reconciliation and Product-Quality Expansion

- Reconciled requirements with completed GitHub Actions implementation.
- Marked scheduled execution as implemented and production-validated.
- Marked automated persistence as implemented.
- Marked production failure visibility as implemented.
- Recorded deliberate critical configuration failure validation.
- Recorded deliberate degraded-source publication validation.
- Recorded no-change commit-guard validation.
- Recorded repository-native historical production output.
- Recorded current 06:05 Europe/Rome schedule.
- Added scheduling-latency tolerance as a product concern.
- Added scheduler-delay/report-window coupling as an open product decision.
- Added FR-1.4 for source accessibility and follow-up value.
- Added FR-6.4 for sparse/concentrated report quality.
- Added FR-8.6 for sufficient context without immediate click-through.
- Added FR-8.7 for inaccessible-link resilience.
- Added FR-9.6 for scheduling-latency tolerance.
- Added FR-10.4 for explicit automated-source eligibility.
- Expanded source-maintenance requirements to include accessibility and metadata richness.
- Recorded Sifted Pro access as concrete evidence requiring source review.
- Recorded Bocconi access as a personal reading/research layer rather than automation permission.
- Reframed the primary user workflow so source links are for deeper reading rather than basic comprehension.
- Changed the next product-development priority from automation to source/domain correction and expansion.
- Deferred richer-report implementation until a dedicated design phase is completed.
- Preserved zero recurring monetary cost and no-production-AI constraints.

## 2026-08-11 — Phase 2 Requirements Reconciliation

- Reconciled requirements with the validated seven-source real-source implementation.
- Updated configurable source registry requirements.
- Updated public structured source requirements.
- Updated partial-source-failure requirements.
- Added bounded remote collection requirement.
- Recorded 10-second timeout and explicit User-Agent.
- Recorded normal SSL verification.
- Updated metadata and timestamp requirements.
- Recorded seven implemented domains.
- Recorded conservative source-default policy.
- Recorded evidence-based classification refinement.
- Updated report requirements with real-output validation.
- Recorded real degraded-source behaviour.
- Recorded 110 passing tests.
- Made GitHub Actions the next production requirement.

## 2026-08-11 — Phase 1 Requirements Reconciliation

- Reconciled requirements with the validated local implementation.
- Preserved original functional requirement identifiers.
- Recorded collection-window behaviour.
- Recorded exact duplicate handling.
- Recorded current multi-domain and unclassified policy.
- Recorded provisional ranking formula.
- Recorded report limits and description-length defaults.
- Recorded operational report requirements.
- Distinguished local persistence from future automated persistence.
- Deferred near-duplicate and multi-source clustering.
- Preserved zero recurring monetary cost and no-production-AI constraints.

## Initial Product Requirements Baseline

- Defined core user jobs.
- Defined functional and non-functional MVP requirements.
- Defined Markdown report requirements.
- Defined automation, source-health, privacy and copyright constraints.
- Defined end-to-end MVP acceptance criteria.