import os
import re
import pandas as pd

from utilities import *


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


FILE_NAME = "ESR_Demographics"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_NAME)
    check_file_names("ESR_Demographics")

    path = os.path.join("Trust_data", "ESR_Demographics")

    comb = Combiner(path)
    result = comb.main(extract_date_function=extract_date_function)
    result = result.reset_index(drop=True)

    temporary_file_path = os.path.join("Trust_data", "Temporary_Files")
    to_file(result, temporary_file_path, "ESR_Demographics_Combined.csv")
