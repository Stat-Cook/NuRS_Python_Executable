"""
Combine Allocate Shifts Worked data sets into a single file.
NB: This data set contains PID to allow alignment at later stages.
Hence - this data set should not be removed from Trusts.
Steps:
1. Find files in Trust_data/ESR_Demographics
2. Iterate through files opening and combine - adding date from file name into the frame.
3. Reindex the data frame
4. Save to Temporary_Files ESR_Demographics_Combined.csv
"""
import re
import pandas as pd

from .utilities import ScriptFactory, check_file_names
from .config import EXTRACT_PATH


def extract_date_function(file: str):
    """
    Extract the date time from file name string.
    Parameters
    ----------
    file: str
        The file name being processed
    Returns
    -------
    pd.datetime
    """
    pattern = re.compile(r"(\d+)")
    match = pattern.search(file)
    if match:
        date = pd.to_datetime(match.group(), yearfirst=True)
        if (date.year < 2025) and (date.year > 2000):
            return date

        return pd.to_datetime(match.group(), yearfirst=False)

    raise AttributeError("Date string not found in file name")


if __name__ == '__main__':

    check_file_names("ESR_Demographics")
    # NB: PID removal purposely not included.  Data set is not for export outside the Trust.
    tasks = {
        "Join file names": dict(file="ESR_Demographics"),
        "Combine datasets": dict(extract_date_function=extract_date_function),
        "Reset index": {},
        "To file": dict(
            extract_path=("Trust_data", "Temporary_Files"),
            file_name="ESR_Demographics_Combined"
        )
    }
    routine = ScriptFactory(EXTRACT_PATH, "ESR_Demographics", tasks)
    routine.process_script()
