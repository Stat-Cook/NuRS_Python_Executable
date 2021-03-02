"""
Tools for applying a function to a divided data set.
"""
import os
import pandas as pd

from .io import merge_in_file
from .progress_bar import progress_bar_iter


class SplitApplier:
    """
    Class for pre-processing and post-processing data.
    Allows for the original order of the data set to be preserved.
    Parameters
    ----------
    data: pandas.DataFrame
        the data set to be pre-processed
    group_by: List[str]
        the column names for grouping by.
    """

    def __init__(self, data, group_by):

        self.data = data.copy()
        self.columns = list(self.data.columns)
        self.groupby = group_by
        self.temporary_index = self.make_temporary_index()

    def pre_process(self):
        """
        Capture the index as a temporary variable in the data set.

        Returns
        -------
        pandas.DataFrame
        """
        self.data[self.temporary_index] = self.data.index
        groups = self.data.set_index(self.groupby).groupby(lambda x: x)
        return groups


    def post_process(self, new_data):
        """
        Restore original ordering based on `temporary_index`, and return columns to
        original order with any created columns at the end.
        Parameters
        ----------
        new_data: pandas.DataFrame
            the data set that has been processed.

        Returns
        -------
        pandas.DataFrame
        """
        new_data = new_data.set_index(self.temporary_index)
        new_data = new_data.sort_index()

        columns = self.columns + [i for i in new_data.columns if i not in self.columns]
        return new_data.reset_index(drop=True)[columns]

    def make_temporary_index(self):
        """
        Make a column name for the temporary index that isn't in use by the dataset.
        Returns
        -------
        str
        """
        template = "__Raw_Index_{}__"
        i = 0
        while True:
            proposed_column = template.format(i)
            if proposed_column not in self.columns:
                return proposed_column

            i += 1


def split_apply(frm, groupby, func):
    """
    Divide a data set based on a column and apply a function to each chunk
    Parameters
    ----------
    frm: pandas.DataFrame
        data set to be grouped
    groupby: str or List[str]
        column to group on
    func: function
        function to apply to each chunk of data
    size_check: bool
        boolean flag - if True check each chunk has more than 1 case.

    Returns
    -------
    pandas.DataFrame
    """
    split_applier = SplitApplier(frm, groupby)
    groups = split_applier.pre_process()

    merged = pd.concat(progress_bar_iter(groups, func))
    merged = merged.reset_index()

    return split_applier.post_process(merged)


def cached_split_apply(frm, groupby, func, file):
    """
    Divide a data set based on a column and apply a function to each chunk.
    Recombine the data by caching to a temporary file.
    Parameters
    ----------
    frm: pandas.DataFrame
        data set to be grouped
    groupby: str or List[str]
        column to group on
    func: function
        function to apply to each chunk of data
    size_check: bool
        boolean flag - if True check each chunk has more than 1 case.
    file: str or IOStream
        the file to combine the data in.

    Returns
    -------
    pandas.DataFrame
    """
    split_applier = SplitApplier(frm, groupby)
    groups = split_applier.pre_process()

    if os.path.isfile(file):
        os.remove(file)

    _iter = progress_bar_iter(groups, func)
    with open(file, "a") as output_file:
        merge_in_file(output_file, _iter, index=True)

    result = pd.read_csv(file)
    os.remove(file)

    return split_applier.post_process(result)
