import os

from .utilities import *
from .config import EXTRACT_PATH


def check_file_exists(*path):
    file_path = os.path.join(*path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File {} not found".format(path[-1]))
    return 0


if __name__ == '__main__':


    tasks = {
        "Find files": dict(path="Trust_data", name="ESR_Sickness"),
        "Find more files": dict(
            path=("Trust_data", "Temporary_Files"),
            name="ESR_Demographics_Combined"
        ),
         "Merge as of": dict(
            left_on="Employee Number",
            right_on="Employee Number",
            left_date="Absence Start Date",
            right_date="Date_stamp"
        ),
        "Scramble in months": dict(aggregate_columns="Organisation"),
        "Remove PID": {},
        "To file": dict(
            extract_path=EXTRACT_PATH,
            file_name="ESR_Sickness_Demographics_Combined"
        )
    }
    routine = ScriptFactory(EXTRACT_PATH, "ESR_Sickness_Demographics_Combined", tasks)
    routine.process_script()
