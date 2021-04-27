import pandas as pd
from nurs_routines.utilities.merge_asof import MergeAsOf

from nurs_routines.tests.fixtures.merge_asof_fixtures import test_data, \
    test_data_extra_bodies, test_reference, merged_data, merge_object, \
    merged_data_extra_bodies, merged_object_extra_bodies


def test_merge_n_cases(test_data, merged_data):
    assert merged_data.shape[0] == test_data.shape[0]


def test_merge_k_features(test_data, merged_data):
    assert merged_data.shape[1] != test_data.shape[1]


def test_merge_columns_kept(test_data, merged_data):
    assert all(i in merged_data.columns for i in test_data.columns)


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
    with open("temp.txt", "r") as file:
        string = file.read()
    split_string = string.split("\n")
    assert len(split_string) == 11


def test_merge_mixed_dtype():
    folder = "nurs_routines/tests/test_data/merge_mixed_dtype"
    merger = MergeAsOf(
        f"{folder}/Mixed_Shifts.csv", f"{folder}/Mixed_Demos.csv",
        "Staff Number", "Employee Number",
        dtypes={"Staff Number": str, "Employee Number": str}
    )
    merged_data = merger.main(
        left_on="Duty Date",
        right_on="Date_stamp"
    )
    assert not merged_data["Value2"].isna().all()


def test_merge_mixed_dtype_fails():

    folder = "nurs_routines/tests/test_data/merge_mixed_dtype"
    merger = MergeAsOf(
        f"{folder}/Mixed_Shifts.csv", f"{folder}/Mixed_Demos.csv",
        "Staff Number", "Employee Number"
    )
    merged_data = merger.main(
        left_on="Duty Date",
        right_on="Date_stamp"
    )
    assert merged_data["Value2"].isna().all()
