import pandas as pd
from datetime import datetime
from .grouped_frame import GroupedFrame
from .progress_bar import ProgressBar


pd.options.mode.chained_assignment = None


class MergeAsOf:

    def __init__(self, data, reference, left_group, right_group,
                 earliest_date=datetime(1970,1,1)):
        self.data = GroupedFrame(data, left_group)
        self.reference = GroupedFrame(reference, right_group)
        self.earliest_date = earliest_date

    def prepend_data(self, data, date_column):
        prepend = pd.DataFrame([self.earliest_date], columns=[date_column])
        return pd.concat([
            prepend,
            data
        ])


    def get_group(self, value):
        return self.data[value], self.reference[value]

    def merge_asof(self, value, left_on, right_on):
        left_data, right_data = self.get_group(value)
        right_data = self.prepend_data(right_data, right_on)

        left_data.loc[:, left_on] = pd.to_datetime(left_data[left_on])
        right_data.loc[:, right_on] = pd.to_datetime(right_data[right_on])

        left_data = left_data.sort_values(left_on)
        right_data = right_data.sort_values(right_on)

        right_cols = [i for i in right_data.columns if i not in left_data.columns]
        if left_on == right_on:
            right_cols += [right_on]

        return pd.merge_asof(left_data, right_data[right_cols], left_on=left_on, right_on=right_on)

    def iterate_merge(self, left_on, right_on):
        progress_bar = ProgressBar(20, len(self.data.options))
        print("Merge progress:")
        for value in self.data.options:
            progress_bar.step()
            yield self.merge_asof(value, left_on, right_on)

    def main(self, left_on, right_on):
        values = self.iterate_merge(left_on, right_on)
        result = pd.concat(values)
        print("\nMerge Completed\n")
        return result
