import os
from combiner import Combiner
from config import EXTRACT_PATH


if __name__ == '__main__':

    sickness_path = find_file("Trust_data", "ESR_Sickness")
    sickness = load_data(sickness_path)

    to_remove = [
        "Last Name", "Middle Name", "First Name",
        "Title", "Supervisor"
    ]
    to_remove = [i for i in to_remove if i in sickness.columns]
    result = sickness.drop(columns=to_remove)

    to_file = os.path.join(EXTRACT_PATH, "ESR_Sickness_processed.csv")
    result.to_csv(to_file, drop_index=True)