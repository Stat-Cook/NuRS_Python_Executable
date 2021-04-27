"""
Tools for working with grouped data.
Used for merging aggregated data.
"""

import pandas as pd
from .io import load_data


class GroupedFrame:
    """
    A pandas grouped DataFrame loaded from file.
    Parameters
    ----------
    file_path: str
        Path to the data set file
    group_by: str or list
        The column(s) to group on.
    """

    def __init__(self, file_path, group_by, dtypes=None):
        self.path = None
        self.data = None
        self.columns = None
        self.options = None

        if file_path is not None:
            data = load_data(file_path, dtypes=dtypes)
            self.path = file_path
            self.initialize_values(data, group_by)

    @classmethod
    def from_data(cls, data, group_by, dtypes=None):
        empty = cls(None, None)
        if dtypes:
            data = data.astype(dtypes)

        empty.initialize_values(data, group_by)
        return empty

    def initialize_values(self, data, group_by):
        self.data = data.groupby(group_by)
        self.columns = data.columns
        self.options = list(self.data.groups)  # data[group_by].unique()

    def __repr__(self):
        return "GroupedFrame(path={})".format(self.path)

    def __getitem__(self, item):
        try:
            return self.data.get_group(item)
        except KeyError:
            return pd.DataFrame([], columns=self.columns)
