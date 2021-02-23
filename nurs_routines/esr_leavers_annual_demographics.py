"""
Combine ESR Leavers data sets into a single file.
Steps:
1. Find files in Trust_data/ESR_Leavers
2. Calculate the Termination Year (TODO: consider financial year not calendar year)
3. Remove PID
4. Scramble at Organization-Year level.
5. Save to file Leavers_Annual_Demographics.csv
"""
from .utilities import ScriptFactory, check_file_names
from .config import EXTRACT_PATH

tasks = {
    "Load data": dict(path="Trust_data", name="ESR_Leavers"),
    "To datetime": dict(columns=["Termination Date"]),
    "Manipulate column": dict(
        new_column="Termination Year",
        old_column="Termination Date",
        function=lambda x: x.year
    ),
    "Remove PID": {},
    "Scramble": dict(keys=["Organisation", "Termination Year"]),
    "To file": dict(extract_path=EXTRACT_PATH, file_name="Leavers_Annual_Demographics")
}

if __name__ == '__main__':

    check_file_names("ESR_Leavers")

    routine = ScriptFactory(EXTRACT_PATH, "ESR_Leavers", tasks)
    routine.process_script()
