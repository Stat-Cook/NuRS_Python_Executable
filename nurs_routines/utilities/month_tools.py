"""
Tools for shuffling a time interval data set,
i.e. where we know the start and end times and wish to know which months it contains.
"""
import logging
import pandas as pd

from .utilities import shuffle
from .progress_bar import ProgressBar
from .file_structure import START, END


class GetMonth:
    """
    Iterate through a data set from 'start' to 'end' by month,
    extracting values that overlap that time, and shuffle values.
    Parameters
    ----------
    start: datetime.datetime
        date stamp to start from
    end: datetime.datetime
        date time to end at.
    """
    def __init__(self, start=START, end=END):
        self.start = start
        self.end = end

    @property
    def months(self):
        """Month start date(s) between 'start' and 'end'"""
        return pd.date_range(self.start, self.end, freq="MS")

    @property
    def current_months(self):
        """Start of monthly periods"""
        return self.months[:-1]

    @property
    def next_month(self):
        """End of monthly periods"""
        return self.months[1:]

    def yield_data(self, data, start_column="Absence Start Date", end_column="Absence End Date"):
        """
        Iterate through data, looking up months bound by start_column and end_column.
        Parameters
        ----------
        data: pandas.DataFrame
            frame to look up in
        start_column: str
            the column of data that serves as month start
        end_column: str
            the column of data the serves as month end
        """
        zipped_months = zip(self.current_months, self.next_month)

        for start_of_month, end_of_month in zipped_months:
            month = data[
                (data[start_column] < end_of_month) &
                (data[end_column] >= start_of_month)
            ]
            month["Month"] = start_of_month
            yield start_of_month, month

    def monthly_shuffle(self, data, columns_to_shuffle,
                        start_column="Absence Start Date", end_column="Absence End Date"):
        """
        Take a data set, extract a month, and shuffle.
        Parameters
        ----------
        data: pandas.DataFrame
            the data set to monthly shuffle
        columns_to_shuffle: str
            the column of 'data' to shuffle
        start_column: str
            the column to treat as month start
        end_column: str
            the column to treat as month end
        """
        monthly_data = self.yield_data(data, start_column, end_column)
        for start_of_month, month in monthly_data:
            month[columns_to_shuffle] = shuffle(
                frm=month[columns_to_shuffle],
                size_check=True,
                name=start_of_month
            )

            yield month

    def shuffle_and_join(self, data, columns_to_shuffle,
                         start_column="Absence Start Date", end_column="Absence End Date"
                         ):
        """
        Iterate through each month, extract monthly data, shuffle and join into a data frame.
        Parameters
        ----------
        data: pandas.DataFrame
            the data set to monthly shuffle
        columns_to_shuffle: str
            the column of 'data' to shuffle
        start_column: str
            the column to treat as month start
        end_column: str
            the column to treat as month end

        Returns
        -------
        pandas.DataFrame
        """
        monthly_data = self.monthly_shuffle(data, columns_to_shuffle, start_column, end_column)
        return pd.concat(monthly_data)


    def grouped_monthly_shuffle(self,
                                data, groupby, columns_to_shuffle,
                                date_columns=None
                                ):
        """
        Carry out the monthly extract-shuffle with an aggregated DataFrame.
        Does the shuffle for each aggregate independently.
        Parameters
        ----------
        data: pandas.DataFrame
            the data set to monthly shuffle
        groupby: str or list
            the column(s) to aggregate on to shuffle
        columns_to_shuffle: str
            the column of 'data' to shuffle
        date_columns: tuple(str)
            the columns to treat as month start and month end
        Returns
        -------
        pandas.DataFrame
        """
        start_column, end_column = date_columns or ["Absence Start Date", "Absence End Date"]
        grps = data.groupby(groupby)
        _iter = self.progres_bar_iteration(
            grps, columns_to_shuffle,
            start_column, end_column
        )
        return pd.concat(_iter)


    def progres_bar_iteration(self,
                              groups, columns_to_shuffle,
                              start_column="Absence Start Date", end_column="Absence End Date"
                              ):
        """
        Iterate through a grouped DataFrame - doing a monthly shuffle on set columns
        with a progress bar to track where the process is.
        Parameters
        ----------
        groups: pandas.GroupedDataFrame
            a grouped pandas DataFrame
        columns_to_shuffle: str
            the column of 'data' to shuffle
        start_column: str
            the column to treat as month start
        end_column: str
            the column to treat as month end
        """
        progress = ProgressBar(20, len(groups.groups))

        logging.info("Shuffle in progress:")
        for _, frame in groups:
            progress.step()
            yield self.shuffle_and_join(frame, columns_to_shuffle, start_column, end_column)
