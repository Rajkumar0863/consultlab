# Solution Options Assessment

**Engagement:** ConsultLab — Post-Offer Conversion Improvement
**Related:** [BRD](../03-requirements/BRD.md) · [Traceability matrix](../03-requirements/traceability-matrix.md) · [As-is findings](../02-as-is/findings.md)

---

## 1. What is being decided

The as-is analysis established that 33.1% of applications are cancelled after an
offer has been issued, and that the activity intended to re-engage those
applicants holds 65.5% of all queue time in the process. The requirements
specify what the business needs; this document assesses how that need could be
met and recommends one route.

Three options are assessed. All three are real alternatives, not a preferred
option flanked by two straw men — each is genuinely the right answer under
different assumptions, and those assumptions are stated.

---

## 2. Options

### Option A — Reprioritise the existing follow-up queue

Order the post-offer follow-up work by risk of the offer lapsing rather than by
arrival, and raise a follow-up action when a live offer passes an age threshold.
No new applicant-facing channel; the same handlers do the same work in a
different order.

*Satisfies:* BR-01, BR-02, BR-03, BR-04
*Does not satisfy:* BR-05 (no non-handler channel), BR-07

**Assumption it rests on:** that a meaningful share of lost offers were
recoverable and were simply never reached in time. If the queue is genuinely
oversubscribed rather than mis-ordered, reordering moves the loss around rather
than reducing it.

---

### Option B — Reprioritise, plus automated applicant reminders

Everything in Option A, plus an automated reminder to applicants with a live
unresponded offer, stating the outstanding action, subject to contact-frequency
limits. Adds a channel that consumes no handler capacity.

*Satisfies:* BR-01 through BR-06, BR-08, BR-09
*Partially satisfies:* BR-07 (reminder can state what is outstanding, but the
submission-stage checklist is a separate change)

**Assumption it rests on:** that a share of non-responding applicants are
inattentive rather than decided — that a prompt changes behaviour. Where an
applicant has chosen not to proceed, a reminder achieves nothing.

---

### Option C — Replace the case management system

Procure or build a replacement offering offer-stage workflow, automated
customer communication, configurable SLAs and native reporting.

*Satisfies:* all requirements, in principle
*Conflicts with:* NFR-05, which requires operating against the existing system,
and with the project brief's scope boundary

**Assumption it rests on:** that the constraint is systemic rather than local —
that the existing platform cannot support the required behaviour at acceptable
cost. Nothing in the evidence establishes this.

---

## 3. Assessment criteria

Weights reflect what the sponsor is accountable for. Benefit dominates because
the problem is revenue loss, not efficiency; disruption and effort carry real
weight because handler capacity is fixed and the engagement excludes
restructuring.

| Criterion | Weight | What a high score means |
|---|---|---|
| Benefit realisation | 30% | Addresses the identified loss directly and at scale |
| Speed to value | 20% | Delivers measurable change within months, not years |
| Implementation effort | 20% | Low build, integration and procurement cost |
| Operational disruption | 15% | Little change to how 149 handlers work day to day |
| Requirements coverage | 10% | Satisfies the specified requirements |
| Risk | 5% | Low delivery and compliance risk |

*Scores are 1–5, assessed against the criteria above. They are judgements
informed by the evidence, not measurements — the underlying reasoning is stated
in section 5 so the scoring can be challenged.*

---

## 4. Weighted scoring

| Criterion | Weight | A: Reprioritise | B: Reprioritise + reminders | C: Replace system |
|---|---|---|---|---|
| Benefit realisation | 30% | 3 | 4 | 5 |
| Speed to value | 20% | 5 | 4 | 1 |
| Implementation effort | 20% | 5 | 4 | 1 |
| Operational disruption | 15% | 4 | 4 | 1 |
| Requirements coverage | 10% | 3 | 5 | 5 |
| Risk | 5% | 5 | 4 | 2 |
| **Weighted total** | **100%** | **4.05** | **4.10** | **2.55** |

---

## 5. Reasoning behind the scores

**Benefit.** Option C scores highest in principle — it could address every
requirement including those deferred here. Option B scores above A because
Option A can only redistribute a fixed amount of handler attention across
40,321 queue-days, while B adds capacity that does not compete for handler time.
Option A is not scored low: reordering alone may capture a substantial share of
the recoverable value, and it does so at almost no cost.

**Speed and effort.** A and B operate against the existing system and could be
delivered within a quarter. C is a multi-year procurement with a business case
of its own, and would deliver nothing during the period in which the current
loss continues.

**Disruption.** A and B change what a handler sees, not what a handler does. C
changes the working method of 149 people simultaneously.

**Risk.** B carries a compliance dimension A does not — automated applicant
contact must respect frequency limits set by Risk & Compliance (BR-08), which is
why FR-09 exists. C carries delivery risk proportional to its size.

**The close result between A and B is real and should not be smoothed over.**
4.05 against 4.10 is not a decisive margin, and it is sensitive to the weighting.
If implementation effort were weighted above benefit — a reasonable position for
a capacity-constrained operation — Option A would win. The recommendation
therefore rests on sequencing rather than on the margin.

---

## 6. Recommendation

**Adopt Option B, delivered in two stages: Option A first, then reminders.**

The two options are not really competitors — A is contained within B. Delivering
A first is what makes B defensible:

1. **Stage one (Option A)** establishes offer-stage measurement and reprioritises
   the queue. This is low cost, low risk, and — critically — it creates the
   baseline that does not currently exist (BR-04). Without it, no subsequent
   change can be shown to have worked.

2. **Stage two (reminders)** adds the automated channel once stage one has shown
   whether timing affects conversion. If reprioritisation alone moves the
   cancellation rate, the causal assumption underlying this engagement is
   supported and the investment in stage two is justified. If it does not, the
   business has learned something important at minimal cost, and stage two
   should be reconsidered rather than proceeded with.

**What this recommendation gives up.** It is slower to full benefit than
implementing B in one pass, and it defers the documentation-clarity requirement
(BR-07) entirely. It also accepts that the existing case management system
constrains what is possible — Option C's ceiling is genuinely higher, and if the
business intends to replace the platform for other reasons, this recommendation
should be revisited as a bridge rather than a destination.

**Option C is not recommended now, but is not dismissed.** It is the right answer
if the platform is being replaced anyway, or if stage one demonstrates that the
constraint is systemic. The engagement recommends against initiating it *on the
strength of this finding alone*.

---

## 7. Decision dependencies

| # | Dependency | Owner | Needed before |
|---|---|---|---|
| 1 | Contact-frequency and channel limits | Risk & Compliance (S7) | Stage two design |
| 2 | Elapsed-time threshold for intervention | Operations (S2) | Stage one build |
| 3 | Recovery-rate assumption for the business case | Finance (S9) | Investment approval |
| 4 | Confirmation that offer and response timestamps are complete | IT (S5) | Stage one build |

---

## 8. Sensitivity

The recommendation changes under these conditions:

- **If the follow-up queue is oversubscribed rather than mis-ordered** —
  reprioritisation yields little, and stage two becomes the primary intervention
  rather than the follow-on.
- **If non-responding applicants have largely decided against proceeding** —
  both A and B underperform, and the engagement's central assumption fails. This
  is the single largest risk to the recommendation and is why stage one is
  structured as a test.
- **If platform replacement is already funded for other reasons** — Option C
  absorbs this work and the staged approach becomes redundant.
