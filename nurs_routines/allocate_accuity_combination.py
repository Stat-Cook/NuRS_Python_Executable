import os
from combiner import Combiner
from config import EXTRACT_PATH


if __name__ == '__main__':

    path = os.path.join("Trust_data", "Allocate_Accuity")

    comb = Combiner(path)
    result = comb.main().reset_index(drop=True)

    to_file = os.path.join(EXTRACT_PATH, "Allocate_Accuity_Combined.csv")
    result.to_csv(to_file, drop_index=True)
