import os
import numpy as np
import pandas as pd

TEST_ROOT_DIR = os.path.join("nurs_routines", "tests", "test_data")


def make_blank_files(path, names):
    for name in names:
        file = os.path.join(TEST_ROOT_DIR, path, name)
        with open(file, "w") as f:
            f.write("")


def delete_directory_contents(path):
    path_content = os.listdir(os.path.join(TEST_ROOT_DIR, path))
    for i in path_content:
        os.remove(os.path.join(TEST_ROOT_DIR, path, i))


def make_monthly_files(path="file_names/Monthly_data"):
    delete_directory_contents(path)

    months = pd.date_range("2015-07", "2020-06", freq="MS")
    date_strings = (i.strftime("%y%m%d") for i in months)
    names = ("Monthly_Test {}.csv".format(i) for i in date_strings)

    make_blank_files(path, names)


def make_quarterly_files(path="file_names/Quarterly_data"):
    delete_directory_contents(path)

    months = pd.date_range("2015-07", "2020-06", freq="3MS")
    date_strings = (i.strftime("%y%m%d") for i in months)
    names = ("Quarterly_Test {}.csv".format(i) for i in date_strings)

    make_blank_files(path, names)


def generate_poor_file_names(path, make_file_function):
    make_file_function(path)

    path_content = os.listdir(os.path.join(TEST_ROOT_DIR, path))
    to_delete = np.random.choice(path_content, 3, replace=False)
    for file in to_delete:
        os.remove(os.path.join(TEST_ROOT_DIR, path, file))

    duplicate_files = np.random.choice(path_content, 3, replace=False)
    make_blank_files(path, duplicate_files)

    extra_files = ["Extra_1.csv", "Extra_1.txt"]
    make_blank_files(path, extra_files)


if __name__ == '__main__':

    make_monthly_files("file_names/Monthly_data")
    make_quarterly_files("file_names/Quarterly_data")
    generate_poor_file_names("file_names/Monthly_data_failure", make_monthly_files)
    generate_poor_file_names("file_names/Quarterly_data_failure", make_quarterly_files)
