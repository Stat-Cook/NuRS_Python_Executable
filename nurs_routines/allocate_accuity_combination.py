import os
from utilities import check_file_names, trust_data_path_join, \
    Combiner, main_routine, ScriptFactory

from config import EXTRACT_PATH

FILE_NAME = "Allocate_Accuity_Combined"

if __name__ == '__main__':

    check_file_names("Allocate_Accuity")
    tasks = {
        "Join file names": None,
        "Combine data": None,
        "Main routine": None,
        "Reset index": None,
        "Remove PID": None,
        "To file": [EXTRACT_PATH, FILE_NAME]
    }

    # tasks = [
    #     # Join file names
    #     trust_data_path_join,
    #     # Define combiner object
    #     trust_data_path_join,
    #     # Run main loop
    #     main_routine
    #     # Automatically saves to file
    # ]

    routine = ScriptFactory(EXTRACT_PATH, FILE_NAME, tasks)
    routine.process_script("Allocate_Accuity")
