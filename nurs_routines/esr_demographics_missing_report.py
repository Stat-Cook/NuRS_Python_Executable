"""
Check how much of the demographic data is missing.
Steps:
1. Load the ESR demographics data.
2. Check the average rate of NA values per column
3. Write results to file.
"""
from .utilities import ScriptFactory
from .config import EXTRACT_PATH


tasks = {
    "Load data": dict(name="ESR_Demographics_Combined",
                      path="Trust_data/Temporary_Files"),
    "Is NA": {},
    "To file": dict(extract_path=EXTRACT_PATH, file_name="ESR_Demographics_Missing",
                    index=True)
}

if __name__ == '__main__':

    routine = ScriptFactory(EXTRACT_PATH, "ESR_Demographics_Missing", tasks)
    routine.process_script()


