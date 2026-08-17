# ConsultLab — Loan Application Process Diagnostic

> A business analysis engagement: reconstructing a real loan application process from system event data, diagnosing where cycle time and rework are lost, and specifying a technology-enabled recommendation with a quantified business case.

**🚧 Status: in development.** This repository is being built in the open, deliverable by deliverable. Findings and figures will be published here as they are produced — nothing is claimed ahead of the work.

---

## The Engagement

A retail lending function processes loan applications submitted through an online channel. Leadership can see application volumes and approval rates, but has no visibility into **where time is lost between submission and decision**, or how much handling effort goes into re-doing work that should have completed first time.

**The question:** where is cycle time being lost, what is causing it, and what should the business change?

Rather than model the process from documentation or assumption, this engagement uses **process mining** to reconstruct what actually happens from the system's own event log — then treats the gap between the documented process and the real one as the finding.

---

## Business Questions

1. What does the loan application process look like in practice, as opposed to how it is documented?
2. Where are the bottlenecks, and how much cycle time does each cost?
3. How much of total handling effort is rework rather than first-pass work?
4. Which intervention — process redesign, targeted automation, or system change — delivers the most benefit for the least disruption?

---

## Data

**BPI Challenge 2017** — a real event log from the loan application process of a Dutch financial institution, covering applications filed through an online system in 2016 and their subsequent events.

4TU.ResearchData · DOI `10.4121/uuid:5f3067df-f10b-45da-b98b-86ae4c7a310b`

The raw log is excluded from this repository (see `.gitignore`) and should be downloaded from the source above.

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

---

## Planned Deliverables

| # | Deliverable | Status |
|---|---|---|
| 1 | Project brief & business case | ⬜ Not started |
| 2 | Stakeholder map & RACI | ⬜ Not started |
| 3 | As-is process model (BPMN) | ⬜ Not started |
| 4 | Process mining analysis | ⬜ Not started |
| 5 | Business requirements document | ⬜ Not started |
| 6 | User stories & traceability matrix | ⬜ Not started |
| 7 | To-be process & options assessment | ⬜ Not started |
| 8 | Recommendation deck & roadmap | ⬜ Not started |

*Update each row to 🟨 In progress / ✅ Complete as work lands.*

---

## Repository Structure

```text
consultlab/
├── 01-discovery/        Project brief, stakeholder map, RACI
├── 02-as-is/            Process mining analysis, as-is BPMN
├── 03-requirements/     BRD, user stories, traceability matrix
├── 04-to-be/            To-be BPMN, options assessment, business case
├── 05-deliverables/     Recommendation deck, implementation roadmap
├── data/                Event log (excluded — see source above)
└── requirements.txt
```

---

## Methods & Tools

`Process Mining` · `BPMN` · `Requirements Elicitation` · `Stakeholder Analysis` · `Root-Cause Analysis` · `Options Assessment` · `Business Case Development`

`Python` · `pm4py` · `pandas` · `Power BI`

Requirements are documented in line with **BABOK v3** terminology and structure.

---

## Why This Project

Analytics answers *what is happening*. Business analysis has to go further — establish *why*, specify *what should change*, and make the case for it in terms a business will act on. This engagement is built to demonstrate that full path, and to produce the artifacts a business analyst is actually accountable for: process models, requirements, options assessments and a recommendation.

---

## Author

**Rajkumar Vijayan**
MSc Software Development (International Systems), University of Limerick
[LinkedIn](https://linkedin.com/in/rajkumar-vijayan-0135a8338/) · vijayanrajkumar478@gmail.com

---

*Data source: van Dongen, B.F. (2017). BPI Challenge 2017. 4TU.ResearchData. Used for educational and portfolio purposes.*
