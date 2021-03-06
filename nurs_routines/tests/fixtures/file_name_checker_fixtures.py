"""Fixtures for test_file_name_checker"""
import os
import pytest

from nurs_routines.utilities.file_name_checker import FileNameChecker

test_data_path = os.path.join("nurs_routines", "tests", "test_data", "file_names")


@pytest.fixture
def file_name_checker_monthly():
    """
    Name checker class for testing monthly functions.
    """

    name_checker = FileNameChecker("Monthly_Test", "Effective date",
                                   "Monthly", "Monthly_data", prepend_path=test_data_path)
    return name_checker


@pytest.fixture
def file_name_checker_monthly_fails():
    """
    File Name Checker to test monthly files fail.
    """

    name_checker = FileNameChecker("Monthly_Test", "Effective date",
                                   "Monthly", "Monthly_data_failure", prepend_path=test_data_path)
    return name_checker


@pytest.fixture
def file_name_checker_quarterly():
    """
    File Name Checker to test quarterly files.
    """
    name_checker = FileNameChecker("Quarterly_Test", "Effective date",
                                   "Quarterly", "Quarterly_data", prepend_path=test_data_path)
    return name_checker


@pytest.fixture
def file_name_checker_quarterly_fails():
    """
    File Name Checker to test quarterly files fail.
    """
    name_checker = FileNameChecker("Quarterly_Test", "Effective date",
                                   "Quarterly", "Quarterly_data_failure",
                                   prepend_path=test_data_path)
    return name_checker


@pytest.fixture
def file_name_checker_full():
    """
    File Name Checker to test full file names.
    """
    name_checker = FileNameChecker("Full_Test", "Time Series",
                                   "Full", "", prepend_path=test_data_path)
    return name_checker
