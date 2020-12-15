
import re
import pandas as pd

from utilities import *
from config import EXTRACT_PATH


def extract_date_function(file):
    pattern = re.compile(r"(\d+)")
    m = pattern.search(file)
    if m:
        date = pd.to_datetime(m.group(), yearfirst=True)
        if (date.year < 2025) and (date.year > 2000):
            return date
        else:
            return pd.to_datetime(m.group(), yearfirst=False)

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
