# Requirements Traceability Matrix

**Engagement:** ConsultLab — Post-Offer Conversion Improvement
**Related:** [BRD](BRD.md) · [User stories](user-stories.md) · [As-is findings](../02-as-is/findings.md) · [Project brief](../01-discovery/project-brief.md)

*Every requirement traces backwards to an objective and to evidence, and forwards
to a story and a validation method. A requirement that cannot trace backwards is
unjustified; one that cannot trace forwards is unverifiable.*

---

## 1. Objectives

| ID | Objective |
|---|---|
| O1 | Establish why applications are lost after an offer is issued |
| O2 | Determine whether follow-up timing measurably affects conversion |
| O3 | Define a practical intervention within the window in which an offer is live |
| O4 | Quantify the recoverable value on stated, conservative assumptions |
| O5 | Specify the change in requirements a delivery team could act on |

## 2. Evidence

| ID | Finding | Source |
|---|---|---|
| E1 | 33.1% of applications cancelled after offer issue (10,431 cases) | findings.md §2 |
| E2 | 9.2% of cancelled applications returned documents | findings.md §2 |
| E3 | Median 31.6 days to cancellation vs 14.8 days to acceptance | findings.md §2 |
| E4 | `W_Call after offers` holds 65.5% of all queue time (40,321 days) | findings.md §3 |
| E5 | Processing time for that activity is 181 days — the work is fast, the wait is not | findings.md §3 |
| E6 | 73.4% of successful applications enter the incompleteness loop, +5.6 days each | findings.md §4 |
| E7 | 15,930 distinct process variants; no path exceeds 3.4% of cases | findings.md §1 |
| E8 | Cancellation reason is not recorded in the log | findings.md, Limitations |

---

## 3. Traceability

| Requirement | Objective | Evidence | Functional | Story | Priority | Validation |
|---|---|---|---|---|---|---|
| BR-01 Offer-stage visibility | O1 | E1, E3 | FR-01, FR-02 | US-01 | M | Live offers and elapsed time visible on demand |
| BR-02 Risk-based prioritisation | O2, O3 | E4, E5 | FR-03, FR-04 | US-03 | M | Queue order demonstrably differs from arrival order |
| BR-03 Identify non-response while offer is live | O3 | E1, E2, E3 | FR-02, FR-05 | US-04 | M | Action raised before offer lapses, not at closure |
| BR-04 Offer-stage measurement | O1, O4 | E1, E3 | FR-01, FR-10 | US-02 | M | Baseline and current measures reportable |
| BR-05 Non-handler applicant reminder | O3 | E4, E5 | FR-06 | US-05 | S | Reminder issued with no handler action |
| BR-06 Distinguish declined from non-responsive | O1 | E8 | FR-07 | US-06 | S | Cancellations separately countable by reason |
| BR-07 Documentation clarity before validation | O2 | E6 | FR-08 | US-07 | S | Applicant confirms receipt against checklist |
| BR-08 Contact within compliance limits | — | Stakeholder S7 | FR-09 | US-05 | M | Contact frequency enforced and auditable |
| BR-09 Measures in management reporting | O4 | E1 | FR-10 | US-02 | C | Report produced without manual extraction |

---

## 4. Coverage checks

**Every objective is addressed**

| Objective | Requirements |
|---|---|
| O1 | BR-01, BR-04, BR-06, BR-09 |
| O2 | BR-02, BR-07 |
| O3 | BR-02, BR-03, BR-05 |
| O4 | BR-04, BR-09 |
| O5 | Satisfied by this specification as a whole |

**Every finding is either acted on or explicitly deferred**

| Evidence | Disposition |
|---|---|
| E1, E2, E3 | Addressed — BR-01, BR-03, BR-04 |
| E4, E5 | Addressed — BR-02, BR-05 |
| E6 | Partially addressed — BR-07. Full remedy deferred: the log does not record *what* was incomplete |
| E7 | Not addressed. Process variance is context, not an opportunity; noted in the project brief as out of scope |
| E8 | Addressed — BR-06 |

**Every functional requirement traces to a business requirement**

FR-01 → BR-01, BR-04 · FR-02 → BR-01, BR-03 · FR-03 → BR-02 · FR-04 → BR-02 ·
FR-05 → BR-03 · FR-06 → BR-05 · FR-07 → BR-06 · FR-08 → BR-07 · FR-09 → BR-08 ·
FR-10 → BR-04, BR-09

No orphans in either direction.

---

## 5. Open items carried into the to-be design

| # | Item | Why it is open |
|---|---|---|
| 1 | Whether follow-up timing causally affects conversion | The log establishes co-occurrence only; BR-02 and BR-05 rest on this assumption |
| 2 | The elapsed-time threshold for intervention | Requires either an A/B trial or client input; not derivable from the log |
| 3 | The realistic recovery rate for lapsed offers | Load-bearing for the business case; must be stated as an assumption with a sensitivity range |
| 4 | Contact-frequency limits | Set by Risk & Compliance; constrains BR-05 and BR-08 |
