"""

"""
from utilities import check_file_names, ScriptFactory
from config import EXTRACT_PATH


if __name__ == '__main__':

    check_file_names("Allocate_Accuity")

    tasks = {
        "Join file names": dict(file="Allocate_Accuity"),
        "Combine datasets": {},
        "Reset index": {},
        "Remove PID": {},
        "To file": dict(extract_path=EXTRACT_PATH, file_name="Allocate_Accuity_Combined")
    }

    routine = ScriptFactory(EXTRACT_PATH, "Allocate_Accuity_Combined", tasks)
    routine.process_script()
