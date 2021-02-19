"""
Unit tests for split_apply function.
"""
import os

from nurs_routines.utilities.split_apply import split_apply, cached_split_apply
from nurs_routines.tests.fixtures.split_apply_fixtures import split_apply_frm, \
    split_apply_increment_frm
from nurs_routines.tests.utilities import increment_column


def split_function(frm, *args):  # pylint: disable=unused-argument
    """Utility function for testing split_apply"""
    return increment_column(frm, "Value")


def test_split_apply(split_apply_frm, split_apply_increment_frm):
    """Check split_apply performs as expected"""
    result = split_apply(split_apply_frm, "ID", split_function)
    assert (result == split_apply_increment_frm).values.all()


def test_split_apply2(split_apply_frm, split_apply_increment_frm):
    """Check split_apply performs as expected"""
    result = split_apply(split_apply_frm, "ID2", split_function, sort_index=True)
    assert (result == split_apply_increment_frm).values.all()


def test_split_apply_two_levels(split_apply_frm, split_apply_increment_frm):
    """Check multi level split_apply performs as expected"""
    result = split_apply(split_apply_frm, ["ID", "ID2"], split_function)
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply."""
    result = cached_split_apply(split_apply_frm, "ID", split_function, "temp")
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply_file_exists(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply when file already exists"""
    open("temp", "w")

    result = cached_split_apply(split_apply_frm, "ID", split_function, "temp")
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply_replicate(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply with repeated use."""
    cached_split_apply(split_apply_frm, "ID", split_function, "temp")
    result = cached_split_apply(split_apply_frm, "ID", split_function, "temp")
    assert (result == split_apply_increment_frm).values.all()


def test_cached_split_apply_removes_file(split_apply_frm, split_apply_increment_frm):
    """Check cached split apply cleans up temporary files."""
    cached_split_apply(split_apply_frm, "ID", split_function, "temp")
    assert "temp" not in os.listdir()
