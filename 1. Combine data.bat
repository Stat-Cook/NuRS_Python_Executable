@echo off

call NuRS_executable\Scripts\activate

:: Allocate
call python nurs_routines/allocate_accuity_combination.py
call python nurs_routines/allocate_assignment_combination.py

:: EST
call python nurs_routines/esr_leavers_annual_demographics.py
call python nurs_routines/esr_leavers_monthly_frequency.py
call python nurs_routines/esr_mandatory_training_overview_combination.py
call python nurs_routines/esr_sickness_extract.py

pause