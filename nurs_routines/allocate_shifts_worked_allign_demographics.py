import os

from utilities import MergeAsOf, find_file, split_apply, shuffle
from config import EXTRACT_PATH


if __name__ == '__main__':

    # Find paths to files:
    shifts_worked_path = find_file("Trust_data", "Temporary_data", "Allocate_Shifts_Worked_Combined")
    demographics_path = find_file("Trust_data", "Temporary_data", "ESR_Demographics_Combined")

    # Set up data and merge on 'Staff Number' to 'Employee Number' and
    # looking up last closest 'Date_stamp' to 'Duty Date'
    merger = MergeAsOf(shifts_worked_path, demographics_path, "Staff Number", "Employee Number")
    merged_data = merger.main("Duty Date", "Date_stamp")

    # Extract columns from demographics dataset, adding in aggregate columns:
    demographic_columns = [i for i in merger.reference.columns if i in merged_data.columns]
    demographic_columns += ["Owning Unit", "Duty Date"]

    # Replace demographic columns with scrambled demographic columns.
    # Scrambling done at "Owning Unit", "Duty Date" aggregate
    # i.e. ward and day.
    merged_data[demographic_columns] = split_apply(
        merged_data[demographic_columns],
        ["Owning Unit", "Duty Date"],
        shuffle
    )

    # Remove any direct PID that may not have been washed out sooner.
    to_remove = [
        "Employee Number", "Last Name", "First Name", "Title"
        "Assignment Number",  "Person", "Staff Number"
    ]
    to_remove = [i for i in to_remove if i in merged_data.columns]
    result = merged_data.drop(columns=to_remove)

    to_file = os.path.join(EXTRACT_PATH, "Shifts_Worked_Demographics_Combined.csv")
    result.to_csv(to_file)
