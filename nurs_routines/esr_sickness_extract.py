"""
Process ESR Sickness data sets to remove PID.
Steps:
1. Find files in Trust_data/ESR_Mandatory_Training
2. Open and remove any PID.
3. Save to file ESR_Sickness_processed.csv
"""
from .utilities import *
from .config import EXTRACT_PATH


if __name__ == '__main__':

    check_file_names("ESR_Sickness")
    tasks = {
        "Load data": dict(path="Trust_data", name="ESR_Sickness"),
        "Remove PID": dict(
            extra_remove=["Last Name", "Middle Name", "First Name", "Title", "Supervisor"]
        ),
        "To file": dict(extract_path=EXTRACT_PATH, file_name="ESR_Sickness_processed")
    }
    routine = ScriptFactory(EXTRACT_PATH, "ESR_Sickness", tasks)
    routine.process_script()
