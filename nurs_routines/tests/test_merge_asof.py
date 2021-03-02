import pytest
import pandas as pd

from nurs_routines.utilities.merge_asof import MergeAsOf


@pytest.fixture
def merge_object():
    return MergeAsOf(
        "nurs_routines/tests/test_data/merge_data.csv",
        "nurs_routines/tests/test_data/merge_reference.csv",
        "user", "user")


@pytest.fixture
def merged_data(merge_object):
    return merge_object.main("date", "date")


@pytest.fixture
def merged_object_extra_bodies():
    return MergeAsOf(
        "nurs_routines/tests/test_data/merge_data_extra_bodies.csv",
        "nurs_routines/tests/test_data/merge_reference.csv",
        "user", "user")


@pytest.fixture
def merged_data_extra_bodies(merged_object_extra_bodies):
    return merged_object_extra_bodies.main("date", "date")


def test_merge_n_cases(merged_data):
    raw_data = pd.read_csv("nurs_routines/tests/test_data/merge_data.csv")
    assert merged_data.shape[0] == raw_data.shape[0]


def test_merge_k_features(merged_data):
    raw_data = pd.read_csv("nurs_routines/tests/test_data/merge_data.csv")
    assert merged_data.shape[1] != raw_data.shape[1]


def test_merge_columns_kept(merged_data):
    raw_data = pd.read_csv("nurs_routines/tests/test_data/merge_data.csv")
    assert all(i in merged_data.columns for i in raw_data.columns)


def test_merge_last_values(merged_data):
    date_window = merged_data["date"] == "2020-01-01"
    assert (merged_data[date_window]["value"] == 4).all()


def test_merge_values_vary(merged_data):
    date_window = merged_data["date"] == "2020-01-01"
    assert not (merged_data[date_window]["value2"] == 4).all()


def test_merge_early_values(merged_data):
    date_window = merged_data["date"] == "2017-01-01"
    assert (merged_data[date_window]["value"] == 3).all()


def test_merge_predating_values(merged_data):
    date_window = merged_data["date"] == "2000-01-01"
    assert (merged_data[date_window]["value"].isna()).all()


def test_merge_copes_with_missing_keys(merged_data_extra_bodies):
    user_window = merged_data_extra_bodies["user"].apply(lambda x: x not in "ABCD")
    assert user_window.shape[0] > 0
    assert merged_data_extra_bodies[user_window]["value"].isna().all()


def test_overlap(merge_object):
    assert len(merge_object.overlap["In Both"]) == 4


def test_overlap_report(merged_object_extra_bodies):
    merged_object_extra_bodies.overlap_report_to_file("temp.txt")
