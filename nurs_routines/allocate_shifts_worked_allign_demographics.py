import os

from utilities import ScriptFactory, check_file_names
from config import EXTRACT_PATH


def check_file_exists(*path):
    file_path = os.path.join(*path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File {} not found".format(path[-1]))
    return 0

#TODO: filter out null keys from ESR_Demographics.
if __name__ == '__main__':

    tasks = {
        "Find files": dict(
            path=("Trust_data", "Temporary_Files"),
            name="Allocate_Shifts_Worked_Combined"
        ),
        "Find more files": dict(
            path=("Trust_data", "Temporary_Files"),
            name="ESR_Demographics_Combined"
        ),
        "Merge as of": dict(
            left_on="Staff Number",
            right_on="Employee Number",
            left_date="Duty Date",
            right_date="Date_stamp"
        ),
        "Scramble as of": dict(
            aggregate_columns=["Owning Unit", "Duty Date", "Shift"],
            file_path="Trust_data/Temporary_Files/Temporary_Shift_Demographics.csv"
        ),
        "Remove PID": {},
        "To file": dict(
            extract_path=EXTRACT_PATH,
            file_name="Allocate_Shifts_Worked_Demographics_Combined"
        )
    }

    routine = ScriptFactory(
        EXTRACT_PATH, "Allocate_Shifts_Worked_Demographics_Combined", tasks
    )
    routine.process_script()
