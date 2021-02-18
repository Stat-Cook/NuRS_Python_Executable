import pytest

from nurs_routines.utilities.combine_file import CombineFile
from nurs_routines.tests.fixtures.combiner_fixtures import combine_data_path


@pytest.fixture
def combiner_processor_no_expected_columns(combine_data_path):
    return CombineFile("file_1.csv", combine_data_path, None)


@pytest.fixture
def combiner_processor_expected_columns(combine_data_path):
    return CombineFile("file_1.csv", combine_data_path, list("ABCDE"))

@pytest.fixture
def combiner_processor_too_few_columns(combine_data_path):
    return CombineFile("file_1.csv", combine_data_path, list("AB"))


@pytest.fixture
def combiner_processor_no_such_file(combine_data_path):
    return CombineFile("file_X.csv", combine_data_path, None)
