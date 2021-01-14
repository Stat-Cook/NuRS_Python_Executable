"""
Combine Allocate Shifts Worked data sets into a single file.
NB: This data set contains PID to allow alignment at later stages.
Hence - this data set should not be removed from Trusts.
Steps:
1. Find files in Trust_data/Allocate_Shifts_Worked
2. Iterate through files opening and combining
3. Reindex the data frame
4. Save to Temporary_Files Allocate_Shifts_Worked_Combined.csv
"""
from .utilities import check_file_names, ScriptFactory
from .config import EXTRACT_PATH

# PID purposefully not removed for later alignment.
tasks = {
    "Join file names": dict(file="Allocate_Shifts_Worked"),
    "Combine datasets": {},
    "Reset index": {},
    "To file": dict(
        extract_path=("Trust_data", "Temporary_Files"),
        file_name="Allocate_Shifts_Worked_Combined"
    )
}

if __name__ == '__main__':

    check_file_names("Allocate_Shifts_Worked")

    routine = ScriptFactory(EXTRACT_PATH, "Allocate_Shifts_Worked_Combined", tasks)
    routine.process_script()
