import os
import sys
from utilities import *
import logging

from config import EXTRACT_PATH

FILE_NAME = "Allocate_Accuity_Combined"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_NAME)
    check_file_names("Allocate_Accuity")

    path = os.path.join("Trust_data", "Allocate_Accuity")

    comb = Combiner(path)
    result = comb.main()
    result = result.reset_index(drop=True)

    to_file(result, EXTRACT_PATH, FILE_NAME + ".csv")
