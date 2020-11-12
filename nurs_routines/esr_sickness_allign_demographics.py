import os
import time
import pandas as pd

from utilities import *
from config import EXTRACT_PATH


def check_file_exists(*path):
    file_path = os.path.join(*path)
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File {} not found".format(path[-1]))
    return 0


if __name__ == '__main__':

    # Find paths to files:
    temporary_files_path = os.path.join("Trust_data", "Temporary_Files")
    sickness_path = find_file("Trust_data", "ESR_Sickness")
    demographics_path = find_file(temporary_files_path, "ESR_Demographics_Combined")

    # Set up data and merge on 'Staff Number' to 'Employee Number' and
    # looking up last closest 'Date_stamp' to 'Duty Date'
    merger = MergeAsOf(sickness_path, demographics_path, "Employee Number", "Employee Number")
    merged_data = merger.main("Absence Start Date", "Date_stamp")

    # Extract columns from demographics dataset, adding in aggregate columns:
    demographic_columns = [i for i in merger.reference.columns if i in merged_data.columns]

    # Replace demographic columns with scrambled demographic columns.
    # Scrambling done at "Owning Unit", Month aggregate

    month_shuffler = GetMonth()
    # grps = merged_data.grouped_monthly_shuffle("Organisation")
    # _iter = (month_shuffler.shuffle_and_join(df, demographic_columns) for _, df in grps)
    # merged_data = month_shuffler.shuffle_and_join(merged_data, demographic_columns)
    # merged_data = pd.concat(_iter)
    merged_data = month_shuffler.grouped_monthly_shuffle(merged_data, "Organisation", demographic_columns)

    print("\nShuffling completed")
#     print("Shuffling data time: {:0f}s".format(time.time() - t0))
    t0 = time.time()

    # Remove any direct PID that may not have been washed out sooner.
    result = remove_pid(merged_data)

    to_file(result, EXTRACT_PATH, "ESR_Sickness_Demographics_Combined.csv")

    # to_file = os.path.join(EXTRACT_PATH, "Allocate_Accuity_Combined.csv")
    # result.to_csv(to_file, index=False)
