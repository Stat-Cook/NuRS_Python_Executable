import os
from utilities import *
from config import EXTRACT_PATH


if __name__ == '__main__':

    check_file_names("Allocate_Accuity")

    path = os.path.join("Trust_data", "Allocate_Accuity")

    comb = Combiner(path)
    result = comb.main()
    result = result.reset_index(drop=True)

    to_file(result, EXTRACT_PATH, "Allocate_Accuity_Combined.csv")
