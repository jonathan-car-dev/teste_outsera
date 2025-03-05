import logging
import pandas as pd
from app.utils import get_database_instance
from app.models import IntervalPrizes, Interval


def retrieve_producer_interval_reward() -> IntervalPrizes:
    movies = get_database_instance().retrieve_all_winners()

    if len(movies) == 0:
        return IntervalPrizes(min=[], max=[])

    df = pd.DataFrame([vars(movie) for movie in movies])

    df = df.sort_values(['producer', 'year'])

    df["previousWin"] = df.groupby("producer")["year"].shift(1)

    df["interval"] = df["year"] - df["previousWin"]

    df = df.dropna()

    min_interval_value = df["interval"].min()

    max_interval_value = df["interval"].max()

    min_intervals = [Interval(**row) for row in df[df["interval"] == min_interval_value][["producer", "interval", "previousWin", "year"]].rename(
        columns={"producer": "producer", "year": "followingWin"})
                    .to_dict(orient="records")]

    max_intervals = [Interval(**row) for row in df[df["interval"] == max_interval_value][["producer", "interval", "previousWin", "year"]].rename(
        columns={"producer": "producer", "year": "followingWin"})
                     .to_dict(orient="records")]

    return IntervalPrizes(max=max_intervals, min=min_intervals)
