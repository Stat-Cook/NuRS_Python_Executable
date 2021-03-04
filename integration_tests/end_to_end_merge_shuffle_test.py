"""

"""
import os

from nurs_routines.utilities import ScriptFactory, check_file_names
from nurs_routines.config import EXTRACT_PATH

tasks = {
    "Find files": dict(
        path=("integration_tests", "test_data"),
        name="data"
    ),
    "Find more files": dict(
        path=("integration_tests",  "test_data"),
        name="reference"
    ),
    "Merge as of": dict(
        left_on="ID",
        right_on="ID",
        left_date="dates",
        right_date="dates"
    ),
    "Scramble as of": dict(
        aggregate_columns=["Ward", "dates"],
        file_path="Trust_data/Temporary_Files/end_to_end_temp.csv"
    ),
    "Remove PID": dict(
        extra_remove=["ID"]
    ),
    "To file": dict(
        extract_path=os.path.join("integration_tests", "test_data"),
        file_name="shuffled"
    )
}

if __name__ == '__main__':

    routine = ScriptFactory(EXTRACT_PATH, "end_to_end", tasks)
    result = routine.process_script()
