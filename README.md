# ConsultLab — Loan Application Process Diagnostic

> A business analysis engagement diagnosing rework and delay in a loan application process — and setting out a technology-enabled recommendation with a quantified business case.

**Status:** 🚧 In development — target completion [DATE]
*(Delete this line when the engagement is complete. Do not publish quantified claims below until they are produced.)*

---

## Executive Summary

A process diagnostic of **[N] loan applications** from a European financial institution, using process mining to reconstruct the as-is process directly from system event data. The analysis identified **[X]% of applications entering a document-rework loop**, adding an average of **[Y] days** to end-to-end cycle time, and sets out a prioritised solution recommendation worth an estimated **[€Z]** in annual operational saving.

Delivered as a full business analysis pack: as-is and to-be process models, a requirements specification, a weighted options assessment, and an executive recommendation deck.

---

## The Client Problem

A retail lending function processes loan applications submitted through an online channel. Leadership can see application volumes and approval rates, but has no visibility into **where time is lost between submission and decision** — or how much of the handling effort is spent re-doing work that should have completed first time.

**The question:** where is cycle time being lost, what is causing it, and what should the business change?

---

## Business Questions

1. What does the loan application process actually look like in practice, as opposed to how it is documented?
2. Where are the bottlenecks, and how much cycle time does each cost?
3. How much of total handling effort is rework rather than first-pass work?
4. Which intervention — process redesign, automation, or system change — delivers the most benefit for the least disruption?

---

## The Data

**Source:** BPI Challenge 2017 event log — a real loan application process from a Dutch financial institution, covering applications filed through an online system in 2016 and their subsequent events.
4TU.ResearchData · DOI `10.4121/uuid:5f3067df-f10b-45da-b98b-86ae4c7a310b`

- **[N]** applications | **[M]** recorded events | **[R]** distinct resources
- Event log format: XES, converted to a pandas event table for analysis
- The raw log is excluded from this repository (see `.gitignore`); download it from the source above

### Scope and assumptions

- [Scope decision — e.g. analysis limited to the application sub-process; offer sub-process excluded]
- [Incomplete cases at the log boundary excluded — state count]
- [Cost assumptions used in the business case, with source]

---

## Approach

```text
Event log
    ↓
Process discovery (as-is)
    ↓
Bottleneck & rework analysis
    ↓
Root-cause analysis
    ↓
Requirements definition
    ↓
Solution options assessment
    ↓
To-be process + business case
    ↓
Recommendation
```

1. **Discover** — reconstructed the as-is process from the event log using process mining, rather than from documentation or assumption.
2. **Measure** — computed end-to-end cycle time, per-activity waiting time, and rework frequency across all cases.
3. **Diagnose** — isolated the highest-cost bottleneck and traced it to root cause.
4. **Specify** — translated the diagnosis into business and functional requirements with acceptance criteria.
5. **Assess** — scored three solution options against weighted criteria.
6. **Recommend** — packaged the outcome into an executive deck with an implementation roadmap.

---

## Key Findings

- **Cycle time:** median [X] days, 90th percentile [Y] days — a [Z]-fold spread between typical and worst-case handling.
- **Rework:** **[X]%** of applications enter a document resubmission loop, consuming an estimated **[Y]%** of total handling effort.
- **Bottleneck:** [activity name] accounts for **[X]%** of total waiting time, driven by [root cause].
- **Variation:** the process runs through **[N] distinct path variants**, against [N] documented in the process manual — evidence of undocumented workaround behaviour.
- **Opportunity:** an estimated **[€Z] per year**, on deliberately conservative assumptions stated in the business case.

---

## Recommendation

**[One-sentence recommendation — the single thing the business should do.]**

| Option | Description | Benefit | Cost | Disruption | Score |
|---|---|---|---|---|---|
| A — Process redesign | [ ] | [ ] | [ ] | [ ] | [ ] |
| B — Targeted automation | [ ] | [ ] | [ ] | [ ] | [ ] |
| C — System replacement | [ ] | [ ] | [ ] | [ ] | [ ] |

**Selected: [Option].** [Two sentences on why this option over the others — the trade-off, not just the benefit.]

### Implementation roadmap

| Phase | Duration | Activities | Outcome |
|---|---|---|---|
| Phase 1 | [ ] | [ ] | [ ] |
| Phase 2 | [ ] | [ ] | [ ] |
| Phase 3 | [ ] | [ ] | [ ] |

---

## Deliverables

| # | Deliverable | Location |
|---|---|---|
| 1 | Project brief & business case | [`01-discovery/project-brief.md`](01-discovery/) |
| 2 | Stakeholder map & RACI | [`01-discovery/stakeholder-analysis.md`](01-discovery/) |
| 3 | As-is process model (BPMN) | [`02-as-is/`](02-as-is/) |
| 4 | Process mining analysis | [`02-as-is/process-discovery.ipynb`](02-as-is/) |
| 5 | Business requirements document | [`03-requirements/BRD.md`](03-requirements/) |
| 6 | User stories & traceability matrix | [`03-requirements/`](03-requirements/) |
| 7 | To-be process model & options assessment | [`04-to-be/`](04-to-be/) |
| 8 | Recommendation deck | [`05-deliverables/`](05-deliverables/) |

---

## Methods & Tools

`Process Mining` · `BPMN` · `Requirements Elicitation` · `Stakeholder Analysis` · `Root-Cause Analysis` · `Options Assessment` · `Business Case Development`

`Python` · `pm4py` · `pandas` · `Power BI` · `BPMN modelling`

Requirements are documented in line with **BABOK v3** terminology and structure.

---

## Repository Structure

```text
consultlab/
├── 01-discovery/        Project brief, stakeholder map, RACI
├── 02-as-is/            Process mining notebook, as-is BPMN
├── 03-requirements/     BRD, user stories, traceability matrix
├── 04-to-be/            To-be BPMN, options assessment, business case
├── 05-deliverables/     Recommendation deck, implementation roadmap
├── data/                Event log (excluded — see source above)
└── requirements.txt
```

## Running the Analysis

```bash
pip install -r requirements.txt
jupyter notebook 02-as-is/process-discovery.ipynb
```

---

## What This Project Demonstrates

Business analysis applied end to end: taking an ambiguous operational problem, establishing what is actually happening from system evidence, translating the diagnosis into specified requirements, and arriving at a recommendation a business could act on.

---

## Author

**Rajkumar Vijayan**
MSc Software Development (International Systems), University of Limerick
[LinkedIn](https://linkedin.com/in/rajkumar-vijayan-0135a8338/) · vijayanrajkumar478@gmail.com

---

*Data source: van Dongen, B.F. (2017). BPI Challenge 2017. 4TU.ResearchData. Used for educational and portfolio purposes.*
