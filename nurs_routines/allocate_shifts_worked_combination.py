import os
from combiner import Combiner
from config import EXTRACT_PATH


if __name__ == '__main__':

    path = os.path.join("Trust_data", "Allocate_Shifts_Worked")

    comb = Combiner(path)
    result = comb.main().reset_index(drop=True)

    to_file = os.path.join("Trust_data", "Temporary_Files", "Allocate_Shifts_Worked_Combined.csv")
    result.to_csv(to_file, drop_index=True)
