import pandas as pd
from .utilities import load_data


class GroupedFrame:

    def __init__(self, file_path, group_by):
        data = load_data(file_path)
        self.data = data.groupby(group_by)
        self.columns = data.columns
        self.options = data[group_by].unique()

    def __getitem__(self, item):
        try:
            return self.data.get_group(item)
        except KeyError:
            return pd.DataFrame([], columns=self.columns)
