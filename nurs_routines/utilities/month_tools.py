import pandas as pd
from .utilities import shuffle

from .file_structure import START, END


class GetMonth:

    def __init__(self, start=START, end=END):
        self.start = start
        self.end = end

    @property
    def months(self):
        return pd.date_range(self.start, self.end, freq="MS")

    @property
    def current_months(self):
        return self.months[:-1]

    @property
    def next_month(self):
        return self.months[1:]

    def yield_data(self, data, start_column="Absence Start Date", end_column="Absence End Date"):
        z = zip(self.current_months, self.next_month)

        for start_of_month, end_of_month in z:
            month = data[
                (data[start_column] < end_of_month) &
                (data[end_column] >= start_of_month)
            ]
            month["Month"] = start_of_month
            yield month

    def monthly_shuffle(self, data, columns_to_shuffle,
                        start_column="Absence Start Date", end_column="Absence End Date"):
        monthly_data = self.yield_data(data, start_column, end_column)
        for month in monthly_data:
            try:
                month[columns_to_shuffle] = shuffle(month[columns_to_shuffle], True)
            except:
                print(month["Month"].unique())
            yield month

    def shuffle_and_join(self, data, columns_to_shuffle,
                        start_column="Absence Start Date", end_column="Absence End Date"):
        monthly_data = self.monthly_shuffle(data, columns_to_shuffle, start_column, end_column)
        return pd.concat(monthly_data)
