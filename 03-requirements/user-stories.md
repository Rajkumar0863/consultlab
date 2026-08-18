# User Stories & Acceptance Criteria

**Engagement:** ConsultLab — Post-Offer Conversion Improvement
**Related:** [BRD](BRD.md) · [Traceability matrix](traceability-matrix.md)

*Acceptance criteria are written in Given / When / Then form. Stories are grouped
by the outcome they serve, not by system component.*

---

## Epic 1 — See what is happening at the offer stage

### US-01 — Offer pipeline visibility
**As an** Operations Manager
**I want** to see every live offer with the time elapsed since it was issued
**So that** I can tell how much value is sitting unresolved before it lapses

*Traces to: BR-01, FR-01, FR-02*

**Acceptance criteria**
- Given an offer has been issued and no final outcome recorded, when I open the offer view, then the offer appears with its elapsed time since issue.
- Given an applicant has responded, when I open the offer view, then the offer is shown as responded and is no longer counted as awaiting response.
- Given an application reaches a final outcome, when I open the offer view, then that offer no longer appears in the live list.
- Given offer data is refreshed daily, when I open the view, then the displayed status is no more than one working day old.

---

### US-02 — Offer-stage performance measures
**As a** Head of Retail Lending
**I want** offer-stage response and conversion rates reported against a baseline
**So that** I can tell whether a change has improved conversion

*Traces to: BR-04, BR-09, FR-01, FR-10*

**Acceptance criteria**
- Given a reporting period, when I request offer-stage measures, then I receive response rate, median time to first contact, and conversion rate for that period.
- Given a baseline period has been established, when I view current measures, then they are presented against that baseline.
- Given measures are requested, when the report is produced, then no manual data extraction is required.

---

## Epic 2 — Act before the offer lapses

### US-03 — Risk-prioritised follow-up queue
**As an** Application Handler
**I want** my follow-up queue ordered by which offers are most at risk of lapsing
**So that** I spend my available time where it changes the outcome

*Traces to: BR-02, FR-03, FR-04*

**Acceptance criteria**
- Given multiple offers awaiting follow-up, when I open my queue, then offers are ordered by risk indicator rather than creation date.
- Given an offer's elapsed time increases, when the queue refreshes, then its position rises accordingly.
- Given an applicant has responded, when the queue refreshes, then that offer is removed from the follow-up queue.
- Given I complete a follow-up contact, when I record the outcome, then the offer's risk indicator is recalculated.

---

### US-04 — Threshold-triggered intervention
**As an** Operations Manager
**I want** a defined action to trigger when an offer passes an age threshold
**So that** no live offer goes unattended purely because the queue was long

*Traces to: BR-03, FR-05*

**Acceptance criteria**
- Given a configurable elapsed-time threshold, when a live offer passes it, then a follow-up action is created for that offer.
- Given the threshold is changed, when the next cycle runs, then the new threshold is applied without code change.
- Given an offer already has an open follow-up action, when the threshold is passed again, then a duplicate action is not created.

---

### US-05 — Automated applicant reminder
**As an** Applicant
**I want** a reminder that my offer is open and what I need to do next
**So that** I do not lose an approved offer through inattention

*Traces to: BR-05, BR-08, FR-06, FR-09*

**Acceptance criteria**
- Given an offer is live and unresponded at a defined interval, when the reminder cycle runs, then the applicant receives a reminder stating the outstanding action.
- Given contact-frequency limits are configured, when a reminder would exceed them, then it is suppressed and the suppression recorded.
- Given the applicant has responded, when the reminder cycle runs, then no reminder is sent.
- Given a reminder is sent, when I check the case record, then the channel, time and outcome are recorded.

---

## Epic 3 — Understand why applications are lost

### US-06 — Cancellation reason capture
**As a** Business Analyst
**I want** cancellations to distinguish declined from non-responsive
**So that** future analysis can address the right cause

*Traces to: BR-06, FR-07*

**Acceptance criteria**
- Given an application is cancelled, when the closure is recorded, then a reason code is required.
- Given reason codes exist, when I report on cancellations, then declined and non-responsive are separately countable.
- Given a reason is not known, when closure is recorded, then an explicit "unknown" value is captured rather than a blank.

---

### US-07 — Documentation clarity at submission
**As an** Applicant
**I want** to know exactly what documentation is required and whether mine was accepted
**So that** my application is not delayed by an avoidable resubmission

*Traces to: BR-07, FR-08*

**Acceptance criteria**
- Given I am submitting an application, when I reach the documentation step, then I am shown a checklist of what is required.
- Given I upload documentation, when submission completes, then I receive confirmation of what was received against the checklist.
- Given an item is missing, when I complete submission, then I am told which item is outstanding before the application proceeds to validation.

---

## Story map against the as-is process

| As-is stage | Current behaviour | Stories |
|---|---|---|
| Complete application | 73.4% enter incompleteness loop, +5.6 days | US-07 |
| Create and send offer | No measure of what happens next | US-01, US-02 |
| Call after offers | 65.5% of all queue time; served in arrival order | US-03, US-04, US-05 |
| Application cancelled | 33.1%; reason not recorded | US-06 |

---

## Out of scope for this release

Credit decisioning changes · pricing or offer terms · replacement of the case
management system · changes to handler headcount or reporting lines.
