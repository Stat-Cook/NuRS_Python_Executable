"""
Combine ESR Leavers data sets into a single file.
Steps:
1. Find files in Trust_data/ESR_Leavers
2. Calculate the Termination Year-Month
3. Group by Year-Month, Ward and Leaving Reason and calculate leavers frequency
4. Drop all columns except Organisation, Termination Month, Leaving Reason, Frequency.
5. Save to file Leavers_Monthly_Frequencies.csv
"""
import pandas as pd
import numpy as np

from .utilities import check_file_names, ScriptFactory
from .config import EXTRACT_PATH, ALLOCATE_WARD_COLUMN

FILE_NAME = "ESR_Leavers"


def monthly_frequency(data):
    """
    Reduce a data set to a frequency table.
    Parameters
    ----------
    data: pandas.DataFrame
        ESR Leavers data set.
    Returns
    -------
    pandas.DataFrame
    """
    grps = data.groupby([ALLOCATE_WARD_COLUMN, "Termination Month", "Leaving Reason"])
    result = pd.DataFrame(
        [np.concatenate((i, j.shape))[:-1] for i, j in grps]
    )
    result.columns = ["Organisation", "Termination Month", "Leaving Reason", "Count"]
    return result


tasks = {
    "Load data": dict(path="Trust_data", name="ESR_Leavers"),
    "To datetime": dict(columns=["Termination Date"]),
    "Manipulate column": dict(
        new_column="Termination Month",
        old_column="Termination Date",
        function=lambda x: "{}-{}".format(x.year, x.month)
    ),
    "Apply function": dict(function=monthly_frequency),
    "To file": dict(extract_path=EXTRACT_PATH, file_name="Leavers_Monthly_Frequencies")
}


if __name__ == '__main__':

    routine = ScriptFactory(EXTRACT_PATH, "ESR_Leavers", tasks)
    check_file_names("ESR_Leavers")
    routine.process_script()
