import pandas as pd
import numpy as np
import os

from utilities import find_file, load_data
from config import EXTRACT_PATH

if __name__ == '__main__':

    leavers_path = find_file("Trust_data", "ESR_Leavers")
    leavers = load_data(leavers_path)

    leavers["Termination Month"] = leavers["Termination Date"].apply(lambda x: "{}-{}".format(x.year, x.month))
    grps = leavers.groupby(["Organisation", "Termination Month",  "Leaving Reason"])

    result = pd.DataFrame(
        [np.concatenate((i, j.shape))[:-1] for i, j in grps]
    )
    result.columns = ["Organisation","Termination Month",  "Leaving Reason", "Count"]

    to_file = os.path.join(EXTRACT_PATH, "Leavers_Monthly_Frequencies.csv")
    result.to_csv(to_file)
