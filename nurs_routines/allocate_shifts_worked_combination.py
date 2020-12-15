"""
Script to combine Allocate Shift Worked quarterly data sets into one file for export.
Allocate Shift Work data sets will sit in Trust_data/Allocate_Shifts_Worked.
The script finds all files in this directory and combines before exporting.
"""

from utilities import check_file_names, ScriptFactory
from config import EXTRACT_PATH


if __name__ == '__main__':

    check_file_names("Allocate_Shifts_Worked")
    # PID purposefully not removed for later allignment.
    tasks = {
        "Join file names": dict(file="Allocate_Shifts_Worked"),
        "Combine datasets": {},
        "Reset index": {},
        "To file": dict(
            extract_path=("Trust_data", "Temporary_Files"),
            file_name="Allocate_Shifts_Worked_Combined")
    }
    routine = ScriptFactory(EXTRACT_PATH, "Allocate_Shifts_Worked_Combined", tasks)
    routine.process_script()
