from utilities import *
from config import EXTRACT_PATH

if __name__ == '__main__':

    check_file_names("ESR_Leavers")

    leavers_path = find_file("Trust_data", "ESR_Leavers")
    leavers = load_data(leavers_path)
    leavers["Termination Year"] = leavers["Termination Date"].apply(lambda x: x.year)

    data = remove_pid(leavers)

    result = split_apply(data, ["Organisation", "Termination Year"], shuffle)
    to_file(result, EXTRACT_PATH, "Leavers_Annual_Demographics.csv")
