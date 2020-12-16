"""
Combine Allocate Acuity data sets into a single file.
Steps:
1. Find files in Trust_data/Allocate_Acuity
2. Iterate through files opening and combining
3. Reindex the data frame
4. Remove any PID.
5. Save to file Allocate_Acuity_Combined.csv
"""
from .utilities import check_file_names, ScriptFactory
from .config import EXTRACT_PATH


def main():
    """
    Main routine for combining Allocate Acuity data sets.
    Returns
    -------
    (pandas.DataFrame, [processed steps])
    """
    check_file_names("Allocate_Acuity")

    tasks = {
        "Join file names": dict(file="Allocate_Acuity"),
        "Combine datasets": {},
        "Reset index": {},
        "Remove PID": {},
        "To file": dict(extract_path=EXTRACT_PATH, file_name="Allocate_Acuity_Combined")
    }

    routine = ScriptFactory(EXTRACT_PATH, "Allocate_Acuity_Combined", tasks)
    return routine.process_script()


if __name__ == '__main__':

    main()
