"""
Unit tests for utilities/io.py
"""
import os
import pytest
import pandas as pd

from nurs_routines.utilities.io import find_file, load_data, merge_in_file, remove_file, to_file
from nurs_routines.tests.fixtures.io_fixtures import test_data_path, data_generator, to_file_frame


def test_find_file(test_data_path):
    """
    Check function can find file that exists.
    """
    file = find_file(test_data_path, "find_me")
    _, name = os.path.split(file)
    assert ".csv" in name


def test_find_text_file(test_data_path):
    """
    Check error is raised if no file of type .csv, or .xls(x) is found.
    """
    with pytest.raises(FileNotFoundError, match=r"text_file"):
        find_file(test_data_path, "text_file")


def test_find_file_fails(test_data_path):
    """
    Check error is raised if file doesn't exist.
    """
    with pytest.raises(FileNotFoundError, match="dont_find_me"):
        find_file(test_data_path, "dont_find_me")


def test_load_data_csv(test_data_path):
    """
    Check .csv files can be read
    """
    path = os.path.join(test_data_path, "data_1.csv")
    data = load_data(path)
    assert data["A"].sum() == 5


def test_load_data_text(test_data_path):
    """
    Check .txt files can be read.
    """
    path = os.path.join(test_data_path, "text_data.txt")
    load_data(path)


def test_load_data_excel(test_data_path):
    """
    Check .xlsx files can be read.
    """
    path = os.path.join(test_data_path, "data_1.xlsx")
    load_data(path)


def test_load_data_fails_csv(test_data_path):
    """
    Check error is raised if a .csv file doesn't exist.
    """
    path = os.path.join(test_data_path, "no_file.csv")
    with pytest.raises(FileNotFoundError):
        load_data(path)


def test_load_data_fails_excel(test_data_path):
    """
    Check error is raised if a .xlsx file doesn't exist.
    """
    path = os.path.join(test_data_path, "no_file.xlsx")
    with pytest.raises(FileNotFoundError):
        load_data(path)


def test_load_data_fails_text(test_data_path):
    """
    Check error is raised if a .txt file doesn't exist.
    """
    path = os.path.join(test_data_path, "empty_text_data.txt")
    with pytest.raises(pd.errors.EmptyDataError):
        load_data(path)


def test_merge_in_file(test_data_path, data_generator):
    """
    Check that files can be merged in a temporary file
    """
    output = os.path.join(test_data_path, "merged_data.csv")
    remove_file(output)

    gen = data_generator(10, 5, 2)
    merge_in_file(output, gen)

    frame = pd.read_csv(output)
    n_cases, k = frame.shape
    assert n_cases == 10 * 5
    assert k == 2

def test_merge_in_file_repetition(test_data_path, data_generator):
    """
    Check that files can be merged in a temporary file when function called twice.
    """
    output = os.path.join(test_data_path, "merged_data.csv")
    remove_file(output)

    gen = data_generator(10, 5, 2)
    merge_in_file(output, gen)

    gen = data_generator(10, 5, 2)
    merge_in_file(output, gen)

    frame = pd.read_csv(output)
    n_cases, k = frame.shape
    assert n_cases == 10 * 5
    assert k == 2


def test_merge_in_file_fails(test_data_path, data_generator):
    """
    Check that error is raised if argument isn't an iterable of pandas data structures.
    """
    output = os.path.join(test_data_path, "merge_fail.csv")
    remove_file(output)

    with pytest.raises(TypeError):
        merge_in_file(output, 12)


def test_to_file(test_data_path, to_file_frame):
    """
    Check write to file works
    """
    output = os.path.join(test_data_path, "to_file.csv")
    remove_file(output)

    to_file(to_file_frame, test_data_path, "to_file.csv")
    frm = pd.read_csv(output)
    assert frm["A"].sum() == 6


def test_to_file_fails(test_data_path, to_file_frame):
    """
    Check error raises when writing to file non-pandas entity.

    """
    output = os.path.join(test_data_path, "to_file.csv")
    remove_file(output)

    with pytest.raises(AttributeError):
        to_file([1, 2, 3], test_data_path, "to_file.csv")
