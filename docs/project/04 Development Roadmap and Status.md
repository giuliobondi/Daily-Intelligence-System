# Daily Intelligence System — Development Roadmap and Status

> **Purpose**
>
> This document controls the implementation of the Daily Intelligence System.
>
> It records the current phase, completed decisions, active milestone, blockers, deferred work and next highest-priority action.
>
> It is not a long-term product vision document and should not duplicate the Project Brief, Product Requirements, System Architecture or Information Taxonomy and Source Policy.
>
> ---
>
> **Primary Question**
>
> > *What should be built now, what has already been completed, and what is the next highest-value step?*
>
> ---
>
> **Update Frequency**
>
> Update whenever the active milestone, project status, blocker or implementation priority changes.

---

# Roadmap Principles

Development should follow these rules:

- Build one complete vertical slice before expanding scope.
- Start from the user need and workflow, not from a preferred technology.
- Prefer working output over additional infrastructure.
- Do not create features without a validated need.
- Prefer the simplest solution that satisfies the requirement.
- Do not add recurring monetary cost.
- Do not introduce production AI calls or recurring AI-credit consumption.
- Keep daily manual work negligible.
- Prefer RSS, official APIs and other structured public sources before scraping.
- Prefer deterministic rules before machine learning or LLM-based logic.
- Use public or explicitly permitted source material in the automated pipeline.
- Do not treat personal or institutional reading access as permission for automated ingestion.
- Validate locally before changing production automation where practical.
- Use Git and tests as the verification layer for every material change.
- Keep the repository public-safe.
- Stop at stable checkpoints.
- Treat technically successful execution as insufficient if the report is noisy, repetitive, misleading, inaccessible, too sparse or too thin to understand without unnecessary click-through.

The project should not move to the next phase until the current phase has a clear completion condition or there is evidence that a different immediate priority creates materially more user value.

---

# Current Project Status

| Field | Current Status |
|---|---|
| Project Phase | Phase 3 complete — entering evidence-driven information-quality improvement |
| Current Milestone | Milestone 4 — Correct and expand the source and domain universe |
| Repository Status | Public Python repository with automated GitHub-native daily execution and repository-native historical outputs |
| Implementation Status | Deterministic collect → normalize → validate → filter → deduplicate → classify → rank → store → report pipeline implemented and production-validated |
| Automation Status | GitHub Actions implemented; manual and scheduled execution validated; outputs persisted automatically |
| Production Schedule | Daily at 06:05 Europe/Rome; GitHub scheduling latency remains an observed operational limitation |
| Source Registry | Seven active production sources pending immediate quality/accessibility review |
| Taxonomy Status | Seven implemented domains; Financial Markets, Italy, and Milan/Bocconi remain candidate expansion domains |
| Testing Status | 110 automated tests passing |
| Current Product-Quality Findings | Current reports can be too thin, some linked articles may be inaccessible, source concentration can be high, and scheduler latency can shift the rolling 24-hour window |
| Current Blockers | No automation blocker; information-source quality and report usefulness are now the active constraints |
| Current Priority | Review, correct and expand sources and domains, beginning with accessibility and metadata-richness problems exposed by Sifted |

---

# Completed Work

## Project Decisions

The following decisions are established unless explicitly changed later:

- Use a hybrid information model:
  - ChatGPT provides independent interpretation, planning and synthesis outside the production pipeline.
  - GitHub and Python provide deterministic collection, organisation, ranking, reporting and archiving.
- Zero recurring monetary cost is a hard constraint.
- Daily manual work should be negligible.
- Production must not consume GitHub AI, Copilot or other recurring AI credits.
- Public structured sources are the default automated input class.
- RSS and Atom are the first supported automated source types.
- Production automation uses ordinary Python and GitHub Actions.
- The core system does not depend on LLM calls, agents, RAG, embeddings, vector databases or paid APIs.
- The repository remains public.
- Private Career OS materials remain outside the repository.
- Bocconi institutional credentials and other private credentials must never be embedded in the production pipeline.
- Personal or institutional access to a publication does not automatically make that publication eligible for automated ingestion.
- Processed records use JSON Lines.
- Run summaries use JSON.
- Daily reports use Markdown.
- Internal timestamps use timezone-aware UTC datetimes.
- Reports use one primary placement per item, with secondary domains shown as metadata.
- Relevance scoring is deterministic and explainable.
- Repository-native persistence is the current production delivery model.
- GitHub Issues, GitHub Pages and other interface layers remain optional and deferred.
- Broad heterogeneous feeds may use no default domain rather than forcing every item into a misleading classification.
- Source defaults should represent a genuine source-wide topical guarantee rather than a broad publisher category.
- Unclassified records are preferable to misleading classifications.
- Retry logic should not be added without evidence that current bounded single-attempt collection is insufficient.
- A technically compatible source is not automatically a good production source.
- Production source quality must consider both automation suitability and end-user usefulness.
- A source that frequently links to inaccessible content or exposes too little public context may be replaced rather than supported with increasingly complex logic.
- Report quality must be evaluated independently from technical run success.

## Repository and Package Setup

Completed repository foundations include:

- public GitHub repository;
- `README.md`;
- `.gitignore`;
- `LICENSE`;
- `pyproject.toml`;
- `config/`;
- `src/daily_intelligence/`;
- `tests/` and controlled fixtures;
- `docs/project/` for canonical project documentation;
- `.github/workflows/daily-intelligence.yml` for production automation;
- repository-native `data/` and `reports/` production history.

The Python package uses a `src/` layout and requires Python 3.12 or later.

## Implemented Processing Modules

The processing core includes:

```text
src/daily_intelligence/
├── __init__.py
├── cli.py
├── classify.py
├── collect.py
├── config.py
├── deduplicate.py
├── filter_window.py
├── models.py
├── normalize.py
├── pipeline.py
├── rank.py
├── report.py
├── run_summary.py
├── storage.py
└── validate.py
```

The exact repository tree remains the source of truth if file names later change.

---

# Development Phases

---

# Phase 0 — Definition and Repository Setup

## Objective

Create the minimum project definition required to begin implementation without major ambiguity.

## Scope

- define project purpose;
- define product behaviour;
- define information taxonomy and source policy;
- define system architecture;
- define implementation roadmap;
- establish repository structure;
- make hard constraints explicit;
- separate current requirements from deferred ideas.

## Completion Criteria

Phase 0 is complete when:

- documents `00` through `04` are internally consistent enough to guide implementation;
- no major contradiction blocks the local slice;
- unresolved decisions are explicitly visible;
- the MVP boundary is clear;
- the next implementation milestone is defined;
- repository foundations exist.

## Status

**Complete**

## Completion Notes

Phase 0 established the initial product, architecture, information policy and implementation sequence.

The canonical documents are updated as implementation changes rather than being treated as immutable historical snapshots.

---

# Phase 1 — Local Vertical Slice

## Objective

Build the smallest complete local pipeline that proves the core workflow from collection to readable output.

## Implemented Scope

Phase 1 implemented and validated:

1. configuration loading;
2. RSS/Atom collection from controlled inputs;
3. structured source-level collection results;
4. record normalisation;
5. required-field validation;
6. deterministic collection-window filtering;
7. exact duplicate reduction;
8. simple deterministic domain classification;
9. provisional deterministic relevance scoring;
10. JSON Lines persistence;
11. deterministic Markdown report selection and rendering;
12. structured JSON run summaries;
13. end-to-end local orchestration;
14. one-command CLI execution;
15. source-level failure isolation and degraded-run behaviour;
16. user-facing operational report metadata and warnings;
17. minimal standard-library run-level logging;
18. automated tests for critical deterministic logic and integration paths.

## Local Execution

The pipeline can be run locally with:

```text
python -m daily_intelligence.cli run
```

The CLI constructs repository-default output paths and a previous-24-hours collection window.

## Phase 1 Controlled Configuration

Phase 1 intentionally used:

- one fixture/sample source;
- Technology and Software domain;
- Artificial Intelligence domain;
- deterministic ranking weights;
- configurable report limits.

That setup existed to validate pipeline behaviour before introducing real network and information-quality uncertainty.

## Key Implemented Behaviour

### Collection

Each source returns a structured result with status:

- `success`;
- `empty`;
- `failed`.

Expected source-level failures are isolated so one bad source does not discard successful source results.

### Normalisation and Identity

Records preserve useful source metadata while normalising titles, URLs and timestamps.

Record identity is deterministic from source identity and normalised URL.

### Validation

Invalid records are separated visibly from valid records before later processing.

### Collection Window

The reporting window is enforced rather than recorded only as metadata.

Current behaviour:

- requires timezone-aware window boundaries;
- uses inclusive boundaries;
- excludes records published before or after the window;
- excludes records without a confirmed publication timestamp;
- rejects reversed windows.

### Deduplication

Current exact duplicate handling uses:

1. normalised URL;
2. normalised title.

The first deterministic occurrence is retained.

### Classification

Classification uses source defaults plus deterministic keyword matching with word-boundary protection.

Multiple domains are allowed.

Unclassified records remain valid processed records but are omitted from the main report.

### Ranking

The current provisional score is deterministic and based on:

- configured source tier;
- number of domain matches;
- number of keyword matches.

Score components are stored for transparency.

### Storage and Reporting

Processed records are written as JSON Lines using deterministic overwrite semantics for a target file.

The Markdown report:

- applies deterministic selection;
- respects total and per-domain limits;
- places each item once under a primary domain;
- shows secondary domains as metadata;
- shows relevance score;
- uses only feed-provided descriptions;
- truncates descriptions to configuration limits;
- omits unclassified records from the main report;
- exposes run status, monitored window, source health, collected count and displayed count;
- exposes warnings on degraded runs.

### Run Summary and Logging

Each run produces a structured JSON summary containing operational counts, status, warnings and monitored window.

The pipeline emits lightweight standard-library logs for:

- pipeline start;
- source outcomes;
- validation counts;
- collection-window retention;
- duplicate counts;
- classification/ranking counts;
- output paths;
- final run status.

## Phase 1 Validation Completed

Phase 1 was validated through:

- unit tests for deterministic modules;
- controlled feed fixture tests;
- end-to-end pipeline integration tests;
- degraded source integration testing;
- collection-window boundary and exclusion tests;
- report-selection and operational-header tests;
- CLI invocation tests;
- logging tests;
- manual one-command CLI runs;
- generated JSONL inspection;
- generated Markdown inspection;
- run-summary inspection;
- repeated full-suite execution.

At Phase 1 closeout:

> **104 tests passed.**

A manual CLI run also exposed a real gap: the original pipeline recorded a collection window without enforcing it.

The missing filter was implemented, regression-tested and revalidated through the CLI.

This established the development pattern used in later phases:

> real output should drive the next justified change.

## Status

**Complete**

---

# Phase 2 — Minimal Real-Source Production Readiness

## Objective

Validate the local pipeline against a deliberately small real public source set before adding automation or speculative quality features.

The purpose was to discover real source, metadata, network and report-quality problems using the smallest useful production-like input set.

## Implemented Real-Source Set

The validated active registry contains seven public RSS sources:

1. BBC News World;
2. BBC News Business;
3. European Central Bank;
4. European Commission Highlighted News;
5. Istat Press Releases;
6. OpenAI News;
7. Sifted.

The source set was intentionally small enough to remain inspectable during initial production-readiness work.

The set is no longer considered final.

Production use has now provided enough evidence to begin a structured source review and expansion.

## Implemented Taxonomy

The implemented taxonomy contains seven active domains:

1. Global Politics and Geopolitics;
2. Economics and Macroeconomics;
3. Companies and Corporate Strategy;
4. Artificial Intelligence;
5. Technology and Software;
6. Startups and Venture Capital;
7. Europe and the European Union.

The target taxonomy remains broader than the implemented subset.

The following target domains remain candidate additions:

- Financial Markets;
- Italy;
- Milan and Bocconi ecosystem.

These should be reconsidered during the next source/domain strategy phase rather than added automatically.

## Network Production-Readiness Changes

Real-source testing exposed two concrete collector requirements:

- remote requests needed a bounded timeout;
- some feeds required an explicit User-Agent.

The collector was therefore hardened using ordinary Python standard-library networking.

Current remote collection behaviour:

```text
remote feed URL
→ urllib Request
→ explicit User-Agent and Accept headers
→ 10-second timeout
→ response bytes
→ feedparser
```

Expected HTTP, URL and timeout failures are converted into `CollectionError`.

Source-level failures remain isolated by `collect_source`.

Normal SSL certificate verification remains enabled.

No SSL bypass was introduced.

No new third-party HTTP dependency was added.

No retry policy was added because real-source testing did not demonstrate a current need for one.

## Real-Source Compatibility Validation

All seven selected feeds were collected successfully through the actual project collector during Phase 2.

Observed feed sizes included:

- BBC World — approximately two dozen entries;
- BBC Business — approximately five dozen entries;
- ECB — 15 entries;
- European Commission — 30 entries;
- Istat — 10 entries;
- OpenAI — more than one thousand entries;
- Sifted — approximately two dozen entries.

The large OpenAI feed did not create a blocker because collection-window filtering reduces the eligible record set after validation.

All returned entries from the seven feeds during the compatibility test normalised successfully.

No missing publication timestamps were observed in the tested entries.

Missing descriptions occurred for some feeds and entries but were valid under the original optional-description model.

That model is now under product review because real production use showed that thin descriptions can materially reduce report usefulness.

## Source-Default Classification Correction

The first full real-source report exposed misleading classification caused by overly broad source defaults.

Examples included:

- unrelated BBC Business items being forced into Economics and Macroeconomics;
- an ECB concert announcement being classified as Economics and Europe/EU;
- relevance scores being inflated by domains assigned solely from broad publisher defaults.

The smallest correction was to make `default_domains` explicitly optional.

Broad sources may use:

```yaml
default_domains: []
```

Current default-domain policy:

- BBC News World → no default domain;
- BBC News Business → no default domain;
- European Central Bank → no default domain;
- European Commission Highlighted News → no default domain;
- Istat Press Releases → Economics and Macroeconomics;
- OpenAI News → Artificial Intelligence;
- Sifted → Startups and Venture Capital.

This policy reflects the rule:

> A source default should represent a genuine source-wide topical guarantee, not merely the general category of the publisher.

`geographic_scope` remains required and non-empty.

Domain keyword lists remain required and non-empty.

## Evidence-Based Keyword Adjustment

Removing broad source defaults improved precision but exposed a recall gap in Global Politics and Geopolitics.

Real in-window BBC World items were manually reviewed.

Candidate keywords were simulated against the actual processed sample before configuration was changed.

The following keywords were added because they recovered clearly relevant political or geopolitical stories without observed false positives in the sample:

- `war`;
- `conflict`;
- `parliament`.

Several broader candidates were tested but deliberately not added, including:

- `government`;
- `defence`;
- `president`;
- `prime minister`.

Those terms produced ambiguous or low-value matches in the observed sample.

This preserves the policy of preferring under-classification over noisy classification.

## Real Report Validation

The first production-like run succeeded technically but exposed classification noise.

The initial report displayed 15 items.

After removing inappropriate broad source defaults, the report became smaller and more credible, displaying 8 items.

After evidence-based Global Politics keyword additions, the report displayed 11 items across useful sections including:

- Global Politics and Geopolitics;
- Economics and Macroeconomics;
- Artificial Intelligence;
- Startups and Venture Capital.

This demonstrated that technical success alone is insufficient and that real report inspection should drive deterministic corrections.

The result was judged useful enough to justify moving to automation.

## Degraded Real-Source Validation

A controlled run was executed using:

- one valid real Istat source;
- one deliberately invalid remote source.

Observed behaviour:

- Istat collection succeeded;
- the invalid source failed with `CollectionError`;
- the overall run status became `degraded`;
- the failure appeared in structured warnings;
- the valid Istat record still reached the final report;
- successful-source output was preserved.

This confirmed real-network partial-source failure isolation rather than relying only on fixture tests.

## Phase 2 Validation Completed

Phase 2 validation included:

- direct live feed compatibility probing;
- hardened collector tests;
- real collection through the actual project collector;
- normalization of all returned entries from the seven selected feeds;
- repeated full-suite automated testing;
- real CLI execution;
- real JSONL inspection;
- real Markdown report inspection;
- real run-summary inspection;
- classification coverage review;
- simulated keyword evaluation against actual processed samples;
- deliberate degraded real-network execution;
- repeated report-quality comparison after deterministic corrections.

At Phase 2 closeout:

> **110 automated tests pass.**

## Completion Criteria

Phase 2 is complete because:

- a small real-source set can be collected manually and repeatedly;
- remote requests use an explicit bounded timeout;
- feeds that require a User-Agent collect successfully;
- normal SSL verification remains intact;
- source failures remain isolated and visible;
- publication timestamps behave adequately for the current reporting-window model;
- real metadata survives normalization;
- all tested real entries normalised successfully;
- real JSONL, Markdown and run-summary outputs were generated and inspected;
- report-quality problems were identified from real output;
- only small deterministic corrections justified by evidence were added;
- misleading broad source defaults were removed;
- conservative classification recall was improved with tested keywords;
- a deliberate real-network failure produced a usable degraded run;
- the full automated suite passes;
- zero recurring monetary cost remains intact;
- no production AI dependency was introduced.

## Status

**Complete**

---

# Phase 3 — GitHub Automation

## Objective

Run the validated real-source pipeline automatically in the public repository with zero recurring monetary cost and negligible daily manual work.

## Implemented Scope

Phase 3 implemented and validated:

- GitHub Actions workflow;
- manual `workflow_dispatch`;
- GitHub-hosted Ubuntu runner;
- Python 3.12 runtime;
- deterministic package installation;
- full automated test execution;
- production CLI execution;
- explicit workflow timeout;
- repository-write permission limited to the workflow's production persistence need;
- generated-output validation;
- visible application logs;
- coherent automated output commit;
- no-empty-commit guard;
- automated repository persistence;
- deliberate critical-failure validation;
- deliberate degraded-source validation;
- scheduled daily execution;
- concurrency protection;
- timezone-aware production schedule.

## Production Workflow

The production path is:

```text
workflow_dispatch or schedule
→ checkout repository
→ set up Python 3.12
→ install project and development dependencies
→ run 110 automated tests
→ run production CLI
→ validate generated outputs
→ stage production output directories
→ stop if no output changes exist
→ commit as github-actions[bot]
→ push generated outputs
```

The production workflow remains deterministic and does not use:

- paid APIs;
- paid automation services;
- OpenAI API credits;
- GitHub AI or Copilot credits;
- private credentials;
- cloud databases;
- external persistence services.

## Manual Workflow Validation

Manual Actions execution validated that:

- the workflow could be triggered from GitHub;
- dependencies installed successfully;
- 110 tests passed in the hosted runner;
- the production CLI executed successfully;
- all seven production sources were attempted;
- logs exposed source-level progress and final run status;
- JSONL, Markdown and run-summary outputs were generated in expected paths;
- generated files were inspectable.

A missing CLI logging configuration was discovered during the first Actions run because pipeline INFO logs were not visible.

The CLI was updated to configure standard-library logging.

The targeted tests and full suite were rerun successfully.

The subsequent Actions run displayed source collection, validation, filtering, deduplication, classification, output and final-status logs correctly.

## Automated Persistence Validation

The workflow was extended to:

- validate generated output paths;
- stage only production output directories;
- avoid empty commits;
- use the `github-actions[bot]` identity;
- commit changed outputs;
- push them to the executing branch.

A successful production run created one coherent bot commit containing:

- processed JSONL;
- run-summary JSON;
- daily Markdown report.

Repository-native production history is therefore operational.

## No-Change Validation

The commit guard was explicitly validated.

When no staged output differences exist:

```text
git diff --cached --quiet
```

causes the workflow persistence logic to exit without creating an empty commit.

No additional complexity was added for same-day reruns because legitimate timestamp and content changes may still produce real differences.

## Critical-Failure Validation

A temporary branch deliberately changed one source to an invalid configuration:

```yaml
geographic_scope: []
```

Observed behaviour:

- configuration validation failed;
- automated tests failed;
- the workflow returned a non-zero result;
- the production pipeline did not proceed to valid publication;
- no misleading successful output publication occurred.

This validated the distinction between critical configuration failure and recoverable source failure.

## Degraded-Source Validation

A temporary branch deliberately changed the BBC World feed URL to an invalid `.invalid` hostname while keeping the source configuration structurally valid.

Observed behaviour:

- 110 automated tests still passed;
- BBC World collection failed;
- the other six sources continued successfully;
- the pipeline completed with `status: degraded`;
- run-summary JSON recorded 7 active, 6 successful and 1 failed source;
- the warning identified `bbc_world`;
- the Markdown report visibly showed `Run status: degraded`;
- successful-source content remained available;
- the workflow itself completed successfully;
- degraded outputs were persisted by the bot.

This validated the intended production distinction:

> recoverable source failure should produce visible degraded intelligence, not suppress all usable output.

## Concurrency

Once both manual and scheduled execution existed, overlap protection became justified.

The production workflow uses one concurrency group and does not cancel an already-running production job.

This reduces the risk of simultaneous runs writing and pushing the same date-based output paths.

## Scheduled Execution

Scheduled execution was enabled only after manual workflow, persistence and failure semantics were validated.

The workflow uses a timezone-aware `Europe/Rome` schedule.

The production schedule is currently:

```text
06:05 Europe/Rome
```

The earlier target was moved earlier after real scheduled runs demonstrated substantial GitHub scheduling delay.

## Scheduler-Latency Observation

Scheduled execution is functional but not punctual.

Observed behaviour included scheduled runs beginning materially later than their configured cron time, including delays of more than two hours during controlled testing.

This is treated as an external GitHub scheduling limitation rather than a pipeline failure.

Moving the production trigger earlier creates delivery buffer but does not eliminate the underlying timing uncertainty.

## Reporting-Window Coupling

The current CLI defines the collection window relative to actual pipeline start time.

Therefore:

```text
late GitHub start
→ later 24-hour reporting window
→ potentially different eligible content
```

This means scheduling latency currently affects not only delivery time but also report composition.

A scheduled production report on 14 August was substantially shorter than the preceding reports while source collection remained technically healthy.

This is not yet sufficient evidence for an immediate architecture change, but it creates a validated design question:

> Should the reporting window remain anchored to actual execution time, or should it use a deterministic reporting cutoff independent of GitHub scheduler latency?

This issue should be considered during the upcoming product-quality design work.

## Phase 3 Validation Completed

Phase 3 validation included:

- manual `workflow_dispatch`;
- hosted-runner dependency installation;
- full 110-test execution in Actions;
- production seven-source run;
- operational log inspection;
- output path inspection;
- JSONL inspection;
- Markdown inspection;
- run-summary inspection;
- automated bot persistence;
- coherent commit inspection;
- no-change commit-guard validation;
- critical configuration failure;
- degraded source failure;
- preservation of successful-source content;
- scheduled execution;
- concurrency protection;
- confirmation that production remains zero-cost and does not consume AI credits.

## Completion Criteria

Phase 3 is complete because:

- manual Actions execution works;
- all dependencies install successfully;
- the full automated suite passes in Actions;
- production real feeds are attempted in Actions;
- outputs are generated and inspectable;
- application logs are visible;
- changed outputs create one coherent bot commit;
- unchanged outputs do not create empty commits;
- degraded source failure remains visible and usable;
- critical configuration failure blocks misleading publication;
- an explicit timeout is present;
- overlap protection is present;
- scheduled execution has been observed successfully;
- no credentials are exposed;
- no paid service is required;
- no recurring AI credits are consumed.

## Status

**Complete**

---

# Phase 4 — Source and Domain Correction / Expansion

## Objective

Correct weaknesses in the current seven-source baseline and expand the source and domain universe only where the resulting information product becomes materially more useful.

This phase is now the active priority.

## Why This Phase Is Now Justified

The original seven-source registry was sufficient to validate the pipeline and automation architecture.

Production use has now exposed concrete information-quality limitations.

### Sifted Accessibility Problem

At least one Sifted item selected into a production report linked to an article requiring Sifted Pro access.

This matters because:

- the automated system currently provides only limited feed-derived context;
- the user may therefore need to open the original article to understand the development;
- a paywalled destination can make the selected report item substantially less useful;
- Sifted feed metadata has also been observed to provide limited descriptive context for some entries.

Sifted should therefore be reviewed as a production source.

Its status should not be assumed to be either permanently retained or immediately removed.

The review should compare:

- topical value;
- public-feed richness;
- frequency of inaccessible linked articles;
- uniqueness of coverage;
- availability of better accessible alternatives;
- maintenance burden.

### Source Accessibility

Production source eligibility must now distinguish:

1. whether the system can legally and reliably ingest the source;
2. whether the resulting item is actually useful to the user.

A technically valid RSS feed may still be a weak production source if it repeatedly leads to inaccessible content and does not provide enough lawful context inside the feed itself.

### Bocconi Access

The user has substantial institutional access through Bocconi.

This creates a personal reading and research advantage but does not change automation rules.

The upcoming source review should distinguish:

- public web access;
- direct publisher access through Bocconi;
- SearchLib access;
- academic database access;
- access requiring an additional personal paid subscription.

Bocconi credentials must remain outside the production system.

Institutional access can improve the value of a source for manual follow-up but must not be treated as permission for automated scraping, systematic downloading or redistribution.

### Coverage and Domain Gaps

The current taxonomy still excludes target domains that may now be useful:

- Financial Markets;
- Italy;
- Milan and Bocconi ecosystem.

Production reports have also shown that some days can become highly concentrated in only a few sources or domains.

The next source/domain strategy should therefore reconsider:

- missing high-value coverage;
- excessive source concentration;
- weak or inaccessible sources;
- sources whose structured metadata is too thin;
- domains that are consistently underrepresented;
- domains that are strategically important but currently absent.

## Source/Domain Strategy Ownership

The Career Agent should first help define:

- desired information universe;
- priority domains;
- high-value publications;
- professional and career relevance;
- acceptable source mix.

This Development project should then evaluate candidate sources technically.

Technical evaluation should include:

- public structured access;
- RSS/Atom availability;
- official free API availability;
- metadata richness;
- timestamp reliability;
- description quality;
- automation permission;
- paywall/accessibility characteristics;
- expected maintenance;
- overlap with existing sources;
- source quality;
- compatibility with the public-repository model.

No source should be added to production merely because it is prestigious or personally accessible.

## Candidate Domain Review

The following domains should now be explicitly reconsidered:

- Financial Markets;
- Italy;
- Milan and Bocconi ecosystem.

Their implementation remains contingent on:

- demonstrated user value;
- suitable source availability;
- classification design;
- manageable noise;
- zero recurring cost.

## Completion Criteria

Phase 4 is complete when:

- current seven-source performance has been reviewed;
- Sifted has a deliberate keep/replace/remove decision;
- low-value or inaccessible sources have explicit decisions;
- the Career Agent source/domain strategy has been received;
- candidate sources have been technically evaluated;
- candidate domains have been assessed against available sources;
- the smallest justified source/domain corrections have been implemented;
- configuration tests pass;
- real-source collection remains reliable;
- generated reports are manually inspected;
- source concentration and accessibility improve or remain acceptably balanced;
- zero recurring cost and credential safety remain intact.

## Status

**Current active phase**

---

# Phase 5 — Richer-Report Product Design

## Objective

Design a report that provides enough lawful context for the user to understand key developments without requiring immediate click-through.

This phase should be deliberate and design-heavy before implementation begins.

## Validated Problem

The current report often contains:

- headline;
- source;
- timestamp;
- relevance score;
- optional secondary domain;
- short feed-provided description;
- source link.

This is useful for triage but can be too thin for daily intelligence.

The current workflow can therefore become:

```text
report
→ identify potentially relevant item
→ click source
→ read article to understand development
```

The desired workflow is closer to:

```text
report
→ understand the core development
→ open only selected sources for deeper reading
```

This is now a validated product requirement rather than a speculative feature.

## Design Questions

Before implementation, determine:

- what “enough context” means in practical terms;
- how much context should each item contain;
- how report length should remain bounded;
- which feed fields are available by source;
- which sources provide rich public summaries;
- which sources provide only titles or thin excerpts;
- when public article metadata can be used safely;
- whether any source-specific extraction is permitted and maintainable;
- what should happen when sufficient context is unavailable;
- whether inaccessible linked content should disqualify an item;
- how source attribution should be preserved;
- how copied source text should be limited;
- how copyright and licence boundaries should be enforced;
- whether the system should distinguish feed summary from system-generated context;
- how the new report quality should be objectively validated.

## Hard Boundaries

The design must preserve:

- zero recurring monetary cost;
- no production OpenAI API dependency;
- no recurring AI-credit use;
- no authenticated scraping of premium sources;
- no use of Bocconi credentials in GitHub Actions;
- no paywall bypass;
- no storage of restricted full article bodies;
- no substantial copyrighted reproduction in the public repository;
- source transparency;
- manageable report length;
- low maintenance.

## Preferred Design Order

Evaluate solutions in this order:

1. richer existing RSS/Atom fields;
2. public structured metadata exposed by the source;
3. official free APIs where available and permitted;
4. limited deterministic public-page extraction only if clearly justified and allowed;
5. more complex approaches only if simpler options cannot satisfy the requirement.

Do not assume AI summarization is required.

## Reporting-Window Design

The same design phase should also consider whether report composition should remain coupled to actual GitHub execution time.

Evaluate whether a deterministic cutoff would create a more stable daily information product.

Do not implement this solely from one sparse report.

Use additional production evidence before changing the current window semantics.

## Completion Criteria

Phase 5 is complete when:

- the richer-context requirement is precise;
- acceptable source-content boundaries are explicit;
- fallback behaviour is defined;
- report-length expectations are defined;
- source metadata richness has been inspected systematically;
- candidate implementation approaches have been compared;
- the smallest compliant approach has been selected;
- acceptance tests are defined before implementation.

---

# Phase 6 — Richer-Report Implementation and Quality Evaluation

## Objective

Implement the smallest justified richer-report solution and evaluate whether it materially improves the daily reading experience.

## Entry Condition

Phase 5 design is complete.

## Possible Implementation Areas

Depending on the design outcome:

- additional normalized source fields;
- richer feed-description handling;
- structured public metadata ingestion;
- deterministic context construction;
- source-specific safe metadata adapters;
- report-rendering changes;
- explicit missing-context fallbacks;
- updated source-quality rules;
- updated selection logic where insufficient context makes an item low-value;
- reporting-window stabilization if separately justified.

## Validation

Validation should include:

- deterministic unit tests;
- source-specific fixture tests;
- malformed/missing-context cases;
- real-source sample inspection;
- copyright-safe output inspection;
- report-length comparison;
- click-through requirement comparison;
- source concentration review;
- accessibility review;
- ranking/classification regression checks.

## Longitudinal Evaluation

After implementation, use repeated reports to evaluate:

### Usage

- Is the report opened consistently?
- Can the main developments be understood without opening every article?
- Are source links used mainly for deeper reading?

### Coverage

- Are major relevant stories missed?
- Are important domains consistently empty?
- Are some sources or domains overrepresented?

### Context Quality

- Is each item sufficiently understandable?
- Are summaries or descriptions too thin?
- Is context misleading because the public source material is incomplete?
- Are important facts omitted?

### Accessibility

- Do selected stories frequently lead to inaccessible pages?
- Does Bocconi access materially improve follow-up usability?
- Are inaccessible links acceptable when the report itself contains sufficient context?

### Noise

- Are low-value items frequently displayed?
- Is promotional content overrepresented?
- Are duplicate or near-duplicate developments common?

### Classification and Ranking

- Are items assigned to useful domains?
- Is the unclassified rate acceptable?
- Do high-value items appear near the top?
- Do source-tier weights distort relevance?
- Are keyword matches creating noisy score inflation?

### Operations

- Do scheduled runs complete reliably?
- Are failures understandable?
- Is source maintenance acceptably low?
- Does scheduler latency materially affect report composition?
- Does the project remain at zero recurring cost?

## Completion Criteria

Phase 6 is complete when:

- repeated reports demonstrate meaningful improvement;
- the user can understand most key selected developments without immediate click-through;
- source accessibility is acceptable;
- source concentration is acceptable;
- report length remains manageable;
- remaining weaknesses are documented with examples;
- further changes are prioritized by observed impact rather than speculative sophistication.

---

# Phase 7 — Optional Delivery and Interface Improvements

## Objective

Improve access only if repository-native Markdown reports become a demonstrated usability limitation.

## Possible Enhancements

- stable latest-report link;
- GitHub Issues delivery;
- GitHub Pages;
- weekly archive summaries;
- opportunity-specific views;
- other zero-cost delivery improvements.

## Entry Condition

Reports must already be used in practice and the delivery limitation must be observed rather than assumed.

## Current Mobile Position

GitHub-rendered Markdown remains the default mobile-access path.

Obsidian or another reading interface may be considered later only if it reduces real friction without creating recurring cost or significant maintenance.

## Excluded by Default

- paid APIs;
- automated ChatGPT integration;
- authenticated premium-content ingestion;
- private email ingestion;
- unrestricted full-article extraction;
- autonomous agents;
- RAG;
- vector databases;
- complex cloud infrastructure;
- sophisticated frontend development;
- dedicated mobile application development.

---

# Current Milestone

## Milestone 4 — Correct and Expand the Source and Domain Universe

### Objective

Improve the information inputs before adding richer report logic.

The immediate problem is not pipeline reliability.

The immediate problem is that some current sources may be inaccessible, too thin in metadata, overly concentrated, or insufficient for the intended intelligence workflow.

### Required Work

- review all seven current production sources;
- investigate Sifted accessibility and public metadata quality;
- distinguish automated-source eligibility from personal reading accessibility;
- use Bocconi access as a manual reading factor only;
- obtain source/domain priorities from the Career Agent;
- evaluate candidate sources technically;
- reconsider Financial Markets, Italy, and Milan/Bocconi domains;
- identify replacements for weak sources where appropriate;
- avoid adding sources merely to increase count;
- preserve zero recurring cost;
- preserve public-repository and credential safety.

### Validation Checklist

- [ ] Current source registry reviewed systematically.
- [ ] Sifted keep/replace/remove decision made.
- [ ] Source accessibility recorded.
- [ ] Public metadata richness recorded.
- [ ] Automation permission/access model recorded.
- [ ] Candidate source overlap assessed.
- [ ] Candidate source reliability assessed.
- [ ] Candidate source maintenance cost assessed.
- [ ] Career Agent source/domain priorities incorporated.
- [ ] Financial Markets domain decision made.
- [ ] Italy domain decision made.
- [ ] Milan/Bocconi domain decision made.
- [ ] Source configuration changes are minimal and justified.
- [ ] Configuration tests pass.
- [ ] Full automated suite passes.
- [ ] Real collection works.
- [ ] New reports are manually inspected.
- [ ] No credential or premium-content ingestion is introduced.
- [ ] Zero recurring monetary cost remains intact.

### Completion Action

When the source/domain universe is corrected and validated:

> Begin the dedicated richer-report design phase before implementing summary or context-generation logic.

---

# Active Product-Quality Findings

The following findings are now validated enough to guide development.

## 1. Report Context Is Too Thin

Current report items can require immediate click-through before the user understands the development.

**Consequence:** richer report context is now a validated requirement.

**Owner:** `01 Product Requirements.md`.

**Next action:** design in Phase 5 after source/domain correction.

---

## 2. Source Accessibility Matters

A technically valid feed can link to content the user cannot access.

Sifted provided a concrete example through a production-selected article requiring Sifted Pro.

**Consequence:** accessibility and metadata richness must become explicit source-quality criteria.

**Owner:** `03 Information Taxonomy and Source Policy.md`.

**Next action:** review current and candidate sources during Milestone 4.

---

## 3. Bocconi Access Expands Manual Reading but Not Automation Rights

The user has institutional access to high-value publications and research databases.

This materially improves manual follow-up possibilities.

It does not justify automated authenticated ingestion.

**Consequence:** source evaluation must distinguish personal accessibility from production ingestion permission.

**Owner:** `03 Information Taxonomy and Source Policy.md`.

---

## 4. Scheduled Runs Can Be Delayed

GitHub scheduled workflows have been observed to start materially later than their configured time.

**Consequence:** production schedule has been moved earlier to 06:05 Europe/Rome.

**Owner:** `02 System Architecture.md`.

---

## 5. Scheduler Delay Can Shift Report Composition

The current rolling 24-hour window is anchored to actual execution time.

A delayed scheduled run therefore changes the monitored period.

**Consequence:** deterministic reporting cutoff is now an evidence-based design question.

**Owner:** `02 System Architecture.md` and future Product Requirements if behavior changes.

---

## 6. Technical Success Does Not Guarantee a Good Report

A recent production run completed successfully with all sources healthy but produced a much shorter and more concentrated report than previous days.

**Consequence:** report length, source concentration and domain coverage must remain product-quality metrics rather than purely operational metrics.

**Owner:** this roadmap for prioritization; `01 Product Requirements.md` for acceptance criteria.

---

# Deferred Features

| Feature | Status | Reason |
|---|---|---|
| Near-duplicate clustering | Deferred pending repeated evidence | Exact deduplication remains sufficient until real repetition materially reduces usefulness |
| Multi-source story clustering | Deferred pending evidence | Adds false-merge risk and complexity |
| Geographic classification | Deferred pending evidence | Topic-level geography logic has not yet become the main bottleneck |
| Entity tracking | Deferred pending evidence | No demonstrated current requirement |
| Content-type classification | Deferred pending evidence | Source correction and report context have higher priority |
| Source-health history | Deferred pending repeated operational need | Current run summaries expose per-run health sufficiently |
| Advanced ranking | Deferred pending stronger evidence | Current source and context limitations are more urgent |
| GitHub Issues delivery | Deferred | Repository-native reports should be used first |
| GitHub Pages | Deferred | Delivery interface is not yet the main problem |
| Obsidian-specific production delivery | Deferred | Mobile reading friction has not yet justified additional sync complexity |
| Newsletter-email ingestion | Rejected for core system | Adds privacy, authentication and workflow complexity |
| Public newsletter feeds | Possible later | May be evaluated as ordinary public structured sources |
| LLM summaries | Not selected | Richer context is validated, but implementation design has not established a need for LLMs |
| Automated ChatGPT integration | Rejected for core system | Violates deterministic zero-cost architecture |
| Machine-learning classification | Rejected for current scope | Deterministic logic remains default |
| Embeddings and semantic search | Rejected for current scope | No validated need |
| RAG | Rejected for current scope | No validated workflow problem |
| Autonomous agents | Rejected for current scope | Adds complexity without current value |
| Cloud database | Rejected for current scope | Repository-native JSONL remains sufficient |
| Authenticated premium-source ingestion | Rejected | Conflicts with credential, licensing and public-repository constraints |
| Multi-user support | Rejected for current scope | Product remains single-user |

---

# Project Risks

## Source Expansion Without Discipline

Expanding the source universe can increase noise, duplication and maintenance faster than it increases intelligence value.

**Control:** every new source must pass explicit automation, quality, accessibility, overlap and maintenance criteria.

---

## Prestige Bias in Source Selection

High-prestige publications may appear attractive even when they cannot be ingested safely or provide insufficient public structured metadata.

**Control:** separate source prestige and personal reading value from production automation eligibility.

---

## Paywalled Follow-Up

A report item may appear useful but lead to inaccessible source content.

**Control:** evaluate user accessibility and public context richness during source selection; replace weak sources when better alternatives exist.

---

## Misuse of Institutional Access

Bocconi access may tempt the project to treat authenticated premium content as an automated input.

**Control:** Bocconi resources remain personal reading/research tools unless a source explicitly provides a separate automation-permitted public interface.

---

## Weak Information Quality

The pipeline may run correctly while producing a sparse, concentrated, repetitive or context-poor report.

**Control:** technical success and product usefulness remain separate validation dimensions.

---

## Scheduler Latency

GitHub cron execution may start substantially later than configured.

**Control:** schedule earlier than the desired reading time; keep scheduler latency visible; investigate deterministic reporting cutoff only if production evidence justifies it.

---

## Reporting-Window Drift

Because the current window is relative to actual start time, scheduler delay can change eligible content.

**Control:** record actual monitored windows and evaluate whether fixed cutoff semantics are needed.

---

## Network and Feed Instability

Real RSS/Atom sources may fail, hang, change format or publish inconsistent metadata.

**Control:** source-level isolation, 10-second timeout, explicit request headers, visible warnings and conservative source selection.

---

## Repository Growth

Daily JSON and Markdown files may accumulate indefinitely.

**Control:** keep the initial repository-native storage model and review retention only after real production history becomes large enough to create a demonstrated problem.

---

## Maintenance Burden

Poor sources may create recurring debugging or manual review work.

**Control:** prefer stable structured sources and replace low-value sources rather than compensating with complex source-specific logic.

---

## Misleading Success States

A technically completed run may conceal failed sources or poor information quality.

**Control:** preserve structured operational status while separately inspecting report quality.

---

## Installed-Package Freshness During Local Development

A locally installed package may lag behind the source tree even when source-based tests pass.

**Control:** remember that pytest can exercise repository source while `python -m daily_intelligence.cli` may execute an installed package copy. Refresh the installation when CLI behaviour does not reflect validated source changes.

---

# Decision Gates

The following gates prevent premature complexity.

## Gate 1 — Begin Implementation

**Status: passed**

Required:

- core project documents existed;
- repository foundations existed;
- no major unresolved blocker prevented the local slice.

---

## Gate 2 — Complete the Local Vertical Slice

**Status: passed**

Required:

- local end-to-end pipeline works;
- collection-window filtering works;
- exact duplicate handling works;
- deterministic classification and ranking work;
- output is inspectable;
- failures are visible;
- initial tests pass;
- one-command local execution works.

---

## Gate 3 — Add GitHub Actions

**Status: passed**

Evidence:

- seven real public feeds validated;
- remote requests bounded by a 10-second timeout;
- User-Agent requirement observed and implemented;
- real reports generated repeatedly;
- classification noise identified and corrected conservatively;
- real degraded-source behaviour validated;
- 110 automated tests passing;
- zero recurring monetary cost preserved.

---

## Gate 4 — Enable Scheduled Production

**Status: passed**

Required:

- manual Actions execution works;
- package installation works;
- tests pass in Actions;
- logs are visible;
- outputs validate;
- persistence works;
- no-change behavior works;
- degraded behavior works;
- critical-failure behavior works;
- concurrency behavior is acceptable.

Evidence:

- manual production workflow validated;
- bot persistence validated;
- no-change commit guard validated;
- deliberate critical configuration failure validated;
- deliberate degraded source run validated;
- scheduled run observed successfully.

---

## Gate 5 — Correct and Expand Sources / Domains

**Status: passed for controlled expansion**

This gate is no longer blocked because concrete production evidence now exists.

Evidence includes:

- Sifted accessibility problem;
- thin report context;
- source concentration;
- sparse production report;
- deferred strategic domains;
- substantial available Bocconi reading universe;
- current seven-source set proven sufficient for automation but not necessarily for mature intelligence quality.

Passing this gate does not authorize indiscriminate source expansion.

Every new source still requires individual validation.

---

## Gate 6 — Implement Richer Report Context

**Status: not yet passed**

Required:

- richer-context requirement is precisely defined;
- current source metadata is inspected;
- content-use boundaries are clear;
- simpler structured-data solutions are evaluated;
- acceptance criteria exist;
- zero-cost constraint is preserved.

Current evidence validates the problem, but not yet the implementation method.

---

## Gate 7 — Add Delivery Features

**Status: not yet passed**

Required:

- reports are being used;
- repository or mobile reading is a demonstrated usability limitation;
- proposed delivery improvement remains zero-cost and low-maintenance.

---

# Status Tracking

## Current Phase

Phase 4 — Source and Domain Correction / Expansion.

## Current Milestone

Milestone 4 — Correct and Expand the Source and Domain Universe.

## Completed Since Last Documentation Baseline

- implemented `.github/workflows/daily-intelligence.yml`;
- added manual `workflow_dispatch`;
- used Python 3.12 in GitHub Actions;
- executed 110 automated tests successfully in Actions;
- added production CLI logging configuration;
- validated all seven real sources in hosted execution;
- validated JSONL, Markdown and JSON run-summary generation in Actions;
- added output validation before persistence;
- enabled automated repository output commits;
- validated `github-actions[bot]` persistence;
- validated no-empty-commit logic;
- deliberately triggered and validated a critical configuration failure;
- deliberately triggered and validated a degraded source run;
- confirmed degraded output remains usable and is persisted;
- added `contents: write` permission required for repository persistence;
- added explicit workflow timeout;
- added concurrency protection;
- enabled timezone-aware scheduled execution;
- observed successful scheduled execution;
- observed substantial GitHub scheduling delay;
- moved production schedule to 06:05 Europe/Rome to create delivery buffer;
- accumulated real production report history;
- identified that current reports can be too thin;
- identified Sifted paywall/accessibility friction;
- identified source accessibility as a production-quality criterion;
- identified Bocconi access as a useful personal-reading layer but not an automation permission;
- observed a technically healthy but unusually sparse and concentrated scheduled report;
- identified scheduler-latency/report-window coupling as a future design question.

## Active Work

- reconcile canonical project documentation with completed Phase 3;
- review and correct the existing source set;
- plan source/domain expansion;
- use the Career Agent to define information priorities and candidate sources;
- return to this Development project for technical source evaluation;
- prepare the later richer-report design phase.

## Blockers

No infrastructure blocker exists.

The main constraints are now product-quality decisions:

- which current sources should remain;
- which weak or inaccessible sources should be replaced;
- which new domains should become active;
- which candidate sources are suitable for public automated collection;
- what minimum metadata richness is required;
- how personal Bocconi access should influence follow-up reading without entering automation.

## Next Highest-Priority Action

After this canonical documentation refresh:

> Use the Career Agent to define the desired expanded source/domain universe, beginning from the observed weaknesses of the current seven-source set, then return to the Development project to evaluate each candidate for automation suitability, accessibility, metadata richness, reliability and maintenance cost.

The first concrete current-source review should include Sifted.

## After Milestone 4

When the source/domain universe is corrected:

> Begin the richer-report product-design phase and spend sufficient time defining the requirement, safe information boundaries, metadata strategy, fallback behaviour and acceptance tests before implementing anything.

---

# Deferred Until Later

- richer-report implementation until design is complete;
- fixed reporting-cutoff implementation until timing evidence is stronger;
- near-duplicate logic;
- multi-source clustering;
- entities;
- geography classification;
- content types;
- source-health history;
- advanced ranking;
- GitHub Pages;
- GitHub Issues delivery;
- dedicated mobile delivery;
- AI-generated summaries;
- authenticated premium-content ingestion.

---

# Changelog

## 2026-08-14 — Phase 3 GitHub Automation Completed and Source/Domain Review Activated

- Implemented and validated the GitHub Actions production workflow.
- Validated manual `workflow_dispatch`.
- Validated dependency installation and 110 automated tests in GitHub Actions.
- Added CLI logging configuration after the first hosted run exposed missing INFO-level application logs.
- Validated full seven-source production execution in Actions.
- Validated generated JSONL, Markdown and run-summary outputs.
- Implemented output validation and repository-native automated persistence.
- Validated `github-actions[bot]` output commits.
- Validated no-empty-commit behaviour.
- Validated deliberate critical configuration failure.
- Validated deliberate degraded source failure with successful-source preservation.
- Added concurrency protection.
- Enabled scheduled execution.
- Observed successful scheduled runs.
- Observed substantial GitHub scheduler delay and moved the production trigger to 06:05 Europe/Rome.
- Identified that actual execution time currently shifts the rolling 24-hour content window.
- Observed a technically healthy but unusually sparse scheduled report.
- Identified richer per-story context as a new validated product requirement.
- Identified source accessibility as a source-quality requirement after a Sifted report item required Sifted Pro access.
- Recorded that Bocconi institutional access expands the user's personal reading universe but does not authorize automated ingestion.
- Passed the gate for controlled source/domain expansion.
- Made source/domain correction and expansion the next active milestone.
- Deferred richer-report implementation until a deliberate design phase is complete.

## 2026-08-11 — Phase 2 Real-Source Production Readiness Completed

- Selected and validated seven public real-source RSS feeds.
- Hardened remote collection with explicit request headers and a 10-second timeout.
- Confirmed normal SSL verification and real-source redirect behaviour.
- Kept retry logic absent because current evidence did not justify it.
- Validated real feed metadata and publication timestamps through the existing normalizer.
- Expanded the implemented taxonomy from two to seven domains without expanding the full target taxonomy.
- Added support for empty `default_domains` for broad heterogeneous sources.
- Replaced misleading broad source defaults with conservative source-wide defaults.
- Used real report inspection to identify classification false positives.
- Added `war`, `conflict` and `parliament` only after testing candidate keywords against real processed records.
- Generated and manually inspected real JSONL, Markdown and run-summary outputs.
- Improved the real report from a noisy initial version to a smaller, more credible output.
- Validated deliberate real-network partial-source failure and degraded-run behaviour.
- Reached 110 passing automated tests.
- Marked Phase 2 complete.
- Passed Gate 3 and made Phase 3 GitHub Automation the active phase.

## 2026-08-11 — Phase 1 Local Vertical Slice Completed

- Replaced the stale Phase 0 implementation status with the validated repository state.
- Marked Phase 0 and Phase 1 complete.
- Recorded the implemented local pipeline, CLI, collection-window filtering, operational reporting and logging.
- Recorded 104 passing tests at Phase 1 closeout.
- Reordered the roadmap so minimal real-source production-readiness validation preceded GitHub Actions.
- Moved speculative quality features behind evidence from real reports.
- Preserved zero recurring cost, deterministic processing, negligible daily manual work and public-repository safety as fixed constraints.
- Defined Milestone 2 as the next active development milestone.

## 2026-08-05 — Initial Roadmap Baseline

- Restored the original project roadmap and project-control structure.
- Defined the local vertical slice as the first implementation phase.
- Deferred automation, delivery features and production AI until the deterministic core was validated.