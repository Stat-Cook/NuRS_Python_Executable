"""
Tools for reporting on PID in a data set.
"""

import numpy as np
import pandas as pd
from .pid_result import PIDResults
from .pid_pattern import PIDPattern


class PIDReporter:
    """
    Report on PID contained in a data set.
    Properties
    -----------
    pattern_list: List[str]
    """

    def __init__(self, pattern_list):
        self.pattern_list = pattern_list
        self.melted = None
        self.results_dict = PIDResults(dict)

    def melt_data(self, data: pd.DataFrame):
        """
        Melt a pandas data frame into long form
        Parameters
        ----------
        data: pandas.DataFrame
            Data set to be checked for PID
        Returns
        -------
        None
        """
        self.melted = data.melt(ignore_index=False)

    def check_pattern(self, pattern):
        """
        For a given string, check if it appears in the self.melted
        Parameters
        ----------
        pattern: str
            String to check against e.g. 'bob'.
        Returns
        -------
        np.matrix with columns [row, column, PID]
        """
        if self.melted is None:
            raise AttributeError("Data not loaded yet.")

        compiled_pattern = PIDPattern(pattern)
        sel = self.melted[self.melted["value"].apply(str).apply(compiled_pattern.match).apply(bool)]
        pid_location = np.transpose([
            sel.index,
            sel["variable"].values,
            sel["value"].values
        ])
        return pid_location

    def check_data(self):
        """
        Iterate through all patterns given at initialization and produce a report object.
        Returns
        -------
        PIDResults
        """
        results_dict = PIDResults(dict)

        for pattern in self.pattern_list:
            results_dict[pattern] = self.check_pattern(pattern)

        return results_dict

    def check_data_set(self, data):
        """
        Check data set for all patterns given at initialization.
        Parameters
        ----------
        data: pandas.DataFrame
            Data frame to check for PID
        Returns
        -------
        PIDResults dictionary
        """

        if not isinstance(data, pd.DataFrame):
            data = pd.DataFrame(data)

        self.melt_data(data)
        return self.check_data()

    def report_data_set_to_file(self, data, filename):
        """
        Send report on PID to a file.
        Parameters
        ----------
        data: pandas.DataFrame
            Data frame to check for PID
        filename: str
            File name to save results to
        Returns
        -------
        PIDResults
        """
        results = self.check_data_set(data)
        results.context_to_screen()
        results.context_to_file(filename)
        return results
