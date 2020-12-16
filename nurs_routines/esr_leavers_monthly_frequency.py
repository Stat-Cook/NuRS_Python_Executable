import pandas as pd
import numpy as np

from .utilities import check_file_names, ScriptFactory
from .config import EXTRACT_PATH

FILE_NAME = "ESR_Leavers"


def monthly_frequency(data):
    grps = data.groupby(["Organisation", "Termination Month",  "Leaving Reason"])
    result = pd.DataFrame(
        [np.concatenate((i, j.shape))[:-1] for i, j in grps]
    )
    result.columns = ["Organisation", "Termination Month",  "Leaving Reason", "Count"]
    return result


if __name__ == '__main__':

    check_file_names("ESR_Leavers")

    tasks = {
        "Load data": dict(path="Trust_data", name="ESR_Leavers"),
        "Manipulate column": dict(
            new_column="Termination Month",
            old_column="Termination Date",
            function=lambda x: "{}-{}".format(x.year, x.month)
        ),
        "Apply function": dict(function=monthly_frequency),
        "To file": dict(extract_path=EXTRACT_PATH, file_name="Leavers_Monthly_Frequencies")
    }

    routine = ScriptFactory(EXTRACT_PATH, "ESR_Leavers", tasks)
    routine.process_script()
