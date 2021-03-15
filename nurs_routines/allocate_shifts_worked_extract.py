"""
Add ESR Demographics data to Allocate Shift Worked data sets into a single file.
Steps:
1. Find file Allocate_Shifts_Worked_Combined.csv
2. Find file ESR_Demographics_Combined.csv
3. Merge the files by Employee number looking backwards in date.
4. Scramble the data at Ward-Date-Shift level
5. Remove any PID.
6. Save to file Allocate_Shifts_Worked_Demographics_Combined.csv
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
