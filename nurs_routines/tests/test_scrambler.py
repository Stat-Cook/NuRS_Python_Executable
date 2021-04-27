"""
Unit tests for scramble functions
"""
import pandas as pd
from nurs_routines.utilities.scrambler import scramble, scramble_to_file
from nurs_routines.tests.fixtures.scrambler_fixtures import scrambling_data, \
    scrambled_averages, scrambled_averages_id_id2, mixed_size_scramble_data, \
    mixed_size_scramble_data2


def test_scramble(scrambling_data, scrambled_averages):
    """Check scramble function for single column aggregation"""
    scrambled = scramble(scrambling_data, ["ID"], ["value"])
    groups = scrambled.groupby("ID")
    averages = pd.Series({key: df["value"].mean() for key, df in groups})
    assert (averages == scrambled_averages).values.all()


def test_scramble_2_levels(scrambling_data, scrambled_averages_id_id2):
    """Check scramble function for two column aggregation"""
    scrambled = scramble(scrambling_data, ["ID", "ID2"], ["value"])
    groups = scrambled.groupby(["ID", "ID2"])
    averages = pd.Series({key: df["value"].mean() for key, df in groups})
    assert (averages == scrambled_averages_id_id2).values.all()


def test_scramble_to_file(scrambling_data, scrambled_averages):
    """Check scramble_to_file with one column aggregation"""
    scrambled = scramble_to_file(scrambling_data, ["ID"], ["value"], "test_temp")
    groups = scrambled.groupby("ID")
    averages = pd.Series({key: df["value"].mean() for key, df in groups})
    assert (averages == scrambled_averages).values.all()


def test_scramble_to_file_repeat(scrambling_data, scrambled_averages):
    """Check repetition of scramble_to_file with one column aggregation"""
    scramble_to_file(scrambling_data, ["ID"], ["value"], "test_temp")
    scrambled = scramble_to_file(scrambling_data, ["ID"], ["value"], "test_temp")
    groups = scrambled.groupby("ID")
    averages = pd.Series({key: df["value"].mean() for key, df in groups})
    assert (averages == scrambled_averages).values.all()


def test_scramble_to_file_2_levels(scrambling_data, scrambled_averages_id_id2):
    """Check scramble_to_file with two column aggregation"""
    scrambled = scramble_to_file(scrambling_data, ["ID", "ID2"], ["value"], "test_temp")
    groups = scrambled.groupby(["ID", "ID2"])
    averages = pd.Series({key: df["value"].mean() for key, df in groups})
    assert (averages == scrambled_averages_id_id2).values.all()


def test_mixed_size_scramble_retains_index_order(mixed_size_scramble_data):
    scrambled = scramble_to_file(mixed_size_scramble_data, ["A"], ["B", "C"], "test_temp")
    assert all((scrambled["A"] == scrambled["A2"]).values)


def test_mixed_size_scramble_check_data_removed(mixed_size_scramble_data):
    scrambled = scramble_to_file(mixed_size_scramble_data, ["A"], ["B", "C"], "test_temp")
    assert all(scrambled[scrambled["A"] == "C"]["B"].isna().values)


def test_mixed_size_scramble_no_data_loss(mixed_size_scramble_data2):
    scrambled = scramble_to_file(mixed_size_scramble_data2, ["A", "A2"], ["B", "C"], "test_temp")
    assert scrambled.shape[0] == mixed_size_scramble_data2.shape[0]
