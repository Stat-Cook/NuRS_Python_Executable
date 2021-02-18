import pandas as pd

from nurs_routines.tests.fixtures.combine_file_fixtures import *


def test_load_data(combiner_processor_no_expected_columns):
    data = combiner_processor_no_expected_columns.load_data()
    assert isinstance(data, pd.DataFrame)


def test_load_data_no_known_file(combiner_processor_no_such_file):
    with pytest.raises(FileNotFoundError):
        combiner_processor_no_such_file.load_data()


def test_load_data_column_miss_match(combiner_processor_expected_columns):
    with pytest.raises(AttributeError):
        combiner_processor_expected_columns.process_file()


def test_load_data_too_few_columns(combiner_processor_too_few_columns):
    with pytest.raises(ValueError):
        combiner_processor_too_few_columns.process_file()


def test_compare_column_length(combiner_processor_expected_columns):
    combiner_processor_expected_columns.compare_column_length(range(5))


def test_compare_column_length_fails(combiner_processor_expected_columns):
    with pytest.raises(ValueError):
        combiner_processor_expected_columns.compare_column_length(range(6))


def test_compare_column_length_fails_str(combiner_processor_expected_columns):
    with pytest.raises(TypeError):
        combiner_processor_expected_columns.are_columns_consistent("ABCDE")
