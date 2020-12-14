"""
Script to combine Allocate Shift Worked quarterly data sets into one file for export.
Allocate Shift Work data sets will sit in Trust_data/Allocate_Shifts_Worked.
The script finds all files in this directory and combines before exporting.
"""

import os
from utilities import *

from config import EXTRACT_PATH

FILE_NAME = "Allocate_Shifts_Worked_Combined"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_NAME)
    check_file_names("Allocate_Shifts_Worked")

    tasks = {
        "Join file names": None,
        "Combine data": None,
        "Main routine": None,
        "Reset index": None,
        "Remove PID": None,
        "To file": [("Trust_data", "Temporary_Files"), "Allocate_Shifts_Worked_Combined.csv"]
    }
    routine = ScriptFactory(EXTRACT_PATH, FILE_NAME, tasks)
    routine.process_script("Allocate_Shifts_Worked")
