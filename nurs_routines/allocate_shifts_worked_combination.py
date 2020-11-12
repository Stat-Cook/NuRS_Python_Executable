import os
from utilities import *


FILE_NAME = "Allocate_Shifts_Worked_Combined"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_NAME)
    check_file_names("Allocate_Shifts_Worked")

    path = os.path.join("Trust_data", "Allocate_Shifts_Worked")

    comb = Combiner(path)
    result = comb.main().reset_index(drop=True)

    temporary_files = os.path.join("Trust_data", "Temporary_Files")
    to_file(result, temporary_files, "Allocate_Shifts_Worked_Combined.csv")
