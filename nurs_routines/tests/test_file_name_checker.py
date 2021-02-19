"""
Unit tests for FileNameChecker class
"""
import os
import pytest

from nurs_routines.tests.fixtures.file_name_checker_fixtures import file_name_checker_monthly,\
    file_name_checker_quarterly, file_name_checker_full
from nurs_routines.utilities import check_file_names
from nurs_routines.utilities.file_structure import file_options
from nurs_routines.utilities.file_name_checker import FileNameChecker


def test_fnc_init():
    """
    Check class can initialize.
    """
    options = file_options["ESR_Demographics"]
    name_checker = FileNameChecker(**options)
    assert os.path.isdir(name_checker.path)


def test_fnc_monthly(file_name_checker_monthly):
    """
    Check FNC monthly makes the right number of file names
    """
    expected_names = file_name_checker_monthly.target
    assert len(expected_names) == 60


def test_fnc_quarterly(file_name_checker_quarterly):
    """
    Check FNC quarterly makes the right number of file names
    """
    expected_names = file_name_checker_quarterly.target
    assert len(expected_names) == 20


def test_fnc_full(file_name_checker_full):
    """
    Check FNC full series makes the right number of file names
    """
    expected_names = file_name_checker_full.target
    assert len(expected_names) == 1


# Testing monthly file names:


def test_fnc_monthly_expected(file_name_checker_monthly):
    """
    Check FNC monthly performs as expected when no files are missing.
    """
    file_name_checker_monthly.report_missing(raise_exception=True)


def test_fnc_monthly_expected_fails(file_name_checker_monthly_fails):
    """
    Check FNC monthly raises error if files are missing.
    """
    with pytest.raises(FileNotFoundError):
        file_name_checker_monthly_fails.report_missing(raise_exception=True)


def test_fnc_monthly_duplicates(file_name_checker_monthly):
    """
    Check FNC monthly performs as expected when no files are duplicated.
    """
    file_name_checker_monthly.report_duplicates(raise_exception=True)


def test_fnc_monthly_duplicates_fails(file_name_checker_monthly_fails):
    """
    Check FNC monthly raises error if files are duplicated.
    """
    with pytest.raises(Exception):
        file_name_checker_monthly_fails.report_duplicates(raise_exception=True)


def test_fnc_monthly_extra(file_name_checker_monthly):
    """
    Check FNC monthly performs as expected when no files are unexpected.
    """
    file_name_checker_monthly.report_extra(raise_exception=True)


def test_fnc_monthly_extra_fails(file_name_checker_monthly_fails):
    """
    Check FNC monthly raises error if there are unexpected files.
    """
    with pytest.raises(Exception):
        file_name_checker_monthly_fails.report_duplicates(raise_exception=True)


# Testing quarterly file names:


def test_fnc_quarterly_missing(file_name_checker_quarterly):
    """
    Check FNC quarterly performs as expected when no files are missing.
    """
    file_name_checker_quarterly.report_missing(raise_exception=True)


def test_fnc_quarterly_missing_fails(file_name_checker_quarterly_fails):
    """
    Check FNC quarterly raises error if there are missing files.
    """
    with pytest.raises(FileNotFoundError):
        file_name_checker_quarterly_fails.report_missing(raise_exception=True)


def test_fnc_quarterly_duplicates(file_name_checker_quarterly):
    """
    Check FNC quarterly performs as expected when no files are duplicated.
    """
    file_name_checker_quarterly.report_duplicates(raise_exception=True)


def test_fnc_quarterly_duplicates_fails(file_name_checker_quarterly_fails):
    """
    Check FNC quarterly raises error if there are duplicated files.
    """
    with pytest.raises(Exception, match="duplicated"):
        file_name_checker_quarterly_fails.report_duplicates(raise_exception=True)


def test_fnc_quarterly_extra(file_name_checker_quarterly):
    """
    Check FNC quarterly performs as expected when no files are unnecessary.
    """
    file_name_checker_quarterly.report_extra(raise_exception=True)


def test_fnc_quarterly_extra_fails(file_name_checker_quarterly_fails):
    """
    Check FNC quarterly raises error if there are unnecessary files.
    """
    with pytest.raises(Exception, match="unexpected"):
        file_name_checker_quarterly_fails.report_extra(raise_exception=True)


# Test function binding:


def test_check_file_names_monthly():
    """
    Check function binding performs as expected
    """
    check_file_names("ESR_Demographics")


def test_check_file_names_monthly_fails():
    """
    Check function binding fails if the file doesn't exist in
    nurs_routines.utilities.file_structure.file_options
    """
    with pytest.raises(KeyError, match="no_data"):
        check_file_names("no_data")
