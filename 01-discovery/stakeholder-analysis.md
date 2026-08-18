# Stakeholder Analysis — Post-Offer Conversion Improvement

**Engagement:** ConsultLab
**Related:** [`project-brief.md`](project-brief.md) · [`../02-as-is/findings.md`](../02-as-is/findings.md)

*Stakeholders are identified from the roles evidenced in the event log (149 distinct
resources performing 24 activity types) and from the organisational roles a change
of this kind necessarily touches. Where a role is inferred rather than observed,
this is stated.*

---

## 1. Stakeholder register

| ID | Stakeholder | Role in the process | Interest in the change |
|---|---|---|---|
| S1 | Head of Retail Lending | Owns conversion and lending volume | Sponsor. Accountable for the 33.1% attrition rate |
| S2 | Operations Manager, Applications | Owns day-to-day handling capacity | Owns the follow-up backlog; any capacity change lands here |
| S3 | Application handlers (observed: 149 resources) | Perform assessment, completion, validation, follow-up calls | Directly affected. Workload and prioritisation change |
| S4 | Offer / underwriting team | Compose, issue and re-issue offers | Affected by any change to offer validity or re-issue rules |
| S5 | IT / Application Systems | Owns the case management system | Delivers any system change; owns feasibility and effort estimates |
| S6 | Data & MI team | Reports process performance | Supplies the measures the to-be process depends on |
| S7 | Risk & Compliance | Governs contact policy and credit decisioning | Constrains how and how often applicants may be contacted |
| S8 | Customer / applicant | Receives the offer, returns documents | Beneficiary. Not consulted directly; represented by proxy |
| S9 | Finance | Owns the business case | Approves investment; scrutinises the assumptions |

---

## 2. Power / interest grid

```text
        HIGH │  S5  IT & Systems          │  S1  Head of Retail Lending
     P       │  S7  Risk & Compliance     │  S2  Operations Manager
     O       │  S9  Finance               │
     W       ├────────────────────────────┼────────────────────────────
     E       │  S6  Data & MI             │  S3  Application handlers
     R  LOW  │                            │  S4  Offer team
             │                            │  S8  Customer (by proxy)
             └────────────────────────────┴────────────────────────────
                       LOW                          HIGH
                                  INTEREST
```

| Quadrant | Stakeholders | Engagement approach |
|---|---|---|
| High power / high interest | S1, S2 | Manage closely. Co-design the to-be process; validate findings before recommendation |
| High power / low interest | S5, S7, S9 | Keep satisfied. Consult early on feasibility, contact policy and financial assumptions; escalate only on constraints |
| Low power / high interest | S3, S4, S8 | Keep informed. Elicit requirements from handlers; represent the customer through behavioural evidence in the log |
| Low power / low interest | S6 | Monitor. Engage when defining to-be measures |

---

## 3. Stakeholder concerns and how the engagement addresses them

| Stakeholder | Likely concern | Response |
|---|---|---|
| S1 Head of Retail Lending | "Is this real money or an efficiency story?" | Business case states recovered lending and margin, not requested principal |
| S2 Operations Manager | "You're asking for more calls with the same headcount" | Options assessment includes reprioritisation and automation, not headcount alone |
| S3 Handlers | "More monitoring of our work" | Requirements target queue prioritisation, not individual performance measurement |
| S5 IT | "Another system request with no effort estimate" | Options scored on implementation effort and disruption, not benefit alone |
| S7 Risk & Compliance | "How often will applicants be contacted?" | Contact frequency treated as a constraint on the to-be design, set by policy |
| S9 Finance | "How conservative are these numbers?" | Recovery rate stated as an explicit assumption with a sensitivity range |

---

## 4. RACI — engagement deliverables

**R** Responsible · **A** Accountable · **C** Consulted · **I** Informed

| Deliverable | Analyst | S1 Lending | S2 Ops | S3 Handlers | S5 IT | S7 Risk | S9 Finance |
|---|---|---|---|---|---|---|---|
| As-is process model & findings | R | A | C | C | I | I | I |
| Business requirements document | R | A | C | C | C | C | I |
| User stories & acceptance criteria | R | I | C | C | C | I | — |
| Solution options assessment | R | A | C | I | C | C | C |
| To-be process model | R | A | C | C | C | C | I |
| Business case | R | C | I | — | I | I | A |
| Recommendation & roadmap | R | A | C | I | C | C | C |

*Finance is accountable for the business case; Retail Lending is accountable for
everything that defines or changes the process. The analyst is responsible
throughout — this engagement produces recommendations, not decisions.*

---

## 5. Elicitation approach

Direct stakeholder access is not available in this engagement, so requirements are
derived from evidence and stated as such. Where a technique would normally be used,
the substitute is recorded:

| BABOK technique | Normal use | Substitute used here |
|---|---|---|
| Interviews | Understand why applicants go quiet | Behavioural inference from the event log; assumption flagged as load-bearing |
| Observation | Understand how handlers prioritise queued work | Queue and processing times derived from lifecycle transitions |
| Document analysis | Compare documented process to practice | Process discovery from event data; 15,930 variants against any single documented path |
| Workshops | Validate the to-be design | Options assessment scored against stated criteria, presented for client validation |

**This is a limitation, not a shortcut.** Findings that would normally be confirmed
in interview are marked in `findings.md` as coincidence rather than causation, and
the recommendation is framed accordingly.
