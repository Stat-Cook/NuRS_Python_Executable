"""
Extract Allocate Shift Worked data without PID into a single file:
Steps:
1. Find file Allocate_Shifts_Worked_Combined.csv
2. Remove any PID.
3. Save to file Allocate_Shifts_Worked.csv

"""
from .utilities import ScriptFactory
from .config import EXTRACT_PATH

tasks = {
    # "Find files": dict(
    #    path=("Trust_data", "Temporary_Files"),
    #    name="Allocate_Shifts_Worked_Combined"
    # ),
    "Load data": dict(name="Allocate_Shifts_Worked_Combined",
                      path="Trust_data/Temporary_Files"),
    "Remove PID": {},
    "To file": dict(
        extract_path=EXTRACT_PATH,
        file_name="Allocate_Shifts_Worked"
    )
}

if __name__ == '__main__':
    routine = ScriptFactory(
        EXTRACT_PATH, "Allocate_Shifts_Worked_Extract", tasks
    )
    routine.process_script()
