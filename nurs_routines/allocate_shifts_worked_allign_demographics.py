"""
Add ESR Demographics data to Allocate Shift Worked data sets into a single file.
Steps:
1. Find file Allocate_Shifts_Worked_Combined.csv
2. Find file ESR_Demographics_Combined.csv
3. Merge the files by Employee number looking backwards in date.
4. Scramble the data at Ward-Date-Shift level
5. Remove any PID.
6. Save to file Allocate_Shifts_Worked_Demographics_Combined.csv
"""
from .utilities import ScriptFactory
from .config import EXTRACT_PATH

tasks = {
    "Find files": dict(
        path=("Trust_data", "Temporary_Files"),
        name="Allocate_Shifts_Worked_Combined"
    ),
    "Find more files": dict(
        path=("Trust_data", "Temporary_Files"),
        name="ESR_Demographics_Combined"
    ),
    "Merge as of": dict(
        left_on="Staff Number",
        right_on="Employee Number",
        left_date="Duty Date",
        right_date="Date_stamp",
        report_path="Trust_data/Temporary_Files/Shifts_Demographics_report.txt",
        no_pid_report_path="Extract_data/Shifts_Demographics_report_short.txt",
        dtypes={"Staff Number": str, "Employee Number": str}
    ),
    "Scramble as of": dict(
        aggregate_columns=["Owning Unit", "Duty Date", "Shift Type"],
        file_path="Trust_data/Temporary_Files/Temporary_Shift_Demographics.csv"
    ),
    "Remove PID": {},
    "To file by year": dict(
        extract_path=EXTRACT_PATH,
        date_column="Duty Date",
        file_name_function=lambda x: f"Allocate_Shifts_Worked_Demographics_Combined_{x}"
    )
}

if __name__ == '__main__':

    routine = ScriptFactory(
        EXTRACT_PATH, "Allocate_Shifts_Worked_Demographics_Combined", tasks
    )
    routine.process_script()
