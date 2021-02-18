"""
Tools for combining data sets in a folder.
Requires data sets to have the same data structure.
"""

import os
import logging
import pandas as pd

from .io import load_data
from .combine_file import CombineFile


class Combiner:

    """
    Combine multiple data sets in a destination path into a single data set.
    Can mix .xls(x) and .csv types - will only read the first sheet of .xls(x).
    Parameters
    ----------
    path: str
        Relative path to location of data sets.

    Attributes
    ----------
    data: pandas.DataFrame or None
        Current state of the data being combined

    columns: list
        The column headings of the first data set read in.
        Any after the first must have the same column headings.

    """

    def __init__(self, path: str):
        self.path = path
        self.data = None
        self.columns = None

    @property
    def path_content(self):
        """
        Check what files are at 'path'
        """
        return [i for i in os.listdir(self.path) if not i.startswith(".")]

    @property
    def path(self):
        """
        path property
        """
        return self._path

    @path.setter
    def path(self, path):
        try:
            assert os.path.isdir(path)
        except AssertionError:
            raise FileNotFoundError("No directory {} found".format(path))
        self._path = path


    def iterate_through_path(self, extract_date_function):
        """
        For each data set at 'path':
        * Read data
        * Parse file name for inclusion in data set [optional]
        * Check data headings match previous
        * Yield data.

        Parameters
        ----------
        extract_date_function: function
            Handler function to parse file name to date stamp.
            TODO: generalize this to extract any aspect of file name,
                will need to pass in and return data.

        """
        for file in self.path_content:
            logging.info("Adding %s", file)
            
            combine_file = CombineFile(file, self.path, self.columns)
            new_data = combine_file.process_file(extract_date_function)

            if self.columns is None:
                self.columns = new_data.columns

            yield new_data

    def read_and_combine(self, extract_date_function):
        """
        Combine all data sets at 'path'

        Parameters
        ----------
        extract_date_function: function
            Handler function to parse file name to date stamp.
            TODO: generalize this to extract any aspect of file name,
                will need to pass in and return data.
        """
        _iter = self.iterate_through_path(extract_date_function=extract_date_function)
        return pd.concat(_iter)

    def check_file_types(self):
        """
        Guard against incorrect file types prior to starting data read.
        """
        for file in self.path_content:
            file_type = any([i in file for i in ["xlsx", "xls", "csv"]])

            if not file_type:
                logging.info("Combine failed - Incorrect file type for %s", file)
                raise TypeError(
                    "Incorrect file type found (not xlsx, xls, or csv) for file {}.  "
                    "Please remove from folder {}".format(file, self.path)
                )

    def main(self, extract_date_function=None):
        """
        Main routine:
        * Checks file types at 'path'
        * Reads each data set (applying extract_date_function [optional])
        * Combine into a single data set.

        Parameters
        ----------
        extract_date_function: function
            Handler function to parse file name to date stamp.
        """
        print("Checking file types in {}".format(self.path))
        self.check_file_types()
        print("File types - Passed")
        print("Opening and combining files in {}".format(self.path))
        result = self.read_and_combine(extract_date_function)
        logging.info("Combination - Succesful")
        return result

    def __repr__(self):
        return "Combiner(path={}, number_of_files={})".format(
            self.path, len(self.path_content)
        )
