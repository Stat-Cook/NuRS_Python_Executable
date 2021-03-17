"""
Utilities for file IO.
"""

import os
import logging
import pandas as pd
import pandas.errors

def find_file(path, name):
    """
    Find file with extension in path.
    Checks if found file has an appropriate extension.
    Parameters
    ----------
    path: str
        relative path to look in
    name: str
        file name of interest
    """
    _dir = [i for i in os.listdir(path) if not i.startswith(".")]
    files = [i for i in _dir if name in i]
    if not files:
        raise FileNotFoundError(
            "No files found for {} at {}".format(name, path)
        )

    files = [i for i in files if (".xls" in i) or (".csv" in i)]
    if not files:
        raise FileNotFoundError(
            "File not found of correct file type (csv, xls, or xlsx) for file {}".format(name)
        )
    if len(files) == 1:
        return os.path.join(path, files[0])

    return [os.path.join(path, file) for file in files]


def load_data(file_path):
    """
    Load data from a file_path. Adapts to deal with .csv or .xls(x)
    Parameters
    ----------
    file_path: str
        relative path to data set.
    """
    try:
        if ".xls" in file_path:
            # 'engine' unnecessary in later version of pandas:
            return pd.read_excel(file_path, engine="openpyxl")

        return pd.read_csv(file_path)
    except pandas.errors.ParserError:
        raise TypeError(f"File at {file_path} could not be read.  "
                        f"Check file type and try again.")


def merge_in_file(file, frame_iterable, delete_file=False, index=False):
    """
    Concatenate pandas frames by writing them to file.
    Parameters
    ----------
    file: str
        output destination
    frame_iterable: iterable
        a collection of data frames to concat.
    delete_file: bool
        Remove file if it all ready exists.
    drop_index
    """
    if delete_file and os.path.isfile(file):
        os.remove(file)
    # Catch if data isn't iterable already:
    _iter = iter(frame_iterable)
    # Write first to file with headings.
    frame = next(frame_iterable)
    frame.to_csv(file, mode="a", header=True, index=index)
    # Iterate over the rest without headings.
    for frame in frame_iterable:
        frame.to_csv(file, mode='a', header=False, index=index)


def to_file(data, path, file_name, index=False):
    """
    Write data to a location.
    Parameters
    ----------
    data: pandas.DataFrame
        data set to export
    path: str
        path to write file to
    file_name: str
        name for file
    """
    export_file = os.path.join(path, file_name)
    data.to_csv(export_file, index=index)
    logging.info("Data written to  %s", export_file)


def remove_file(file):
    """
    Remove a file if it exists.
    Parameters
    ----------
    file: str
        path to file to remove if it exists
    """
    try:
        os.remove(file)
    except FileNotFoundError:
        pass
