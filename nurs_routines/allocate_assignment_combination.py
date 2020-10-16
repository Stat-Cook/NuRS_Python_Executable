import os
from utilities import Combiner
from config import EXTRACT_PATH


if __name__ == '__main__':

    path = os.path.join("Trust_data", "Allocate_Assignment")

    comb = Combiner(path)
    result = comb.main().reset_index(drop=True)

    to_file = os.path.join(EXTRACT_PATH, "Allocate_Assignment_Combined.csv")
    result.to_csv(to_file)
