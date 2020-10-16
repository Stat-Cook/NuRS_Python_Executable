import os
import re
import pandas as pd

from utilities import Combiner
from config import EXTRACT_PATH


def extract_date_function(file):
    pattern = re.compile(r" .*\.")
    m = pattern.search(file)
    return pd.to_datetime(m.group()[1:-1])


if __name__ == '__main__':

    path = os.path.join("Trust_data", "ESR_Demographics")

    comb = Combiner(path)

    result = comb.main(extract_date_function=extract_date_function)
    result = result.reset_index(drop=True)

    to_file = os.path.join("Trust_data", "Temporary_data", "ESR_Demographics_Combined.csv")
    result.to_csv(to_file)
