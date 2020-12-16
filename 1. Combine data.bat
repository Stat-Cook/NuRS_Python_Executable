@echo off

call NuRS_executable\Scripts\activate

:: Allocate
call python -m nurs_routines.allocate_acuity_combination
call python -m nurs_routines.allocate_assignment_combination

:: EST
call python -m nurs_routines.esr_leavers_annual_demographics
call python -m nurs_routines.esr_leavers_monthly_frequency
call python -m nurs_routines.esr_mandatory_training_overview_combination
call python -m nurs_routines.esr_sickness_extract

pause