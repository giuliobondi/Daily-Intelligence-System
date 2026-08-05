# Daily Intelligence System — System Architecture

> **Purpose**
>
> This document defines how the Daily Intelligence System will satisfy the approved product requirements.
>
> It describes the system components, data flow, configuration, storage, automation, failure handling and public-repository boundaries.
>
> It defines the intended architecture without locking the project into unnecessary implementation complexity.
>
> ---
>
> **Primary Question**
>
> > *How should the system collect, process, store and publish information reliably at zero recurring cost and with negligible daily manual work?*
>
> ---
>
> **Update Frequency**
>
> Update when a material architectural decision changes the system’s components, data flow, storage, automation, security boundaries or operational model.

---

# Architectural Objective

The architecture should support one complete daily workflow:

```text
Configured public sources
        ↓
Collection
        ↓
Record normalisation
        ↓
Validation
        ↓
Duplicate reduction
        ↓
Domain classification
        ↓
Relevance scoring
        ↓
Processed storage
        ↓
Daily Markdown report
        ↓
Automated persistence
        ↓
Visible run status