@echo off

call NuRS_executable\Scripts\activate

:: Combine temporary files
call python -m nurs_routines.allocate_shifts_worked_combination
call python -m nurs_routines.demographics_combination
call python -m nurs_routines.esr_sickness_extract

:: Allign demographics and remove PID
call python -m nurs_routines.allocate_shifts_worked_allign_demographics
call python -m nurs_routines.esr_sickness_allign_demographics

pause