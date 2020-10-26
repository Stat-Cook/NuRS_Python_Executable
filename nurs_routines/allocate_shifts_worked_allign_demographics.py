import os
import time

from utilities import MergeAsOf, find_file, split_apply, shuffle, to_file, remove_pid, scramble
from config import EXTRACT_PATH



def check_file_exists(*path):
    file_path = os.path.join(*path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File {} not found".format(path[-1]))
    return 0


if __name__ == '__main__':

    t0 = time.time()
    # Find paths to files:
    temporary_files_path = os.path.join("Trust_data", "Temporary_Files")
    shifts_worked_path = find_file(temporary_files_path, "Allocate_Shifts_Worked_Combined")
    demographics_path = find_file(temporary_files_path, "ESR_Demographics_Combined")
    print("Load data time: {:0f}s".format(time.time() - t0))
    t0 = time.time()

    # Set up data and merge on 'Staff Number' to 'Employee Number' and
    # looking up last closest 'Date_stamp' to 'Duty Date'
    merger = MergeAsOf(shifts_worked_path, demographics_path, "Staff Number", "Employee Number")
    merged_data = merger.main("Duty Date", "Date_stamp")
    print("Merge data time: {:0f}s".format(time.time() - t0))
    t0 = time.time()

    # Extract columns from demographics dataset, adding in aggregate columns:
    demographic_columns = [i for i in merger.reference.columns if i in merged_data.columns]

    # Replace demographic columns with scrambled demographic columns.
    # Scrambling done at "Owning Unit", "Duty Date" aggregate
    # i.e. ward and day.
    merged_data = scramble(
        merged_data,
        ["Owning Unit", "Duty Date", "Shift"],
        demographic_columns
    )
    print("\nShuffling completed")
    print("Shuffling data time: {:0f}s".format(time.time() - t0))
    t0 = time.time()

    # Remove any direct PID that may not have been washed out sooner.
    result = remove_pid(merged_data)
    print("Remove PID time: {:0f}s".format(time.time() - t0))
    t0 = time.time()

    # Save to file:
    to_file(result, EXTRACT_PATH, "Allocate_Shifts_Worked_Demographics_Combined.csv")
    print("Export data time: {:0f}s".format(time.time() - t0))
    t0 = time.time()