import os
import re
import pandas as pd

from utilities import *


def extract_date_function(file):
    pattern = re.compile(r" .*\.")
    m = pattern.search(file)
    return pd.to_datetime(m.group()[1:-1], yearfirst=True)


if __name__ == '__main__':

    check_file_names("ESR_Demographics")

    path = os.path.join("Trust_data", "ESR_Demographics")

    comb = Combiner(path)
    result = comb.main(extract_date_function=extract_date_function)
    result = result.reset_index(drop=True)

    temporary_file_path = os.path.join("Trust_data", "Temporary_Files")
    to_file(result, temporary_file_path, "ESR_Demographics_Combined.csv")
