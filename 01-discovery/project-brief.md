# Project Brief — Post-Offer Conversion Improvement

**Engagement:** ConsultLab
**Client (simulated):** Retail lending function, European financial institution
**Analyst:** Rajkumar Vijayan
**Evidence base:** BPI Challenge 2017 event log (31,509 applications, Jan 2016 – Feb 2017)
**Status:** Initiated following as-is process discovery — see [`02-as-is/findings.md`](../02-as-is/findings.md)

---

## 1. Background

The lending function receives loan applications through an online channel, assesses
them, and issues offers to approved applicants. Application volumes and approval
rates are visible to management, but performance after an offer is issued is not.
No measure currently exists for how long an offer stays live, how many applicants
respond, or how many are lost while an offer remains open.

Process discovery was carried out against thirteen months of system event data to
establish what the process does in practice. That work is complete and its findings
form the evidence base for this brief.

---

## 2. Problem statement

**Of 31,509 applications, 10,431 (33.1%) are cancelled after a formal offer has been
issued. Fewer than one in ten of those applicants ever returns documentation.**

The loss occurs after the lender has completed the costly part of the process —
assessment, credit decision, and offer preparation. The median cancelled application
is closed 31.6 days after submission, roughly twice the 14.8 days taken by one that
converts.

Alongside this, the activity intended to re-engage applicants after an offer is sent
(`W_Call after offers`) holds **65.5% of all queue time in the process** — 40,321
days of accumulated waiting against 181 days of actual handling. The intervention
designed for this failure mode is the most under-served task in the process.

These two facts coincide. The event log does not establish that the follow-up
backlog causes the attrition, and this engagement does not assume it does; testing
that link is within scope.

---

## 3. Business objectives

| # | Objective |
|---|---|
| O1 | Establish why applications are lost after an offer is issued |
| O2 | Determine whether follow-up timing measurably affects conversion |
| O3 | Define a practical intervention within the window in which an offer is live |
| O4 | Quantify the recoverable value on stated, conservative assumptions |
| O5 | Specify the change in requirements a delivery team could act on |

---

## 4. Success measures

The engagement is successful if it delivers:

| Measure | Target |
|---|---|
| M1 | A root-cause account of post-offer attrition, evidenced or explicitly bounded by what the data can support |
| M2 | A to-be process addressing the identified cause, modelled in BPMN |
| M3 | A quantified opportunity with every assumption stated and sourced |
| M4 | A requirements set traceable to the business objectives above |
| M5 | A recommendation with a costed implementation roadmap |

Operational measures the client would track post-implementation — reduction in
cancellation rate, reduction in median time to first follow-up contact — are
proposed in the to-be design rather than fixed here, since baselines depend on the
option selected.

---

## 5. Scope

### In scope

- The application lifecycle from submission to final outcome (accepted, denied, cancelled)
- The offer sub-process: creation, issue, response, and closure
- Follow-up and contact activities performed after an offer is sent
- Document submission and validation, insofar as they affect conversion
- Process and system change; capacity and scheduling of follow-up work

### Out of scope

- Credit risk policy and underwriting criteria. Applications declined on credit
  grounds are a policy matter, not a process matter.
- Pricing and product design. Whether an offer is competitive is a commercial
  question this analysis cannot address from event data.
- Marketing and lead acquisition upstream of application submission.
- Organisational or staffing structure beyond the scheduling of follow-up work.
- Full technology replacement. The engagement assesses replacement as an option
  but does not scope a system procurement.

### Explicitly deferred

The rework loop identified in the as-is findings — 73.4% of successful applications
delayed 5.6 days each by document incompleteness, totalling 70,868 application-days
— is a genuine and quantified inefficiency. It is deferred because its remedy
depends on knowing *what* was incomplete, which the available data does not record,
and because its benefit is cycle-time reduction on applications that already
convert. It is carried into the requirements as a secondary consideration and
flagged for a follow-on engagement.

---

## 6. Approach

| Phase | Activity | Output |
|---|---|---|
| 1 | Process discovery and diagnosis | `02-as-is/findings.md` ✅ |
| 2 | Stakeholder and process modelling | Stakeholder analysis, as-is BPMN |
| 3 | Requirements definition | BRD, user stories, traceability matrix |
| 4 | Solution options assessment | Weighted options assessment, to-be BPMN |
| 5 | Business case and recommendation | Business case, recommendation deck, roadmap |

---

## 7. Assumptions

- The event log is a complete and accurate record of system activity for the period.
- The process observed in 2016–17 is representative of current operation.
- Cancellation reflects applicant non-response rather than deliberate withdrawal,
  in the majority of cases. This assumption is load-bearing and is tested in the
  root-cause analysis.
- Staff capacity for follow-up work is finite and cannot be increased without cost.

---

## 8. Constraints

- Analysis is limited to system event data. Applicant motivation, contact-attempt
  outcomes, and the content of incomplete documentation are not recorded.
- No access to staff, applicants, or the client's own process documentation, so
  elicitation techniques requiring stakeholder contact are simulated rather than
  performed.
- No cost data. The business case therefore works from stated assumptions rather
  than client financials, and presents a range rather than a point estimate.

---

## 9. Key risks

| Risk | Impact | Mitigation |
|---|---|---|
| The follow-up backlog is a symptom of volume rather than a cause of attrition | Recommendation targets the wrong lever | Test the link in root-cause analysis; state the limit of what the data proves |
| Requested loan principal (€166.0m across cancelled applications) is mistaken for opportunity | Business case is indefensible | Value stated only as recovered lending × margin, with the recovery rate as an explicit assumption |
| Scope expands into credit policy | Engagement loses focus | Scope boundary stated above and held |

---

## 10. Deliverables

1. Stakeholder analysis and RACI
2. As-is process model (BPMN) — supported by `02-as-is/findings.md`
3. Business requirements document
4. User stories with acceptance criteria
5. Requirements traceability matrix
6. Solution options assessment
7. To-be process model (BPMN)
8. Business case
9. Recommendation deck and implementation roadmap
