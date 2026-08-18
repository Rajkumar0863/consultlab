# Business Case — Post-Offer Conversion Improvement

**Engagement:** ConsultLab
**Related:** [Options assessment](options-assessment.md) · [BRD](../03-requirements/BRD.md) · [As-is findings](../02-as-is/findings.md)

---

## 1. Summary

The recommended programme breaks even if **233 of the 9,629 applications lost
each year after an offer** are recovered — a recovery rate of **2.4%**.

On base-case assumptions (5% recovery, 2.0% net interest margin) the programme
returns **2.1× its three-year cost**. On pessimistic assumptions it **does not
pay back**. That downside is the reason the recommendation is staged rather than
committed in full: stage one costs €125,000 over three years and establishes
which case is true before stage two is funded.

---

## 2. What is *not* claimed

The 10,431 cancelled applications carry a combined requested principal of
**€166,018,320**. That figure appears nowhere in this business case as a
benefit, and should not be quoted as one.

It is the amount applicants asked to borrow. It is not revenue. The lender's
return on a loan is net interest margin earned on the outstanding balance over
the loan term — a small fraction of principal — and a share of these
applications would have been declined on credit grounds regardless. Treating
principal as opportunity would overstate the benefit by roughly two orders of
magnitude.

---

## 3. Baseline

Derived from the event log, annualised from the 13-month observation period.

| Measure | Observed (13 months) | Annualised |
|---|---|---|
| Applications cancelled after offer | 10,431 | 9,629 |
| Requested principal, cancelled applications | €166,018,320 | €153,247,680 |
| Median requested amount | €11,000 | €11,000 |
| Applications returning documents | 959 (9.2%) | — |

---

## 4. Assumptions

Every figure below is an assumption, not a measurement. None is derivable from
the event log. Each is stated so it can be challenged, and each is tested in the
sensitivity analysis.

| # | Assumption | Low | Base | High | Basis |
|---|---|---|---|---|---|
| A1 | Recovery rate — share of lapsed applications converted to funded lending by timely intervention | 2% | **5%** | 10% | Only 9.2% of cancelled applicants ever engaged after the offer; most went silent. A nudge recovers a modest minority, not a majority |
| A2 | Net interest margin on recovered lending | 1.5% | **2.0%** | 2.5% | Typical eurozone retail unsecured lending margin |
| A3 | Average outstanding balance over term | 55% of principal | 55% | 55% | Amortising loan; balance declines steadily from drawdown |
| A4 | Average loan term | 3 years | 3 years | 3 years | Consistent with a median €11,000 personal loan |
| A5 | Stage 1 build cost | — | €80,000 | — | Scoring, prioritised queue and reporting against the existing system |
| A6 | Stage 1 annual run cost | — | €15,000 | — | Support and maintenance |
| A7 | Stage 2 build cost | — | €60,000 | — | Automated reminder channel with contact-limit enforcement |
| A8 | Stage 2 annual run cost | — | €20,000 | — | Messaging costs and support |

**A1 is the load-bearing assumption.** The entire case rests on it, it cannot be
established from the data available, and stage one exists to measure it.

---

## 5. Benefit calculation

Recovered principal → average outstanding balance → margin over term.

**Base case, one annual cohort:**

| Step | Calculation | Value |
|---|---|---|
| Lapsed principal (annualised) | — | €153,247,680 |
| Recovered principal | × 5% (A1) | €7,662,384 |
| Applications recovered | 9,629 × 5% | 481 |
| Average outstanding balance | × 55% (A3) | €4,214,311 |
| Annual net interest margin | × 2.0% (A2) | €84,286 |
| Lifetime margin over 3-year term | × 3 (A4) | €252,859 |

Because a new cohort is recovered each year, annual margin accumulates: year 1
earns one cohort, year 2 two, year 3 three.

---

## 6. Three-year case — full programme

| | Low | Base | High |
|---|---|---|---|
| Recovery rate / NIM | 2% / 1.5% | **5% / 2.0%** | 10% / 2.5% |
| Applications recovered per year | 193 | 481 | 963 |
| Gross margin over 3 years | €151,715 | **€505,717** | €1,264,293 |
| Cost over 3 years | €245,000 | €245,000 | €245,000 |
| **Net** | **−€93,285** | **€260,717** | **€1,019,293** |
| **Return on cost** | **0.6×** | **2.1×** | **5.2×** |

*Cost: €140,000 build (stages 1 and 2) plus €35,000 annual run.*

**The low case is negative.** This is the central financial risk and is not
smoothed over: if the recovery rate is 2% rather than 5%, committing to the full
programme upfront destroys value.

---

## 7. Three-year case — stage 1 only

Stage one is assumed to capture 60% of total benefit — reprioritisation moves
existing handler attention to where it matters, but adds no capacity.

| | Low | Base | High |
|---|---|---|---|
| Gross margin over 3 years | €91,029 | **€303,430** | €758,576 |
| Cost over 3 years | €125,000 | €125,000 | €125,000 |
| **Net** | **−€33,971** | **€178,430** | **€633,576** |
| **Return on cost** | **0.7×** | **2.4×** | **6.1×** |

Stage one returns *more per euro spent* than the full programme in every
scenario, and exposes €125,000 rather than €245,000 to the possibility that A1
is wrong.

---

## 8. Break-even

| Scenario | Break-even recovery rate | Applications per year |
|---|---|---|
| Full programme | 2.42% | 233 of 9,629 |
| Stage 1 only | 2.06% | 198 of 9,629 |

**233 applications a year is the number that matters.** Framed against 9,629
lost annually — all of which received a formal offer and 91% of which never
responded at all — recovering fewer than one in forty is the threshold at which
this programme pays for itself.

---

## 9. Non-financial benefits

Not quantified, but material to the decision:

- **Measurement where none exists.** Offer-stage performance is currently
  invisible; stage one creates the baseline (BR-04) that makes any future change
  assessable.
- **A tested causal assumption.** Stage one establishes whether follow-up timing
  affects conversion — a question the event log cannot answer.
- **Reason codes on cancellation** (BR-06) enable root-cause analysis that is
  impossible today.
- **Reduced rework.** The documentation checklist (BR-07) targets a loop
  affecting 73.4% of successful applications at 5.6 days each. Cycle-time
  benefit is real but accrues to applications that already convert, so it is
  excluded from the financial case.

---

## 10. Risks to the case

| Risk | Effect | Mitigation |
|---|---|---|
| Recovery rate below 2.4% | Programme does not pay back | Staged funding; stage one measures the rate before stage two is committed |
| Non-responders have decided against proceeding rather than being inattentive | Both stages underperform | Reason codes (BR-06) distinguish the two; stage one result is the test |
| Follow-up queue is oversubscribed rather than mis-ordered | Stage one yields little | Stage two becomes primary rather than follow-on; assessed at the stage gate |
| Contact limits restrict reminder frequency | Stage two benefit reduced | Limits confirmed with Risk & Compliance before stage two design |
| Margin assumption too high | Benefit overstated proportionally | Sensitivity range applied; A2 is a market figure, not a client figure |

---

## 11. Recommendation

**Fund stage one (€80,000 build, €15,000 annual run). Defer the stage two
decision to a gate review after twelve months of stage one operation.**

At the gate, the question is no longer "what might the recovery rate be" but
"what was it." If it exceeds roughly 2.4%, stage two is justified on the same
arithmetic. If it does not, the business will have spent €95,000 to learn that a
€245,000 programme would not have paid back — which is itself a good outcome.

---

## 12. Limitations

- All financial figures rest on assumptions A1–A8; none is drawn from client
  financial data, which was not available to this engagement.
- Cost estimates are indicative and would require IT (S5) validation before
  investment approval.
- The 60% benefit attribution for stage one is a judgement, not a measurement.
- Annualisation assumes the 13-month observation period is representative;
  seasonality is not assessed.
