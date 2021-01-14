"""
Combine ESR Sickness data sets into a single file.
Steps:
1. Find files in Trust_data/ESR_Sickness
2. Iterate through files opening and combining
3. Reindex the data frame
4. Save to file Temporary_Files/ESR_Sickness_processed.csv
"""
from .utilities import ScriptFactory, check_file_names
from .config import EXTRACT_PATH

tasks = {
    "Join file names": dict(file="ESR_Sickness"),
    "Combine datasets": {},
    "Reset index": {},
    "To file": dict(extract_path="Trust_data/Temporary_Files", file_name="ESR_Sickness_Combined")
}

if __name__ == '__main__':

    routine = ScriptFactory(EXTRACT_PATH, "Allocate_Assignment_Combined", tasks)
    routine.process_script()
