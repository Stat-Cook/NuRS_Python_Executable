"""
Class for processing files during combination.
"""
import os

from .io import load_data


class CombineFile:
    """
    Process a data file from disk as needed by nurs_routines.utilities.Combiner
    Parameters
    ----------
    file: str
        The file to be loaded
    path: str
        The system path to the file.
    expected_columns: list or None
        The expected column headings.
    """

    def __init__(self, file, path, expected_columns: list = None):

        self.file = file
        self.path = path
        self.expected_columns = expected_columns

    def __repr__(self):
        return f"CombineFile(file={self.file}, path={self.path}, " \
               f"expected_columns={self.expected_columns})"

    def load_data(self):
        """
        Read data from path/file.
        Returns
        -------
        pandas.DataFrame
        """
        file_path = os.path.join(self.path, self.file)
        return load_data(file_path)

    def apply_extract_date_function(self, extract_date_function, data):
        """
        Create a new column based on the given function
        Parameters
        ----------
        extract_date_function: func
            Function to convert file name to date stamp
        data: pandas.DataFrame
            Data structure to be added to
        Returns
        -------
        pandas.DataFrame
        """
        data["Date_stamp"] = extract_date_function(self.file)
        return data

    def compare_column_length(self, proposed_columns):
        """
        Check new columns and existing columns are of equivalent length
        Parameters
        ----------
        proposed_columns: list
            The new column headings.
        Returns
        -------
        None
        """
        len_expected = len(self.expected_columns)
        len_proposed = len(proposed_columns)

        if len_expected != len_proposed:
            raise ValueError(
                f"New data columns  not of same length as expected columns "
                f"({len_proposed} vs {len_expected})."
                f"  Error with file ({self.file})"
            )

    def compare_column_content(self, proposed_columns):
        """
        Check that old and new columns contain the same headings in the same order.
        Parameters
        ----------
        proposed_columns: list
            The new column headings.
        Returns
        -------
        None
        """
        if any(i != j for i, j in zip(self.expected_columns, proposed_columns)):
            raise AttributeError(
                f"New data columns do not match expected columns, error with file {self.file}"
            )

    def are_columns_consistent(self, proposed_columns: list):
        """
        Apply various rules to check old and new columns match
        Parameters
        ----------
        proposed_columns: list
            New column headings.
        Returns
        -------
        bool
        """
        if isinstance(proposed_columns, str):
            raise TypeError("Argument `proposed_columns` should be a list or tuple.")

        if self.expected_columns is None:
            return True

        self.compare_column_length(proposed_columns)
        self.compare_column_content(proposed_columns)

        return True

    def process_file(self, extract_date_function=None):
        """
        Process the data from path/file, extracting date if needed and ensuring column
        names are as expected
        Parameters
        ----------
        extract_date_function: func
            Function to extract date stamp from file name.
        Returns
        -------
        pandas.DataFrame
        """
        data = self.load_data()

        if extract_date_function:
            data = self.apply_extract_date_function(extract_date_function, data)

        self.are_columns_consistent(data.columns)

        return data
