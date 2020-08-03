@echo Off

if not exist "%CD%/NuRS_executable\Scripts\activate.bat" (
    install_venv
)
call check_python
call check_pandas
pause