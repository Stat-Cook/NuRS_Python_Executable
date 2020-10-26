import os

from utilities import *
from config import EXTRACT_PATH


if __name__ == '__main__':

    check_file_names("ESR_Mandatory_Training")

    path = os.path.join("Trust_data", "ESR_Mandatory_Training")

    comb = Combiner(path)
    result = comb.main(add_file_name_to_frame=True)
    result = result.reset_index(drop=True)

    to_file(result, EXTRACT_PATH, "ESR_Mandatory_Training_Combined.csv")
