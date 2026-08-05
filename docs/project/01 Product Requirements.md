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

It is not responsible for producing deep AI-generated interpretation. Interpretation remains the responsibility of the separate ChatGPT briefing layer.

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
- start the workflow manually under normal conditions;
- review raw logs unless a failure occurs;
- make daily classification or ranking decisions.

---

# Core User Jobs

The product should help the user complete five main jobs.

## Job 1 — Discover Important Developments

Identify relevant items published by monitored sources during the configured time window.

## Job 2 — Reduce Noise

Remove or suppress obvious duplicates, malformed records and low-value items.

## Job 3 — Organise Information

Group stories into meaningful and configurable domains.

## Job 4 — Prioritise Attention

Rank items using transparent and deterministic criteria.

## Job 5 — Preserve Information

Store structured article records and historical daily reports for later review.

---

# Primary User Workflow

Under normal operation, the daily workflow should be:

1. The system runs automatically at a configured time.
2. It collects new items from configured public sources.
3. It processes and validates the collected metadata.
4. It generates the daily report.
5. It stores the report and processed records.
6. It makes success or failure visible.
7. The user opens the latest report and scans the most relevant items.
8. The user follows only the links that justify deeper reading.

The normal daily user interaction should require no configuration or data entry.

---

# Functional Requirements

Requirements are classified as:

- **MUST** — required for the MVP;
- **SHOULD** — important but may follow the first vertical slice;
- **COULD** — optional future enhancement;
- **WILL NOT** — explicitly outside the MVP.

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
- country or geographic scope;
- active or inactive status.

### Acceptance Criteria

- A new compatible source can be added through configuration without modifying core collection logic.
- A source can be disabled without deleting it.
- Invalid source configuration produces a visible error.

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

---

## FR-1.3 — Partial Source Failure

**Priority:** MUST

A failure affecting one source should not automatically prevent successful sources from being processed.

### Acceptance Criteria

- The workflow records which source failed.
- Successful source results remain available.
- The report or execution summary indicates that the run was incomplete.
- A source failure is not silently ignored.

---

# 2. Collection

## FR-2.1 — Scheduled Collection

**Priority:** MUST

The system must support automatic daily execution.

### Acceptance Criteria

- The production workflow runs without daily manual initiation.
- The schedule is visible in repository configuration.
- The workflow can also be started manually for testing or recovery.

---

## FR-2.2 — Configurable Collection Window

**Priority:** MUST

The system must support a defined publication window for selecting relevant items.

The initial expected window is approximately the previous 24 hours, with flexibility for schedule delays and source timestamp differences.

### Acceptance Criteria

- The monitored period is explicit in the generated report.
- Items outside the configured window are excluded or clearly identified.
- Time comparisons use a consistent timezone policy.

---

## FR-2.3 — Metadata Retrieval

**Priority:** MUST

The system must collect the available metadata required for later processing.

This should include, where available:

- title;
- article URL;
- source;
- author;
- publication timestamp;
- feed description or summary;
- retrieval timestamp.

### Acceptance Criteria

- Records preserve the original source identifier.
- Missing optional metadata does not necessarily stop processing.
- Missing required metadata is handled explicitly.

---

# 3. Normalisation and Validation

## FR-3.1 — Standard Record Format

**Priority:** MUST

Collected items must be converted into a consistent internal record format.

### Acceptance Criteria

- Records from different sources use the same field names and data types.
- Optional missing values are represented consistently.
- Required fields are validated before later processing.

---

## FR-3.2 — Timestamp Normalisation

**Priority:** MUST

Publication and retrieval times must be normalised to a consistent machine-readable format.

### Acceptance Criteria

- Valid timestamps use the same format.
- The system preserves or documents the chosen timezone convention.
- Missing or invalid publication timestamps are flagged.
- Timestamp failures do not silently produce incorrect ordering.

---

## FR-3.3 — URL Normalisation

**Priority:** MUST

The system must normalise article URLs where practical.

Normalisation may include:

- removing common tracking parameters;
- normalising trailing slashes;
- handling fragments;
- preserving the original URL if canonicalisation is uncertain.

### Acceptance Criteria

- Obvious tracking variations do not create separate records.
- The system does not invent a replacement URL.
- The final report contains a usable direct link.

---

## FR-3.4 — Invalid Record Handling

**Priority:** MUST

Malformed or incomplete records must be handled without corrupting the complete run.

### Acceptance Criteria

- Invalid records are excluded or marked according to explicit rules.
- The reason for exclusion is logged.
- One malformed item does not stop unrelated items from being processed.

---

# 4. Duplicate Reduction

## FR-4.1 — Exact Duplicate Detection

**Priority:** MUST

The system must detect obvious duplicates using deterministic identifiers such as normalised URLs and exact normalised titles.

### Acceptance Criteria

- Records with the same normalised URL are not shown as separate primary items.
- Exact normalised-title duplicates are grouped or suppressed.
- The retained record remains linked to its source.

---

## FR-4.2 — Similar Story Detection

**Priority:** SHOULD

The system should identify likely duplicate or closely related items with materially similar titles.

### Acceptance Criteria

- The method is deterministic and configurable.
- Similarity thresholds are documented.
- Similar but genuinely different stories are not automatically discarded without trace.
- Cluster membership can be inspected.

---

## FR-4.3 — Multi-Source Coverage

**Priority:** SHOULD

When several sources cover the same event, the system should preserve evidence of multi-source coverage.

### Acceptance Criteria

- The primary report item can indicate the number of related records or sources.
- Related source links remain recoverable from structured records.
- Duplicate reduction does not erase useful source diversity.

---

# 5. Domain Classification

## FR-5.1 — Configurable Domain Taxonomy

**Priority:** MUST

The system must classify items using a configurable set of domains.

### Acceptance Criteria

- Domains are stored outside core application logic.
- Domains can be added, renamed or disabled through configuration.
- The initial domain set matches the approved Information Taxonomy.

---

## FR-5.2 — Deterministic Classification

**Priority:** MUST

The MVP must use transparent deterministic classification logic.

Possible inputs may include:

- source defaults;
- configured keywords;
- tracked entities;
- title;
- description;
- geographic tags.

### Acceptance Criteria

- Classification can be explained from configuration and record content.
- The system does not require an LLM.
- Classification rules can be changed without rewriting the full pipeline.

---

## FR-5.3 — Multiple Domains

**Priority:** SHOULD

An item should be able to belong to more than one domain when justified.

### Acceptance Criteria

- The data model does not force every record into exactly one domain.
- The daily report avoids unnecessary repetition when an item has several domains.

---

## FR-5.4 — Unclassified Items

**Priority:** MUST

The system must handle items that match no configured domain.

### Acceptance Criteria

- Unclassified items are marked explicitly.
- They do not cause processing failure.
- They can be reviewed during quality evaluation.

---

# 6. Relevance Ranking

## FR-6.1 — Transparent Relevance Score

**Priority:** MUST

The system must calculate a deterministic relevance score for eligible items.

The exact formula will be defined after the taxonomy and source policy are approved.

Possible factors may include:

- source tier;
- domain priority;
- recency;
- geographic relevance;
- tracked entities;
- multi-source coverage;
- duplicate penalties;
- promotional-content penalties.

### Acceptance Criteria

- The factors contributing to a score are documented.
- Scoring weights are configurable where practical.
- The same input and configuration produce the same score.
- The ranking process does not require a paid model or API.

---

## FR-6.2 — Stable Ordering

**Priority:** MUST

Items must be ordered consistently within reports.

### Acceptance Criteria

- Primary sorting uses relevance score.
- Tie-breaking uses documented deterministic fields.
- Repeated generation from unchanged data produces the same ordering.

---

## FR-6.3 — Report-Length Control

**Priority:** MUST

The system must prevent the daily report from becoming an unbounded list.

### Acceptance Criteria

- Maximum items per report or domain are configurable.
- Higher-ranked items are retained before lower-ranked items.
- The report indicates when additional processed items exist outside the displayed selection.

---

# 7. Structured Storage

## FR-7.1 — Processed Record Persistence

**Priority:** MUST

The system must persist processed article records required for inspection and historical use.

### Acceptance Criteria

- Records survive beyond a single workflow run.
- Stored records preserve enough information to understand report output.
- The chosen storage method is compatible with a public Git repository and expected data volume.

---

## FR-7.2 — Historical Daily Reports

**Priority:** MUST

The system must preserve dated daily reports.

### Acceptance Criteria

- Each report has a unique date-based location or identifier.
- Previous reports are not overwritten by normal daily operation.
- The archive can be browsed without running code.

---

## FR-7.3 — Reproducibility

**Priority:** SHOULD

Where practical, generated reports should be reproducible from persisted processed records and configuration.

### Acceptance Criteria

- Report generation is separate from live collection logic.
- Re-running report generation on unchanged inputs produces materially identical output.

---

# 8. Daily Report

## FR-8.1 — Markdown Output

**Priority:** MUST

The MVP must generate a readable Markdown report.

### Acceptance Criteria

- The report renders correctly on GitHub.
- It can be read without specialised software.
- It contains valid direct source links.

---

## FR-8.2 — Report Header

**Priority:** MUST

The report header must include:

- report date;
- monitored time window;
- generation timestamp;
- run status;
- number of active sources;
- number of successful and failed sources;
- number of collected and displayed items.

### Acceptance Criteria

- The user can determine whether the report is complete.
- Failed-source counts are visible.

---

## FR-8.3 — Domain Sections

**Priority:** MUST

Displayed items must be grouped into domain sections.

### Acceptance Criteria

- Sections follow a defined ordering.
- Empty domains are omitted or explicitly marked according to configuration.
- Cross-domain items are not repeated excessively.

---

## FR-8.4 — Story Entry

**Priority:** MUST

Each displayed story should include, where available:

- headline;
- source;
- publication timestamp;
- short feed-provided description;
- relevance score or ranking position;
- direct article link;
- multi-source indicator.

### Acceptance Criteria

- The report does not fabricate an analytical summary.
- Missing optional fields do not break formatting.
- Restricted full-text content is not reproduced.

---

## FR-8.5 — Failure Notice

**Priority:** MUST

Incomplete or degraded runs must be visible in the report.

### Acceptance Criteria

- Failed sources are identified or linked to execution details.
- The report does not present an incomplete run as fully successful.

---

# 9. Automation and Delivery

## FR-9.1 — GitHub Actions Execution

**Priority:** MUST

The production workflow must run through GitHub Actions or an equally zero-cost approved repository-native mechanism.

### Acceptance Criteria

- The workflow file is version-controlled.
- It supports scheduled and manual execution.
- It does not call paid AI services.
- It has an explicit timeout.

---

## FR-9.2 — Automated Persistence

**Priority:** MUST

Successful production runs must automatically preserve their intended outputs.

### Acceptance Criteria

- The user is not required to download and re-upload reports.
- Generated changes are committed or otherwise stored through an approved automated workflow.
- The automation avoids unnecessary commits when output has not changed.

---

## FR-9.3 — Failure Visibility

**Priority:** MUST

The user must be able to detect failed production runs.

### Acceptance Criteria

- Failed GitHub Actions runs are visible in the repository.
- Relevant logs identify the failing stage.
- A failed workflow does not create a falsely successful report.

---

## FR-9.4 — Daily GitHub Issue

**Priority:** COULD

The system may create a daily GitHub issue as an additional delivery channel after the core pipeline is validated.

This is not required for the first MVP.

---

## FR-9.5 — GitHub Pages

**Priority:** COULD

The system may publish a simple GitHub Pages interface after report usefulness has been validated.

This is not required for the MVP.

---

# 10. Source Health

## FR-10.1 — Source Success Tracking

**Priority:** MUST

The system must track whether each configured source succeeds or fails during a run.

### Acceptance Criteria

- Source-level success or failure is visible in logs.
- Repeated failures can be identified over time or through periodic review.

---

## FR-10.2 — Empty Feed Handling

**Priority:** MUST

A successful feed containing no new eligible items must be distinguished from a failed feed.

### Acceptance Criteria

- “No new items” is not logged as a technical failure.
- The report does not imply collection failure when the feed was valid but inactive.

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
- Maintenance does not require changing core logic.

---

# Non-Functional Requirements

# 1. Cost

## NFR-1.1

Recurring monetary cost must remain zero.

## NFR-1.2

Production must not consume GitHub Copilot or other GitHub AI credits.

## NFR-1.3

The core system must not depend on limited promotional cloud credits.

---

# 2. Manual Work

## NFR-2.1

Normal daily operation should require no manual execution.

## NFR-2.2

Normal daily operation should require no copying between GitHub and ChatGPT.

## NFR-2.3

Periodic source review and maintenance are acceptable.

---

# 3. Performance

## NFR-3.1

The daily workflow should complete within a practical lightweight GitHub Actions runtime.

The exact limit will be established during architecture and testing.

## NFR-3.2

The system should avoid unnecessary repeated downloads and processing where practical.

## NFR-3.3

The workflow should use an explicit execution timeout.

---

# 4. Reliability

## NFR-4.1

One source failure should not automatically invalidate successful source results.

## NFR-4.2

A failure in a critical processing stage must prevent false success.

## NFR-4.3

Repeated runs should not create uncontrolled duplicate records or reports.

## NFR-4.4

The system should behave predictably when no eligible stories are found.

---

# 5. Maintainability

## NFR-5.1

Configuration should be separated from core processing logic where appropriate.

## NFR-5.2

Dependencies should remain limited and documented.

## NFR-5.3

Files and modules should have clear responsibilities.

## NFR-5.4

A future contributor should be able to understand how to add a source, run the project and inspect a failure.

---

# 6. Transparency

## NFR-6.1

Every report item must retain a direct source link.

## NFR-6.2

Classification and ranking logic must be inspectable.

## NFR-6.3

Incomplete runs, missing metadata and failed sources must not be concealed.

## NFR-6.4

The system must distinguish feed-provided text from system-generated metadata.

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

---

# 9. Usability

## NFR-9.1

The report should be scannable in approximately 10–15 minutes.

## NFR-9.2

The most relevant items should be easy to identify.

## NFR-9.3

The report should remain readable on desktop and mobile GitHub views.

## NFR-9.4

The report should not require understanding the underlying code.

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

## Initial Report Structure

```text
Report title and date

Run summary
- monitored period
- generation time
- source success
- items collected
- items displayed
- warnings

Domain 1
- ranked story entries

Domain 2
- ranked story entries

...

Source or workflow warnings