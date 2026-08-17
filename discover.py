"""
ConsultLab — As-is process discovery and diagnostic
BPI Challenge 2017 loan application event log.

Run:  python discover.py

Reads   : data/BPI_Challenge_2017.xes.gz
Writes  : outputs/*.csv  and prints a summary of every figure the
          README needs.
"""

import os
import pandas as pd
import pm4py

LOG_PATH = os.path.join("data", "BPI_Challenge_2017.xes.gz")
CACHE = os.path.join("data", "events.pkl")
OUT = "outputs"

CASE, ACT, TIME, RES = (
    "case:concept:name",
    "concept:name",
    "time:timestamp",
    "org:resource",
)


def load():
    """Read the XES once, then cache as parquet — the XES takes minutes."""
    if os.path.exists(CACHE):
        print(f"Loading cached event table from {CACHE} ...")
        return pd.read_pickle(CACHE)

    print(f"Reading {LOG_PATH} (this takes a few minutes the first time) ...")
    df = pm4py.read_xes(LOG_PATH)
    df = pd.DataFrame(df)
    df[TIME] = pd.to_datetime(df[TIME], utc=True)
    df = df.sort_values([CASE, TIME]).reset_index(drop=True)
    df.to_pickle(CACHE)
    print(f"Cached to {CACHE}")
    return df


def scale(df):
    """Q: how big is the process, and who runs it?"""
    lifecycles = (
        df["lifecycle:transition"].value_counts().to_dict()
        if "lifecycle:transition" in df.columns
        else {}
    )
    return {
        "cases": df[CASE].nunique(),
        "events": len(df),
        "activities": df[ACT].nunique(),
        "resources": df[RES].nunique() if RES in df.columns else None,
        "first_event": df[TIME].min(),
        "last_event": df[TIME].max(),
        "lifecycle_transitions": lifecycles,
    }


def cycle_times(df):
    """Q: how long does an application take end to end?"""
    g = df.groupby(CASE)[TIME]
    dur = ((g.max() - g.min()).dt.total_seconds() / 86400).rename("days")
    return dur, {
        "median_days": round(dur.median(), 1),
        "mean_days": round(dur.mean(), 1),
        "p90_days": round(dur.quantile(0.90), 1),
        "p95_days": round(dur.quantile(0.95), 1),
        "max_days": round(dur.max(), 1),
    }


def variants(df):
    """Q: how many distinct paths does the process actually take?"""
    seq = df.groupby(CASE)[ACT].apply(lambda s: " -> ".join(s))
    counts = seq.value_counts()
    top = counts.head(20).rename_axis("variant").reset_index(name="cases")
    top["pct_of_cases"] = (top["cases"] / len(seq) * 100).round(2)
    return top, {
        "distinct_variants": len(counts),
        "top1_pct": round(counts.iloc[0] / len(seq) * 100, 1),
        "variants_covering_80pct": int(
            (counts.cumsum() / len(seq) < 0.80).sum() + 1
        ),
    }


def rework(df, dur, marker="A_Incomplete"):
    """Q: how much work is re-done, and what does it cost in days?"""
    # Cases that hit the incompleteness marker at least once.
    flagged = set(df.loc[df[ACT] == marker, CASE].unique())
    all_cases = set(df[CASE].unique())

    with_rw = dur[dur.index.isin(flagged)]
    without_rw = dur[~dur.index.isin(flagged)]

    # Repeated activities within a case = generic rework signal.
    per_case_act = df.groupby([CASE, ACT]).size()
    repeats = per_case_act[per_case_act > 1]
    repeated_events = int((repeats - 1).sum())

    top_repeated = (
        (repeats - 1)
        .groupby(level=1)
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .rename("extra_executions")
        .reset_index()
        .rename(columns={ACT: "activity"})
    )

    delta = (
        round(with_rw.median() - without_rw.median(), 1)
        if len(with_rw) and len(without_rw)
        else None
    )

    return top_repeated, {
        "marker": marker,
        "cases_with_rework": len(with_rw),
        "pct_cases_with_rework": round(len(with_rw) / len(all_cases) * 100, 1),
        "median_days_with_rework": round(with_rw.median(), 1) if len(with_rw) else None,
        "median_days_without_rework": (
            round(without_rw.median(), 1) if len(without_rw) else None
        ),
        "extra_days_per_reworked_case": delta,
        "total_delay_days": (
            round(delta * len(with_rw)) if delta is not None else None
        ),
        "repeated_events_total": repeated_events,
        "pct_events_that_are_repeats": round(repeated_events / len(df) * 100, 1),
    }


def bottlenecks(df):
    """Q: where does the waiting time actually accumulate?

    Waiting is attributed to the activity the case was waiting FOR:
    the gap between the previous event and this one.
    """
    d = df[[CASE, ACT, TIME]].copy()
    d["prev_time"] = d.groupby(CASE)[TIME].shift(1)
    d["wait_h"] = (d[TIME] - d["prev_time"]).dt.total_seconds() / 3600
    d = d.dropna(subset=["wait_h"])
    d = d[d["wait_h"] >= 0]

    agg = (
        d.groupby(ACT)["wait_h"]
        .agg(total_wait_h="sum", median_wait_h="median", occurrences="count")
        .sort_values("total_wait_h", ascending=False)
        .reset_index()
        .rename(columns={ACT: "activity"})
    )
    total = agg["total_wait_h"].sum()
    agg["pct_of_total_wait"] = (agg["total_wait_h"] / total * 100).round(1)
    agg["total_wait_days"] = (agg["total_wait_h"] / 24).round(0)
    agg["median_wait_h"] = agg["median_wait_h"].round(2)
    return agg


def outcomes(df):
    """Q: how do applications end?"""
    finals = ["A_Pending", "A_Denied", "A_Cancelled"]
    rows = []
    n = df[CASE].nunique()
    for f in finals:
        c = df.loc[df[ACT] == f, CASE].nunique()
        rows.append({"outcome": f, "cases": c, "pct": round(c / n * 100, 1)})
    return pd.DataFrame(rows)


def show(title, d):
    print(f"\n{title}")
    print("-" * len(title))
    for k, v in d.items():
        print(f"  {k:32} {v}")


def main():
    os.makedirs(OUT, exist_ok=True)
    df = load()

    show("SCALE", scale(df))

    dur, ct = cycle_times(df)
    show("CYCLE TIME (days, end to end)", ct)

    var_top, var_stats = variants(df)
    show("PROCESS VARIANTS", var_stats)
    var_top.to_csv(f"{OUT}/variants_top20.csv", index=False)

    rw_top, rw_stats = rework(df, dur)
    show("REWORK", rw_stats)
    rw_top.to_csv(f"{OUT}/repeated_activities.csv", index=False)
    print("\n  Most repeated activities:")
    print(rw_top.head(8).to_string(index=False))

    bn = bottlenecks(df)
    bn.to_csv(f"{OUT}/waiting_time_by_activity.csv", index=False)
    print("\nBOTTLENECKS (by total waiting time)")
    print("-" * 34)
    print(
        bn.head(10)[
            ["activity", "total_wait_days", "pct_of_total_wait", "median_wait_h"]
        ].to_string(index=False)
    )

    oc = outcomes(df)
    oc.to_csv(f"{OUT}/outcomes.csv", index=False)
    print("\nOUTCOMES")
    print("-" * 8)
    print(oc.to_string(index=False))

    dur.reset_index().to_csv(f"{OUT}/case_durations.csv", index=False)
    print(f"\nCSV outputs written to {OUT}/")


if __name__ == "__main__":
    main()
