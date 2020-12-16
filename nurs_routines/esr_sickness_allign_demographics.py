"""
Add ESR Demographics data to ESR Sickness data sets into a single file.
Steps:
1. Find file ESR_Sickness.csv
2. Find file ESR_Demographics_Combined.csv
3. Merge the files by Employee number looking backwards in date.
4. Scramble the data at Ward level
5. Remove any PID.
6. Save to file ESR_Sickness_Demographics_Combined.csv
"""
from .utilities import *
from .config import EXTRACT_PATH


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
