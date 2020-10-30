import pandas as pd
import numpy as np
import logging

from utilities import *
from config import EXTRACT_PATH

FILE_NAME = "ESR_Leavers"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_NAME)
    check_file_names("ESR_Leavers")

    leavers_path = find_file("Trust_data", "ESR_Leavers")
    leavers = load_data(leavers_path)

    leavers["Termination Month"] = leavers["Termination Date"].apply(lambda x: "{}-{}".format(x.year, x.month))
    grps = leavers.groupby(["Organisation", "Termination Month",  "Leaving Reason"])

    result = pd.DataFrame(
        [np.concatenate((i, j.shape))[:-1] for i, j in grps]
    )
    result.columns = ["Organisation", "Termination Month",  "Leaving Reason", "Count"]

    to_file(result, EXTRACT_PATH, "Leavers_Monthly_Frequencies.csv")

