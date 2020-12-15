from utilities import ScriptFactory, check_file_names
from config import EXTRACT_PATH


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
