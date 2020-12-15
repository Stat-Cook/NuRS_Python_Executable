@echo off

call NuRS_executable\Scripts\activate

:: Combine temporary files
call python nurs_routines/allocate_shifts_worked_combination.py
call python nurs_routines/demographics_combination.py
call python nurs_routines/esr_sickness_extract.py

:: Allign demographics and remove PID
call python nurs_routines/allocate_shifts_worked_allign_demographics.py
call python nurs_routines/esr_sickness_allign_demographics.py

pause