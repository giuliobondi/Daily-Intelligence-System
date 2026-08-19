# Daily Intelligence System — Information Taxonomy and Source Policy

> **Purpose**
>
> Define what information the Daily Intelligence System should collect, how it should classify that information, which sources are acceptable, and which rules govern source selection, accessibility, storage and public presentation.
>
> This document is the canonical quality-control and source-governance policy for information entering the system.

> **Primary question**
>
> *What information should the system collect, from which sources, and under which classification, accessibility and quality rules?*

> **Update frequency**
>
> Update when monitored domains, source-selection rules, accessibility assumptions, metadata requirements, source-audit conclusions or source-governance policies materially change.

---

# Information Objective

The system should provide broad but selective awareness of developments that may affect:

- economics and macroeconomics;
- politics and geopolitics;
- financial markets;
- companies and corporate strategy;
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
7. reader accessibility;
8. metadata richness;
9. suitability for automated collection;
10. maintenance burden.

The system should prefer a smaller set of strong, differentiated sources over broad but noisy coverage.

A technically compatible source is not automatically a good product source.

A prestigious source is not automatically a viable production source.

A source should be added because it closes an information-function gap, not merely because it increases publisher count.

---

# Current Implementation Status

The deterministic information-processing model is implemented and production-automated.

Current production configuration:

- thirteen active public RSS sources;
- ten active topic domains;
- deterministic title-and-description keyword rules;
- optional source-default domains;
- support for source-defined domains with empty keyword lists when explicitly justified;
- deterministic source-tier scoring;
- exact duplicate reduction;
- previous-24-hours publication window;
- explicit handling of unclassified records;
- scheduled GitHub Actions execution;
- automated output persistence;
- source-level failure isolation;
- degraded-run reporting;
- generic HTML-to-text normalisation for feed descriptions;
- explicit `Source context` report provenance;
- deterministic bounded report-context rendering at 500 characters;
- sentence-aware truncation with word-boundary fallback;
- explicit fallback when source context is missing or duplicates the title.

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

Current implemented domains:

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

All ten strategic topic macroareas now have an implemented domain.

Phase 4 produced several validated information-quality corrections and source-governance decisions:

- Sifted was replaced by Tech.eu;
- Tech.eu uses no blanket source-default domain;
- Financial Markets was implemented conservatively;
- Milan and Bocconi Ecosystem was implemented through Tech Europe Foundation;
- `milan_bocconi_ecosystem` is source-defined with an empty keyword list;
- multilingual classification was corrected so intentionally uppercase keywords such as `AI` are case-sensitive while lowercase keywords remain case-insensitive;
- Federal Reserve Board Monetary Policy was added as Tier 1 US monetary-policy evidence;
- Italy was implemented as the tenth domain;
- MIMIT News was added as Tier 1 Italian industrial-policy and company-policy evidence;
- Lavoce.info Imprese was added as Tier 2 independent Italian business-analysis evidence;
- narrow Italian-language keywords were added only after live-record testing and historical-regression checks;
- Google DeepMind News was added as a second Tier 1 frontier-lab primary AI source;
- ISPI Geoeconomics was added as a Tier 3 specialist source for differentiated geoeconomic interpretation, with no source-default domain and no taxonomy changes;
- ISPI Business Events was kept on standby because publication time is not a reliable event or actionability date;
- DG Competition was kept on standby because its broad official feed creates excessive routine State-aid signal under the current Europe classification and no clean narrow RSS route was found;
- ESMA was kept on standby because its feed lacks standard publication timestamps, carries long descriptions that distort classification, and would require multiple compensating processing changes;
- Italian Tech Alliance remains a deferred production-readiness candidate after a live feed probe confirmed strong Italian VC/programme value but substantial thin press-clipping repetition;
- Bocconi Career Services, Fintech District and Camera di Commercio Milano Monza Brianza Lodi were audited as Milan/Bocconi complements but are not suitable for automated MVP ingestion under the current public-structured-source and article-model constraints;
- Nasdaq, Bruegel, Assolombarda and Ars Technica remain deferred or standby because access, persistence, metadata or architecture constraints outweigh their incremental value.

Phase 5 completed a source-metadata audit to determine whether richer report context could be delivered without expanding the ingestion architecture.

The audit established that:

- the former 300-character display cap was not the dominant context limitation across most sources;
- Tech Europe Foundation, Lavoce.info Imprese and some ISPI descriptions lost useful context under the 300-character cap;
- several other sources already expose concise usable descriptions below 300 characters;
- ECB provides no useful description in the tested sample;
- Federal Reserve descriptions are often title-like;
- Google DeepMind description availability is partial;
- richer RSS `content` fields exist for some sources but can be body-like and thousands of characters long;
- generic use of those `content` fields would increase persistence and classification/ranking risk.

Phase 6 implemented the smallest accepted response:

```text
existing normalized description
→ explicit Source context label
→ 500-character display bound
→ complete-sentence preference
→ word-boundary fallback
→ explicit no-context fallback
```

The implementation deliberately does not:

- add a new context field;
- ingest article bodies;
- use generic RSS `content` fields;
- scrape article pages;
- use LLM summarisation;
- change classification evidence;
- change ranking evidence;
- change report item caps.

The current implementation checkpoint passed:

- 20 feed-fixture tests;
- 14 report tests;
- 122 tests in the full suite;
- a clean `git diff --check`;
- a production-equivalent run with all thirteen active sources successful and zero invalid records;
- manual inspection of generated report output.

The governing policy is now:

> **Preserve the current source universe and metadata/persistence boundaries, use bounded source-provided context in reports, and reopen source expansion or richer enrichment only when real product use demonstrates a material remaining gap.**

---

# Taxonomy Principles

## Configurable

Domains, keywords, source tiers and source defaults belong in configuration rather than being scattered through processing code.

Configuration should expand only when corresponding information value is justified.

## Multi-Domain

A story may legitimately belong to more than one domain.

Examples:

- an EU AI regulation may belong to Artificial Intelligence, Technology and Europe/EU;
- an ECB or Federal Reserve decision may belong to Economics and Financial Markets;
- a startup acquisition may belong to Startups/VC and Companies/Corporate Strategy;
- an Italian industrial-policy story may belong to Italy and Companies/Corporate Strategy.

## One Primary Report Placement

A multi-domain item should appear once in the report.

Current policy:

- first assigned eligible domain becomes primary placement;
- additional domains appear as secondary metadata.

## Explainable

Current classification evidence consists of:

- source defaults;
- matched configured keywords.

Any future mechanism should remain inspectable.

## Conservative

Prefer an unclassified record over a misleading classification.

Unclassified records remain valid processed records but are omitted from the main report by default.

A high unclassified share is not itself a defect.

The correct question is:

> **Are important stories being missed or weak stories being promoted?**

not:

> **Is the classification rate high?**

## Broad but Bounded

The system should not become a generic global-news taxonomy.

## Independent Dimensions

Topic, geography, source tier, reader accessibility and content type are conceptually separate.

Only topic classification and source tier are currently implemented at article level.

Source-level geographic scope exists in configuration.

## Information Functions Before Publisher Count

Source expansion should solve missing information functions.

Examples of distinct information roles include:

- primary institutional evidence;
- monetary-policy evidence;
- market/company reporting;
- independent analysis;
- specialist ecosystem intelligence;
- professional opportunity discovery;
- frontier-lab primary evidence;
- independent technology scrutiny.

Do not add several publications simply because they cover the same subject.

The operating principle is:

> **Correct information-function gaps before correcting publisher-count gaps.**

---

# Target Topic Taxonomy

The strategic target remains ten macroareas.

All ten now have implemented domains.

Implementation does not imply maturity.

Several domains still lack the differentiated source roles required for strong long-term coverage.

---

## 1. Global Politics and Geopolitics

### Scope

Major political, diplomatic, security and geopolitical developments with international or material economic relevance.

### Include

- wars and conflicts;
- peace negotiations;
- sanctions;
- tariffs and trade restrictions;
- major elections with material consequences;
- major foreign-policy changes;
- defence and security developments;
- geopolitical shocks affecting markets, technology, energy or supply chains.

### Exclude or Deprioritise

- routine political theatre;
- personality-driven coverage;
- minor party disputes;
- local politics without wider consequence.

### Current Status

**Implemented.**

Evidence-backed refinements include:

- `war`;
- `conflict`;
- `parliament`;
- `tariffs`.

Broad terms such as `government`, `defence`, `president` and `prime minister` were previously tested but rejected because they produced ambiguous or low-value matches.

Current production sources provide sufficient baseline MVP coverage.

This is no longer a priority source-expansion domain.

---

## 2. Economics and Macroeconomics

### Scope

Macroeconomic developments, economic policy and economic indicators.

### Include

- inflation;
- GDP and growth;
- unemployment and labour-market indicators;
- monetary policy;
- fiscal policy;
- public debt;
- economic forecasts;
- major structural economic changes.

### Current Status

**Implemented and sufficiently mature for the MVP.**

Primary evidence comes from:

- ECB;
- Istat;
- Federal Reserve;
- selected MIMIT and Lavoce.info records.

Current deterministic terms include:

- `inflation`;
- `gdp`;
- `unemployment`;
- `interest rates`;
- `monetary policy`;
- `fiscal policy`;
- `public debt`;
- `economic forecast`;
- `inflazione`.

No major source gap currently blocks MVP use.

---

## 3. Financial Markets

### Scope

Material developments in financial markets, market structure and financial stability.

### Include

- bond markets;
- bond yields;
- yield curves;
- credit spreads;
- capital markets;
- financial stability;
- market sell-offs;
- foreign exchange;
- equities;
- asset management;
- IPOs;
- major central-bank market signals;
- important changes in settlement, trading infrastructure or market regulation.

### Current Status

**Implemented and sufficient for the current MVP baseline, but incomplete.**

Current production evidence is strongest for:

- monetary-policy-linked market conditions;
- rates;
- central-bank signals;
- capital-markets references in selected Italian analysis.

Current deterministic terms include:

- `stock market`;
- `bond market`;
- `bond yields`;
- `yield curve`;
- `credit spreads`;
- `capital markets`;
- `financial stability`;
- `market sell-off`;
- `foreign exchange`;
- `equities`;
- `asset management`;
- `ipo`;
- `FOMC`;
- `Federal Open Market Committee`;
- `discount rate`;
- `mercati dei capitali`.

The Federal Reserve now provides dedicated Tier 1 US monetary-policy evidence.

The domain remains weaker on:

- market structure;
- trading infrastructure;
- settlement;
- broader securities-market supervision;
- global market reporting beyond central-bank-linked developments.

### ESMA Audit Conclusion

ESMA was audited as the strongest obvious candidate for broader Financial Markets coverage.

The strategic role passed:

- market structure;
- trading;
- settlement;
- funds;
- investment services;
- market data;
- financial infrastructure;
- securities-market supervision.

The production fit did not pass.

Observed issues:

- official RSS accessible;
- ten records collected successfully;
- standard `published` and `updated` fields absent;
- dates embedded inside HTML description payloads;
- normalized descriptions approximately 1,000–2,400 characters in the tested sample;
- long description bodies produced incidental keyword matches and inflated multi-domain classification;
- several genuinely valuable Financial Markets stories remained unclassified;
- activation would require timestamp-recovery plus description/classification changes.

Current decision:

> **ESMA remains on standby.**

Do not add a source-specific date parser or description-processing path solely for ESMA.

Reconsider only if:

- a cleaner official endpoint appears;
- a generic reusable solution becomes independently justified;
- real report use demonstrates a sufficiently costly Financial Markets gap.

---

## 4. Companies and Corporate Strategy

### Scope

Material company-level developments with strategic significance.

### Include

- acquisitions;
- mergers;
- restructurings;
- divestments;
- market entry;
- bankruptcy;
- earnings guidance with strategic significance;
- major strategic plans;
- industrial-policy interventions affecting firms;
- competition and antitrust actions with material company implications.

### Current Status

**Implemented and sufficient for the MVP baseline, but globally incomplete.**

Current evidence comes from:

- BBC Business;
- Tech.eu;
- MIMIT;
- Lavoce.info;
- selected institutional sources.

Current terms include:

- `acquisition`;
- `acquired`;
- `merger`;
- `restructuring`;
- `divestment`;
- `market entry`;
- `bankruptcy`;
- `earnings guidance`;
- `strategic plan`;
- `tavoli di crisi`;
- `accordo di sviluppo`;
- `quadro industriale`;
- `rilevanza strategica`;
- `fusione e acquisizione`;
- `piano industriale`.

### DG Competition Audit Conclusion

DG Competition was audited as a high-value candidate for:

- M&A;
- competition policy;
- antitrust;
- Foreign Subsidies Regulation;
- corporate strategic actions.

The strategic role passed strongly.

The general official RSS feed was technically clean:

- thirty records collected;
- thirty normalized;
- zero normalization errors;
- concise descriptions;
- reliable timestamps.

However, the broad feed also carries large volumes of routine State-aid material.

Under the current classifier, many of those routine items matched:

- `european commission`;
- Europe/EU.

Because DG Competition would be Tier 1, routine notices received relevance scores comparable with stronger existing Europe/EU intelligence.

Narrow RSS routes were tested for:

- Mergers;
- Antitrust and Cartels;
- Foreign Subsidies Regulation.

All tested narrow feed routes returned `404`.

Current decision:

> **DG Competition remains on standby.**

Do not:

- weaken `european commission` globally;
- add DG-specific ranking penalties;
- introduce source-specific filtering;
- build a custom Mergers/Antitrust scraper.

Reconsider if a narrow official structured feed becomes available.

---

## 5. Artificial Intelligence

### Scope

Material AI research, products, regulation, infrastructure and market developments.

### Include

- major model releases;
- foundation models;
- frontier-lab announcements;
- AI regulation;
- important infrastructure or compute developments;
- material enterprise adoption;
- significant AI safety, security or governance developments.

### Current Status

**Implemented and sufficient for the MVP baseline.**

Primary-source coverage now includes:

- OpenAI News;
- Google DeepMind News.

Current terms include:

- `artificial intelligence`;
- intentionally case-sensitive `AI`;
- `machine learning`;
- `large language model`;
- `foundation model`;
- `model release`;
- `IA`.

The addition of DeepMind corrected the prior concentration of primary AI evidence around OpenAI.

The remaining maturity gap is independent critical interpretation and scrutiny.

That gap is real but not an MVP blocker.

---

## 6. Technology and Software

### Scope

Material developments in software, cloud, cybersecurity, developer infrastructure and technology strategy.

### Include

- major software products;
- cloud infrastructure;
- cybersecurity;
- developer tools;
- open source;
- APIs;
- technology infrastructure;
- major strategic technology shifts.

### Current Status

**Implemented and sufficient for the MVP baseline.**

Current terms include:

- `software`;
- `cloud`;
- `cybersecurity`;
- `developer`;
- `open source`;
- `api`.

Technology coverage is currently provided through:

- Tech.eu;
- OpenAI;
- DeepMind;
- selected BBC and institutional stories.

Independent technology scrutiny remains thinner than desired.

Ars Technica remains on standby because persistence terms are not sufficiently clean for the current public-repository model.

No additional technology source is currently required.

Future expansion should be evidence-triggered by real report use or a materially cleaner independent source.

---

## 7. Startups and Venture Capital

### Scope

Material developments in startups, scaleups, funding and venture capital.

### Include

- funding rounds;
- startup acquisitions;
- VC funds;
- accelerator/programme activity;
- scaleups;
- venture-market trends;
- material startup-policy developments.

### Current Status

**Implemented and sufficient for the MVP baseline, but still concentrated.**

Primary production evidence currently comes from:

- Tech.eu;
- Tech Europe Foundation.

Current terms include:

- `funding`;
- `funding round`;
- `series a`;
- `series b`;
- `series c`;
- `venture capital`;
- `vc`;
- `early-stage fund`;
- `funding market`.

Generic `startup` was previously tested and rejected because it promoted low-value profile content.

### Italian Tech Alliance Audit Conclusion

Italian Tech Alliance remains strategically valuable for:

- Italian venture-capital statistics;
- ecosystem policy;
- training programmes;
- startup and tech-transfer initiatives.

Its public feed is technically clean:

- standard RSS;
- timestamps present;
- twenty live entries collected successfully.

However, most tested descriptions were extremely thin and acted as press-clipping labels such as:

- `Articolo su Corriere della Sera`;
- `Articolo sul Sole24Ore`;
- `Articolo su Repubblica`.

The feed also showed repeated coverage of the same underlying Italian VC developments.

A minority of entries were genuinely differentiated, including:

- Venture Academy;
- training programmes;
- registration deadlines;
- ecosystem initiatives.

Current decision:

> **Italian Tech Alliance remains a deferred production-readiness candidate.**

Do not activate it merely to increase Startups/VC publisher diversity.

Do not give it a Milan/Bocconi source default.

Reconsider if:

- its feed becomes richer;
- programme/deadline discovery becomes a validated product priority;
- real report use shows a costly Italian VC ecosystem gap.

---

## 8. Europe and the European Union

### Scope

Material EU institutional, regulatory, economic and strategic developments.

### Include

- European Commission actions;
- European Parliament developments;
- European Council decisions;
- ECB developments;
- EU regulation;
- Single Market developments;
- major EU strategic initiatives;
- geoeconomic developments with material European implications.

### Current Status

**Implemented and sufficiently mature for the MVP, but not fully diversified.**

Current evidence includes:

- ECB;
- European Commission Highlighted News;
- BBC;
- ISPI Geoeconomics;
- selected MIMIT and Lavoce.info stories.

Current terms include:

- `european union`;
- `european commission`;
- `european parliament`;
- `european central bank`;
- `euro area`;
- `european council`;
- `eu regulation`;
- `single market`.

The institutional evidence layer is strong.

The previous independent-interpretation gap has been partially improved by ISPI Geoeconomics, but it remains incomplete.

### ISPI Geoeconomics

ISPI Geoeconomics is active as:

- Tier 3;
- Italian-language;
- no source-default domains;
- geographic scope:
  - Global;
  - Europe;
  - Italy.

Its information role is differentiated geoeconomic interpretation covering areas such as:

- economic security;
- trade;
- industrial policy;
- strategic dependencies;
- supply chains;
- technology competition;
- business implications of geopolitical change.

Controlled validation showed:

- official public RSS;
- ten items collected;
- ten normalized;
- zero normalization errors;
- generic geopolitical items often remained unclassified;
- AI/technology-relevant items were classified selectively;
- no source-specific ranking boost required;
- no new keywords justified;
- no source default justified;
- no same-domain historical overlap found within the tested ±3-day comparison window.

Current decision:

> **ISPI Geoeconomics is active and should remain configuration-only.**

Do not add broad geoeconomic keywords solely to increase its classification rate.

---

## 9. Italy

### Scope

Material Italian economic, policy, industrial, company and institutional developments.

### Include

- macroeconomic developments;
- industrial-policy measures;
- company-policy interventions;
- investment and development programmes;
- material regulatory changes;
- relevant Italian business analysis;
- strategically important Italian innovation and venture developments.

### Current Status

**Implemented and sufficiently mature for the MVP.**

Current production evidence includes:

- Istat;
- MIMIT;
- Lavoce.info;
- Tech Europe Foundation;
- selected BBC/European institutional records;
- ISPI where classification evidence supports inclusion.

Italy no longer represents a missing-domain problem.

Remaining gaps concern maturity and source diversity rather than basic coverage.

Il Sole 24 Ore remains in standby despite strong strategic value because persistence/licensing compatibility with the public Git archive is not currently clean enough.

---

## 10. Milan and Bocconi Ecosystem

### Scope

Material developments in the Milan and Bocconi professional, academic, startup, employer and business ecosystem.

### Include

- entrepreneurship and startup programmes;
- deep-tech initiatives;
- innovation ecosystem activity;
- professional programmes;
- high-value public employer events;
- selected finance and consulting ecosystem developments;
- established-company and industrial ecosystem intelligence;
- high-value public lectures or institutional events when practically automatable.

### Current Status

**MVP-sufficient but deliberately incomplete.**

The implemented production sensor is:

- Tech Europe Foundation.

The domain intentionally uses:

- no broad keywords;
- source-defined classification through Tech Europe Foundation.

This avoids false positives from generic terms such as:

- Milan;
- Bocconi;
- career;
- internship;
- event.

TEF provides meaningful coverage of:

- entrepreneurship;
- startup ecosystem activity;
- deep tech;
- founder/programme activity;
- university-linked innovation.

However, important roles remain incomplete:

- finance recruiting;
- consulting recruiting;
- employer events;
- complete opportunity/deadline discovery;
- established-company ecosystem;
- industrial ecosystem;
- selected high-value public lectures.

The latest targeted source audits demonstrate that these remaining gaps are constrained by public structured-source availability and the current article model rather than by insufficient searching.

### Bocconi Career Services

Strategic value is extremely high for:

- recruiting;
- employer events;
- finance;
- consulting;
- professional opportunities.

Public pages expose meaningful information such as:

- Investment Banking Days;
- Bocconi&Jobs;
- sector-specific Recruiting Dates;
- employer participation;
- registration windows.

However:

- the most actionable layer remains partly inside authenticated `yoU@B` / JobGate infrastructure;
- authenticated automated access is prohibited;
- no sufficiently narrow public RSS/Atom/API was identified;
- event/actionability semantics do not map cleanly to publication-date article processing.

Current decision:

> **Bocconi Career Services remains a high-value manual/private complementary layer and is not an automated MVP source.**

Do not automate authenticated access.

Do not build a broad Bocconi crawler.

### Assolombarda

Assolombarda remains strategically strong for:

- established companies;
- Milan/Lombardy industrial ecosystem;
- business policy;
- economic analysis.

Its audited feeds remain incompatible because:

- publication timestamps were absent in the tested feed records;
- substantive copyrighted descriptions would create persistence concerns;
- Centro Studi did not expose a suitable public feed.

Current decision:

> **Assolombarda remains on standby.**

### Fintech District

Fintech District is strategically strong for:

- Milan finance;
- fintech;
- corporate innovation;
- startups;
- professional ecosystem intelligence.

Controlled endpoint probing found:

- WordPress API routes: `404`;
- RSS/feed routes: `404`;
- public sitemap: available;
- sitemap content insufficient for reliable previous-24-hours article ingestion;
- site implemented as a Next.js application.

Current decision:

> **Fintech District remains on standby because no clean public RSS/API route has been established.**

Do not reverse-engineer internal Next.js APIs for the MVP.

### Camera di Commercio Milano Monza Brianza Lodi

The Chamber is strategically strong for:

- local companies;
- business demography;
- Milan economic ecosystem;
- business programmes and initiatives.

Controlled endpoint probing found that:

- RSS routes;
- feed routes;
- sitemap;
- robots.txt;

all returned the same Incapsula/Imperva interstitial shell rather than usable machine-readable content.

Current decision:

> **Camera di Commercio Milano Monza Brianza Lodi remains on standby because clean automation-compatible access was not established.**

Do not attempt to bypass the access-control layer.

### Milan/Bocconi MVP Boundary

The current product does not provide comprehensive Milan/Bocconi ecosystem intelligence.

It does provide:

- one meaningful automated structured sensor;
- validated domain architecture;
- documented private/manual Career Services boundary;
- controlled evaluation of the strongest obvious complementary sources;
- explicit evidence that several remaining high-value roles would require:
  - authenticated access;
  - custom scraping;
  - event/deadline semantics;
  - source-specific timestamp recovery;
  - access-control workarounds.

For the current MVP:

> **Milan/Bocconi is sufficiently developed because it has more than nominal automated coverage and a demonstrated public-structured-source/current-architecture ceiling.**

Future expansion should be triggered by actual user cost from missed opportunities rather than by a desire for abstract completeness.

---

# Source Tier Policy

Source tier represents evidence quality and authority, not user preference.

## Tier 1

Primary institutions and high-authority direct sources.

Examples:

- ECB;
- Federal Reserve;
- Istat;
- European Commission;
- MIMIT;
- OpenAI;
- Google DeepMind.

Default score contribution:

- 4 points.

## Tier 2

High-quality specialist reporting and analysis.

Examples:

- Tech.eu;
- Lavoce.info.

Default score contribution:

- 3 points.

## Tier 3

Credible specialist analysis, ecosystem intelligence and interpretation.

Examples:

- Tech Europe Foundation;
- ISPI Geoeconomics.

Default score contribution:

- 2 points.

## Tier 4

Lower-priority or supplementary sources.

Default score contribution:

- 1 point.

Tier does not guarantee display.

A Tier 1 source may still produce irrelevant stories.

A Tier 3 source may produce uniquely valuable intelligence.

---

# Source-Default Domain Policy

Source defaults are allowed only when the source-wide information function genuinely guarantees topical relevance.

Good examples:

- OpenAI → Artificial Intelligence;
- Google DeepMind → Artificial Intelligence;
- Federal Reserve Monetary Policy → Economics/Macroeconomics;
- MIMIT News → Italy;
- Lavoce.info Imprese → Italy;
- Tech Europe Foundation → Milan/Bocconi Ecosystem.

Bad defaults include:

- BBC Business → Companies;
- ECB → Economics for every item;
- European Commission → Europe for every item;
- Tech.eu → Startups/VC;
- ISPI Geoeconomics → Europe or Global Politics;
- Italian Tech Alliance → Milan/Bocconi.

Source defaults should not be used to compensate for weak classification.

The policy is:

> **Use source defaults only for source-wide topical guarantees, not for publisher identity or expected subject matter.**

---

# Empty-Keyword Domain Policy

A domain may intentionally have an empty keyword list when:

- its identity is source-defined;
- keyword rules would create unacceptable false positives;
- a source default provides stronger evidence.

Current example:

```yaml
milan_bocconi_ecosystem:
  keywords: []
```

This is intentional.

Do not add generic Milan/Bocconi keywords merely to avoid an empty configuration.

---

# Keyword Policy

Keywords should be:

- specific enough to represent meaningful topical evidence;
- validated against real records;
- tested for false positives;
- added only when they recover useful misses.

Avoid generic terms merely because they increase coverage.

Current keyword policy includes:

- lowercase terms are case-insensitive;
- intentionally uppercase acronyms such as `AI` remain case-sensitive.

Every material keyword change should be validated against:

1. current source records;
2. historical processed records where available;
3. ranking consequences;
4. false-positive risk.

The goal is not a large keyword dictionary.

The goal is the smallest keyword set that captures important signal.

---

# Classification Policy

Classification uses normalized:

- title;
- description.

Evidence comes from:

1. source-default domains;
2. configured keyword matches.

A record may receive multiple domains.

Unclassified records remain valid.

Do not classify based solely on source name unless the source default has been explicitly approved.

Do not use machine learning or LLM classification while deterministic rules remain sufficient.

---

# Ranking Policy

Current deterministic ranking:

```text
source-tier score
+ 2 × number of assigned domains
+ 1 × number of matched keywords
```

Current source-tier values:

| Tier | Score |
|---|---:|
| 1 | 4 |
| 2 | 3 |
| 3 | 2 |
| 4 | 1 |

Ranking should reward strong evidence.

Do not introduce:

- source-specific ranking penalties;
- source-specific boosts;
- opaque learned ranking;
- manual publisher prestige scores beyond source tier;

unless repeated report-quality evidence independently justifies the change.

Bad upstream evidence should be corrected upstream rather than patched with ranking exceptions.

---

# Duplicate Policy

Current implementation performs exact normalized duplicate reduction.

This is sufficient for the MVP.

Near-duplicate or story-cluster logic remains deferred until repeated reports show a material problem.

Do not add fuzzy matching solely because multiple sources occasionally cover the same event.

---

# Publication-Time Policy

The previous-24-hours collection window depends on a confirmed article publication timestamp.

Records without a reliable `published_at` should not be treated as current merely because they were retrieved now.

The current policy deliberately does not use retrieval time as publication time.

Source-specific recovery from:

- embedded HTML dates;
- page bodies;
- guessed date fragments;

is not generally approved.

A generic fallback may be reconsidered only if:

- multiple high-value sources share the same pattern;
- the logic is deterministic;
- ambiguity is low;
- maintenance burden is justified independently.

The ESMA audit reinforced this policy.

---

# Event and Opportunity Semantics

The current core data model is article-oriented.

For ordinary news:

```text
publication time ≈ actionability time
```

For events, programmes and opportunities this may not hold:

```text
publication time
≠ event date
≠ registration opening
≠ application deadline
```

ISPI Business Events and Bocconi Career Services provided direct evidence of this mismatch.

The system should not introduce a separate event/deadline model solely because these sources exist.

A new opportunity/event architecture should be considered only when repeated real use shows that missed deadlines or event timing create meaningful user cost.

Until then:

- keep private/authenticated Career Services manual;
- do not misuse publication date as event date;
- keep high-value incompatible event feeds on standby.

---

# Source Accessibility Policy

Source accessibility has two distinct dimensions:

## Automation Accessibility

Can the production system retrieve the source through:

- public RSS;
- Atom;
- official free API;
- another explicitly approved public structured endpoint?

## Reader Accessibility

Can the user open and meaningfully read the linked item?

These are not the same.

A source can be:

- automation-compatible but reader-paywalled;
- reader-accessible through Bocconi but not automation-compatible;
- fully public on both dimensions;
- unsuitable on both dimensions.

Source decisions should evaluate both dimensions explicitly.

---

# Bocconi Access Policy

The user has legitimate institutional access through Bocconi to several premium publications and research platforms.

This includes direct or institutional access to sources such as:

- Financial Times;
- Wall Street Journal;
- New York Times;
- The Economist;
- Il Sole 24 Ore;
- Foreign Affairs;
- Harvard Business Review;
- Factiva;
- Nexis Uni;
- Business Source Ultimate;
- Bloomberg Terminal;
- LSEG Workspace;
- FactSet;
- Capital IQ Pro;
- Aida.

This access improves:

- personal reading;
- manual follow-up;
- strategic research.

It does **not** automatically make a source suitable for automated ingestion.

The automated production system must not:

- embed Bocconi credentials;
- scrape authenticated premium pages;
- automate `yoU@B`;
- automate JobGate;
- ingest private newsletters or mailboxes;
- store restricted full-text content.

---

# Premium Bocconi Exception

A narrow exception may apply when:

- a premium publication has very high strategic value;
- the user can legitimately access it through Bocconi;
- a public automation-compatible metadata endpoint exists;
- the pipeline does not access authenticated article bodies;
- only minimal public metadata is persisted.

This exception is:

- source-specific;
- deliberate;
- not a general licence to automate paywalled content.

A thinner report entry may be acceptable when the publication's value justifies manual click-through.

---

# Public Repository and Persistence Policy

The repository is public.

Persistence policy must therefore be conservative.

Prefer storing:

- title;
- URL;
- publisher/source;
- timestamps;
- short feed-provided descriptions;
- classification metadata;
- ranking metadata.

Do not store:

- authenticated article bodies;
- copied paywalled text;
- restricted copyrighted full content;
- credentials;
- private user data;
- private newsletter content.

A public RSS endpoint does not automatically imply that every exposed content body should be permanently republished in Git.

When descriptions are unusually large or appear to reproduce article bodies, inspect persistence suitability before activation.

---

# Metadata Richness Policy

Metadata quality is a product attribute.

Preferred feed entries contain:

- clear title;
- canonical URL;
- reliable publication timestamp;
- concise but useful description;
- identifiable source.

Weak metadata patterns include:

- missing publication timestamps;
- empty descriptions;
- title-duplicate descriptions;
- descriptions consisting only of external publisher labels;
- descriptions containing large portions of page bodies;
- malformed publisher-provided spacing or truncation;
- unstable or malformed links.

Metadata richness should be evaluated before source activation because it affects:

- classification;
- ranking;
- report context;
- public persistence.

The Phase 5 metadata audit established an important distinction:

> **thin metadata and display truncation are different problems.**

Increasing the report display limit can recover context that already exists in a feed description.

It cannot create context where the feed exposes:

- no description;
- only a title-like description;
- a malformed or already-truncated publisher snippet.

The current report-context policy therefore uses the existing normalized description as the source of truth and exposes thin metadata transparently.

Do not substitute body-like RSS `content` fields merely because they are longer.

Some active sources expose materially richer `content` fields, but controlled auditing showed that these can contain thousands of characters and behave more like article bodies than bounded feed metadata.

Generic ingestion would create unnecessary risk for:

- public-repository persistence;
- classification quality;
- ranking quality;
- maintenance;
- copyright boundaries.

Source-provided metadata defects should remain visible unless a safe deterministic correction is validated at the actual defect layer.

The Tech.eu audit is the current example:

```text
malformed spacing
→ already present in raw RSS description
→ source-quality limitation
→ no speculative generic word repair
```

---

# Current Production Source Universe

| Source | Tier | Default Domain | Language | Scope | Status |
|---|---:|---|---|---|---|
| BBC News World | 2 | None | EN | Global | Active |
| BBC News Business | 2 | None | EN | Global | Active |
| ECB Press | 1 | None | EN | Europe | Active |
| European Commission Highlighted News | 1 | None | EN | Europe | Active |
| Istat Press Releases | 1 | Economics/Macro | EN | Italy | Active |
| OpenAI News | 1 | Artificial Intelligence | EN | Global | Active |
| Tech.eu | 2 | None | EN | Europe | Active |
| Tech Europe Foundation | 3 | Milan/Bocconi Ecosystem | EN | Europe / Milan | Active |
| Federal Reserve Monetary Policy | 1 | Economics/Macro | EN | United States / Global | Active |
| MIMIT News | 1 | Italy | IT | Italy | Active |
| Lavoce.info Imprese | 2 | Italy | IT | Italy | Active |
| Google DeepMind News | 1 | Artificial Intelligence | EN | Global | Active |
| ISPI Geoeconomics | 3 | None | IT | Global / Europe / Italy | Active |

Current language balance:

- English: 10 active sources;
- Italian: 3 active sources.

The system does not require symmetric language representation.

---

# Active Source Decisions

## BBC News World

Role:

- broad geopolitical and international-news sensor.

Strengths:

- public RSS;
- strong timeliness;
- broad global scope.

Limitations:

- heterogeneous topics;
- keyword classification required.

Keep active.

---

## BBC News Business

Role:

- broad business and company-news sensor.

Strengths:

- public RSS;
- useful company and economic reporting.

Limitations:

- not every item is Companies/Corporate Strategy;
- no blanket company default.

Keep active.

---

## European Central Bank

Role:

- Tier 1 euro-area institutional evidence.

Strengths:

- monetary policy;
- euro-area economics;
- financial stability.

No blanket Economics default because ECB output can span multiple topics.

Keep active.

---

## European Commission Highlighted News

Role:

- Tier 1 EU institutional evidence.

Strengths:

- regulation;
- policy;
- Single Market;
- strategic EU initiatives.

No blanket Europe default because not every highlighted item merits inclusion.

Keep active.

---

## Istat

Role:

- Tier 1 Italian macroeconomic evidence.

Source default:

- Economics/Macro.

Keep active.

---

## OpenAI

Role:

- Tier 1 primary AI evidence.

Source default:

- Artificial Intelligence.

Keep active.

---

## Tech.eu

Role:

- European startup, technology, funding and company intelligence.

Tier:

- 2.

No source default.

Reason:

- feed contains both strong startup/company stories and lower-value profiles;
- classification should remain evidence-driven.

Keep active.

---

## Tech Europe Foundation

Role:

- Milan/Bocconi external ecosystem sensor;
- entrepreneurship;
- deep tech;
- university-linked innovation;
- startup programmes.

Tier:

- 3.

Source default:

- Milan/Bocconi Ecosystem.

Keep active.

---

## Federal Reserve Monetary Policy

Role:

- Tier 1 US monetary-policy evidence;
- macroeconomic and rates context.

Source default:

- Economics/Macro.

Keep active.

---

## MIMIT News

Role:

- Tier 1 Italian industrial-policy and company-policy evidence.

Source default:

- Italy.

Keep active.

---

## Lavoce.info Imprese

Role:

- Tier 2 independent Italian business analysis.

Source default:

- Italy.

Keep active.

---

## Google DeepMind News

Role:

- Tier 1 primary frontier-AI evidence.

Source default:

- Artificial Intelligence.

Keep active.

---

## ISPI Geoeconomics

Role:

- specialist geoeconomic interpretation;
- trade;
- economic security;
- industrial policy;
- strategic dependencies;
- technology competition.

Tier:

- 3.

Source default:

- None.

Language:

- Italian.

Geographic scope:

- Global;
- Europe;
- Italy.

Audit evidence:

- official RSS reachable;
- ten items collected;
- ten items normalized;
- complete usable publication timestamps;
- generic pipeline compatible;
- no source-specific parser;
- no source-specific ranking rule;
- no taxonomy expansion required;
- conservative classification naturally excludes much generic geopolitical material;
- three tested records classified through existing AI/Technology evidence;
- no same-domain historical overlap found within the tested ±3-day comparison window;
- ranking remained proportional under Tier 3.

Keep active.

---

# Standby and Deferred Source Decisions

## ISPI Business Events

Status:

> **Standby — event/actionability semantics**

Strengths:

- narrow public feed exists;
- strong professional/business/geoeconomic event value;
- descriptions contain meaningful event information.

Blocker:

- feed publication time does not reliably represent event date or actionability;
- some entries appear after the event has already occurred;
- current 24-hour article model cannot reliably detect opportunities.

Do not introduce event/deadline architecture solely for this feed.

---

## DG Competition

Status:

> **Standby — product quality / feed breadth**

Strengths:

- excellent M&A;
- antitrust;
- competition;
- Foreign Subsidies Regulation;
- company-strategy intelligence.

Technical findings:

- general official RSS accessible;
- thirty items collected;
- thirty normalized;
- zero normalization errors;
- reliable timestamps;
- concise descriptions.

Product blocker:

- general feed is heavily mixed with routine State-aid notices;
- many routine notices classify as Europe/EU via `european commission`;
- Tier 1 source score makes routine items overly competitive in ranking;
- tested narrow Mergers, Antitrust and FSR RSS routes returned `404`.

Do not add:

- DG-specific ranking penalties;
- DG-specific exclusion rules;
- broad taxonomy changes;
- a custom scraper.

---

## ESMA

Status:

> **Standby — architecture**

Strengths:

- high-value Financial Markets information function;
- market structure;
- settlement;
- trading;
- market data;
- investment services;
- financial supervision.

Blockers:

- RSS `published` and `updated` fields absent;
- dates embedded inside HTML descriptions;
- normalized descriptions remain long;
- long bodies cause incidental keyword matches and score inflation;
- several core Financial Markets stories still remain unclassified;
- activation would require multiple compensating changes.

Do not introduce source-specific date recovery solely for ESMA.

---

## Italian Tech Alliance

Status:

> **Deferred production-readiness candidate**

Strengths:

- Italian VC statistics;
- startup ecosystem;
- tech-transfer programmes;
- training opportunities;
- public RSS;
- reliable timestamps.

Weaknesses:

- feed dominated by thin press-clipping entries;
- repeated media references to the same underlying developments;
- descriptions often contain only the external publisher name;
- does not provide source-wide Milan/Bocconi evidence.

Keep under consideration.

Do not activate solely for publisher diversification.

---

## Assolombarda

Status:

> **Standby**

Strengths:

- established-company ecosystem;
- industrial policy;
- Milan/Lombardy economic intelligence.

Blockers:

- tested feeds lacked publication timestamps;
- descriptions were substantive copyrighted content;
- Centro Studi lacked a clean public feed.

Revisit only if a compliant low-complexity endpoint appears.

---

## Fintech District

Status:

> **Standby — structured-access limitation**

Strengths:

- Milan fintech;
- finance ecosystem;
- corporate innovation;
- professional-networking relevance.

Endpoint findings:

- WordPress API probes: unavailable;
- RSS/feed probes: unavailable;
- public sitemap exists;
- sitemap alone insufficient for previous-24-hours ingestion;
- site implemented as Next.js.

Do not reverse-engineer internal application APIs for the MVP.

---

## Camera di Commercio Milano Monza Brianza Lodi

Status:

> **Standby — access/architecture**

Strengths:

- local companies;
- business demography;
- Milan economic ecosystem;
- business initiatives.

Endpoint findings:

- tested RSS/feed/sitemap/robots endpoints returned Incapsula/Imperva interstitial HTML rather than usable structured content.

Do not bypass or automate around the access-control layer.

---

## Nasdaq

Status:

> **Standby**

Strategic value remains high for financial markets.

Current access/persistence terms do not justify production integration under the present architecture.

Revisit only if a clean public structured endpoint becomes available.

---

## Bruegel

Status:

> **Rejected / standby depending endpoint**

General RSS:

- rejected because event/session noise undermines product quality.

Analysis/Publications feeds:

- strategically useful but malformed;
- expose excessive/full-content payloads incompatible with the current persistence model.

Do not add a special parser solely for Bruegel.

---

## Ars Technica

Status:

> **Standby**

Strategically useful for independent technology scrutiny.

Current terms do not provide a sufficiently clean basis for permanent RSS-derived public persistence.

Revisit if terms or endpoint structure change.

---

## Il Sole 24 Ore

Status:

> **Standby**

Strategically strong for:

- Italy;
- companies;
- finance;
- economics.

Technically compatible feeds exist.

Current public Git persistence/licensing compatibility is not sufficiently clean.

The user has legitimate Bocconi access, but authenticated premium content must not be automated.

Revisit if a compliant low-complexity metadata-only path becomes available.

---

# Rejected or Non-Production Source Patterns

The following patterns should not be used in the core production system without a new explicit decision:

- authenticated premium scraping;
- Bocconi credential automation;
- JobGate automation;
- `yoU@B` automation;
- newsletter-email ingestion;
- full-page content scraping;
- hidden/internal application APIs discovered through reverse engineering;
- feeds exposing full copyrighted article bodies when persistence rights are unclear;
- event feeds whose publication timestamp is not a reliable actionability timestamp;
- sources requiring source-specific ranking compensation to remain usable.

---

# Source Evaluation Framework

Every candidate should be evaluated in this order.

## 1. Information Function

What missing role does the source solve?

If no differentiated role exists, stop.

## 2. Endpoint

Prefer:

1. RSS;
2. Atom;
3. official free API;
4. explicitly approved structured public source.

Avoid scraping when structured alternatives exist.

## 3. Automation Compatibility

Check:

- HTTP access;
- rate limits;
- authentication;
- anti-bot controls;
- format stability.

## 4. Persistence Compatibility

Check:

- description length;
- full-content exposure;
- copyright/licence;
- public-repository implications.

## 5. Real Collector Probe

Use the actual project collector.

Do not rely only on browser inspection.

## 6. Normalization

Check:

- title;
- URL;
- publication timestamp;
- description;
- language.

## 7. Product Quality

Inspect:

- originality;
- repetition;
- topic concentration;
- likely report value;
- noise.

## 8. Classification

Run real records through the current taxonomy.

Do not add source defaults or keywords before seeing actual misses.

## 9. Historical Regression

Before adding new keywords, search stored records for likely false positives.

## 10. Ranking Consequences

Check whether weak items receive disproportionate scores.

## 11. Production Decision

Choose:

- Active;
- Standby;
- Rejected;
- Manual/research layer;
- Deferred production-readiness candidate.

## 12. Minimal Implementation

If active, make the smallest coherent change.

## 13. Validation

Run:

- targeted tests;
- full tests;
- production-equivalent pipeline;
- report/output inspection;
- Git diff inspection.

---

# Source Addition Acceptance Criteria

A source should be activated only when:

- it solves a validated information-function gap;
- the endpoint is public and automation-compatible;
- persistence is safe;
- metadata is adequate;
- the generic collector can handle it or a generic improvement is independently justified;
- it does not require disproportionate source-specific logic;
- classification/ranking behaviour is acceptable;
- the report contribution is likely useful;
- recurring cost remains zero;
- maintenance burden is reasonable.

A source should be deferred when:

- the strategic value is high but the current endpoint or architecture is unsuitable;
- the information role is useful but redundant;
- metadata is too weak;
- the feed is excessively noisy;
- access/persistence conditions are unclear;
- activation requires one-off technical complexity.

---

# Current Source Expansion Policy

The active Phase 4 expansion cycle is closed for the current MVP boundary.

Future source work should not continue from a standing candidate queue.

Reopen source research only when one of the following is true:

1. repeated report use reveals a materially costly information gap;
2. a previously blocked high-value source exposes a cleaner public structured endpoint;
3. a source's licensing/persistence position materially improves;
4. a new information need is validated;
5. source concentration becomes a demonstrated report-quality problem.

Do not add sources merely because:

- a domain is imperfect;
- a prestigious publication exists;
- a candidate has not yet been tested;
- source count appears low.

The new default is:

> **Preserve the current source universe until real product use creates evidence for another change.**

---

# Current Information-Function Gaps

The following gaps remain known but are not Phase 4 blockers.

## Global Companies / Corporate Strategy

Status:

- sufficient MVP baseline;
- globally incomplete.

DG Competition validated the information function but not the production feed.

## Broader Financial Markets

Status:

- sufficient MVP baseline;
- strongest on monetary/rates evidence;
- market-structure and securities-supervision depth remains incomplete.

ESMA validated the information function but not the production architecture fit.

## Independent AI / Technology Scrutiny

Status:

- primary evidence diversified;
- independent scrutiny still incomplete.

Not currently a blocking gap.

## Independent Europe Interpretation

Status:

- institutional evidence strong;
- ISPI now adds geoeconomic interpretation;
- independent analytical depth remains incomplete.

## Milan Professional / Recruiting Ecosystem

Status:

- MVP-sufficient but incomplete.

Remaining gaps are constrained by:

- authenticated Career Services infrastructure;
- absent structured feeds;
- event/actionability semantics;
- unsuitable public endpoints;
- access-control barriers.

Future work should be triggered by demonstrated missed-opportunity cost.

---

# Report Context and Source Metadata

Richer report context is now an implemented information-policy requirement.

The report should let the reader understand the core development without immediate click-through when source metadata permits it.

Current production policy:

```text
source-provided normalized description
→ explicit Source context provenance
→ maximum 500-character display
→ complete-sentence preference when truncation is needed
→ word-boundary fallback
→ explicit fallback when context is unavailable
```

The 500-character bound is a presentation limit.

It does not change:

- the stored normalized description;
- classification evidence;
- ranking evidence;
- source selection;
- the 5-items-per-domain cap;
- the 30-items-total cap.

## Phase 5 Metadata Audit Findings

The source-metadata audit showed that the former 300-character limit was not the main context constraint across most sources.

Observed source patterns included:

```text
BBC World / BBC Business
→ concise descriptions, generally below 300 characters

European Commission Highlighted News
→ bounded descriptions, generally below 300 characters

OpenAI News
→ concise descriptions, generally below 300 characters

MIMIT News
→ short normalized descriptions

Tech Europe Foundation
→ descriptions commonly around 450–550 characters

Lavoce.info Imprese
→ descriptions around 330–360 characters

ISPI Geoeconomics
→ some descriptions above 300 characters

ECB
→ no usable description in the tested sample

Federal Reserve
→ descriptions often title-like

Google DeepMind
→ description availability partial
```

The audit also found richer RSS `content` fields for some sources, including:

- Istat;
- Tech.eu;
- Tech Europe Foundation;
- ISPI Geoeconomics.

Those fields were often thousands of characters long and body-like.

Current policy therefore rejects generic use of RSS `content` for report enrichment.

## Minimum Useful Context

Where the source provides sufficient metadata, source context should allow the reader to identify:

- the core development;
- the relevant actor or object;
- at least one material qualifier where available, such as:
  - scale;
  - consequence;
  - rationale;
  - next step;
  - constraint;
  - strategic or economic significance.

This is a manual product-quality rubric.

It is not an automated score.

## Provenance

The report label is:

```text
Source context
```

rather than:

```text
Summary
```

because the text is publisher/source-provided metadata and may be:

- a summary;
- an abstract;
- a teaser;
- a short description.

The system must not imply that the text is independently authored or AI-generated.

## Missing or Title-Duplicate Context

When the description is missing or duplicates the title, render:

```text
No additional source-provided context available.
```

This is intentionally transparent.

Do not fabricate context to make every report entry appear equally rich.

## Truncation Policy

Current maximum rendered source context:

```text
500 characters
```

If the description fits within the limit:

```text
render unchanged
```

If it exceeds the limit:

```text
prefer the last complete sentence within the bound
→ otherwise cut at the last word boundary
→ append ... for word-boundary truncation
```

The objective is to avoid awkward mid-word cuts while keeping report length bounded.

## Persistence Boundary

The richer-context requirement does not relax the public-repository persistence policy.

Do not generically persist or render:

- full article bodies;
- large RSS `content` payloads;
- authenticated premium content;
- first paragraphs scraped from article pages.

The current solution uses only the existing normalized feed description.

## Source-Quality Boundary

The system should not guess repairs to malformed publisher metadata.

During Phase 6 validation:

- BBC and OpenAI raw descriptions, normalized descriptions, persisted JSONL and Markdown files were confirmed correctly spaced;
- apparent joined words in copied terminal output were a presentation artefact rather than a pipeline defect;
- Tech.eu malformed spacing was confirmed to exist in the raw RSS description itself.

Current policy:

> **Do not add generic text-repair heuristics for defects that originate in publisher metadata or have not been reproduced in the system's own transformation layer.**

## Deferred Enrichment Methods

The following remain deferred:

- article-page metadata extraction;
- first-paragraph extraction;
- generic RSS body-content ingestion;
- LLM summarisation;
- a new persisted context field.

Reconsider them only if repeated real report use shows that the current bounded source-description approach creates material information loss.

---

# Future Architecture Gates

The following remain deferred unless validated by real use.

## Event / Deadline Model

Reconsider only if missed events or deadlines create meaningful user cost.

Evidence exists that article publication semantics are insufficient for some sources, but the architecture has not yet been justified.

## Source-Specific Timestamp Recovery

Reconsider only if multiple high-value sources independently justify a generic fallback.

## Near-Duplicate Clustering

Reconsider only if repeated report inspection shows meaningful redundancy.

## Entity Extraction

Reconsider only if company/person/entity-level workflows become necessary.

## Machine-Learned Classification

Reconsider only if deterministic classification demonstrably fails important use cases.

## LLM Summarisation

The current richer-context requirement has been satisfied without LLM summarisation.

Reconsider only if repeated real report use demonstrates a material context gap that cannot be solved through safer deterministic/public metadata.

Any future AI enhancement must remain:

- optional;
- non-core;
- zero-recurring-cost compatible;
- transparent;
- replaceable.

---

# Information-Policy Definition of Done for the MVP Boundary

The information universe is sufficient for the current MVP when:

- all ten strategic macroareas have implemented domains;
- each domain has at least a meaningful baseline information function or a documented public-source limit;
- no severe source-quality defect is knowingly contaminating the report;
- source roles are explicit;
- source-access and persistence boundaries are documented;
- major known gaps are visible rather than hidden;
- further source expansion has lower expected value than improving report usefulness.

This condition is now met.

This does **not** mean:

- all domains are complete;
- source diversity is optimal;
- all professional opportunities are captured;
- all premium sources are automated;
- no future source work is needed.

It means the information universe is strong enough to support the current richer-report MVP and evidence-driven future iteration.

---

# Changelog

## 2026-08-19 — Richer-Context Metadata and Persistence Policy Implemented

- Closed the richer-report metadata-design question for the current MVP.
- Replaced the former approximately 300-character report-description policy with a 500-character bounded `Source context` policy.
- Recorded that 300 characters was not the dominant context limitation across most sources, but unnecessarily truncated useful TEF, Lavoce.info and some ISPI descriptions.
- Added the Minimum Useful Context rubric for manual product-quality review.
- Added explicit `Source context` provenance rather than implying AI-generated or independently authored summaries.
- Added the transparent fallback `No additional source-provided context available.` for missing or title-duplicate descriptions.
- Recorded deterministic complete-sentence truncation with word-boundary fallback.
- Preserved existing 5-items-per-domain and 30-items-total report caps.
- Preserved existing classification, ranking and JSONL persistence semantics.
- Recorded that richer RSS `content` fields are not generically used because several tested sources expose body-like payloads thousands of characters long.
- Kept article-page extraction, first-paragraph extraction, generic RSS body-content ingestion, a new context field and LLM summarisation deferred.
- Added the source-quality boundary that malformed publisher metadata should not trigger speculative generic text repair.
- Recorded Phase 6 validation showing BBC/OpenAI spacing was correct through raw feed, normalized data, JSONL and Markdown, while malformed Tech.eu spacing originated in the raw RSS description.
- Confirmed 20 feed-fixture tests, 14 report tests and 122 full-suite tests passed.
- Confirmed a successful 13-source production-equivalent run with zero invalid records.
- Reframed future source or context work as evidence-triggered rather than automatically queued.

## 2026-08-18 — Thirteen-Source / Phase-4 Source-Research Closure

- Added ISPI Geoeconomics as the thirteenth active public RSS source.
- Kept ISPI at Tier 3 with no source-default domains and no new taxonomy terms.
- Validated ISPI through real collection, normalisation, classification, ranking, cadence/overlap review, full tests and a 13-source production-equivalent run.
- Confirmed 118 passing tests.
- Confirmed production-equivalent run with 13/13 successful sources, zero failed sources, zero invalid records and zero warnings.
- Kept ISPI Business Events on standby because publication timestamps do not reliably represent event/actionability dates.
- Audited DG Competition and kept it on standby because the broad official feed mixes high-value M&A/antitrust intelligence with routine State-aid items that score too strongly under current Europe classification; no clean narrow RSS route was found.
- Audited ESMA and kept it on standby because standard RSS timestamps are absent, description payloads are long, classification is distorted by incidental matches and activation would require multiple compensating changes.
- Deepened the Italian Tech Alliance audit and deferred activation because the live feed is dominated by thin press-clipping despite occasional strong programme/deadline items.
- Reassessed Milan/Bocconi public-source coverage.
- Confirmed Bocconi Career Services as a high-value manual/private complementary layer rather than an authenticated automation target.
- Kept Bocconi General News / Events outside the current production architecture because no sufficiently narrow structured public feed was established.
- Audited Fintech District and kept it on standby because no usable RSS/API was found and the public sitemap is insufficient for 24-hour article ingestion.
- Audited Camera di Commercio Milano Monza Brianza Lodi and kept it on standby because automated endpoint probes returned Incapsula/Imperva interstitials rather than usable structured content.
- Reclassified Milan/Bocconi as MVP-sufficient but deliberately incomplete, with a documented public-source/current-architecture ceiling for several remaining roles.
- Closed the active Phase 4 source-research cycle for the current MVP boundary.
- Set richer-report context design as the next information-policy priority.

## 2026-08-18 — Twelve-Source / Ten-Domain Checkpoint and First Gap-Driven Audit Batch Closeout

- Updated production state from eight to twelve active public RSS sources.
- Updated implemented taxonomy from nine to ten active domains.
- Implemented Italy as the tenth strategic macroarea.
- Added Federal Reserve Board Monetary Policy as a Tier 1 source with Economics/Macro source default.
- Added `FOMC`, `Federal Open Market Committee` and `discount rate` to Financial Markets after controlled testing and historical regression.
- Added MIMIT News as a Tier 1 Italy source.
- Added narrow Italian Companies/Corporate Strategy terms:
  - `tavoli di crisi`;
  - `accordo di sviluppo`;
  - `quadro industriale`;
  - `rilevanza strategica`.
- Added `inflazione` to Economics/Macro after MIMIT testing.
- Implemented generic HTML-to-text feed-description normalisation rather than a MIMIT-specific branch.
- Added Lavoce.info Imprese as a Tier 2 Italy source.
- Added:
  - `fusione e acquisizione`;
  - `piano industriale`;
  - `IA`;
  - `mercati dei capitali`.
- Validated the retained Lavoce keywords against historical processed records with zero unintended regressions.
- Added Google DeepMind News as a Tier 1 Artificial Intelligence source.
- Validated 100/100 DeepMind records as appropriate for the AI source default.
- Added no new DeepMind-specific keywords because existing classification was sufficient.
- Closed Nasdaq as standby under current access/persistence terms.
- Closed Bruegel general RSS as rejected for production because of event/session noise.
- Kept Bruegel Analysis and Publications on standby because malformed feeds also expose excessive/full-content payloads incompatible with current public persistence.
- Kept Assolombarda News and Comunicati stampa on standby because both tested feeds exposed 0/15 publication timestamps and substantive copyrighted descriptions.
- Kept Assolombarda Centro Studi in the manual/research layer because no public RSS/feed route was identified.
- Kept Ars Technica on standby because current terms do not provide a clean basis for permanent public-RSS persistence.
- Kept Federal Reserve Banking/Regulatory, MIMIT Incentives and Lavoce Banche e finanza on standby.
- Completed a real twelve-source production-equivalent run successfully on 18 August 2026 with:
  - twelve successful sources;
  - zero failed sources;
  - zero invalid records;
  - zero warnings.
- Reframed Financial Markets from "no dedicated source" to "dedicated monetary/rates evidence exists; broader market coverage remains incomplete."
- Reframed Companies/Corporate Strategy from a severe general gap to a materially improved but still globally incomplete domain.
- Reframed Artificial Intelligence from OpenAI-concentrated primary evidence to diversified OpenAI + DeepMind primary evidence, with independent scrutiny still missing.
- Reframed Italy from pending to implemented and useful, while preserving remaining maturity gaps.
- Retired the completed Nasdaq-to-DeepMind audit queue.
- Set the next source step as a fresh Career Agent research pass against current information-function gaps.
- Added an explicit Phase 4 crossover question: whether another source now has more expected product value than richer report context.

## 2026-08-17 — Source-Audit Consolidation, Milan/Bocconi Activation and New Expansion Queue

- Consolidated completed source-accessibility and policy research.
- Recorded the Bocconi access model and Premium Bocconi Exception.
- Implemented Tech Europe Foundation as the first Milan/Bocconi Ecosystem source.
- Added support for source-defined domains with empty keyword lists.
- Recorded Financial Times, Il Sole 24 Ore, Reuters, Bank of Italy, Bocconi and Italian Tech Alliance audit conclusions.
- Established the first gap-driven candidate queue:
  - Nasdaq;
  - Federal Reserve;
  - MIMIT;
  - Lavoce.info;
  - Bruegel;
  - Assolombarda;
  - Ars Technica;
  - Google DeepMind.
- Preserved richer-report implementation as deferred until the information universe is sufficiently mature.

## 2026-08-17 — Tech.eu Replacement and Financial Markets Activation

- Incorporated the first Career Agent strategic source/domain audit into Phase 4 priorities.
- Replaced Sifted with Tech.eu after controlled comparison.
- Recorded Tech.eu 20/20 description availability versus Sifted 0/24 in the tested samples.
- Activated Tech.eu as Tier 2 Europe with `default_domains: []`.
- Added `acquired` to Companies and Corporate Strategy after real M&A misses.
- Added `early-stage fund` and `funding market` to Startups and Venture Capital after controlled simulation.
- Removed generic `startup` after it promoted a low-value Tech.eu profile.
- Added `tariffs` after a relevant geopolitical trade story remained unclassified.
- Implemented Financial Markets with a conservative first keyword set.
- Validated taxonomy changes against the stored production regression corpus available at that checkpoint.
- Ran the real pipeline successfully on 17 August 2026 and manually inspected the resulting report.
- Recorded that high unclassified share is not itself a defect when excluded records are correctly low-value or out of scope.
- Recorded Milan and Bocconi Ecosystem as a validated product requirement.
- Added the narrow Premium Bocconi Exception while preserving the prohibition on authenticated automated ingestion.
- Preserved zero recurring cost, deterministic processing, public-repository safety and negligible daily manual work.

## 2026-08-14 — Source Accessibility, Bocconi Access and Expansion Policy

- Reconciled source policy with completed Phase 3 automation.
- Added metadata richness and reader accessibility as explicit source-quality dimensions.
- Added the two-axis distinction between automation suitability and reader accessibility.
- Recorded Bocconi Direct, SearchLib, Database and Public Web access modes.
- Recorded the three-layer information-access model.
- Prohibited production use of Bocconi credentials and authenticated premium scraping.
- Added the controlled source-expansion workflow.
- Marked Sifted for explicit review after production accessibility and metadata problems.
- Preserved richer-report implementation as a later phase after source/domain correction.

## 2026-08-11 — Phase 2 Real-Source Taxonomy and Source-Policy Validation

- Expanded the implementation from one sample source to seven validated public RSS sources.
- Expanded the implemented taxonomy from two to seven domains.
- Added the rule that source defaults represent genuine source-wide topical evidence rather than publisher categories.
- Removed broad defaults from BBC World, BBC Business, ECB and European Commission.
- Restricted Istat to Economics and Macroeconomics and OpenAI to Artificial Intelligence.
- Added `war`, `conflict` and `parliament` after real-record testing.
- Rejected overly broad politics keywords after false-positive review.
- Preserved conservative classification, exact deduplication and public-repository safety.

## 2026-08-11 — Phase 1 Taxonomy and Source-Policy Reconciliation

- Recorded implemented classification, ranking and duplicate policies.
- Replaced source-count targets with a smallest-credible-source strategy.
- Kept advanced geography, entity, content-type and clustering logic behind evidence from real reports.

## Initial Baseline

- Established the ten target topic domains.
- Defined source tiers and source inclusion/exclusion criteria.
- Defined classification, ranking and duplicate-reduction policy.
- Defined copyright and public-repository boundaries.