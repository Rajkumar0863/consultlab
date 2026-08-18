# Business Requirements Document

**Engagement:** ConsultLab — Post-Offer Conversion Improvement
**Version:** 1.0
**Author:** Rajkumar Vijayan
**Related:** [Project brief](../01-discovery/project-brief.md) · [Stakeholder analysis](../01-discovery/stakeholder-analysis.md) · [As-is findings](../02-as-is/findings.md)

---

## 1. Purpose

This document specifies what the business needs in order to reduce the loss of
loan applications after an offer has been issued. It states requirements, not
solutions: each requirement describes an outcome the business needs, leaving the
means of achieving it to the options assessment in `04-to-be`.

Requirements are documented in line with BABOK v3 and are traceable to the
business objectives in the project brief and to the evidence in the as-is
findings.

---

## 2. Business need

Of 31,509 applications, 10,431 (33.1%) are cancelled after a formal offer has
been issued. All had received an offer; only 9.2% ever returned documentation.
The median cancelled application is closed 31.6 days after submission.

The activity intended to re-engage these applicants — the post-offer follow-up
call — holds 65.5% of all queue time in the process: 40,321 days of waiting
against 181 days of handling.

The business has no measure of offer-stage performance and no mechanism for
identifying which live offers are at risk while the offer is still open.

---

## 3. Scope of this specification

**Covered:** the period between an offer being issued and the application
reaching a final outcome; the prioritisation and scheduling of follow-up
contact; the measurement of offer-stage performance.

**Not covered:** credit risk policy, pricing, lead acquisition, and full system
replacement. The document-incompleteness loop is addressed only where it affects
post-offer conversion (see BR-07).

---

## 4. Business requirements

Priority: **M** must have · **S** should have · **C** could have

| ID | Requirement | Priority | Objective | Evidence |
|---|---|---|---|---|
| BR-01 | The business must be able to see, at any time, which issued offers are live, how long each has been open, and whether the applicant has responded | M | O1 | No offer-stage visibility exists; 33.1% attrition is undetected until closure |
| BR-02 | Follow-up contact must be prioritised by the risk of the offer lapsing, rather than handled in arrival order | M | O2, O3 | `W_Call after offers` holds 65.5% of queue time; work accumulates faster than it is served |
| BR-03 | The business must be able to identify a non-responding applicant while the offer is still live, not at the point of closure | M | O3 | Median 31.6 days to cancellation; closure is same-day once triggered |
| BR-04 | Offer-stage performance must be measurable — response rate, time to first contact, conversion by segment | M | O1, O4 | No baseline currently exists against which improvement could be shown |
| BR-05 | Applicants must be able to be reminded of an outstanding offer through a channel that does not consume handler capacity | S | O3 | Handler capacity is finite; 40,321 queue-days cannot be served by reprioritisation alone |
| BR-06 | The business must be able to distinguish applicants who declined from those who did not respond | S | O1 | The log records only cancellation; the reason is not captured, limiting root-cause analysis |
| BR-07 | Applicants must be told what documentation is required, and whether what they submitted was sufficient, before validation | S | O2 | 73.4% of successful applications enter the incompleteness loop; 9.2% of cancelled applications also entered it |
| BR-08 | Contact frequency and channel must remain within the limits set by Risk & Compliance | M | — | Constraint from S7; any solution must be compliant by design |
| BR-09 | Offer-stage measures must be available to management reporting without manual extraction | C | O4 | MI team (S6) currently has no offer-stage feed |

---

## 5. Functional requirements

| ID | Requirement | Traces to |
|---|---|---|
| FR-01 | The system shall record the timestamp at which each offer is issued and at which each applicant response is received | BR-01, BR-04 |
| FR-02 | The system shall calculate, for each live offer, the elapsed time since issue | BR-01, BR-03 |
| FR-03 | The system shall assign a risk indicator to each live offer based on elapsed time and response status | BR-02, BR-03 |
| FR-04 | The system shall present the follow-up work queue ordered by risk indicator rather than by creation date | BR-02 |
| FR-05 | The system shall trigger a defined action when a live offer passes a configurable elapsed-time threshold | BR-03, BR-05 |
| FR-06 | The system shall support at least one automated applicant reminder that does not require handler action | BR-05 |
| FR-07 | The system shall capture a reason code when an application is cancelled, distinguishing declined from non-responsive | BR-06 |
| FR-08 | The system shall present the applicant with a documentation checklist at submission and confirm receipt against it | BR-07 |
| FR-09 | The system shall enforce configurable limits on contact frequency per applicant | BR-08 |
| FR-10 | The system shall expose offer-stage measures through the existing reporting layer | BR-04, BR-09 |

---

## 6. Non-functional requirements

| ID | Category | Requirement | Rationale |
|---|---|---|---|
| NFR-01 | Timeliness | Offer status and risk indicators shall reflect events within one working day | A daily cycle is sufficient against a 31.6-day window; real-time adds cost without benefit |
| NFR-02 | Usability | The prioritised queue shall be usable by existing handlers without additional training beyond a briefing | Adoption by 149 resources; training cost affects the options assessment |
| NFR-03 | Compliance | All applicant contact shall be auditable — channel, time, outcome | Risk & Compliance (S7) constraint |
| NFR-04 | Data quality | Offer and response timestamps shall be complete for all live offers | The measures in BR-04 are unusable if the underlying events are missing |
| NFR-05 | Interoperability | The solution shall operate against the existing case management system without replacing it | Full replacement is out of scope per the project brief |
| NFR-06 | Capacity | The solution shall not increase total follow-up handling effort | Handler capacity is fixed; benefit must come from prioritisation or automation |

---

## 7. Assumptions

- Offer issue and applicant response events are recorded with reliable timestamps.
- Handler capacity is fixed for the purposes of this specification.
- Non-response is the dominant cause of cancellation. This is inferred from
  behavioural evidence, not confirmed by applicant contact, and is the
  load-bearing assumption of BR-02, BR-03 and BR-05.
- Contact-policy limits exist and can be obtained from Risk & Compliance.

## 8. Constraints

- No applicant or handler contact was available during this engagement;
  requirements derive from event-log evidence and documented process behaviour.
- The log does not record the content of incomplete documentation, limiting the
  specificity of BR-07.
- No cost data is available; effort and cost estimates are established in the
  options assessment, not here.

## 9. Out of scope

Credit risk policy and underwriting criteria · pricing and product design ·
marketing and lead acquisition · organisational restructuring · replacement of
the case management system.

---

## 10. Acceptance

This document is complete when every business requirement traces to a stated
business objective and to evidence in the as-is findings, and when every
functional requirement traces to a business requirement. That mapping is
maintained in the [requirements traceability matrix](traceability-matrix.md).
