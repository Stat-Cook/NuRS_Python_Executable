import os

from utilities import Combiner
from config import EXTRACT_PATH


if __name__ == '__main__':

    path = os.path.join("Trust_data", "ESR_Mandatory_Training")

    comb = Combiner(path)
    result = comb.main(add_file_name_to_frame=True)
    result = result.reset_index(drop=True)

    to_file = os.path.join(EXTRACT_PATH, "ESR_Mandatory_Training_Combined.csv")
    result.to_csv(to_file, drop_index=True)
