import os

from nurs_routines.utilities.io import find_file, load_data, merge_in_file, remove_file, to_file
from nurs_routines.tests.fixtures.io_fixtures import *


def test_find_file(test_data_path):
    file = find_file(test_data_path, "find_me")
    _, name = os.path.split(file)
    assert ".csv" in name


def test_find_text_file(test_data_path):
    with pytest.raises(FileNotFoundError, match=r"text_file"):
        find_file(test_data_path, "text_file")


def test_find_file_fails(test_data_path):
    with pytest.raises(FileNotFoundError, match="dont_find_me"):
        find_file(test_data_path, "dont_find_me")


def test_load_data_csv(test_data_path):
    path = os.path.join(test_data_path, "data_1.csv")
    data = load_data(path)
    assert data["A"].sum() == 5


def test_load_data_text(test_data_path):
    path = os.path.join(test_data_path, "text_data.txt")
    load_data(path)


def test_load_data_excel(test_data_path):
    path = os.path.join(test_data_path, "data_1.xlsx")
    load_data(path)


def test_load_data_fails_csv(test_data_path):
    path = os.path.join(test_data_path, "no_file.csv")
    with pytest.raises(FileNotFoundError):
        load_data(path)


def test_load_data_fails_excel(test_data_path):
    path = os.path.join(test_data_path, "no_file.xlsx")
    with pytest.raises(FileNotFoundError):
        load_data(path)


def test_load_data_fails_text(test_data_path):
    path = os.path.join(test_data_path, "empty_text_data.txt")
    with pytest.raises(pd.errors.EmptyDataError):
        load_data(path)


def test_merge_in_file(test_data_path, data_generator):
    output = os.path.join(test_data_path, "merged_data.csv")
    remove_file(output)

    gen = data_generator(10, 5, 2)
    merge_in_file(output, gen)

    frame = pd.read_csv(output)
    n, k = frame.shape
    assert n == 10 * 5
    assert k == 2


def test_merge_in_file_fails(test_data_path, data_generator):
    output = os.path.join(test_data_path, "merge_fail.csv")
    remove_file(output)

    with pytest.raises(TypeError):
        merge_in_file(output, 12)


def test_to_file(test_data_path, to_file_frame):
    output = os.path.join(test_data_path, "to_file.csv")
    remove_file(output)

    to_file(to_file_frame, test_data_path, "to_file.csv")
    frm = pd.read_csv(output)
    assert frm["A"].sum() == 6


def test_to_file_fails(test_data_path, to_file_frame):
    output = os.path.join(test_data_path, "to_file.csv")
    remove_file(output)

    with pytest.raises(AttributeError):
        to_file([1, 2, 3], test_data_path, "to_file.csv")

