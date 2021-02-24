"""
Combine ESR Mandatory Training data sets into a single file.
Steps:
1. Find files in Trust_data/ESR_Mandatory_Training
2. Iterate through files opening and combining
3. Reindex the data frame
4. Remove any PID.
5. Save to file ESR_Mandatory_Training.csv
"""
from .utilities import ScriptFactory, check_file_names
from .config import EXTRACT_PATH


tasks = {
    "Join file names": dict(file="ESR_Mandatory_Training"),
    "Combine datasets": {},
    "Reset index": {},
    "Remove PID": {},
    "To file": dict(extract_path=EXTRACT_PATH, file_name="ESR_Mandatory_Training")
}

if __name__ == '__main__':

    routine = ScriptFactory(EXTRACT_PATH, "ESR_Mandatory_Training", tasks)
    check_file_names("ESR_Mandatory_Training")
    routine.process_script()
