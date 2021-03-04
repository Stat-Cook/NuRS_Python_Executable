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
    )
}

if __name__ == '__main__':

    routine = ScriptFactory(EXTRACT_PATH, "end_to_end", tasks)
    result = routine.process_script()
    export_path = os.path.join(
        "integration_tests", "test_data", "merged.csv"
    )
    result[0][0].to_csv(export_path)
