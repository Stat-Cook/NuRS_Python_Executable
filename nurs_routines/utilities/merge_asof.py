"""
Aggregated merge based on date look up.
"""
from datetime import datetime
import logging
import pandas as pd

from .grouped_frame import GroupedFrame
from .progress_bar import ProgressBar
from .io import merge_in_file

pd.options.mode.chained_assignment = None


class MergeAsOf:
    """
    Aggregated-merge two data sets, based on the last relevant time in the reference set.
    Parameters
    ----------
    ungrouped_data: str or pd.DataFrame
        path to core data set or actual data set with dates to match.
    ungrouped_reference: str
        path to lookup data set or actual dat set to match to.
    left_group: str
        The group to aggregate 'data' on
    right_group: str
        The group to aggregate 'reference' on.
    earliest_date: datetime.datetime
        The earliest date that might appear in 'data'.  Defaults to Unix-epoch.
    log_merge: bool
        True/ False flag to control logging during merge.
        If true log file contains list of all merge keys.
    """
    # pylint:disable=too-many-arguments
    def __init__(self, ungrouped_data, ungrouped_reference, left_group, right_group,
                 earliest_date=datetime(1970, 1, 1), log_merge=False, dtypes=None):
        if isinstance(ungrouped_data, str):
            self.data = GroupedFrame(ungrouped_data, left_group, dtypes=dtypes)
        else:
            self.data = GroupedFrame.from_data(ungrouped_data, left_group, dtypes=dtypes)

        if isinstance(ungrouped_reference, str):
            self.reference = GroupedFrame(ungrouped_reference, right_group, dtypes=dtypes)
        else:
            self.reference = GroupedFrame.from_data(ungrouped_reference, right_group, dtypes=dtypes)

        self.earliest_date = earliest_date
        self.log_merge = log_merge


    def prepend_data(self, data, date_column):
        """
        Add an empty row to the start of a data set with one column set to 'earliest_date'
        Parameters
        ----------
        data: pandas.DataFrame
            The data set to add a row to the start to.
        date_column: str
            The column to insert 'earliest_date' at.
        """
        prepend = pd.DataFrame([self.earliest_date], columns=[date_column])
        return pd.concat([
            prepend,
            data
        ])


    def get_group(self, value):
        """
        Return the values for 'data' and 'reference' at a given key.
        Parameters
        ----------
        value: str
            the look up key.
        """
        return self.data[value], self.reference[value]

    def merge_asof(self, value, left_on, right_on):
        """
        Merge a group of 'data' and 'reference' by a look-backwards date merge.
        Parameters
        ----------
        value: str
            the group to look-up in 'data' and 'reference'.
        left_on: str
            the column in 'data' to merge on
        right_on: str
            the column in 'reference' to merge as of
        """
        left_data, right_data = self.get_group(value)
        right_data = self.prepend_data(right_data, right_on)

        left_data = self.date_sort(left_data, left_on)
        right_data = self.date_sort(right_data, right_on)

        right_cols = [i for i in right_data.columns if i not in left_data.columns]
        if left_on == right_on:
            right_cols += [right_on]

        return pd.merge_asof(left_data, right_data[right_cols], left_on=left_on, right_on=right_on)

    @staticmethod
    def date_sort(data, date_column, replace_date=datetime(2050, 1, 1)):
        """
        Sort a data set by a date column.
        Parameters
        ----------
        data: pandas.DataFrame
            The dataset to be sorted
        date_column: str
            The column of 'data' to be sorted.

        Returns
        -------
        pandas.DataFrame
        """
        try:
            data.loc[:, date_column] = pd.to_datetime(data[date_column])
        except pd.errors.OutOfBoundsDatetime:
            date_coerce = pd.to_datetime(data[date_column], errors="coerce")
            date_coerce[date_coerce.isna()] = replace_date
            data.loc[:, date_column] = date_coerce
        return data.sort_values(date_column)

    def iterate_merge(self, left_on, right_on):
        """
        Iterate through all values in 'data', and perform a merge as of.
        Parameters
        ----------
        left_on: str
            the column in 'data' to merge on
        right_on: str
            the column in 'reference' to merge as of
        """
        progress_bar = ProgressBar(20, len(self.data.options))

        print("Merge of {} items in progress:".format(progress_bar.max_steps))
        logging.debug("Merging data.")
        for value in self.data.options:
            progress_bar.step()
            if self.log_merge:
                logging.debug("Merging %s.", value)
            yield self.merge_asof(value, left_on, right_on)

    @property
    def overlap(self):
        in_both = [i for i in self.data.options if i in self.reference.options]
        in_data = [i for i in self.data.options if i not in self.reference.options]
        in_reference = [i for i in self.reference.options if i not in self.data.options]
        return {
            "In Both": in_both,
            "Only in Data": in_data,
            "Only in Ref": in_reference
        }

    def overlap_report_to_file(self, file):
        with open(file, "w") as f:
            for i in self.overlap:
                f.write(f"{i}:\n")
                str_map = map(str, self.overlap[i])
                string = "\n".join(str_map)
                f.write(string)
                f.write("\n")

    def pid_less_report_to_file(self, file):
        with open(file, "w") as f:
            for key, value in self.overlap.items():
                f.write(f"{key}: {len(value)}\n")

    def main(self, left_on, right_on, cached_merge=True,
             report_path=None, no_pid_report_path=None):
        """
        Iterate through values in 'data', and merge with 'reference' in a backward look up.
        Parameters
        ----------
        left_on: str
            the column in 'data' to merge on
        right_on: str
            the column in 'reference' to merge as of
        cached_merge: bool
            peform merge step by caching to local file.
        report_path: str
            File path to report overlap to.
        no_pid_report_path: str
            File path to report the quantity of overlap to.
        """
        # TODO: Understand why overlap_report_to_file threw error.
        if report_path:
            self.overlap_report_to_file(report_path)

        if no_pid_report_path:
            self.pid_less_report_to_file(no_pid_report_path)

        values = self.iterate_merge(left_on, right_on)
        if cached_merge:
            merge_in_file("temp.csv", values, delete_file=True)
            result = pd.read_csv("temp.csv")
        else:
            result = pd.concat(values)
        print("\nMerge Completed\n")
        return result
