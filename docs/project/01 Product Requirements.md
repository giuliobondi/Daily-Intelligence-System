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

The Daily Intelligence System should automatically collect, organise, rank and archive relevant public information so that the user can maintain broad awareness without manually scanning many sources.

The product should reduce:

- source fragmentation;
- duplicated stories;
- low-value content;
- manual research time;
- dependence on algorithms optimised for engagement;
- loss of historical information.

The system should increase:

- source transparency;
- information quality;
- domain coverage;
- reading efficiency;
- consistency;
- historical memory;
- awareness of important developments.

The GitHub system is an information collection and organisation product.

It is not responsible for producing deep AI-generated interpretation.

Interpretation remains the responsibility of the separate ChatGPT briefing layer.

---

# Product Status

The local deterministic processing core is implemented and validated.

At Phase 1 closeout, the system can:

- load configuration;
- collect RSS/Atom content from controlled sources;
- isolate source-level failures;
- normalise records;
- validate required fields;
- enforce a publication-time collection window;
- reduce exact duplicates;
- classify records deterministically;
- assign deterministic relevance scores;
- persist processed JSON Lines;
- generate a bounded Markdown report;
- generate a structured JSON run summary;
- expose degraded-run warnings;
- emit run-level logs;
- run locally from one command.

The validated local command is:

```text
python -m daily_intelligence.cli run
```

At Phase 1 closeout:

> **104 automated tests pass.**

The product is not yet production-complete.

The following MVP requirements remain pending:

- a small real-source production set;
- hardened remote-request behaviour;
- GitHub Actions execution;
- automated repository persistence;
- scheduled daily execution;
- production evaluation over time.

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

The user is willing to perform:

- initial setup;
- occasional source review;
- periodic quality evaluation;
- limited maintenance when sources or platform behaviour change.

The user should not need to:

- search each source manually;
- copy content between systems every day;
- start the production workflow manually under normal conditions;
- review raw logs unless a failure occurs;
- make daily classification or ranking decisions.

The current Phase 1 implementation is local and therefore still requires manual invocation.

Automatic daily execution remains a production MVP requirement.

---

# Core User Jobs

The product should help the user complete five main jobs.

## Job 1 — Discover Important Developments

Identify relevant items published by monitored sources during the configured time window.

## Job 2 — Reduce Noise

Remove or suppress malformed records and obvious duplicates.

More advanced near-duplicate handling should be added only if real reports demonstrate a material problem.

## Job 3 — Organise Information

Group stories into meaningful and configurable domains.

## Job 4 — Prioritise Attention

Rank items using transparent and deterministic criteria.

## Job 5 — Preserve Information

Store structured article records and historical daily reports for later review.

---

# Primary User Workflow

Under normal future production operation, the daily workflow should be:

1. The system runs automatically at a configured time.
2. It collects new items from configured public sources.
3. It processes and validates the collected metadata.
4. It selects items inside the configured publication window.
5. It reduces exact duplicates.
6. It classifies and ranks eligible records.
7. It generates the daily report.
8. It stores the report, processed records and run summary.
9. It makes success or failure visible.
10. The user opens the latest report and scans the most relevant items.
11. The user follows only the links that justify deeper reading.

The normal daily user interaction should require no configuration or data entry.

The current local development workflow mirrors this processing path but still requires manual command execution.

---

# Functional Requirements

Requirements are classified as:

- **MUST** — required for the MVP;
- **SHOULD** — important but may follow the first complete production loop;
- **COULD** — optional future enhancement;
- **WILL NOT** — explicitly outside the MVP.

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

### Acceptance Criteria

- A new compatible source can be added through configuration without modifying core collection logic.
- A source can be disabled without deleting it.
- Invalid required source configuration produces a visible error.
- Source configuration remains separate from collection logic.

### Current Status

**Locally validated**

The current implementation supports the required configurable source fields through `sources.yaml`.

The active Phase 1 registry contains one controlled sample source.

A production source universe has not yet been selected.

---

## FR-1.2 — Public Structured Sources

**Priority:** MUST

The MVP must collect only from permitted public structured sources, such as:

- RSS;
- Atom;
- official public APIs;
- other explicitly approved structured endpoints.

### Acceptance Criteria

- The MVP does not require private credentials for normal source collection.
- The MVP does not depend on browser automation.
- The MVP does not depend on prohibited scraping.
- The origin of every collected record is identifiable.

### Current Status

**Locally validated for RSS/Atom-style collection**

No production public-source set has yet been approved.

---

## FR-1.3 — Partial Source Failure

**Priority:** MUST

A failure affecting one source should not automatically prevent successful sources from being processed.

### Acceptance Criteria

- The workflow records which source failed.
- Successful source results remain available.
- The report or execution summary indicates that the run was incomplete.
- A source failure is not silently ignored.

### Current Status

**Implemented and integration-tested**

A degraded run with one successful source and one failed source preserves successful results, records failure metadata, sets run status to `degraded`, exposes warnings in the Markdown report and preserves failure details in the JSON run summary.

---

# 2. Collection

## FR-2.1 — Scheduled Collection

**Priority:** MUST

The system must support automatic daily execution.

### Acceptance Criteria

- The production workflow runs without daily manual initiation.
- The schedule is visible in repository configuration.
- The workflow can also be started manually for testing or recovery.

### Current Status

**Pending**

Local one-command execution is implemented.

GitHub Actions and scheduled execution are not yet implemented.

---

## FR-2.2 — Configurable Collection Window

**Priority:** MUST

The system must support a defined publication window for selecting relevant items.

The current local CLI uses the previous 24 hours.

The value may later be adjusted if live-source behaviour demonstrates a need.

### Acceptance Criteria

- The monitored period is explicit in the generated report.
- Items outside the configured window are excluded.
- Time comparisons use timezone-aware datetimes.
- Collection-window boundaries behave deterministically.

### Current Status

**Implemented and validated**

Current behaviour:

- previous 24 hours in the CLI;
- timezone-aware boundaries required;
- boundaries are inclusive;
- items before the start are excluded;
- items after the end are excluded;
- reversed windows are rejected;
- missing publication timestamps are currently excluded from collection-window eligibility.

The missing-publication-time policy remains provisional pending real-source evidence.

---

## FR-2.3 — Metadata Retrieval

**Priority:** MUST

The system must collect the available metadata required for later processing.

This should include, where available:

- title;
- article URL;
- source;
- publication timestamp;
- feed description or summary;
- retrieval timestamp.

Author metadata may be added when source behaviour and the canonical record schema justify it.

### Acceptance Criteria

- Records preserve the original source identifier.
- Missing optional metadata does not necessarily stop processing.
- Missing required metadata is handled explicitly.
- Retrieval timestamps are recorded.

### Current Status

**Locally validated for the implemented record schema**

---

# 3. Normalisation and Validation

## FR-3.1 — Standard Record Format

**Priority:** MUST

Collected items must be converted into a consistent internal record format.

### Acceptance Criteria

- Records from different compatible sources use the same field names and data types.
- Optional missing values are represented consistently.
- Required fields are validated before later processing.
- Derived metadata remains distinguishable from source-provided metadata.

### Current Status

**Implemented and tested**

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

**Implemented and tested**

---

## FR-3.3 — URL Normalisation

**Priority:** MUST

The system must normalise article URLs where practical.

Normalisation may include:

- removing common tracking parameters;
- handling fragments;
- preserving the original URL;
- avoiding aggressive canonicalisation that may damage valid links.

### Acceptance Criteria

- Obvious tracking variations do not create separate normalised URLs.
- The system does not invent a replacement URL.
- The original publisher URL remains available.
- The final report contains a usable direct link.

### Current Status

**Implemented and tested**

The current normaliser removes selected tracking parameters and fragments while preserving the original article URL separately.

---

## FR-3.4 — Invalid Record Handling

**Priority:** MUST

Malformed or incomplete records must be handled without corrupting the complete run.

### Acceptance Criteria

- Invalid records are separated according to explicit rules.
- The reason for invalidity is inspectable.
- One malformed item does not automatically stop unrelated valid items.
- Validation results distinguish valid and invalid records.

### Current Status

**Implemented and tested at the validation layer**

Per-entry normalisation exceptions are not yet broadly isolated during live-source orchestration.

Unexpected normalisation failures remain critical until real-source evidence justifies a more granular recovery policy.

---

# 4. Duplicate Reduction

## FR-4.1 — Exact Duplicate Detection

**Priority:** MUST

The system must detect obvious duplicates using deterministic identifiers such as normalised URLs and exact normalised titles.

### Acceptance Criteria

- Records with the same normalised URL are not shown as separate primary items.
- Exact normalised-title duplicates are reduced.
- Duplicate handling is deterministic.
- Duplicate records remain inspectable through processing results.

### Current Status

**Implemented and tested**

Current order:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

---

## FR-4.2 — Similar Story Detection

**Priority:** SHOULD

The system may later identify likely duplicate or closely related items with materially similar titles when real reports demonstrate that exact deduplication is insufficient.

### Acceptance Criteria

If implemented:

- the method must remain deterministic or otherwise fully inspectable;
- similarity thresholds must be documented;
- uncertain stories must not be silently discarded;
- false merging must be evaluated explicitly.

### Current Status

**Deferred pending evidence**

Near-duplicate detection is not a Phase 1 or Phase 2 prerequisite unless real-source reports show material repetition.

---

## FR-4.3 — Multi-Source Coverage

**Priority:** SHOULD

When several independent sources cover the same event, the system may preserve evidence of multi-source coverage.

### Acceptance Criteria

If implemented:

- related sources remain recoverable;
- duplicate handling does not erase meaningful source diversity;
- multi-source coverage does not create artificial ranking inflation.

### Current Status

**Deferred pending evidence**

---

# 5. Domain Classification

## FR-5.1 — Configurable Domain Taxonomy

**Priority:** MUST

The system must classify items using a configurable set of domains.

### Acceptance Criteria

- Domains are stored outside core application logic.
- Domains can be changed through configuration.
- Disabled domains do not participate in report selection.
- The data model can support later taxonomy expansion.

### Current Status

**Implemented and tested**

Current Phase 1 active domains:

- Technology and Software;
- Artificial Intelligence.

The full target taxonomy remains defined in `03 Information Taxonomy and Source Policy.md`.

The current two-domain configuration is deliberately narrow and should not be mistaken for final production coverage.

---

## FR-5.2 — Deterministic Classification

**Priority:** MUST

The MVP must use transparent deterministic classification logic.

Current inputs include:

- source defaults;
- configured keywords;
- title;
- description.

Future inputs may include additional deterministic metadata if justified.

### Acceptance Criteria

- Classification can be explained from configuration and record content.
- The system does not require an LLM.
- Rules can be changed without rewriting the complete pipeline.
- Keyword matching avoids obvious substring false positives where practical.

### Current Status

**Implemented and tested**

Current keyword matching is case-insensitive and uses word-boundary protection.

---

## FR-5.3 — Multiple Domains

**Priority:** SHOULD

An item should be able to belong to more than one domain when justified.

### Acceptance Criteria

- The data model does not force exactly one domain.
- Multi-domain records appear once in the main report.
- Secondary domains remain visible where useful.

### Current Status

**Implemented and tested**

Current report behaviour:

- first assigned eligible domain = primary report section;
- later assigned domains = secondary metadata.

---

## FR-5.4 — Unclassified Items

**Priority:** MUST

The system must handle items that match no configured domain.

### Acceptance Criteria

- Unclassified items do not cause processing failure.
- They remain in processed storage.
- They can be reviewed during quality evaluation.
- Main-report inclusion behaviour is explicit.

### Current Status

**Implemented and tested**

Current policy:

- unclassified records remain processed;
- they are omitted from the main Markdown report by default.

---

# 6. Relevance Ranking

## FR-6.1 — Transparent Relevance Score

**Priority:** MUST

The system must calculate a deterministic relevance score for eligible items.

The current Phase 1 formula is intentionally provisional.

### Current Score Model

Current configured scoring is:

```text
source-tier score
+ 2 × domain matches
+ 1 × keyword matches
```

Current source-tier scores are:

- Tier 1 → 4;
- Tier 2 → 3;
- Tier 3 → 2;
- Tier 4 → 1.

### Acceptance Criteria

- Score contributions are documented.
- Scoring weights are configurable.
- The same input and configuration produce the same score.
- Score components remain inspectable.
- No paid model or API is required.

### Current Status

**Implemented and tested**

The formula should be revised only if real-report evaluation demonstrates systematic ranking problems.

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

Current ordering uses deterministic score and metadata-based tie-breaking.

---

## FR-6.3 — Report-Length Control

**Priority:** MUST

The system must prevent the daily report from becoming an unbounded list.

### Acceptance Criteria

- Maximum items per domain are configurable.
- Maximum total items are configurable.
- Higher-ranked eligible items are retained before lower-ranked items.
- Report selection is deterministic.

### Current Status

**Implemented and tested**

Current configured defaults:

- maximum 5 items per domain;
- maximum 30 items overall.

These values remain provisional until real-use evaluation.

---

# 7. Structured Storage

## FR-7.1 — Processed Record Persistence

**Priority:** MUST

The system must persist processed article records required for inspection and historical use.

### Acceptance Criteria

- Records can survive beyond a single run.
- Stored records preserve enough metadata to explain report output.
- The chosen storage method is compatible with the public Git repository.
- Repeated writes to the same target do not create uncontrolled duplication.

### Current Status

**Locally implemented and tested**

Current format:

- JSON Lines.

Current target-file behaviour:

- deterministic overwrite.

Production automated persistence is not yet implemented.

---

## FR-7.2 — Historical Daily Reports

**Priority:** MUST

The system must preserve dated daily reports in production.

### Acceptance Criteria

- Each production report has a date-based repository location.
- Previous production reports are not unintentionally overwritten.
- The archive can be browsed without running code.

### Current Status

**Path model implemented locally; automated historical persistence pending**

The CLI currently targets:

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

Production GitHub persistence is not yet implemented.

---

## FR-7.3 — Reproducibility

**Priority:** SHOULD

Where practical, generated reports should be reproducible from processed records and configuration.

### Acceptance Criteria

- Report generation remains separate from live collection logic.
- Selection and rendering are deterministic.
- Re-running report generation on unchanged inputs produces materially identical output.

### Current Status

**Locally validated for deterministic report generation**

---

# 8. Daily Report

## FR-8.1 — Markdown Output

**Priority:** MUST

The MVP must generate a readable Markdown report.

### Acceptance Criteria

- The report can render correctly in GitHub-compatible Markdown.
- It can be read without specialised software.
- It contains valid source links.
- It remains bounded and scan-friendly.

### Current Status

**Implemented and tested**

---

## FR-8.2 — Report Header

**Priority:** MUST

The report header must include:

- report date;
- monitored time window;
- generation timestamp;
- run status;
- number of active sources;
- number of successful sources;
- number of empty sources;
- number of failed sources;
- number of collected items;
- number of displayed items.

### Acceptance Criteria

- The user can determine whether the report is complete.
- Failed-source counts are visible.
- The monitored period is visible.
- Collected and displayed counts are distinguishable.

### Current Status

**Implemented and integration-tested**

---

## FR-8.3 — Domain Sections

**Priority:** MUST

Displayed items must be grouped into domain sections.

### Acceptance Criteria

- Only domains containing selected records need to be displayed.
- Cross-domain items are not repeated excessively.
- Section placement is deterministic.

### Current Status

**Implemented and tested**

Current policy:

- one primary section per story;
- secondary domains shown as metadata.

---

## FR-8.4 — Story Entry

**Priority:** MUST

Each displayed story should include, where available:

- headline;
- source;
- publication timestamp;
- short feed-provided description;
- relevance score;
- direct article link;
- secondary-domain information where relevant.

A multi-source indicator may be added later if multi-source clustering is implemented.

### Acceptance Criteria

- The report does not fabricate analytical summaries.
- Missing optional fields do not break formatting.
- Restricted full-text content is not reproduced.
- Feed-provided description length is bounded.

### Current Status

**Implemented and tested for current fields**

Current maximum description length:

- 300 characters.

Relevance score is currently displayed.

---

## FR-8.5 — Failure Notice

**Priority:** MUST

Incomplete or degraded runs must be visible in the report.

### Acceptance Criteria

- Degraded status is explicit.
- Warnings identify failed sources or equivalent operational problems.
- The report does not present a degraded run as fully successful.

### Current Status

**Implemented and integration-tested**

---

# 9. Automation and Delivery

## FR-9.1 — GitHub Actions Execution

**Priority:** MUST

The production workflow must run through GitHub Actions or an equally zero-cost approved repository-native mechanism.

### Acceptance Criteria

- The workflow file is version-controlled.
- It supports manual execution.
- It supports scheduled execution.
- It does not call paid AI services.
- It has an explicit timeout.
- It uses minimum required permissions.

### Current Status

**Pending**

GitHub Actions has not yet been implemented.

Real-source production readiness should be validated before automation begins.

---

## FR-9.2 — Automated Persistence

**Priority:** MUST

Successful production runs must automatically preserve intended outputs.

### Acceptance Criteria

- The user is not required to download and re-upload reports.
- Generated changes are committed or otherwise persisted through the approved workflow.
- No-change runs do not create unnecessary commits.
- Invalid outputs are not published as successful production results.

### Current Status

**Pending**

---

## FR-9.3 — Failure Visibility

**Priority:** MUST

The user must be able to detect failed production runs.

### Acceptance Criteria

- Failed automation runs are visible.
- Relevant logs identify the failing stage.
- A failed workflow does not create a falsely successful report.
- Degraded runs remain distinguishable from failed runs.

### Current Status

**Locally implemented at pipeline/report/run-summary level; production automation pending**

---

## FR-9.4 — Daily GitHub Issue

**Priority:** COULD

The system may create a daily GitHub issue as an additional delivery channel after the core pipeline has been validated in real use.

### Current Status

**Deferred**

---

## FR-9.5 — GitHub Pages

**Priority:** COULD

The system may publish a simple GitHub Pages interface only if repository-native reports become a demonstrated usability limitation.

### Current Status

**Deferred**

---

# 10. Source Health

## FR-10.1 — Source Success Tracking

**Priority:** MUST

The system must track whether each configured source succeeds, returns no entries or fails during a run.

### Acceptance Criteria

- Source-level status is inspectable.
- Failure details are preserved.
- Run-level counts distinguish successful, empty and failed sources.
- Source outcomes are visible in logs or structured output.

### Current Status

**Implemented and tested**

Current statuses:

- `success`;
- `empty`;
- `failed`.

Long-term historical source-health tracking is not yet implemented.

---

## FR-10.2 — Empty Feed Handling

**Priority:** MUST

A valid source containing no entries must be distinguished from a failed source.

### Acceptance Criteria

- An empty valid source is not treated as a technical failure.
- Empty-source count is preserved.
- The report does not falsely imply technical failure.

### Current Status

**Implemented at source-result and run-summary level**

---

## FR-10.3 — Source Maintenance

**Priority:** SHOULD

The system should support periodic review of sources that are:

- repeatedly unavailable;
- consistently low-value;
- highly duplicative;
- no longer relevant;
- changed in format.

### Acceptance Criteria

- Sources can be disabled through configuration.
- Maintenance does not require changing core processing logic.
- Low-value sources may be removed rather than supported through disproportionate technical complexity.

### Current Status

**Configuration support implemented; real production maintenance process pending**

---

# Non-Functional Requirements

# 1. Cost

## NFR-1.1

Recurring monetary cost must remain zero.

**Status:** Satisfied by current architecture.

## NFR-1.2

Production must not consume GitHub Copilot or other GitHub AI credits.

**Status:** Satisfied by design; production automation still pending.

## NFR-1.3

The core system must not depend on limited promotional cloud credits.

**Status:** Satisfied by current architecture.

---

# 2. Manual Work

## NFR-2.1

Normal production operation should require no daily manual execution.

**Status:** Pending GitHub Actions.

## NFR-2.2

Normal daily operation should require no copying between GitHub and ChatGPT.

**Status:** Satisfied by architecture; the two layers remain independent.

## NFR-2.3

Periodic source review and maintenance are acceptable.

**Status:** Established operating rule.

---

# 3. Performance

## NFR-3.1

The daily workflow should complete within a lightweight GitHub Actions runtime.

The production threshold should be validated during automation.

## NFR-3.2

The system should avoid unnecessary repeated downloads and processing where practical.

## NFR-3.3

Production automation must use an explicit execution timeout.

**Status:** Pending GitHub Actions.

---

# 4. Reliability

## NFR-4.1

One source failure should not automatically invalidate successful source results.

**Status:** Implemented and tested.

## NFR-4.2

A failure in a critical processing stage must prevent false success.

**Status:** Partially implemented locally; GitHub publication behaviour still pending.

## NFR-4.3

Repeated runs should not create uncontrolled duplicate records or reports.

**Status:** Locally validated for target-file writes and deterministic report generation.

## NFR-4.4

The system should behave predictably when no eligible stories are found.

**Status:** Implemented and tested.

The current report explicitly states when no classified items were selected.

---

# 5. Maintainability

## NFR-5.1

Configuration should be separated from core processing logic where appropriate.

**Status:** Implemented.

## NFR-5.2

Dependencies should remain limited and documented.

**Status:** Implemented.

Current core dependencies are intentionally small.

## NFR-5.3

Files and modules should have clear responsibilities.

**Status:** Implemented in the current local architecture.

## NFR-5.4

A future contributor should be able to understand how to add a source, run the project and inspect a failure.

**Status:** Partially satisfied; canonical documentation is being refreshed and production-source workflow remains to be added.

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

**Status:** Implemented locally.

## NFR-6.4

The system must distinguish feed-provided text from system-generated metadata.

**Status:** Implemented by architecture and report behaviour.

The system does not generate article summaries.

---

# 7. Security and Privacy

## NFR-7.1

No credentials or secrets may be committed to the repository.

## NFR-7.2

The MVP should avoid requiring secrets where possible.

## NFR-7.3

Private Career OS documents must remain outside the public repository.

## NFR-7.4

Private emails, restricted newsletters and personal account information must not be ingested during the MVP.

**Current Status:** All remain fixed architectural constraints.

---

# 8. Copyright and Source Compliance

## NFR-8.1

The system should store and display only permitted metadata and short feed-provided descriptions.

## NFR-8.2

The system must not reproduce complete copyrighted articles.

## NFR-8.3

The system must not bypass paywalls.

## NFR-8.4

Sources should be accessed through permitted public endpoints.

**Current Status:** Satisfied by current controlled implementation and retained as production constraints.

---

# 9. Usability

## NFR-9.1

The report should be scannable in approximately 10–15 minutes.

**Status:** Requires real production evaluation.

## NFR-9.2

The most relevant items should be easy to identify.

**Status:** Current deterministic ranking and bounded report support this, but real-source evaluation is still required.

## NFR-9.3

The report should remain readable on normal GitHub desktop and mobile views.

**Status:** Markdown design supports this; production use should validate it.

## NFR-9.4

The report should not require understanding the underlying code.

**Status:** Satisfied by the current report design.

---

# Report Requirements

The daily report should optimise for:

1. relevance;
2. source quality;
3. diversity;
4. novelty;
5. manageable length;
6. transparency.

It should not optimise for the maximum number of articles.

## Current Implemented Report Structure

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

## Current Story Structure

Each displayed story may include:

```text
Headline and direct publisher link
Source
Publication timestamp
Relevance score
Secondary domains
Short feed-provided description
```

The system does not fabricate summaries.

---

# Current Product Decisions

The following decisions were previously open and are now resolved for the current MVP implementation.

## Relevance Score Display

**Decision:** displayed in the Markdown report.

Rationale:

- improves transparency during early evaluation;
- makes ranking behaviour easier to inspect.

This may be reconsidered later if it reduces readability.

---

## Unclassified Items

**Decision:** remain processed but are omitted from the main daily report by default.

Rationale:

- prevents weak classification from polluting the primary report;
- preserves records for later taxonomy evaluation.

---

## Multi-Domain Items

**Decision:** appear once under one primary domain.

Secondary domains are displayed as metadata.

Rationale:

- reduces repetition;
- preserves cross-domain information.

---

## Maximum Items Per Domain

**Current configured default:** 5.

---

## Maximum Total Items

**Current configured default:** 30.

---

## Feed Description Length

**Current configured maximum:** 300 characters.

Descriptions are feed-provided text only.

---

## Collection Window

**Current local default:** previous 24 hours.

Boundaries are inclusive.

The exact production tolerance may be changed only if real-source behaviour demonstrates a systematic need.

---

## Missing Publication Timestamp

**Current behaviour:** structurally valid records with `published_at=None` are excluded from collection-window eligibility.

This is a conservative Phase 1 policy, not necessarily a permanent product rule.

---

## Run Status Visibility

**Decision:** the Markdown report must expose operational completeness.

The report currently displays:

- run status;
- monitored window;
- source health;
- collected-item count;
- displayed-item count;
- warnings where applicable.

---

# Remaining Open Product Decisions

The following remain unresolved by design.

## Production Execution Time

Choose only when GitHub Actions scheduling is implemented.

## Production Source Universe

Determine the smallest credible real-source set during Phase 2.

Do not set an arbitrary large source target before quality is validated.

## Network Timeout Behaviour

Determine during real-source validation.

## Retry Behaviour

Add only if live failures demonstrate that a bounded retry materially improves reliability.

## Missing Publication Timestamp Policy

Revisit only if useful real sources frequently omit publication timestamps.

## Collection-Window Tolerance

Current default is 24 hours.

Reconsider only if real-source timing creates systematic missed stories.

## Near-Duplicate Detection

Implement only if exact deduplication leaves material repeated coverage.

## Multi-Source Coverage Indicator

Add only if clustering becomes useful.

## Opportunity-Specific Report Section

Remain part of future taxonomy/report evaluation rather than current core behaviour.

## Publisher Concentration Controls

Evaluate during real production use before adding ranking penalties or quotas.

---

# MVP Acceptance Criteria

The production MVP is accepted only when the complete end-to-end scenario works with real structured sources and repository automation.

## Scenario

Given:

- a configured small set of valid public feeds;
- at least one source containing eligible items;
- at least one source that can demonstrate degraded behaviour;
- valid deterministic configuration;

When the production pipeline runs:

- valid sources are collected;
- source failures are recorded;
- records are normalised;
- malformed records are handled according to explicit rules;
- publication-window eligibility is enforced;
- exact duplicates are reduced;
- items are classified;
- relevance scores are calculated;
- processed records are persisted;
- a Markdown report is generated;
- a JSON run summary is generated;
- operational warnings are visible;
- outputs are automatically preserved;
- the run status is visible.

Then:

- the report is readable;
- source links work;
- failed sources are visible;
- no paid AI or paid API service is required;
- no normal daily manual step is required;
- unchanged deterministic inputs produce consistent processing behaviour;
- report length remains bounded;
- invalid critical output is not published as successful.

---

# Local Phase 1 Acceptance Status

The following parts of the MVP acceptance scenario have already been validated locally:

- configuration loading;
- controlled source collection;
- structured source outcomes;
- partial source failure;
- record normalisation;
- validation;
- publication-window filtering;
- exact deduplication;
- domain classification;
- deterministic ranking;
- JSONL persistence;
- Markdown generation;
- run-summary JSON;
- degraded warnings;
- deterministic report limits;
- local CLI execution;
- run-level logging;
- full automated test suite.

At Phase 1 closeout:

> **104 tests pass.**

Still required before full production MVP acceptance:

- live real-source validation;
- network hardening where needed;
- GitHub Actions;
- automated repository persistence;
- scheduled daily execution;
- initial production-use evaluation.

---

# MVP Exclusions

The MVP will not require:

- AI-generated summaries;
- ChatGPT API integration;
- private-repository connectors as a production dependency;
- email ingestion;
- private newsletter parsing;
- full-article extraction;
- browser automation;
- a web application;
- user accounts;
- personalisation for multiple users;
- push notifications outside standard GitHub mechanisms;
- semantic embeddings;
- vector search;
- autonomous agents;
- RAG;
- machine-learning classification;
- investment recommendations;
- political recommendations.

These exclusions may be revisited only if a real validated workflow problem justifies them without violating the system constraints.

---

# Quality Evaluation After Launch

After approximately two weeks of stable automated use, review:

## Usage

- Was the report opened consistently?
- Was it scanned within the intended time?
- Were article links followed selectively?

## Coverage

- Were major relevant developments missed?
- Were any intended domains consistently empty?
- Were some domains overrepresented?
- Was the source universe too narrow or unnecessarily broad?

## Noise

- Were low-value stories frequently included?
- Was promotional content overrepresented?
- Did exact duplicate reduction work adequately?
- Did repeated coverage justify near-duplicate logic?

## Classification

- Were items placed in useful domains?
- Were too many relevant items unclassified?
- Were secondary-domain tags useful?
- Did the two-domain Phase 1 logic generalise cleanly when taxonomy expanded?

## Ranking

- Did high-value developments appear near the top?
- Did source-tier scoring overwhelm actual relevance?
- Did keyword matches inflate weak items?
- Should ranking weights be changed?

## Operations

- Did scheduled runs complete reliably?
- Were source failures visible?
- Was maintenance acceptably low?
- Did any source require disproportionate support?
- Did the system remain at zero recurring cost?

Further product development should be based on this review rather than on assumed needs.

---

# Requirements Traceability

Each material implementation component should be traceable to one or more requirements in this document.

Primary ownership is:

- `00 Project Brief.md` — project purpose, constraints and success definition;
- `01 Product Requirements.md` — required user-visible behaviour;
- `02 System Architecture.md` — technical implementation model;
- `03 Information Taxonomy and Source Policy.md` — information-quality and source-selection policy;
- `04 Development Roadmap and Status.md` — implementation sequencing and current project status.

The requirements document should not become the detailed development changelog.

Implementation completion status belongs primarily in `04 Development Roadmap and Status.md`.

---

# Current Requirement Status Summary

## Locally Validated

- FR-1.1 — Configurable Source Registry
- FR-1.2 — Public Structured Sources for controlled RSS/Atom inputs
- FR-1.3 — Partial Source Failure
- FR-2.2 — Configurable Collection Window
- FR-2.3 — Metadata Retrieval for implemented schema
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
- FR-7.1 — Local Processed Record Persistence
- FR-7.3 — Deterministic Report Reproducibility
- FR-8.1 — Markdown Output
- FR-8.2 — Report Header
- FR-8.3 — Domain Sections
- FR-8.4 — Story Entry
- FR-8.5 — Failure Notice
- FR-10.1 — Source Success Tracking
- FR-10.2 — Empty Feed Handling

## Partially Satisfied / Production Pending

- FR-2.1 — Scheduled Collection
- FR-7.2 — Historical Daily Reports
- FR-9.1 — GitHub Actions Execution
- FR-9.2 — Automated Persistence
- FR-9.3 — Production Failure Visibility
- FR-10.3 — Source Maintenance with real production sources

## Deferred Pending Evidence

- FR-4.2 — Similar Story Detection
- FR-4.3 — Multi-Source Coverage
- FR-9.4 — Daily GitHub Issue
- FR-9.5 — GitHub Pages

---

# Current Status

**Status:** Product requirements reconciled with completed Phase 1 implementation

**Phase 1 local requirements status:**

- deterministic local vertical slice complete;
- operational report behaviour complete;
- collection-window enforcement complete;
- degraded-source handling complete;
- local observability complete;
- 104 tests passing.

**Production MVP still requires:**

- minimal real-source validation;
- network production-readiness;
- GitHub Actions;
- automated persistence;
- scheduled execution;
- real-use evaluation.

**Next product-development focus:**

> Validate the smallest credible real-source run before automating the pipeline.

---

# Changelog

## 2026-08-11 — Phase 1 Requirements Reconciliation

- Reconciled product requirements with the validated local implementation.
- Preserved original functional requirement identifiers.
- Recorded implemented collection-window behaviour.
- Recorded exact duplicate behaviour.
- Recorded current multi-domain and unclassified-item policy.
- Recorded the provisional deterministic ranking formula.
- Recorded report limits and description-length defaults.
- Recorded user-facing operational report requirements as implemented.
- Distinguished local persistence from future automated production persistence.
- Moved near-duplicate and multi-source clustering behind evidence from real reports.
- Clarified that GitHub Actions and scheduled execution remain production MVP requirements but are not Phase 1 requirements.
- Added a concise current requirement-status summary.
- Preserved zero recurring monetary cost and no-production-AI constraints.

## Initial Product Requirements Baseline

- Defined core user jobs.
- Defined functional and non-functional MVP requirements.
- Defined Markdown report requirements.
- Defined automation, source-health, privacy and copyright constraints.
- Defined end-to-end MVP acceptance criteria.