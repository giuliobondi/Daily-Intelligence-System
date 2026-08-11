````markdown
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

The deterministic local processing core and the minimal real-source layer are implemented and validated.

At Phase 2 closeout, the system can:

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
- persist processed JSON Lines locally;
- generate a bounded Markdown report;
- generate a structured JSON run summary;
- expose degraded-run warnings;
- emit run-level logs;
- run locally from one command.

The validated local command is:

```text
python -m daily_intelligence.cli run
```

The active real-source configuration contains seven validated public RSS sources:

- BBC News World;
- BBC News Business;
- European Central Bank;
- European Commission Highlighted News;
- Istat Press Releases;
- OpenAI News;
- Sifted.

The implemented taxonomy currently contains seven active domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

At Phase 2 closeout:

> **110 automated tests pass.**

The product is not yet production-complete.

The following MVP requirements remain pending:

- GitHub Actions execution;
- automated repository persistence;
- scheduled daily execution;
- production failure and publication behaviour in GitHub Actions;
- longitudinal production evaluation over repeated daily runs.

The next product-development step is therefore automation, not additional classification or source expansion.

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

The current implementation still requires manual local invocation.

Automatic daily execution remains a production MVP requirement.

---

# Core User Jobs

The product should help the user complete five main jobs.

## Job 1 — Discover Important Developments

Identify relevant items published by monitored sources during the configured time window.

## Job 2 — Reduce Noise

Remove or suppress malformed records and obvious duplicates.

More advanced near-duplicate handling should be added only if repeated real reports demonstrate a material problem.

## Job 3 — Organise Information

Group stories into meaningful and configurable domains.

The system should prefer leaving an item unclassified over assigning a misleading domain.

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
9. It makes success, degradation or failure visible.
10. The user opens the latest report and scans the most relevant items.
11. The user follows only the links that justify deeper reading.

The normal daily user interaction should require no configuration or data entry.

The current local development workflow mirrors this complete processing path but still requires manual command execution.

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

A source may explicitly have no default domain when the feed is too broad for a source-wide topical assumption.

### Acceptance Criteria

- A new compatible source can be added through configuration without modifying core collection logic.
- A source can be disabled without deleting it.
- Invalid required source configuration produces a visible error.
- Source configuration remains separate from collection logic.
- Broad sources can rely entirely on article-level classification without being forced into a default topic.

### Current Status

**Implemented and real-source validated**

The current implementation supports the required configurable source fields through `sources.yaml`.

The active registry contains seven validated real public RSS sources.

Current source-default policy allows:

```yaml
default_domains: []
```

for broad heterogeneous feeds.

Current active source defaults are intentionally narrow:

- BBC News World → none;
- BBC News Business → none;
- European Central Bank → none;
- European Commission Highlighted News → none;
- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

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
- Public-source metadata can be stored safely in the public repository.

### Current Status

**Implemented and real-source validated for RSS**

Seven real public RSS sources were successfully collected through the actual project collector.

The current source universe requires:

- no paid API;
- no browser automation;
- no private credentials;
- no prohibited scraping.

Atom remains supported by the configuration and collector design but is not currently represented in the seven-source real registry.

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

**Implemented and validated with fixtures and real network behaviour**

A degraded run with one successful source and one failed source:

- preserves successful results;
- records failure metadata;
- sets run status to `degraded`;
- exposes warnings in the Markdown report;
- preserves failure details in the JSON run summary.

Phase 2 also deliberately tested one valid real Istat source together with one invalid remote hostname.

Observed behaviour matched the requirement:

- Istat succeeded;
- the invalid source failed with `CollectionError`;
- successful output remained available;
- the run became degraded rather than falsely successful.

---

# 2. Collection

## FR-2.1 — Scheduled Collection

**Priority:** MUST

The system must support automatic daily execution.

### Acceptance Criteria

- The production workflow runs without daily manual initiation.
- The schedule is visible in repository configuration.
- The workflow can also be started manually for testing or recovery.
- Manual workflow execution is validated before scheduled execution is enabled.

### Current Status

**Pending**

Local one-command execution is implemented and real-source validated.

GitHub Actions has not yet been implemented.

The next implementation step is a manual `workflow_dispatch` workflow.

Scheduled execution should be enabled only after that workflow is validated.

---

## FR-2.2 — Configurable Collection Window

**Priority:** MUST

The system must support a defined publication window for selecting relevant items.

The current local CLI uses the previous 24 hours.

The value may later be adjusted if repeated production behaviour demonstrates a need.

### Acceptance Criteria

- The monitored period is explicit in the generated report.
- Items outside the configured window are excluded.
- Time comparisons use timezone-aware datetimes.
- Collection-window boundaries behave deterministically.

### Current Status

**Implemented and real-source validated**

Current behaviour:

- previous 24 hours in the CLI;
- timezone-aware boundaries required;
- boundaries are inclusive;
- items before the start are excluded;
- items after the end are excluded;
- reversed windows are rejected;
- missing publication timestamps are excluded from collection-window eligibility.

Phase 2 real-source runs showed that the current seven-source set provides usable publication timestamps for the implemented policy.

No collection-window tolerance change was justified.

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
- Real-source metadata remains usable after collection and normalisation.

### Current Status

**Implemented and real-source validated**

Across the seven validated real feeds:

- titles were usable;
- article URLs were usable;
- publication timestamps were usable in the observed sample;
- source identifiers were preserved;
- retrieval timestamps were recorded.

Descriptions may legitimately be missing.

Phase 2 observed:

- all ECB entries in the compatibility sample lacking descriptions;
- all Sifted entries in the compatibility sample lacking descriptions;
- some OpenAI entries lacking descriptions.

Missing descriptions did not block processing.

---

## FR-2.4 — Bounded Remote Collection

**Priority:** MUST

Remote source collection must not be able to wait indefinitely.

Remote requests should use clear, normal public HTTP behaviour and should not weaken standard transport security.

### Acceptance Criteria

- Remote requests use an explicit bounded timeout.
- Requests use an identifiable User-Agent where appropriate.
- Ordinary HTTP and network failures are converted into visible source failures.
- Standard SSL verification remains enabled.
- A failed remote source does not automatically terminate unrelated successful sources.
- The solution does not require a paid HTTP or automation service.

### Current Status

**Implemented and real-source validated**

Current behaviour:

- 10-second remote request timeout;
- explicit User-Agent;
- explicit Accept header;
- normal SSL certificate verification;
- ordinary redirect behaviour;
- HTTP/network/timeout errors converted into `CollectionError`.

The real-source set successfully collected through this behaviour.

No retry logic is currently implemented because Phase 2 did not demonstrate a material need.

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

### Acceptance Criteria

- The same logical fields are represented consistently.
- Required fields are validated before later processing.
- Derived metadata remains distinguishable from source-provided metadata.

### Current Status

**Implemented, tested and real-source exercised**

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

**Implemented and real-source validated**

All observed entries returned by the seven selected real feeds during compatibility validation provided usable parsed publication timestamps.

No timestamp fallback mechanism was required.

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

- Obvious tracking variations do not create separate normalised URLs where current rules recognise them.
- The system does not invent a replacement URL.
- The original publisher URL remains available.
- The final report contains a usable direct link.

### Current Status

**Implemented and tested**

The current normaliser removes selected tracking parameters and fragments while preserving the original article URL separately.

Phase 2 real output showed that some publisher-specific BBC parameters such as `at_medium` and `at_campaign` remain.

This is a known lower-priority limitation and is not currently blocking the MVP.

---

## FR-3.4 — Invalid Record Handling

**Priority:** MUST

Malformed or incomplete records must be handled without corrupting the complete run.

### Acceptance Criteria

- Invalid records are separated according to explicit rules.
- The reason for invalidity is inspectable.
- One malformed item does not automatically stop unrelated valid items where the implemented processing boundary supports isolation.
- Validation results distinguish valid and invalid records.

### Current Status

**Implemented and tested at the validation layer**

All observed entries returned by the seven selected feeds during Phase 2 compatibility validation normalised successfully.

No real-source evidence justified broader per-entry `NormalizationError` isolation.

The current orchestration limitation remains visible:

- an unexpected per-entry normalisation exception is not yet broadly isolated after a source collection succeeds.

This should change only if a real source exposes the problem and a regression test can reproduce it.

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

**Implemented, tested and exercised with real-source runs**

Current order:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

Real Phase 2 runs observed and removed exact duplicates.

---

## FR-4.2 — Similar Story Detection

**Priority:** SHOULD

The system may later identify likely duplicate or closely related items with materially similar titles when repeated real reports demonstrate that exact deduplication is insufficient.

### Acceptance Criteria

If implemented:

- the method must remain deterministic or otherwise fully inspectable;
- similarity thresholds must be documented;
- uncertain stories must not be silently discarded;
- false merging must be evaluated explicitly.

### Current Status

**Deferred pending production evidence**

Phase 2 did not justify near-duplicate detection.

The current report became useful without it.

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

**Deferred pending production evidence**

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
- The configured taxonomy can remain narrower than the complete target taxonomy.

### Current Status

**Implemented and real-source validated**

Current active implemented domains:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Companies and Corporate Strategy;
- Artificial Intelligence;
- Technology and Software;
- Startups and Venture Capital;
- Europe and the European Union.

The full target taxonomy remains defined in `03 Information Taxonomy and Source Policy.md`.

The following target domains remain deferred:

- Financial Markets;
- Italy;
- Milan and Bocconi Ecosystem.

The seven-domain implementation is sufficient for the current automation milestone.

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
- Source-wide defaults are not used where they systematically misclassify broad feeds.

### Current Status

**Implemented, tested and refined from real report evidence**

Current keyword matching is:

- case-insensitive;
- word-boundary protected;
- deterministic.

Phase 2 showed that broad source defaults created misleading classifications and inflated relevance scores.

The source-default policy was therefore tightened.

Broad feeds may use:

```yaml
default_domains: []
```

The Global Politics keyword list was also expanded conservatively after testing candidate terms against real processed records.

The evidence-based additions were:

- `war`;
- `conflict`;
- `parliament`.

Broader candidates such as `government`, `defence`, `president` and `prime minister` were tested and not added because they produced ambiguous or low-value matches.

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

**Implemented and real-source validated**

Current policy:

- unclassified records remain processed;
- they are omitted from the main Markdown report by default.

Phase 2 confirmed that this conservative policy is preferable to forcing broad feeds into weak source-default classifications.

---

# 6. Relevance Ranking

## FR-6.1 — Transparent Relevance Score

**Priority:** MUST

The system must calculate a deterministic relevance score for eligible items.

The current formula is intentionally provisional.

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

**Implemented, tested and real-source exercised**

Phase 2 demonstrated that poor classification evidence can inflate ranking even when the formula itself is behaving correctly.

The source-default issue was therefore corrected upstream rather than by prematurely changing score weights.

The formula should be revised only if repeated production reports demonstrate systematic ranking problems.

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

**Implemented and real-report validated**

Current configured defaults:

- maximum 5 items per domain;
- maximum 30 items overall.

Phase 2 real reports remained below the configured global maximum after conservative classification.

These limits should remain unchanged until repeated automated use demonstrates a problem.

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

**Locally implemented, tested and real-output validated**

Current format:

- JSON Lines.

Current target-file behaviour:

- deterministic overwrite.

Real JSONL output was generated and manually inspected during Phase 2.

Automated production persistence is not yet implemented.

Manual Phase 2 runtime artifacts were removed after validation rather than automatically treated as permanent repository history.

---

## FR-7.2 — Historical Daily Reports

**Priority:** MUST

The system must preserve dated daily reports in production.

### Acceptance Criteria

- Each production report has a date-based repository location.
- Previous production reports are not unintentionally overwritten.
- The archive can be browsed without running code.
- Automated production persistence has clear success and failure semantics.

### Current Status

**Path model and local generation validated; automated historical persistence pending**

The CLI currently targets:

```text
reports/daily/YYYY/MM/YYYY-MM-DD.md
```

Real Markdown reports were generated and inspected during Phase 2.

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

**Implemented, tested and real-output validated**

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

**Implemented, integration-tested and validated on real runs**

---

## FR-8.3 — Domain Sections

**Priority:** MUST

Displayed items must be grouped into domain sections.

### Acceptance Criteria

- Only domains containing selected records need to be displayed.
- Cross-domain items are not repeated excessively.
- Section placement is deterministic.
- Misleading source-wide classification should not be used merely to populate sections.

### Current Status

**Implemented and real-report validated**

Current policy:

- one primary section per story;
- secondary domains shown as metadata.

Phase 2 report review confirmed that empty sections are preferable to forcing irrelevant stories into a domain.

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

**Implemented and validated for current fields**

Current maximum description length:

- 300 characters.

Relevance score is displayed.

Descriptions remain optional.

Real Phase 2 reports rendered correctly when source descriptions were absent.

---

## FR-8.5 — Failure Notice

**Priority:** MUST

Incomplete or degraded runs must be visible in the report.

### Acceptance Criteria

- Degraded status is explicit.
- Warnings identify failed sources or equivalent operational problems.
- The report does not present a degraded run as fully successful.

### Current Status

**Implemented and validated with real degraded execution**

The deliberate Phase 2 degraded-source run produced:

- `degraded` status;
- visible failed-source warning;
- successful valid-source content in the same report.

---

# 9. Automation and Delivery

## FR-9.1 — GitHub Actions Execution

**Priority:** MUST

The production workflow must run through GitHub Actions or an equally zero-cost approved repository-native mechanism.

### Acceptance Criteria

- The workflow file is version-controlled.
- It supports manual execution.
- It supports scheduled execution after manual validation.
- It does not call paid AI services.
- It has an explicit timeout.
- It uses minimum required permissions.
- The workflow invokes the same validated deterministic pipeline rather than creating a separate processing path.

### Current Status

**Pending — next active implementation requirement**

Phase 2 real-source readiness is complete.

The next product-development step is:

```text
workflow_dispatch
→ manual GitHub Actions validation
→ output and commit inspection
→ scheduled execution only after successful validation
```

---

## FR-9.2 — Automated Persistence

**Priority:** MUST

Successful production runs must automatically preserve intended outputs.

### Acceptance Criteria

- The user is not required to download and re-upload reports.
- Generated changes are committed or otherwise persisted through the approved workflow.
- No-change runs do not create unnecessary commits.
- Invalid outputs are not published as successful production results.
- Persistence behaviour remains understandable from the repository history.

### Current Status

**Pending**

Local production-shaped paths and outputs are validated.

Automated repository persistence has not yet been implemented.

---

## FR-9.3 — Failure Visibility

**Priority:** MUST

The user must be able to detect failed production runs.

### Acceptance Criteria

- Failed automation runs are visible.
- Relevant logs identify the failing stage.
- A failed workflow does not create a falsely successful report.
- Degraded runs remain distinguishable from failed runs.
- Source-level degradation does not automatically erase useful successful-source output.

### Current Status

**Implemented at pipeline/report/run-summary level; GitHub Actions behaviour pending**

Local and real-network degraded behaviour is validated.

Production workflow failure and publication semantics remain to be implemented.

---

## FR-9.4 — Daily GitHub Issue

**Priority:** COULD

The system may create a daily GitHub issue as an additional delivery channel after the core pipeline has been validated in real use.

### Current Status

**Deferred**

Repository-native Markdown reports should be used first.

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

**Implemented, tested and real-source validated**

Current statuses:

- `success`;
- `empty`;
- `failed`.

Phase 2 real-source runs successfully tracked seven active feeds.

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

**Implemented and tested**

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
- Source support should not expand merely to preserve a poor feed.

### Current Status

**Configuration and real-source review process partially validated**

Phase 2 demonstrated:

- seven real sources can be maintained through configuration;
- source-default quality can be reviewed without changing core collection logic;
- poor classification evidence can be corrected through configuration;
- network special handling should remain minimal.

A longitudinal production maintenance process remains pending repeated automated runs.

---

# Non-Functional Requirements

# 1. Cost

## NFR-1.1

Recurring monetary cost must remain zero.

**Status:** Satisfied by current architecture and Phase 2 real-source implementation.

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

**Status:** Pending GitHub Actions and scheduled execution.

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

**Current evidence:** the seven-source real pipeline runs comfortably in local development and does not currently require paid infrastructure.

## NFR-3.2

The system should avoid unnecessary repeated downloads and processing where practical.

The current design performs one feed request per active source per run.

## NFR-3.3

Production automation must use an explicit execution timeout.

**Status:** Pending GitHub Actions.

## NFR-3.4

Individual remote source requests must be bounded.

**Status:** Implemented.

Current remote request timeout:

- 10 seconds.

---

# 4. Reliability

## NFR-4.1

One source failure should not automatically invalidate successful source results.

**Status:** Implemented and validated with fixtures and real network behaviour.

## NFR-4.2

A failure in a critical processing stage must prevent false success.

**Status:** Partially implemented locally; GitHub publication behaviour still pending.

## NFR-4.3

Repeated runs should not create uncontrolled duplicate records or reports.

**Status:** Locally validated for target-file writes, exact duplicate reduction and deterministic report generation.

## NFR-4.4

The system should behave predictably when no eligible stories are found.

**Status:** Implemented and tested.

The current report explicitly states when no classified items were selected.

## NFR-4.5

Remote collection should fail visibly rather than hanging indefinitely.

**Status:** Implemented and real-source validated.

---

# 5. Maintainability

## NFR-5.1

Configuration should be separated from core processing logic where appropriate.

**Status:** Implemented.

## NFR-5.2

Dependencies should remain limited and documented.

**Status:** Implemented.

Current core dependencies remain intentionally small.

Remote HTTP retrieval uses the Python standard library rather than introducing a new HTTP dependency.

## NFR-5.3

Files and modules should have clear responsibilities.

**Status:** Implemented in the current architecture.

## NFR-5.4

A future contributor should be able to understand how to add a source, run the project and inspect a failure.

**Status:** Partially satisfied.

Canonical project documentation has been reconciled with Phase 2.

GitHub Actions production-operation instructions remain to be added during Phase 3.

## NFR-5.5

Source-specific complexity should remain proportionate to source value.

**Status:** Established and exercised during Phase 2.

The preferred response to an unstable or low-value source is removal or replacement before disproportionate custom handling.

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

**Status:** Implemented locally and validated in a real degraded run.

## NFR-6.4

The system must distinguish feed-provided text from system-generated metadata.

**Status:** Implemented by architecture and report behaviour.

The system does not generate article summaries.

## NFR-6.5

Source-wide classification assumptions must remain visible in configuration.

**Status:** Implemented.

Broad sources may explicitly use no default domains.

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

The current seven-source registry requires no credentials.

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

**Current Status:** Satisfied by the current real-source implementation and retained as production constraints.

---

# 9. Usability

## NFR-9.1

The report should be scannable in approximately 10–15 minutes.

**Status:** Provisionally supported by Phase 2 real-report inspection; requires longitudinal production evaluation.

The final Phase 2 real report contained 11 displayed items and was judged useful enough to justify automation.

## NFR-9.2

The most relevant items should be easy to identify.

**Status:** Current deterministic ranking and bounded report support this, but repeated production evaluation is still required.

## NFR-9.3

The report should remain readable on normal GitHub desktop and mobile views.

**Status:** Markdown design supports this; production use should validate it.

## NFR-9.4

The report should not require understanding the underlying code.

**Status:** Satisfied by the current report design.

## NFR-9.5

The report should prefer a smaller credible output over a larger misleading one.

**Status:** Established through Phase 2 real-report evaluation.

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

## Real-Report Validation

Phase 2 validated report behaviour using the seven-source real registry.

The first production-like report exposed misleading source-default classification.

After conservative corrections:

- broad source defaults were removed;
- source-wide defaults were retained only for sufficiently narrow feeds;
- a small Global Politics keyword correction was added after simulation against real records.

The final Phase 2 validation report displayed 11 items across useful domain sections.

The report was considered useful enough to proceed to automation without further tuning from a single day of data.

---

# Current Product Decisions

The following decisions are resolved for the current MVP implementation.

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
- preserves records for later taxonomy evaluation;
- Phase 2 demonstrated that under-classification is preferable to broad misleading defaults.

---

## Multi-Domain Items

**Decision:** appear once under one primary domain.

Secondary domains are displayed as metadata.

Rationale:

- reduces repetition;
- preserves cross-domain information.

---

## Source Defaults

**Decision:** source defaults are optional classification evidence, not publisher categories.

Broad sources may use:

```yaml
default_domains: []
```

Rationale:

- broad defaults created real false-positive classifications;
- assigned domains also affect ranking score;
- source identity alone does not guarantee item-level relevance.

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

Phase 2 did not demonstrate a need to change the current tolerance.

---

## Missing Publication Timestamp

**Current behaviour:** structurally valid records with `published_at=None` are excluded from collection-window eligibility.

Phase 2 real-source validation did not expose a problem with this policy.

---

## Remote Request Timeout

**Decision:** individual remote feed requests use a 10-second timeout.

Rationale:

- production collection must not hang indefinitely;
- the value worked with the current seven-source real registry.

---

## Remote User-Agent

**Decision:** remote collection uses an explicit User-Agent.

Rationale:

- real-source testing showed that some valid feeds rejected the previous bare request behaviour.

---

## Retry Behaviour

**Decision:** no retry logic is currently implemented.

Rationale:

- the current real-source set did not demonstrate sufficient transient-failure evidence to justify the additional complexity.

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

## Real-Source Set

**Decision:** use the current seven-source registry for the first automation phase.

Do not expand merely because additional feeds are available.

Rationale:

- the set is large enough to expose real network, metadata and classification behaviour;
- it remains small enough for manual quality inspection;
- further expansion should be driven by demonstrated coverage gaps.

---

# Remaining Open Product Decisions

The following remain unresolved by design.

## Production Execution Time

Choose only after manual GitHub Actions execution is validated and scheduling is being implemented.

## GitHub Actions Commit Behaviour

Determine:

- when outputs should be committed;
- how no-change runs avoid empty commits;
- how critical failures prevent invalid publication;
- how degraded but usable runs should be handled.

## GitHub Actions Permissions

Use the minimum repository permissions required for validated output persistence.

## GitHub Actions Timeout

Set an explicit workflow-level execution timeout.

## Scheduled Execution

Enable only after `workflow_dispatch` works reliably.

## Production Persistence Policy

Determine the exact automated repository persistence behaviour during Phase 3.

Manual Phase 2 runtime artifacts were deliberately removed after validation.

## Missing Publication Timestamp Policy

Revisit only if useful future sources frequently omit publication timestamps.

## Collection-Window Tolerance

Current default is 24 hours.

Reconsider only if repeated automated source timing creates systematic missed stories.

## Near-Duplicate Detection

Implement only if exact deduplication leaves material repeated coverage.

## Multi-Source Coverage Indicator

Add only if clustering becomes useful.

## Financial Markets Domain

Implement only if repeated production reports demonstrate a meaningful coverage gap.

## Italy Domain

Implement only if topic classification plus source geography proves insufficient.

## Milan and Bocconi Domain

Implement only when a suitable structured public source or validated workflow exists.

## Opportunity-Specific Report Section

Remain part of future taxonomy/report evaluation rather than current core behaviour.

## Publisher Concentration Controls

Evaluate during repeated production use before adding ranking penalties or quotas.

## Ranking Weights

Change only when repeated reports demonstrate systematic ordering problems.

## Retry Behaviour

Reconsider only if repeated automated runs demonstrate meaningful transient source failures.

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
- remote requests remain bounded;
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
- invalid critical output is not published as successful;
- degraded source-level failure does not automatically erase valid successful-source output;
- no-change automation runs do not create unnecessary commits.

---

# Phase 2 Acceptance Status

The following parts of the production MVP acceptance scenario are now validated locally with real structured sources:

- configuration loading;
- seven-source public RSS registry;
- public source access without credentials;
- bounded remote requests;
- explicit User-Agent behaviour;
- normal SSL verification;
- real source collection;
- structured source outcomes;
- real-network partial source failure;
- record normalisation;
- metadata validation;
- publication-window filtering;
- exact deduplication;
- seven-domain classification;
- conservative unclassified behaviour;
- deterministic ranking;
- JSONL generation;
- Markdown generation;
- run-summary JSON;
- degraded warnings;
- deterministic report limits;
- real report-quality inspection;
- local CLI execution;
- run-level logging;
- full automated test suite.

At Phase 2 closeout:

> **110 tests pass.**

The following remain required before full production MVP acceptance:

- GitHub Actions execution;
- manual `workflow_dispatch` validation;
- automated repository persistence;
- production commit behaviour;
- production failure/publication behaviour;
- scheduled daily execution;
- initial longitudinal production-use evaluation.

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
- Was the seven-source universe too narrow or unnecessarily broad?
- Do any of the three deferred target domains need implementation?

## Noise

- Were low-value stories frequently included?
- Was promotional content overrepresented?
- Did exact duplicate reduction work adequately?
- Did repeated coverage justify near-duplicate logic?
- Did any source default create systematic false positives?

## Classification

- Were items placed in useful domains?
- Were too many relevant items unclassified?
- Were secondary-domain tags useful?
- Did the seven-domain taxonomy provide enough practical coverage?
- Did any keyword create repeated false positives?

## Ranking

- Did high-value developments appear near the top?
- Did source-tier scoring overwhelm actual relevance?
- Did keyword matches inflate weak items?
- Did domain count inflate weak items?
- Should ranking weights be changed?

## Operations

- Did scheduled runs complete reliably?
- Were source failures visible?
- Was maintenance acceptably low?
- Did any source require disproportionate support?
- Were degraded runs still useful?
- Did no-change runs avoid unnecessary commits?
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

## Implemented and Validated

- FR-1.1 — Configurable Source Registry
- FR-1.2 — Public Structured Sources
- FR-1.3 — Partial Source Failure
- FR-2.2 — Configurable Collection Window
- FR-2.3 — Metadata Retrieval
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
- FR-10.3 — Longitudinal Source Maintenance

## Deferred Pending Evidence

- FR-4.2 — Similar Story Detection
- FR-4.3 — Multi-Source Coverage
- FR-9.4 — Daily GitHub Issue
- FR-9.5 — GitHub Pages

---

# Current Status

**Status:** Product requirements reconciled with completed Phase 2 real-source validation

**Phase 2 requirements status:**

- deterministic local vertical slice complete;
- seven-source real public RSS registry validated;
- network request hardening complete;
- real metadata and timestamp behaviour validated;
- exact deduplication exercised on real data;
- seven-domain taxonomy operational;
- source-default classification corrected from real report evidence;
- conservative keyword refinement completed;
- real report generation and quality review completed;
- degraded real-network source failure validated;
- operational report behaviour complete;
- local observability complete;
- 110 tests passing.

**Production MVP still requires:**

- GitHub Actions;
- manual `workflow_dispatch` validation;
- automated persistence;
- production commit and publication behaviour;
- scheduled execution;
- repeated production-use evaluation.

**Next product-development focus:**

> Run the validated real-source pipeline through the smallest safe GitHub Actions `workflow_dispatch` workflow, validate outputs and persistence, and only then enable scheduled execution.

---

# Changelog

## 2026-08-11 — Phase 2 Requirements Reconciliation

- Reconciled product requirements with the validated seven-source real-source implementation.
- Updated FR-1.1 to reflect the active seven-source configurable registry and optional empty default domains.
- Updated FR-1.2 to reflect successful public real-source RSS validation.
- Updated FR-1.3 to include deliberate real-network degraded-source validation.
- Added FR-2.4 for bounded remote collection because this became a concrete production requirement during real-source testing.
- Recorded the implemented 10-second remote timeout and explicit User-Agent requirement.
- Recorded that normal SSL verification remains enabled.
- Updated metadata and timestamp requirements with real-source evidence.
- Recorded the seven implemented active domains.
- Recorded conservative source-default behaviour and evidence-based classification refinement.
- Recorded real exact-deduplication behaviour.
- Updated report requirements with real-output validation.
- Recorded the current seven-source production-like set as sufficient for the automation phase.
- Updated source-maintenance requirements with Phase 2 evidence.
- Updated non-functional reliability and maintainability requirements for real networking.
- Replaced Phase 1 acceptance status with Phase 2 real-source acceptance status.
- Updated the requirement-status summary from local-only validation to real-source validation where justified.
- Recorded 110 passing automated tests.
- Made GitHub Actions `workflow_dispatch` the next active product requirement.
- Preserved scheduled execution and automated persistence as production MVP requirements.
- Kept near-duplicate logic, multi-source clustering and delivery features deferred pending evidence.

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
````
