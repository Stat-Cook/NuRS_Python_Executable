import os
import time

from utilities import *
from config import EXTRACT_PATH



def check_file_exists(*path):
    file_path = os.path.join(*path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File {} not found".format(path[-1]))
    return 0

FILE_PATH = "Allocate_Shifts_Worked_Demographics_Combined"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_PATH)

    # Find paths to files:
    temporary_files_path = os.path.join("Trust_data", "Temporary_Files")
    shifts_worked_path = find_file(temporary_files_path, "Allocate_Shifts_Worked_Combined")
    demographics_path = find_file(temporary_files_path, "ESR_Demographics_Combined")

    # Set up data and merge on 'Staff Number' to 'Employee Number' and
    # looking up last closest 'Date_stamp' to 'Duty Date'
    merger = MergeAsOf(shifts_worked_path, demographics_path, "Staff Number", "Employee Number")
    merged_data = merger.main("Duty Date", "Date_stamp")

    # Extract columns from demographics dataset, adding in aggregate columns:
    demographic_columns = [i for i in merger.reference.columns if i in merged_data.columns]

    # sub set for development:
    # import datetime
    # merged_data = merged_data[merged_data["Duty Date"] > datetime.datetime(2020, 1, 1)]

    # Replace demographic columns with scrambled demographic columns.
    # Scrambling done at "Owning Unit", "Duty Date" aggregate
    # i.e. ward and day.

    t0 = time.time()
    scramble_to_file(
        merged_data,
        ["Owning Unit", "Duty Date", "Shift"],
        demographic_columns,
        "Trust_data/Temporary_Files/Temporary_Shift_Demographics.csv"
    )

    print(time.time() - t0)
    print("\nShuffling completed")

    # Remove any direct PID that may not have been washed out sooner.
    result = remove_pid(merged_data)

    # Save to file:
    to_file(result, EXTRACT_PATH, "Allocate_Shifts_Worked_Demographics_Combined.csv")
