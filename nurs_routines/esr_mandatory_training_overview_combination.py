"""

"""
from .utilities import ScriptFactory, check_file_names
from .config import EXTRACT_PATH

if __name__ == '__main__':

    check_file_names("ESR_Mandatory_Training")

    tasks = {
        "Join file names": dict(file="ESR_Mandatory_Training"),
        "Combine datasets": {},
        "Reset index": {},
        "Remove PID": {},
        "To file": dict(extract_path=EXTRACT_PATH, file_name="ESR_Mandatory_Training")
    }

    routine = ScriptFactory(EXTRACT_PATH, "ESR_Mandatory_Training", tasks)
    routine.process_script()
