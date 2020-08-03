@echo off

if exist "%CD%/NuRS_executable\Scripts\activate.bat" (
    rem file exists
    echo Virtual environment found
    :: Activate virtual environment
    NuRS_executable\Scripts\activate
    :: Run main script
    python src/check_pandas.py
) else (
    rem file doesn't exist
    echo File Missing. Run install_venv.bat
)

pause