import os
import pytest

from nurs_routines.utilities.file_name_checker import FileNameChecker, check_file_names
from nurs_routines.utilities.file_structure import file_options


test_data_path = os.path.join("nurs_routines", "tests", "test_data", "file_names")


@pytest.fixture
def file_name_checker_monthly():

    name_checker = FileNameChecker("Monthly_Test", "Effective date",
                                   "Monthly", "Monthly_data", prepend_path=test_data_path)
    return name_checker

@pytest.fixture
def file_name_checker_monthly_fails():

    name_checker = FileNameChecker("Monthly_Test", "Effective date",
                                   "Monthly", "Monthly_data_failure", prepend_path=test_data_path)
    return name_checker


@pytest.fixture
def file_name_checker_quarterly():
    name_checker = FileNameChecker("Quarterly_Test", "Effective date",
                                   "Quarterly", "Quarterly_data", prepend_path=test_data_path)
    return name_checker


@pytest.fixture
def file_name_checker_quarterly_fails():
    name_checker = FileNameChecker("Quarterly_Test", "Effective date",
                                   "Quarterly", "Quarterly_data_failure", prepend_path=test_data_path)
    return name_checker


@pytest.fixture
def file_name_checker_full():
    name_checker = FileNameChecker("Full_Test", "Time Series",
                                   "Full", "", prepend_path=test_data_path)
    return name_checker