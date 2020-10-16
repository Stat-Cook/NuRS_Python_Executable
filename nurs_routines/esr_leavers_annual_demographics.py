import pandas as pd
import os

from utilities import find_file, load_data, shuffle, split_apply
from config import EXTRACT_PATH

if __name__ == '__main__':

    leavers_path = find_file("Trust_data", "ESR_Leavers")
    leavers = load_data(leavers_path)
    leavers["Termination Year"] = leavers["Termination Date"].apply(lambda x: x.year)

    to_remove = [
        "Last Name", "Middle Name", "First Name", "Title",
        "NI Number", "Email Address", "Address Line 1", "Address Line 2", "Address Line 3",
        "Town or City", "County", "Postal Code", "Home Phone", "Mobile Phone",
        "Personal Email Address"
    ]

    data = leavers.drop(columns=to_remove)

    # data = leavers[['Organisation', "Termination Year", 'Length of Service (Years)',
    #    'Staff Group', 'Job Role', 'Religious Belief', 'Sexual Orientation',
    #    'Ethnic Origin', 'Marital Status', 'Nationality',
    #    'Age Band', 'Gender', 'Disability']]

    result = split_apply(data, ["Organisation", "Termination Year"], shuffle)

    to_file = os.path.join(EXTRACT_PATH, "Leavers_Annual_Demographics.csv")
    result.to_csv(to_file)
