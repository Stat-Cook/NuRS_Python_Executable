import os
from utilities import *


if __name__ == '__main__':

    check_file_names("Allocate_Shifts_Worked")

    path = os.path.join("Trust_data", "Allocate_Shifts_Worked")

    comb = Combiner(path)
    result = comb.main().reset_index(drop=True)

    temporary_files = os.path.join("Trust_data", "Temporary_Files")
    to_file(result, temporary_files, "Allocate_Shifts_Worked_Combined.csv")

    # to_file = os.path.join("Trust_data", "Temporary_Files", "Allocate_Shifts_Worked_Combined.csv")
    # result.to_csv(to_file, index=False)
