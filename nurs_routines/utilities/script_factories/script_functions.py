"""
Human readable bindings to the nurs_routine.utilities implementations.
Supplies pipe-able APIs so that each function takes the operable data as
the first argument.
"""
import os
import pandas as pd

from ..combiner import Combiner
from ..io import find_file, load_data, to_file
from ..utilities import shuffle
from ..scrambler import scramble_to_file
from ..merge_asof import MergeAsOf
from ..month_tools import GetMonth
from ..remove_pid import remove_pid
from ..split_apply import split_apply


class ScriptFunctionFactory:

    """
    Class for binging APIs to pipe-able functions with human readable names.
    """

    def __init__(self):
        pass

    @staticmethod
    def find_file(name, path="Trust_data"):
        """
        Binding to nurs_routines.io.find_file.
        Parameters
        ----------
        name: str
            file name
        path: str
            path to file
        Returns
        -------
        str
        """
        if not isinstance(path, str):
            path = os.path.join(*path)
        return find_file(path, name)

    @staticmethod
    def scramble(data, keys):
        """
        Binding to nurs_routines.split_apply.split_apply and
        nurs_routines.utilities.shuffle
        Parameters
        ----------
        data: pandas.DataFrame
            data to be shuffled.
        keys: List[str]
            keys to group data on for shuffling
        Returns
        -------
        pandas.DataFrame
        """
        return split_apply(data, keys, shuffle)

    @staticmethod
    def load_data(name, path="Trust_data"):
        """
        Binding to nurs_routines.io.load_data
        Parameters
        ----------
        name: str
            file name
        path: str
            path to read data from
        Returns
        -------
        pandas.DataFrame
        """
        file_path = find_file(path, name)
        return load_data(file_path)

    def find_more_files(self, file, name, path):
        """
        Binding to nurs_routines.io.find_file when multiple files are needed,
        e.g. alignment scripts.
        Parameters
        ----------
        file: str
            relative file path to data file
        name: str
            name of additional file path
        path: str
            path to additional file path
        Returns
        -------
        List[str]
        """
        return [file] + [self.find_file(name, path)]

    @staticmethod
    def merge_as_of(paths, left_on, right_on, left_date, right_date, report_path=None):
        """
        Binding to nurs_routines.merge_asof.MergeAsOf.main routine.
        Allows for alignment of two data sets via the lockback method.
        Parameters
        ----------
        paths: List[str]
            paths to the 'left' and 'right' data sets.
            'Left' is the core data set.
            'Right' the reference data set to look up in
        left_on: str
            column in 'left' to group on
        right_on: str
            column in 'right' to group on
        left_date: str
            column in 'left' to look up from
        right_date: str
            column in 'right' to look back to.
        Returns
        -------
        pandas.DataFrame
        """
        assert len(paths) == 2
        merger = MergeAsOf(*paths, left_on, right_on)
        merged_data = merger.main(left_date, right_date, report_path=report_path)
        return (
            merged_data,
            [i for i in merger.reference.columns if i in merged_data.columns]
        )

    @staticmethod
    def month_shuffler(data, aggregate_columns=None):
        """
        Binding to nurs_routines.utilities.month_tools.GetMonth.grouped_monthly_shuffle
        Parameters
        ----------
        data: pandas.DataFrame
            Data set to shuffle
        aggregate_columns: List[str]
            Column of data to group by before shuffle
        Returns
        -------
        pandas.DataFrame
        """
        month_shuffler = GetMonth()
        return month_shuffler.grouped_monthly_shuffle(data[0], aggregate_columns, data[1])

    @staticmethod
    def scramble_merge_as_of(data, aggregate_columns=None, file_path=None):
        """
        Binding to nurs_routines.utilities.scrambler.scramble_to_file.
        Parameters
        ----------
        data: (pandas.DataSet, List[str])
            (The data set to be scrambled, columns to scramble)
        aggregate_columns: List[str]
            Columns to aggregate
        file_path: str
            Path for the temporary file location for caching data to.
        Returns
        -------
        pandas.DataFrame
        """
        assert len(data) == 2
        return scramble_to_file(
            data[0],
            aggregate_columns,
            data[1],
            file_path
        )

    @staticmethod
    def to_file_scripted(data, extract_path, file_name):
        """
        Binding to nurs_routines.utilites.io.to_file.
        Parameters
        ----------
        data: pandas.DataFrame
            Data set to be saved to file
        extract_path: str
            Path for export
        file_name: str
            Name of file for export.
        Returns
        -------
        pandas.DataFrame
        """
        if not isinstance(extract_path, str):
            extract_path = os.path.join(*extract_path)

        to_file(data, extract_path, file_name + ".csv")

        print("Complete - data written to {}".format(
            os.path.join(extract_path, file_name + ".csv")
        ))

        return data

    @staticmethod
    def manipulate_column(data, new_column, old_column, function):
        """
        Apply a one off function to a new column of data to 'data'
        Parameters
        ----------
        data: pandas.DataFrame
            data set to be manipulated
        new_column: str
            Name of new column
        old_column: str
            Name of existing column
        function: function
            Function to apply to existing column

        Returns
        -------
        pandas.DataFrame
        """
        data[new_column] = data[old_column].apply(function)
        return data

    @staticmethod
    def combine_data_sets(path, extract_date_function=None, progress_bar=False):
        """
        Binding to nurs_routines.utilites.combiner.Combiner.main.
        Parameters
        ----------
        path: Str
            file path to a folder of data sets
        extract_date_function: function [optional]
            function to extract a date from the file names and add to the data set
        Returns
        -------
        pandas.DataFrame
        """
        return Combiner(path, progress_bar).main(extract_date_function=extract_date_function)

    def to_datetime(self, data, columns):
        """
        Cast columns of data to datetimes.
        Parameters
        ----------
        data: pandas.DataFrame
            Data set to be manipulated
        columns: List[str] or str
            Column(s) to be case to datetime.
        Returns
        -------
        pandas.DataFrame
        """
        if not isinstance(columns, str):
            data[columns] = data[columns].apply(pd.to_datetime)
        else:
            data[columns] = pd.to_datetime(data[columns])
        return data

    def inject_data(self, data):
        return data

    @property
    def script_functions(self):
        """
        Property - dictionary of function bindings with human readable names.
        Returns
        -------
        dict
        """
        return {
            "Apply function": lambda data, function: function(data),
            "Inject data": self.inject_data,
            "Join file names": lambda file: os.path.join("Trust_data", file),
            "Find files": self.find_file,
            "Find more files": self.find_more_files,
            "Load data": self.load_data,
            "Combine datasets": self.combine_data_sets,
            "Manipulate column": self.manipulate_column,
            "To datetime": self.to_datetime,
            "Reset index": lambda x: x.reset_index(drop=True),
            "Merge as of": self.merge_as_of,
            "Scramble": self.scramble,
            "Scramble as of": self.scramble_merge_as_of,
            "Scramble in months": self.month_shuffler,
            "Remove PID": remove_pid,
            "To file": self.to_file_scripted
        }
