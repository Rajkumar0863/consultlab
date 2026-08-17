"""
ConsultLab — As-is diagnostic, v2 (lifecycle-aware)
BPI Challenge 2017 loan application event log.

Fixes two measurement errors in v1:

  1. LIFECYCLE TRANSITIONS. BPI 2017 records up to seven transitions per
     activity instance (schedule, start, suspend, resume, ate_abort,
     withdraw, complete). v1 counted each as a separate execution, which
     inflated "rework" to 59% of events. v2 counts one execution per
     'complete' transition, and uses the other transitions only to
     separate WAITING time from PROCESSING time.

  2. OUTCOME CONFOUNDING. v1 compared cases with and without rework
     across all outcomes. Cancelled applications sit idle for weeks
     before closure, so they dominated the "no rework" group and made
     rework look beneficial. v2 compares like with like, within outcome.

Run:  python discover2.py   (reads the cache written by discover.py)
"""

import os
import pandas as pd

CACHE = os.path.join("data", "events.pkl")
OUT = "outputs"

CASE, ACT, TIME, RES, LIFE = (
    "case:concept:name",
    "concept:name",
    "time:timestamp",
    "org:resource",
    "lifecycle:transition",
)

AMOUNT = "case:RequestedAmount"


def load():
    df = pd.read_pickle(CACHE)
    df[TIME] = pd.to_datetime(df[TIME], utc=True)
    return df.sort_values([CASE, TIME]).reset_index(drop=True)


def completed(df):
    """One row per completed activity instance."""
    if LIFE in df.columns:
        return df[df[LIFE] == "complete"].copy()
    return df.copy()


def classify_outcomes(df):
    """Each application ends pending (offer accepted), denied, or cancelled."""
    n = df[CASE].nunique()
    out = pd.Series("in_progress", index=pd.Index(df[CASE].unique(), name=CASE))
    for act, label in [
        ("A_Denied", "denied"),
        ("A_Cancelled", "cancelled"),
        ("A_Pending", "pending"),
    ]:
        cases = df.loc[df[ACT] == act, CASE].unique()
        out.loc[out.index.isin(cases)] = label
    summary = (
        out.value_counts()
        .rename_axis("outcome")
        .reset_index(name="cases")
        .assign(pct=lambda d: (d["cases"] / n * 100).round(1))
    )
    return out, summary


def durations(df):
    g = df.groupby(CASE)[TIME]
    return ((g.max() - g.min()).dt.total_seconds() / 86400).rename("days")


def cycle_by_outcome(dur, outcome):
    d = pd.DataFrame({"days": dur, "outcome": outcome.reindex(dur.index)})
    return (
        d.groupby("outcome")["days"]
        .agg(cases="count", median="median", p90=lambda s: s.quantile(0.90))
        .round(1)
        .reset_index()
    )


def rework_within_outcome(comp, dur, outcome, marker="A_Incomplete"):
    """The v1 comparison, done correctly: like-for-like, within outcome."""
    flagged = set(comp.loc[comp[ACT] == marker, CASE].unique())
    rows = []
    for label in ["pending", "denied", "cancelled"]:
        cases = outcome[outcome == label].index
        d = dur[dur.index.isin(cases)]
        w = d[d.index.isin(flagged)]
        wo = d[~d.index.isin(flagged)]
        if not len(w) or not len(wo):
            continue
        delta = w.median() - wo.median()
        rows.append(
            {
                "outcome": label,
                "cases": len(d),
                "pct_with_rework": round(len(w) / len(d) * 100, 1),
                "median_days_with": round(w.median(), 1),
                "median_days_without": round(wo.median(), 1),
                "extra_days": round(delta, 1),
                "total_extra_days": round(delta * len(w)),
            }
        )
    return pd.DataFrame(rows)


def true_rework(comp):
    """Repeat executions, counted once per completed instance."""
    per = comp.groupby([CASE, ACT]).size()
    extra = (per - 1)
    extra = extra[extra > 0]
    top = (
        extra.groupby(level=1)
        .agg(extra_executions="sum", cases_affected="count")
        .sort_values("extra_executions", ascending=False)
        .head(12)
        .reset_index()
        .rename(columns={ACT: "activity"})
    )
    return top, {
        "completed_instances": len(comp),
        "extra_executions": int(extra.sum()),
        "pct_instances_that_are_repeats": round(extra.sum() / len(comp) * 100, 1),
        "cases_with_any_repeat": int(
            extra.reset_index()[CASE].nunique()
        ),
    }


def waiting_vs_processing(df):
    """Split queue time from hands-on time using lifecycle transitions.

    Within a (case, activity), the gap that follows a 'schedule' event is
    queue time; the gap that follows a 'start' event is processing time.
    """
    if LIFE not in df.columns:
        return pd.DataFrame()
    d = df[[CASE, ACT, TIME, LIFE]].copy()
    d = d.sort_values([CASE, ACT, TIME])
    d["next_time"] = d.groupby([CASE, ACT])[TIME].shift(-1)
    d["gap_h"] = (d["next_time"] - d[TIME]).dt.total_seconds() / 3600
    d = d.dropna(subset=["gap_h"])
    d = d[d["gap_h"] >= 0]

    wait = (
        d[d[LIFE] == "schedule"]
        .groupby(ACT)["gap_h"]
        .agg(queue_total_h="sum", queue_median_h="median", queued="count")
    )
    work = (
        d[d[LIFE] == "start"]
        .groupby(ACT)["gap_h"]
        .agg(work_total_h="sum", work_median_h="median", started="count")
    )
    out = wait.join(work, how="outer").fillna(0)
    out["queue_total_days"] = (out["queue_total_h"] / 24).round(0)
    out["work_total_days"] = (out["work_total_h"] / 24).round(0)
    out["queue_median_h"] = out["queue_median_h"].round(2)
    out["work_median_h"] = out["work_median_h"].round(2)
    tot = out["queue_total_h"].sum()
    out["pct_of_queue"] = (out["queue_total_h"] / tot * 100).round(1) if tot else 0
    return (
        out.sort_values("queue_total_h", ascending=False)
        .reset_index()
        .rename(columns={ACT: "activity"})
    )


def cancellation_analysis(comp, dur, outcome):
    """The commercial question: what is being abandoned, and how late?"""
    cancelled = outcome[outcome == "cancelled"].index
    c = comp[comp[CASE].isin(cancelled)].copy()
    if c.empty:
        return {}, pd.DataFrame()

    # Idle time: last substantive activity -> the cancellation event.
    cancel_ts = c[c[ACT] == "A_Cancelled"].groupby(CASE)[TIME].min()
    prior = c[c[ACT] != "A_Cancelled"].groupby(CASE)[TIME].max()
    idle = ((cancel_ts - prior).dt.total_seconds() / 86400).dropna()
    idle = idle[idle >= 0]

    # Last thing that happened before the case went quiet.
    last_act = (
        c[c[ACT] != "A_Cancelled"]
        .sort_values(TIME)
        .groupby(CASE)[ACT]
        .last()
        .value_counts()
        .head(10)
        .rename_axis("last_activity_before_cancel")
        .reset_index(name="cases")
    )
    last_act["pct"] = (last_act["cases"] / len(cancelled) * 100).round(1)

    # How far down the funnel did they get?
    def reached(act):
        return c.loc[c[ACT] == act, CASE].nunique()

    stats = {
        "cancelled_cases": len(cancelled),
        "median_days_to_cancellation": round(dur[dur.index.isin(cancelled)].median(), 1),
        "median_idle_days_before_cancel": round(idle.median(), 1),
        "p90_idle_days_before_cancel": round(idle.quantile(0.90), 1),
        "total_idle_days": round(idle.sum()),
        "reached_offer_created": reached("O_Created"),
        "reached_offer_sent": reached("O_Sent (mail and online)")
        + reached("O_Sent (online only)"),
        "returned_documents": reached("O_Returned"),
        "hit_incomplete_loop": reached("A_Incomplete"),
    }

    if AMOUNT in comp.columns:
        amounts = (
            comp[comp[CASE].isin(cancelled)]
            .groupby(CASE)[AMOUNT]
            .first()
            .astype(float)
        )
        stats["cancelled_requested_value_total"] = round(amounts.sum())
        stats["cancelled_requested_value_median"] = round(amounts.median())

    return stats, last_act


def show(title, d):
    print(f"\n{title}")
    print("-" * len(title))
    for k, v in d.items():
        print(f"  {k:36} {v}")


def main():
    os.makedirs(OUT, exist_ok=True)
    df = load()
    comp = completed(df)

    show(
        "SCALE (lifecycle-corrected)",
        {
            "raw events": len(df),
            "completed activity instances": len(comp),
            "cases": df[CASE].nunique(),
            "activities": comp[ACT].nunique(),
            "resources": df[RES].nunique() if RES in df.columns else "n/a",
        },
    )

    outcome, osum = classify_outcomes(comp)
    print("\nOUTCOMES")
    print("-" * 8)
    print(osum.to_string(index=False))
    osum.to_csv(f"{OUT}/outcomes.csv", index=False)

    dur = durations(df)
    cbo = cycle_by_outcome(dur, outcome)
    print("\nCYCLE TIME BY OUTCOME (days)")
    print("-" * 28)
    print(cbo.to_string(index=False))
    cbo.to_csv(f"{OUT}/cycle_time_by_outcome.csv", index=False)

    rw = rework_within_outcome(comp, dur, outcome)
    print("\nREWORK, CONTROLLED FOR OUTCOME")
    print("-" * 30)
    print(rw.to_string(index=False))
    rw.to_csv(f"{OUT}/rework_by_outcome.csv", index=False)

    top, rstats = true_rework(comp)
    show("REPEAT EXECUTIONS (corrected)", rstats)
    print("\n  Most repeated activities:")
    print(top.to_string(index=False))
    top.to_csv(f"{OUT}/repeated_activities.csv", index=False)

    wp = waiting_vs_processing(df)
    if not wp.empty:
        print("\nQUEUE vs PROCESSING TIME (top by queue)")
        print("-" * 39)
        print(
            wp.head(10)[
                [
                    "activity",
                    "queue_total_days",
                    "pct_of_queue",
                    "queue_median_h",
                    "work_total_days",
                    "work_median_h",
                ]
            ].to_string(index=False)
        )
        wp.to_csv(f"{OUT}/queue_vs_processing.csv", index=False)

    cstats, last_act = cancellation_analysis(comp, dur, outcome)
    if cstats:
        show("CANCELLATION ANALYSIS", cstats)
        print("\n  Last activity before cancellation:")
        print(last_act.to_string(index=False))
        last_act.to_csv(f"{OUT}/cancellation_last_activity.csv", index=False)

    print(f"\nCSV outputs written to {OUT}/")


if __name__ == "__main__":
    main()
