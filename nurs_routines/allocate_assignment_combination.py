"""
Combine Allocate Assignment data sets into a single file.
Steps:
1. Find files in Trust_data/Allocate_Assignment
2. Iterate through files opening and combining
3. Reindex the data frame
4. Remove any PID.
5. Save to file
"""
from .utilities import ScriptFactory, check_file_names
from .config import EXTRACT_PATH


if __name__ == '__main__':

    check_file_names("Allocate_Assignment")

    tasks = {
        "Join file names": dict(file="Allocate_Assignment"),
        "Combine datasets": {},
        "Reset index": {},
        "Remove PID": {},
        "To file": dict(extract_path=EXTRACT_PATH, file_name="Allocate_Assignment_Combined")
    }

    routine = ScriptFactory(EXTRACT_PATH, "Allocate_Assignment_Combined", tasks)
    routine.process_script()
