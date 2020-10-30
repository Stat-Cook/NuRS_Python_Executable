import os
from utilities import *
from config import EXTRACT_PATH

FILE_NAME = "ESR_Sickness"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_NAME)
    check_file_names("ESR_Sickness")

    sickness_path = find_file("Trust_data", "ESR_Sickness")
    sickness = load_data(sickness_path)
    to_remove = [
        "Last Name", "Middle Name", "First Name",
        "Title", "Supervisor"
    ]

    result = remove_pid(sickness, to_remove)

    to_file(result, EXTRACT_PATH, "ESR_Sickness_processed.csv")
