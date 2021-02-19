"""
Unit tests for CombineFile class.
"""
import pandas as pd
import pytest

from nurs_routines.tests.fixtures.combine_file_fixtures import \
    combiner_processor_no_expected_columns, combiner_processor_no_such_file, \
    combiner_processor_expected_columns, combiner_processor_too_few_columns


def test_load_data(combiner_processor_no_expected_columns):
    """
    Test data loads successfully.
    """
    data = combiner_processor_no_expected_columns.load_data()
    assert isinstance(data, pd.DataFrame)


def test_load_data_no_known_file(combiner_processor_no_such_file):
    """
    Test for error when file can't be found.
    """
    with pytest.raises(FileNotFoundError):
        combiner_processor_no_such_file.load_data()


def test_load_data_column_miss_match(combiner_processor_expected_columns):
    """
    Check for error when new data has different columns than expected.
    """
    with pytest.raises(AttributeError):
        combiner_processor_expected_columns.process_file()


def test_load_data_too_few_columns(combiner_processor_too_few_columns):
    """
    Check for error when new data has less columns than expected.
    """
    with pytest.raises(ValueError):
        combiner_processor_too_few_columns.process_file()


def test_compare_column_length(combiner_processor_expected_columns):
    """
    Check compare old and new column lengths.
    """
    combiner_processor_expected_columns.compare_column_length(range(5))


def test_compare_column_length_fails(combiner_processor_expected_columns):
    """
    Check error raises when old and new columns are different lengths.
    """
    with pytest.raises(ValueError):
        combiner_processor_expected_columns.compare_column_length(range(6))


def test_compare_column_length_fails_str(combiner_processor_expected_columns):
    """
    Check for error when passing in a string instead of a list.
    """
    with pytest.raises(TypeError):
        combiner_processor_expected_columns.are_columns_consistent("ABCDE")
