"""
Unit tests for split_apply function.
"""
import os
import numpy as np

from nurs_routines.utilities.split_apply import split_apply, cached_split_apply
from nurs_routines.tests.fixtures.split_apply_fixtures import split_apply_frm, \
    split_apply_increment_frm
from nurs_routines.tests.fixtures.scrambler_fixtures import mixed_size_scramble_data
from nurs_routines.tests.utilities import increment_column
from nurs_routines.utilities import shuffle


def split_function(frm, *args):  # pylint: disable=unused-argument
    """Utility function for testing split_apply"""
    return increment_column(frm, "Value")


def test_split_apply(split_apply_frm, split_apply_increment_frm):
    """Check split_apply performs as expected"""
    result = split_apply(split_apply_frm, "ID", split_function)
    assert (result == split_apply_increment_frm).values.all()


def test_split_apply2(split_apply_frm, split_apply_increment_frm):
    """Check split_apply performs as expected"""
    result = split_apply(split_apply_frm, "ID2", split_function)
    assert (result == split_apply_increment_frm).values.all()


def test_split_apply_two_levels(split_apply_frm, split_apply_increment_frm):
    """Check multi level split_apply performs as expected"""
    result = split_apply(split_apply_frm, ["ID", "ID2"], split_function)
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply."""
    result = cached_split_apply(split_apply_frm, "ID", split_function, "split_apply_temp")
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply_file_exists(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply when file already exists"""
    result = cached_split_apply(split_apply_frm, "ID", split_function, "split_apply_temp")
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply_replicate(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply with repeated use."""
    cached_split_apply(split_apply_frm, "ID", split_function, "split_apply_temp")
    result = cached_split_apply(split_apply_frm, "ID", split_function, "split_apply_temp")
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply_removes_file(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply cleans up temporary files."""
    cached_split_apply(split_apply_frm, "ID", split_function, "split_apply_temp")
    assert "temp" not in os.listdir()


def test_split_apply_shuffle(split_apply_frm):
    raw_means = split_apply_frm.groupby("ID").mean()
    result = split_apply(split_apply_frm, ["ID"], shuffle)
    shuffle_means = result.groupby("ID").mean()
    assert (shuffle_means == raw_means).values.all()


def test_split_apply_shuffle_breaks_corr(split_apply_frm):
    result = split_apply(split_apply_frm, ["ID"], shuffle)
    cov_matrix = np.cov(result["Value"], split_apply_frm["Value"])
    assert cov_matrix[0, 0] != cov_matrix[0, 1]


def test_split_apply_shuffle_some_small(mixed_size_scramble_data):
    result = split_apply(mixed_size_scramble_data, ["A"], shuffle)
    assert result["B"].isna().any()


def test_split_apply_check_end_size(mixed_size_scramble_data):
    result = split_apply(mixed_size_scramble_data, ["A"], shuffle)
    assert result.shape[0] == mixed_size_scramble_data.shape[0]
