import pytest

from nurs_routines.tests.file_name_checker_fixtures import *
from nurs_routines.utilities import check_file_names


def test_FileNameChecker_init():
    options = file_options["ESR_Demographics"]
    name_checker = FileNameChecker(**options)
    assert os.path.isdir(name_checker.path)


def test_FNC_monthly(file_name_checker_monthly):
    expected_names = file_name_checker_monthly.target
    assert len(expected_names) == 60


def test_FNC_quarterly(file_name_checker_quarterly):
    expected_names = file_name_checker_quarterly.target
    assert len(expected_names) == 20


def test_FNC_full(file_name_checker_full):
    expected_names = file_name_checker_full.target
    assert len(expected_names) == 1


# Testing monthly file names:


def test_FNC_monthly_expected(file_name_checker_monthly):
    file_name_checker_monthly.report_missing(raise_exception=True)


def test_FNC_monthly_expected_fails(file_name_checker_monthly_fails):
    with pytest.raises(FileNotFoundError):
        file_name_checker_monthly_fails.report_missing(raise_exception=True)


def test_FNC_monthly_duplicates(file_name_checker_monthly):
    file_name_checker_monthly.report_duplicates(raise_exception=True)


def test_FNC_monthly_duplicates_fails(file_name_checker_monthly_fails):
    with pytest.raises(Exception):
        file_name_checker_monthly_fails.report_duplicates(raise_exception=True)


def test_FNC_monthly_extra(file_name_checker_monthly):
    file_name_checker_monthly.report_extra(raise_exception=True)


def test_FNC_monthly_extra_fails(file_name_checker_monthly_fails):
    with pytest.raises(Exception):
        file_name_checker_monthly_fails.report_duplicates(raise_exception=True)


# Testing quarterly file names:


def test_FNC_quarterly_missing(file_name_checker_quarterly):
    file_name_checker_quarterly.report_missing(raise_exception=True)


def test_FNC_quarterly_missing_fails(file_name_checker_quarterly_fails):
    with pytest.raises(FileNotFoundError):
        file_name_checker_quarterly_fails.report_missing(raise_exception=True)


def test_FNC_quarterly_duplicates(file_name_checker_quarterly):
    file_name_checker_quarterly.report_duplicates(raise_exception=True)


def test_FNC_quarterly_duplicates_fails(file_name_checker_quarterly_fails):
    with pytest.raises(Exception, match="duplicated"):
        file_name_checker_quarterly_fails.report_duplicates(raise_exception=True)


def test_FNC_quarterly_extra(file_name_checker_quarterly):
    file_name_checker_quarterly.report_extra(raise_exception=True)


def test_FNC_quarterly_extra_fails(file_name_checker_quarterly_fails):
    with pytest.raises(Exception, match="unexpected"):
        file_name_checker_quarterly_fails.report_extra(raise_exception=True)


# Test function binding:


def test_check_file_names_monthly():
    check_file_names("ESR_Demographics")


def test_check_file_names_monthly_fails():
    with pytest.raises(KeyError, match="no_data"):
        check_file_names("no_data")
