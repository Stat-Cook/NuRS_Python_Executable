import pytest
from datetime import datetime
import pandas as pd
from nurs_routines.utilities.month_tools import GetMonth


@pytest.fixture
def get_month():
    return GetMonth(start=datetime(2018, 1, 1), end=datetime(2019, 12, 31))


@pytest.fixture
def shuffling_data():
    return pd.DataFrame({
        "Absence Start Date": 10*["2018-05"],
        "Absence End Date": 10*["2018-07"],
        "Group": 5*["A"] + 5*["B"],
        "Value": range(10),
        "Value2": range(10)
    })


def test_month_length(get_month):
    assert len(get_month.months) == 24


def test_monthly_shuffle(get_month, shuffling_data):
    shuffled = pd.concat(get_month.monthly_shuffle(shuffling_data, ["Value"]))
    assert shuffled.shape[0] == 30


def test_monthly_group_shuffle(get_month, shuffling_data):
    shuffle_by_group = get_month.grouped_monthly_shuffle(shuffling_data, "Group", ["Value"])
    assert shuffle_by_group.shape[0] == 30


def test_monthly_group_shuffle_mean(get_month, shuffling_data):
    shuffle_by_group = get_month.grouped_monthly_shuffle(shuffling_data, "Group",
                                                         ["Value", "Value2"])
    grps = shuffle_by_group.groupby("Group")
    means = [df["Value"].mean() for _, df in grps]
    assert (means[0] == 2.0) and (means[1] == 7.0)


def test_monthly_group_shuffle_vars(get_month, shuffling_data):
    shuffle_by_group = get_month.grouped_monthly_shuffle(
        shuffling_data, "Group", ["Value", "Value2"]
    )

    print(shuffle_by_group[["Value", "Value2"]])
    correlations = shuffle_by_group[["Value", "Value2"]].applymap(float).corr()
    assert ((correlations != 1).any().any())
