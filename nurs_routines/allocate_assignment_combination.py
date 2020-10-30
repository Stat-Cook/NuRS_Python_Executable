import os
from utilities import *
from config import EXTRACT_PATH


FILE_NAME = "Allocate_Assignment_Combined"

if __name__ == '__main__':

    define_logger(EXTRACT_PATH, FILE_NAME)
    check_file_names("Allocate_Assignment")

    path = os.path.join("Trust_data", "Allocate_Assignment")

    comb = Combiner(path)
    result = comb.main()
    result = result.reset_index(drop=True)

    to_file(result, EXTRACT_PATH,  "Allocate_Assignment_Combined.csv")
    #
    # to_file = os.path.join(EXTRACT_PATH, "Allocate_Assignment_Combined.csv")
    # result.to_csv(to_file, index=False)
