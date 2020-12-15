from utilities import ScriptFactory, check_file_names
from config import EXTRACT_PATH

if __name__ == '__main__':

    check_file_names("ESR_Leavers")

    tasks = {
        "Load data": dict(path="Trust_data", name="ESR_Leavers"),
        "Manipulate column": dict(
            new_column="Termination Year",
            old_column="Termination Date",
            function=lambda x: x.year
        ),
        "Remove PID": {},
        "Scramble": dict(keys=["Organisation", "Termination Year"]),
        "To file": dict(extract_path=EXTRACT_PATH, file_name="Leavers_Annual_Demographics")
    }

    routine = ScriptFactory(EXTRACT_PATH, "ESR_Leavers", tasks)
    routine.process_script()
